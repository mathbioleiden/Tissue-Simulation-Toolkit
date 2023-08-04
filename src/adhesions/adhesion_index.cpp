#include "adhesion_index.hpp"

#include "sqr.hpp"

AttachedBond::AttachedBond(
        ParPos const & neighbour, BondType const & bond_type)
    : neighbour(neighbour)
    , bond_type(bond_type)
{}


double AttachedBond::move_dh(ParPos from, ParPos to) const {
    auto a_from = (from - neighbour).length();
    auto a_to = (to - neighbour).length();
    auto H_from = bond_type.k * 0.5 * sqr(a_from - bond_type.r0);
    auto H_to = bond_type.k * 0.5 * sqr(a_to - bond_type.r0);
    return H_to - H_from;
}


AttachedAngleCst::AttachedAngleCst(
        ParPos const & middle, ParPos const & far,
        AngleCstType const & angle_cst_type)
    : middle(middle)
    , far(far)
    , angle_cst_type(angle_cst_type)
{}

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
        ParId par_id, ParPos const & position)
    : par_id(par_id)
    , position(position)
{}


double AdhesionWithEnvironment::move_dh(PixelDisplacement move) const {
    double dh = 0.0;

    auto from = position;
    auto to = position + ParDisplacement(move);

    for (auto const & bond : bonds)
        dh += bond.move_dh(from, to);

    for (auto const & angle_cst : angle_csts)
        dh += angle_cst.move_dh(from, to);

    return dh;
}


AdhesionIndex::AdhesionIndex(ExtraCellularMatrix const & ecm) {
    rebuild(ecm);
}


namespace {
    // Helper functions for rebuild(), only visible within this file because of
    // the anonymous namespace.

    // Map adhesion particles to bonds attached to them
    std::unordered_map<ParId, std::vector<BondId>> make_bond_index(
            ExtraCellularMatrix const & ecm)
    {
        std::unordered_map<ParId, std::vector<BondId>> bond_index;
        for (BondId bid = 0; bid < ecm.bonds.size(); ++bid) {
            Bond const & bond = ecm.bonds[bid];

            ParticleType p1_type = ecm.particles[bond.p1].type;
            bool p1_adh = p1_type == ParticleType::adhesion;
            bool p1_unfit = p1_adh || (p1_type == ParticleType::excluded);

            ParticleType p2_type = ecm.particles[bond.p2].type;
            bool p2_adh = p2_type == ParticleType::adhesion;
            bool p2_unfit = p2_adh || (p2_type == ParticleType::excluded);

            if (p1_adh && !p2_unfit)
                bond_index[bond.p1].push_back(bid);

            if (p2_adh && !p1_unfit)
                bond_index[bond.p2].push_back(bid);
        }
        return bond_index;
    }

    // Map adhesion particles to angle constraints attached to them
    std::unordered_map<ParId, std::vector<AngleCstId>> make_angle_cst_index(
            ExtraCellularMatrix const & ecm)
    {
        std::unordered_map<ParId, std::vector<AngleCstId>> angle_cst_index;
        for (AngleCstId aid = 0; aid < ecm.angle_csts.size(); ++aid) {
            AngleCst const & angle_cst = ecm.angle_csts[aid];

            ParticleType p1_type = ecm.particles[angle_cst.p1].type;
            bool p1_adh = p1_type == ParticleType::adhesion;
            bool p1_unfit = p1_adh || (p1_type == ParticleType::excluded);

            ParticleType p3_type = ecm.particles[angle_cst.p3].type;
            bool p3_adh = p3_type == ParticleType::adhesion;
            bool p3_unfit = p3_adh || (p3_type == ParticleType::excluded);

            if (p1_adh && !p3_unfit)
                angle_cst_index[angle_cst.p1].push_back(aid);

            if (p3_adh && !p1_unfit)
                angle_cst_index[angle_cst.p3].push_back(aid);
        }
        return angle_cst_index;
    }
}


void AdhesionIndex::rebuild(ExtraCellularMatrix const & ecm) {
    auto bonds_for = make_bond_index(ecm);
    auto angle_csts_for = make_angle_cst_index(ecm);

    adhesions_by_pixel_.clear();
    for (ParId pid = 0; pid < ecm.particles.size(); ++pid) {
        if (ecm.particles[pid].type == ParticleType::adhesion) {
            auto const & pos = ecm.particles[pid].pos;
            PixelPos containing_pixel(floor(pos.x), floor(pos.y));
            adhesions_by_pixel_[containing_pixel].emplace_back(pid, pos);
            auto & awe = adhesions_by_pixel_[containing_pixel].back();

            for (BondId bid: bonds_for[pid]) {
                auto const & bond = ecm.bonds[bid];

                ParPos neighbor_pos;
                if (bond.p1 == pid)
                    neighbor_pos = ecm.particles[bond.p2].pos;
                else
                    neighbor_pos = ecm.particles[bond.p1].pos;

                awe.bonds.emplace_back(neighbor_pos, ecm.bond_types[bond.type]);
            }

            for (AngleCstId aid: angle_csts_for[pid]) {
                auto const & angle_cst = ecm.angle_csts[aid];

                ParPos middle_pos = ecm.particles[angle_cst.p2].pos;

                ParPos far_pos;
                if (angle_cst.p1 == pid)
                    far_pos = ecm.particles[angle_cst.p3].pos;
                else
                    far_pos = ecm.particles[angle_cst.p1].pos;

                awe.angle_csts.emplace_back(
                        middle_pos, far_pos, ecm.angle_cst_types[angle_cst.type]);
            }
        }
    }
}

std::vector<AdhesionWithEnvironment> const & AdhesionIndex::get_adhesions(
                PixelPos pixel) const
{
    auto it = adhesions_by_pixel_.find(pixel);
    if (it != adhesions_by_pixel_.end())
        return it->second;
    return no_adhesions_;
}

void AdhesionIndex::move_adhesions(PixelPos from, PixelPos to) {
    if (from == to) return;
    auto it = adhesions_by_pixel_.find(from);
    if (it != adhesions_by_pixel_.end()) {
        for (auto & awe: it->second) {
            awe.position += to - from;
            adhesions_by_pixel_[to].push_back(awe);
        }
        it->second.clear();
    }
}

void AdhesionIndex::remove_adhesions(PixelPos pixel) {
    auto it = adhesions_by_pixel_.find(pixel);
    if (it != adhesions_by_pixel_.end())
        it->second.clear();
}

std::vector<AdhesionWithEnvironment> AdhesionIndex::no_adhesions_;

