# libMCDS/python/menv.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a5790c8a21be241e816b30ef3ed05db7a41180b2
# Generated 2016-11-29 16:42:21.906208 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace microenvironment [xmlns:menv]

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
import bm as _ImportedBinding_bm
import var as _ImportedBinding_var
import mesh as _ImportedBinding_mesh
import vas as _ImportedBinding_vas
import pyxb.binding.datatypes
import common as _ImportedBinding_common

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('microenvironment', create_if_missing=True)
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


# Complex type {microenvironment}domain with content type ELEMENT_ONLY
class domain (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {microenvironment}domain with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'domain')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 13, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element variables uses Python identifier variables
    __variables = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'variables'), 'variables', '__microenvironment_domain_variables', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 15, 12), )

    
    variables = property(__variables.value, __variables.set, None, '\n                        Should add Schematron warning if there are no variables\n                    ')

    
    # Element experimental_condition uses Python identifier experimental_condition
    __experimental_condition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'experimental_condition'), 'experimental_condition', '__microenvironment_domain_experimental_condition', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 22, 12), )

    
    experimental_condition = property(__experimental_condition.value, __experimental_condition.set, None, None)

    
    # Element mesh uses Python identifier mesh
    __mesh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mesh'), 'mesh', '__microenvironment_domain_mesh', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 23, 12), )

    
    mesh = property(__mesh.value, __mesh.set, None, None)

    
    # Element data uses Python identifier data
    __data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'data'), 'data', '__microenvironment_domain_data', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 24, 12), )

    
    data = property(__data.value, __data.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__microenvironment_domain_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 25, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__microenvironment_domain_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 28, 8)
    __name._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 28, 8)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __variables.name() : __variables,
        __experimental_condition.name() : __experimental_condition,
        __mesh.name() : __mesh,
        __data.name() : __data,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.domain = domain
Namespace.addCategoryObject('typeBinding', 'domain', domain)


# Complex type {microenvironment}microenvironment with content type ELEMENT_ONLY
class microenvironment (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {microenvironment}microenvironment with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'microenvironment')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 32, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element domain uses Python identifier domain
    __domain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'domain'), 'domain', '__microenvironment_microenvironment_domain', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 34, 12), )

    
    domain = property(__domain.value, __domain.set, None, None)

    
    # Element vascular_network uses Python identifier vascular_network
    __vascular_network = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vascular_network'), 'vascular_network', '__microenvironment_microenvironment_vascular_network', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 36, 12), )

    
    vascular_network = property(__vascular_network.value, __vascular_network.set, None, None)

    
    # Element basement_membrane uses Python identifier basement_membrane
    __basement_membrane = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'basement_membrane'), 'basement_membrane', '__microenvironment_microenvironment_basement_membrane', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 37, 12), )

    
    basement_membrane = property(__basement_membrane.value, __basement_membrane.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__microenvironment_microenvironment_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 38, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __domain.name() : __domain,
        __vascular_network.name() : __vascular_network,
        __basement_membrane.name() : __basement_membrane,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.microenvironment = microenvironment
Namespace.addCategoryObject('typeBinding', 'microenvironment', microenvironment)




domain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'variables'), _ImportedBinding_var.list_of_variables, scope=domain, documentation='\n                        Should add Schematron warning if there are no variables\n                    ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 15, 12)))

domain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'experimental_condition'), _ImportedBinding_var.experimental_conditions, scope=domain, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 22, 12)))

domain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mesh'), _ImportedBinding_mesh.mesh, scope=domain, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 23, 12)))

domain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'data'), _ImportedBinding_var.data, scope=domain, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 24, 12)))

domain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=domain, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 25, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 15, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(domain._UseForTag(pyxb.namespace.ExpandedName(None, 'variables')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 15, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 22, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(domain._UseForTag(pyxb.namespace.ExpandedName(None, 'experimental_condition')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 22, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 23, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(domain._UseForTag(pyxb.namespace.ExpandedName(None, 'mesh')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 23, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 24, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(domain._UseForTag(pyxb.namespace.ExpandedName(None, 'data')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 24, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 25, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(domain._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 25, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 15, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 22, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 23, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 24, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 25, 12))
    counters.add(cc_4)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 14, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
domain._Automaton = _BuildAutomaton()




microenvironment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'domain'), domain, scope=microenvironment, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 34, 12)))

microenvironment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vascular_network'), _ImportedBinding_vas.vascular_network, scope=microenvironment, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 36, 12)))

microenvironment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'basement_membrane'), _ImportedBinding_bm.basement_membrane, scope=microenvironment, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 37, 12)))

microenvironment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=microenvironment, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 38, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 34, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 36, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 37, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 38, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(microenvironment._UseForTag(pyxb.namespace.ExpandedName(None, 'domain')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 34, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(microenvironment._UseForTag(pyxb.namespace.ExpandedName(None, 'vascular_network')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 36, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(microenvironment._UseForTag(pyxb.namespace.ExpandedName(None, 'basement_membrane')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 37, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(microenvironment._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/microenvironment.xsd', 38, 12))
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
microenvironment._Automaton = _BuildAutomaton_6()

