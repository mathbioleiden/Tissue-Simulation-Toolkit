#!/usr/bin/python
#############################################################
#  Created by Samuel Friedman
#
#  This code is a sample for reading in a MultiCellXML file
#
#############################################################

import MultiCellDS

xml = open('temp.xml').read()
result = MultiCellDS.CreateFromDocument(xml)

print(result.cell_line[0].phenotype_dataset[1].phenotype[0].geometrical_properties.lengths.radius.value())

f = open('output.xml', 'w')
#f.write(result.toxml('utf-8'))
f.write(result.toDOM().toprettyxml())
