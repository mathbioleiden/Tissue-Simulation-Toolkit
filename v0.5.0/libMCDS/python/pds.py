# libMCDS/python/pds.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b2446027374ad48566470101163507cf023e1307
# Generated 2016-11-27 21:16:28.668948 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace phenotype_dataset [xmlns:pds]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d081bdce-b529-11e6-8dd4-0800272323b7')

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
import menv as _ImportedBinding_menv
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('phenotype_dataset', create_if_missing=True)
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


# Complex type {phenotype_dataset}phenotype_dataset with content type ELEMENT_ONLY
class phenotype_dataset (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_dataset}phenotype_dataset with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phenotype_dataset')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 14, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element microenvironment uses Python identifier microenvironment
    __microenvironment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'microenvironment'), 'microenvironment', '__phenotype_dataset_phenotype_dataset_microenvironment', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 16, 12), )

    
    microenvironment = property(__microenvironment.value, __microenvironment.set, None, None)

    
    # Element phenotype uses Python identifier phenotype
    __phenotype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'phenotype'), 'phenotype', '__phenotype_dataset_phenotype_dataset_phenotype', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 17, 12), )

    
    phenotype = property(__phenotype.value, __phenotype.set, None, None)

    
    # Element cell_part uses Python identifier cell_part
    __cell_part = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_part'), 'cell_part', '__phenotype_dataset_phenotype_dataset_cell_part', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 31, 12), )

    
    cell_part = property(__cell_part.value, __cell_part.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_dataset_phenotype_dataset_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 32, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute keywords uses Python identifier keywords
    __keywords = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'keywords'), 'keywords', '__phenotype_dataset_phenotype_dataset_keywords', pyxb.binding.datatypes.string)
    __keywords._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 34, 8)
    __keywords._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 34, 8)
    
    keywords = property(__keywords.value, __keywords.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__phenotype_dataset_phenotype_dataset_ID', pyxb.binding.datatypes.unsignedLong)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 35, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 35, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __microenvironment.name() : __microenvironment,
        __phenotype.name() : __phenotype,
        __cell_part.name() : __cell_part,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __keywords.name() : __keywords,
        __ID.name() : __ID
    })
_module_typeBindings.phenotype_dataset = phenotype_dataset
Namespace.addCategoryObject('typeBinding', 'phenotype_dataset', phenotype_dataset)




phenotype_dataset._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'microenvironment'), _ImportedBinding_menv.microenvironment, scope=phenotype_dataset, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 16, 12)))

phenotype_dataset._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'phenotype'), _ImportedBinding__nsgroup.phenotype, scope=phenotype_dataset, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 17, 12)))

phenotype_dataset._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_part'), _ImportedBinding__nsgroup.cell_parts, scope=phenotype_dataset, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 31, 12)))

phenotype_dataset._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=phenotype_dataset, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 32, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 16, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=3, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 17, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 31, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 32, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_dataset._UseForTag(pyxb.namespace.ExpandedName(None, 'microenvironment')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 16, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_dataset._UseForTag(pyxb.namespace.ExpandedName(None, 'phenotype')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 17, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_dataset._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_part')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 31, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_dataset._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_dataset.xsd', 32, 12))
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
phenotype_dataset._Automaton = _BuildAutomaton()

