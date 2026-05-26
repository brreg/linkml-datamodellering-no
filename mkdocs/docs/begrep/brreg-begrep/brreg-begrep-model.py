# Auto generated from brreg-begrep-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-24T12:07:29
# Schema: brreg-begrep
#
# id: https://data.norge.no/linkml/brreg-begrep
# description: Begrepskatalog for Registerenheten i Brønnøysund. Begreper modellert lokalt med midlertidige URI-ar, klare for validering og eksport til Felles Begrepskatalog.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDate

metamodel_version = "1.11.0"
version = "1.0.0"

# Namespaces
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms#')
CAPNO = CurieNamespace('capno', 'https://data.norge.no/linkml/common-ap-no/')
CV = CurieNamespace('cv', 'http://data.europa.eu/m8g/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
EUVOC = CurieNamespace('euvoc', 'http://publications.europa.eu/ontology/euvoc#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ORG = CurieNamespace('org', 'http://www.w3.org/ns/org#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SKOSNO = CurieNamespace('skosno', 'https://data.norge.no/vocabulary/skosno#')
UNESKOS = CurieNamespace('uneskos', 'http://purl.org/umu/uneskos#')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns#')
XKOS = CurieNamespace('xkos', 'http://rdf-vocabulary.ddialliance.org/xkos#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://data.norge.no/linkml/brreg-begrep/')


# Types
class Spraak(str):
    """ Språk """
    type_class_uri = DCT["language"]
    type_class_curie = "dct:language"
    type_name = "Spraak"
    type_model_uri = URIRef("https://data.norge.no/linkml/brreg-begrep/Spraak")


class LangString(str):
    """ Språktagget streng (rdf:langString). """
    type_class_uri = RDF["langString"]
    type_class_curie = "rdf:langString"
    type_name = "LangString"
    type_model_uri = URIRef("https://data.norge.no/linkml/brreg-begrep/LangString")


class NonNegativeInteger(int):
    """ Ikkje-negativ heltalsverdi (xsd:nonNegativeInteger). """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "NonNegativeInteger"
    type_model_uri = URIRef("https://data.norge.no/linkml/brreg-begrep/NonNegativeInteger")


class Duration(str):
    """ ISO 8601-varigheit (xsd:duration), t.d. PT15M. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "Duration"
    type_model_uri = URIRef("https://data.norge.no/linkml/brreg-begrep/Duration")


class GYear(str):
    """ Gregorisk årstal (xsd:gYear), t.d. 2024. """
    type_class_uri = XSD["gYear"]
    type_class_curie = "xsd:gYear"
    type_name = "GYear"
    type_model_uri = URIRef("https://data.norge.no/linkml/brreg-begrep/GYear")


# Class references
class OrganisasjonId(URIorCURIE):
    pass


class VCardKontaktId(URIorCURIE):
    pass


class BegrepId(URIorCURIE):
    pass


class DefinisjonId(URIorCURIE):
    pass


class AssosiativRelasjonId(URIorCURIE):
    pass


class GeneriskRelasjonId(URIorCURIE):
    pass


class PartitivRelasjonId(URIorCURIE):
    pass


class SamlingId(URIorCURIE):
    pass


class MediatypeId(URIorCURIE):
    pass


class KonseptId(URIorCURIE):
    pass


class BegrepssamlingId(URIorCURIE):
    pass


@dataclass(repr=False)
class BegrepContainer(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/brreg-begrep/BegrepContainer")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BegrepContainer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/brreg-begrep/BegrepContainer")

    begrep: Optional[Union[dict[Union[str, BegrepId], Union[dict, "Begrep"]], list[Union[dict, "Begrep"]]]] = empty_dict()
    samlingar: Optional[Union[dict[Union[str, SamlingId], Union[dict, "Samling"]], list[Union[dict, "Samling"]]]] = empty_dict()
    definisjoner: Optional[Union[dict[Union[str, DefinisjonId], Union[dict, "Definisjon"]], list[Union[dict, "Definisjon"]]]] = empty_dict()
    generiske_relasjonar: Optional[Union[dict[Union[str, GeneriskRelasjonId], Union[dict, "GeneriskRelasjon"]], list[Union[dict, "GeneriskRelasjon"]]]] = empty_dict()
    partitive_relasjonar: Optional[Union[dict[Union[str, PartitivRelasjonId], Union[dict, "PartitivRelasjon"]], list[Union[dict, "PartitivRelasjon"]]]] = empty_dict()
    assosiative_relasjonar: Optional[Union[dict[Union[str, AssosiativRelasjonId], Union[dict, "AssosiativRelasjon"]], list[Union[dict, "AssosiativRelasjon"]]]] = empty_dict()
    organisasjonar: Optional[Union[list[Union[str, OrganisasjonId]], dict[Union[str, OrganisasjonId], Union[dict, "Organisasjon"]]]] = empty_dict()
    kontaktpunkt: Optional[Union[list[Union[str, VCardKontaktId]], dict[Union[str, VCardKontaktId], Union[dict, "VCardKontakt"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="begrep", slot_type=Begrep, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="samlingar", slot_type=Samling, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="definisjoner", slot_type=Definisjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="generiske_relasjonar", slot_type=GeneriskRelasjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="partitive_relasjonar", slot_type=PartitivRelasjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="assosiative_relasjonar", slot_type=AssosiativRelasjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="organisasjonar", slot_type=Organisasjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kontaktpunkt", slot_type=VCardKontakt, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organisasjon(YAMLRoot):
    """
    Ein organisasjon som er utgjevar eller ansvarleg for eit omgrep.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ORG["Organization"]
    class_class_curie: ClassVar[str] = "org:Organization"
    class_name: ClassVar[str] = "Organisasjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/brreg-begrep/Organisasjon")

    id: Union[str, OrganisasjonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganisasjonId):
            self.id = OrganisasjonId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VCardKontakt(YAMLRoot):
    """
    Kontaktinformasjon (vCard) for omgrepseigaren.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VCARD["Kind"]
    class_class_curie: ClassVar[str] = "vcard:Kind"
    class_name: ClassVar[str] = "VCardKontakt"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/brreg-begrep/VCardKontakt")

    id: Union[str, VCardKontaktId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VCardKontaktId):
            self.id = VCardKontaktId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Begrep(YAMLRoot):
    """
    Eit omgrep med definisjon og tilhøyrande metadata (skos:Concept).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["Concept"]
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "Begrep"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/brreg-begrep/Begrep")

    id: Union[str, BegrepId] = None
    anbefalt_term: Union[str, list[str]] = None
    identifikator_literal: str = None
    kontaktpunkt_vcard: Union[Union[str, VCardKontaktId], list[Union[str, VCardKontaktId]]] = None
    utgjevar: Union[str, OrganisasjonId] = None
    definisjon: Optional[Union[str, list[str]]] = empty_list()
    har_definisjon: Optional[Union[Union[str, DefinisjonId], list[Union[str, DefinisjonId]]]] = empty_list()
    ansvarleg_verksemd: Optional[Union[str, OrganisasjonId]] = None
    gyldig_fra: Optional[Union[str, XSDDate]] = None
    gyldig_til: Optional[Union[str, XSDDate]] = None
    opprettingsdato: Optional[Union[str, XSDDate]] = None
    endringsdato: Optional[Union[str, XSDDate]] = None
    fagomrade: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    merknad: Optional[Union[str, list[str]]] = empty_list()
    tillate_term: Optional[Union[str, list[str]]] = empty_list()
    datastruktur_term: Optional[Union[str, list[str]]] = empty_list()
    eksempel: Optional[Union[str, list[str]]] = empty_list()
    er_del_av_omgrep: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    er_erstatta_av: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    er_fra_omgrep_i: Optional[Union[Union[str, AssosiativRelasjonId], list[Union[str, AssosiativRelasjonId]]]] = empty_list()
    assosiert_med: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    erstattar: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    forkasta_term: Optional[Union[str, list[str]]] = empty_list()
    generaliserer: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    noyaktig_samsvar: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    har_generisk_relasjon: Optional[Union[Union[str, GeneriskRelasjonId], list[Union[str, GeneriskRelasjonId]]]] = empty_list()
    naert_samsvar: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    har_partitiv_relasjon: Optional[Union[Union[str, PartitivRelasjonId], list[Union[str, PartitivRelasjonId]]]] = empty_list()
    har_del_omgrep: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    er_medlem_av: Optional[Union[Union[str, SamlingId], list[Union[str, SamlingId]]]] = empty_list()
    sja_ogsa_omgrep: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    spesifiserer: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    euvoc_status: Optional[Union[str, BegrepId]] = None
    verdiomrade: Optional[Union[str, list[str]]] = empty_list()
    har_versjonsnummer: Optional[str] = None
    versjonsmerknad: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BegrepId):
            self.id = BegrepId(self.id)

        if self._is_empty(self.anbefalt_term):
            self.MissingRequiredField("anbefalt_term")
        if not isinstance(self.anbefalt_term, list):
            self.anbefalt_term = [self.anbefalt_term] if self.anbefalt_term is not None else []
        self.anbefalt_term = [v if isinstance(v, str) else str(v) for v in self.anbefalt_term]

        if self._is_empty(self.identifikator_literal):
            self.MissingRequiredField("identifikator_literal")
        if not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self._is_empty(self.kontaktpunkt_vcard):
            self.MissingRequiredField("kontaktpunkt_vcard")
        if not isinstance(self.kontaktpunkt_vcard, list):
            self.kontaktpunkt_vcard = [self.kontaktpunkt_vcard] if self.kontaktpunkt_vcard is not None else []
        self.kontaktpunkt_vcard = [v if isinstance(v, VCardKontaktId) else VCardKontaktId(v) for v in self.kontaktpunkt_vcard]

        if self._is_empty(self.utgjevar):
            self.MissingRequiredField("utgjevar")
        if not isinstance(self.utgjevar, OrganisasjonId):
            self.utgjevar = OrganisasjonId(self.utgjevar)

        if not isinstance(self.definisjon, list):
            self.definisjon = [self.definisjon] if self.definisjon is not None else []
        self.definisjon = [v if isinstance(v, str) else str(v) for v in self.definisjon]

        if not isinstance(self.har_definisjon, list):
            self.har_definisjon = [self.har_definisjon] if self.har_definisjon is not None else []
        self.har_definisjon = [v if isinstance(v, DefinisjonId) else DefinisjonId(v) for v in self.har_definisjon]

        if self.ansvarleg_verksemd is not None and not isinstance(self.ansvarleg_verksemd, OrganisasjonId):
            self.ansvarleg_verksemd = OrganisasjonId(self.ansvarleg_verksemd)

        if self.gyldig_fra is not None and not isinstance(self.gyldig_fra, XSDDate):
            self.gyldig_fra = XSDDate(self.gyldig_fra)

        if self.gyldig_til is not None and not isinstance(self.gyldig_til, XSDDate):
            self.gyldig_til = XSDDate(self.gyldig_til)

        if self.opprettingsdato is not None and not isinstance(self.opprettingsdato, XSDDate):
            self.opprettingsdato = XSDDate(self.opprettingsdato)

        if self.endringsdato is not None and not isinstance(self.endringsdato, XSDDate):
            self.endringsdato = XSDDate(self.endringsdato)

        if not isinstance(self.fagomrade, list):
            self.fagomrade = [self.fagomrade] if self.fagomrade is not None else []
        self.fagomrade = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.fagomrade]

        if not isinstance(self.merknad, list):
            self.merknad = [self.merknad] if self.merknad is not None else []
        self.merknad = [v if isinstance(v, str) else str(v) for v in self.merknad]

        if not isinstance(self.tillate_term, list):
            self.tillate_term = [self.tillate_term] if self.tillate_term is not None else []
        self.tillate_term = [v if isinstance(v, str) else str(v) for v in self.tillate_term]

        if not isinstance(self.datastruktur_term, list):
            self.datastruktur_term = [self.datastruktur_term] if self.datastruktur_term is not None else []
        self.datastruktur_term = [v if isinstance(v, str) else str(v) for v in self.datastruktur_term]

        if not isinstance(self.eksempel, list):
            self.eksempel = [self.eksempel] if self.eksempel is not None else []
        self.eksempel = [v if isinstance(v, str) else str(v) for v in self.eksempel]

        if not isinstance(self.er_del_av_omgrep, list):
            self.er_del_av_omgrep = [self.er_del_av_omgrep] if self.er_del_av_omgrep is not None else []
        self.er_del_av_omgrep = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.er_del_av_omgrep]

        if not isinstance(self.er_erstatta_av, list):
            self.er_erstatta_av = [self.er_erstatta_av] if self.er_erstatta_av is not None else []
        self.er_erstatta_av = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.er_erstatta_av]

        if not isinstance(self.er_fra_omgrep_i, list):
            self.er_fra_omgrep_i = [self.er_fra_omgrep_i] if self.er_fra_omgrep_i is not None else []
        self.er_fra_omgrep_i = [v if isinstance(v, AssosiativRelasjonId) else AssosiativRelasjonId(v) for v in self.er_fra_omgrep_i]

        if not isinstance(self.assosiert_med, list):
            self.assosiert_med = [self.assosiert_med] if self.assosiert_med is not None else []
        self.assosiert_med = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.assosiert_med]

        if not isinstance(self.erstattar, list):
            self.erstattar = [self.erstattar] if self.erstattar is not None else []
        self.erstattar = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.erstattar]

        if not isinstance(self.forkasta_term, list):
            self.forkasta_term = [self.forkasta_term] if self.forkasta_term is not None else []
        self.forkasta_term = [v if isinstance(v, str) else str(v) for v in self.forkasta_term]

        if not isinstance(self.generaliserer, list):
            self.generaliserer = [self.generaliserer] if self.generaliserer is not None else []
        self.generaliserer = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.generaliserer]

        if not isinstance(self.noyaktig_samsvar, list):
            self.noyaktig_samsvar = [self.noyaktig_samsvar] if self.noyaktig_samsvar is not None else []
        self.noyaktig_samsvar = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.noyaktig_samsvar]

        if not isinstance(self.har_generisk_relasjon, list):
            self.har_generisk_relasjon = [self.har_generisk_relasjon] if self.har_generisk_relasjon is not None else []
        self.har_generisk_relasjon = [v if isinstance(v, GeneriskRelasjonId) else GeneriskRelasjonId(v) for v in self.har_generisk_relasjon]

        if not isinstance(self.naert_samsvar, list):
            self.naert_samsvar = [self.naert_samsvar] if self.naert_samsvar is not None else []
        self.naert_samsvar = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.naert_samsvar]

        if not isinstance(self.har_partitiv_relasjon, list):
            self.har_partitiv_relasjon = [self.har_partitiv_relasjon] if self.har_partitiv_relasjon is not None else []
        self.har_partitiv_relasjon = [v if isinstance(v, PartitivRelasjonId) else PartitivRelasjonId(v) for v in self.har_partitiv_relasjon]

        if not isinstance(self.har_del_omgrep, list):
            self.har_del_omgrep = [self.har_del_omgrep] if self.har_del_omgrep is not None else []
        self.har_del_omgrep = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.har_del_omgrep]

        if not isinstance(self.er_medlem_av, list):
            self.er_medlem_av = [self.er_medlem_av] if self.er_medlem_av is not None else []
        self.er_medlem_av = [v if isinstance(v, SamlingId) else SamlingId(v) for v in self.er_medlem_av]

        if not isinstance(self.sja_ogsa_omgrep, list):
            self.sja_ogsa_omgrep = [self.sja_ogsa_omgrep] if self.sja_ogsa_omgrep is not None else []
        self.sja_ogsa_omgrep = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.sja_ogsa_omgrep]

        if not isinstance(self.spesifiserer, list):
            self.spesifiserer = [self.spesifiserer] if self.spesifiserer is not None else []
        self.spesifiserer = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.spesifiserer]

        if self.euvoc_status is not None and not isinstance(self.euvoc_status, BegrepId):
            self.euvoc_status = BegrepId(self.euvoc_status)

        if not isinstance(self.verdiomrade, list):
            self.verdiomrade = [self.verdiomrade] if self.verdiomrade is not None else []
        self.verdiomrade = [v if isinstance(v, str) else str(v) for v in self.verdiomrade]

        if self.har_versjonsnummer is not None and not isinstance(self.har_versjonsnummer, str):
            self.har_versjonsnummer = str(self.har_versjonsnummer)

        if not isinstance(self.versjonsmerknad, list):
            self.versjonsmerknad = [self.versjonsmerknad] if self.versjonsmerknad is not None else []
        self.versjonsmerknad = [v if isinstance(v, str) else str(v) for v in self.versjonsmerknad]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Definisjon(YAMLRoot):
    """
    Ein definisjon av eit omgrep via eit eige objekt (euvoc:XlNote).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EUVOC["XlNote"]
    class_class_curie: ClassVar[str] = "euvoc:XlNote"
    class_name: ClassVar[str] = "Definisjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/brreg-begrep/Definisjon")

    id: Union[str, DefinisjonId] = None
    tekst: str = None
    kjelde_relasjon: Optional[Union[str, BegrepId]] = None
    kjelde: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    malgruppe_def: Optional[Union[str, BegrepId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DefinisjonId):
            self.id = DefinisjonId(self.id)

        if self._is_empty(self.tekst):
            self.MissingRequiredField("tekst")
        if not isinstance(self.tekst, str):
            self.tekst = str(self.tekst)

        if self.kjelde_relasjon is not None and not isinstance(self.kjelde_relasjon, BegrepId):
            self.kjelde_relasjon = BegrepId(self.kjelde_relasjon)

        if not isinstance(self.kjelde, list):
            self.kjelde = [self.kjelde] if self.kjelde is not None else []
        self.kjelde = [v if isinstance(v, URI) else URI(v) for v in self.kjelde]

        if self.malgruppe_def is not None and not isinstance(self.malgruppe_def, BegrepId):
            self.malgruppe_def = BegrepId(self.malgruppe_def)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssosiativRelasjon(YAMLRoot):
    """
    Ein assosiativ relasjon mellom to omgrep.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOSNO["AssociativeConceptRelation"]
    class_class_curie: ClassVar[str] = "skosno:AssociativeConceptRelation"
    class_name: ClassVar[str] = "AssosiativRelasjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/brreg-begrep/AssosiativRelasjon")

    id: Union[str, AssosiativRelasjonId] = None
    til_omgrep: Union[Union[str, BegrepId], list[Union[str, BegrepId]]] = None
    relasjontype: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssosiativRelasjonId):
            self.id = AssosiativRelasjonId(self.id)

        if self._is_empty(self.til_omgrep):
            self.MissingRequiredField("til_omgrep")
        if not isinstance(self.til_omgrep, list):
            self.til_omgrep = [self.til_omgrep] if self.til_omgrep is not None else []
        self.til_omgrep = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.til_omgrep]

        if self._is_empty(self.relasjontype):
            self.MissingRequiredField("relasjontype")
        if not isinstance(self.relasjontype, str):
            self.relasjontype = str(self.relasjontype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneriskRelasjon(YAMLRoot):
    """
    Ein generisk relasjon mellom eit overomgrep og eit underomgrep.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOSNO["GenericConceptRelation"]
    class_class_curie: ClassVar[str] = "skosno:GenericConceptRelation"
    class_name: ClassVar[str] = "GeneriskRelasjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/brreg-begrep/GeneriskRelasjon")

    id: Union[str, GeneriskRelasjonId] = None
    har_generisk_omgrep: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    har_spesifikt_omgrep: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    inndelingskriterium: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneriskRelasjonId):
            self.id = GeneriskRelasjonId(self.id)

        if not isinstance(self.har_generisk_omgrep, list):
            self.har_generisk_omgrep = [self.har_generisk_omgrep] if self.har_generisk_omgrep is not None else []
        self.har_generisk_omgrep = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.har_generisk_omgrep]

        if not isinstance(self.har_spesifikt_omgrep, list):
            self.har_spesifikt_omgrep = [self.har_spesifikt_omgrep] if self.har_spesifikt_omgrep is not None else []
        self.har_spesifikt_omgrep = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.har_spesifikt_omgrep]

        if not isinstance(self.inndelingskriterium, list):
            self.inndelingskriterium = [self.inndelingskriterium] if self.inndelingskriterium is not None else []
        self.inndelingskriterium = [v if isinstance(v, str) else str(v) for v in self.inndelingskriterium]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PartitivRelasjon(YAMLRoot):
    """
    Ein partitiv relasjon mellom eit heilskapleg og eit partitivt omgrep.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOSNO["PartitiveConceptRelation"]
    class_class_curie: ClassVar[str] = "skosno:PartitiveConceptRelation"
    class_name: ClassVar[str] = "PartitivRelasjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/brreg-begrep/PartitivRelasjon")

    id: Union[str, PartitivRelasjonId] = None
    har_partitivt_omgrep: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    har_heilskapleg_omgrep: Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]] = empty_list()
    inndelingskriterium: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PartitivRelasjonId):
            self.id = PartitivRelasjonId(self.id)

        if not isinstance(self.har_partitivt_omgrep, list):
            self.har_partitivt_omgrep = [self.har_partitivt_omgrep] if self.har_partitivt_omgrep is not None else []
        self.har_partitivt_omgrep = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.har_partitivt_omgrep]

        if not isinstance(self.har_heilskapleg_omgrep, list):
            self.har_heilskapleg_omgrep = [self.har_heilskapleg_omgrep] if self.har_heilskapleg_omgrep is not None else []
        self.har_heilskapleg_omgrep = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.har_heilskapleg_omgrep]

        if not isinstance(self.inndelingskriterium, list):
            self.inndelingskriterium = [self.inndelingskriterium] if self.inndelingskriterium is not None else []
        self.inndelingskriterium = [v if isinstance(v, str) else str(v) for v in self.inndelingskriterium]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Samling(YAMLRoot):
    """
    Ei namngitt samling av omgrep (skos:Collection).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["Collection"]
    class_class_curie: ClassVar[str] = "skos:Collection"
    class_name: ClassVar[str] = "Samling"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/brreg-begrep/Samling")

    id: Union[str, SamlingId] = None
    identifikator_literal: str = None
    medlem: Union[Union[str, BegrepId], list[Union[str, BegrepId]]] = None
    kontaktpunkt_vcard: Union[Union[str, VCardKontaktId], list[Union[str, VCardKontaktId]]] = None
    tittel: Union[str, list[str]] = None
    utgjevar: Union[str, OrganisasjonId] = None
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SamlingId):
            self.id = SamlingId(self.id)

        if self._is_empty(self.identifikator_literal):
            self.MissingRequiredField("identifikator_literal")
        if not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self._is_empty(self.medlem):
            self.MissingRequiredField("medlem")
        if not isinstance(self.medlem, list):
            self.medlem = [self.medlem] if self.medlem is not None else []
        self.medlem = [v if isinstance(v, BegrepId) else BegrepId(v) for v in self.medlem]

        if self._is_empty(self.kontaktpunkt_vcard):
            self.MissingRequiredField("kontaktpunkt_vcard")
        if not isinstance(self.kontaktpunkt_vcard, list):
            self.kontaktpunkt_vcard = [self.kontaktpunkt_vcard] if self.kontaktpunkt_vcard is not None else []
        self.kontaktpunkt_vcard = [v if isinstance(v, VCardKontaktId) else VCardKontaktId(v) for v in self.kontaktpunkt_vcard]

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.utgjevar):
            self.MissingRequiredField("utgjevar")
        if not isinstance(self.utgjevar, OrganisasjonId):
            self.utgjevar = OrganisasjonId(self.utgjevar)

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Mediatype(YAMLRoot):
    """
    Ein medietype eller filformat (dct:MediaTypeOrExtent).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["MediaTypeOrExtent"]
    class_class_curie: ClassVar[str] = "dct:MediaTypeOrExtent"
    class_name: ClassVar[str] = "Mediatype"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/brreg-begrep/Mediatype")

    id: Union[str, MediatypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MediatypeId):
            self.id = MediatypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Konsept(YAMLRoot):
    """
    Referanse til eit SKOS-omgrep frå eit kontrollert vokabular.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["Concept"]
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "Konsept"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/brreg-begrep/Konsept")

    id: Union[str, KonseptId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KonseptId):
            self.id = KonseptId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Begrepssamling(YAMLRoot):
    """
    Ei SKOS-omgrepssamling (temavokabular).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["ConceptScheme"]
    class_class_curie: ClassVar[str] = "skos:ConceptScheme"
    class_name: ClassVar[str] = "Begrepssamling"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/brreg-begrep/Begrepssamling")

    id: Union[str, BegrepssamlingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BegrepssamlingId):
            self.id = BegrepssamlingId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.definisjon = Slot(uri=SKOS.definition, name="definisjon", curie=SKOS.curie('definition'),
                   model_uri=DEFAULT_.definisjon, domain=None, range=Optional[Union[str, list[str]]])

slots.har_definisjon = Slot(uri=EUVOC.xlDefinition, name="har_definisjon", curie=EUVOC.curie('xlDefinition'),
                   model_uri=DEFAULT_.har_definisjon, domain=None, range=Optional[Union[Union[str, DefinisjonId], list[Union[str, DefinisjonId]]]])

slots.kontaktpunkt_vcard = Slot(uri=DCAT.contactPoint, name="kontaktpunkt_vcard", curie=DCAT.curie('contactPoint'),
                   model_uri=DEFAULT_.kontaktpunkt_vcard, domain=None, range=Optional[Union[Union[str, VCardKontaktId], list[Union[str, VCardKontaktId]]]])

slots.utgjevar = Slot(uri=DCT.publisher, name="utgjevar", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.utgjevar, domain=None, range=Optional[Union[str, OrganisasjonId]])

slots.ansvarleg_verksemd = Slot(uri=DCT.creator, name="ansvarleg_verksemd", curie=DCT.curie('creator'),
                   model_uri=DEFAULT_.ansvarleg_verksemd, domain=None, range=Optional[Union[str, OrganisasjonId]])

slots.gyldig_fra = Slot(uri=EUVOC.startDate, name="gyldig_fra", curie=EUVOC.curie('startDate'),
                   model_uri=DEFAULT_.gyldig_fra, domain=None, range=Optional[Union[str, XSDDate]])

slots.gyldig_til = Slot(uri=EUVOC.endDate, name="gyldig_til", curie=EUVOC.curie('endDate'),
                   model_uri=DEFAULT_.gyldig_til, domain=None, range=Optional[Union[str, XSDDate]])

slots.opprettingsdato = Slot(uri=DCT.created, name="opprettingsdato", curie=DCT.curie('created'),
                   model_uri=DEFAULT_.opprettingsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.fagomrade = Slot(uri=DCT.subject, name="fagomrade", curie=DCT.curie('subject'),
                   model_uri=DEFAULT_.fagomrade, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.merknad = Slot(uri=SKOS.scopeNote, name="merknad", curie=SKOS.curie('scopeNote'),
                   model_uri=DEFAULT_.merknad, domain=None, range=Optional[Union[str, list[str]]])

slots.tillate_term = Slot(uri=SKOS.altLabel, name="tillate_term", curie=SKOS.curie('altLabel'),
                   model_uri=DEFAULT_.tillate_term, domain=None, range=Optional[Union[str, list[str]]])

slots.datastruktur_term = Slot(uri=SKOSNO.dataStructureLabel, name="datastruktur_term", curie=SKOSNO.curie('dataStructureLabel'),
                   model_uri=DEFAULT_.datastruktur_term, domain=None, range=Optional[Union[str, list[str]]])

slots.eksempel = Slot(uri=SKOS.example, name="eksempel", curie=SKOS.curie('example'),
                   model_uri=DEFAULT_.eksempel, domain=None, range=Optional[Union[str, list[str]]])

slots.er_del_av_omgrep = Slot(uri=XKOS.isPartOf, name="er_del_av_omgrep", curie=XKOS.curie('isPartOf'),
                   model_uri=DEFAULT_.er_del_av_omgrep, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.er_erstatta_av = Slot(uri=DCT.isReplacedBy, name="er_erstatta_av", curie=DCT.curie('isReplacedBy'),
                   model_uri=DEFAULT_.er_erstatta_av, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.er_fra_omgrep_i = Slot(uri=SKOSNO.isFromConceptIn, name="er_fra_omgrep_i", curie=SKOSNO.curie('isFromConceptIn'),
                   model_uri=DEFAULT_.er_fra_omgrep_i, domain=None, range=Optional[Union[Union[str, AssosiativRelasjonId], list[Union[str, AssosiativRelasjonId]]]])

slots.assosiert_med = Slot(uri=SKOS.related, name="assosiert_med", curie=SKOS.curie('related'),
                   model_uri=DEFAULT_.assosiert_med, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.erstattar = Slot(uri=DCT.replaces, name="erstattar", curie=DCT.curie('replaces'),
                   model_uri=DEFAULT_.erstattar, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.forkasta_term = Slot(uri=SKOS.hiddenLabel, name="forkasta_term", curie=SKOS.curie('hiddenLabel'),
                   model_uri=DEFAULT_.forkasta_term, domain=None, range=Optional[Union[str, list[str]]])

slots.generaliserer = Slot(uri=XKOS.generalizes, name="generaliserer", curie=XKOS.curie('generalizes'),
                   model_uri=DEFAULT_.generaliserer, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.noyaktig_samsvar = Slot(uri=SKOS.exactMatch, name="noyaktig_samsvar", curie=SKOS.curie('exactMatch'),
                   model_uri=DEFAULT_.noyaktig_samsvar, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.har_generisk_relasjon = Slot(uri=SKOSNO.hasGenericConceptRelation, name="har_generisk_relasjon", curie=SKOSNO.curie('hasGenericConceptRelation'),
                   model_uri=DEFAULT_.har_generisk_relasjon, domain=None, range=Optional[Union[Union[str, GeneriskRelasjonId], list[Union[str, GeneriskRelasjonId]]]])

slots.naert_samsvar = Slot(uri=SKOS.closeMatch, name="naert_samsvar", curie=SKOS.curie('closeMatch'),
                   model_uri=DEFAULT_.naert_samsvar, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.har_partitiv_relasjon = Slot(uri=SKOSNO.hasPartitiveConceptRelation, name="har_partitiv_relasjon", curie=SKOSNO.curie('hasPartitiveConceptRelation'),
                   model_uri=DEFAULT_.har_partitiv_relasjon, domain=None, range=Optional[Union[Union[str, PartitivRelasjonId], list[Union[str, PartitivRelasjonId]]]])

slots.har_del_omgrep = Slot(uri=XKOS.hasPart, name="har_del_omgrep", curie=XKOS.curie('hasPart'),
                   model_uri=DEFAULT_.har_del_omgrep, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.er_medlem_av = Slot(uri=UNESKOS.memberOf, name="er_medlem_av", curie=UNESKOS.curie('memberOf'),
                   model_uri=DEFAULT_.er_medlem_av, domain=None, range=Optional[Union[Union[str, SamlingId], list[Union[str, SamlingId]]]])

slots.sja_ogsa_omgrep = Slot(uri=RDFS.seeAlso, name="sja_ogsa_omgrep", curie=RDFS.curie('seeAlso'),
                   model_uri=DEFAULT_.sja_ogsa_omgrep, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.spesifiserer = Slot(uri=XKOS.specializes, name="spesifiserer", curie=XKOS.curie('specializes'),
                   model_uri=DEFAULT_.spesifiserer, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.euvoc_status = Slot(uri=EUVOC.status, name="euvoc_status", curie=EUVOC.curie('status'),
                   model_uri=DEFAULT_.euvoc_status, domain=None, range=Optional[Union[str, BegrepId]])

slots.verdiomrade = Slot(uri=SKOSNO.valueRange, name="verdiomrade", curie=SKOSNO.curie('valueRange'),
                   model_uri=DEFAULT_.verdiomrade, domain=None, range=Optional[Union[str, list[str]]])

slots.tekst = Slot(uri=RDF.value, name="tekst", curie=RDF.curie('value'),
                   model_uri=DEFAULT_.tekst, domain=None, range=Optional[str])

slots.kjelde_relasjon = Slot(uri=SKOSNO.relationshipWithSource, name="kjelde_relasjon", curie=SKOSNO.curie('relationshipWithSource'),
                   model_uri=DEFAULT_.kjelde_relasjon, domain=None, range=Optional[Union[str, BegrepId]])

slots.kjelde = Slot(uri=DCT.source, name="kjelde", curie=DCT.curie('source'),
                   model_uri=DEFAULT_.kjelde, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.malgruppe_def = Slot(uri=DCT.audience, name="malgruppe_def", curie=DCT.curie('audience'),
                   model_uri=DEFAULT_.malgruppe_def, domain=None, range=Optional[Union[str, BegrepId]])

slots.til_omgrep = Slot(uri=SKOSNO.hasToConcept, name="til_omgrep", curie=SKOSNO.curie('hasToConcept'),
                   model_uri=DEFAULT_.til_omgrep, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.relasjontype = Slot(uri=SKOSNO.relationRole, name="relasjontype", curie=SKOSNO.curie('relationRole'),
                   model_uri=DEFAULT_.relasjontype, domain=None, range=Optional[str])

slots.har_generisk_omgrep = Slot(uri=SKOSNO.hasGenericConcept, name="har_generisk_omgrep", curie=SKOSNO.curie('hasGenericConcept'),
                   model_uri=DEFAULT_.har_generisk_omgrep, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.har_spesifikt_omgrep = Slot(uri=SKOSNO.hasSpecificConcept, name="har_spesifikt_omgrep", curie=SKOSNO.curie('hasSpecificConcept'),
                   model_uri=DEFAULT_.har_spesifikt_omgrep, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.inndelingskriterium = Slot(uri=DCT.description, name="inndelingskriterium", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.inndelingskriterium, domain=None, range=Optional[Union[str, list[str]]])

slots.har_partitivt_omgrep = Slot(uri=SKOSNO.hasPartitiveConcept, name="har_partitivt_omgrep", curie=SKOSNO.curie('hasPartitiveConcept'),
                   model_uri=DEFAULT_.har_partitivt_omgrep, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.har_heilskapleg_omgrep = Slot(uri=SKOSNO.hasComprehensiveConcept, name="har_heilskapleg_omgrep", curie=SKOSNO.curie('hasComprehensiveConcept'),
                   model_uri=DEFAULT_.har_heilskapleg_omgrep, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.medlem = Slot(uri=SKOS.member, name="medlem", curie=SKOS.curie('member'),
                   model_uri=DEFAULT_.medlem, domain=None, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.id = Slot(uri=CAPNO.id, name="id", curie=CAPNO.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.tittel = Slot(uri=DCT.title, name="tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.tittel, domain=None, range=Optional[Union[str, list[str]]])

slots.beskrivelse = Slot(uri=DCT.description, name="beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.beskrivelse, domain=None, range=Optional[Union[str, list[str]]])

slots.identifikator_literal = Slot(uri=DCT.identifier, name="identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.identifikator_literal, domain=None, range=Optional[str])

slots.type_concept = Slot(uri=DCT.type, name="type_concept", curie=DCT.curie('type'),
                   model_uri=DEFAULT_.type_concept, domain=None, range=Optional[Union[str, KonseptId]])

slots.endringsdato = Slot(uri=DCT.modified, name="endringsdato", curie=DCT.curie('modified'),
                   model_uri=DEFAULT_.endringsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.utgivelsesdato = Slot(uri=DCT.issued, name="utgivelsesdato", curie=DCT.curie('issued'),
                   model_uri=DEFAULT_.utgivelsesdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.spraak = Slot(uri=DCT.language, name="spraak", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.spraak, domain=None, range=Optional[Union[str, list[str]]])

slots.format = Slot(uri=DCT.format, name="format", curie=DCT.curie('format'),
                   model_uri=DEFAULT_.format, domain=None, range=Optional[str])

slots.har_referanse = Slot(uri=RDFS.seeAlso, name="har_referanse", curie=RDFS.curie('seeAlso'),
                   model_uri=DEFAULT_.har_referanse, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.har_merknad = Slot(uri=RDFS.comment, name="har_merknad", curie=RDFS.curie('comment'),
                   model_uri=DEFAULT_.har_merknad, domain=None, range=Optional[Union[str, list[str]]])

slots.har_versjonsnummer = Slot(uri=OWL.versionInfo, name="har_versjonsnummer", curie=OWL.curie('versionInfo'),
                   model_uri=DEFAULT_.har_versjonsnummer, domain=None, range=Optional[str])

slots.nokkelord = Slot(uri=DCAT.keyword, name="nokkelord", curie=DCAT.curie('keyword'),
                   model_uri=DEFAULT_.nokkelord, domain=None, range=Optional[Union[str, list[str]]])

slots.dekningsomraade = Slot(uri=DCT.spatial, name="dekningsomraade", curie=DCT.curie('spatial'),
                   model_uri=DEFAULT_.dekningsomraade, domain=None, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.status = Slot(uri=ADMS.status, name="status", curie=ADMS.curie('status'),
                   model_uri=DEFAULT_.status, domain=None, range=Optional[Union[str, KonseptId]])

slots.valuta = Slot(uri=CV.currency, name="valuta", curie=CV.curie('currency'),
                   model_uri=DEFAULT_.valuta, domain=None, range=Optional[Union[str, KonseptId]])

slots.heimeside = Slot(uri=FOAF.homepage, name="heimeside", curie=FOAF.curie('homepage'),
                   model_uri=DEFAULT_.heimeside, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.anbefalt_term = Slot(uri=SKOS.prefLabel, name="anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=DEFAULT_.anbefalt_term, domain=None, range=Optional[Union[str, list[str]]])

slots.versjonsmerknad = Slot(uri=ADMS.versionNotes, name="versjonsmerknad", curie=ADMS.curie('versionNotes'),
                   model_uri=DEFAULT_.versjonsmerknad, domain=None, range=Optional[Union[str, list[str]]])

slots.begrepContainer__begrep = Slot(uri=DEFAULT_.begrep, name="begrepContainer__begrep", curie=DEFAULT_.curie('begrep'),
                   model_uri=DEFAULT_.begrepContainer__begrep, domain=None, range=Optional[Union[dict[Union[str, BegrepId], Union[dict, Begrep]], list[Union[dict, Begrep]]]])

slots.begrepContainer__samlingar = Slot(uri=DEFAULT_.samlingar, name="begrepContainer__samlingar", curie=DEFAULT_.curie('samlingar'),
                   model_uri=DEFAULT_.begrepContainer__samlingar, domain=None, range=Optional[Union[dict[Union[str, SamlingId], Union[dict, Samling]], list[Union[dict, Samling]]]])

slots.begrepContainer__definisjoner = Slot(uri=DEFAULT_.definisjoner, name="begrepContainer__definisjoner", curie=DEFAULT_.curie('definisjoner'),
                   model_uri=DEFAULT_.begrepContainer__definisjoner, domain=None, range=Optional[Union[dict[Union[str, DefinisjonId], Union[dict, Definisjon]], list[Union[dict, Definisjon]]]])

slots.begrepContainer__generiske_relasjonar = Slot(uri=DEFAULT_.generiske_relasjonar, name="begrepContainer__generiske_relasjonar", curie=DEFAULT_.curie('generiske_relasjonar'),
                   model_uri=DEFAULT_.begrepContainer__generiske_relasjonar, domain=None, range=Optional[Union[dict[Union[str, GeneriskRelasjonId], Union[dict, GeneriskRelasjon]], list[Union[dict, GeneriskRelasjon]]]])

slots.begrepContainer__partitive_relasjonar = Slot(uri=DEFAULT_.partitive_relasjonar, name="begrepContainer__partitive_relasjonar", curie=DEFAULT_.curie('partitive_relasjonar'),
                   model_uri=DEFAULT_.begrepContainer__partitive_relasjonar, domain=None, range=Optional[Union[dict[Union[str, PartitivRelasjonId], Union[dict, PartitivRelasjon]], list[Union[dict, PartitivRelasjon]]]])

slots.begrepContainer__assosiative_relasjonar = Slot(uri=DEFAULT_.assosiative_relasjonar, name="begrepContainer__assosiative_relasjonar", curie=DEFAULT_.curie('assosiative_relasjonar'),
                   model_uri=DEFAULT_.begrepContainer__assosiative_relasjonar, domain=None, range=Optional[Union[dict[Union[str, AssosiativRelasjonId], Union[dict, AssosiativRelasjon]], list[Union[dict, AssosiativRelasjon]]]])

slots.begrepContainer__organisasjonar = Slot(uri=DEFAULT_.organisasjonar, name="begrepContainer__organisasjonar", curie=DEFAULT_.curie('organisasjonar'),
                   model_uri=DEFAULT_.begrepContainer__organisasjonar, domain=None, range=Optional[Union[list[Union[str, OrganisasjonId]], dict[Union[str, OrganisasjonId], Union[dict, Organisasjon]]]])

slots.begrepContainer__kontaktpunkt = Slot(uri=DEFAULT_.kontaktpunkt, name="begrepContainer__kontaktpunkt", curie=DEFAULT_.curie('kontaktpunkt'),
                   model_uri=DEFAULT_.begrepContainer__kontaktpunkt, domain=None, range=Optional[Union[list[Union[str, VCardKontaktId]], dict[Union[str, VCardKontaktId], Union[dict, VCardKontakt]]]])

slots.Begrep_anbefalt_term = Slot(uri=SKOS.prefLabel, name="Begrep_anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=DEFAULT_.Begrep_anbefalt_term, domain=Begrep, range=Union[str, list[str]])

slots.Begrep_identifikator_literal = Slot(uri=DCT.identifier, name="Begrep_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Begrep_identifikator_literal, domain=Begrep, range=str)

slots.Begrep_kontaktpunkt_vcard = Slot(uri=DCAT.contactPoint, name="Begrep_kontaktpunkt_vcard", curie=DCAT.curie('contactPoint'),
                   model_uri=DEFAULT_.Begrep_kontaktpunkt_vcard, domain=Begrep, range=Union[Union[str, VCardKontaktId], list[Union[str, VCardKontaktId]]])

slots.Begrep_utgjevar = Slot(uri=DCT.publisher, name="Begrep_utgjevar", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.Begrep_utgjevar, domain=Begrep, range=Union[str, OrganisasjonId])

slots.Begrep_definisjon = Slot(uri=SKOS.definition, name="Begrep_definisjon", curie=SKOS.curie('definition'),
                   model_uri=DEFAULT_.Begrep_definisjon, domain=Begrep, range=Optional[Union[str, list[str]]])

slots.Begrep_har_definisjon = Slot(uri=EUVOC.xlDefinition, name="Begrep_har_definisjon", curie=EUVOC.curie('xlDefinition'),
                   model_uri=DEFAULT_.Begrep_har_definisjon, domain=Begrep, range=Optional[Union[Union[str, DefinisjonId], list[Union[str, DefinisjonId]]]])

slots.Begrep_ansvarleg_verksemd = Slot(uri=DCT.creator, name="Begrep_ansvarleg_verksemd", curie=DCT.curie('creator'),
                   model_uri=DEFAULT_.Begrep_ansvarleg_verksemd, domain=Begrep, range=Optional[Union[str, OrganisasjonId]])

slots.Begrep_gyldig_fra = Slot(uri=EUVOC.startDate, name="Begrep_gyldig_fra", curie=EUVOC.curie('startDate'),
                   model_uri=DEFAULT_.Begrep_gyldig_fra, domain=Begrep, range=Optional[Union[str, XSDDate]])

slots.Begrep_gyldig_til = Slot(uri=EUVOC.endDate, name="Begrep_gyldig_til", curie=EUVOC.curie('endDate'),
                   model_uri=DEFAULT_.Begrep_gyldig_til, domain=Begrep, range=Optional[Union[str, XSDDate]])

slots.Begrep_opprettingsdato = Slot(uri=DCT.created, name="Begrep_opprettingsdato", curie=DCT.curie('created'),
                   model_uri=DEFAULT_.Begrep_opprettingsdato, domain=Begrep, range=Optional[Union[str, XSDDate]])

slots.Begrep_endringsdato = Slot(uri=DCT.modified, name="Begrep_endringsdato", curie=DCT.curie('modified'),
                   model_uri=DEFAULT_.Begrep_endringsdato, domain=Begrep, range=Optional[Union[str, XSDDate]])

slots.Begrep_fagomrade = Slot(uri=DCT.subject, name="Begrep_fagomrade", curie=DCT.curie('subject'),
                   model_uri=DEFAULT_.Begrep_fagomrade, domain=Begrep, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.Begrep_merknad = Slot(uri=SKOS.scopeNote, name="Begrep_merknad", curie=SKOS.curie('scopeNote'),
                   model_uri=DEFAULT_.Begrep_merknad, domain=Begrep, range=Optional[Union[str, list[str]]])

slots.Begrep_tillate_term = Slot(uri=SKOS.altLabel, name="Begrep_tillate_term", curie=SKOS.curie('altLabel'),
                   model_uri=DEFAULT_.Begrep_tillate_term, domain=Begrep, range=Optional[Union[str, list[str]]])

slots.Begrep_datastruktur_term = Slot(uri=SKOSNO.dataStructureLabel, name="Begrep_datastruktur_term", curie=SKOSNO.curie('dataStructureLabel'),
                   model_uri=DEFAULT_.Begrep_datastruktur_term, domain=Begrep, range=Optional[Union[str, list[str]]])

slots.Begrep_eksempel = Slot(uri=SKOS.example, name="Begrep_eksempel", curie=SKOS.curie('example'),
                   model_uri=DEFAULT_.Begrep_eksempel, domain=Begrep, range=Optional[Union[str, list[str]]])

slots.Begrep_er_del_av_omgrep = Slot(uri=XKOS.isPartOf, name="Begrep_er_del_av_omgrep", curie=XKOS.curie('isPartOf'),
                   model_uri=DEFAULT_.Begrep_er_del_av_omgrep, domain=Begrep, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.Begrep_er_erstatta_av = Slot(uri=DCT.isReplacedBy, name="Begrep_er_erstatta_av", curie=DCT.curie('isReplacedBy'),
                   model_uri=DEFAULT_.Begrep_er_erstatta_av, domain=Begrep, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.Begrep_er_fra_omgrep_i = Slot(uri=SKOSNO.isFromConceptIn, name="Begrep_er_fra_omgrep_i", curie=SKOSNO.curie('isFromConceptIn'),
                   model_uri=DEFAULT_.Begrep_er_fra_omgrep_i, domain=Begrep, range=Optional[Union[Union[str, AssosiativRelasjonId], list[Union[str, AssosiativRelasjonId]]]])

slots.Begrep_assosiert_med = Slot(uri=SKOS.related, name="Begrep_assosiert_med", curie=SKOS.curie('related'),
                   model_uri=DEFAULT_.Begrep_assosiert_med, domain=Begrep, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.Begrep_erstattar = Slot(uri=DCT.replaces, name="Begrep_erstattar", curie=DCT.curie('replaces'),
                   model_uri=DEFAULT_.Begrep_erstattar, domain=Begrep, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.Begrep_forkasta_term = Slot(uri=SKOS.hiddenLabel, name="Begrep_forkasta_term", curie=SKOS.curie('hiddenLabel'),
                   model_uri=DEFAULT_.Begrep_forkasta_term, domain=Begrep, range=Optional[Union[str, list[str]]])

slots.Begrep_generaliserer = Slot(uri=XKOS.generalizes, name="Begrep_generaliserer", curie=XKOS.curie('generalizes'),
                   model_uri=DEFAULT_.Begrep_generaliserer, domain=Begrep, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.Begrep_noyaktig_samsvar = Slot(uri=SKOS.exactMatch, name="Begrep_noyaktig_samsvar", curie=SKOS.curie('exactMatch'),
                   model_uri=DEFAULT_.Begrep_noyaktig_samsvar, domain=Begrep, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.Begrep_har_generisk_relasjon = Slot(uri=SKOSNO.hasGenericConceptRelation, name="Begrep_har_generisk_relasjon", curie=SKOSNO.curie('hasGenericConceptRelation'),
                   model_uri=DEFAULT_.Begrep_har_generisk_relasjon, domain=Begrep, range=Optional[Union[Union[str, GeneriskRelasjonId], list[Union[str, GeneriskRelasjonId]]]])

slots.Begrep_naert_samsvar = Slot(uri=SKOS.closeMatch, name="Begrep_naert_samsvar", curie=SKOS.curie('closeMatch'),
                   model_uri=DEFAULT_.Begrep_naert_samsvar, domain=Begrep, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.Begrep_har_partitiv_relasjon = Slot(uri=SKOSNO.hasPartitiveConceptRelation, name="Begrep_har_partitiv_relasjon", curie=SKOSNO.curie('hasPartitiveConceptRelation'),
                   model_uri=DEFAULT_.Begrep_har_partitiv_relasjon, domain=Begrep, range=Optional[Union[Union[str, PartitivRelasjonId], list[Union[str, PartitivRelasjonId]]]])

slots.Begrep_har_del_omgrep = Slot(uri=XKOS.hasPart, name="Begrep_har_del_omgrep", curie=XKOS.curie('hasPart'),
                   model_uri=DEFAULT_.Begrep_har_del_omgrep, domain=Begrep, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.Begrep_er_medlem_av = Slot(uri=UNESKOS.memberOf, name="Begrep_er_medlem_av", curie=UNESKOS.curie('memberOf'),
                   model_uri=DEFAULT_.Begrep_er_medlem_av, domain=Begrep, range=Optional[Union[Union[str, SamlingId], list[Union[str, SamlingId]]]])

slots.Begrep_sja_ogsa_omgrep = Slot(uri=RDFS.seeAlso, name="Begrep_sja_ogsa_omgrep", curie=RDFS.curie('seeAlso'),
                   model_uri=DEFAULT_.Begrep_sja_ogsa_omgrep, domain=Begrep, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.Begrep_spesifiserer = Slot(uri=XKOS.specializes, name="Begrep_spesifiserer", curie=XKOS.curie('specializes'),
                   model_uri=DEFAULT_.Begrep_spesifiserer, domain=Begrep, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.Begrep_euvoc_status = Slot(uri=EUVOC.status, name="Begrep_euvoc_status", curie=EUVOC.curie('status'),
                   model_uri=DEFAULT_.Begrep_euvoc_status, domain=Begrep, range=Optional[Union[str, BegrepId]])

slots.Begrep_verdiomrade = Slot(uri=SKOSNO.valueRange, name="Begrep_verdiomrade", curie=SKOSNO.curie('valueRange'),
                   model_uri=DEFAULT_.Begrep_verdiomrade, domain=Begrep, range=Optional[Union[str, list[str]]])

slots.Begrep_har_versjonsnummer = Slot(uri=OWL.versionInfo, name="Begrep_har_versjonsnummer", curie=OWL.curie('versionInfo'),
                   model_uri=DEFAULT_.Begrep_har_versjonsnummer, domain=Begrep, range=Optional[str])

slots.Begrep_versjonsmerknad = Slot(uri=ADMS.versionNotes, name="Begrep_versjonsmerknad", curie=ADMS.curie('versionNotes'),
                   model_uri=DEFAULT_.Begrep_versjonsmerknad, domain=Begrep, range=Optional[Union[str, list[str]]])

slots.Definisjon_tekst = Slot(uri=RDF.value, name="Definisjon_tekst", curie=RDF.curie('value'),
                   model_uri=DEFAULT_.Definisjon_tekst, domain=Definisjon, range=str)

slots.Definisjon_kjelde_relasjon = Slot(uri=SKOSNO.relationshipWithSource, name="Definisjon_kjelde_relasjon", curie=SKOSNO.curie('relationshipWithSource'),
                   model_uri=DEFAULT_.Definisjon_kjelde_relasjon, domain=Definisjon, range=Optional[Union[str, BegrepId]])

slots.Definisjon_kjelde = Slot(uri=DCT.source, name="Definisjon_kjelde", curie=DCT.curie('source'),
                   model_uri=DEFAULT_.Definisjon_kjelde, domain=Definisjon, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Definisjon_malgruppe_def = Slot(uri=DCT.audience, name="Definisjon_malgruppe_def", curie=DCT.curie('audience'),
                   model_uri=DEFAULT_.Definisjon_malgruppe_def, domain=Definisjon, range=Optional[Union[str, BegrepId]])

slots.AssosiativRelasjon_til_omgrep = Slot(uri=SKOSNO.hasToConcept, name="AssosiativRelasjon_til_omgrep", curie=SKOSNO.curie('hasToConcept'),
                   model_uri=DEFAULT_.AssosiativRelasjon_til_omgrep, domain=AssosiativRelasjon, range=Union[Union[str, BegrepId], list[Union[str, BegrepId]]])

slots.AssosiativRelasjon_relasjontype = Slot(uri=SKOSNO.relationRole, name="AssosiativRelasjon_relasjontype", curie=SKOSNO.curie('relationRole'),
                   model_uri=DEFAULT_.AssosiativRelasjon_relasjontype, domain=AssosiativRelasjon, range=str)

slots.GeneriskRelasjon_har_generisk_omgrep = Slot(uri=SKOSNO.hasGenericConcept, name="GeneriskRelasjon_har_generisk_omgrep", curie=SKOSNO.curie('hasGenericConcept'),
                   model_uri=DEFAULT_.GeneriskRelasjon_har_generisk_omgrep, domain=GeneriskRelasjon, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.GeneriskRelasjon_har_spesifikt_omgrep = Slot(uri=SKOSNO.hasSpecificConcept, name="GeneriskRelasjon_har_spesifikt_omgrep", curie=SKOSNO.curie('hasSpecificConcept'),
                   model_uri=DEFAULT_.GeneriskRelasjon_har_spesifikt_omgrep, domain=GeneriskRelasjon, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.GeneriskRelasjon_inndelingskriterium = Slot(uri=DCT.description, name="GeneriskRelasjon_inndelingskriterium", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.GeneriskRelasjon_inndelingskriterium, domain=GeneriskRelasjon, range=Optional[Union[str, list[str]]])

slots.PartitivRelasjon_har_partitivt_omgrep = Slot(uri=SKOSNO.hasPartitiveConcept, name="PartitivRelasjon_har_partitivt_omgrep", curie=SKOSNO.curie('hasPartitiveConcept'),
                   model_uri=DEFAULT_.PartitivRelasjon_har_partitivt_omgrep, domain=PartitivRelasjon, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.PartitivRelasjon_har_heilskapleg_omgrep = Slot(uri=SKOSNO.hasComprehensiveConcept, name="PartitivRelasjon_har_heilskapleg_omgrep", curie=SKOSNO.curie('hasComprehensiveConcept'),
                   model_uri=DEFAULT_.PartitivRelasjon_har_heilskapleg_omgrep, domain=PartitivRelasjon, range=Optional[Union[Union[str, BegrepId], list[Union[str, BegrepId]]]])

slots.PartitivRelasjon_inndelingskriterium = Slot(uri=DCT.description, name="PartitivRelasjon_inndelingskriterium", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.PartitivRelasjon_inndelingskriterium, domain=PartitivRelasjon, range=Optional[Union[str, list[str]]])

slots.Samling_identifikator_literal = Slot(uri=DCT.identifier, name="Samling_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Samling_identifikator_literal, domain=Samling, range=str)

slots.Samling_medlem = Slot(uri=SKOS.member, name="Samling_medlem", curie=SKOS.curie('member'),
                   model_uri=DEFAULT_.Samling_medlem, domain=Samling, range=Union[Union[str, BegrepId], list[Union[str, BegrepId]]])

slots.Samling_kontaktpunkt_vcard = Slot(uri=DCAT.contactPoint, name="Samling_kontaktpunkt_vcard", curie=DCAT.curie('contactPoint'),
                   model_uri=DEFAULT_.Samling_kontaktpunkt_vcard, domain=Samling, range=Union[Union[str, VCardKontaktId], list[Union[str, VCardKontaktId]]])

slots.Samling_tittel = Slot(uri=DCT.title, name="Samling_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Samling_tittel, domain=Samling, range=Union[str, list[str]])

slots.Samling_utgjevar = Slot(uri=DCT.publisher, name="Samling_utgjevar", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.Samling_utgjevar, domain=Samling, range=Union[str, OrganisasjonId])

slots.Samling_beskrivelse = Slot(uri=DCT.description, name="Samling_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.Samling_beskrivelse, domain=Samling, range=Optional[Union[str, list[str]]])

