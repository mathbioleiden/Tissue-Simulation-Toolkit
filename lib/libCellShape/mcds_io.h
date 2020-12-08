#include <iostream>
#include <map>
#include <vector>
#include <string>

#include "MultiCellDS.hpp"
#include "MultiCellDS-pimpl.hpp"
#include "MultiCellDS-simpl.hpp"

enum MCDS_IO_TYPES{
	VECTOR,
	LATTICE,
};

struct io_face{
	mesh::face * mcds_obj;
	double lowest_x;
	double lowest_y;
	double highest_x;
	double highest_y;
	std::vector<int> node_ids;
	std::vector<int> edge_ids;
	std::vector<int> cell_ids;
};

struct io_edge{
	mesh::edge * mcds_obj;
	double lowest_x;
	double lowest_y;
	double highest_x;
	double highest_y;
	std::vector<int> node_ids;
	std::vector<int> face_ids;
	std::vector<int> cell_ids;
};

struct io_node{
	mesh::node * mcds_obj;
	double x;
	double y;
	std::vector<int> edge_ids;
	std::vector<int> face_ids;
	std::vector<int> cell_ids;
};

struct io_cell{
	cell::cell * mcds_obj;
	int type;
	double centroid_x;
	double centroid_y;
	double area;
	double target_area;
	double major_axis;
	double minor_axis;
	int lattice_id;
	std::vector<int> node_ids;
	std::vector<int> edge_ids;
	std::vector<int> face_ids;
};

class MCDS_io{
	public:
		MCDS_io();
		MCDS_io(std::string filename, double unit_ratio = 1, std::string unit_name = "");
		void read(std::string filename);
		void write(std::string filename);
		void add_metadata(std::string filename);
		void add_time();
		void finalize_cellshapes();
		void process_cellshapes();
		
		inline MultiCellDS* get_multicellds(){return multicellds;}
		inline std::map<int, io_face>* get_faces(){return &faces;}
		inline std::map<int, io_edge>* get_edges(){return &edges;}
		inline std::map<int, io_node>* get_nodes(){return &nodes;}
		inline std::map<int, io_cell>* get_cells(){return &cells;}
		
		inline io_face* face_by_id(int id){return & faces[id];}
		inline io_edge* edge_by_id(int id){return & edges[id];}
		inline io_node* node_by_id(int id){return & nodes[id];}
		inline io_cell* cell_by_id(int id){return & cells[id];}
		
		inline int get_lowest_x(){return lowest_x;}
		inline int get_lowest_y(){return lowest_y;}
		inline int get_highest_x(){return highest_x;}
		inline int get_highest_y(){return highest_y;}
		
		inline int get_size_x(){return size_x;}
		inline int get_size_y(){return size_y;}
		inline void set_size(int x, int y){ size_x = x; size_y = y;};
		
		void inline set_unit_mult(double mult){unit_r = mult;}
		void inline set_unit_name(std::string unit){unit_n = unit;}

		io_cell* get_new_cell(int id);
		io_edge* get_new_edge(int id);
		io_face* get_new_face(int id);
		io_node* get_new_node(int id);

		inline int ** get_lattice(){return lattice;};
		inline void set_lattice(int ** new_lattice, int sizex, int sizey){lattice = new_lattice; 
			set_size(sizex, sizey); };
		
		int get_new_edge_uniq(int node1, int node2);

		void vector_from_lattice();
		void lattice_from_vector();
		
		void denoise(int repeats);

	private:
		double lowest_x;
		double lowest_y;
		double highest_x;
		double highest_y;
		
		double unit_r;
		std::string unit_n;
		
		bool mapped = false;
		MultiCellDS* multicellds;
		std::map<int, io_face> faces;
		std::map<int, io_edge> edges;
		std::map<int, io_node> nodes;
		std::map<int, io_cell> cells;
		
		std::map<std::string, int> edge_by_nodes;
		
		cell::cell* finalize_cell(int id);
		mesh::nodes_edges_faces* finalize_shape(io_cell& cell);
		mesh::face* finalize_face(int id);
		mesh::edge* finalize_edge(int id);
		mesh::node* finalize_node(int id);
		
		int ** lattice;
		int size_x;
		int size_y;
		
		void process_nodes(cell::cell* cell);
		void process_edges(cell::cell* cell);
		void process_faces(cell::cell* cell);

		void highlow_xy(double* lowest_x, double* highest_x,
                         double* lowest_y, double* highest_y,
                         double x, double y,
                         bool first);

		void nodes_from_lattice();
		void edges_from_lattice();
		void faces_from_lattice();

		void lattice_from_face(int face_id, int id, int offset_x, int offset_y);
};

