#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <ctime>
#include <string>
#include <locale.h>

#include "MultiCellDS.hpp"
#include "MultiCellDS-pimpl.hpp"
#include "MultiCellDS-simpl.hpp"
#include "mcds_io.h" 
#include "lattice_util.h"

MCDS_io::MCDS_io(){
	setlocale(LC_NUMERIC, "C");
	multicellds = new MultiCellDS;
}

MCDS_io::MCDS_io(std::string filename, double unit_ratio, std::string unit_name){
	setlocale(LC_NUMERIC, "C");
	unit_r = unit_ratio;
	unit_n = unit_name;
	read(filename);
}

void MCDS_io::read(std::string filename){
	MultiCellDS_paggr MultiCellDS_p;
	xml_schema::document_pimpl doc_p (MultiCellDS_p.root_parser (),
					  MultiCellDS_p.root_name ());
	MultiCellDS_p.pre ();
	doc_p.parse(filename);
	multicellds = MultiCellDS_p.post();
}

void MCDS_io::add_metadata(std::string filename){
	MultiCellDS_paggr MultiCellDS_p;
	xml_schema::document_pimpl doc_p (MultiCellDS_p.root_parser (),
					  MultiCellDS_p.root_name ());
	MultiCellDS_p.pre ();
	doc_p.parse(filename);
	MultiCellDS* h_meta = MultiCellDS_p.post ();
	multicellds->metadata(&h_meta->metadata());
}

io_cell * MCDS_io::get_new_cell(int id){
	if (cells.find(id) == cells.end())
		cells[id] = io_cell();
	return &cells[id];
}

io_face * MCDS_io::get_new_face(int id){
	if (faces.find(id) == faces.end())
		faces[id] = io_face();
	return &faces[id];
}

io_edge * MCDS_io::get_new_edge(int id){
	if (edges.find(id) == edges.end())
		edges[id] = io_edge();
	return &edges[id];
}

io_node * MCDS_io::get_new_node(int id){
	if (nodes.find(id) == nodes.end())
		nodes[id] = io_node();
	return &nodes[id];
}

mesh::nodes_edges_faces* MCDS_io::finalize_shape(io_cell& cell){
	mesh::nodes_edges_faces * shape_ds = new mesh::nodes_edges_faces; 
	mesh::faces* faces_ds = new mesh::faces;
	mesh::edges* edges_ds = new mesh::edges;
	mesh::nodes* nodes_ds = new mesh::nodes;
//////BUG IN MCDS forces placing a string in nodes->custom////
//	std::string * test_nds = new std::string("-");
//	common::custom * custom_node = new common::custom;
//	custom_node->custom_data().push_back((void *) (test_nds));
//	nodes_ds->custom(custom_node);
////////////////////////////////////////////////////////////// 
	shape_ds->faces(faces_ds);
	shape_ds->nodes(nodes_ds);
	shape_ds->edges(edges_ds);
	for(int cell_node_id : cell.node_ids ){
		nodes_ds->node().push_back(finalize_node(cell_node_id));
	}
	for(int cell_edge_id : cell.edge_ids ){
		edges_ds->edge().push_back(finalize_edge(cell_edge_id));
	}
	for(int face_id : cell.face_ids ){
		faces_ds->face().push_back(finalize_face(face_id));
	}
	return shape_ds;
}

cell::cell* MCDS_io::finalize_cell(int id){
	io_cell cell = cells[id];
	cell::cell * cell_ds = new cell::cell;
	cell_ds->ID(id);
	
	state::state * state = new state::state;
	cell_ds->state(state);
	state->shape(finalize_shape(cell));
	
	phenotype_dataset::phenotype_dataset* p_set = new phenotype_dataset::phenotype_dataset();
	cell_ds->phenotype_dataset(p_set);
	phenotype::phenotype* phenotype_ds = new phenotype::phenotype;
	phenotype_ds->type(phenotype_base::phenotype_type::current);
	
	p_set->ID(cell.type); 
	
	phenotype_common::geometrical_properties* gp = new phenotype_common::geometrical_properties;
	phenotype_common::volumes* volumes = new phenotype_common::volumes; 
	common::units_decimal_nonnegative* current_volume = new common::units_decimal_nonnegative;
	current_volume->units(unit_n + " squared");
	current_volume->base_value(cell.area);
	volumes->total_volume(current_volume);
	gp->volumes(volumes);
	
	phenotype::phenotype* phenotype_target_ds = new phenotype::phenotype;
	phenotype_common::geometrical_properties* gp_target = new phenotype_common::geometrical_properties;
	phenotype_target_ds->type(phenotype_base::phenotype_type::target);
	phenotype_common::volumes* volumes_target = new phenotype_common::volumes;
	common::units_decimal_nonnegative* target_volume = new common::units_decimal_nonnegative;
	target_volume->units(unit_n + " squared");
	target_volume->base_value(cell.target_area);
	volumes_target->total_volume(target_volume);
	gp_target->volumes(volumes);
	phenotype_target_ds->geometrical_properties(gp_target);
	
	phenotype_common::lengths * lengths = new phenotype_common::lengths();
	common::units_decimal_nonnegative * ma_ax = new common::units_decimal_nonnegative;
	common::units_decimal_nonnegative * mi_ax = new common::units_decimal_nonnegative;
	ma_ax->base_value(cell.major_axis);
	mi_ax->base_value(cell.minor_axis);
	ma_ax->units(unit_n);
	mi_ax->units(unit_n); 
	lengths->major_axis(ma_ax);
	lengths->minor_axis(mi_ax);
	gp->lengths(lengths);
	
	phenotype_ds->geometrical_properties(gp);
	p_set->phenotype().push_back(phenotype_ds);
	p_set->phenotype().push_back(phenotype_target_ds);
	return cell_ds; 
}

mesh::face* MCDS_io::finalize_face(int id){
	io_face face = faces[id];
	mesh::face * face_ds = new mesh::face;
	face_ds->ID(id);
	for (int edge_id : face.edge_ids){
		face_ds->edge_ID().push_back(edge_id);	
	}
	return face_ds;
}

mesh::edge* MCDS_io::finalize_edge(int id){
	mesh::edge * edge_ds = new mesh::edge;
	edge_ds->ID(id);
	edge_ds->node_ID().push_back(edges[id].node_ids[0]);
	edge_ds->node_ID().push_back(edges[id].node_ids[1]);
	return edge_ds;
}

mesh::node * MCDS_io::finalize_node(int id){
	io_node node = nodes[id];
	mesh::node * node_ds = new mesh::node;
	node_ds->ID(id);
	common::units_double_list * node_position = new common::units_double_list;
	node_position->push_back(node.x);
	node_position->push_back(node.y);
	node_ds->position(node_position);
	return node_ds;
}

int MCDS_io::get_new_edge_uniq(int node1, int node2){
	std::string key;
	int id;
	if (node1 > node2) key = std::to_string(node2) + std::to_string(node1);
	else key = std::to_string(node1) + std::to_string(node2);
	if (edge_by_nodes.find(key) == edge_by_nodes.end()){
		id = edges.size();
		edge_by_nodes[key] = id;
		edges[id] = io_edge();
		edges[id].node_ids.push_back(node1);
		edges[id].node_ids.push_back(node2);
	}
	else id = edge_by_nodes[key];
	return id;
}

void MCDS_io::finalize_cellshapes(){
	cell::cell_population_individual * cell_population_individual = new cell::cell_population_individual;
	cell::cellular_information * cellular_information = new  cell::cellular_information;
	multicellds->cellular_information(cellular_information);
	cell::cell_populations * cell_populations = new cell::cell_populations;
	cellular_information->cell_populations(cell_populations);
	cell_populations->cell_population(cell_population_individual); 
	for(auto cell_it : cells){
		int cell_id = cell_it.first;
		cell_population_individual->cell().push_back(finalize_cell(cell_id));
	}
}

void MCDS_io::add_time(){
	std::time_t t = std::time(NULL);
	struct tm lt = *std::localtime(&t);
	time_t offset_second(lt.tm_gmtoff);
	tm off_t = *std::gmtime(&offset_second);
	short timezone_hour = (off_t.tm_hour+12)%24-12, timezone_minute = off_t.tm_min;
	xml_schema::date_time new_times(lt.tm_year+1900, lt.tm_mon, lt.tm_mday, lt.tm_hour, 
			lt.tm_min, lt.tm_sec, timezone_hour, timezone_minute);
	multicellds->metadata().created(new_times);
	multicellds->metadata().last_modified(new_times);
}

void MCDS_io::write(std::string filename){
	MultiCellDS_saggr MultiCellDS_s;
	xml_schema::document_simpl doc_s (MultiCellDS_s.root_serializer (),
			MultiCellDS_s.root_name ());
	MultiCellDS_s.pre (*multicellds);
	std::ofstream ofs(filename);
	doc_s.serialize (ofs, xml_schema::document_simpl::pretty_print);
	ofs << std::endl;
	MultiCellDS_s.post (); 
}

void MCDS_io::process_edges(cell::cell* cell_ds){
	for (mesh::edges::edge_iterator edge_ds = cell_ds->state().shape().edges().edge().begin(); 
			edge_ds != cell_ds->state().shape().edges().edge().end(); edge_ds ++){
		if(edges.find(edge_ds->ID()) == edges.end()){
			io_edge * edge = new io_edge;
			int edge_id = edge_ds->ID();
			edges[edge_id] = * edge;
			edge->cell_ids.push_back(cell_ds->ID());
			cells[cell_ds->ID()].edge_ids.push_back(edge_id);
			for (int edge_node_index = 0; edge_node_index < 2; edge_node_index ++){
				int edge_node_id = edge_ds->node_ID()[edge_node_index];
				edge->node_ids.push_back(edge_node_id);
				io_node * edge_node = &nodes[edge_node_id];
				edge_node->edge_ids.push_back(edge_id);
				highlow_xy(&edge->lowest_x, &edge->highest_x, &edge->lowest_y, &edge->highest_y, 
						edge_node->x, edge_node->y, edge_node_index == 0);
			}   
			edges[edge_id] = *edge;
		} 
	}
}

void MCDS_io::process_nodes(cell::cell* cell_ds){
	for (mesh::nodes::node_iterator node_ds = cell_ds->state().shape().nodes().node().begin();
	     node_ds != cell_ds->state().shape().nodes().node().end(); node_ds ++){
		if(nodes.find(node_ds->ID()) == nodes.end()){
			io_node * node = new io_node;
			int node_id = node_ds->ID();
			node->mcds_obj = &(*node_ds); 
			node->cell_ids.push_back(cell_ds->ID());
			node->x = node_ds->position()[0];
			node->y = node_ds->position()[1];
			cells[cell_ds->ID()].node_ids.push_back(node_id);
			highlow_xy(&lowest_x, &highest_x, &lowest_y, &highest_y, 
					node->x, node->y, 
					node_ds == cell_ds->state().shape().nodes().node().begin() && 
					cell_ds->ID() == 
					multicellds->cellular_information().cell_populations().
					cell_population().cell().begin()->ID());
			nodes[node_id] = *node;
		}
	}
}

void MCDS_io::process_faces(cell::cell* cell_ds){
	for (mesh::faces::face_iterator face_ds = cell_ds->state().shape().faces().face().begin();
			face_ds != cell_ds->state().shape().faces().face().end(); face_ds ++){
		if(faces.find(face_ds->ID()) == faces.end()){
			io_face * face = new io_face;
			int face_id = face_ds->ID();
			face->mcds_obj = &(*face_ds);
			face->cell_ids.push_back(cell_ds->ID());
			faces[face_id] = * face;
			cells[cell_ds->ID()].face_ids.push_back(face_id);
			for(unsigned int face_edge_index = 0; face_edge_index < face_ds->edge_ID().size(); 
					face_edge_index++){
				int face_edge_id = face_ds->edge_ID()[face_edge_index];
				face->edge_ids.push_back(face_edge_id);
				edges[face_edge_id].face_ids.push_back(face_id);
				for (int face_edge_node_index = 0; face_edge_node_index < 2; 
						face_edge_node_index ++){
					io_node * face_edge_node = 
						&nodes[edges[face_edge_id].node_ids[face_edge_node_index]];
					face_edge_node->edge_ids.push_back(face_edge_id);
					highlow_xy(&face->lowest_x, &face->highest_x, 
							&face->lowest_y, &face->highest_y, 
						       	face_edge_node->x, face_edge_node->y,
							face_ds == cell_ds->state().shape().faces().face().begin() &&
							face_edge_index == 0 && face_edge_node_index == 0);
				}
			}
			faces[face_id] = *face;
		}
	}
}

void MCDS_io::process_cellshapes(){
	for (cell::cell_population_individual::cell_iterator cell_ds = 
			multicellds->cellular_information().cell_populations().cell_population().cell().begin();
			cell_ds != multicellds->cellular_information().cell_populations()
			.cell_population().cell().end(); cell_ds++){
		io_cell * cell = new io_cell;
		int cell_id = cell_ds->ID();
		cell->mcds_obj = &(*cell_ds);
		cells[cell_id] = *cell;
		process_nodes(cell->mcds_obj);
		process_edges(cell->mcds_obj);
		process_faces(cell->mcds_obj);
	}
	mapped = true;
}

void MCDS_io::denoise(int repeats){
	int ** tmp_lattice = make_lattice(size_x, size_y);
	int ** swap = 0;
	for (int index = 0; index < repeats; index++){
		denoise_lattice(lattice, tmp_lattice, size_x, size_y);
		swap = lattice;
		lattice = tmp_lattice;
		tmp_lattice = swap;
	}
	if (repeats%2 != 0){
		swap = lattice;
                lattice = tmp_lattice;
                tmp_lattice = swap;
	}
	delete tmp_lattice;
}

void MCDS_io::highlow_xy(double* lowest_x, double* highest_x,
                         double* lowest_y, double* highest_y,
                         double x, double y,
                         bool first){
        if (first){
                *lowest_x  = x;
                *highest_x = x;
                *lowest_y  = y;
                *highest_y = y;
        }
        if (x < *lowest_x )  *lowest_x = x;
        if (y < *lowest_y )  *lowest_y = y;
        if (x > *highest_x ) *highest_x = x;
        if (y > *highest_y ) *highest_y = y;
}
