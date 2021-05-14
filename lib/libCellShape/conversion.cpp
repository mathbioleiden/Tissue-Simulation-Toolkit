#include <iostream>
#include <set>

#include "mcds_io.h"
#include "lattice_util.h"

void MCDS_io::nodes_from_lattice(){
	int node_id = 0;
	for (int y = 0; y < size_x; y++){
		for (int x = 0; x < size_y; x++){
			//std::cout << "X: " << x << " Y:" << y << std::endl; 
			//std::cout << "Lattice: " << lattice[x][y] << std::endl;
			double a = 0, b = 0, c = 0, d = 0;
			if (x > 0 && y > 0){          a = lattice[x-1][y-1];}
			if (y > 0 && x < size_x){     b = lattice[x][y-1];}
			if (x > 0 && y < size_y){     c = lattice[x-1][y];}
			if (x < size_x && y < size_y){d = lattice[x][y];}
			if (a > 0 || b > 0 || c > 0 || d > 0){
				std::set<int> cells;
				if(a > 0) {cells.insert(a);}    
				if(b > 0) {cells.insert(b);}
				if(c > 0) {cells.insert(c);}
				if(d > 0) {cells.insert(d);}
				if (cells.size() > 0){
					if (!((a == b && a != c && c == d) ||
					      (b == d && b != a && a == c) ||
					      (d == c && d != b && b == a) ||
					      (c == a && c != d && d == b) ||
					      (a == b && a == c && a == d))){
						io_node * node = get_new_node(node_id);
						node->x = x -0.5;
						node->y = y -0.5;
						for(int cell_id : cells){
							std::cout << "Adding node " << node_id << " to " << cell_id << "" << std::endl;
							cell_by_id(cell_id)->node_ids.push_back(node_id);
						}
						node->cell_ids = std::vector<int>(cells.begin(), cells.end()); 
						node_id ++;
					}
				}
			}
		}
	}
}

void MCDS_io::edges_from_lattice(){
	for (auto cell_i : cells){
		int cell_id = cell_i.first;
		io_cell * cell = cell_by_id(cell_id); 
		for(int node_id_a : cell->node_ids) {
			io_node * node_a = node_by_id(node_id_a);
			int closest_x = -1, distance_x = -1, closest_y = -1, distance_y = -1;
			int sx = node_a->x +0.5, sy = node_a->y +0.5;
			for(int node_id_b : cell->node_ids){
				io_node * node_b = node_by_id(node_id_b);
				double dx = node_a->x - node_b->x;
				double dy = node_a->y - node_b->y;
				int  b = 0, c = 0, d = 0;
				if (sy > 0 && sx < size_x){                  b = lattice[sx][sy-1];}
				if (sx > 0 && sy < size_y){                  c = lattice[sx-1][sy];}
				if (sx < size_x && sy < size_y){ d = lattice[sx][sy];  }
				bool going_right = dx < 0 && dy == 0;
				bool going_down  = dy < 0 && dx == 0;
				bool is_on_edge_down  = going_down  && ((c != d) && (c == cell_id || d == cell_id));
				bool is_on_edge_right = going_right && ((b != d) && (b == cell_id || d == cell_id));
				if ((abs(dx) < distance_x || closest_x == -1) && is_on_edge_right){
					distance_x = abs(dx); closest_x = node_id_b;
				}
				if((abs(dy) < distance_y || closest_y == -1) && is_on_edge_down){
					distance_y = abs(dy); closest_y = node_id_b;
				}
			}
			if(closest_x != -1){
				int edge_id = get_new_edge_uniq(node_id_a, closest_x);
				cell->edge_ids.push_back(edge_id);
				edge_by_id(edge_id)->cell_ids.push_back(cell_i.first);  
			}
			if(closest_y != -1){
				int edge_id = get_new_edge_uniq(node_id_a, closest_y);
				cell->edge_ids.push_back(edge_id);
				edge_by_id(edge_id)->cell_ids.push_back(cell_i.first);
			}
		}
	}
}

void MCDS_io::faces_from_lattice(){
	int face_id = 0;
	for (auto cell_i : cells){
		io_cell * cell = cell_by_id(cell_i.first);
		io_face * face = get_new_face(face_id);
		for (int edge_id : cell->edge_ids){
			face->edge_ids.push_back(edge_id);
		}
		cell->face_ids.push_back(face_id);
		face_id++;
	}
}

void MCDS_io::vector_from_lattice(){
	nodes_from_lattice();
	edges_from_lattice();
	faces_from_lattice();
}

void MCDS_io::lattice_from_face(int face_id, int id, int offset_x, int offset_y){
	io_face * face = face_by_id(face_id);
	double intersection_points[face->edge_ids.size()+1];
	std::cout << "poly_add face: " << face_id << std::endl; 
	for (int y = face->lowest_y; y < face->highest_y; y++){
		double ym = y + 0.5, lowest = -1, highest = -1;
		int point_index = 0; 
		std:: cout << "Y level: " << y << std::endl;
		for (int edge_id : face->edge_ids){
			io_edge * edge = edge_by_id(edge_id);
			if(y > edge->lowest_y  && y < edge->highest_y ){
				std::cout << "Edge_id: " << edge_id << std::endl; 
				double x1 = node_by_id(edge->node_ids[0])->x;
				double x2 = node_by_id(edge->node_ids[1])->x;
				double y1 = node_by_id(edge->node_ids[0])->y;
				double y2 = node_by_id(edge->node_ids[1])->y;
				std::cout << "x1: " << x1 << " y1: " << y1 <<  " x2: " << x2 << " y2: " << y2 << std::endl;
				if (y1 != y2){
					double res;
					if(x1 == x2){
						res = x1;
					}
					else{
						double f = (y1-y2)/(x1-x2);
						double a = y1 - x1*f;
						res = (ym-a)/((y2-y1)/(x2-x1));
					}
					if (res < face->lowest_x){ res = face->lowest_x;}
					if (res > face->highest_x){ res = face->highest_x;}
					if (edge_id == *face->edge_ids.begin()){lowest = res; highest = res;}
					if (res < lowest){ lowest = res;}
					if (res > highest){ highest = res;}
					std::cout << "Intersection point: " << res << std::endl;
					intersection_points[point_index] = res;
					point_index++;
				} 
			}
		}
		intersection_points[point_index+1] = -1;
		for (int x = lowest; x <= highest; x++){
			double xm = x + 0.5;
			int evenodd = 0;
			for (int index =0; index < point_index && intersection_points[index] != -1; index++){ 
				if ((xm - intersection_points[index]) > 0){
					evenodd++;
				}
			}
			if (evenodd%2 == 1){
				int fx = x + offset_x;
				int fy = y + offset_y;
				if (fx < 0 || fy < 0 || fx > size_x-1 || fy > size_y-1){ 
					std::cerr << "OOPS! Polygon outside of mesh!" << std::endl ;continue;} 
				std::cout << "lattice X:" << x << " Y: " << y << " val: "<< id << std::endl;
				lattice[fx][fy] = id;
			} 
		}
	}
}

void MCDS_io::lattice_from_vector(){
	size_x = (highest_x - lowest_x) * 1.5;
	size_y = (highest_y - lowest_y) * 1.5;
	int offset_x = (size_x / 2) - (highest_x - ((highest_x - lowest_x) / 2));
	int offset_y = (size_y / 2) - (highest_y - ((highest_y - lowest_y) / 2));
	int add_id = 0;
	lattice = make_lattice(size_x, size_y);	
	for (auto iocell : cells){
		if (iocell.second.mcds_obj->ID() == 0) {add_id = 1;  break;}
	}
	for (auto iocell : cells){
		for (int face_id : iocell.second.face_ids){
			iocell.second.lattice_id =  iocell.second.mcds_obj->ID() + add_id;
			lattice_from_face(face_id, iocell.second.lattice_id, offset_x, offset_y);
		}
	}
	for (int x = 0; x < size_x; x++){
		for (int y = 0; y < size_y; y++ ){
			std::cout << "X:" << x << " Y: " << y << " val: " << lattice[x][y] << std::endl; 	
		}
	}
}

