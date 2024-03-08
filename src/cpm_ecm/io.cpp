#include <libmuscle/libmuscle.hpp>

#include "cell_ecm_interactions.hpp"
#include "cpm_ecm/io.hpp"
#include "ecm_boundary_state.hpp"
#include "util/muscle3/muscle3_grid.hpp"

#include <cinttypes>
#include <unordered_map>
#include <utility>

using libmuscle::Data;
using libmuscle::DataConstRef;

namespace {

Data encode_change_type_in_area(ChangeTypeInArea const &ctia, AutoMemory &mem) {
  mem.m0.resize(ctia.change_area.size() * 2u);
  for (std::size_t i = 0u; i < ctia.change_area.size(); ++i) {
    mem.m0[i * 2u] = ctia.change_area[i].x;
    mem.m0[i * 2u + 1u] = ctia.change_area[i].y;
  }

  auto change_area = Data::grid<int32_t>(
      mem.m0.data(), {ctia.change_area.size(), 2u}, {"par_id", "xy"});

  return Data::dict("change_area", change_area, "num_particles",
                    ctia.num_particles, "from_type",
                    static_cast<int>(ctia.from_type), "to_type",
                    static_cast<int>(ctia.to_type));
}

Data encode_add_adhesion_particles(AddAdhesionParticles const &aap,
                                   AutoMemory &mem) {
  mem.m1.resize(aap.new_pos.size() * 2u);
  for (std::size_t i = 0u; i < aap.new_pos.size(); ++i) {
    mem.m1[i * 2u] = aap.new_pos[i].x;
    mem.m1[i * 2u + 1u] = aap.new_pos[i].y;
  }

  auto new_pos =
      Data::grid<double>(mem.m1.data(), {aap.new_pos.size(), 2u}, {"i", "xy"});

  auto bond_attempt_radius = Data::grid<double>(
      aap.bond_attempt_radius.data(), {aap.bond_attempt_radius.size()}, {"i"});

  return Data::dict("new_pos", new_pos, "bond_attempt_radius",
                    bond_attempt_radius);
}

Data encode_move_adhesion_particles(MoveAdhesionParticles const &map,
                                    AutoMemory &mem) {
  auto par_id =
      Data::grid<int32_t>(map.par_id.data(), {map.par_id.size()}, {"i"});

  mem.m2.resize(map.new_pos.size() * 2u);
  for (std::size_t i = 0u; i < map.new_pos.size(); ++i) {
    mem.m2[i * 2u] = map.new_pos[i].x;
    mem.m2[i * 2u + 1u] = map.new_pos[i].y;
  }

  auto new_pos =
      Data::grid<double>(mem.m2.data(), {map.new_pos.size(), 2u}, {"i", "xy"});

  return Data::dict("par_id", par_id, "new_pos", new_pos);
}

std::unordered_map<ParId, Particle> decode_particles(DataConstRef const &data) {
  std::unordered_map<ParId, Particle> result;

  Muscle3Grid<int32_t> par_ids(data["par_ids"]);
  Muscle3Grid<double> positions(data["positions"]);
  Muscle3Grid<int32_t> types(data["types"]);

  for (std::size_t i = 0u; i < par_ids.shape(0u); ++i) {
    result[par_ids(i)] =
        Particle(par_ids(i), {positions(i, 0), positions(i, 1)},
                 static_cast<ParticleType>(types(i)));
  }

  return result;
}

std::unordered_map<BondTypeId, BondType>
decode_bond_types(DataConstRef const &data) {
  std::unordered_map<BondTypeId, BondType> result;

  Muscle3Grid<int32_t> bond_type_ids(data["bond_type_ids"]);
  Muscle3Grid<double> r0(data["r0"]);
  Muscle3Grid<double> k(data["k"]);

  for (std::size_t i = 0u; i < bond_type_ids.shape(0u); ++i)
    result[bond_type_ids(i)] = BondType(r0(i), k(i));

  return result;
}

std::unordered_map<BondId, Bond> decode_bonds(DataConstRef const &data) {
  std::unordered_map<BondId, Bond> result;

  Muscle3Grid<int32_t> bond_ids(data["bond_ids"]);
  Muscle3Grid<int32_t> particle_groups(data["particle_groups"]);
  Muscle3Grid<int32_t> types(data["types"]);

  for (std::size_t i = 0u; i < bond_ids.shape(0u); ++i)
    result[bond_ids(i)] = Bond(particle_groups(i, 0), particle_groups(i, 1),
                               static_cast<BondTypeId>(types(i)));

  return result;
}

std::unordered_map<AngleCstTypeId, AngleCstType>
decode_angle_cst_types(DataConstRef const &data) {
  std::unordered_map<AngleCstTypeId, AngleCstType> result;

  Muscle3Grid<int32_t> angle_cst_type_ids(data["angle_cst_type_ids"]);
  Muscle3Grid<double> t0(data["t0"]);
  Muscle3Grid<double> k(data["k"]);

  for (std::size_t i = 0u; i < angle_cst_type_ids.shape(0u); ++i)
    result[angle_cst_type_ids(i)] = AngleCstType(t0(i), k(i));

  return result;
}

std::unordered_map<AngleCstId, AngleCst>
decode_angle_csts(DataConstRef const &data) {
  std::unordered_map<AngleCstId, AngleCst> result;

  Muscle3Grid<int32_t> angle_cst_ids(data["angle_cst_ids"]);
  Muscle3Grid<int32_t> particle_groups(data["particle_groups"]);
  Muscle3Grid<int32_t> types(data["types"]);

  for (std::size_t i = 0u; i < angle_cst_ids.shape(0u); ++i)
    result[angle_cst_ids(i)] =
        AngleCst(particle_groups(i, 0), particle_groups(i, 1),
                 particle_groups(i, 2), static_cast<AngleCstTypeId>(types(i)));

  return result;
}

} // namespace

std::pair<Data, AutoMemory>
encode_cell_ecm_interactions(CellECMInteractions const &interactions) {
  AutoMemory mem;

  auto change_type_in_area =
      encode_change_type_in_area(interactions.change_type_in_area, mem);

  auto add_adhesion_particles =
      encode_add_adhesion_particles(interactions.add_adhesion_particles, mem);

  auto move_adhesion_particles =
      encode_move_adhesion_particles(interactions.move_adhesion_particles, mem);

  auto const &rap = interactions.remove_adhesion_particles;
  auto remove_adhesion_particles =
      Data::dict("par_id", Data::grid<int32_t>(rap.par_id.data(),
                                               {rap.par_id.size()}, {"i"}));

  auto result =
      Data::dict("change_type_in_area", change_type_in_area,
                 "add_adhesion_particles", add_adhesion_particles,
                 "move_adhesion_particles", move_adhesion_particles,
                 "remove_adhesion_particles", remove_adhesion_particles);

  return std::make_pair(result, mem);
}

ECMBoundaryState decode_ecm_boundary_state(DataConstRef const &data) {
  ECMBoundaryState result;
  result.particles = decode_particles(data["particles"]);
  result.bond_types = decode_bond_types(data["bond_types"]);
  result.bonds = decode_bonds(data["bonds"]);
  result.angle_cst_types = decode_angle_cst_types(data["angle_cst_types"]);
  result.angle_csts = decode_angle_csts(data["angle_csts"]);
  return result;
}
