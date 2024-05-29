#include "adhesion_mover.hpp"

#include <algorithm>

#include "adhesion_movement.hpp"

AdhesionDisplacements::AdhesionDisplacements() : source({0, 0}), target({0, 0})
{
}

AdhesionDisplacements::AdhesionDisplacements(PixelDisplacement source,
                                             PixelDisplacement target)
    : source(source), target(target)
{
}

const PixelDisplacement
    AdhesionDisplacements::annihilated(std::numeric_limits<int>::min(),
                                       std::numeric_limits<int>::min());

AdhesionMover::AdhesionMover(CellularPotts const &ca) : ca_(ca) {}
#include "random.hpp"
void AdhesionMover::ContractAdhesionInCells(double cell_force)
{
    auto adhesion_list = index_.get_all_adhesions();

    for (auto posadh : adhesion_list)
    {
        auto pos = posadh.first;
        auto adhs = posadh.second;

        auto spin = ca_.Sigma(pos.x, pos.y);
        ParPos cell_center = {ca_.getCell(spin).getCenterX(),
                              ca_.getCell(spin).getCenterY()};

        for (auto const &adh : adhs)
        {
//            std::vector<PixelPos> direction =  {
//                PixelPos(-1,-1), PixelPos(-1, 0), PixelPos(-1, 1),
//                PixelPos( 0, 1), PixelPos( 0,-1), PixelPos( 1,-1), PixelPos( 1, 0), PixelPos( 1, 1)};
//            std::shuffle(direction.begin(), direction.end(), std::default_random_engine(RANDOM())); 
            auto deltaR = cell_center - adh.position;
            //for (auto const delta : direction) {
                // Use the infinty norm because we want to map the vector
                // to the moore neighbourhood and moore neighbourhood = circle in
                // (R^2, |.|_\infty).
                auto deltaR_norm = std::max(std::abs(deltaR.x), std::abs(deltaR.y));
                if ((deltaR_norm == 0.0) 
//				||
//                    (deltaR.dot(deltaR) <
//                     par.adhesion_maximum_contractile_percentage *
//                         par.adhesion_maximum_contractile_percentage *
//                         par.target_area / 3.14)
                         )
                {
                    continue;
                }
                auto delta_normalized = (1.0 / deltaR_norm) * deltaR;
		PixelPos delta(delta_normalized.x,delta_normalized.y);

                ParPos new_pos = adh.position + ParPos(delta.x, delta.y);
                PixelPos new_pixel = PixelPos(std::floor(new_pos.x), std::floor(new_pos.y));

                if (ca_.Sigma(new_pixel.x, new_pixel.y) == spin)
                {
                    // Here should be a check on the tension
                    auto new_deltaR = cell_center - new_pos;

                    double delta_energy_ecm = adh.move_dh(delta);
                    double delta_energy_cyto =
                        cell_force * adh.myosin_force_fraction * 0.5 *
                        (new_deltaR.dot(new_deltaR) - deltaR.dot(deltaR));
                    double delta_energy = delta_energy_ecm + delta_energy_cyto;
                    if (delta_energy < 0)
                    {
                        index_.move_adhesion(adh.par_id, pos, new_pos);
                        // break;
                    }
                }
            //}
        }
    }
}

double AdhesionMover::move_dh(PixelPos source_pixel, PixelPos target_pixel,
                              AdhesionDisplacements &displacements) const
{
    double source_dh(0.0), target_dh(0.0);

    auto num_source_adhesions = index_.get_adhesions(source_pixel).size();
    if (num_source_adhesions > 0)
    {
        auto possible_displacements =
            extension_displacements(ca_, source_pixel, target_pixel);
        std::tie(displacements.source, source_dh) =
            select_displacement(index_, source_pixel, possible_displacements);
    }

    auto adhesions_at_pixel = index_.get_adhesions(target_pixel);
    auto num_target_adhesions = adhesions_at_pixel.size();
    if (num_target_adhesions > 0)
    {
        if (par.adhesion_yielding)
        {
            target_dh = compute_yielding_penalty(adhesions_at_pixel);
            displacements.target = AdhesionDisplacements::annihilated;
        }
        else
        {
            auto possible_displacements =
                retraction_displacements(ca_, source_pixel, target_pixel);
            if (possible_displacements.empty())
            {
                displacements.target = AdhesionDisplacements::annihilated;
                target_dh = annihilation_penalty(num_target_adhesions);
            }
            else
            {
                std::tie(displacements.target, target_dh) = select_displacement(
                    index_, target_pixel, possible_displacements);
            }
        }
    }

    return source_dh + target_dh;
}

void AdhesionMover::commit_move(PixelPos source_pixel, PixelPos target_pixel,
                                AdhesionDisplacements const &displacements)
{
    // Source pixel
    if (displacements.source != PixelDisplacement(0, 0))
        index_.move_adhesions(source_pixel,
                              source_pixel + displacements.source);

    // Target pixel
    if (displacements.target != PixelDisplacement(0, 0))
    {
        if (displacements.target != AdhesionDisplacements::annihilated)
        {
            index_.move_adhesions(target_pixel,
                                  target_pixel + displacements.target);
        }
        else
            index_.remove_adhesions(target_pixel);
    }
}

CellECMInteractions AdhesionMover::get_cell_ecm_interactions() const
{
    return index_.get_cell_ecm_interactions();
}

void AdhesionMover::reset_cell_ecm_interactions()
{
    index_.reset_cell_ecm_interactions();
}

void AdhesionMover::update(ECMBoundaryState const &ecm_boundary)
{
    index_.rebuild(ecm_boundary);
    std::vector<ParPos> midpoints;

    for (auto const &cell : *ca_.getCellArray()) {
        midpoints.push_back(cell.CenterVector());
    }
    index_.setting_force_on_adhesions(midpoints, ca_.getSigma());
    index_.setting_size_on_adhesions();
}

void AdhesionMover::update_myosin(const ACT::ActField act_field){
    index_.set_myosin(act_field);
}

double
compute_yielding_penalty(const std::vector<AdhesionWithEnvironment> adhesions)
{
    Integrin total(0);
    for (auto const &adh : adhesions)
    {
        total += adh.size - par.adhesion_integrin_N0;
    }

    Integrin resisting = std::max(0, total);
    // The 1.0 (with .0) makes the division a division of doubles instead of
    // division of ints.
    double fraction(1.0 * resisting / (1.0*(par.adhesion_yielding_Nh + resisting)));
    return fraction * par.adhesion_yielding_lambda;
}
