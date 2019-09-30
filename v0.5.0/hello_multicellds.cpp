#include <iostream>
#include <fstream>
#include <string>

#include "MultiCellDS.hpp"
#include "MultiCellDS-pimpl.hpp"
#include "MultiCellDS-simpl.hpp"
#include "cell_cycle.hpp"

using namespace std;

// Usage: mcds_hello filename.xml

int main (int argc, char* argv[]) {
  try {
    // Parse.
    //
    MultiCellDS_paggr MultiCellDS_p;
    xml_schema::document_pimpl doc_p (MultiCellDS_p.root_parser (),
                                      MultiCellDS_p.root_name ());
    MultiCellDS_p.pre ();
    doc_p.parse (argv[1]);
    MultiCellDS* h = MultiCellDS_p.post ();
    //cell_cycle_phase* ccp_p;
    //phenotype_dataset* pds_p;

    // Change the greeting phrase.
    //
    //h->greeting ("Hi");
    //cout << h->cell_line().begin()->phenotype_dataset().begin()->phenotype().cell_death().duration() << endl;

    h->cell_line().begin()->phenotype_dataset().begin()->phenotype().begin()->cell_death().begin()->duration().base_value() = (230.0);

    auto pds_p = h->cell_line().begin()->phenotype_dataset().begin();
    
    while(pds_p->keywords() != "normoxic")
      pds_p++;

    //auto phenotype = pds_p->phenotype();
    auto cell_cycles_p = &(*(pds_p->phenotype().begin()->cell_cycle().begin())); //.cell_cycle_phase().begin();

    while(cell_cycles_p->model() != "Ki67_advanced")
      cell_cycles_p++;

    auto cell_cycle_phase = cell_cycles_p->cell_cycle_phase().begin();

    while(cell_cycle_phase->name() != "Ki67_postmitotic")
      cell_cycle_phase++;

    cout << "Duration measurement type: " <<     cell_cycle_phase->duration().measurement_type() << endl; 

    cell_cycle_phase->duration().measurement_type() = "problematic";

    cout << "Duration measurement type: " <<     cell_cycle_phase->duration().measurement_type() << endl; 
    
    // Add another entry to the name sequence.
    //
    //h->name ().push_back ("mars");

    // Serialize the modified object model to XML.
    //
    MultiCellDS_saggr MultiCellDS_s, MultiCellDS_s2;
    xml_schema::document_simpl doc_s (MultiCellDS_s.root_serializer (),
                                      MultiCellDS_s.root_name ());
    xml_schema::document_simpl doc_s2 (MultiCellDS_s2.root_serializer (),
                                      MultiCellDS_s2.root_name ());
    MultiCellDS_s.pre (*h);
    MultiCellDS_s2.pre (*h);
    ofstream ofs("blah.xml");
    //doc_s.serialize (cout, xml_schema::document_simpl::pretty_print);
    doc_s2.serialize (ofs, xml_schema::document_simpl::pretty_print);
    MultiCellDS_s.post ();
    MultiCellDS_s2.post ();

    delete h;
  }
  catch (const xml_schema::parser_exception& e)
  {
    cerr << argv[1] << ":" << e.line () << ":" << e.column ()
         << ": " << e.text () << endl;
    return 1;
  }
  catch (const xml_schema::serializer_exception& e)
  {
    cerr << "error: " << e.text () << endl;
    return 1;
  }
}
