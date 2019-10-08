# libMCDS/python/_nsgroup.py
# -*- coding: utf-8 -*-
# PyXB bindings for NGM:974ccceaa29dbbcd18035a098a16f5b28ad68d8c
# Generated 2016-11-29 16:42:21.918985 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Group contents:
# Namespace cell_cycle [xmlns:cc]
# Namespace phenotype [xmlns:p]
# Namespace phenotype_base [xmlns:pbase]


from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.utils.utility
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
import pkpd as _ImportedBinding_pkpd
import pc as _ImportedBinding_pc
import common as _ImportedBinding_common
import var as _ImportedBinding_var

# NOTE: All namespace declarations are reserved within the binding
_Namespace_cc = pyxb.namespace.NamespaceForURI('cell_cycle', create_if_missing=True)
_Namespace_cc.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_pbase = pyxb.namespace.NamespaceForURI('phenotype_base', create_if_missing=True)
_Namespace_pbase.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_p = pyxb.namespace.NamespaceForURI('phenotype', create_if_missing=True)
_Namespace_p.configureCategories(['typeBinding', 'elementBinding'])

# Atomic simple type: {cell_cycle}death_type
class death_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cc, 'death_type')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 106, 4)
    _Documentation = None
death_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=death_type, enum_prefix=None)
death_type.apoptosis = death_type._CF_enumeration.addEnumeration(unicode_value='apoptosis', tag='apoptosis')
death_type.necrosis = death_type._CF_enumeration.addEnumeration(unicode_value='necrosis', tag='necrosis')
death_type.autophagy = death_type._CF_enumeration.addEnumeration(unicode_value='autophagy', tag='autophagy')
death_type._InitializeFacetMap(death_type._CF_enumeration)
_Namespace_cc.addCategoryObject('typeBinding', 'death_type', death_type)
_module_typeBindings.death_type = death_type

# Atomic simple type: {cell_cycle}arrest_type
class arrest_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cc, 'arrest_type')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 123, 4)
    _Documentation = None
arrest_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=arrest_type, enum_prefix=None)
arrest_type.maximum_cell_density = arrest_type._CF_enumeration.addEnumeration(unicode_value='maximum_cell_density', tag='maximum_cell_density')
arrest_type.maximum_cell_surface_density = arrest_type._CF_enumeration.addEnumeration(unicode_value='maximum_cell_surface_density', tag='maximum_cell_surface_density')
arrest_type.maximum_cell_volume_density = arrest_type._CF_enumeration.addEnumeration(unicode_value='maximum_cell_volume_density', tag='maximum_cell_volume_density')
arrest_type.maximum_cell_number = arrest_type._CF_enumeration.addEnumeration(unicode_value='maximum_cell_number', tag='maximum_cell_number')
arrest_type.maximum_volume_fraction = arrest_type._CF_enumeration.addEnumeration(unicode_value='maximum_volume_fraction', tag='maximum_volume_fraction')
arrest_type.maximum_area_fraction = arrest_type._CF_enumeration.addEnumeration(unicode_value='maximum_area_fraction', tag='maximum_area_fraction')
arrest_type._InitializeFacetMap(arrest_type._CF_enumeration)
_Namespace_cc.addCategoryObject('typeBinding', 'arrest_type', arrest_type)
_module_typeBindings.arrest_type = arrest_type

# Atomic simple type: {phenotype_base}phenotype_type
class phenotype_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_pbase, 'phenotype_type')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 76, 4)
    _Documentation = None
phenotype_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=phenotype_type, enum_prefix=None)
phenotype_type.expected = phenotype_type._CF_enumeration.addEnumeration(unicode_value='expected', tag='expected')
phenotype_type.current = phenotype_type._CF_enumeration.addEnumeration(unicode_value='current', tag='current')
phenotype_type.target = phenotype_type._CF_enumeration.addEnumeration(unicode_value='target', tag='target')
phenotype_type._InitializeFacetMap(phenotype_type._CF_enumeration)
_Namespace_pbase.addCategoryObject('typeBinding', 'phenotype_type', phenotype_type)
_module_typeBindings.phenotype_type = phenotype_type

# Complex type {cell_cycle}cell_cycle_arrest with content type ELEMENT_ONLY
class cell_cycle_arrest (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {cell_cycle}cell_cycle_arrest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cc, 'cell_cycle_arrest')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 30, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element condition uses Python identifier condition
    __condition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'condition'), 'condition', '__cell_cycle_cell_cycle_arrest_condition', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 32, 12), )

    
    condition = property(__condition.value, __condition.set, None, None)

    _ElementMap.update({
        __condition.name() : __condition
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.cell_cycle_arrest = cell_cycle_arrest
_Namespace_cc.addCategoryObject('typeBinding', 'cell_cycle_arrest', cell_cycle_arrest)


# Complex type {cell_cycle}transition with content type ELEMENT_ONLY
class transition (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {cell_cycle}transition with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cc, 'transition')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 36, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element checkpoint_failure_probability uses Python identifier checkpoint_failure_probability
    __checkpoint_failure_probability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'checkpoint_failure_probability'), 'checkpoint_failure_probability', '__cell_cycle_transition_checkpoint_failure_probability', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 38, 12), )

    
    checkpoint_failure_probability = property(__checkpoint_failure_probability.value, __checkpoint_failure_probability.set, None, None)

    
    # Element subsequent_phase uses Python identifier subsequent_phase
    __subsequent_phase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'subsequent_phase'), 'subsequent_phase', '__cell_cycle_transition_subsequent_phase', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 39, 12), )

    
    subsequent_phase = property(__subsequent_phase.value, __subsequent_phase.set, None, None)

    
    # Element threshold uses Python identifier threshold
    __threshold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'threshold'), 'threshold', '__cell_cycle_transition_threshold', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 40, 12), )

    
    threshold = property(__threshold.value, __threshold.set, None, None)

    
    # Element transition_rate uses Python identifier transition_rate
    __transition_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transition_rate'), 'transition_rate', '__cell_cycle_transition_transition_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 41, 12), )

    
    transition_rate = property(__transition_rate.value, __transition_rate.set, None, None)

    _ElementMap.update({
        __checkpoint_failure_probability.name() : __checkpoint_failure_probability,
        __subsequent_phase.name() : __subsequent_phase,
        __threshold.name() : __threshold,
        __transition_rate.name() : __transition_rate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.transition = transition
_Namespace_cc.addCategoryObject('typeBinding', 'transition', transition)


# Complex type {cell_cycle}cell_cycle_phase with content type ELEMENT_ONLY
class cell_cycle_phase (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {cell_cycle}cell_cycle_phase with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cc, 'cell_cycle_phase')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 45, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element birth_rate uses Python identifier birth_rate
    __birth_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'birth_rate'), 'birth_rate', '__cell_cycle_cell_cycle_phase_birth_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 13, 12), )

    
    birth_rate = property(__birth_rate.value, __birth_rate.set, None, None)

    
    # Element duration uses Python identifier duration
    __duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'duration'), 'duration', '__cell_cycle_cell_cycle_phase_duration', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 14, 12), )

    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Element death_rate uses Python identifier death_rate
    __death_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'death_rate'), 'death_rate', '__cell_cycle_cell_cycle_phase_death_rate', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 15, 12), )

    
    death_rate = property(__death_rate.value, __death_rate.set, None, None)

    
    # Element net_birth_rate uses Python identifier net_birth_rate
    __net_birth_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'net_birth_rate'), 'net_birth_rate', '__cell_cycle_cell_cycle_phase_net_birth_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 16, 12), )

    
    net_birth_rate = property(__net_birth_rate.value, __net_birth_rate.set, None, None)

    
    # Element population_doubling_time uses Python identifier population_doubling_time
    __population_doubling_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'population_doubling_time'), 'population_doubling_time', '__cell_cycle_cell_cycle_phase_population_doubling_time', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 17, 12), )

    
    population_doubling_time = property(__population_doubling_time.value, __population_doubling_time.set, None, None)

    
    # Element cell_cycle_arrest uses Python identifier cell_cycle_arrest
    __cell_cycle_arrest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_cycle_arrest'), 'cell_cycle_arrest', '__cell_cycle_cell_cycle_phase_cell_cycle_arrest', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 48, 12), )

    
    cell_cycle_arrest = property(__cell_cycle_arrest.value, __cell_cycle_arrest.set, None, None)

    
    # Element transition uses Python identifier transition
    __transition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transition'), 'transition', '__cell_cycle_cell_cycle_phase_transition', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 49, 12), )

    
    transition = property(__transition.value, __transition.set, None, None)

    
    # Element cell_part uses Python identifier cell_part
    __cell_part = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_part'), 'cell_part', '__cell_cycle_cell_cycle_phase_cell_part', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 50, 12), )

    
    cell_part = property(__cell_part.value, __cell_part.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__cell_cycle_cell_cycle_phase_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 51, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__cell_cycle_cell_cycle_phase_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 53, 8)
    __name._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 53, 8)
    
    name = property(__name.value, __name.set, None, '\n                    We should insert either Schematron or XML Schema 1.1 to verify that the name is part of the containing cell cycle model \n                ')

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__cell_cycle_cell_cycle_phase_ID', pyxb.binding.datatypes.unsignedLong)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 60, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 60, 8)
    
    ID = property(__ID.value, __ID.set, None, '\n                    The ID attribute SHOULD be used. It may become required in future versions of the Schema. It requires a unique ID in each XML file.\n                ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __birth_rate.name() : __birth_rate,
        __duration.name() : __duration,
        __death_rate.name() : __death_rate,
        __net_birth_rate.name() : __net_birth_rate,
        __population_doubling_time.name() : __population_doubling_time,
        __cell_cycle_arrest.name() : __cell_cycle_arrest,
        __transition.name() : __transition,
        __cell_part.name() : __cell_part,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __name.name() : __name,
        __ID.name() : __ID
    })
_module_typeBindings.cell_cycle_phase = cell_cycle_phase
_Namespace_cc.addCategoryObject('typeBinding', 'cell_cycle_phase', cell_cycle_phase)


# Complex type {cell_cycle}summary_elements with content type ELEMENT_ONLY
class summary_elements (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {cell_cycle}summary_elements with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cc, 'summary_elements')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 70, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element birth_rate uses Python identifier birth_rate
    __birth_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'birth_rate'), 'birth_rate', '__cell_cycle_summary_elements_birth_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 13, 12), )

    
    birth_rate = property(__birth_rate.value, __birth_rate.set, None, None)

    
    # Element duration uses Python identifier duration
    __duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'duration'), 'duration', '__cell_cycle_summary_elements_duration', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 14, 12), )

    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Element death_rate uses Python identifier death_rate
    __death_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'death_rate'), 'death_rate', '__cell_cycle_summary_elements_death_rate', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 15, 12), )

    
    death_rate = property(__death_rate.value, __death_rate.set, None, None)

    
    # Element net_birth_rate uses Python identifier net_birth_rate
    __net_birth_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'net_birth_rate'), 'net_birth_rate', '__cell_cycle_summary_elements_net_birth_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 16, 12), )

    
    net_birth_rate = property(__net_birth_rate.value, __net_birth_rate.set, None, None)

    
    # Element population_doubling_time uses Python identifier population_doubling_time
    __population_doubling_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'population_doubling_time'), 'population_doubling_time', '__cell_cycle_summary_elements_population_doubling_time', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 17, 12), )

    
    population_doubling_time = property(__population_doubling_time.value, __population_doubling_time.set, None, None)

    _ElementMap.update({
        __birth_rate.name() : __birth_rate,
        __duration.name() : __duration,
        __death_rate.name() : __death_rate,
        __net_birth_rate.name() : __net_birth_rate,
        __population_doubling_time.name() : __population_doubling_time
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.summary_elements = summary_elements
_Namespace_cc.addCategoryObject('typeBinding', 'summary_elements', summary_elements)


# Complex type {cell_cycle}cell_cycle with content type ELEMENT_ONLY
class cell_cycle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {cell_cycle}cell_cycle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cc, 'cell_cycle')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 74, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element cell_cycle_phase uses Python identifier cell_cycle_phase
    __cell_cycle_phase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_cycle_phase'), 'cell_cycle_phase', '__cell_cycle_cell_cycle_cell_cycle_phase', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 76, 12), )

    
    cell_cycle_phase = property(__cell_cycle_phase.value, __cell_cycle_phase.set, None, None)

    
    # Element cell_death uses Python identifier cell_death
    __cell_death = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_death'), 'cell_death', '__cell_cycle_cell_cycle_cell_death', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 77, 12), )

    
    cell_death = property(__cell_death.value, __cell_death.set, None, None)

    
    # Element summary_elements uses Python identifier summary_elements
    __summary_elements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'summary_elements'), 'summary_elements', '__cell_cycle_cell_cycle_summary_elements', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 78, 12), )

    
    summary_elements = property(__summary_elements.value, __summary_elements.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__cell_cycle_cell_cycle_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 79, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute model uses Python identifier model
    __model = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'model'), 'model', '__cell_cycle_cell_cycle_model', pyxb.binding.datatypes.string, required=True)
    __model._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 81, 8)
    __model._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 81, 8)
    
    model = property(__model.value, __model.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__cell_cycle_cell_cycle_ID', pyxb.binding.datatypes.unsignedLong)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 82, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 82, 8)
    
    ID = property(__ID.value, __ID.set, None, '\n                    The ID attribute SHOULD be used. It may become required in future versions of the Schema. It requires a unique ID in each XML file.\n                ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __cell_cycle_phase.name() : __cell_cycle_phase,
        __cell_death.name() : __cell_death,
        __summary_elements.name() : __summary_elements,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __model.name() : __model,
        __ID.name() : __ID
    })
_module_typeBindings.cell_cycle = cell_cycle
_Namespace_cc.addCategoryObject('typeBinding', 'cell_cycle', cell_cycle)


# Complex type {cell_cycle}cycles_and_deaths with content type ELEMENT_ONLY
class cycles_and_deaths (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {cell_cycle}cycles_and_deaths with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cc, 'cycles_and_deaths')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 135, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element cell_cycle uses Python identifier cell_cycle
    __cell_cycle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_cycle'), 'cell_cycle', '__cell_cycle_cycles_and_deaths_cell_cycle', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 137, 12), )

    
    cell_cycle = property(__cell_cycle.value, __cell_cycle.set, None, None)

    
    # Element cell_death uses Python identifier cell_death
    __cell_death = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_death'), 'cell_death', '__cell_cycle_cycles_and_deaths_cell_death', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 147, 12), )

    
    cell_death = property(__cell_death.value, __cell_death.set, None, None)

    _ElementMap.update({
        __cell_cycle.name() : __cell_cycle,
        __cell_death.name() : __cell_death
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.cycles_and_deaths = cycles_and_deaths
_Namespace_cc.addCategoryObject('typeBinding', 'cycles_and_deaths', cycles_and_deaths)


# Complex type {phenotype_base}cell_parts with content type ELEMENT_ONLY
class cell_parts (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_base}cell_parts with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_pbase, 'cell_parts')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 57, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element phenotype uses Python identifier phenotype
    __phenotype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'phenotype'), 'phenotype', '__phenotype_base_cell_parts_phenotype', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 59, 12), )

    
    phenotype = property(__phenotype.value, __phenotype.set, None, None)

    
    # Element cell_part uses Python identifier cell_part
    __cell_part = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_part'), 'cell_part', '__phenotype_base_cell_parts_cell_part', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 60, 12), )

    
    cell_part = property(__cell_part.value, __cell_part.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_base_cell_parts_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 61, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__phenotype_base_cell_parts_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 293, 8)
    __name._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 293, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__phenotype_base_cell_parts_ID', pyxb.binding.datatypes.unsignedInt)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 294, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 294, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __phenotype.name() : __phenotype,
        __cell_part.name() : __cell_part,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __name.name() : __name,
        __ID.name() : __ID
    })
_module_typeBindings.cell_parts = cell_parts
_Namespace_pbase.addCategoryObject('typeBinding', 'cell_parts', cell_parts)


# Complex type {cell_cycle}cell_death with content type ELEMENT_ONLY
class cell_death (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {cell_cycle}cell_death with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cc, 'cell_death')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 94, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element duration uses Python identifier duration
    __duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'duration'), 'duration', '__cell_cycle_cell_death_duration', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 96, 12), )

    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Element cell_part uses Python identifier cell_part
    __cell_part = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_part'), 'cell_part', '__cell_cycle_cell_death_cell_part', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 97, 12), )

    
    cell_part = property(__cell_part.value, __cell_part.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__cell_cycle_cell_death_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 98, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__cell_cycle_cell_death_type', _module_typeBindings.death_type, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 100, 8)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 100, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__cell_cycle_cell_death_ID', pyxb.binding.datatypes.unsignedLong)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 101, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 101, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __duration.name() : __duration,
        __cell_part.name() : __cell_part,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __type.name() : __type,
        __ID.name() : __ID
    })
_module_typeBindings.cell_death = cell_death
_Namespace_cc.addCategoryObject('typeBinding', 'cell_death', cell_death)


# Complex type {phenotype}phenotype_elements with content type ELEMENT_ONLY
class phenotype_elements (cycles_and_deaths):
    """Complex type {phenotype}phenotype_elements with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_p, 'phenotype_elements')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype.xsd', 12, 4)
    _ElementMap = cycles_and_deaths._ElementMap.copy()
    _AttributeMap = cycles_and_deaths._AttributeMap.copy()
    # Base type is cycles_and_deaths
    
    # Element cell_cycle (cell_cycle) inherited from {cell_cycle}cycles_and_deaths
    
    # Element cell_death (cell_death) inherited from {cell_cycle}cycles_and_deaths
    
    # Element adhesion uses Python identifier adhesion
    __adhesion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adhesion'), 'adhesion', '__phenotype_phenotype_elements_adhesion', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 19, 12), )

    
    adhesion = property(__adhesion.value, __adhesion.set, None, None)

    
    # Element geometrical_properties uses Python identifier geometrical_properties
    __geometrical_properties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometrical_properties'), 'geometrical_properties', '__phenotype_phenotype_elements_geometrical_properties', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 20, 12), )

    
    geometrical_properties = property(__geometrical_properties.value, __geometrical_properties.set, None, None)

    
    # Element mass uses Python identifier mass
    __mass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mass'), 'mass', '__phenotype_phenotype_elements_mass', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 22, 12), )

    
    mass = property(__mass.value, __mass.set, None, None)

    
    # Element mechanics uses Python identifier mechanics
    __mechanics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mechanics'), 'mechanics', '__phenotype_phenotype_elements_mechanics', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 23, 12), )

    
    mechanics = property(__mechanics.value, __mechanics.set, None, None)

    
    # Element motility uses Python identifier motility
    __motility = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'motility'), 'motility', '__phenotype_phenotype_elements_motility', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 24, 12), )

    
    motility = property(__motility.value, __motility.set, None, None)

    
    # Element PKPD uses Python identifier PKPD
    __PKPD = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PKPD'), 'PKPD', '__phenotype_phenotype_elements_PKPD', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 25, 12), )

    
    PKPD = property(__PKPD.value, __PKPD.set, None, None)

    
    # Element timescale uses Python identifier timescale
    __timescale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'timescale'), 'timescale', '__phenotype_phenotype_elements_timescale', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 35, 12), )

    
    timescale = property(__timescale.value, __timescale.set, None, '\n                        This element needs to be nillable, not have any "text" content, so as to permit use by only attributes\n                    ')

    
    # Element transport_processes uses Python identifier transport_processes
    __transport_processes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transport_processes'), 'transport_processes', '__phenotype_phenotype_elements_transport_processes', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 42, 12), )

    
    transport_processes = property(__transport_processes.value, __transport_processes.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_phenotype_elements_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 43, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __adhesion.name() : __adhesion,
        __geometrical_properties.name() : __geometrical_properties,
        __mass.name() : __mass,
        __mechanics.name() : __mechanics,
        __motility.name() : __motility,
        __PKPD.name() : __PKPD,
        __timescale.name() : __timescale,
        __transport_processes.name() : __transport_processes,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.phenotype_elements = phenotype_elements
_Namespace_p.addCategoryObject('typeBinding', 'phenotype_elements', phenotype_elements)


# Complex type {phenotype_base}phenotype_base with content type ELEMENT_ONLY
class phenotype_base (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_base}phenotype_base with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_pbase, 'phenotype_base')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 12, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element adhesion uses Python identifier adhesion
    __adhesion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adhesion'), 'adhesion', '__phenotype_base_phenotype_base_adhesion', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 19, 12), )

    
    adhesion = property(__adhesion.value, __adhesion.set, None, None)

    
    # Element geometrical_properties uses Python identifier geometrical_properties
    __geometrical_properties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometrical_properties'), 'geometrical_properties', '__phenotype_base_phenotype_base_geometrical_properties', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 20, 12), )

    
    geometrical_properties = property(__geometrical_properties.value, __geometrical_properties.set, None, None)

    
    # Element mass uses Python identifier mass
    __mass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mass'), 'mass', '__phenotype_base_phenotype_base_mass', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 22, 12), )

    
    mass = property(__mass.value, __mass.set, None, None)

    
    # Element mechanics uses Python identifier mechanics
    __mechanics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mechanics'), 'mechanics', '__phenotype_base_phenotype_base_mechanics', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 23, 12), )

    
    mechanics = property(__mechanics.value, __mechanics.set, None, None)

    
    # Element motility uses Python identifier motility
    __motility = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'motility'), 'motility', '__phenotype_base_phenotype_base_motility', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 24, 12), )

    
    motility = property(__motility.value, __motility.set, None, None)

    
    # Element PKPD uses Python identifier PKPD
    __PKPD = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PKPD'), 'PKPD', '__phenotype_base_phenotype_base_PKPD', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 25, 12), )

    
    PKPD = property(__PKPD.value, __PKPD.set, None, None)

    
    # Element timescale uses Python identifier timescale
    __timescale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'timescale'), 'timescale', '__phenotype_base_phenotype_base_timescale', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 35, 12), )

    
    timescale = property(__timescale.value, __timescale.set, None, '\n                        This element needs to be nillable, not have any "text" content, so as to permit use by only attributes\n                    ')

    
    # Element transport_processes uses Python identifier transport_processes
    __transport_processes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transport_processes'), 'transport_processes', '__phenotype_base_phenotype_base_transport_processes', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 42, 12), )

    
    transport_processes = property(__transport_processes.value, __transport_processes.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_base_phenotype_base_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 43, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__phenotype_base_phenotype_base_type', _module_typeBindings.phenotype_type)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 67, 8)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 67, 8)
    
    type = property(__type.value, __type.set, None, '\n                    Current is default assumed value\n                ')

    _ElementMap.update({
        __adhesion.name() : __adhesion,
        __geometrical_properties.name() : __geometrical_properties,
        __mass.name() : __mass,
        __mechanics.name() : __mechanics,
        __motility.name() : __motility,
        __PKPD.name() : __PKPD,
        __timescale.name() : __timescale,
        __transport_processes.name() : __transport_processes,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.phenotype_base = phenotype_base
_Namespace_pbase.addCategoryObject('typeBinding', 'phenotype_base', phenotype_base)


# Complex type {phenotype}phenotype with content type ELEMENT_ONLY
class phenotype (phenotype_elements):
    """Complex type {phenotype}phenotype with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_p, 'phenotype')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype.xsd', 32, 4)
    _ElementMap = phenotype_elements._ElementMap.copy()
    _AttributeMap = phenotype_elements._AttributeMap.copy()
    # Base type is phenotype_elements
    
    # Element cell_cycle (cell_cycle) inherited from {cell_cycle}cycles_and_deaths
    
    # Element cell_death (cell_death) inherited from {cell_cycle}cycles_and_deaths
    
    # Element adhesion (adhesion) inherited from {phenotype}phenotype_elements
    
    # Element geometrical_properties (geometrical_properties) inherited from {phenotype}phenotype_elements
    
    # Element mass (mass) inherited from {phenotype}phenotype_elements
    
    # Element mechanics (mechanics) inherited from {phenotype}phenotype_elements
    
    # Element motility (motility) inherited from {phenotype}phenotype_elements
    
    # Element PKPD (PKPD) inherited from {phenotype}phenotype_elements
    
    # Element timescale (timescale) inherited from {phenotype}phenotype_elements
    
    # Element transport_processes (transport_processes) inherited from {phenotype}phenotype_elements
    
    # Element custom (custom) inherited from {phenotype}phenotype_elements
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__phenotype_phenotype_type', _module_typeBindings.phenotype_type)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 67, 8)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 67, 8)
    
    type = property(__type.value, __type.set, None, '\n                    Current is default assumed value\n                ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.phenotype = phenotype
_Namespace_p.addCategoryObject('typeBinding', 'phenotype', phenotype)


# Complex type {cell_cycle}arrest_condition with content type SIMPLE
class arrest_condition (_ImportedBinding_common.units_decimal):
    """Complex type {cell_cycle}arrest_condition with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cc, 'arrest_condition')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 115, 4)
    _ElementMap = _ImportedBinding_common.units_decimal._ElementMap.copy()
    _AttributeMap = _ImportedBinding_common.units_decimal._AttributeMap.copy()
    # Base type is _ImportedBinding_common.units_decimal
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__cell_cycle_arrest_condition_type', _module_typeBindings.arrest_type)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 118, 16)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 118, 16)
    
    type = property(__type.value, __type.set, None, None)

    
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
        __type.name() : __type
    })
_module_typeBindings.arrest_condition = arrest_condition
_Namespace_cc.addCategoryObject('typeBinding', 'arrest_condition', arrest_condition)


# Complex type {cell_cycle}death_rate_type with content type SIMPLE
class death_rate_type (_ImportedBinding_common.units_decimal_nonnegative):
    """Complex type {cell_cycle}death_rate_type with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding_common.STD_ANON
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cc, 'death_rate_type')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 21, 4)
    _ElementMap = _ImportedBinding_common.units_decimal_nonnegative._ElementMap.copy()
    _AttributeMap = _ImportedBinding_common.units_decimal_nonnegative._AttributeMap.copy()
    # Base type is _ImportedBinding_common.units_decimal_nonnegative
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__cell_cycle_death_rate_type_type', _module_typeBindings.death_type, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 24, 16)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 24, 16)
    
    type = property(__type.value, __type.set, None, None)

    
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
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.death_rate_type = death_rate_type
_Namespace_cc.addCategoryObject('typeBinding', 'death_rate_type', death_rate_type)


# Complex type {phenotype_base}expected_timescale with content type SIMPLE
class expected_timescale (_ImportedBinding_common.units_decimal_nonnegative):
    """Complex type {phenotype_base}expected_timescale with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding_common.STD_ANON
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_pbase, 'expected_timescale')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 47, 4)
    _ElementMap = _ImportedBinding_common.units_decimal_nonnegative._ElementMap.copy()
    _AttributeMap = _ImportedBinding_common.units_decimal_nonnegative._AttributeMap.copy()
    # Base type is _ImportedBinding_common.units_decimal_nonnegative
    
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
    
    # Attribute cell_cycle_ID uses Python identifier cell_cycle_ID
    __cell_cycle_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cell_cycle_ID'), 'cell_cycle_ID', '__phenotype_base_expected_timescale_cell_cycle_ID', pyxb.binding.datatypes.unsignedInt)
    __cell_cycle_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 50, 16)
    __cell_cycle_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 50, 16)
    
    cell_cycle_ID = property(__cell_cycle_ID.value, __cell_cycle_ID.set, None, None)

    
    # Attribute cell_cycle_phase_ID uses Python identifier cell_cycle_phase_ID
    __cell_cycle_phase_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cell_cycle_phase_ID'), 'cell_cycle_phase_ID', '__phenotype_base_expected_timescale_cell_cycle_phase_ID', pyxb.binding.datatypes.unsignedInt)
    __cell_cycle_phase_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 51, 16)
    __cell_cycle_phase_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 51, 16)
    
    cell_cycle_phase_ID = property(__cell_cycle_phase_ID.value, __cell_cycle_phase_ID.set, None, None)

    
    # Attribute cell_death_ID uses Python identifier cell_death_ID
    __cell_death_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cell_death_ID'), 'cell_death_ID', '__phenotype_base_expected_timescale_cell_death_ID', pyxb.binding.datatypes.unsignedInt)
    __cell_death_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 52, 16)
    __cell_death_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 52, 16)
    
    cell_death_ID = property(__cell_death_ID.value, __cell_death_ID.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __cell_cycle_ID.name() : __cell_cycle_ID,
        __cell_cycle_phase_ID.name() : __cell_cycle_phase_ID,
        __cell_death_ID.name() : __cell_death_ID
    })
_module_typeBindings.expected_timescale = expected_timescale
_Namespace_pbase.addCategoryObject('typeBinding', 'expected_timescale', expected_timescale)




cell_cycle_arrest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'condition'), arrest_condition, scope=cell_cycle_arrest, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 32, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 32, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle_arrest._UseForTag(pyxb.namespace.ExpandedName(None, 'condition')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 32, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cell_cycle_arrest._Automaton = _BuildAutomaton()




transition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'checkpoint_failure_probability'), _ImportedBinding_common.units_decimal, scope=transition, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 38, 12)))

transition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'subsequent_phase'), pyxb.binding.datatypes.unsignedLong, scope=transition, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 39, 12)))

transition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'threshold'), _ImportedBinding_var.transition_threshold, scope=transition, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 40, 12)))

transition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transition_rate'), _ImportedBinding_common.units_decimal, scope=transition, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 41, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 38, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 39, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 40, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 41, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(transition._UseForTag(pyxb.namespace.ExpandedName(None, 'checkpoint_failure_probability')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 38, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(transition._UseForTag(pyxb.namespace.ExpandedName(None, 'subsequent_phase')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 39, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(transition._UseForTag(pyxb.namespace.ExpandedName(None, 'threshold')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 40, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(transition._UseForTag(pyxb.namespace.ExpandedName(None, 'transition_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 41, 12))
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
transition._Automaton = _BuildAutomaton_()




cell_cycle_phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'birth_rate'), _ImportedBinding_common.units_decimal_nonnegative, scope=cell_cycle_phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 13, 12)))

cell_cycle_phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'duration'), _ImportedBinding_common.units_decimal_nonnegative, scope=cell_cycle_phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 14, 12)))

cell_cycle_phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'death_rate'), death_rate_type, scope=cell_cycle_phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 15, 12)))

cell_cycle_phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'net_birth_rate'), _ImportedBinding_common.units_decimal, scope=cell_cycle_phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 16, 12)))

cell_cycle_phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'population_doubling_time'), _ImportedBinding_common.units_decimal_nonnegative, scope=cell_cycle_phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 17, 12)))

cell_cycle_phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_cycle_arrest'), cell_cycle_arrest, scope=cell_cycle_phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 48, 12)))

cell_cycle_phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transition'), transition, scope=cell_cycle_phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 49, 12)))

cell_cycle_phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_part'), cell_parts, scope=cell_cycle_phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 50, 12)))

cell_cycle_phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=cell_cycle_phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 51, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 13, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 14, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=3, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 15, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 48, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 49, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 50, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 51, 12))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle_phase._UseForTag(pyxb.namespace.ExpandedName(None, 'birth_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 13, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle_phase._UseForTag(pyxb.namespace.ExpandedName(None, 'duration')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 14, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle_phase._UseForTag(pyxb.namespace.ExpandedName(None, 'death_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 15, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle_phase._UseForTag(pyxb.namespace.ExpandedName(None, 'net_birth_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle_phase._UseForTag(pyxb.namespace.ExpandedName(None, 'population_doubling_time')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 17, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle_phase._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_cycle_arrest')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 48, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle_phase._UseForTag(pyxb.namespace.ExpandedName(None, 'transition')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 49, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle_phase._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_part')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 50, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle_phase._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 51, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cell_cycle_phase._Automaton = _BuildAutomaton_2()




summary_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'birth_rate'), _ImportedBinding_common.units_decimal_nonnegative, scope=summary_elements, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 13, 12)))

summary_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'duration'), _ImportedBinding_common.units_decimal_nonnegative, scope=summary_elements, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 14, 12)))

summary_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'death_rate'), death_rate_type, scope=summary_elements, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 15, 12)))

summary_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'net_birth_rate'), _ImportedBinding_common.units_decimal, scope=summary_elements, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 16, 12)))

summary_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'population_doubling_time'), _ImportedBinding_common.units_decimal_nonnegative, scope=summary_elements, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 17, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 13, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 14, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=3, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 15, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 17, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(summary_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'birth_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 13, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(summary_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'duration')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 14, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(summary_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'death_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 15, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(summary_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'net_birth_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(summary_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'population_doubling_time')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 17, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
summary_elements._Automaton = _BuildAutomaton_3()




cell_cycle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_cycle_phase'), cell_cycle_phase, scope=cell_cycle, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 76, 12)))

cell_cycle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_death'), cell_death, scope=cell_cycle, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 77, 12)))

cell_cycle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'summary_elements'), summary_elements, scope=cell_cycle, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 78, 12)))

cell_cycle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=cell_cycle, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 79, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 76, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 77, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 78, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 79, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_cycle_phase')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 76, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_death')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 77, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle._UseForTag(pyxb.namespace.ExpandedName(None, 'summary_elements')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 78, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cell_cycle._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 79, 12))
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
cell_cycle._Automaton = _BuildAutomaton_4()




cycles_and_deaths._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_cycle'), cell_cycle, scope=cycles_and_deaths, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 137, 12)))

cycles_and_deaths._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_death'), cell_death, scope=cycles_and_deaths, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 147, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 137, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 147, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cycles_and_deaths._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_cycle')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 137, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cycles_and_deaths._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_death')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 147, 12))
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
cycles_and_deaths._Automaton = _BuildAutomaton_5()




cell_parts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'phenotype'), phenotype_base, scope=cell_parts, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 59, 12)))

cell_parts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_part'), cell_parts, scope=cell_parts, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 60, 12)))

cell_parts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=cell_parts, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 61, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=3, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 59, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 60, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 61, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_parts._UseForTag(pyxb.namespace.ExpandedName(None, 'phenotype')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 59, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cell_parts._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_part')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 60, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cell_parts._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 61, 12))
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
cell_parts._Automaton = _BuildAutomaton_6()




cell_death._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'duration'), _ImportedBinding_common.units_decimal, scope=cell_death, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 96, 12)))

cell_death._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_part'), cell_parts, scope=cell_death, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 97, 12)))

cell_death._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=cell_death, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 98, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 97, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 98, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cell_death._UseForTag(pyxb.namespace.ExpandedName(None, 'duration')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 96, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_death._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_part')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 97, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cell_death._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 98, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
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
cell_death._Automaton = _BuildAutomaton_7()




phenotype_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adhesion'), _ImportedBinding_pc.adhesion, scope=phenotype_elements, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 19, 12)))

phenotype_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometrical_properties'), _ImportedBinding_pc.geometrical_properties, scope=phenotype_elements, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 20, 12)))

phenotype_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mass'), _ImportedBinding_pc.mass, scope=phenotype_elements, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 22, 12)))

phenotype_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mechanics'), _ImportedBinding_pc.mechanics, scope=phenotype_elements, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 23, 12)))

phenotype_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'motility'), _ImportedBinding_pc.motility, scope=phenotype_elements, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 24, 12)))

phenotype_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PKPD'), _ImportedBinding_pkpd.PKPD, scope=phenotype_elements, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 25, 12)))

phenotype_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'timescale'), expected_timescale, nillable=pyxb.binding.datatypes.boolean(1), scope=phenotype_elements, documentation='\n                        This element needs to be nillable, not have any "text" content, so as to permit use by only attributes\n                    ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 35, 12)))

phenotype_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transport_processes'), _ImportedBinding_pc.transport_processes, scope=phenotype_elements, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 42, 12)))

phenotype_elements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=phenotype_elements, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 43, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 137, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 147, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 19, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 20, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 22, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 23, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 24, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 25, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 35, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 42, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 43, 12))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_cycle')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 137, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_death')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 147, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'adhesion')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 19, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'geometrical_properties')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 20, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'mass')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 22, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'mechanics')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 23, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'motility')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 24, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'PKPD')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 25, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'timescale')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 35, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'transport_processes')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 42, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_elements._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 43, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
phenotype_elements._Automaton = _BuildAutomaton_8()




phenotype_base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adhesion'), _ImportedBinding_pc.adhesion, scope=phenotype_base, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 19, 12)))

phenotype_base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometrical_properties'), _ImportedBinding_pc.geometrical_properties, scope=phenotype_base, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 20, 12)))

phenotype_base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mass'), _ImportedBinding_pc.mass, scope=phenotype_base, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 22, 12)))

phenotype_base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mechanics'), _ImportedBinding_pc.mechanics, scope=phenotype_base, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 23, 12)))

phenotype_base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'motility'), _ImportedBinding_pc.motility, scope=phenotype_base, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 24, 12)))

phenotype_base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PKPD'), _ImportedBinding_pkpd.PKPD, scope=phenotype_base, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 25, 12)))

phenotype_base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'timescale'), expected_timescale, nillable=pyxb.binding.datatypes.boolean(1), scope=phenotype_base, documentation='\n                        This element needs to be nillable, not have any "text" content, so as to permit use by only attributes\n                    ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 35, 12)))

phenotype_base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transport_processes'), _ImportedBinding_pc.transport_processes, scope=phenotype_base, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 42, 12)))

phenotype_base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=phenotype_base, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 43, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 19, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 20, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 22, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 23, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 24, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 25, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 35, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 42, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 43, 12))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_base._UseForTag(pyxb.namespace.ExpandedName(None, 'adhesion')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 19, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_base._UseForTag(pyxb.namespace.ExpandedName(None, 'geometrical_properties')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 20, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_base._UseForTag(pyxb.namespace.ExpandedName(None, 'mass')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 22, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_base._UseForTag(pyxb.namespace.ExpandedName(None, 'mechanics')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 23, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_base._UseForTag(pyxb.namespace.ExpandedName(None, 'motility')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 24, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_base._UseForTag(pyxb.namespace.ExpandedName(None, 'PKPD')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 25, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_base._UseForTag(pyxb.namespace.ExpandedName(None, 'timescale')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 35, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_base._UseForTag(pyxb.namespace.ExpandedName(None, 'transport_processes')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 42, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(phenotype_base._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 43, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
phenotype_base._Automaton = _BuildAutomaton_9()




def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 137, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 147, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 19, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 20, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 22, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 23, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 24, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 25, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 35, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 42, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 43, 12))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(phenotype._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_cycle')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 137, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(phenotype._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_death')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/cell_cycle.xsd', 147, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(phenotype._UseForTag(pyxb.namespace.ExpandedName(None, 'adhesion')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 19, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(phenotype._UseForTag(pyxb.namespace.ExpandedName(None, 'geometrical_properties')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 20, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(phenotype._UseForTag(pyxb.namespace.ExpandedName(None, 'mass')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 22, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(phenotype._UseForTag(pyxb.namespace.ExpandedName(None, 'mechanics')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 23, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(phenotype._UseForTag(pyxb.namespace.ExpandedName(None, 'motility')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 24, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(phenotype._UseForTag(pyxb.namespace.ExpandedName(None, 'PKPD')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 25, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(phenotype._UseForTag(pyxb.namespace.ExpandedName(None, 'timescale')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 35, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(phenotype._UseForTag(pyxb.namespace.ExpandedName(None, 'transport_processes')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 42, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(phenotype._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_base.xsd', 43, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
phenotype._Automaton = _BuildAutomaton_10()

