#include "parameter.hpp"
extern Parameter par;
#include "adhesion_index.hpp"
#include "novikova_storm.hpp"
#include "sqr.hpp"
#include "act.hpp"

AttachedBond::AttachedBond(
    ParPos const& neighbour, BondType const& bond_type)
    : neighbour(neighbour), bond_type(bond_type) {}

double AttachedBond::move_dh(ParPos from, ParPos to) const {
    auto a_from = (from - neighbour).length();
    auto a_to = (to - neighbour).length();
    auto H_from = bond_type.k * 0.5 * sqr(a_from - bond_type.r0);
    auto H_to = bond_type.k * 0.5 * sqr(a_to - bond_type.r0);
    return H_to - H_from;
}

AttachedAngleCst::AttachedAngleCst(
    ParPos const& middle, ParPos const& far,
    AngleCstType const& angle_cst_type)
    : middle(middle), far(far), angle_cst_type(angle_cst_type) {}

double AttachedAngleCst::move_dh(ParPos from, ParPos to) const {
    auto x_from = from - middle;
    auto x_to = to - middle;
    auto y = far - middle;

    auto cos_theta_from = x_from.dot(y) / (x_from.length() * y.length());
    if (cos_theta_from < -1.0) cos_theta_from = -1.0;
    if (cos_theta_from > 1.0) cos_theta_from = 1.0;

    auto cos_theta_to = x_to.dot(y) / (x_to.length() * y.length());
    if (cos_theta_to < -1.0) cos_theta_to = -1.0;
    if (cos_theta_to > 1.0) cos_theta_to = 1.0;

    auto theta_from = acos(cos_theta_from);
    auto theta_to = acos(cos_theta_to);

    auto H_from = angle_cst_type.k * 0.5 * sqr((theta_from - angle_cst_type.t0));
    auto H_to = angle_cst_type.k * 0.5 * sqr((theta_to - angle_cst_type.t0));

    return H_to - H_from;
}

AdhesionWithEnvironment::AdhesionWithEnvironment(
    ParId par_id, ParPos const& position, Integrin size, double myosin_force_fraction)
    : par_id(par_id), position(position), size(size), myosin_force_fraction(myosin_force_fraction) {}

double AdhesionWithEnvironment::move_dh(PixelDisplacement move) const {
    double dh = 0.0;

    auto from = position;
    auto to = position + ParDisplacement(move);

    for (auto const& bond : bonds)
        dh += bond.move_dh(from, to);

    for (auto const& angle_cst : angle_csts)
        dh += angle_cst.move_dh(from, to);

    return dh;
}

namespace {
// Helper functions for rebuild(), only visible within this file because of
// the anonymous namespace.

// Map adhesion particles to bonds attached to them
std::unordered_map<ParId, std::vector<BondId>> make_bond_index(
    ECMBoundaryState const& ecm_boundary) {
    std::unordered_map<ParId, std::vector<BondId>> bond_index;
    for (auto const& id_bond : ecm_boundary.bonds) {
        BondId bid = id_bond.first;
        Bond const& bond = id_bond.second;

        ParticleType p1_type = ecm_boundary.particles.at(bond.p1).type;
        bool p1_adh = p1_type == ParticleType::adhesion;
        bool p1_unfit = (p1_type == ParticleType::excluded); //|| p1_adh;

        ParticleType p2_type = ecm_boundary.particles.at(bond.p2).type;
        bool p2_adh = p2_type == ParticleType::adhesion;
        bool p2_unfit = (p2_type == ParticleType::excluded); // || p2_adh;

        if (p1_adh && !p2_unfit)
            bond_index[bond.p1].push_back(bid);

        if (p2_adh && !p1_unfit)
            bond_index[bond.p2].push_back(bid);
    }
    return bond_index;
}

// Map adhesion particles to angle constraints attached to them
std::unordered_map<ParId, std::vector<AngleCstId>> make_angle_cst_index(
    ECMBoundaryState const& ecm_boundary) {
    std::unordered_map<ParId, std::vector<AngleCstId>> angle_cst_index;
    for (auto const& id_angle_cst : ecm_boundary.angle_csts) {
        AngleCstId aid = id_angle_cst.first;
        AngleCst const& angle_cst = id_angle_cst.second;

        ParticleType p1_type = ecm_boundary.particles.at(angle_cst.p1).type;
        bool p1_adh = p1_type == ParticleType::adhesion;
        bool p1_unfit = p1_adh; // || (p1_type == ParticleType::excluded);

        ParticleType p3_type = ecm_boundary.particles.at(angle_cst.p3).type;
        bool p3_adh = p3_type == ParticleType::adhesion;
        bool p3_unfit = p3_adh; //|| (p3_type == ParticleType::excluded);

        if (p1_adh && !p3_unfit)
            angle_cst_index[angle_cst.p1].push_back(aid);

        if (p3_adh && !p1_unfit)
            angle_cst_index[angle_cst.p3].push_back(aid);
    }
    return angle_cst_index;
}
}  // namespace

void AdhesionIndex::rebuild(ECMBoundaryState const& ecm_boundary) {
    // Adhesion particles' positions are sent along by the other side,
    // but the adhesion particles are part of our state, so they don't
    // get to say where they are, we decided that. Unless they have
    // created new adhesion particles for us and picked the location,
    // which is weird but can happen with the original adhesion
    // generation algorithm. So we save our existing adhesion
    // particles' positions here, and keep them, only using the sent
    // positions for adhesions particles we didn't have yet.
    std::unordered_map<ParId, ParPos> adh_par_pos;
    std::unordered_map<ParId, double> adh_par_size;
    std::unordered_map<ParId, double> adh_par_myosin;
    for (auto const& pixel_awes : adhesions_by_pixel_)
        for (auto const& awe : pixel_awes.second) {
            adh_par_pos[awe.par_id] = awe.position;
            adh_par_size[awe.par_id] = awe.size;
            adh_par_myosin[awe.par_id] = awe.myosin_force_fraction;
        }

    auto bonds_for = make_bond_index(ecm_boundary);
    auto angle_csts_for = make_angle_cst_index(ecm_boundary);

    adhesions_by_pixel_.clear();
    for (auto const id_par : ecm_boundary.particles) {
        ParId pid = id_par.first;
        Particle const& particle = id_par.second;

        if (particle.type == ParticleType::adhesion) {
            double myosin = adh_par_myosin.count(pid) ? adh_par_myosin[pid] : 0.1;
            double size = adh_par_size.count(pid) ? adh_par_size[pid] : par.adhesion_integrin_N0;
            ParPos pos = adh_par_pos.count(pid) ? adh_par_pos[pid] : particle.pos;
            PixelPos containing_pixel(floor(pos.x), floor(pos.y));
            adhesions_by_pixel_[containing_pixel].emplace_back(pid, pos);
            auto& awe = adhesions_by_pixel_[containing_pixel].back();
            awe.size = size;
            awe.myosin_force_fraction = myosin;

            for (BondId bid : bonds_for[pid]) {
                auto const& bond = ecm_boundary.bonds.at(bid);

                ParPos neighbor_pos;
                if (bond.p1 == pid)
                    neighbor_pos = ecm_boundary.particles.at(bond.p2).pos;
                else
                    neighbor_pos = ecm_boundary.particles.at(bond.p1).pos;

                awe.bonds.emplace_back(
                    neighbor_pos, ecm_boundary.bond_types.at(bond.type));
            }

            for (AngleCstId aid : angle_csts_for[pid]) {
                auto const& angle_cst = ecm_boundary.angle_csts.at(aid);

                ParPos middle_pos = ecm_boundary.particles.at(angle_cst.p2).pos;

                ParPos far_pos;
                if (angle_cst.p1 == pid)
                    far_pos = ecm_boundary.particles.at(angle_cst.p3).pos;
                else
                    far_pos = ecm_boundary.particles.at(angle_cst.p1).pos;

                awe.angle_csts.emplace_back(
                    middle_pos, far_pos,
                    ecm_boundary.angle_cst_types.at(angle_cst.type));
            }
        }
    }
}

namespace {
   double myosin_derivate(double act_percentage, double myosin) {
        return par.myosin_creation_rate * ( 1.0 - myosin) - par.myosin_decay_rate * act_percentage * (myosin - 0.1); 
   } 
   double myosin_FE(double act_percentage, double myosin) {
        double T = 0;
        while (T < par.myosin_intergration_time) {
            auto dm = myosin_derivate(act_percentage, myosin) * par.myosin_intergration_timestep;
            myosin += dm;
            T += par.myosin_intergration_timestep;            
        } 
        return myosin;
   }
}

void AdhesionIndex::set_myosin(const ACT::ActField act_field) {
    for (auto & pos_adhesions : adhesions_by_pixel_) {
        auto pos = pos_adhesions.first;
        auto act_percentage = act_field.Value(pos) / par.max_Act;
        for (auto & awe : pos_adhesions.second) {
            auto myosin = myosin_FE(
                act_percentage,
                awe.myosin_force_fraction
            );
            awe.myosin_force_fraction = myosin;
        }
    }
}

void AdhesionIndex::setting_force_on_adhesions(std::vector<ParPos> midpoints, int** sigma) {
    for (auto& pos_adhesions : adhesions_by_pixel_) {
        for (auto& awe : pos_adhesions.second) {
            Force force(0.0, 0.0);
            auto spin = sigma[pos_adhesions.first.x][pos_adhesions.first.y];
            auto center = midpoints[spin];
            auto delta  = center - awe.position;
            delta = (1.0 / delta.length()) * delta;

            auto new_pos = awe.position + delta;

            for (auto const& bond : awe.bonds) {
                force += getLinearHarmonicForceOnB(
                    bond.neighbour,
                    new_pos,
                    bond.bond_type.k,
                    bond.bond_type.r0);
            }
            for (auto const& acst : awe.angle_csts) {
                force += getAngularHarmonicForceOnA(
                    new_pos,
                    acst.middle,
                    acst.far,
                    acst.angle_cst_type.k,
                    acst.angle_cst_type.t0);
            }
            awe.tension = std::sqrt(force.dot(force));
//            awe.tension = std::sqrt(force.dot(force)) + 
//                          par.adhesion_contraction_force * (
//                              midpoints[spin] + (-1.0)*awe.position
//                          ).length();
        }
    }
}

void AdhesionIndex::setting_size_on_adhesions() {
    NS::Parameter nspar(
        par.ns_Nt,
        par.ns_phi_s,
        par.ns_phi_c,
        par.ns_d0,
        par.ns_gamma,
        par.ns_dt,
        par.ns_T,
        par.adhesion_integrin_N0,
        par.ns_f_star);
    for (auto& pos_adhesions : adhesions_by_pixel_) {
        for (auto& awe : pos_adhesions.second) {
            awe.size = NS::integrate(awe.tension, awe.size, nspar);
        }
    }
}

std::vector<AdhesionWithEnvironment> const& AdhesionIndex::get_adhesions(
    PixelPos pixel) const {
    auto it = adhesions_by_pixel_.find(pixel);
    if (it != adhesions_by_pixel_.end())
        return it->second;
    return no_adhesions_;
}

void AdhesionIndex::move_adhesions(PixelPos from, PixelPos to) {
    if (from == to) return;
    auto it = adhesions_by_pixel_.find(from);
    if (it != adhesions_by_pixel_.end()) {
        for (auto& awe : it->second) {
            awe.position += to - from;
            ecm_interaction_tracker_.record_move_particle(awe.par_id, awe.position);
            adhesions_by_pixel_[to].push_back(awe);
        }
        it->second.clear();
    }
}

void AdhesionIndex::move_adhesion(ParId who, PixelPos from, ParPos to) {
    auto it = adhesions_by_pixel_.find(from);
    if (it != adhesions_by_pixel_.end()) {
        PixelPos to_as_pixel(floor(to.x), floor(to.y));
        for (auto& adh : it->second) {
            if (adh.par_id == who) {
                adh.position += to_as_pixel - from;
                ecm_interaction_tracker_.record_move_particle(adh.par_id, adh.position);
                adhesions_by_pixel_[to_as_pixel].push_back(adh);
            }
        }
    }
}

void AdhesionIndex::remove_adhesion(ParId particle) {
    ecm_interaction_tracker_.record_remove_particle(particle);
}
void AdhesionIndex::remove_adhesions(PixelPos pixel) {
    auto it = adhesions_by_pixel_.find(pixel);
    if (it != adhesions_by_pixel_.end()) {
        for (auto& awe : it->second)
            ecm_interaction_tracker_.record_remove_particle(awe.par_id);
        it->second.clear();
    }
}

CellECMInteractions AdhesionIndex::get_cell_ecm_interactions() const {
    return ecm_interaction_tracker_.get_changes();
}

void AdhesionIndex::reset_cell_ecm_interactions() {
    ecm_interaction_tracker_.reset();
}

std::vector<AdhesionWithEnvironment> AdhesionIndex::no_adhesions_;

const std::unordered_map<
    PixelPos, std::vector<AdhesionWithEnvironment>>
AdhesionIndex::get_all_adhesions() const {
    return adhesions_by_pixel_;
}
