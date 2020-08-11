#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <ctime>

#include "mcds_io.h"
#include "MultiCellDS.hpp"
#include "MultiCellDS-pimpl.hpp"
#include "MultiCellDS-simpl.hpp"


MCDS_io::MCDS_io(){
  multicellds = new MultiCellDS;
}

MCDS_io::MCDS_io(std::string filename){
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


void MCDS_io::add_time(){
  std::time_t t = std::time(NULL);
  struct tm lt = *std::localtime(&t);
  time_t offset_second(lt.tm_gmtoff);
  tm off_t = *std::gmtime(&offset_second);
  short timezone_hour = (off_t.tm_hour+12)%24-12, timezone_minute = off_t.tm_min;
  xml_schema::date_time new_times(lt.tm_year+1900, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min, lt.tm_sec, timezone_hour, timezone_minute);
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

void MCDS_io::map_cellshape(){
  for (cell::cell_population_individual::cell_iterator cell_ds = 
       multicellds->cellular_information().cell_populations().cell_population().cell().begin();
       cell_ds != multicellds->cellular_information().cell_populations().cell_population().cell().end();
       cell_ds++){
    io_cell * cell = new io_cell;
    int cell_id = cell_ds->ID();
    cell->mcds_obj = &(*cell_ds);
    for (mesh::nodes::node_iterator node_ds = cell_ds->state().shape().nodes().node().begin();
         node_ds != cell_ds->state().shape().nodes().node().end(); node_ds ++){
      if(nodes.find(node_ds->ID()) == nodes.end()){
        io_node * node = new io_node;
        int node_id = node_ds->ID();
        node->mcds_obj = &(*node_ds); 
        node->cell_ids.push_back(cell_id);
        node->x = node_ds->position()[0];
        node->y = node_ds->position()[1];
        //std::cout <<"node ID: "<< node_id << " node X: " << node->x << " node Y: " << node->y << std::endl;
        if (node_ds == cell_ds->state().shape().nodes().node().begin() && cell_ds == 
            multicellds->cellular_information().cell_populations().cell_population().cell().begin()){
          lowest_x = node->x; lowest_y = node->y; highest_x = node->x; highest_y = node->y;
        }
        //std::cout << "low: "<< lowest_y << " high: "<<  highest_y << std::endl;
	if (node->x < lowest_x ) lowest_x = node->x;
        if (node->y < lowest_y ) lowest_y = node->y;
        if (node->x > highest_x ) highest_x = node->x;
        if (node->y > highest_y ) highest_y = node->y;
        nodes[node_id] = node;
      }
    }
    for ( mesh::edges::edge_iterator edge_ds = cell_ds->state().shape().edges().edge().begin(); 
          edge_ds != cell_ds->state().shape().edges().edge().end(); edge_ds ++){
      if(edges.find(edge_ds->ID()) == edges.end()){
        io_edge * edge = new io_edge;
        int edge_id = edge_ds->ID();
        edge->mcds_obj = &(*edge_ds);
        edges[edge_id] = edge;
        edge->cell_ids.push_back(cell_id);
        for (int edge_node_index = 0; edge_node_index < 2; edge_node_index ++){
          int edge_node_id = edge_ds->node_ID()[edge_node_index];
          //std::cout << "edge node ID: " << edge_node_id << std::endl;
          edge->node_ids.push_back(edge_node_id);
          io_node * edge_node = nodes[edge_node_id];
          edge_node->edge_ids.push_back(edge_id);
          //std::cout << "Node_edge: id: " << edge_node_id << " x: "<< edge_node->x << " y: " << edge_node->y << std::endl;
          if ( edge_node_index == 0){
            edge->lowest_x = edge_node->x; edge->lowest_y = edge_node->y; edge->highest_x = edge_node->x; edge->highest_y = edge_node->y;

          }
          //std::cout << "Edge: low: "<< edge->lowest_y << " high: "<< edge->highest_y << std::endl; 
          if (edge_node->x < edge->lowest_x ) edge->lowest_x = edge_node->x;
          if (edge_node->y < edge->lowest_y ) edge->lowest_y = edge_node->y;
          if (edge_node->x > edge->highest_x ) edge->highest_x = edge_node->x;
          if (edge_node->y > edge->highest_y ) edge->highest_y = edge_node->y;
        }   
        edges[edge_id] = edge;
      } 
    }
    for (mesh::faces::face_iterator face_ds = cell_ds->state().shape().faces().face().begin();
         face_ds != cell_ds->state().shape().faces().face().end(); face_ds ++){
      if(faces.find(face_ds->ID()) == faces.end()){
        io_face * face = new io_face;
        int face_id = face_ds->ID();
        face->mcds_obj = &(*face_ds);
        face->cell_ids.push_back(cell_id);
        faces[face_id] = face;
        cell->face_ids.push_back(face_id);
       // std::cout  << "FaceIndx: " << face_id << std::endl;
        for(unsigned int face_edge_index = 0; face_edge_index < face_ds->edge_ID().size(); 
            face_edge_index++){
          int face_edge_id = face_ds->edge_ID()[face_edge_index];
          //std::cout << "face egde index: " << face_edge_index << std::endl;
          face->edge_ids.push_back(face_edge_id);
          edges[face_edge_id]->face_ids.push_back(face_id);
          for (int face_edge_node_index = 0; face_edge_node_index < 2; face_edge_node_index ++){
            
            io_node * face_edge_node = nodes[edges[face_edge_id]->node_ids[face_edge_node_index]];
            face_edge_node->edge_ids.push_back(face_edge_id);
            //std::cout << "Node_face: id: " << edges[face_edge_id]->node_ids[face_edge_node_index] << " x: "  << face_edge_node->x << " y: " << face_edge_node->y << std::endl; 
            if (face_ds == cell_ds->state().shape().faces().face().begin() && face_edge_index == 0 && face_edge_node_index == 0){
              face->lowest_x = face_edge_node->x;
              face->lowest_y = face_edge_node->y;
              face->highest_x = face_edge_node->x;
              face->highest_y = face_edge_node->y;
            }
            if (face_edge_node->x < face->lowest_x )  face->lowest_x = face_edge_node->x;
            if (face_edge_node->y < face->lowest_y )  face->lowest_y = face_edge_node->y;
            if (face_edge_node->x > face->highest_x ) face->highest_x = face_edge_node->x;
            if (face_edge_node->y > face->highest_y ) face->highest_y = face_edge_node->y;
          }
        }
        faces[face_id] = face;
      }
    }
    cells[cell_id] = cell;
  }
  mapped = true;
}
