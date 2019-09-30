# libMCDS/python/pkpd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a8992307f6e93435a2056554e4634cd39e2a55b9
# Generated 2016-11-27 21:16:28.665913 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace pkpd [xmlns:pkpd]

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
Namespace = pyxb.namespace.NamespaceForURI('pkpd', create_if_missing=True)
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


# Complex type {pkpd}pharmacokinetics with content type ELEMENT_ONLY
class pharmacokinetics (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {pkpd}pharmacokinetics with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pharmacokinetics')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 18, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element inactivation_rate uses Python identifier inactivation_rate
    __inactivation_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inactivation_rate'), 'inactivation_rate', '__pkpd_pharmacokinetics_inactivation_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 20, 12), )

    
    inactivation_rate = property(__inactivation_rate.value, __inactivation_rate.set, None, None)

    
    # Element half_life uses Python identifier half_life
    __half_life = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'half_life'), 'half_life', '__pkpd_pharmacokinetics_half_life', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 21, 12), )

    
    half_life = property(__half_life.value, __half_life.set, None, None)

    _ElementMap.update({
        __inactivation_rate.name() : __inactivation_rate,
        __half_life.name() : __half_life
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.pharmacokinetics = pharmacokinetics
Namespace.addCategoryObject('typeBinding', 'pharmacokinetics', pharmacokinetics)


# Complex type {pkpd}drug with content type ELEMENT_ONLY
class drug (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {pkpd}drug with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'drug')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 38, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element dose uses Python identifier dose
    __dose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dose'), 'dose', '__pkpd_drug_dose', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 40, 12), )

    
    dose = property(__dose.value, __dose.set, None, None)

    
    # Element pharmacokinetics uses Python identifier pharmacokinetics
    __pharmacokinetics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pharmacokinetics'), 'pharmacokinetics', '__pkpd_drug_pharmacokinetics', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 41, 12), )

    
    pharmacokinetics = property(__pharmacokinetics.value, __pharmacokinetics.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __dose.name() : __dose,
        __pharmacokinetics.name() : __pharmacokinetics
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.drug = drug
Namespace.addCategoryObject('typeBinding', 'drug', drug)


# Complex type {pkpd}drug_dose with content type ELEMENT_ONLY
class drug_dose (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {pkpd}drug_dose with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'drug_dose')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 46, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element dose uses Python identifier dose
    __dose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dose'), 'dose', '__pkpd_drug_dose_dose', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 48, 12), )

    
    dose = property(__dose.value, __dose.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__pkpd_drug_dose_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 27, 8)
    __name._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 27, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__pkpd_drug_dose_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 29, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 29, 8)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__pkpd_drug_dose_ID', pyxb.binding.datatypes.unsignedShort)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 34, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 34, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute ChEBI_ID uses Python identifier ChEBI_ID
    __ChEBI_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ChEBI_ID'), 'ChEBI_ID', '__pkpd_drug_dose_ChEBI_ID', pyxb.binding.datatypes.string)
    __ChEBI_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 65, 8)
    __ChEBI_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 65, 8)
    
    ChEBI_ID = property(__ChEBI_ID.value, __ChEBI_ID.set, None, None)

    
    # Attribute MeSH_ID uses Python identifier MeSH_ID
    __MeSH_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MeSH_ID'), 'MeSH_ID', '__pkpd_drug_dose_MeSH_ID', pyxb.binding.datatypes.string)
    __MeSH_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 66, 8)
    __MeSH_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 66, 8)
    
    MeSH_ID = property(__MeSH_ID.value, __MeSH_ID.set, None, None)

    
    # Attribute DrugBank_ID uses Python identifier DrugBank_ID
    __DrugBank_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DrugBank_ID'), 'DrugBank_ID', '__pkpd_drug_dose_DrugBank_ID', pyxb.binding.datatypes.string)
    __DrugBank_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 67, 8)
    __DrugBank_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 67, 8)
    
    DrugBank_ID = property(__DrugBank_ID.value, __DrugBank_ID.set, None, None)

    
    # Attribute GMO_ID uses Python identifier GMO_ID
    __GMO_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GMO_ID'), 'GMO_ID', '__pkpd_drug_dose_GMO_ID', pyxb.binding.datatypes.string)
    __GMO_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 68, 8)
    __GMO_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 68, 8)
    
    GMO_ID = property(__GMO_ID.value, __GMO_ID.set, None, None)

    
    # Attribute GO_ID uses Python identifier GO_ID
    __GO_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GO_ID'), 'GO_ID', '__pkpd_drug_dose_GO_ID', pyxb.binding.datatypes.string)
    __GO_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 69, 8)
    __GO_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 69, 8)
    
    GO_ID = property(__GO_ID.value, __GO_ID.set, None, None)

    
    # Attribute UniProt_ID uses Python identifier UniProt_ID
    __UniProt_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UniProt_ID'), 'UniProt_ID', '__pkpd_drug_dose_UniProt_ID', pyxb.binding.datatypes.string)
    __UniProt_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 70, 8)
    __UniProt_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 70, 8)
    
    UniProt_ID = property(__UniProt_ID.value, __UniProt_ID.set, None, None)

    
    # Attribute PR_ID uses Python identifier PR_ID
    __PR_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PR_ID'), 'PR_ID', '__pkpd_drug_dose_PR_ID', pyxb.binding.datatypes.string)
    __PR_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 71, 8)
    __PR_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 71, 8)
    
    PR_ID = property(__PR_ID.value, __PR_ID.set, None, None)

    _ElementMap.update({
        __dose.name() : __dose
    })
    _AttributeMap.update({
        __name.name() : __name,
        __units.name() : __units,
        __ID.name() : __ID,
        __ChEBI_ID.name() : __ChEBI_ID,
        __MeSH_ID.name() : __MeSH_ID,
        __DrugBank_ID.name() : __DrugBank_ID,
        __GMO_ID.name() : __GMO_ID,
        __GO_ID.name() : __GO_ID,
        __UniProt_ID.name() : __UniProt_ID,
        __PR_ID.name() : __PR_ID
    })
_module_typeBindings.drug_dose = drug_dose
Namespace.addCategoryObject('typeBinding', 'drug_dose', drug_dose)


# Complex type {pkpd}drug_pk with content type ELEMENT_ONLY
class drug_pk (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {pkpd}drug_pk with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'drug_pk')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 53, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pharmacokinetics uses Python identifier pharmacokinetics
    __pharmacokinetics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pharmacokinetics'), 'pharmacokinetics', '__pkpd_drug_pk_pharmacokinetics', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 55, 12), )

    
    pharmacokinetics = property(__pharmacokinetics.value, __pharmacokinetics.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__pkpd_drug_pk_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 27, 8)
    __name._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 27, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__pkpd_drug_pk_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 29, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 29, 8)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__pkpd_drug_pk_ID', pyxb.binding.datatypes.unsignedShort)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 34, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 34, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute ChEBI_ID uses Python identifier ChEBI_ID
    __ChEBI_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ChEBI_ID'), 'ChEBI_ID', '__pkpd_drug_pk_ChEBI_ID', pyxb.binding.datatypes.string)
    __ChEBI_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 65, 8)
    __ChEBI_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 65, 8)
    
    ChEBI_ID = property(__ChEBI_ID.value, __ChEBI_ID.set, None, None)

    
    # Attribute MeSH_ID uses Python identifier MeSH_ID
    __MeSH_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MeSH_ID'), 'MeSH_ID', '__pkpd_drug_pk_MeSH_ID', pyxb.binding.datatypes.string)
    __MeSH_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 66, 8)
    __MeSH_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 66, 8)
    
    MeSH_ID = property(__MeSH_ID.value, __MeSH_ID.set, None, None)

    
    # Attribute DrugBank_ID uses Python identifier DrugBank_ID
    __DrugBank_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DrugBank_ID'), 'DrugBank_ID', '__pkpd_drug_pk_DrugBank_ID', pyxb.binding.datatypes.string)
    __DrugBank_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 67, 8)
    __DrugBank_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 67, 8)
    
    DrugBank_ID = property(__DrugBank_ID.value, __DrugBank_ID.set, None, None)

    
    # Attribute GMO_ID uses Python identifier GMO_ID
    __GMO_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GMO_ID'), 'GMO_ID', '__pkpd_drug_pk_GMO_ID', pyxb.binding.datatypes.string)
    __GMO_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 68, 8)
    __GMO_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 68, 8)
    
    GMO_ID = property(__GMO_ID.value, __GMO_ID.set, None, None)

    
    # Attribute GO_ID uses Python identifier GO_ID
    __GO_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GO_ID'), 'GO_ID', '__pkpd_drug_pk_GO_ID', pyxb.binding.datatypes.string)
    __GO_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 69, 8)
    __GO_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 69, 8)
    
    GO_ID = property(__GO_ID.value, __GO_ID.set, None, None)

    
    # Attribute UniProt_ID uses Python identifier UniProt_ID
    __UniProt_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UniProt_ID'), 'UniProt_ID', '__pkpd_drug_pk_UniProt_ID', pyxb.binding.datatypes.string)
    __UniProt_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 70, 8)
    __UniProt_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 70, 8)
    
    UniProt_ID = property(__UniProt_ID.value, __UniProt_ID.set, None, None)

    
    # Attribute PR_ID uses Python identifier PR_ID
    __PR_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PR_ID'), 'PR_ID', '__pkpd_drug_pk_PR_ID', pyxb.binding.datatypes.string)
    __PR_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 71, 8)
    __PR_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 71, 8)
    
    PR_ID = property(__PR_ID.value, __PR_ID.set, None, None)

    _ElementMap.update({
        __pharmacokinetics.name() : __pharmacokinetics
    })
    _AttributeMap.update({
        __name.name() : __name,
        __units.name() : __units,
        __ID.name() : __ID,
        __ChEBI_ID.name() : __ChEBI_ID,
        __MeSH_ID.name() : __MeSH_ID,
        __DrugBank_ID.name() : __DrugBank_ID,
        __GMO_ID.name() : __GMO_ID,
        __GO_ID.name() : __GO_ID,
        __UniProt_ID.name() : __UniProt_ID,
        __PR_ID.name() : __PR_ID
    })
_module_typeBindings.drug_pk = drug_pk
Namespace.addCategoryObject('typeBinding', 'drug_pk', drug_pk)


# Complex type {pkpd}therapy with content type ELEMENT_ONLY
class therapy (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {pkpd}therapy with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'therapy')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 68, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element drug uses Python identifier drug
    __drug = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'drug'), 'drug', '__pkpd_therapy_drug', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 70, 12), )

    
    drug = property(__drug.value, __drug.set, None, None)

    _ElementMap.update({
        __drug.name() : __drug
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.therapy = therapy
Namespace.addCategoryObject('typeBinding', 'therapy', therapy)


# Complex type {pkpd}response with content type ELEMENT_ONLY
class response (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {pkpd}response with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'response')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 74, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element maximum_birth_inhibition uses Python identifier maximum_birth_inhibition
    __maximum_birth_inhibition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'maximum_birth_inhibition'), 'maximum_birth_inhibition', '__pkpd_response_maximum_birth_inhibition', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 76, 12), )

    
    maximum_birth_inhibition = property(__maximum_birth_inhibition.value, __maximum_birth_inhibition.set, None, None)

    
    # Element maximum_birth_inhibition_time uses Python identifier maximum_birth_inhibition_time
    __maximum_birth_inhibition_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'maximum_birth_inhibition_time'), 'maximum_birth_inhibition_time', '__pkpd_response_maximum_birth_inhibition_time', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 77, 12), )

    
    maximum_birth_inhibition_time = property(__maximum_birth_inhibition_time.value, __maximum_birth_inhibition_time.set, None, None)

    
    # Element birth_inhibition_recovery_rate uses Python identifier birth_inhibition_recovery_rate
    __birth_inhibition_recovery_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'birth_inhibition_recovery_rate'), 'birth_inhibition_recovery_rate', '__pkpd_response_birth_inhibition_recovery_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 79, 12), )

    
    birth_inhibition_recovery_rate = property(__birth_inhibition_recovery_rate.value, __birth_inhibition_recovery_rate.set, None, None)

    
    # Element maximum_death_rate uses Python identifier maximum_death_rate
    __maximum_death_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'maximum_death_rate'), 'maximum_death_rate', '__pkpd_response_maximum_death_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 81, 12), )

    
    maximum_death_rate = property(__maximum_death_rate.value, __maximum_death_rate.set, None, None)

    
    # Element maximum_death_time uses Python identifier maximum_death_time
    __maximum_death_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'maximum_death_time'), 'maximum_death_time', '__pkpd_response_maximum_death_time', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 82, 12), )

    
    maximum_death_time = property(__maximum_death_time.value, __maximum_death_time.set, None, None)

    
    # Element death_recovery_rate uses Python identifier death_recovery_rate
    __death_recovery_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'death_recovery_rate'), 'death_recovery_rate', '__pkpd_response_death_recovery_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 83, 12), )

    
    death_recovery_rate = property(__death_recovery_rate.value, __death_recovery_rate.set, None, None)

    
    # Element response_observation uses Python identifier response_observation
    __response_observation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'response_observation'), 'response_observation', '__pkpd_response_response_observation', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 84, 12), )

    
    response_observation = property(__response_observation.value, __response_observation.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__pkpd_response_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 90, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __maximum_birth_inhibition.name() : __maximum_birth_inhibition,
        __maximum_birth_inhibition_time.name() : __maximum_birth_inhibition_time,
        __birth_inhibition_recovery_rate.name() : __birth_inhibition_recovery_rate,
        __maximum_death_rate.name() : __maximum_death_rate,
        __maximum_death_time.name() : __maximum_death_time,
        __death_recovery_rate.name() : __death_recovery_rate,
        __response_observation.name() : __response_observation,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.response = response
Namespace.addCategoryObject('typeBinding', 'response', response)


# Complex type {pkpd}response_observation with content type ELEMENT_ONLY
class response_observation (pyxb.binding.basis.complexTypeDefinition):
    """
                notes xmlns=''>
                    Birth rate and death rate elements are measurements for the "live_apoptotic" cell cycle model.
                    Net birth rate and net death rate elements are measurements for the "total cell" cell cycle model.
                /notes>
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'response_observation')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 94, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'time'), 'time', '__pkpd_response_observation_time', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 104, 12), )

    
    time = property(__time.value, __time.set, None, None)

    
    # Element birth_rate uses Python identifier birth_rate
    __birth_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'birth_rate'), 'birth_rate', '__pkpd_response_observation_birth_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 105, 12), )

    
    birth_rate = property(__birth_rate.value, __birth_rate.set, None, None)

    
    # Element death_rate uses Python identifier death_rate
    __death_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'death_rate'), 'death_rate', '__pkpd_response_observation_death_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 106, 12), )

    
    death_rate = property(__death_rate.value, __death_rate.set, None, None)

    
    # Element net_birth_rate uses Python identifier net_birth_rate
    __net_birth_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'net_birth_rate'), 'net_birth_rate', '__pkpd_response_observation_net_birth_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 107, 12), )

    
    net_birth_rate = property(__net_birth_rate.value, __net_birth_rate.set, None, None)

    
    # Element net_death_rate uses Python identifier net_death_rate
    __net_death_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'net_death_rate'), 'net_death_rate', '__pkpd_response_observation_net_death_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 108, 12), )

    
    net_death_rate = property(__net_death_rate.value, __net_death_rate.set, None, None)

    
    # Element apoptotic_duration uses Python identifier apoptotic_duration
    __apoptotic_duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'apoptotic_duration'), 'apoptotic_duration', '__pkpd_response_observation_apoptotic_duration', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 109, 12), )

    
    apoptotic_duration = property(__apoptotic_duration.value, __apoptotic_duration.set, None, None)

    
    # Element percent_cell_viability uses Python identifier percent_cell_viability
    __percent_cell_viability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'percent_cell_viability'), 'percent_cell_viability', '__pkpd_response_observation_percent_cell_viability', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 110, 12), )

    
    percent_cell_viability = property(__percent_cell_viability.value, __percent_cell_viability.set, None, '\n                        \n                    ')

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__pkpd_response_observation_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 125, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __time.name() : __time,
        __birth_rate.name() : __birth_rate,
        __death_rate.name() : __death_rate,
        __net_birth_rate.name() : __net_birth_rate,
        __net_death_rate.name() : __net_death_rate,
        __apoptotic_duration.name() : __apoptotic_duration,
        __percent_cell_viability.name() : __percent_cell_viability,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.response_observation = response_observation
Namespace.addCategoryObject('typeBinding', 'response_observation', response_observation)


# Complex type {pkpd}pharmacodynamics with content type ELEMENT_ONLY
class pharmacodynamics (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {pkpd}pharmacodynamics with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pharmacodynamics')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 129, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element therapy_measurement_set uses Python identifier therapy_measurement_set
    __therapy_measurement_set = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'therapy_measurement_set'), 'therapy_measurement_set', '__pkpd_pharmacodynamics_therapy_measurement_set', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 131, 12), )

    
    therapy_measurement_set = property(__therapy_measurement_set.value, __therapy_measurement_set.set, None, None)

    _ElementMap.update({
        __therapy_measurement_set.name() : __therapy_measurement_set
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.pharmacodynamics = pharmacodynamics
Namespace.addCategoryObject('typeBinding', 'pharmacodynamics', pharmacodynamics)


# Complex type {pkpd}therapy_measurement_set with content type ELEMENT_ONLY
class therapy_measurement_set (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {pkpd}therapy_measurement_set with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'therapy_measurement_set')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 140, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element therapy uses Python identifier therapy
    __therapy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'therapy'), 'therapy', '__pkpd_therapy_measurement_set_therapy', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 142, 12), )

    
    therapy = property(__therapy.value, __therapy.set, None, None)

    
    # Element response uses Python identifier response
    __response = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'response'), 'response', '__pkpd_therapy_measurement_set_response', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 148, 12), )

    
    response = property(__response.value, __response.set, None, '\n                        There should only be one response for a given therapy.\n                    ')

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__pkpd_therapy_measurement_set_ID', pyxb.binding.datatypes.unsignedShort)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 156, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 156, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __therapy.name() : __therapy,
        __response.name() : __response
    })
    _AttributeMap.update({
        __ID.name() : __ID
    })
_module_typeBindings.therapy_measurement_set = therapy_measurement_set
Namespace.addCategoryObject('typeBinding', 'therapy_measurement_set', therapy_measurement_set)


# Complex type {pkpd}PKPD with content type ELEMENT_ONLY
class PKPD (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {pkpd}PKPD with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PKPD')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 160, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element drug uses Python identifier drug
    __drug = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'drug'), 'drug', '__pkpd_PKPD_drug', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 162, 12), )

    
    drug = property(__drug.value, __drug.set, None, None)

    
    # Element pharmacodynamics uses Python identifier pharmacodynamics
    __pharmacodynamics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pharmacodynamics'), 'pharmacodynamics', '__pkpd_PKPD_pharmacodynamics', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 163, 12), )

    
    pharmacodynamics = property(__pharmacodynamics.value, __pharmacodynamics.set, None, None)

    _ElementMap.update({
        __drug.name() : __drug,
        __pharmacodynamics.name() : __pharmacodynamics
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PKPD = PKPD
Namespace.addCategoryObject('typeBinding', 'PKPD', PKPD)


# Complex type {pkpd}dose with content type SIMPLE
class dose (_ImportedBinding_common.units_decimal):
    """Complex type {pkpd}dose with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dose')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 60, 4)
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
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__pkpd_dose_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 63, 16)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 63, 16)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.dose = dose
Namespace.addCategoryObject('typeBinding', 'dose', dose)




pharmacokinetics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inactivation_rate'), _ImportedBinding_common.units_decimal, scope=pharmacokinetics, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 20, 12)))

pharmacokinetics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'half_life'), _ImportedBinding_common.units_decimal, scope=pharmacokinetics, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 21, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 20, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 21, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pharmacokinetics._UseForTag(pyxb.namespace.ExpandedName(None, 'inactivation_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 20, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pharmacokinetics._UseForTag(pyxb.namespace.ExpandedName(None, 'half_life')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 21, 12))
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
pharmacokinetics._Automaton = _BuildAutomaton()




drug._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dose'), dose, scope=drug, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 40, 12)))

drug._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pharmacokinetics'), pharmacokinetics, scope=drug, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 41, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(drug._UseForTag(pyxb.namespace.ExpandedName(None, 'dose')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 40, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(drug._UseForTag(pyxb.namespace.ExpandedName(None, 'pharmacokinetics')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 41, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
drug._Automaton = _BuildAutomaton_()




drug_dose._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dose'), dose, scope=drug_dose, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 48, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(drug_dose._UseForTag(pyxb.namespace.ExpandedName(None, 'dose')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 48, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
drug_dose._Automaton = _BuildAutomaton_2()




drug_pk._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pharmacokinetics'), pharmacokinetics, scope=drug_pk, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 55, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(drug_pk._UseForTag(pyxb.namespace.ExpandedName(None, 'pharmacokinetics')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 55, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
drug_pk._Automaton = _BuildAutomaton_3()




therapy._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'drug'), drug_dose, scope=therapy, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 70, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(therapy._UseForTag(pyxb.namespace.ExpandedName(None, 'drug')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 70, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
therapy._Automaton = _BuildAutomaton_4()




response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'maximum_birth_inhibition'), _ImportedBinding_common.units_decimal, scope=response, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 76, 12)))

response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'maximum_birth_inhibition_time'), _ImportedBinding_common.units_decimal, scope=response, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 77, 12)))

response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'birth_inhibition_recovery_rate'), _ImportedBinding_common.units_decimal, scope=response, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 79, 12)))

response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'maximum_death_rate'), _ImportedBinding_common.units_decimal, scope=response, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 81, 12)))

response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'maximum_death_time'), _ImportedBinding_common.units_decimal, scope=response, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 82, 12)))

response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'death_recovery_rate'), _ImportedBinding_common.units_decimal, scope=response, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 83, 12)))

response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'response_observation'), response_observation, scope=response, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 84, 12)))

response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=response, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 90, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 76, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 77, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 79, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 81, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 82, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 83, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 84, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 90, 12))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(response._UseForTag(pyxb.namespace.ExpandedName(None, 'maximum_birth_inhibition')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 76, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(response._UseForTag(pyxb.namespace.ExpandedName(None, 'maximum_birth_inhibition_time')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 77, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(response._UseForTag(pyxb.namespace.ExpandedName(None, 'birth_inhibition_recovery_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 79, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(response._UseForTag(pyxb.namespace.ExpandedName(None, 'maximum_death_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 81, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(response._UseForTag(pyxb.namespace.ExpandedName(None, 'maximum_death_time')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 82, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(response._UseForTag(pyxb.namespace.ExpandedName(None, 'death_recovery_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 83, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(response._UseForTag(pyxb.namespace.ExpandedName(None, 'response_observation')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 84, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(response._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 90, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
response._Automaton = _BuildAutomaton_5()




response_observation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'time'), _ImportedBinding_common.units_decimal, scope=response_observation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 104, 12)))

response_observation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'birth_rate'), _ImportedBinding_common.units_decimal_nonnegative, scope=response_observation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 105, 12)))

response_observation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'death_rate'), _ImportedBinding_common.units_decimal_nonnegative, scope=response_observation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 106, 12)))

response_observation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'net_birth_rate'), _ImportedBinding_common.units_decimal, scope=response_observation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 107, 12)))

response_observation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'net_death_rate'), _ImportedBinding_common.units_decimal, scope=response_observation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 108, 12)))

response_observation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'apoptotic_duration'), _ImportedBinding_common.units_decimal, scope=response_observation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 109, 12)))

response_observation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'percent_cell_viability'), _ImportedBinding_common.units_decimal, scope=response_observation, documentation='\n                        \n                    ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 110, 12)))

response_observation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=response_observation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 125, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 104, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 105, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 106, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 107, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 108, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 109, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 110, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 125, 12))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(response_observation._UseForTag(pyxb.namespace.ExpandedName(None, 'time')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 104, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(response_observation._UseForTag(pyxb.namespace.ExpandedName(None, 'birth_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 105, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(response_observation._UseForTag(pyxb.namespace.ExpandedName(None, 'death_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 106, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(response_observation._UseForTag(pyxb.namespace.ExpandedName(None, 'net_birth_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 107, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(response_observation._UseForTag(pyxb.namespace.ExpandedName(None, 'net_death_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 108, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(response_observation._UseForTag(pyxb.namespace.ExpandedName(None, 'apoptotic_duration')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 109, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(response_observation._UseForTag(pyxb.namespace.ExpandedName(None, 'percent_cell_viability')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 110, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(response_observation._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 125, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
response_observation._Automaton = _BuildAutomaton_6()




pharmacodynamics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'therapy_measurement_set'), therapy_measurement_set, scope=pharmacodynamics, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 131, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(pharmacodynamics._UseForTag(pyxb.namespace.ExpandedName(None, 'therapy_measurement_set')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 131, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
pharmacodynamics._Automaton = _BuildAutomaton_7()




therapy_measurement_set._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'therapy'), therapy, scope=therapy_measurement_set, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 142, 12)))

therapy_measurement_set._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'response'), response, scope=therapy_measurement_set, documentation='\n                        There should only be one response for a given therapy.\n                    ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 148, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(therapy_measurement_set._UseForTag(pyxb.namespace.ExpandedName(None, 'therapy')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 142, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(therapy_measurement_set._UseForTag(pyxb.namespace.ExpandedName(None, 'response')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 148, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
therapy_measurement_set._Automaton = _BuildAutomaton_8()




PKPD._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'drug'), drug_pk, scope=PKPD, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 162, 12)))

PKPD._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pharmacodynamics'), pharmacodynamics, scope=PKPD, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 163, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 162, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 163, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PKPD._UseForTag(pyxb.namespace.ExpandedName(None, 'drug')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 162, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PKPD._UseForTag(pyxb.namespace.ExpandedName(None, 'pharmacodynamics')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/pkpd.xsd', 163, 12))
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
PKPD._Automaton = _BuildAutomaton_9()

