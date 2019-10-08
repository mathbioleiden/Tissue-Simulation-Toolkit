# libMCDS/python/meta.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:4c24b2612e94e2ae622e54397663f2b7bf0a2e17
# Generated 2016-11-29 16:42:21.920706 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace metadata [xmlns:meta]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('metadata', create_if_missing=True)
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


# Atomic simple type: {metadata}URL
class URL (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'URL')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 12, 4)
    _Documentation = None
URL._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'URL', URL)
_module_typeBindings.URL = URL

# Complex type {metadata}orcid-identifier with content type ELEMENT_ONLY
class orcid_identifier (pyxb.binding.basis.complexTypeDefinition):
    """
                    Eventually, replace with the ORCID XSDs.
                """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'orcid-identifier')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 18, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element path uses Python identifier path
    __path = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'path'), 'path', '__metadata_orcid_identifier_path', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 25, 16), )

    
    path = property(__path.value, __path.set, None, None)

    
    # Element given-names uses Python identifier given_names
    __given_names = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'given-names'), 'given_names', '__metadata_orcid_identifier_given_names', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 26, 16), )

    
    given_names = property(__given_names.value, __given_names.set, None, None)

    
    # Element family-name uses Python identifier family_name
    __family_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'family-name'), 'family_name', '__metadata_orcid_identifier_family_name', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 27, 16), )

    
    family_name = property(__family_name.value, __family_name.set, None, None)

    
    # Element email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'email'), 'email', '__metadata_orcid_identifier_email', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 28, 16), )

    
    email = property(__email.value, __email.set, None, None)

    
    # Element url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__metadata_orcid_identifier_url', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 29, 16), )

    
    url = property(__url.value, __url.set, None, None)

    
    # Element organization-name uses Python identifier organization_name
    __organization_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'organization-name'), 'organization_name', '__metadata_orcid_identifier_organization_name', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 30, 16), )

    
    organization_name = property(__organization_name.value, __organization_name.set, None, None)

    
    # Element department-name uses Python identifier department_name
    __department_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'department-name'), 'department_name', '__metadata_orcid_identifier_department_name', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 31, 16), )

    
    department_name = property(__department_name.value, __department_name.set, None, None)

    _ElementMap.update({
        __path.name() : __path,
        __given_names.name() : __given_names,
        __family_name.name() : __family_name,
        __email.name() : __email,
        __url.name() : __url,
        __organization_name.name() : __organization_name,
        __department_name.name() : __department_name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.orcid_identifier = orcid_identifier
Namespace.addCategoryObject('typeBinding', 'orcid-identifier', orcid_identifier)


# Complex type {metadata}orcid-person with content type ELEMENT_ONLY
class orcid_person (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {metadata}orcid-person with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'orcid-person')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 38, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element orcid-identifier uses Python identifier orcid_identifier
    __orcid_identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orcid-identifier'), 'orcid_identifier', '__metadata_orcid_person_orcid_identifier', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 40, 16), )

    
    orcid_identifier = property(__orcid_identifier.value, __orcid_identifier.set, None, None)

    _ElementMap.update({
        __orcid_identifier.name() : __orcid_identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.orcid_person = orcid_person
Namespace.addCategoryObject('typeBinding', 'orcid-person', orcid_person)


# Complex type {metadata}curation with content type ELEMENT_ONLY
class curation (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'curation')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 43, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element created uses Python identifier created
    __created = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'created'), 'created', '__metadata_curation_created', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 56, 16), )

    
    created = property(__created.value, __created.set, None, None)

    
    # Element last_modified uses Python identifier last_modified
    __last_modified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'last_modified'), 'last_modified', '__metadata_curation_last_modified', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 57, 16), )

    
    last_modified = property(__last_modified.value, __last_modified.set, None, None)

    
    # Element classification uses Python identifier classification
    __classification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'classification'), 'classification', '__metadata_curation_classification', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 59, 20), )

    
    classification = property(__classification.value, __classification.set, None, None)

    
    # Element version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__metadata_curation_version', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 60, 20), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Element creator uses Python identifier creator
    __creator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'creator'), 'creator', '__metadata_curation_creator', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 63, 16), )

    
    creator = property(__creator.value, __creator.set, None, None)

    
    # Element current_contact uses Python identifier current_contact
    __current_contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'current_contact'), 'current_contact', '__metadata_curation_current_contact', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 65, 16), )

    
    current_contact = property(__current_contact.value, __current_contact.set, None, '\n                            This element could be like the PersonContact in NCO\n                        ')

    
    # Element curator uses Python identifier curator
    __curator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'curator'), 'curator', '__metadata_curation_curator', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 73, 16), )

    
    curator = property(__curator.value, __curator.set, None, '\n                            This element is required for a cell line. The schematron test for this is in the parent complexType/class.\n                        ')

    
    # Element last_modified_by uses Python identifier last_modified_by
    __last_modified_by = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'last_modified_by'), 'last_modified_by', '__metadata_curation_last_modified_by', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 80, 16), )

    
    last_modified_by = property(__last_modified_by.value, __last_modified_by.set, None, None)

    
    # Attribute curated uses Python identifier curated
    __curated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'curated'), 'curated', '__metadata_curation_curated', pyxb.binding.datatypes.boolean)
    __curated._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 84, 12)
    __curated._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 84, 12)
    
    curated = property(__curated.value, __curated.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        __created.name() : __created,
        __last_modified.name() : __last_modified,
        __classification.name() : __classification,
        __version.name() : __version,
        __creator.name() : __creator,
        __current_contact.name() : __current_contact,
        __curator.name() : __curator,
        __last_modified_by.name() : __last_modified_by
    })
    _AttributeMap.update({
        __curated.name() : __curated
    })
_module_typeBindings.curation = curation
Namespace.addCategoryObject('typeBinding', 'curation', curation)


# Complex type {metadata}classification with content type ELEMENT_ONLY
class classification (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {metadata}classification with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'classification')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 88, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element classification_number uses Python identifier classification_number
    __classification_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'classification_number'), 'classification_number', '__metadata_classification_classification_number', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 90, 12), )

    
    classification_number = property(__classification_number.value, __classification_number.set, None, None)

    
    # Element line uses Python identifier line
    __line = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'line'), 'line', '__metadata_classification_line', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 91, 12), )

    
    line = property(__line.value, __line.set, None, None)

    
    # Element variant uses Python identifier variant
    __variant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'variant'), 'variant', '__metadata_classification_variant', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 92, 12), )

    
    variant = property(__variant.value, __variant.set, None, None)

    
    # Element branch uses Python identifier branch
    __branch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'branch'), 'branch', '__metadata_classification_branch', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 93, 12), )

    
    branch = property(__branch.value, __branch.set, None, None)

    
    # Element version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__metadata_classification_version', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 94, 12), )

    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __classification_number.name() : __classification_number,
        __line.name() : __line,
        __variant.name() : __variant,
        __branch.name() : __branch,
        __version.name() : __version
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.classification = classification
Namespace.addCategoryObject('typeBinding', 'classification', classification)


# Complex type {metadata}citation with content type ELEMENT_ONLY
class citation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {metadata}citation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'citation')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 104, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'text'), 'text', '__metadata_citation_text', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 106, 16), )

    
    text = property(__text.value, __text.set, None, None)

    
    # Element DOI uses Python identifier DOI
    __DOI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DOI'), 'DOI', '__metadata_citation_DOI', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 107, 16), )

    
    DOI = property(__DOI.value, __DOI.set, None, None)

    
    # Element URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'URL'), 'URL', '__metadata_citation_URL', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 108, 16), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Element PMID uses Python identifier PMID
    __PMID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PMID'), 'PMID', '__metadata_citation_PMID', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 109, 16), )

    
    PMID = property(__PMID.value, __PMID.set, None, None)

    
    # Element PMCID uses Python identifier PMCID
    __PMCID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PMCID'), 'PMCID', '__metadata_citation_PMCID', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 110, 16), )

    
    PMCID = property(__PMCID.value, __PMCID.set, None, None)

    
    # Element arXiv uses Python identifier arXiv
    __arXiv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'arXiv'), 'arXiv', '__metadata_citation_arXiv', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 111, 16), )

    
    arXiv = property(__arXiv.value, __arXiv.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'notes'), 'notes', '__metadata_citation_notes', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 112, 16), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__metadata_citation_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 113, 16), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __text.name() : __text,
        __DOI.name() : __DOI,
        __URL.name() : __URL,
        __PMID.name() : __PMID,
        __PMCID.name() : __PMCID,
        __arXiv.name() : __arXiv,
        __notes.name() : __notes,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.citation = citation
Namespace.addCategoryObject('typeBinding', 'citation', citation)


# Complex type {metadata}data_origin with content type ELEMENT_ONLY
class data_origin (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {metadata}data_origin with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'data_origin')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 123, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element instrumentation_information uses Python identifier instrumentation_information
    __instrumentation_information = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'instrumentation_information'), 'instrumentation_information', '__metadata_data_origin_instrumentation_information', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 125, 16), )

    
    instrumentation_information = property(__instrumentation_information.value, __instrumentation_information.set, None, None)

    
    # Element experimental_protocol uses Python identifier experimental_protocol
    __experimental_protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'experimental_protocol'), 'experimental_protocol', '__metadata_data_origin_experimental_protocol', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 126, 16), )

    
    experimental_protocol = property(__experimental_protocol.value, __experimental_protocol.set, None, None)

    
    # Element citation uses Python identifier citation
    __citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'citation'), 'citation', '__metadata_data_origin_citation', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 127, 16), )

    
    citation = property(__citation.value, __citation.set, None, None)

    
    # Element xpath uses Python identifier xpath
    __xpath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'xpath'), 'xpath', '__metadata_data_origin_xpath', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 128, 16), )

    
    xpath = property(__xpath.value, __xpath.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'notes'), 'notes', '__metadata_data_origin_notes', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 129, 16), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__metadata_data_origin_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 130, 16), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__metadata_data_origin_ID', pyxb.binding.datatypes.unsignedLong)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 132, 12)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 132, 12)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __instrumentation_information.name() : __instrumentation_information,
        __experimental_protocol.name() : __experimental_protocol,
        __citation.name() : __citation,
        __xpath.name() : __xpath,
        __notes.name() : __notes,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __ID.name() : __ID
    })
_module_typeBindings.data_origin = data_origin
Namespace.addCategoryObject('typeBinding', 'data_origin', data_origin)


# Complex type {metadata}data_origins with content type ELEMENT_ONLY
class data_origins (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {metadata}data_origins with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'data_origins')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 137, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element data_origin uses Python identifier data_origin
    __data_origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'data_origin'), 'data_origin', '__metadata_data_origins_data_origin', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 139, 16), )

    
    data_origin = property(__data_origin.value, __data_origin.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__metadata_data_origins_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 140, 16), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __data_origin.name() : __data_origin,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.data_origins = data_origins
Namespace.addCategoryObject('typeBinding', 'data_origins', data_origins)


# Complex type {metadata}data_analysis with content type ELEMENT_ONLY
class data_analysis (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {metadata}data_analysis with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'data_analysis')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 150, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'URL'), 'URL', '__metadata_data_analysis_URL', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 152, 16), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Element citation uses Python identifier citation
    __citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'citation'), 'citation', '__metadata_data_analysis_citation', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 153, 16), )

    
    citation = property(__citation.value, __citation.set, None, None)

    
    # Element software uses Python identifier software
    __software = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'software'), 'software', '__metadata_data_analysis_software', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 154, 16), )

    
    software = property(__software.value, __software.set, None, None)

    
    # Element xpath uses Python identifier xpath
    __xpath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'xpath'), 'xpath', '__metadata_data_analysis_xpath', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 155, 16), )

    
    xpath = property(__xpath.value, __xpath.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'notes'), 'notes', '__metadata_data_analysis_notes', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 156, 16), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__metadata_data_analysis_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 157, 16), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __URL.name() : __URL,
        __citation.name() : __citation,
        __software.name() : __software,
        __xpath.name() : __xpath,
        __notes.name() : __notes,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.data_analysis = data_analysis
Namespace.addCategoryObject('typeBinding', 'data_analysis', data_analysis)


# Complex type {metadata}software with content type ELEMENT_ONLY
class software (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {metadata}software with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'software')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 162, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element software_name uses Python identifier software_name
    __software_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'software_name'), 'software_name', '__metadata_software_software_name', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 182, 12), )

    
    software_name = property(__software_name.value, __software_name.set, None, None)

    
    # Element software_version uses Python identifier software_version
    __software_version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'software_version'), 'software_version', '__metadata_software_software_version', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 183, 12), )

    
    software_version = property(__software_version.value, __software_version.set, None, None)

    
    # Element software_input_configuration uses Python identifier software_input_configuration
    __software_input_configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'software_input_configuration'), 'software_input_configuration', '__metadata_software_software_input_configuration', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 184, 12), )

    
    software_input_configuration = property(__software_input_configuration.value, __software_input_configuration.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__metadata_software_name', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 185, 12), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__metadata_software_version', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 186, 12), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Element input_configuration uses Python identifier input_configuration
    __input_configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'input_configuration'), 'input_configuration', '__metadata_software_input_configuration', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 187, 12), )

    
    input_configuration = property(__input_configuration.value, __input_configuration.set, None, None)

    
    # Element URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'URL'), 'URL', '__metadata_software_URL', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 188, 12), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Element creator uses Python identifier creator
    __creator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'creator'), 'creator', '__metadata_software_creator', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 189, 12), )

    
    creator = property(__creator.value, __creator.set, None, None)

    
    # Element citation uses Python identifier citation
    __citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'citation'), 'citation', '__metadata_software_citation', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 190, 12), )

    
    citation = property(__citation.value, __citation.set, None, None)

    
    # Element user uses Python identifier user
    __user = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'user'), 'user', '__metadata_software_user', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 191, 12), )

    
    user = property(__user.value, __user.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__metadata_software_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 192, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __software_name.name() : __software_name,
        __software_version.name() : __software_version,
        __software_input_configuration.name() : __software_input_configuration,
        __name.name() : __name,
        __version.name() : __version,
        __input_configuration.name() : __input_configuration,
        __URL.name() : __URL,
        __creator.name() : __creator,
        __citation.name() : __citation,
        __user.name() : __user,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.software = software
Namespace.addCategoryObject('typeBinding', 'software', software)


# Complex type {metadata}cell_origin with content type ELEMENT_ONLY
class cell_origin (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {metadata}cell_origin with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cell_origin')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 222, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element BTO_ID uses Python identifier BTO_ID
    __BTO_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BTO_ID'), 'BTO_ID', '__metadata_cell_origin_BTO_ID', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 224, 12), )

    
    BTO_ID = property(__BTO_ID.value, __BTO_ID.set, None, None)

    
    # Element CLO_ID uses Python identifier CLO_ID
    __CLO_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CLO_ID'), 'CLO_ID', '__metadata_cell_origin_CLO_ID', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 225, 12), )

    
    CLO_ID = property(__CLO_ID.value, __CLO_ID.set, None, None)

    
    # Element species uses Python identifier species
    __species = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'species'), 'species', '__metadata_cell_origin_species', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 226, 12), )

    
    species = property(__species.value, __species.set, None, None)

    
    # Element strain uses Python identifier strain
    __strain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'strain'), 'strain', '__metadata_cell_origin_strain', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 227, 12), )

    
    strain = property(__strain.value, __strain.set, None, None)

    
    # Element organ uses Python identifier organ
    __organ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'organ'), 'organ', '__metadata_cell_origin_organ', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 228, 12), )

    
    organ = property(__organ.value, __organ.set, None, None)

    
    # Element disease uses Python identifier disease
    __disease = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'disease'), 'disease', '__metadata_cell_origin_disease', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 229, 12), )

    
    disease = property(__disease.value, __disease.set, None, None)

    
    # Element morphology uses Python identifier morphology
    __morphology = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'morphology'), 'morphology', '__metadata_cell_origin_morphology', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 230, 12), )

    
    morphology = property(__morphology.value, __morphology.set, None, None)

    
    # Element patient_derived uses Python identifier patient_derived
    __patient_derived = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'patient_derived'), 'patient_derived', '__metadata_cell_origin_patient_derived', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 231, 12), )

    
    patient_derived = property(__patient_derived.value, __patient_derived.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__metadata_cell_origin_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 232, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __BTO_ID.name() : __BTO_ID,
        __CLO_ID.name() : __CLO_ID,
        __species.name() : __species,
        __strain.name() : __strain,
        __organ.name() : __organ,
        __disease.name() : __disease,
        __morphology.name() : __morphology,
        __patient_derived.name() : __patient_derived,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.cell_origin = cell_origin
Namespace.addCategoryObject('typeBinding', 'cell_origin', cell_origin)


# Complex type {metadata}species with content type SIMPLE
class species (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {metadata}species with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'species')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 236, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute MeSH_ID uses Python identifier MeSH_ID
    __MeSH_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MeSH_ID'), 'MeSH_ID', '__metadata_species_MeSH_ID', pyxb.binding.datatypes.string)
    __MeSH_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 239, 16)
    __MeSH_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 239, 16)
    
    MeSH_ID = property(__MeSH_ID.value, __MeSH_ID.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __MeSH_ID.name() : __MeSH_ID
    })
_module_typeBindings.species = species
Namespace.addCategoryObject('typeBinding', 'species', species)


# Complex type {metadata}disease with content type SIMPLE
class disease (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {metadata}disease with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'disease')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 244, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute EFO_ID uses Python identifier EFO_ID
    __EFO_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'EFO_ID'), 'EFO_ID', '__metadata_disease_EFO_ID', pyxb.binding.datatypes.string)
    __EFO_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 247, 16)
    __EFO_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 247, 16)
    
    EFO_ID = property(__EFO_ID.value, __EFO_ID.set, None, None)

    
    # Attribute DOID_ID uses Python identifier DOID_ID
    __DOID_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DOID_ID'), 'DOID_ID', '__metadata_disease_DOID_ID', pyxb.binding.datatypes.string)
    __DOID_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 248, 16)
    __DOID_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 248, 16)
    
    DOID_ID = property(__DOID_ID.value, __DOID_ID.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __EFO_ID.name() : __EFO_ID,
        __DOID_ID.name() : __DOID_ID
    })
_module_typeBindings.disease = disease
Namespace.addCategoryObject('typeBinding', 'disease', disease)


# Complex type {metadata}patient_derived with content type SIMPLE
class patient_derived (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {metadata}patient_derived with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.boolean
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'patient_derived')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 253, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.boolean
    
    # Attribute patient_ID uses Python identifier patient_ID
    __patient_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'patient_ID'), 'patient_ID', '__metadata_patient_derived_patient_ID', pyxb.binding.datatypes.string)
    __patient_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 256, 16)
    __patient_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 256, 16)
    
    patient_ID = property(__patient_ID.value, __patient_ID.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __patient_ID.name() : __patient_ID
    })
_module_typeBindings.patient_derived = patient_derived
Namespace.addCategoryObject('typeBinding', 'patient_derived', patient_derived)


# Complex type {metadata}MultiCellDB with content type ELEMENT_ONLY
class MultiCellDB (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {metadata}MultiCellDB with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiCellDB')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 265, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ID uses Python identifier ID
    __ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__metadata_MultiCellDB_ID', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 267, 12), )

    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__metadata_MultiCellDB_name', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 268, 12), )

    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __ID.name() : __ID,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MultiCellDB = MultiCellDB
Namespace.addCategoryObject('typeBinding', 'MultiCellDB', MultiCellDB)


# Complex type {metadata}rights with content type ELEMENT_ONLY
class rights (pyxb.binding.basis.complexTypeDefinition):
    """
                We follow the DCMI term for rights
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rights')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 272, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element license uses Python identifier license
    __license = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'license'), 'license', '__metadata_rights_license', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 279, 12), )

    
    license = property(__license.value, __license.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__metadata_rights_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 280, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __license.name() : __license,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.rights = rights
Namespace.addCategoryObject('typeBinding', 'rights', rights)


# Complex type {metadata}license with content type ELEMENT_ONLY
class license (pyxb.binding.basis.complexTypeDefinition):
    """
                We follow the DCMI term for license
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'license')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 284, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LicenseDocument uses Python identifier LicenseDocument
    __LicenseDocument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LicenseDocument'), 'LicenseDocument', '__metadata_license_LicenseDocument', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 291, 12), )

    
    LicenseDocument = property(__LicenseDocument.value, __LicenseDocument.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'notes'), 'notes', '__metadata_license_notes', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 292, 12), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__metadata_license_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 293, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __LicenseDocument.name() : __LicenseDocument,
        __notes.name() : __notes,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.license = license
Namespace.addCategoryObject('typeBinding', 'license', license)


# Complex type {metadata}LicenseDocument with content type ELEMENT_ONLY
class LicenseDocument (pyxb.binding.basis.complexTypeDefinition):
    """
                We follow the DCMI term for LicenseDocument
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseDocument')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 297, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__metadata_LicenseDocument_name', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 304, 12), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'URL'), 'URL', '__metadata_LicenseDocument_URL', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 305, 12), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__metadata_LicenseDocument_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 306, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __URL.name() : __URL,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LicenseDocument = LicenseDocument
Namespace.addCategoryObject('typeBinding', 'LicenseDocument', LicenseDocument)


# Complex type {metadata}metadata with content type ELEMENT_ONLY
class metadata (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {metadata}metadata with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'metadata')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 310, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element MultiCellDB uses Python identifier MultiCellDB
    __MultiCellDB = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MultiCellDB'), 'MultiCellDB', '__metadata_metadata_MultiCellDB', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 312, 16), )

    
    MultiCellDB = property(__MultiCellDB.value, __MultiCellDB.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__metadata_metadata_description', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 313, 16), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element software uses Python identifier software
    __software = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'software'), 'software', '__metadata_metadata_software', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 314, 16), )

    
    software = property(__software.value, __software.set, None, None)

    
    # Element citation uses Python identifier citation
    __citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'citation'), 'citation', '__metadata_metadata_citation', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 315, 16), )

    
    citation = property(__citation.value, __citation.set, None, None)

    
    # Element curation uses Python identifier curation
    __curation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'curation'), 'curation', '__metadata_metadata_curation', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 316, 16), )

    
    curation = property(__curation.value, __curation.set, None, None)

    
    # Element data_origins uses Python identifier data_origins
    __data_origins = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'data_origins'), 'data_origins', '__metadata_metadata_data_origins', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 317, 16), )

    
    data_origins = property(__data_origins.value, __data_origins.set, None, None)

    
    # Element data_analysis uses Python identifier data_analysis
    __data_analysis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'data_analysis'), 'data_analysis', '__metadata_metadata_data_analysis', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 318, 16), )

    
    data_analysis = property(__data_analysis.value, __data_analysis.set, None, None)

    
    # Element rights uses Python identifier rights
    __rights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rights'), 'rights', '__metadata_metadata_rights', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 319, 16), )

    
    rights = property(__rights.value, __rights.set, None, None)

    
    # Element cell_origin uses Python identifier cell_origin
    __cell_origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_origin'), 'cell_origin', '__metadata_metadata_cell_origin', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 320, 16), )

    
    cell_origin = property(__cell_origin.value, __cell_origin.set, None, None)

    
    # Element current_time uses Python identifier current_time
    __current_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'current_time'), 'current_time', '__metadata_metadata_current_time', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 321, 16), )

    
    current_time = property(__current_time.value, __current_time.set, None, None)

    
    # Element current_runtime uses Python identifier current_runtime
    __current_runtime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'current_runtime'), 'current_runtime', '__metadata_metadata_current_runtime', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 322, 16), )

    
    current_runtime = property(__current_runtime.value, __current_runtime.set, None, None)

    
    # Element created uses Python identifier created
    __created = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'created'), 'created', '__metadata_metadata_created', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 323, 16), )

    
    created = property(__created.value, __created.set, None, None)

    
    # Element last_modified uses Python identifier last_modified
    __last_modified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'last_modified'), 'last_modified', '__metadata_metadata_last_modified', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 324, 16), )

    
    last_modified = property(__last_modified.value, __last_modified.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'notes'), 'notes', '__metadata_metadata_notes', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 325, 16), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__metadata_metadata_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 326, 16), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __MultiCellDB.name() : __MultiCellDB,
        __description.name() : __description,
        __software.name() : __software,
        __citation.name() : __citation,
        __curation.name() : __curation,
        __data_origins.name() : __data_origins,
        __data_analysis.name() : __data_analysis,
        __rights.name() : __rights,
        __cell_origin.name() : __cell_origin,
        __current_time.name() : __current_time,
        __current_runtime.name() : __current_runtime,
        __created.name() : __created,
        __last_modified.name() : __last_modified,
        __notes.name() : __notes,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.metadata = metadata
Namespace.addCategoryObject('typeBinding', 'metadata', metadata)




orcid_identifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'path'), pyxb.binding.datatypes.string, scope=orcid_identifier, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 25, 16)))

orcid_identifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'given-names'), pyxb.binding.datatypes.string, scope=orcid_identifier, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 26, 16)))

orcid_identifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'family-name'), pyxb.binding.datatypes.string, scope=orcid_identifier, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 27, 16)))

orcid_identifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'email'), pyxb.binding.datatypes.string, scope=orcid_identifier, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 28, 16)))

orcid_identifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'url'), URL, scope=orcid_identifier, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 29, 16)))

orcid_identifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'organization-name'), pyxb.binding.datatypes.string, scope=orcid_identifier, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 30, 16)))

orcid_identifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'department-name'), pyxb.binding.datatypes.string, scope=orcid_identifier, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 31, 16)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 25, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(orcid_identifier._UseForTag(pyxb.namespace.ExpandedName(None, 'path')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 25, 16))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 26, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(orcid_identifier._UseForTag(pyxb.namespace.ExpandedName(None, 'given-names')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 26, 16))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 27, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(orcid_identifier._UseForTag(pyxb.namespace.ExpandedName(None, 'family-name')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 27, 16))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 28, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(orcid_identifier._UseForTag(pyxb.namespace.ExpandedName(None, 'email')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 28, 16))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 29, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(orcid_identifier._UseForTag(pyxb.namespace.ExpandedName(None, 'url')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 29, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 30, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(orcid_identifier._UseForTag(pyxb.namespace.ExpandedName(None, 'organization-name')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 30, 16))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 31, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(orcid_identifier._UseForTag(pyxb.namespace.ExpandedName(None, 'department-name')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 31, 16))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 25, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 26, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 27, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 28, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 29, 16))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 30, 16))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 31, 16))
    counters.add(cc_6)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    sub_automata.append(_BuildAutomaton_6())
    sub_automata.append(_BuildAutomaton_7())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 24, 12)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
orcid_identifier._Automaton = _BuildAutomaton()




orcid_person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orcid-identifier'), orcid_identifier, scope=orcid_person, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 40, 16)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(orcid_person._UseForTag(pyxb.namespace.ExpandedName(None, 'orcid-identifier')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 40, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
orcid_person._Automaton = _BuildAutomaton_8()




curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'created'), pyxb.binding.datatypes.dateTime, scope=curation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 56, 16)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'last_modified'), pyxb.binding.datatypes.dateTime, scope=curation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 57, 16)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'classification'), classification, scope=curation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 59, 20)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'version'), pyxb.binding.datatypes.string, scope=curation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 60, 20)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'creator'), orcid_person, scope=curation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 63, 16)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'current_contact'), orcid_person, scope=curation, documentation='\n                            This element could be like the PersonContact in NCO\n                        ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 65, 16)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'curator'), orcid_person, scope=curation, documentation='\n                            This element is required for a cell line. The schematron test for this is in the parent complexType/class.\n                        ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 73, 16)))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'last_modified_by'), orcid_person, scope=curation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 80, 16)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 73, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 82, 16))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, 'created')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 56, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, 'last_modified')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 57, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, 'classification')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 59, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, 'version')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 60, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, 'creator')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 63, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, 'current_contact')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 65, 16))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, 'curator')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 73, 16))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(curation._UseForTag(pyxb.namespace.ExpandedName(None, 'last_modified_by')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 80, 16))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 82, 16))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
curation._Automaton = _BuildAutomaton_9()




classification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'classification_number'), pyxb.binding.datatypes.string, scope=classification, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 90, 12)))

classification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'line'), pyxb.binding.datatypes.unsignedInt, scope=classification, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 91, 12)))

classification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'variant'), pyxb.binding.datatypes.unsignedInt, scope=classification, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 92, 12)))

classification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'branch'), pyxb.binding.datatypes.unsignedInt, scope=classification, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 93, 12)))

classification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'version'), pyxb.binding.datatypes.unsignedInt, scope=classification, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 94, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(classification._UseForTag(pyxb.namespace.ExpandedName(None, 'classification_number')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 90, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(classification._UseForTag(pyxb.namespace.ExpandedName(None, 'line')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 91, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(classification._UseForTag(pyxb.namespace.ExpandedName(None, 'variant')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 92, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(classification._UseForTag(pyxb.namespace.ExpandedName(None, 'branch')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 93, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(classification._UseForTag(pyxb.namespace.ExpandedName(None, 'version')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 94, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
classification._Automaton = _BuildAutomaton_10()




citation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'text'), pyxb.binding.datatypes.string, scope=citation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 106, 16)))

citation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DOI'), pyxb.binding.datatypes.string, scope=citation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 107, 16)))

citation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'URL'), URL, scope=citation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 108, 16)))

citation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PMID'), pyxb.binding.datatypes.string, scope=citation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 109, 16)))

citation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PMCID'), pyxb.binding.datatypes.string, scope=citation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 110, 16)))

citation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'arXiv'), pyxb.binding.datatypes.string, scope=citation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 111, 16)))

citation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'notes'), pyxb.binding.datatypes.string, scope=citation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 112, 16)))

citation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=citation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 113, 16)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 106, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 107, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 108, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 109, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 110, 16))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 111, 16))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 112, 16))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 113, 16))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(citation._UseForTag(pyxb.namespace.ExpandedName(None, 'text')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 106, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(citation._UseForTag(pyxb.namespace.ExpandedName(None, 'DOI')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 107, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(citation._UseForTag(pyxb.namespace.ExpandedName(None, 'URL')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 108, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(citation._UseForTag(pyxb.namespace.ExpandedName(None, 'PMID')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 109, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(citation._UseForTag(pyxb.namespace.ExpandedName(None, 'PMCID')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 110, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(citation._UseForTag(pyxb.namespace.ExpandedName(None, 'arXiv')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 111, 16))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(citation._UseForTag(pyxb.namespace.ExpandedName(None, 'notes')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 112, 16))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(citation._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 113, 16))
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
citation._Automaton = _BuildAutomaton_11()




data_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'instrumentation_information'), pyxb.binding.datatypes.string, scope=data_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 125, 16)))

data_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'experimental_protocol'), pyxb.binding.datatypes.string, scope=data_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 126, 16)))

data_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'citation'), citation, scope=data_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 127, 16)))

data_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'xpath'), pyxb.binding.datatypes.string, scope=data_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 128, 16)))

data_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'notes'), pyxb.binding.datatypes.string, scope=data_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 129, 16)))

data_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=data_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 130, 16)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 125, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 126, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 127, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 128, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 129, 16))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 130, 16))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(data_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'instrumentation_information')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 125, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(data_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'experimental_protocol')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 126, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(data_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'citation')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 127, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(data_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'xpath')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 128, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(data_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'notes')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 129, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(data_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 130, 16))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
data_origin._Automaton = _BuildAutomaton_12()




data_origins._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'data_origin'), data_origin, scope=data_origins, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 139, 16)))

data_origins._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=data_origins, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 140, 16)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 140, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(data_origins._UseForTag(pyxb.namespace.ExpandedName(None, 'data_origin')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 139, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(data_origins._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 140, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
data_origins._Automaton = _BuildAutomaton_13()




data_analysis._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'URL'), URL, scope=data_analysis, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 152, 16)))

data_analysis._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'citation'), citation, scope=data_analysis, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 153, 16)))

data_analysis._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'software'), software, scope=data_analysis, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 154, 16)))

data_analysis._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'xpath'), pyxb.binding.datatypes.string, scope=data_analysis, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 155, 16)))

data_analysis._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'notes'), pyxb.binding.datatypes.string, scope=data_analysis, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 156, 16)))

data_analysis._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=data_analysis, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 157, 16)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 152, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 153, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 154, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 155, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 156, 16))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 157, 16))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(data_analysis._UseForTag(pyxb.namespace.ExpandedName(None, 'URL')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 152, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(data_analysis._UseForTag(pyxb.namespace.ExpandedName(None, 'citation')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 153, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(data_analysis._UseForTag(pyxb.namespace.ExpandedName(None, 'software')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 154, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(data_analysis._UseForTag(pyxb.namespace.ExpandedName(None, 'xpath')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 155, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(data_analysis._UseForTag(pyxb.namespace.ExpandedName(None, 'notes')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 156, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(data_analysis._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 157, 16))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
data_analysis._Automaton = _BuildAutomaton_14()




software._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'software_name'), pyxb.binding.datatypes.string, scope=software, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 182, 12)))

software._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'software_version'), pyxb.binding.datatypes.string, scope=software, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 183, 12)))

software._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'software_input_configuration'), _ImportedBinding_common.custom, scope=software, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 184, 12)))

software._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=software, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 185, 12)))

software._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'version'), pyxb.binding.datatypes.string, scope=software, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 186, 12)))

software._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'input_configuration'), _ImportedBinding_common.custom, scope=software, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 187, 12)))

software._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'URL'), URL, scope=software, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 188, 12)))

software._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'creator'), orcid_person, scope=software, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 189, 12)))

software._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'citation'), citation, scope=software, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 190, 12)))

software._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'user'), orcid_person, scope=software, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 191, 12)))

software._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=software, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 192, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 182, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 183, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 184, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 185, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 186, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 187, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 188, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 189, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 190, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 191, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 192, 12))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(software._UseForTag(pyxb.namespace.ExpandedName(None, 'software_name')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 182, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(software._UseForTag(pyxb.namespace.ExpandedName(None, 'software_version')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 183, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(software._UseForTag(pyxb.namespace.ExpandedName(None, 'software_input_configuration')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 184, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(software._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 185, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(software._UseForTag(pyxb.namespace.ExpandedName(None, 'version')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 186, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(software._UseForTag(pyxb.namespace.ExpandedName(None, 'input_configuration')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 187, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(software._UseForTag(pyxb.namespace.ExpandedName(None, 'URL')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 188, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(software._UseForTag(pyxb.namespace.ExpandedName(None, 'creator')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 189, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(software._UseForTag(pyxb.namespace.ExpandedName(None, 'citation')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 190, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(software._UseForTag(pyxb.namespace.ExpandedName(None, 'user')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 191, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(software._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 192, 12))
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
software._Automaton = _BuildAutomaton_15()




cell_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BTO_ID'), pyxb.binding.datatypes.string, scope=cell_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 224, 12)))

cell_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CLO_ID'), pyxb.binding.datatypes.string, scope=cell_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 225, 12)))

cell_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'species'), species, scope=cell_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 226, 12)))

cell_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'strain'), pyxb.binding.datatypes.string, scope=cell_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 227, 12)))

cell_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'organ'), pyxb.binding.datatypes.string, scope=cell_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 228, 12)))

cell_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'disease'), disease, scope=cell_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 229, 12)))

cell_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'morphology'), pyxb.binding.datatypes.string, scope=cell_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 230, 12)))

cell_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'patient_derived'), patient_derived, scope=cell_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 231, 12)))

cell_origin._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=cell_origin, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 232, 12)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 224, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'BTO_ID')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 224, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 225, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'CLO_ID')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 225, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 226, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'species')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 226, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 227, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'strain')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 227, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 228, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'organ')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 228, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 229, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'disease')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 229, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 230, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'morphology')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 230, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 231, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'patient_derived')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 231, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 232, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_origin._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 232, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 224, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 225, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 226, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 227, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 228, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 229, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 230, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 231, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 232, 12))
    counters.add(cc_8)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_17())
    sub_automata.append(_BuildAutomaton_18())
    sub_automata.append(_BuildAutomaton_19())
    sub_automata.append(_BuildAutomaton_20())
    sub_automata.append(_BuildAutomaton_21())
    sub_automata.append(_BuildAutomaton_22())
    sub_automata.append(_BuildAutomaton_23())
    sub_automata.append(_BuildAutomaton_24())
    sub_automata.append(_BuildAutomaton_25())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 223, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cell_origin._Automaton = _BuildAutomaton_16()




MultiCellDB._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ID'), pyxb.binding.datatypes.string, scope=MultiCellDB, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 267, 12)))

MultiCellDB._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=MultiCellDB, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 268, 12)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 267, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MultiCellDB._UseForTag(pyxb.namespace.ExpandedName(None, 'ID')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 267, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 268, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MultiCellDB._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 268, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 267, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 268, 12))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_27())
    sub_automata.append(_BuildAutomaton_28())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 266, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MultiCellDB._Automaton = _BuildAutomaton_26()




rights._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'license'), license, scope=rights, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 279, 12)))

rights._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=rights, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 280, 12)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 280, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(rights._UseForTag(pyxb.namespace.ExpandedName(None, 'license')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 279, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(rights._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 280, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
rights._Automaton = _BuildAutomaton_29()




license._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LicenseDocument'), LicenseDocument, scope=license, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 291, 12)))

license._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'notes'), pyxb.binding.datatypes.string, scope=license, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 292, 12)))

license._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=license, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 293, 12)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 292, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 293, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(license._UseForTag(pyxb.namespace.ExpandedName(None, 'LicenseDocument')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 291, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(license._UseForTag(pyxb.namespace.ExpandedName(None, 'notes')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 292, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(license._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 293, 12))
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
license._Automaton = _BuildAutomaton_30()




LicenseDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=LicenseDocument, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 304, 12), unicode_default='CC BY 4.0'))

LicenseDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'URL'), URL, scope=LicenseDocument, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 305, 12), unicode_default='https://creativecommons.org/licenses/by/4.0/'))

LicenseDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=LicenseDocument, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 306, 12)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 305, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 306, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LicenseDocument._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 304, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LicenseDocument._UseForTag(pyxb.namespace.ExpandedName(None, 'URL')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 305, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LicenseDocument._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 306, 12))
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
LicenseDocument._Automaton = _BuildAutomaton_31()




metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MultiCellDB'), MultiCellDB, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 312, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 313, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'software'), software, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 314, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'citation'), citation, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 315, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'curation'), curation, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 316, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'data_origins'), data_origins, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 317, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'data_analysis'), data_analysis, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 318, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rights'), rights, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 319, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_origin'), cell_origin, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 320, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'current_time'), _ImportedBinding_common.units_decimal_nonnegative, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 321, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'current_runtime'), _ImportedBinding_common.units_decimal_nonnegative, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 322, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'created'), pyxb.binding.datatypes.dateTime, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 323, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'last_modified'), pyxb.binding.datatypes.dateTime, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 324, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'notes'), pyxb.binding.datatypes.string, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 325, 16)))

metadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=metadata, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 326, 16)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 312, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 313, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 314, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 315, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 316, 16))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 317, 16))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 318, 16))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 320, 16))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 321, 16))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 322, 16))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 323, 16))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 324, 16))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 325, 16))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 326, 16))
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'MultiCellDB')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 312, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 313, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'software')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 314, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'citation')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 315, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'curation')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 316, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'data_origins')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 317, 16))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'data_analysis')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 318, 16))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'rights')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 319, 16))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_origin')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 320, 16))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'current_time')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 321, 16))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'current_runtime')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 322, 16))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'created')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 323, 16))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'last_modified')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 324, 16))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'notes')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 325, 16))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(metadata._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/metadata.xsd', 326, 16))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
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
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
metadata._Automaton = _BuildAutomaton_32()

