# libMCDS/python/dcl.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:85785ad52411ddec7f30524bbbe84872dbc88e5c
# Generated 2016-11-29 16:42:21.933040 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace cell_line [xmlns:dcl]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:da1167f0-b695-11e6-8a8c-0800272323b7')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import common as _ImportedBinding_common
import meta as _ImportedBinding_meta
import pds as _ImportedBinding_pds

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('cell_line', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {cell_line}cell_line with content type ELEMENT_ONLY
class cell_line (pyxb.binding.basis.complexTypeDefinition):
    """
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cell_line')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 16, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__cell_line_cell_line_metadata', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 27, 12), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element phenotype_dataset uses Python identifier phenotype_dataset
    __phenotype_dataset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'phenotype_dataset'), 'phenotype_dataset', '__cell_line_cell_line_phenotype_dataset', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 28, 12), )

    
    phenotype_dataset = property(__phenotype_dataset.value, __phenotype_dataset.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__cell_line_cell_line_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 31, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__cell_line_cell_line_ID', pyxb.binding.datatypes.string)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 46, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 46, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__cell_line_cell_line_label', pyxb.binding.datatypes.string)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 47, 8)
    __label._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 47, 8)
    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute curated uses Python identifier curated
    __curated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'curated'), 'curated', '__cell_line_cell_line_curated', pyxb.binding.datatypes.boolean)
    __curated._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 48, 8)
    __curated._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 48, 8)
    
    curated = property(__curated.value, __curated.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __phenotype_dataset.name() : __phenotype_dataset,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __ID.name() : __ID,
        __label.name() : __label,
        __curated.name() : __curated
    })
_module_typeBindings.cell_line = cell_line
Namespace.addCategoryObject('typeBinding', 'cell_line', cell_line)


# Complex type {cell_line}DCLs with content type ELEMENT_ONLY
class DCLs (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {cell_line}DCLs with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DCLs')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 79, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element cell_line uses Python identifier cell_line
    __cell_line = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_line'), 'cell_line', '__cell_line_DCLs_cell_line', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 67, 12), )

    
    cell_line = property(__cell_line.value, __cell_line.set, None, None)

    _ElementMap.update({
        __cell_line.name() : __cell_line
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DCLs = DCLs
Namespace.addCategoryObject('typeBinding', 'DCLs', DCLs)




cell_line._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), _ImportedBinding_meta.metadata, scope=cell_line, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 27, 12)))

cell_line._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'phenotype_dataset'), _ImportedBinding_pds.phenotype_dataset, scope=cell_line, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 28, 12)))

cell_line._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=cell_line, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 31, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 27, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 28, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 31, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_line._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 27, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cell_line._UseForTag(pyxb.namespace.ExpandedName(None, 'phenotype_dataset')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 28, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cell_line._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 31, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cell_line._Automaton = _BuildAutomaton()




DCLs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_line'), cell_line, scope=DCLs, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 67, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DCLs._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_line')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_line.xsd', 67, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DCLs._Automaton = _BuildAutomaton_()

