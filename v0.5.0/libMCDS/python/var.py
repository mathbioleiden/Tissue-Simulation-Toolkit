# libMCDS/python/var.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:bc5af2310c7f15770a4ed0028648ce367e3e2ec0
# Generated 2016-11-27 21:16:28.665373 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace variables [xmlns:var]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('variables', create_if_missing=True)
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


# Atomic simple type: {variables}amount_type
class amount_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'amount_type')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 46, 4)
    _Documentation = None
amount_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=amount_type, enum_prefix=None)
amount_type.concentration = amount_type._CF_enumeration.addEnumeration(unicode_value='concentration', tag='concentration')
amount_type.density = amount_type._CF_enumeration.addEnumeration(unicode_value='density', tag='density')
amount_type.volume_fraction = amount_type._CF_enumeration.addEnumeration(unicode_value='volume_fraction', tag='volume_fraction')
amount_type.volume_percent = amount_type._CF_enumeration.addEnumeration(unicode_value='volume_percent', tag='volume_percent')
amount_type.volume_percentage = amount_type._CF_enumeration.addEnumeration(unicode_value='volume_percentage', tag='volume_percentage')
amount_type.surface_density = amount_type._CF_enumeration.addEnumeration(unicode_value='surface_density', tag='surface_density')
amount_type.area_fraction = amount_type._CF_enumeration.addEnumeration(unicode_value='area_fraction', tag='area_fraction')
amount_type.area_percent = amount_type._CF_enumeration.addEnumeration(unicode_value='area_percent', tag='area_percent')
amount_type.area_percentage = amount_type._CF_enumeration.addEnumeration(unicode_value='area_percentage', tag='area_percentage')
amount_type.count = amount_type._CF_enumeration.addEnumeration(unicode_value='count', tag='count')
amount_type.partial_pressure = amount_type._CF_enumeration.addEnumeration(unicode_value='partial_pressure', tag='partial_pressure')
amount_type.surface = amount_type._CF_enumeration.addEnumeration(unicode_value='surface', tag='surface')
amount_type._InitializeFacetMap(amount_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'amount_type', amount_type)
_module_typeBindings.amount_type = amount_type

# Atomic simple type: {variables}conditions
class conditions (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'conditions')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 111, 4)
    _Documentation = None
conditions._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=conditions, enum_prefix=None)
conditions.surface = conditions._CF_enumeration.addEnumeration(unicode_value='surface', tag='surface')
conditions.suspension = conditions._CF_enumeration.addEnumeration(unicode_value='suspension', tag='suspension')
conditions.spheroid = conditions._CF_enumeration.addEnumeration(unicode_value='spheroid', tag='spheroid')
conditions._InitializeFacetMap(conditions._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'conditions', conditions)
_module_typeBindings.conditions = conditions

# Atomic simple type: {variables}system
class system (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'system')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 119, 4)
    _Documentation = None
system._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=system, enum_prefix=None)
system.in_vivo = system._CF_enumeration.addEnumeration(unicode_value='in vivo', tag='in_vivo')
system.in_vitro = system._CF_enumeration.addEnumeration(unicode_value='in vitro', tag='in_vitro')
system.ex_vivo = system._CF_enumeration.addEnumeration(unicode_value='ex vivo', tag='ex_vivo')
system.in_silico = system._CF_enumeration.addEnumeration(unicode_value='in silico', tag='in_silico')
system._InitializeFacetMap(system._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'system', system)
_module_typeBindings.system = system

# Complex type {variables}physical_parameter_set with content type ELEMENT_ONLY
class physical_parameter_set (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {variables}physical_parameter_set with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'physical_parameter_set')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 82, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element conditions uses Python identifier conditions
    __conditions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'conditions'), 'conditions', '__variables_physical_parameter_set_conditions', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 84, 12), )

    
    conditions = property(__conditions.value, __conditions.set, None, None)

    
    # Element diffusion_coefficient uses Python identifier diffusion_coefficient
    __diffusion_coefficient = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'diffusion_coefficient'), 'diffusion_coefficient', '__variables_physical_parameter_set_diffusion_coefficient', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 85, 12), )

    
    diffusion_coefficient = property(__diffusion_coefficient.value, __diffusion_coefficient.set, None, None)

    
    # Element decay_rate uses Python identifier decay_rate
    __decay_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'decay_rate'), 'decay_rate', '__variables_physical_parameter_set_decay_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 86, 12), )

    
    decay_rate = property(__decay_rate.value, __decay_rate.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__variables_physical_parameter_set_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 87, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __conditions.name() : __conditions,
        __diffusion_coefficient.name() : __diffusion_coefficient,
        __decay_rate.name() : __decay_rate,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.physical_parameter_set = physical_parameter_set
Namespace.addCategoryObject('typeBinding', 'physical_parameter_set', physical_parameter_set)


# Complex type {variables}physical_conditions with content type ELEMENT_ONLY
class physical_conditions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {variables}physical_conditions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'physical_conditions')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 91, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element temperature uses Python identifier temperature
    __temperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'temperature'), 'temperature', '__variables_physical_conditions_temperature', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 93, 12), )

    
    temperature = property(__temperature.value, __temperature.set, None, None)

    
    # Element mechanical_pressure uses Python identifier mechanical_pressure
    __mechanical_pressure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mechanical_pressure'), 'mechanical_pressure', '__variables_physical_conditions_mechanical_pressure', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 94, 12), )

    
    mechanical_pressure = property(__mechanical_pressure.value, __mechanical_pressure.set, None, None)

    
    # Element acidity uses Python identifier acidity
    __acidity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'acidity'), 'acidity', '__variables_physical_conditions_acidity', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 95, 12), )

    
    acidity = property(__acidity.value, __acidity.set, None, None)

    
    # Element pH uses Python identifier pH
    __pH = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pH'), 'pH', '__variables_physical_conditions_pH', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 96, 12), )

    
    pH = property(__pH.value, __pH.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__variables_physical_conditions_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 97, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __temperature.name() : __temperature,
        __mechanical_pressure.name() : __mechanical_pressure,
        __acidity.name() : __acidity,
        __pH.name() : __pH,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.physical_conditions = physical_conditions
Namespace.addCategoryObject('typeBinding', 'physical_conditions', physical_conditions)


# Complex type {variables}experimental_conditions with content type ELEMENT_ONLY
class experimental_conditions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {variables}experimental_conditions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'experimental_conditions')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 101, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element dimensionality uses Python identifier dimensionality
    __dimensionality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dimensionality'), 'dimensionality', '__variables_experimental_conditions_dimensionality', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 103, 12), )

    
    dimensionality = property(__dimensionality.value, __dimensionality.set, None, None)

    
    # Element system uses Python identifier system
    __system = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'system'), 'system', '__variables_experimental_conditions_system', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 104, 12), )

    
    system = property(__system.value, __system.set, None, None)

    
    # Element conditions uses Python identifier conditions
    __conditions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'conditions'), 'conditions', '__variables_experimental_conditions_conditions', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 105, 12), )

    
    conditions = property(__conditions.value, __conditions.set, None, None)

    
    # Element surface_variable uses Python identifier surface_variable
    __surface_variable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'surface_variable'), 'surface_variable', '__variables_experimental_conditions_surface_variable', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 106, 12), )

    
    surface_variable = property(__surface_variable.value, __surface_variable.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__variables_experimental_conditions_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 108, 8)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 108, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __dimensionality.name() : __dimensionality,
        __system.name() : __system,
        __conditions.name() : __conditions,
        __surface_variable.name() : __surface_variable
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.experimental_conditions = experimental_conditions
Namespace.addCategoryObject('typeBinding', 'experimental_conditions', experimental_conditions)


# Complex type {variables}list_of_variables with content type ELEMENT_ONLY
class list_of_variables (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {variables}list_of_variables with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'list_of_variables')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 158, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element variable uses Python identifier variable
    __variable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'variable'), 'variable', '__variables_list_of_variables_variable', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 160, 12), )

    
    variable = property(__variable.value, __variable.set, None, None)

    
    # Element physical_parameter_set uses Python identifier physical_parameter_set
    __physical_parameter_set = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'physical_parameter_set'), 'physical_parameter_set', '__variables_list_of_variables_physical_parameter_set', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 161, 12), )

    
    physical_parameter_set = property(__physical_parameter_set.value, __physical_parameter_set.set, None, '\n                        There should only be one set of physical parameters / circumstances for each grouping \n                        of variables, but can be overridden in each individual vairable. \n                    ')

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__variables_list_of_variables_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 169, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __variable.name() : __variable,
        __physical_parameter_set.name() : __physical_parameter_set,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.list_of_variables = list_of_variables
Namespace.addCategoryObject('typeBinding', 'list_of_variables', list_of_variables)


# Complex type {variables}variable with content type ELEMENT_ONLY
class variable (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {variables}variable with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'variable')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 13, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element material_amount uses Python identifier material_amount
    __material_amount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'material_amount'), 'material_amount', '__variables_variable_material_amount', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 23, 12), )

    
    material_amount = property(__material_amount.value, __material_amount.set, None, None)

    
    # Element physical_parameter_set uses Python identifier physical_parameter_set
    __physical_parameter_set = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'physical_parameter_set'), 'physical_parameter_set', '__variables_variable_physical_parameter_set', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 24, 12), )

    
    physical_parameter_set = property(__physical_parameter_set.value, __physical_parameter_set.set, None, '\n                        There should only be one set of physical parameters / circumstances for a variable. \n                    ')

    
    # Attribute ChEBI_ID uses Python identifier ChEBI_ID
    __ChEBI_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ChEBI_ID'), 'ChEBI_ID', '__variables_variable_ChEBI_ID', pyxb.binding.datatypes.string)
    __ChEBI_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 65, 8)
    __ChEBI_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 65, 8)
    
    ChEBI_ID = property(__ChEBI_ID.value, __ChEBI_ID.set, None, None)

    
    # Attribute MeSH_ID uses Python identifier MeSH_ID
    __MeSH_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MeSH_ID'), 'MeSH_ID', '__variables_variable_MeSH_ID', pyxb.binding.datatypes.string)
    __MeSH_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 66, 8)
    __MeSH_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 66, 8)
    
    MeSH_ID = property(__MeSH_ID.value, __MeSH_ID.set, None, None)

    
    # Attribute DrugBank_ID uses Python identifier DrugBank_ID
    __DrugBank_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DrugBank_ID'), 'DrugBank_ID', '__variables_variable_DrugBank_ID', pyxb.binding.datatypes.string)
    __DrugBank_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 67, 8)
    __DrugBank_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 67, 8)
    
    DrugBank_ID = property(__DrugBank_ID.value, __DrugBank_ID.set, None, None)

    
    # Attribute GMO_ID uses Python identifier GMO_ID
    __GMO_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GMO_ID'), 'GMO_ID', '__variables_variable_GMO_ID', pyxb.binding.datatypes.string)
    __GMO_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 68, 8)
    __GMO_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 68, 8)
    
    GMO_ID = property(__GMO_ID.value, __GMO_ID.set, None, None)

    
    # Attribute GO_ID uses Python identifier GO_ID
    __GO_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GO_ID'), 'GO_ID', '__variables_variable_GO_ID', pyxb.binding.datatypes.string)
    __GO_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 69, 8)
    __GO_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 69, 8)
    
    GO_ID = property(__GO_ID.value, __GO_ID.set, None, None)

    
    # Attribute UniProt_ID uses Python identifier UniProt_ID
    __UniProt_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UniProt_ID'), 'UniProt_ID', '__variables_variable_UniProt_ID', pyxb.binding.datatypes.string)
    __UniProt_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 70, 8)
    __UniProt_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 70, 8)
    
    UniProt_ID = property(__UniProt_ID.value, __UniProt_ID.set, None, None)

    
    # Attribute PR_ID uses Python identifier PR_ID
    __PR_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PR_ID'), 'PR_ID', '__variables_variable_PR_ID', pyxb.binding.datatypes.string)
    __PR_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 71, 8)
    __PR_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 71, 8)
    
    PR_ID = property(__PR_ID.value, __PR_ID.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__variables_variable_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 75, 8)
    __name._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 75, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__variables_variable_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 76, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 76, 8)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__variables_variable_ID', pyxb.binding.datatypes.unsignedLong)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 77, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 77, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__variables_variable_type', _module_typeBindings.amount_type)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 78, 8)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 78, 8)
    
    type = property(__type.value, __type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __material_amount.name() : __material_amount,
        __physical_parameter_set.name() : __physical_parameter_set
    })
    _AttributeMap.update({
        __ChEBI_ID.name() : __ChEBI_ID,
        __MeSH_ID.name() : __MeSH_ID,
        __DrugBank_ID.name() : __DrugBank_ID,
        __GMO_ID.name() : __GMO_ID,
        __GO_ID.name() : __GO_ID,
        __UniProt_ID.name() : __UniProt_ID,
        __PR_ID.name() : __PR_ID,
        __name.name() : __name,
        __units.name() : __units,
        __ID.name() : __ID,
        __type.name() : __type
    })
_module_typeBindings.variable = variable
Namespace.addCategoryObject('typeBinding', 'variable', variable)


# Complex type {variables}data with content type ELEMENT_ONLY
class data (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {variables}data with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'data')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 149, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element filename uses Python identifier filename
    __filename = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'filename'), 'filename', '__variables_data_filename', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 151, 12), )

    
    filename = property(__filename.value, __filename.set, None, None)

    
    # Element data_vector uses Python identifier data_vector
    __data_vector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'data_vector'), 'data_vector', '__variables_data_data_vector', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 152, 12), )

    
    data_vector = property(__data_vector.value, __data_vector.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__variables_data_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 153, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__variables_data_type', _ImportedBinding_common.data_storage_formats)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 155, 8)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 155, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __filename.name() : __filename,
        __data_vector.name() : __data_vector,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.data = data
Namespace.addCategoryObject('typeBinding', 'data', data)


# Complex type {variables}material_amount with content type SIMPLE
class material_amount (_ImportedBinding_common.units_decimal):
    """Complex type {variables}material_amount with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'material_amount')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 37, 4)
    _ElementMap = _ImportedBinding_common.units_decimal._ElementMap.copy()
    _AttributeMap = _ImportedBinding_common.units_decimal._AttributeMap.copy()
    # Base type is _ImportedBinding_common.units_decimal
    
    # Attribute units inherited from {common}units_decimal
    
    # Attribute measurement_type inherited from {common}units_decimal
    
    # Attribute uncertainty inherited from {common}units_decimal
    
    # Attribute negative_uncertainty inherited from {common}units_decimal
    
    # Attribute positive_uncertainty inherited from {common}units_decimal
    
    # Attribute uncertainty_percentage inherited from {common}units_decimal
    
    # Attribute negative_uncertainty_percentage inherited from {common}units_decimal
    
    # Attribute positive_uncertainty_percentage inherited from {common}units_decimal
    
    # Attribute median inherited from {common}units_decimal
    
    # Attribute standard_deviation inherited from {common}units_decimal
    
    # Attribute interquartile_range inherited from {common}units_decimal
    
    # Attribute range inherited from {common}units_decimal
    
    # Attribute min inherited from {common}units_decimal
    
    # Attribute max inherited from {common}units_decimal
    
    # Attribute standard_error inherited from {common}units_decimal
    
    # Attribute standard_error_of_the_mean inherited from {common}units_decimal
    
    # Attribute number_obs inherited from {common}units_decimal
    
    # Attribute skewnesss inherited from {common}units_decimal
    
    # Attribute kurtosis inherited from {common}units_decimal
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__variables_material_amount_type', _module_typeBindings.amount_type)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 40, 16)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 40, 16)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute scale_units uses Python identifier scale_units
    __scale_units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scale_units'), 'scale_units', '__variables_material_amount_scale_units', pyxb.binding.datatypes.string)
    __scale_units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 41, 16)
    __scale_units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 41, 16)
    
    scale_units = property(__scale_units.value, __scale_units.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __scale_units.name() : __scale_units
    })
_module_typeBindings.material_amount = material_amount
Namespace.addCategoryObject('typeBinding', 'material_amount', material_amount)


# Complex type {variables}data_vector with content type SIMPLE
class data_vector (_ImportedBinding_common.units_double_list):
    """Complex type {variables}data_vector with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding_common.double_list
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'data_vector')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 141, 4)
    _ElementMap = _ImportedBinding_common.units_double_list._ElementMap.copy()
    _AttributeMap = _ImportedBinding_common.units_double_list._AttributeMap.copy()
    # Base type is _ImportedBinding_common.units_double_list
    
    # Attribute units inherited from {common}units_double_list
    
    # Attribute measurement_type inherited from {common}units_double_list
    
    # Attribute uncertainty inherited from {common}units_double_list
    
    # Attribute negative_uncertainty inherited from {common}units_double_list
    
    # Attribute positive_uncertainty inherited from {common}units_double_list
    
    # Attribute uncertainty_percentage inherited from {common}units_double_list
    
    # Attribute negative_uncertainty_percentage inherited from {common}units_double_list
    
    # Attribute positive_uncertainty_percentage inherited from {common}units_double_list
    
    # Attribute median inherited from {common}units_double_list
    
    # Attribute standard_deviation inherited from {common}units_double_list
    
    # Attribute interquartile_range inherited from {common}units_double_list
    
    # Attribute range inherited from {common}units_double_list
    
    # Attribute min inherited from {common}units_double_list
    
    # Attribute max inherited from {common}units_double_list
    
    # Attribute standard_error inherited from {common}units_double_list
    
    # Attribute standard_error_of_the_mean inherited from {common}units_double_list
    
    # Attribute number_obs inherited from {common}units_double_list
    
    # Attribute skewnesss inherited from {common}units_double_list
    
    # Attribute kurtosis inherited from {common}units_double_list
    
    # Attribute voxel_ID uses Python identifier voxel_ID
    __voxel_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'voxel_ID'), 'voxel_ID', '__variables_data_vector_voxel_ID', _ImportedBinding_common.unsigned_int_list)
    __voxel_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 144, 16)
    __voxel_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 144, 16)
    
    voxel_ID = property(__voxel_ID.value, __voxel_ID.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __voxel_ID.name() : __voxel_ID
    })
_module_typeBindings.data_vector = data_vector
Namespace.addCategoryObject('typeBinding', 'data_vector', data_vector)


# Complex type {variables}transition_threshold with content type SIMPLE
class transition_threshold (_ImportedBinding_common.transition_threshold):
    """Complex type {variables}transition_threshold with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'transition_threshold')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 173, 4)
    _ElementMap = _ImportedBinding_common.transition_threshold._ElementMap.copy()
    _AttributeMap = _ImportedBinding_common.transition_threshold._AttributeMap.copy()
    # Base type is _ImportedBinding_common.transition_threshold
    
    # Attribute units inherited from {common}units_decimal
    
    # Attribute measurement_type inherited from {common}units_decimal
    
    # Attribute uncertainty inherited from {common}units_decimal
    
    # Attribute negative_uncertainty inherited from {common}units_decimal
    
    # Attribute positive_uncertainty inherited from {common}units_decimal
    
    # Attribute uncertainty_percentage inherited from {common}units_decimal
    
    # Attribute negative_uncertainty_percentage inherited from {common}units_decimal
    
    # Attribute positive_uncertainty_percentage inherited from {common}units_decimal
    
    # Attribute median inherited from {common}units_decimal
    
    # Attribute standard_deviation inherited from {common}units_decimal
    
    # Attribute interquartile_range inherited from {common}units_decimal
    
    # Attribute range inherited from {common}units_decimal
    
    # Attribute min inherited from {common}units_decimal
    
    # Attribute max inherited from {common}units_decimal
    
    # Attribute standard_error inherited from {common}units_decimal
    
    # Attribute standard_error_of_the_mean inherited from {common}units_decimal
    
    # Attribute number_obs inherited from {common}units_decimal
    
    # Attribute skewnesss inherited from {common}units_decimal
    
    # Attribute kurtosis inherited from {common}units_decimal
    
    # Attribute quantity inherited from {common}transition_threshold
    
    # Attribute type inherited from {common}transition_threshold
    
    # Attribute variable_ID inherited from {common}transition_threshold
    
    # Attribute ChEBI_ID uses Python identifier ChEBI_ID
    __ChEBI_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ChEBI_ID'), 'ChEBI_ID', '__variables_transition_threshold_ChEBI_ID', pyxb.binding.datatypes.string)
    __ChEBI_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 65, 8)
    __ChEBI_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 65, 8)
    
    ChEBI_ID = property(__ChEBI_ID.value, __ChEBI_ID.set, None, None)

    
    # Attribute MeSH_ID uses Python identifier MeSH_ID
    __MeSH_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MeSH_ID'), 'MeSH_ID', '__variables_transition_threshold_MeSH_ID', pyxb.binding.datatypes.string)
    __MeSH_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 66, 8)
    __MeSH_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 66, 8)
    
    MeSH_ID = property(__MeSH_ID.value, __MeSH_ID.set, None, None)

    
    # Attribute DrugBank_ID uses Python identifier DrugBank_ID
    __DrugBank_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DrugBank_ID'), 'DrugBank_ID', '__variables_transition_threshold_DrugBank_ID', pyxb.binding.datatypes.string)
    __DrugBank_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 67, 8)
    __DrugBank_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 67, 8)
    
    DrugBank_ID = property(__DrugBank_ID.value, __DrugBank_ID.set, None, None)

    
    # Attribute GMO_ID uses Python identifier GMO_ID
    __GMO_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GMO_ID'), 'GMO_ID', '__variables_transition_threshold_GMO_ID', pyxb.binding.datatypes.string)
    __GMO_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 68, 8)
    __GMO_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 68, 8)
    
    GMO_ID = property(__GMO_ID.value, __GMO_ID.set, None, None)

    
    # Attribute GO_ID uses Python identifier GO_ID
    __GO_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GO_ID'), 'GO_ID', '__variables_transition_threshold_GO_ID', pyxb.binding.datatypes.string)
    __GO_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 69, 8)
    __GO_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 69, 8)
    
    GO_ID = property(__GO_ID.value, __GO_ID.set, None, None)

    
    # Attribute UniProt_ID uses Python identifier UniProt_ID
    __UniProt_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UniProt_ID'), 'UniProt_ID', '__variables_transition_threshold_UniProt_ID', pyxb.binding.datatypes.string)
    __UniProt_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 70, 8)
    __UniProt_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 70, 8)
    
    UniProt_ID = property(__UniProt_ID.value, __UniProt_ID.set, None, None)

    
    # Attribute PR_ID uses Python identifier PR_ID
    __PR_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PR_ID'), 'PR_ID', '__variables_transition_threshold_PR_ID', pyxb.binding.datatypes.string)
    __PR_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 71, 8)
    __PR_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 71, 8)
    
    PR_ID = property(__PR_ID.value, __PR_ID.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ChEBI_ID.name() : __ChEBI_ID,
        __MeSH_ID.name() : __MeSH_ID,
        __DrugBank_ID.name() : __DrugBank_ID,
        __GMO_ID.name() : __GMO_ID,
        __GO_ID.name() : __GO_ID,
        __UniProt_ID.name() : __UniProt_ID,
        __PR_ID.name() : __PR_ID
    })
_module_typeBindings.transition_threshold = transition_threshold
Namespace.addCategoryObject('typeBinding', 'transition_threshold', transition_threshold)




physical_parameter_set._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'conditions'), physical_conditions, scope=physical_parameter_set, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 84, 12)))

physical_parameter_set._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'diffusion_coefficient'), _ImportedBinding_common.units_decimal, scope=physical_parameter_set, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 85, 12)))

physical_parameter_set._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'decay_rate'), _ImportedBinding_common.units_decimal, scope=physical_parameter_set, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 86, 12)))

physical_parameter_set._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=physical_parameter_set, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 87, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 84, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(physical_parameter_set._UseForTag(pyxb.namespace.ExpandedName(None, 'conditions')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 84, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 85, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(physical_parameter_set._UseForTag(pyxb.namespace.ExpandedName(None, 'diffusion_coefficient')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 85, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 86, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(physical_parameter_set._UseForTag(pyxb.namespace.ExpandedName(None, 'decay_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 86, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 87, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(physical_parameter_set._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 87, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 84, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 85, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 86, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 87, 12))
    counters.add(cc_3)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    sub_automata.append(_BuildAutomaton_4())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 83, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
physical_parameter_set._Automaton = _BuildAutomaton()




physical_conditions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'temperature'), _ImportedBinding_common.units_decimal, scope=physical_conditions, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 93, 12)))

physical_conditions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mechanical_pressure'), _ImportedBinding_common.units_decimal, scope=physical_conditions, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 94, 12)))

physical_conditions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'acidity'), _ImportedBinding_common.units_decimal, scope=physical_conditions, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 95, 12)))

physical_conditions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pH'), _ImportedBinding_common.units_decimal, scope=physical_conditions, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 96, 12)))

physical_conditions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=physical_conditions, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 97, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 93, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(physical_conditions._UseForTag(pyxb.namespace.ExpandedName(None, 'temperature')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 93, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 94, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(physical_conditions._UseForTag(pyxb.namespace.ExpandedName(None, 'mechanical_pressure')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 94, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 95, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(physical_conditions._UseForTag(pyxb.namespace.ExpandedName(None, 'acidity')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 95, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 96, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(physical_conditions._UseForTag(pyxb.namespace.ExpandedName(None, 'pH')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 96, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 97, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(physical_conditions._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 97, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 93, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 94, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 95, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 96, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 97, 12))
    counters.add(cc_4)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_6())
    sub_automata.append(_BuildAutomaton_7())
    sub_automata.append(_BuildAutomaton_8())
    sub_automata.append(_BuildAutomaton_9())
    sub_automata.append(_BuildAutomaton_10())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 92, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
physical_conditions._Automaton = _BuildAutomaton_5()




experimental_conditions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dimensionality'), pyxb.binding.datatypes.unsignedShort, scope=experimental_conditions, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 103, 12)))

experimental_conditions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'system'), system, scope=experimental_conditions, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 104, 12)))

experimental_conditions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'conditions'), conditions, scope=experimental_conditions, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 105, 12)))

experimental_conditions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'surface_variable'), variable, scope=experimental_conditions, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 106, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 103, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 104, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 105, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 106, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(experimental_conditions._UseForTag(pyxb.namespace.ExpandedName(None, 'dimensionality')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 103, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(experimental_conditions._UseForTag(pyxb.namespace.ExpandedName(None, 'system')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 104, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(experimental_conditions._UseForTag(pyxb.namespace.ExpandedName(None, 'conditions')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 105, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(experimental_conditions._UseForTag(pyxb.namespace.ExpandedName(None, 'surface_variable')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 106, 12))
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
experimental_conditions._Automaton = _BuildAutomaton_11()




list_of_variables._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'variable'), variable, scope=list_of_variables, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 160, 12)))

list_of_variables._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'physical_parameter_set'), physical_parameter_set, scope=list_of_variables, documentation='\n                        There should only be one set of physical parameters / circumstances for each grouping \n                        of variables, but can be overridden in each individual vairable. \n                    ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 161, 12)))

list_of_variables._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=list_of_variables, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 169, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 161, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 169, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(list_of_variables._UseForTag(pyxb.namespace.ExpandedName(None, 'variable')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 160, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(list_of_variables._UseForTag(pyxb.namespace.ExpandedName(None, 'physical_parameter_set')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 161, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(list_of_variables._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 169, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
list_of_variables._Automaton = _BuildAutomaton_12()




variable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'material_amount'), material_amount, scope=variable, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 23, 12)))

variable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'physical_parameter_set'), physical_parameter_set, scope=variable, documentation='\n                        There should only be one set of physical parameters / circumstances for a variable. \n                    ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 24, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 23, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 24, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(variable._UseForTag(pyxb.namespace.ExpandedName(None, 'material_amount')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 23, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(variable._UseForTag(pyxb.namespace.ExpandedName(None, 'physical_parameter_set')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 24, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
variable._Automaton = _BuildAutomaton_13()




data._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'filename'), pyxb.binding.datatypes.string, scope=data, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 151, 12)))

data._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'data_vector'), data_vector, scope=data, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 152, 12)))

data._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=data, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 153, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 151, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 152, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 153, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(data._UseForTag(pyxb.namespace.ExpandedName(None, 'filename')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 151, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(data._UseForTag(pyxb.namespace.ExpandedName(None, 'data_vector')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 152, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(data._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 153, 12))
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
data._Automaton = _BuildAutomaton_14()

