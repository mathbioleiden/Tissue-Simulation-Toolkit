//############################################################
//
// Created by Samuel Friedman on Nov 20, 2016
//
// Create sample simulation snapshot for MultiCellDS.
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
#include <chrono>
#include <ctime>
#include <iomanip>

#include "MultiCellDS.hpp"
#include "MultiCellDS-pimpl.hpp"
#include "MultiCellDS-simpl.hpp"

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
  xml_schema::string_simpl string_s;
  xml_schema::double_simpl double_s;
  common::units_decimal_simpl decimal_s;
  
  //doc_s

  // Setup for MultiCellDS output
  MultiCellDS *h = new MultiCellDS;

  // Create a list of individual cells for MultiCellDS
  cell::cell_population_individual *cpi = new cell::cell_population_individual;

  // Find the list of individual cells from DCIS
  int cell_i = 0;
  int num_cells = 10;
  
  // For each individual cell ...
  for(cell_i = 0; cell_i < num_cells; cell_i++) {

    // Create a new cell for MultiCellDS
    cell::cell *cell = new cell::cell;

    // Setup for obtaining different aspects of cellular data
    phenotype_dataset::phenotype_dataset *pds = new phenotype_dataset::phenotype_dataset;
    phenotype_common::geometrical_properties *gp = new phenotype_common::geometrical_properties;

    // Put a cell radius into MultiCellDS XML format
    common::units_decimal_nonnegative *radius_dec = new common::units_decimal_nonnegative; // Setup a units_decimal element
    phenotype_common::lengths *lengths_xml = new phenotype_common::lengths; // Setup up the parent container of radius

    // Make up a radius for each cell.
    double radius = 5.0; // Assign a value for the radius as a double
    radius_dec->units("micron"); // Get and the units
    radius_dec->base_value(radius); // Set the radius
    lengths_xml->radius(radius_dec); // Place the radius in lengths
    gp->lengths(lengths_xml); // Place lengths in geometric properties

    // Make up a cell volume for each cell.
    common::units_decimal_nonnegative *volume_dec = new common::units_decimal_nonnegative;    
    phenotype_common::volumes *volumes_xml = new phenotype_common::volumes;
    double volume = 525; // Roughly 4/3*pi*5^3
    volume_dec->units("micron^3");
    volume_dec->base_value(volume);
    volumes_xml->total_volume(volume_dec);

    // Places volumes in geometric properties
    gp->volumes(volumes_xml);

    // Create a phenotype
    phenotype::phenotype *p; p = new phenotype::phenotype;
    p->geometrical_properties(gp); // Place geometric properties in phenotype
    phenotype_base::phenotype_type pt = phenotype_base::phenotype_type::current; // Select the current phenotype instead of target or expected
    p->type(pt); // Place the phenotype type into the phenotype

    // Put the phenotype into the phenotype dataset
    for(int i=0; i<1; i++)
      pds->phenotype().push_back(p);

    
    // Add the phenotype dataset to the cell
    cell->phenotype_dataset(pds);

    // Work on the cell state
    state::state *state = new state::state;
    common::units_string *str = new common::units_string;
    common::units_double_list *udl = new common::units_double_list;
    //pugi::xml_node position = cell_state.child("Position");

    // Put all the cells in a straight line
    double x, y, z;
    x = 0.0+cell_i*10.0;
    y = 0.0;
    z = 0.0;
    udl->push_back(x); udl->push_back(y); udl->push_back(z);
    udl->units("micron");
    state->position(udl);

    // Make up a cell cycle time for each cell MultiCellDS
    state::phase *phase = new state::phase;
    common::units_decimal *age_units = new common::units_decimal;
    age_units->base_value(10.0*cell_i);
    age_units->units("minutes");
    phase->elapsed_time(age_units);
    state->phase(phase);

    // Add state to the cell
    cell->state(state);

    // Add an ID number to the cell
    cell->ID(cell_i);

    // Add the cell to the cell population list
    cpi->cell().push_back(cell);

  }

  // Allow cell populations to have a population of individual cells.
  cell::cell_populations *cps = new cell::cell_populations;
  cps->cell_population(cpi);

  // Allow cellular information to have cell populations
  cell::cellular_information *ci = new cell::cellular_information;
  ci->cell_populations(cps);

  // Allow the root MultiCellDS element to have cellular information
  h->cellular_information(ci);
  MCDS_type mcds_type;// = new MCDS_type;
  mcds_type.value(MCDS_type::value_type::snapshot_simulation); // This is a simulation snapshot (vs experiemnt or clinical)
  h->type(mcds_type); // Assign the type over to the MultiCellDS element
  h->version("0.5.0"); // State the MultiCellDS version number

  //############################################################
  // Add microenvironment
  //############################################################
  // Create the microenvironment and everything with it
  
  // Create the material amount
  double auxin_amount = 0.1;
  //shared_ptr<variables::material_amount> ma(new variables::material_amount);
  variables::material_amount *ma = new variables::material_amount;
  ma->base_value(auxin_amount);
  ma->units("nanoMolar");
  ma->type(variables::amount_type::concentration); // amount_type is an enum with value concentration

  // Create the variables
  //shared_ptr<variables::variable> var(new variables::variable);
  variables::variable *var = new variables::variable;
  //var->material_amount(ma); // Put material amount in the variable
  var->ChEBI_ID("22676"); // ChEBI value for auxin. Found on bioportals.bioontology.org
  var->name("auxin");
  var->type(variables::amount_type::concentration); // amount_type is an enum with value concentration
  var->ID(0); // Internal ID number

  // Create the list of variables
  //shared_ptr<variables::list_of_variables> list_var(new variables::list_of_variables);
  variables::list_of_variables *list_var = new variables::list_of_variables;
  list_var->variable().push_back(var); // Add the variable to the list of variables

  // Create the domain
  //shared_ptr<microenvironment::domain> domain(new microenvironment::domain);
  microenvironment::domain *domain = new microenvironment::domain;
  domain->variables(list_var); // Add list of variables to the domain

  // Create the microenvironment
  //shared_ptr<microenvironment::microenvironment> menv(new microenvironment::microenvironment);
  microenvironment::microenvironment *menv = new microenvironment::microenvironment;
  //cout << "Making the mesh" << endl;
  // Create the mesh
  // Creating a cubic mesh. The points here are considered to be the voxel centers
  mesh::mesh *mesh = new mesh::mesh;
  // Create the data
  double min_pos = 5.0, max_pos = 55.0, spacing_pos = 10.0;
  int num_pos = 6;
  //cout << "Coordinates" << endl;
  common::units_double_list *udl = new common::units_double_list;
  for(int i=0; i<num_pos; i++) {
    //mesh->x_coordinates("5.0 15.0 25.0 35.0 45.0 55.0");
    udl->push_back(min_pos+i*spacing_pos);
  }
  mesh->x_coordinates(udl);
  mesh->y_coordinates(udl);
  mesh->z_coordinates(udl);
  //cout << "Attributes" << endl;
  mesh->type("Cubic");
  //cout << "uniform" << endl;
  mesh->uniform(true);
  //cout << "regular" << endl;
  mesh->regular(true);
  //cout << "units" << endl;
  mesh->units("micron");
  //cout << "Domain" << endl;
  domain->mesh(mesh); // Adding mesh to microenvironment
  //cout << "Making the variable data" << endl;
  variables::data *var_data = new variables::data;
  for(int x_pos = 0; x_pos < num_pos; x_pos++) {
      for(int y_pos = 0; y_pos < num_pos; y_pos++) {
	  for(int z_pos = 0; z_pos < num_pos; z_pos++) {
	    variables::data_vector *data_vector = new variables::data_vector;
	    common::unsigned_int_list *uil = new common::unsigned_int_list;
	    uil->push_back(x_pos); uil->push_back(y_pos); uil->push_back(z_pos);
	    data_vector->voxel_ID(uil);
	    data_vector->push_back(auxin_amount);
	    //variables::
	    var_data->data_vector().push_back(data_vector);
	  }
      }
  }

  //cout << "Assigning pointers for microenvironment " << var_data->data_vector().size() << endl;
  domain->data(var_data);
  
  menv->domain().push_back(domain); // Add the domain to the microenvironment

  // Testing adding custom element
  common::custom *custom_test = new common::custom;
  //common::custom::custom_data_sequence& custom_content(custom_test->custom_data());
  //unique_ptr<string> hw_test; //("hello_world");
  //hw_test.reset(new string("hello_world"));
  string *hw_test = new string("hello_world");  
  //custom_test->custom_data().push_back(hw_test.get());
  custom_test->custom_data().push_back((void *)(hw_test));
  cout << "testing\t" << *(string *)(custom_test->custom_data()[0]) << endl;
  menv->custom(custom_test);
  cout << "Assigned" << endl;
  h->microenvironment(menv); // Add the microenivronment to the main MultiCellDS elemebnt

  
  //############################################################
  // Adding metadata. Read it in from a file. Easier than
  // declaring all kinds of objects.
  //############################################################
  
  // Parse the metadata file.
  //
  MultiCellDS_paggr MultiCellDS_p;
  xml_schema::document_pimpl doc_p (MultiCellDS_p.root_parser (),
				    MultiCellDS_p.root_name ());
  MultiCellDS_p.pre ();
  
  // Adding metadata
  doc_p.parse("example_metadata.xml");
  MultiCellDS* h_meta = MultiCellDS_p.post ();

  // Update the created and last_modified_times
  //auto current_time = std::chrono::system_clock::now();
  std::time_t t = std::time(NULL);
  struct tm lt = *std::localtime(&t);
  // Handle timezones
  time_t offset_second(lt.tm_gmtoff);
  tm off_t = *std::gmtime(&offset_second);
  short timezone_hour = (off_t.tm_hour+12)%24-12, timezone_minute = off_t.tm_min;

  xml_schema::date_time new_times(lt.tm_year+1900, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min, lt.tm_sec, timezone_hour, timezone_minute);
  h_meta->metadata().created(new_times); // Copy time over
  h_meta->metadata().last_modified(new_times); // Copy time over
  h->metadata(&h_meta->metadata()); // Copy metadata over. Could also use _clone()
  
  // Setup for printing the MultiCellDS file
  MultiCellDS_saggr MultiCellDS_s;
  
  // doc_s is intended for printing to the screen
  // doc_s2 is intended for printing to a file

  // XSD/e setup for printing
  xml_schema::document_simpl doc_s (MultiCellDS_s.root_serializer (),
				    MultiCellDS_s.root_name ());
  //cout << "Going to write" << endl;

  try {
    // Initialization
    MultiCellDS_s.pre (*h);
    // Pick a file to write
    ofstream ofs("example.xml");
    // Print to the file
    doc_s.serialize (ofs, xml_schema::document_simpl::pretty_print);
    ofs << endl; // Add an extra newline at the end of the file
    // Cleanup of the writing
    MultiCellDS_s.post ();
    
    cout << "All done" << endl;
  }
  catch (std::exception const &exc)
    {
      std::cerr << "Exception caught " << exc.what() << "\n";
    }
  catch (...)
    {
      std::cerr << "Unknown exception caught\n";
    }
  
  return 0;
}
