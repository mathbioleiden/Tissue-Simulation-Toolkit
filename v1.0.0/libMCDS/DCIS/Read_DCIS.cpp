//############################################################
//
// Created by Samuel Friedman on July 5, 2016
//
// Read DCIS output files into MultiCellDS format
//
//############################################################

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <regex>

#include "MultiCellDS.hpp"
#include "MultiCellDS-pimpl.hpp"
#include "MultiCellDS-simpl.hpp"
#include "pugixml.hpp"

using namespace std;

// Usage: Read_DCIS

string insert_whitespace(string x, string y, string z) {
  ostringstream oss;
  oss << x << " " << y << " " << z;
  return oss.str();
}

string insert_whitespace(double x, double y, double z) {
  ostringstream oss;
  oss << x << " " << y << " " << z;
  return oss.str();
}

string remove_parentheses_comma_to_space(string str) {
  string temp, space = " ";// = str.subst(1,str.length()-1);
  regex re(",");
  regex_replace(back_inserter(temp), str.begin()+1, str.end()-1, re , space);
  return temp;
}

int main (int argc, char* argv[]) {

  // Setup to read DCIS XML file
  pugi::xml_document doc;
  pugi::xml_parse_result result = doc.load_file("output00001080.xml");
  std::cout << "Load result: " << result.description() << endl;
  xml_schema::string_simpl string_s;
  xml_schema::double_simpl double_s;
  common::units_decimal_simpl decimal_s;
  
  //doc_s

  // Setup for MultiCellDS output
  MultiCellDS *h = new MultiCellDS;

  // Create a list of individual cells for MultiCellDS
  cell::cell_population_individual *cpi = new cell::cell_population_individual;

  // Find the list of individual cells from DCIS
  pugi::xml_node cell_list = doc.child("data_set").child("cell_list");
  int cell_i = 0;

  // For each individual cell ...
  for(pugi::xml_node DCIS_cell: cell_list.children("cell") ) {

    // Create a new cell for MultiCellDS
    cell::cell *cell = new cell::cell;

    // Setup for obtaining different aspects of cellular data
    pugi::xml_node cell_properties = DCIS_cell.child("cell_properties");
    pugi::xml_node cell_state = DCIS_cell.child("cell_state");
    phenotype_dataset::phenotype_dataset *pds = new phenotype_dataset::phenotype_dataset;
    phenotype_common::geometrical_properties *gp = new phenotype_common::geometrical_properties;

    // Translate cell radius from DCIS to MultiCellDS
    common::units_decimal *radius_dec = new common::units_decimal; // Setup a units_decimal element
    phenotype_common::lengths *lengths_xml = new phenotype_common::lengths; // Setup up the parent container of radius

    pugi::xml_node cell_radius = cell_properties.child("radius"); // Find DCIS radius element
    double radius = cell_radius.text().as_double(); // Extract the radius as a double
    radius_dec->units(cell_radius.attribute("units").as_string()); // Get and the units
    radius_dec->base_value(radius); // Set the radius
    lengths_xml->radius(radius_dec); // Place the radius in lengths
    gp->lengths(lengths_xml); // Place lengths in geometric properties

    // Translate cell volume from DCIS to MultiCellDS
    common::units_decimal *volume_dec = new common::units_decimal;    
    phenotype_common::volumes *volumes_xml = new phenotype_common::volumes;
    pugi::xml_node cell_volume = cell_properties.child("volume");
    double volume = cell_volume.text().as_double();
    volume_dec->units(cell_volume.attribute("units").as_string());
    volume_dec->base_value(volume);
    volumes_xml->total_volume(volume_dec);

    // Translate solid volume from DCIS to MultiCellDS
    common::units_decimal *solid_volume_dec = new common::units_decimal;
    pugi::xml_node DCIS_volume = cell_properties.child("volume");
    double solid_volume = DCIS_volume.text().as_double();
    solid_volume_dec->units(DCIS_volume.attribute("units").as_string());
    solid_volume_dec->base_value(solid_volume);
    volumes_xml->solid_volume(solid_volume_dec);

    //Test custom
    cout << "Step 1" << endl;
    string hiya = "<hiya>Hello World!</hiya>";
    common::custom *custom_hiya = new common::custom;
    //custom_hiya->custom_data().push_back(const_cast<void *>(reinterpret_cast<const void*>(hiya.c_str())));
    //custom_hiya->custom_data()
    custom_hiya->assign(hiya);
    cout << "Step 2" << endl;
    volumes_xml->custom(*custom_hiya);
    cout << "Step 3" << endl;
    cout << "Sanity check: " << volumes_xml->custom() << endl;
    
    // Places volumes in geometric properties
    gp->volumes(volumes_xml);

    // Setup for adhesion parameters
    phenotype_common::adhesion *adhesion = new phenotype_common::adhesion;

    // Setup for custom elements
    common::custom *custom_adhesion_xml = new common::custom;
    
    // Create a phenotype
    phenotype::phenotype *p; p = new phenotype::phenotype;
    p->geometrical_properties(gp); // Place geometric properties in phenotype
    phenotype_base::phenotype_type pt = phenotype_base::phenotype_type::current; // Select the current phenotype instead of target or expected
    p->type(pt); // Place the phenotype type into the phenotype

    // Put the phenotype into the phenotype dataset
    for(int i=0; i<1; i++)
      pds->phenotype().push_back(p);

    // Work on the cell nucleus

    // Translate nuclear radius from DCIS to MultiCellDS
    // The radius part
    common::units_decimal *nuclear_radius_dec = new common::units_decimal;
    pugi::xml_node DCIS_nuclear_radius = cell_properties.child("nuclear_radius");
    double nuclear_radius = DCIS_nuclear_radius.text().as_double();
    nuclear_radius_dec->units(DCIS_nuclear_radius.attribute("units").as_string());
    nuclear_radius_dec->base_value(nuclear_radius);
    // The lengths part
    phenotype_common::lengths *nuclear_lengths_xml = new phenotype_common::lengths;    
    nuclear_lengths_xml->radius(nuclear_radius_dec);
    // The geometrical properties part
    phenotype_common::geometrical_properties *nuclear_gp = new phenotype_common::geometrical_properties;
    nuclear_gp->lengths(nuclear_lengths_xml);
    // The nuclear phenotype part
    phenotype_base::phenotype_base *nuclear_p = new phenotype_base::phenotype_base;
    nuclear_p->geometrical_properties(nuclear_gp);
    nuclear_p->type(pt);
    // The "cell part" part
    phenotype_base::cell_parts *cell_part = new phenotype_base::cell_parts;
    cell_part->phenotype().push_back(nuclear_p);
    cell_part->name("nucleus"); // Name this cell part "nucleus"
    // Add the nucelus to the phenotype dataset.
    pds->cell_part().push_back(cell_part);

    // Add the phenotype dataset to the cell
    cell->phenotype_dataset(pds);

    // Work on the cell state
    state::state *state = new state::state;
    common::units_string *str = new common::units_string;
    common::units_double_list *udl = new common::units_double_list;
    //pugi::xml_node position = cell_state.child("Position");

    // Translate position from DCIS to MultiCellDS
    string position = cell_state.child("Position").text().as_string();
    istringstream iss(position);
    double x, y, z;
    iss >> x >> y >> z;
    udl->push_back(x); udl->push_back(y); udl->push_back(z);
    udl->units("micron");
    str->assign(remove_parentheses_comma_to_space(position));
    str->units("micron");
    //state->position(str);
    state->position(udl);

    // Translate cell cycle time from DCIS to MultiCellDS
    state::phase *phase = new state::phase;
    //phase->phase_name("growth phase");
    common::units_decimal *age_units = new common::units_decimal;
    age_units->base_value(cell_state.child("cell_cycle_time").text().as_double());
    age_units->units("minutes");
    phase->elapsed_time(age_units);
    state->phase(phase);

    // Add state to the cell
    cell->state(state);

    // Add an ID number to the cell
    cell->ID(cell_i);

    // Add the cell to the cell population list
    cpi->cell().push_back(cell);

    cell_i++;
  }

  // Allow cell populations to have a population of individual cells.
  cell::cell_populations *cps = new cell::cell_populations;
  cps->cell_population(cpi);
  cout << "So far so good" << endl;

  // Allow cellular information to have cell populations
  cell::cellular_information *ci = new cell::cellular_information;
  ci->cell_populations(cps);
  cout << "So far so good" << endl;

  // Allow the root MultiCellDS element to have cellular information
  h->cellular_information(ci);
  MCDS_type mcds_type;// = new MCDS_type;
  mcds_type.value(MCDS_type::value_type::snapshot_simulation); // This is a simulation snapshot (vs experiemnt or clinical)
  h->type(mcds_type); // Assign the type over to the MultiCellDS element
  //h->type("snapshot/simulation");
  h->version("0.5.0"); // State the MultiCellDS version number
  cout << "So far so good" << endl;

  // Setup for printing the MultiCellDS file
  MultiCellDS_saggr MultiCellDS_s, MultiCellDS_s2;
  
  // doc_s is intended for printing to the screen
  // doc_s2 is intended for printing to a file

  // XSD/e setup for printing
  xml_schema::document_simpl doc_s (MultiCellDS_s.root_serializer (),
				    MultiCellDS_s.root_name ());
  xml_schema::document_simpl doc_s2 (MultiCellDS_s2.root_serializer (),
				     MultiCellDS_s2.root_name ());
  
  // Initialization
  MultiCellDS_s.pre (*h);
  MultiCellDS_s2.pre (*h);
  // Print to the screen
  //doc_s.serialize (cout, xml_schema::document_simpl::pretty_print);
  // Pick a file to write
  ofstream ofs("blah.xml");
  // Print to the file
  cout << "Time to write" << endl;
  doc_s2.serialize (ofs, xml_schema::document_simpl::pretty_print);
  ofs << endl; // Add an extra newline at the end of the file
  // Cleanup of the writing
  MultiCellDS_s.post ();
  MultiCellDS_s2.post ();
  
  cout << "All done" << endl;
  
  return 0;
}
