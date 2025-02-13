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
            auto deltaR = cell_center - adh.position;
            auto deltaR_norm = std::max(std::abs(deltaR.x), std::abs(deltaR.y));
            if (deltaR_norm == 0.0)
                continue;

            auto delta_normalized = (1.0 / deltaR_norm) * deltaR;
            PixelPos delta(delta_normalized.x, delta_normalized.y);

            ParPos new_pos = adh.position + ParPos(delta.x, delta.y);
            PixelPos new_pixel =
                PixelPos(std::floor(new_pos.x), std::floor(new_pos.y));

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
        else{
            index_.remove_adhesions(target_pixel,FA_BREAKING_OPTIONS::YIELD, ca_.Time());
        }
    }
}

void AdhesionMover::remove_trailing_adhesions(){
    auto adhesion_list = index_.get_all_adhesions();

     for (auto posadh : adhesion_list)
     {
        auto pos = posadh.first;
        auto adhs = posadh.second;

        auto cell = ca_.getCell(ca_.Sigma(pos.x, pos.y));
        auto polarity = cell.Polarity();
        auto com = cell.CenterVector();
//
        if (polarity.x == 0 && polarity.y == 0)
            continue;

        // auto cosa = cell.PolarityAngle(); 
        // auto prob = 1.0 - exp(
        //     par.polariy_history * (cosa - 1.0)
        // );
        // if (RANDOM() < prob)
        if (polarity.dot(Vec2<double>(pos.x, pos.y) - com) < 0)
             for (auto adh : adhs) {
                // std::cout << "  Removing at " << adh.position << '\n';
                 index_.remove_adhesion(adh,FA_BREAKING_OPTIONS::TRAILING, ca_.Time());
             }
        else {
            if (par.only_tipcell_adh && cell.getTau() == 2) {
                 for (auto adh : adhs) {
                     index_.remove_adhesion(adh, FA_BREAKING_OPTIONS::TRAILING, ca_.Time() );
                 }

            }
        }
     }
}

void AdhesionMover::remove_broken_adhesions()
{
    auto adhesion_list = index_.get_all_adhesions();

    for (auto posadh : adhesion_list)
    {
        auto adhs = posadh.second;
        for (auto adh : adhs)
        {
            if (adh.size <= par.adhesion_integrin_N0)
            {
                index_.remove_adhesion(adh,FA_BREAKING_OPTIONS::BROKEN, ca_.Time());
            }
        }
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
    index_.rebuild(ecm_boundary, ca_.Time());
    std::vector<ParPos> midpoints;

    for (auto const &cell : *ca_.getCellArray())
    {
        midpoints.push_back(cell.CenterVector());
    }
    index_.setting_force_on_adhesions(midpoints, ca_.getSigma());
    const ACT::ActField &act_field = ca_.getActField();
    index_.setting_size_on_adhesions(act_field, ca_.getSigma());
}

void AdhesionMover::update_myosin(std::unordered_map<PixelPos,double> myosin_factor)
{
    index_.set_myosin(myosin_factor);
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
    double fraction(1.0 * resisting /
                    (1.0 * (par.adhesion_yielding_Nh + resisting)));
    return fraction * par.adhesion_yielding_lambda ;
}
