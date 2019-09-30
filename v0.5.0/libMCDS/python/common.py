# libMCDS/python/common.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:94c8c21d08740f5da9eaa38d1f175c592692f0d1
# Generated 2016-11-27 21:16:28.664974 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace common [xmlns:common]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('common', create_if_missing=True)
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


# List simple type: {common}double_list
# superclasses pyxb.binding.datatypes.anySimpleType
class double_list (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.double."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'double_list')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 33, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.double
double_list._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'double_list', double_list)
_module_typeBindings.double_list = double_list

# List simple type: {common}unsigned_int_list
# superclasses pyxb.binding.datatypes.anySimpleType
class unsigned_int_list (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.unsignedInt."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unsigned_int_list')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 36, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.unsignedInt
unsigned_int_list._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'unsigned_int_list', unsigned_int_list)
_module_typeBindings.unsigned_int_list = unsigned_int_list

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 105, 4)
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.double(0.0))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {common}fraction
class fraction (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fraction')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 134, 4)
    _Documentation = None
fraction._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=fraction, value=pyxb.binding.datatypes.double(0.0))
fraction._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=fraction, value=pyxb.binding.datatypes.double(1.0))
fraction._InitializeFacetMap(fraction._CF_minInclusive,
   fraction._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'fraction', fraction)
_module_typeBindings.fraction = fraction

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 141, 4)
    _Documentation = None
STD_ANON_._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_, value=pyxb.binding.datatypes.double(0.0))
STD_ANON_._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_, value=pyxb.binding.datatypes.double(1.0))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minInclusive,
   STD_ANON_._CF_maxInclusive)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: {common}data_storage_formats
class data_storage_formats (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'data_storage_formats')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 163, 4)
    _Documentation = None
data_storage_formats._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=data_storage_formats, enum_prefix=None)
data_storage_formats.xml = data_storage_formats._CF_enumeration.addEnumeration(unicode_value='xml', tag='xml')
data_storage_formats.XML = data_storage_formats._CF_enumeration.addEnumeration(unicode_value='XML', tag='XML')
data_storage_formats.matlab = data_storage_formats._CF_enumeration.addEnumeration(unicode_value='matlab', tag='matlab')
data_storage_formats.Matlab = data_storage_formats._CF_enumeration.addEnumeration(unicode_value='Matlab', tag='Matlab')
data_storage_formats.MATLAB = data_storage_formats._CF_enumeration.addEnumeration(unicode_value='MATLAB', tag='MATLAB')
data_storage_formats.hdf5 = data_storage_formats._CF_enumeration.addEnumeration(unicode_value='hdf5', tag='hdf5')
data_storage_formats.HDF5 = data_storage_formats._CF_enumeration.addEnumeration(unicode_value='HDF5', tag='HDF5')
data_storage_formats._InitializeFacetMap(data_storage_formats._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'data_storage_formats', data_storage_formats)
_module_typeBindings.data_storage_formats = data_storage_formats

# Atomic simple type: {common}threshold_type
class threshold_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'threshold_type')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 208, 4)
    _Documentation = None
threshold_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=threshold_type, enum_prefix=None)
threshold_type.positive = threshold_type._CF_enumeration.addEnumeration(unicode_value='positive', tag='positive')
threshold_type.non_positive = threshold_type._CF_enumeration.addEnumeration(unicode_value='non_positive', tag='non_positive')
threshold_type.negative = threshold_type._CF_enumeration.addEnumeration(unicode_value='negative', tag='negative')
threshold_type.non_negative = threshold_type._CF_enumeration.addEnumeration(unicode_value='non_negative', tag='non_negative')
threshold_type.lower_bound = threshold_type._CF_enumeration.addEnumeration(unicode_value='lower_bound', tag='lower_bound')
threshold_type.upper_bound = threshold_type._CF_enumeration.addEnumeration(unicode_value='upper_bound', tag='upper_bound')
threshold_type._InitializeFacetMap(threshold_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'threshold_type', threshold_type)
_module_typeBindings.threshold_type = threshold_type

# List simple type: {common}two_doubles
# superclasses double_list
class two_doubles (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.double."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'two_doubles')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 39, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.double
two_doubles._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
two_doubles._InitializeFacetMap(two_doubles._CF_length)
Namespace.addCategoryObject('typeBinding', 'two_doubles', two_doubles)
_module_typeBindings.two_doubles = two_doubles

# Complex type {common}custom with content type MIXED
class custom (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {common}custom with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'custom')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 7, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.custom = custom
Namespace.addCategoryObject('typeBinding', 'custom', custom)


# Complex type {common}delimited_list with content type SIMPLE
class delimited_list (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {common}delimited_list with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'delimited_list')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 51, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute delimiter uses Python identifier delimiter
    __delimiter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'delimiter'), 'delimiter', '__common_delimited_list_delimiter', pyxb.binding.datatypes.string)
    __delimiter._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 54, 16)
    __delimiter._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 54, 16)
    
    delimiter = property(__delimiter.value, __delimiter.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __delimiter.name() : __delimiter
    })
_module_typeBindings.delimited_list = delimited_list
Namespace.addCategoryObject('typeBinding', 'delimited_list', delimited_list)


# Complex type {common}units_unsignedShort with content type SIMPLE
class units_unsignedShort (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {common}units_unsignedShort with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.unsignedShort
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'units_unsignedShort')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 114, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.unsignedShort
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__common_units_unsignedShort_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute measurement_type uses Python identifier measurement_type
    __measurement_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'measurement_type'), 'measurement_type', '__common_units_unsignedShort_measurement_type', pyxb.binding.datatypes.string)
    __measurement_type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 23, 8)
    __measurement_type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 23, 8)
    
    measurement_type = property(__measurement_type.value, __measurement_type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units,
        __measurement_type.name() : __measurement_type
    })
_module_typeBindings.units_unsignedShort = units_unsignedShort
Namespace.addCategoryObject('typeBinding', 'units_unsignedShort', units_unsignedShort)


# Complex type {common}units_boolean with content type SIMPLE
class units_boolean (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {common}units_boolean with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.boolean
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'units_boolean')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 124, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.boolean
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__common_units_boolean_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 127, 16)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 127, 16)
    
    units = property(__units.value, __units.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
_module_typeBindings.units_boolean = units_boolean
Namespace.addCategoryObject('typeBinding', 'units_boolean', units_boolean)


# Complex type {common}units_double_list with content type SIMPLE
class units_double_list (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {common}units_double_list with content type SIMPLE"""
    _TypeDefinition = double_list
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'units_double_list')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 44, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is double_list
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__common_units_double_list_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute measurement_type uses Python identifier measurement_type
    __measurement_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'measurement_type'), 'measurement_type', '__common_units_double_list_measurement_type', pyxb.binding.datatypes.string)
    __measurement_type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 23, 8)
    __measurement_type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 23, 8)
    
    measurement_type = property(__measurement_type.value, __measurement_type.set, None, None)

    
    # Attribute uncertainty uses Python identifier uncertainty
    __uncertainty = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uncertainty'), 'uncertainty', '__common_units_double_list_uncertainty', pyxb.binding.datatypes.double)
    __uncertainty._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 26, 8)
    __uncertainty._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 26, 8)
    
    uncertainty = property(__uncertainty.value, __uncertainty.set, None, None)

    
    # Attribute negative_uncertainty uses Python identifier negative_uncertainty
    __negative_uncertainty = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'negative_uncertainty'), 'negative_uncertainty', '__common_units_double_list_negative_uncertainty', pyxb.binding.datatypes.double)
    __negative_uncertainty._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 27, 8)
    __negative_uncertainty._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 27, 8)
    
    negative_uncertainty = property(__negative_uncertainty.value, __negative_uncertainty.set, None, None)

    
    # Attribute positive_uncertainty uses Python identifier positive_uncertainty
    __positive_uncertainty = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'positive_uncertainty'), 'positive_uncertainty', '__common_units_double_list_positive_uncertainty', pyxb.binding.datatypes.double)
    __positive_uncertainty._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 28, 8)
    __positive_uncertainty._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 28, 8)
    
    positive_uncertainty = property(__positive_uncertainty.value, __positive_uncertainty.set, None, None)

    
    # Attribute uncertainty_percentage uses Python identifier uncertainty_percentage
    __uncertainty_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uncertainty_percentage'), 'uncertainty_percentage', '__common_units_double_list_uncertainty_percentage', pyxb.binding.datatypes.double)
    __uncertainty_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 29, 8)
    __uncertainty_percentage._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 29, 8)
    
    uncertainty_percentage = property(__uncertainty_percentage.value, __uncertainty_percentage.set, None, None)

    
    # Attribute negative_uncertainty_percentage uses Python identifier negative_uncertainty_percentage
    __negative_uncertainty_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'negative_uncertainty_percentage'), 'negative_uncertainty_percentage', '__common_units_double_list_negative_uncertainty_percentage', pyxb.binding.datatypes.double)
    __negative_uncertainty_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 30, 8)
    __negative_uncertainty_percentage._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 30, 8)
    
    negative_uncertainty_percentage = property(__negative_uncertainty_percentage.value, __negative_uncertainty_percentage.set, None, None)

    
    # Attribute positive_uncertainty_percentage uses Python identifier positive_uncertainty_percentage
    __positive_uncertainty_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'positive_uncertainty_percentage'), 'positive_uncertainty_percentage', '__common_units_double_list_positive_uncertainty_percentage', pyxb.binding.datatypes.double)
    __positive_uncertainty_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 31, 8)
    __positive_uncertainty_percentage._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 31, 8)
    
    positive_uncertainty_percentage = property(__positive_uncertainty_percentage.value, __positive_uncertainty_percentage.set, None, None)

    
    # Attribute median uses Python identifier median
    __median = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'median'), 'median', '__common_units_double_list_median', pyxb.binding.datatypes.double)
    __median._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 66, 8)
    __median._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 66, 8)
    
    median = property(__median.value, __median.set, None, None)

    
    # Attribute standard_deviation uses Python identifier standard_deviation
    __standard_deviation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standard_deviation'), 'standard_deviation', '__common_units_double_list_standard_deviation', pyxb.binding.datatypes.double)
    __standard_deviation._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 67, 8)
    __standard_deviation._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 67, 8)
    
    standard_deviation = property(__standard_deviation.value, __standard_deviation.set, None, None)

    
    # Attribute interquartile_range uses Python identifier interquartile_range
    __interquartile_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'interquartile_range'), 'interquartile_range', '__common_units_double_list_interquartile_range', _module_typeBindings.two_doubles)
    __interquartile_range._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 68, 8)
    __interquartile_range._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 68, 8)
    
    interquartile_range = property(__interquartile_range.value, __interquartile_range.set, None, None)

    
    # Attribute range uses Python identifier range
    __range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'range'), 'range', '__common_units_double_list_range', _module_typeBindings.two_doubles)
    __range._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 69, 8)
    __range._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 69, 8)
    
    range = property(__range.value, __range.set, None, None)

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__common_units_double_list_min', pyxb.binding.datatypes.double)
    __min._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 70, 8)
    __min._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 70, 8)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__common_units_double_list_max', pyxb.binding.datatypes.double)
    __max._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 71, 8)
    __max._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 71, 8)
    
    max = property(__max.value, __max.set, None, None)

    
    # Attribute standard_error uses Python identifier standard_error
    __standard_error = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standard_error'), 'standard_error', '__common_units_double_list_standard_error', pyxb.binding.datatypes.double)
    __standard_error._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 72, 8)
    __standard_error._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 72, 8)
    
    standard_error = property(__standard_error.value, __standard_error.set, None, None)

    
    # Attribute standard_error_of_the_mean uses Python identifier standard_error_of_the_mean
    __standard_error_of_the_mean = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standard_error_of_the_mean'), 'standard_error_of_the_mean', '__common_units_double_list_standard_error_of_the_mean', pyxb.binding.datatypes.double)
    __standard_error_of_the_mean._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 73, 8)
    __standard_error_of_the_mean._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 73, 8)
    
    standard_error_of_the_mean = property(__standard_error_of_the_mean.value, __standard_error_of_the_mean.set, None, None)

    
    # Attribute number_obs uses Python identifier number_obs
    __number_obs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'number_obs'), 'number_obs', '__common_units_double_list_number_obs', pyxb.binding.datatypes.int)
    __number_obs._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 74, 8)
    __number_obs._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 74, 8)
    
    number_obs = property(__number_obs.value, __number_obs.set, None, None)

    
    # Attribute skewnesss uses Python identifier skewnesss
    __skewnesss = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'skewnesss'), 'skewnesss', '__common_units_double_list_skewnesss', pyxb.binding.datatypes.double)
    __skewnesss._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 75, 8)
    __skewnesss._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 75, 8)
    
    skewnesss = property(__skewnesss.value, __skewnesss.set, None, None)

    
    # Attribute kurtosis uses Python identifier kurtosis
    __kurtosis = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kurtosis'), 'kurtosis', '__common_units_double_list_kurtosis', pyxb.binding.datatypes.double)
    __kurtosis._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 76, 8)
    __kurtosis._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 76, 8)
    
    kurtosis = property(__kurtosis.value, __kurtosis.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units,
        __measurement_type.name() : __measurement_type,
        __uncertainty.name() : __uncertainty,
        __negative_uncertainty.name() : __negative_uncertainty,
        __positive_uncertainty.name() : __positive_uncertainty,
        __uncertainty_percentage.name() : __uncertainty_percentage,
        __negative_uncertainty_percentage.name() : __negative_uncertainty_percentage,
        __positive_uncertainty_percentage.name() : __positive_uncertainty_percentage,
        __median.name() : __median,
        __standard_deviation.name() : __standard_deviation,
        __interquartile_range.name() : __interquartile_range,
        __range.name() : __range,
        __min.name() : __min,
        __max.name() : __max,
        __standard_error.name() : __standard_error,
        __standard_error_of_the_mean.name() : __standard_error_of_the_mean,
        __number_obs.name() : __number_obs,
        __skewnesss.name() : __skewnesss,
        __kurtosis.name() : __kurtosis
    })
_module_typeBindings.units_double_list = units_double_list
Namespace.addCategoryObject('typeBinding', 'units_double_list', units_double_list)


# Complex type {common}units_delimited_list with content type SIMPLE
class units_delimited_list (delimited_list):
    """Complex type {common}units_delimited_list with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'units_delimited_list')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 58, 4)
    _ElementMap = delimited_list._ElementMap.copy()
    _AttributeMap = delimited_list._AttributeMap.copy()
    # Base type is delimited_list
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__common_units_delimited_list_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute measurement_type uses Python identifier measurement_type
    __measurement_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'measurement_type'), 'measurement_type', '__common_units_delimited_list_measurement_type', pyxb.binding.datatypes.string)
    __measurement_type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 23, 8)
    __measurement_type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 23, 8)
    
    measurement_type = property(__measurement_type.value, __measurement_type.set, None, None)

    
    # Attribute uncertainty uses Python identifier uncertainty
    __uncertainty = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uncertainty'), 'uncertainty', '__common_units_delimited_list_uncertainty', pyxb.binding.datatypes.double)
    __uncertainty._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 26, 8)
    __uncertainty._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 26, 8)
    
    uncertainty = property(__uncertainty.value, __uncertainty.set, None, None)

    
    # Attribute negative_uncertainty uses Python identifier negative_uncertainty
    __negative_uncertainty = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'negative_uncertainty'), 'negative_uncertainty', '__common_units_delimited_list_negative_uncertainty', pyxb.binding.datatypes.double)
    __negative_uncertainty._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 27, 8)
    __negative_uncertainty._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 27, 8)
    
    negative_uncertainty = property(__negative_uncertainty.value, __negative_uncertainty.set, None, None)

    
    # Attribute positive_uncertainty uses Python identifier positive_uncertainty
    __positive_uncertainty = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'positive_uncertainty'), 'positive_uncertainty', '__common_units_delimited_list_positive_uncertainty', pyxb.binding.datatypes.double)
    __positive_uncertainty._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 28, 8)
    __positive_uncertainty._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 28, 8)
    
    positive_uncertainty = property(__positive_uncertainty.value, __positive_uncertainty.set, None, None)

    
    # Attribute uncertainty_percentage uses Python identifier uncertainty_percentage
    __uncertainty_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uncertainty_percentage'), 'uncertainty_percentage', '__common_units_delimited_list_uncertainty_percentage', pyxb.binding.datatypes.double)
    __uncertainty_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 29, 8)
    __uncertainty_percentage._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 29, 8)
    
    uncertainty_percentage = property(__uncertainty_percentage.value, __uncertainty_percentage.set, None, None)

    
    # Attribute negative_uncertainty_percentage uses Python identifier negative_uncertainty_percentage
    __negative_uncertainty_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'negative_uncertainty_percentage'), 'negative_uncertainty_percentage', '__common_units_delimited_list_negative_uncertainty_percentage', pyxb.binding.datatypes.double)
    __negative_uncertainty_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 30, 8)
    __negative_uncertainty_percentage._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 30, 8)
    
    negative_uncertainty_percentage = property(__negative_uncertainty_percentage.value, __negative_uncertainty_percentage.set, None, None)

    
    # Attribute positive_uncertainty_percentage uses Python identifier positive_uncertainty_percentage
    __positive_uncertainty_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'positive_uncertainty_percentage'), 'positive_uncertainty_percentage', '__common_units_delimited_list_positive_uncertainty_percentage', pyxb.binding.datatypes.double)
    __positive_uncertainty_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 31, 8)
    __positive_uncertainty_percentage._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 31, 8)
    
    positive_uncertainty_percentage = property(__positive_uncertainty_percentage.value, __positive_uncertainty_percentage.set, None, None)

    
    # Attribute delimiter inherited from {common}delimited_list
    
    # Attribute median uses Python identifier median
    __median = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'median'), 'median', '__common_units_delimited_list_median', pyxb.binding.datatypes.double)
    __median._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 66, 8)
    __median._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 66, 8)
    
    median = property(__median.value, __median.set, None, None)

    
    # Attribute standard_deviation uses Python identifier standard_deviation
    __standard_deviation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standard_deviation'), 'standard_deviation', '__common_units_delimited_list_standard_deviation', pyxb.binding.datatypes.double)
    __standard_deviation._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 67, 8)
    __standard_deviation._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 67, 8)
    
    standard_deviation = property(__standard_deviation.value, __standard_deviation.set, None, None)

    
    # Attribute interquartile_range uses Python identifier interquartile_range
    __interquartile_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'interquartile_range'), 'interquartile_range', '__common_units_delimited_list_interquartile_range', _module_typeBindings.two_doubles)
    __interquartile_range._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 68, 8)
    __interquartile_range._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 68, 8)
    
    interquartile_range = property(__interquartile_range.value, __interquartile_range.set, None, None)

    
    # Attribute range uses Python identifier range
    __range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'range'), 'range', '__common_units_delimited_list_range', _module_typeBindings.two_doubles)
    __range._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 69, 8)
    __range._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 69, 8)
    
    range = property(__range.value, __range.set, None, None)

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__common_units_delimited_list_min', pyxb.binding.datatypes.double)
    __min._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 70, 8)
    __min._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 70, 8)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__common_units_delimited_list_max', pyxb.binding.datatypes.double)
    __max._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 71, 8)
    __max._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 71, 8)
    
    max = property(__max.value, __max.set, None, None)

    
    # Attribute standard_error uses Python identifier standard_error
    __standard_error = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standard_error'), 'standard_error', '__common_units_delimited_list_standard_error', pyxb.binding.datatypes.double)
    __standard_error._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 72, 8)
    __standard_error._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 72, 8)
    
    standard_error = property(__standard_error.value, __standard_error.set, None, None)

    
    # Attribute standard_error_of_the_mean uses Python identifier standard_error_of_the_mean
    __standard_error_of_the_mean = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standard_error_of_the_mean'), 'standard_error_of_the_mean', '__common_units_delimited_list_standard_error_of_the_mean', pyxb.binding.datatypes.double)
    __standard_error_of_the_mean._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 73, 8)
    __standard_error_of_the_mean._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 73, 8)
    
    standard_error_of_the_mean = property(__standard_error_of_the_mean.value, __standard_error_of_the_mean.set, None, None)

    
    # Attribute number_obs uses Python identifier number_obs
    __number_obs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'number_obs'), 'number_obs', '__common_units_delimited_list_number_obs', pyxb.binding.datatypes.int)
    __number_obs._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 74, 8)
    __number_obs._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 74, 8)
    
    number_obs = property(__number_obs.value, __number_obs.set, None, None)

    
    # Attribute skewnesss uses Python identifier skewnesss
    __skewnesss = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'skewnesss'), 'skewnesss', '__common_units_delimited_list_skewnesss', pyxb.binding.datatypes.double)
    __skewnesss._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 75, 8)
    __skewnesss._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 75, 8)
    
    skewnesss = property(__skewnesss.value, __skewnesss.set, None, None)

    
    # Attribute kurtosis uses Python identifier kurtosis
    __kurtosis = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kurtosis'), 'kurtosis', '__common_units_delimited_list_kurtosis', pyxb.binding.datatypes.double)
    __kurtosis._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 76, 8)
    __kurtosis._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 76, 8)
    
    kurtosis = property(__kurtosis.value, __kurtosis.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units,
        __measurement_type.name() : __measurement_type,
        __uncertainty.name() : __uncertainty,
        __negative_uncertainty.name() : __negative_uncertainty,
        __positive_uncertainty.name() : __positive_uncertainty,
        __uncertainty_percentage.name() : __uncertainty_percentage,
        __negative_uncertainty_percentage.name() : __negative_uncertainty_percentage,
        __positive_uncertainty_percentage.name() : __positive_uncertainty_percentage,
        __median.name() : __median,
        __standard_deviation.name() : __standard_deviation,
        __interquartile_range.name() : __interquartile_range,
        __range.name() : __range,
        __min.name() : __min,
        __max.name() : __max,
        __standard_error.name() : __standard_error,
        __standard_error_of_the_mean.name() : __standard_error_of_the_mean,
        __number_obs.name() : __number_obs,
        __skewnesss.name() : __skewnesss,
        __kurtosis.name() : __kurtosis
    })
_module_typeBindings.units_delimited_list = units_delimited_list
Namespace.addCategoryObject('typeBinding', 'units_delimited_list', units_delimited_list)


# Complex type {common}units_decimal with content type SIMPLE
class units_decimal (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {common}units_decimal with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'units_decimal')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 85, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__common_units_decimal_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute measurement_type uses Python identifier measurement_type
    __measurement_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'measurement_type'), 'measurement_type', '__common_units_decimal_measurement_type', pyxb.binding.datatypes.string)
    __measurement_type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 23, 8)
    __measurement_type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 23, 8)
    
    measurement_type = property(__measurement_type.value, __measurement_type.set, None, None)

    
    # Attribute uncertainty uses Python identifier uncertainty
    __uncertainty = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uncertainty'), 'uncertainty', '__common_units_decimal_uncertainty', pyxb.binding.datatypes.double)
    __uncertainty._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 26, 8)
    __uncertainty._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 26, 8)
    
    uncertainty = property(__uncertainty.value, __uncertainty.set, None, None)

    
    # Attribute negative_uncertainty uses Python identifier negative_uncertainty
    __negative_uncertainty = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'negative_uncertainty'), 'negative_uncertainty', '__common_units_decimal_negative_uncertainty', pyxb.binding.datatypes.double)
    __negative_uncertainty._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 27, 8)
    __negative_uncertainty._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 27, 8)
    
    negative_uncertainty = property(__negative_uncertainty.value, __negative_uncertainty.set, None, None)

    
    # Attribute positive_uncertainty uses Python identifier positive_uncertainty
    __positive_uncertainty = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'positive_uncertainty'), 'positive_uncertainty', '__common_units_decimal_positive_uncertainty', pyxb.binding.datatypes.double)
    __positive_uncertainty._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 28, 8)
    __positive_uncertainty._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 28, 8)
    
    positive_uncertainty = property(__positive_uncertainty.value, __positive_uncertainty.set, None, None)

    
    # Attribute uncertainty_percentage uses Python identifier uncertainty_percentage
    __uncertainty_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uncertainty_percentage'), 'uncertainty_percentage', '__common_units_decimal_uncertainty_percentage', pyxb.binding.datatypes.double)
    __uncertainty_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 29, 8)
    __uncertainty_percentage._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 29, 8)
    
    uncertainty_percentage = property(__uncertainty_percentage.value, __uncertainty_percentage.set, None, None)

    
    # Attribute negative_uncertainty_percentage uses Python identifier negative_uncertainty_percentage
    __negative_uncertainty_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'negative_uncertainty_percentage'), 'negative_uncertainty_percentage', '__common_units_decimal_negative_uncertainty_percentage', pyxb.binding.datatypes.double)
    __negative_uncertainty_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 30, 8)
    __negative_uncertainty_percentage._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 30, 8)
    
    negative_uncertainty_percentage = property(__negative_uncertainty_percentage.value, __negative_uncertainty_percentage.set, None, None)

    
    # Attribute positive_uncertainty_percentage uses Python identifier positive_uncertainty_percentage
    __positive_uncertainty_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'positive_uncertainty_percentage'), 'positive_uncertainty_percentage', '__common_units_decimal_positive_uncertainty_percentage', pyxb.binding.datatypes.double)
    __positive_uncertainty_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 31, 8)
    __positive_uncertainty_percentage._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 31, 8)
    
    positive_uncertainty_percentage = property(__positive_uncertainty_percentage.value, __positive_uncertainty_percentage.set, None, None)

    
    # Attribute median uses Python identifier median
    __median = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'median'), 'median', '__common_units_decimal_median', pyxb.binding.datatypes.double)
    __median._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 66, 8)
    __median._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 66, 8)
    
    median = property(__median.value, __median.set, None, None)

    
    # Attribute standard_deviation uses Python identifier standard_deviation
    __standard_deviation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standard_deviation'), 'standard_deviation', '__common_units_decimal_standard_deviation', pyxb.binding.datatypes.double)
    __standard_deviation._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 67, 8)
    __standard_deviation._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 67, 8)
    
    standard_deviation = property(__standard_deviation.value, __standard_deviation.set, None, None)

    
    # Attribute interquartile_range uses Python identifier interquartile_range
    __interquartile_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'interquartile_range'), 'interquartile_range', '__common_units_decimal_interquartile_range', _module_typeBindings.two_doubles)
    __interquartile_range._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 68, 8)
    __interquartile_range._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 68, 8)
    
    interquartile_range = property(__interquartile_range.value, __interquartile_range.set, None, None)

    
    # Attribute range uses Python identifier range
    __range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'range'), 'range', '__common_units_decimal_range', _module_typeBindings.two_doubles)
    __range._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 69, 8)
    __range._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 69, 8)
    
    range = property(__range.value, __range.set, None, None)

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__common_units_decimal_min', pyxb.binding.datatypes.double)
    __min._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 70, 8)
    __min._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 70, 8)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__common_units_decimal_max', pyxb.binding.datatypes.double)
    __max._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 71, 8)
    __max._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 71, 8)
    
    max = property(__max.value, __max.set, None, None)

    
    # Attribute standard_error uses Python identifier standard_error
    __standard_error = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standard_error'), 'standard_error', '__common_units_decimal_standard_error', pyxb.binding.datatypes.double)
    __standard_error._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 72, 8)
    __standard_error._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 72, 8)
    
    standard_error = property(__standard_error.value, __standard_error.set, None, None)

    
    # Attribute standard_error_of_the_mean uses Python identifier standard_error_of_the_mean
    __standard_error_of_the_mean = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standard_error_of_the_mean'), 'standard_error_of_the_mean', '__common_units_decimal_standard_error_of_the_mean', pyxb.binding.datatypes.double)
    __standard_error_of_the_mean._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 73, 8)
    __standard_error_of_the_mean._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 73, 8)
    
    standard_error_of_the_mean = property(__standard_error_of_the_mean.value, __standard_error_of_the_mean.set, None, None)

    
    # Attribute number_obs uses Python identifier number_obs
    __number_obs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'number_obs'), 'number_obs', '__common_units_decimal_number_obs', pyxb.binding.datatypes.int)
    __number_obs._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 74, 8)
    __number_obs._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 74, 8)
    
    number_obs = property(__number_obs.value, __number_obs.set, None, None)

    
    # Attribute skewnesss uses Python identifier skewnesss
    __skewnesss = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'skewnesss'), 'skewnesss', '__common_units_decimal_skewnesss', pyxb.binding.datatypes.double)
    __skewnesss._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 75, 8)
    __skewnesss._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 75, 8)
    
    skewnesss = property(__skewnesss.value, __skewnesss.set, None, None)

    
    # Attribute kurtosis uses Python identifier kurtosis
    __kurtosis = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kurtosis'), 'kurtosis', '__common_units_decimal_kurtosis', pyxb.binding.datatypes.double)
    __kurtosis._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 76, 8)
    __kurtosis._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 76, 8)
    
    kurtosis = property(__kurtosis.value, __kurtosis.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units,
        __measurement_type.name() : __measurement_type,
        __uncertainty.name() : __uncertainty,
        __negative_uncertainty.name() : __negative_uncertainty,
        __positive_uncertainty.name() : __positive_uncertainty,
        __uncertainty_percentage.name() : __uncertainty_percentage,
        __negative_uncertainty_percentage.name() : __negative_uncertainty_percentage,
        __positive_uncertainty_percentage.name() : __positive_uncertainty_percentage,
        __median.name() : __median,
        __standard_deviation.name() : __standard_deviation,
        __interquartile_range.name() : __interquartile_range,
        __range.name() : __range,
        __min.name() : __min,
        __max.name() : __max,
        __standard_error.name() : __standard_error,
        __standard_error_of_the_mean.name() : __standard_error_of_the_mean,
        __number_obs.name() : __number_obs,
        __skewnesss.name() : __skewnesss,
        __kurtosis.name() : __kurtosis
    })
_module_typeBindings.units_decimal = units_decimal
Namespace.addCategoryObject('typeBinding', 'units_decimal', units_decimal)


# Complex type {common}units_string with content type SIMPLE
class units_string (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {common}units_string with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'units_string')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 155, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__common_units_string_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute measurement_type uses Python identifier measurement_type
    __measurement_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'measurement_type'), 'measurement_type', '__common_units_string_measurement_type', pyxb.binding.datatypes.string)
    __measurement_type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 23, 8)
    __measurement_type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 23, 8)
    
    measurement_type = property(__measurement_type.value, __measurement_type.set, None, None)

    
    # Attribute uncertainty uses Python identifier uncertainty
    __uncertainty = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uncertainty'), 'uncertainty', '__common_units_string_uncertainty', pyxb.binding.datatypes.double)
    __uncertainty._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 26, 8)
    __uncertainty._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 26, 8)
    
    uncertainty = property(__uncertainty.value, __uncertainty.set, None, None)

    
    # Attribute negative_uncertainty uses Python identifier negative_uncertainty
    __negative_uncertainty = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'negative_uncertainty'), 'negative_uncertainty', '__common_units_string_negative_uncertainty', pyxb.binding.datatypes.double)
    __negative_uncertainty._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 27, 8)
    __negative_uncertainty._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 27, 8)
    
    negative_uncertainty = property(__negative_uncertainty.value, __negative_uncertainty.set, None, None)

    
    # Attribute positive_uncertainty uses Python identifier positive_uncertainty
    __positive_uncertainty = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'positive_uncertainty'), 'positive_uncertainty', '__common_units_string_positive_uncertainty', pyxb.binding.datatypes.double)
    __positive_uncertainty._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 28, 8)
    __positive_uncertainty._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 28, 8)
    
    positive_uncertainty = property(__positive_uncertainty.value, __positive_uncertainty.set, None, None)

    
    # Attribute uncertainty_percentage uses Python identifier uncertainty_percentage
    __uncertainty_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uncertainty_percentage'), 'uncertainty_percentage', '__common_units_string_uncertainty_percentage', pyxb.binding.datatypes.double)
    __uncertainty_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 29, 8)
    __uncertainty_percentage._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 29, 8)
    
    uncertainty_percentage = property(__uncertainty_percentage.value, __uncertainty_percentage.set, None, None)

    
    # Attribute negative_uncertainty_percentage uses Python identifier negative_uncertainty_percentage
    __negative_uncertainty_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'negative_uncertainty_percentage'), 'negative_uncertainty_percentage', '__common_units_string_negative_uncertainty_percentage', pyxb.binding.datatypes.double)
    __negative_uncertainty_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 30, 8)
    __negative_uncertainty_percentage._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 30, 8)
    
    negative_uncertainty_percentage = property(__negative_uncertainty_percentage.value, __negative_uncertainty_percentage.set, None, None)

    
    # Attribute positive_uncertainty_percentage uses Python identifier positive_uncertainty_percentage
    __positive_uncertainty_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'positive_uncertainty_percentage'), 'positive_uncertainty_percentage', '__common_units_string_positive_uncertainty_percentage', pyxb.binding.datatypes.double)
    __positive_uncertainty_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 31, 8)
    __positive_uncertainty_percentage._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 31, 8)
    
    positive_uncertainty_percentage = property(__positive_uncertainty_percentage.value, __positive_uncertainty_percentage.set, None, None)

    
    # Attribute median uses Python identifier median
    __median = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'median'), 'median', '__common_units_string_median', pyxb.binding.datatypes.double)
    __median._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 66, 8)
    __median._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 66, 8)
    
    median = property(__median.value, __median.set, None, None)

    
    # Attribute standard_deviation uses Python identifier standard_deviation
    __standard_deviation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standard_deviation'), 'standard_deviation', '__common_units_string_standard_deviation', pyxb.binding.datatypes.double)
    __standard_deviation._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 67, 8)
    __standard_deviation._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 67, 8)
    
    standard_deviation = property(__standard_deviation.value, __standard_deviation.set, None, None)

    
    # Attribute interquartile_range uses Python identifier interquartile_range
    __interquartile_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'interquartile_range'), 'interquartile_range', '__common_units_string_interquartile_range', _module_typeBindings.two_doubles)
    __interquartile_range._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 68, 8)
    __interquartile_range._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 68, 8)
    
    interquartile_range = property(__interquartile_range.value, __interquartile_range.set, None, None)

    
    # Attribute range uses Python identifier range
    __range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'range'), 'range', '__common_units_string_range', _module_typeBindings.two_doubles)
    __range._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 69, 8)
    __range._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 69, 8)
    
    range = property(__range.value, __range.set, None, None)

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__common_units_string_min', pyxb.binding.datatypes.double)
    __min._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 70, 8)
    __min._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 70, 8)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__common_units_string_max', pyxb.binding.datatypes.double)
    __max._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 71, 8)
    __max._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 71, 8)
    
    max = property(__max.value, __max.set, None, None)

    
    # Attribute standard_error uses Python identifier standard_error
    __standard_error = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standard_error'), 'standard_error', '__common_units_string_standard_error', pyxb.binding.datatypes.double)
    __standard_error._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 72, 8)
    __standard_error._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 72, 8)
    
    standard_error = property(__standard_error.value, __standard_error.set, None, None)

    
    # Attribute standard_error_of_the_mean uses Python identifier standard_error_of_the_mean
    __standard_error_of_the_mean = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standard_error_of_the_mean'), 'standard_error_of_the_mean', '__common_units_string_standard_error_of_the_mean', pyxb.binding.datatypes.double)
    __standard_error_of_the_mean._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 73, 8)
    __standard_error_of_the_mean._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 73, 8)
    
    standard_error_of_the_mean = property(__standard_error_of_the_mean.value, __standard_error_of_the_mean.set, None, None)

    
    # Attribute number_obs uses Python identifier number_obs
    __number_obs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'number_obs'), 'number_obs', '__common_units_string_number_obs', pyxb.binding.datatypes.int)
    __number_obs._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 74, 8)
    __number_obs._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 74, 8)
    
    number_obs = property(__number_obs.value, __number_obs.set, None, None)

    
    # Attribute skewnesss uses Python identifier skewnesss
    __skewnesss = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'skewnesss'), 'skewnesss', '__common_units_string_skewnesss', pyxb.binding.datatypes.double)
    __skewnesss._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 75, 8)
    __skewnesss._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 75, 8)
    
    skewnesss = property(__skewnesss.value, __skewnesss.set, None, None)

    
    # Attribute kurtosis uses Python identifier kurtosis
    __kurtosis = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kurtosis'), 'kurtosis', '__common_units_string_kurtosis', pyxb.binding.datatypes.double)
    __kurtosis._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 76, 8)
    __kurtosis._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 76, 8)
    
    kurtosis = property(__kurtosis.value, __kurtosis.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units,
        __measurement_type.name() : __measurement_type,
        __uncertainty.name() : __uncertainty,
        __negative_uncertainty.name() : __negative_uncertainty,
        __positive_uncertainty.name() : __positive_uncertainty,
        __uncertainty_percentage.name() : __uncertainty_percentage,
        __negative_uncertainty_percentage.name() : __negative_uncertainty_percentage,
        __positive_uncertainty_percentage.name() : __positive_uncertainty_percentage,
        __median.name() : __median,
        __standard_deviation.name() : __standard_deviation,
        __interquartile_range.name() : __interquartile_range,
        __range.name() : __range,
        __min.name() : __min,
        __max.name() : __max,
        __standard_error.name() : __standard_error,
        __standard_error_of_the_mean.name() : __standard_error_of_the_mean,
        __number_obs.name() : __number_obs,
        __skewnesss.name() : __skewnesss,
        __kurtosis.name() : __kurtosis
    })
_module_typeBindings.units_string = units_string
Namespace.addCategoryObject('typeBinding', 'units_string', units_string)


# Complex type {common}units_decimal_nonnegative with content type SIMPLE
class units_decimal_nonnegative (units_decimal):
    """Complex type {common}units_decimal_nonnegative with content type SIMPLE"""
    _TypeDefinition = STD_ANON
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'units_decimal_nonnegative')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 105, 4)
    _ElementMap = units_decimal._ElementMap.copy()
    _AttributeMap = units_decimal._AttributeMap.copy()
    # Base type is units_decimal
    
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
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.units_decimal_nonnegative = units_decimal_nonnegative
Namespace.addCategoryObject('typeBinding', 'units_decimal_nonnegative', units_decimal_nonnegative)


# Complex type {common}units_fraction with content type SIMPLE
class units_fraction (units_decimal):
    """Complex type {common}units_fraction with content type SIMPLE"""
    _TypeDefinition = STD_ANON_
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'units_fraction')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 141, 4)
    _ElementMap = units_decimal._ElementMap.copy()
    _AttributeMap = units_decimal._AttributeMap.copy()
    # Base type is units_decimal
    
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
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.units_fraction = units_fraction
Namespace.addCategoryObject('typeBinding', 'units_fraction', units_fraction)


# Complex type {common}transition_threshold with content type SIMPLE
class transition_threshold (units_decimal):
    """Complex type {common}transition_threshold with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'transition_threshold')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 176, 4)
    _ElementMap = units_decimal._ElementMap.copy()
    _AttributeMap = units_decimal._AttributeMap.copy()
    # Base type is units_decimal
    
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
    
    # Attribute quantity uses Python identifier quantity
    __quantity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'quantity'), 'quantity', '__common_transition_threshold_quantity', pyxb.binding.datatypes.string, required=True)
    __quantity._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 185, 8)
    __quantity._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 185, 8)
    
    quantity = property(__quantity.value, __quantity.set, None, '\n                    This should be the name of an element in MultiCellDS with possible XPATH \n                    or an ontology element identifier.\n                    \n                    Examples:\n                    //phenotype/mechanics/mechanical_pressure\n                    CBO:PressureMechanical\n                ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__common_transition_threshold_type', _module_typeBindings.threshold_type, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 197, 8)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 197, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute variable_ID uses Python identifier variable_ID
    __variable_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variable_ID'), 'variable_ID', '__common_transition_threshold_variable_ID', pyxb.binding.datatypes.unsignedLong)
    __variable_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 198, 8)
    __variable_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 198, 8)
    
    variable_ID = property(__variable_ID.value, __variable_ID.set, None, '\n                    This should reference the internal variable ID number (optional)\n                    Users can use a different ontology ID number like ChEBI.\n                ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __quantity.name() : __quantity,
        __type.name() : __type,
        __variable_ID.name() : __variable_ID
    })
_module_typeBindings.transition_threshold = transition_threshold
Namespace.addCategoryObject('typeBinding', 'transition_threshold', transition_threshold)




def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 9, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 9, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
custom._Automaton = _BuildAutomaton()

