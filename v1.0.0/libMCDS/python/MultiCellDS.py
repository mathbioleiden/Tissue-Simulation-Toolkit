# libMCDS/python/MultiCellDS.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2016-11-29 16:42:21.936432 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace AbsentNamespace0

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
import menv as _ImportedBinding_menv
import pyxb.binding.datatypes
import cell as _ImportedBinding_cell
import dcl as _ImportedBinding_dcl
import meta as _ImportedBinding_meta

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
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


# Atomic simple type: MCDS_type
class MCDS_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MCDS_type')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 62, 2)
    _Documentation = None
MCDS_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MCDS_type, enum_prefix=None)
MCDS_type.cell_line = MCDS_type._CF_enumeration.addEnumeration(unicode_value='cell_line', tag='cell_line')
MCDS_type.snapshotsimulation = MCDS_type._CF_enumeration.addEnumeration(unicode_value='snapshot/simulation', tag='snapshotsimulation')
MCDS_type.snapshotexperiment = MCDS_type._CF_enumeration.addEnumeration(unicode_value='snapshot/experiment', tag='snapshotexperiment')
MCDS_type.snapshotclinical = MCDS_type._CF_enumeration.addEnumeration(unicode_value='snapshot/clinical', tag='snapshotclinical')
MCDS_type._InitializeFacetMap(MCDS_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MCDS_type', MCDS_type)
_module_typeBindings.MCDS_type = MCDS_type

# Complex type MultiCellDS with content type ELEMENT_ONLY
class MultiCellDS_ (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiCellDS')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 36, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element cell_line uses Python identifier cell_line
    __cell_line = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_line'), 'cell_line', '__AbsentNamespace0_MultiCellDS__cell_line', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 47, 6), )

    
    cell_line = property(__cell_line.value, __cell_line.set, None, None)

    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__AbsentNamespace0_MultiCellDS__metadata', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 53, 6), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element microenvironment uses Python identifier microenvironment
    __microenvironment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'microenvironment'), 'microenvironment', '__AbsentNamespace0_MultiCellDS__microenvironment', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 54, 6), )

    
    microenvironment = property(__microenvironment.value, __microenvironment.set, None, None)

    
    # Element cellular_information uses Python identifier cellular_information
    __cellular_information = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cellular_information'), 'cellular_information', '__AbsentNamespace0_MultiCellDS__cellular_information', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 56, 6), )

    
    cellular_information = property(__cellular_information.value, __cellular_information.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_MultiCellDS__version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 58, 4)
    __version._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 58, 4)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_MultiCellDS__type', _module_typeBindings.MCDS_type)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 59, 4)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 59, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __cell_line.name() : __cell_line,
        __metadata.name() : __metadata,
        __microenvironment.name() : __microenvironment,
        __cellular_information.name() : __cellular_information
    })
    _AttributeMap.update({
        __version.name() : __version,
        __type.name() : __type
    })
_module_typeBindings.MultiCellDS_ = MultiCellDS_
Namespace.addCategoryObject('typeBinding', 'MultiCellDS', MultiCellDS_)


MultiCellDS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MultiCellDS'), MultiCellDS_, documentation='', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 71, 2))
Namespace.addCategoryObject('elementBinding', MultiCellDS.name().localName(), MultiCellDS)



MultiCellDS_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_line'), _ImportedBinding_dcl.cell_line, scope=MultiCellDS_, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 47, 6)))

MultiCellDS_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), _ImportedBinding_meta.metadata, scope=MultiCellDS_, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 53, 6)))

MultiCellDS_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'microenvironment'), _ImportedBinding_menv.microenvironment, scope=MultiCellDS_, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 54, 6)))

MultiCellDS_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cellular_information'), _ImportedBinding_cell.cellular_information, scope=MultiCellDS_, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 56, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 47, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 53, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 54, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 56, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MultiCellDS_._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_line')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 47, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MultiCellDS_._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 53, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MultiCellDS_._UseForTag(pyxb.namespace.ExpandedName(None, 'microenvironment')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 54, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MultiCellDS_._UseForTag(pyxb.namespace.ExpandedName(None, 'cellular_information')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/MultiCellDS.xsd', 56, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MultiCellDS_._Automaton = _BuildAutomaton()

