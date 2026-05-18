# Auto generated from cpsv-ap-no-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-18T09:10:42
# Schema: cpsv-ap-no
#
# id: https://data.norge.no/linkml/cpsv-ap-no
# description: Norsk applikasjonsprofil av CPSV (Core Public Service Vocabulary), modellert i LinkML med lenking framfor inlining. Basert på https://informasjonsforvaltning.github.io/cpsv-ap-no/
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

from linkml_runtime.linkml_model.types import Date, Float, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = "1.0"

# Namespaces
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms#')
CAPNO = CurieNamespace('capno', 'https://data.norge.no/linkml/common-ap-no/')
CCCEVNO = CurieNamespace('cccevno', 'https://data.norge.no/vocabulary/cccevno#')
CPSV = CurieNamespace('cpsv', 'http://purl.org/vocab/cpsv#')
CPSVNO = CurieNamespace('cpsvno', 'https://data.norge.no/vocabulary/cpsvno#')
CV = CurieNamespace('cv', 'http://data.europa.eu/m8g/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCATNO = CurieNamespace('dcatno', 'https://data.norge.no/vocabulary/dcatno#')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
ELI = CurieNamespace('eli', 'http://data.europa.eu/eli/ontology#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LOCN = CurieNamespace('locn', 'http://www.w3.org/ns/locn#')
ORG = CurieNamespace('org', 'http://www.w3.org/ns/org#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns#')
XKOS = CurieNamespace('xkos', 'http://rdf-vocabulary.ddialliance.org/xkos#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://data.norge.no/linkml/cpsv-ap-no/')


# Types
class Spraak(str):
    """ Språk """
    type_class_uri = DCT["language"]
    type_class_curie = "dct:language"
    type_name = "Spraak"
    type_model_uri = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Spraak")


class LangString(str):
    """ Språktagget streng (rdf:langString). """
    type_class_uri = RDF["langString"]
    type_class_curie = "rdf:langString"
    type_name = "LangString"
    type_model_uri = URIRef("https://data.norge.no/linkml/cpsv-ap-no/LangString")


class NonNegativeInteger(int):
    """ Ikkje-negativ heltalsverdi (xsd:nonNegativeInteger). """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "NonNegativeInteger"
    type_model_uri = URIRef("https://data.norge.no/linkml/cpsv-ap-no/NonNegativeInteger")


class Duration(str):
    """ ISO 8601-varigheit (xsd:duration), t.d. PT15M. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "Duration"
    type_model_uri = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Duration")


class GYear(str):
    """ Gregorisk årstal (xsd:gYear), t.d. 2024. """
    type_class_uri = XSD["gYear"]
    type_class_curie = "xsd:gYear"
    type_name = "GYear"
    type_model_uri = URIRef("https://data.norge.no/linkml/cpsv-ap-no/GYear")


# Class references
class OffentligTjenesteId(URIorCURIE):
    pass


class TjenesteId(URIorCURIE):
    pass


class HendelseId(URIorCURIE):
    pass


class LivshendelseId(HendelseId):
    pass


class VirksomhetshendelseId(HendelseId):
    pass


class AktorId(URIorCURIE):
    pass


class OffentligOrganisasjonId(AktorId):
    pass


class KontaktpunktId(URIorCURIE):
    pass


class TjenestekanalId(URIorCURIE):
    pass


class DokumentasjonstypeId(URIorCURIE):
    pass


class TjenesteresultattypeId(URIorCURIE):
    pass


class TjenesteresultattypelisteId(URIorCURIE):
    pass


class GebyrId(URIorCURIE):
    pass


class RegelId(URIorCURIE):
    pass


class RegulativRessursId(URIorCURIE):
    pass


class DeltagelseId(URIorCURIE):
    pass


class AdresseId(URIorCURIE):
    pass


class KatalogId(URIorCURIE):
    pass


class MediatypeId(URIorCURIE):
    pass


class KonseptId(URIorCURIE):
    pass


class BegrepssamlingId(URIorCURIE):
    pass


@dataclass(repr=False)
class OffentligTjeneste(YAMLRoot):
    """
    Ei konkret offentleg teneste levert av ein offentleg organisasjon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CPSV["PublicService"]
    class_class_curie: ClassVar[str] = "cpsv:PublicService"
    class_name: ClassVar[str] = "OffentligTjeneste"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/OffentligTjeneste")

    id: Union[str, OffentligTjenesteId] = None
    tittel: Union[str, list[str]] = None
    beskrivelse: Union[str, list[str]] = None
    identifikator_literal: str = None
    har_kontaktpunkt: Union[Union[str, KontaktpunktId], list[Union[str, KontaktpunktId]]] = None
    har_tenesteresultattype: Union[Union[str, TjenesteresultattypeId], list[Union[str, TjenesteresultattypeId]]] = None
    har_ansvarleg_styremakt: Union[Union[str, OffentligOrganisasjonId], list[Union[str, OffentligOrganisasjonId]]] = None
    tema: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    dekningsomraade: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    har_dokumentasjonstype: Optional[Union[Union[str, DokumentasjonstypeId], list[Union[str, DokumentasjonstypeId]]]] = empty_list()
    heimeside: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    type_concept: Optional[Union[str, KonseptId]] = None
    status: Optional[Union[str, KonseptId]] = None
    temaomrade: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    behandlingstid: Optional[str] = None
    er_beskrive_av: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    er_del_av: Optional[Union[str, URIorCURIE]] = None
    har_del: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    har_tenestekanal: Optional[Union[Union[str, TjenestekanalId], list[Union[str, TjenestekanalId]]]] = empty_list()
    har_deltaking: Optional[Union[Union[str, DeltagelseId], list[Union[str, DeltagelseId]]]] = empty_list()
    spraak: Optional[Union[str, list[str]]] = empty_list()
    relatert_teneste: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    er_gruppert_av: Optional[Union[Union[str, HendelseId], list[Union[str, HendelseId]]]] = empty_list()
    er_klassifisert_av: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    folger: Optional[Union[Union[str, RegelId], list[Union[str, RegelId]]]] = empty_list()
    har_gebyr: Optional[Union[Union[str, GebyrId], list[Union[str, GebyrId]]]] = empty_list()
    har_regulativ_ressurs: Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]] = empty_list()
    krev: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    malgruppe: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    nokkelord: Optional[Union[str, list[str]]] = empty_list()
    sektor: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OffentligTjenesteId):
            self.id = OffentligTjenesteId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.beskrivelse):
            self.MissingRequiredField("beskrivelse")
        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self._is_empty(self.identifikator_literal):
            self.MissingRequiredField("identifikator_literal")
        if not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self._is_empty(self.har_kontaktpunkt):
            self.MissingRequiredField("har_kontaktpunkt")
        if not isinstance(self.har_kontaktpunkt, list):
            self.har_kontaktpunkt = [self.har_kontaktpunkt] if self.har_kontaktpunkt is not None else []
        self.har_kontaktpunkt = [v if isinstance(v, KontaktpunktId) else KontaktpunktId(v) for v in self.har_kontaktpunkt]

        if self._is_empty(self.har_tenesteresultattype):
            self.MissingRequiredField("har_tenesteresultattype")
        if not isinstance(self.har_tenesteresultattype, list):
            self.har_tenesteresultattype = [self.har_tenesteresultattype] if self.har_tenesteresultattype is not None else []
        self.har_tenesteresultattype = [v if isinstance(v, TjenesteresultattypeId) else TjenesteresultattypeId(v) for v in self.har_tenesteresultattype]

        if self._is_empty(self.har_ansvarleg_styremakt):
            self.MissingRequiredField("har_ansvarleg_styremakt")
        if not isinstance(self.har_ansvarleg_styremakt, list):
            self.har_ansvarleg_styremakt = [self.har_ansvarleg_styremakt] if self.har_ansvarleg_styremakt is not None else []
        self.har_ansvarleg_styremakt = [v if isinstance(v, OffentligOrganisasjonId) else OffentligOrganisasjonId(v) for v in self.har_ansvarleg_styremakt]

        if not isinstance(self.tema, list):
            self.tema = [self.tema] if self.tema is not None else []
        self.tema = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.tema]

        if not isinstance(self.dekningsomraade, list):
            self.dekningsomraade = [self.dekningsomraade] if self.dekningsomraade is not None else []
        self.dekningsomraade = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.dekningsomraade]

        if not isinstance(self.har_dokumentasjonstype, list):
            self.har_dokumentasjonstype = [self.har_dokumentasjonstype] if self.har_dokumentasjonstype is not None else []
        self.har_dokumentasjonstype = [v if isinstance(v, DokumentasjonstypeId) else DokumentasjonstypeId(v) for v in self.har_dokumentasjonstype]

        if not isinstance(self.heimeside, list):
            self.heimeside = [self.heimeside] if self.heimeside is not None else []
        self.heimeside = [v if isinstance(v, URI) else URI(v) for v in self.heimeside]

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        if self.status is not None and not isinstance(self.status, KonseptId):
            self.status = KonseptId(self.status)

        if not isinstance(self.temaomrade, list):
            self.temaomrade = [self.temaomrade] if self.temaomrade is not None else []
        self.temaomrade = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.temaomrade]

        if self.behandlingstid is not None and not isinstance(self.behandlingstid, str):
            self.behandlingstid = str(self.behandlingstid)

        if not isinstance(self.er_beskrive_av, list):
            self.er_beskrive_av = [self.er_beskrive_av] if self.er_beskrive_av is not None else []
        self.er_beskrive_av = [v if isinstance(v, URI) else URI(v) for v in self.er_beskrive_av]

        if self.er_del_av is not None and not isinstance(self.er_del_av, URIorCURIE):
            self.er_del_av = URIorCURIE(self.er_del_av)

        if not isinstance(self.har_del, list):
            self.har_del = [self.har_del] if self.har_del is not None else []
        self.har_del = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.har_del]

        if not isinstance(self.har_tenestekanal, list):
            self.har_tenestekanal = [self.har_tenestekanal] if self.har_tenestekanal is not None else []
        self.har_tenestekanal = [v if isinstance(v, TjenestekanalId) else TjenestekanalId(v) for v in self.har_tenestekanal]

        if not isinstance(self.har_deltaking, list):
            self.har_deltaking = [self.har_deltaking] if self.har_deltaking is not None else []
        self.har_deltaking = [v if isinstance(v, DeltagelseId) else DeltagelseId(v) for v in self.har_deltaking]

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

        if not isinstance(self.relatert_teneste, list):
            self.relatert_teneste = [self.relatert_teneste] if self.relatert_teneste is not None else []
        self.relatert_teneste = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.relatert_teneste]

        if not isinstance(self.er_gruppert_av, list):
            self.er_gruppert_av = [self.er_gruppert_av] if self.er_gruppert_av is not None else []
        self.er_gruppert_av = [v if isinstance(v, HendelseId) else HendelseId(v) for v in self.er_gruppert_av]

        if not isinstance(self.er_klassifisert_av, list):
            self.er_klassifisert_av = [self.er_klassifisert_av] if self.er_klassifisert_av is not None else []
        self.er_klassifisert_av = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.er_klassifisert_av]

        if not isinstance(self.folger, list):
            self.folger = [self.folger] if self.folger is not None else []
        self.folger = [v if isinstance(v, RegelId) else RegelId(v) for v in self.folger]

        if not isinstance(self.har_gebyr, list):
            self.har_gebyr = [self.har_gebyr] if self.har_gebyr is not None else []
        self.har_gebyr = [v if isinstance(v, GebyrId) else GebyrId(v) for v in self.har_gebyr]

        if not isinstance(self.har_regulativ_ressurs, list):
            self.har_regulativ_ressurs = [self.har_regulativ_ressurs] if self.har_regulativ_ressurs is not None else []
        self.har_regulativ_ressurs = [v if isinstance(v, RegulativRessursId) else RegulativRessursId(v) for v in self.har_regulativ_ressurs]

        if not isinstance(self.krev, list):
            self.krev = [self.krev] if self.krev is not None else []
        self.krev = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.krev]

        if not isinstance(self.malgruppe, list):
            self.malgruppe = [self.malgruppe] if self.malgruppe is not None else []
        self.malgruppe = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.malgruppe]

        if not isinstance(self.nokkelord, list):
            self.nokkelord = [self.nokkelord] if self.nokkelord is not None else []
        self.nokkelord = [v if isinstance(v, str) else str(v) for v in self.nokkelord]

        if not isinstance(self.sektor, list):
            self.sektor = [self.sektor] if self.sektor is not None else []
        self.sektor = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.sektor]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tjeneste(YAMLRoot):
    """
    Ei teneste levert av ein ikkje-offentleg aktør.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CPSVNO["Service"]
    class_class_curie: ClassVar[str] = "cpsvno:Service"
    class_name: ClassVar[str] = "Tjeneste"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Tjeneste")

    id: Union[str, TjenesteId] = None
    tittel: Union[str, list[str]] = None
    beskrivelse: Union[str, list[str]] = None
    identifikator_literal: str = None
    har_kontaktpunkt: Union[Union[str, KontaktpunktId], list[Union[str, KontaktpunktId]]] = None
    har_tenesteresultattype: Union[Union[str, TjenesteresultattypeId], list[Union[str, TjenesteresultattypeId]]] = None
    eigd_av: Union[Union[str, AktorId], list[Union[str, AktorId]]] = None
    tema: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    dekningsomraade: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    har_dokumentasjonstype: Optional[Union[Union[str, DokumentasjonstypeId], list[Union[str, DokumentasjonstypeId]]]] = empty_list()
    heimeside: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    type_concept: Optional[Union[str, KonseptId]] = None
    status: Optional[Union[str, KonseptId]] = None
    temaomrade: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    behandlingstid: Optional[str] = None
    er_beskrive_av: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    er_del_av: Optional[Union[str, URIorCURIE]] = None
    har_del: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    har_tenestekanal: Optional[Union[Union[str, TjenestekanalId], list[Union[str, TjenestekanalId]]]] = empty_list()
    har_deltaking: Optional[Union[Union[str, DeltagelseId], list[Union[str, DeltagelseId]]]] = empty_list()
    spraak: Optional[Union[str, list[str]]] = empty_list()
    relatert_teneste: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    er_gruppert_av: Optional[Union[Union[str, HendelseId], list[Union[str, HendelseId]]]] = empty_list()
    er_klassifisert_av: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    folger: Optional[Union[Union[str, RegelId], list[Union[str, RegelId]]]] = empty_list()
    har_gebyr: Optional[Union[Union[str, GebyrId], list[Union[str, GebyrId]]]] = empty_list()
    har_regulativ_ressurs: Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]] = empty_list()
    krev: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    malgruppe: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    nokkelord: Optional[Union[str, list[str]]] = empty_list()
    sektor: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TjenesteId):
            self.id = TjenesteId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.beskrivelse):
            self.MissingRequiredField("beskrivelse")
        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self._is_empty(self.identifikator_literal):
            self.MissingRequiredField("identifikator_literal")
        if not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self._is_empty(self.har_kontaktpunkt):
            self.MissingRequiredField("har_kontaktpunkt")
        if not isinstance(self.har_kontaktpunkt, list):
            self.har_kontaktpunkt = [self.har_kontaktpunkt] if self.har_kontaktpunkt is not None else []
        self.har_kontaktpunkt = [v if isinstance(v, KontaktpunktId) else KontaktpunktId(v) for v in self.har_kontaktpunkt]

        if self._is_empty(self.har_tenesteresultattype):
            self.MissingRequiredField("har_tenesteresultattype")
        if not isinstance(self.har_tenesteresultattype, list):
            self.har_tenesteresultattype = [self.har_tenesteresultattype] if self.har_tenesteresultattype is not None else []
        self.har_tenesteresultattype = [v if isinstance(v, TjenesteresultattypeId) else TjenesteresultattypeId(v) for v in self.har_tenesteresultattype]

        if self._is_empty(self.eigd_av):
            self.MissingRequiredField("eigd_av")
        if not isinstance(self.eigd_av, list):
            self.eigd_av = [self.eigd_av] if self.eigd_av is not None else []
        self.eigd_av = [v if isinstance(v, AktorId) else AktorId(v) for v in self.eigd_av]

        if not isinstance(self.tema, list):
            self.tema = [self.tema] if self.tema is not None else []
        self.tema = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.tema]

        if not isinstance(self.dekningsomraade, list):
            self.dekningsomraade = [self.dekningsomraade] if self.dekningsomraade is not None else []
        self.dekningsomraade = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.dekningsomraade]

        if not isinstance(self.har_dokumentasjonstype, list):
            self.har_dokumentasjonstype = [self.har_dokumentasjonstype] if self.har_dokumentasjonstype is not None else []
        self.har_dokumentasjonstype = [v if isinstance(v, DokumentasjonstypeId) else DokumentasjonstypeId(v) for v in self.har_dokumentasjonstype]

        if not isinstance(self.heimeside, list):
            self.heimeside = [self.heimeside] if self.heimeside is not None else []
        self.heimeside = [v if isinstance(v, URI) else URI(v) for v in self.heimeside]

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        if self.status is not None and not isinstance(self.status, KonseptId):
            self.status = KonseptId(self.status)

        if not isinstance(self.temaomrade, list):
            self.temaomrade = [self.temaomrade] if self.temaomrade is not None else []
        self.temaomrade = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.temaomrade]

        if self.behandlingstid is not None and not isinstance(self.behandlingstid, str):
            self.behandlingstid = str(self.behandlingstid)

        if not isinstance(self.er_beskrive_av, list):
            self.er_beskrive_av = [self.er_beskrive_av] if self.er_beskrive_av is not None else []
        self.er_beskrive_av = [v if isinstance(v, URI) else URI(v) for v in self.er_beskrive_av]

        if self.er_del_av is not None and not isinstance(self.er_del_av, URIorCURIE):
            self.er_del_av = URIorCURIE(self.er_del_av)

        if not isinstance(self.har_del, list):
            self.har_del = [self.har_del] if self.har_del is not None else []
        self.har_del = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.har_del]

        if not isinstance(self.har_tenestekanal, list):
            self.har_tenestekanal = [self.har_tenestekanal] if self.har_tenestekanal is not None else []
        self.har_tenestekanal = [v if isinstance(v, TjenestekanalId) else TjenestekanalId(v) for v in self.har_tenestekanal]

        if not isinstance(self.har_deltaking, list):
            self.har_deltaking = [self.har_deltaking] if self.har_deltaking is not None else []
        self.har_deltaking = [v if isinstance(v, DeltagelseId) else DeltagelseId(v) for v in self.har_deltaking]

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

        if not isinstance(self.relatert_teneste, list):
            self.relatert_teneste = [self.relatert_teneste] if self.relatert_teneste is not None else []
        self.relatert_teneste = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.relatert_teneste]

        if not isinstance(self.er_gruppert_av, list):
            self.er_gruppert_av = [self.er_gruppert_av] if self.er_gruppert_av is not None else []
        self.er_gruppert_av = [v if isinstance(v, HendelseId) else HendelseId(v) for v in self.er_gruppert_av]

        if not isinstance(self.er_klassifisert_av, list):
            self.er_klassifisert_av = [self.er_klassifisert_av] if self.er_klassifisert_av is not None else []
        self.er_klassifisert_av = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.er_klassifisert_av]

        if not isinstance(self.folger, list):
            self.folger = [self.folger] if self.folger is not None else []
        self.folger = [v if isinstance(v, RegelId) else RegelId(v) for v in self.folger]

        if not isinstance(self.har_gebyr, list):
            self.har_gebyr = [self.har_gebyr] if self.har_gebyr is not None else []
        self.har_gebyr = [v if isinstance(v, GebyrId) else GebyrId(v) for v in self.har_gebyr]

        if not isinstance(self.har_regulativ_ressurs, list):
            self.har_regulativ_ressurs = [self.har_regulativ_ressurs] if self.har_regulativ_ressurs is not None else []
        self.har_regulativ_ressurs = [v if isinstance(v, RegulativRessursId) else RegulativRessursId(v) for v in self.har_regulativ_ressurs]

        if not isinstance(self.krev, list):
            self.krev = [self.krev] if self.krev is not None else []
        self.krev = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.krev]

        if not isinstance(self.malgruppe, list):
            self.malgruppe = [self.malgruppe] if self.malgruppe is not None else []
        self.malgruppe = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.malgruppe]

        if not isinstance(self.nokkelord, list):
            self.nokkelord = [self.nokkelord] if self.nokkelord is not None else []
        self.nokkelord = [v if isinstance(v, str) else str(v) for v in self.nokkelord]

        if not isinstance(self.sektor, list):
            self.sektor = [self.sektor] if self.sektor is not None else []
        self.sektor = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.sektor]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Hendelse(YAMLRoot):
    """
    Ei hending som kan utløyse behov for ei offentleg teneste.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CV["Event"]
    class_class_curie: ClassVar[str] = "cv:Event"
    class_name: ClassVar[str] = "Hendelse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Hendelse")

    id: Union[str, HendelseId] = None
    tittel: Union[str, list[str]] = None
    identifikator_literal: str = None
    har_kontaktpunkt: Union[Union[str, KontaktpunktId], list[Union[str, KontaktpunktId]]] = None
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()
    kan_utlose: Optional[Union[Union[str, OffentligTjenesteId], list[Union[str, OffentligTjenesteId]]]] = empty_list()
    tema: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    er_beskrive_av: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    type_concept: Optional[Union[str, KonseptId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HendelseId):
            self.id = HendelseId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.identifikator_literal):
            self.MissingRequiredField("identifikator_literal")
        if not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self._is_empty(self.har_kontaktpunkt):
            self.MissingRequiredField("har_kontaktpunkt")
        if not isinstance(self.har_kontaktpunkt, list):
            self.har_kontaktpunkt = [self.har_kontaktpunkt] if self.har_kontaktpunkt is not None else []
        self.har_kontaktpunkt = [v if isinstance(v, KontaktpunktId) else KontaktpunktId(v) for v in self.har_kontaktpunkt]

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if not isinstance(self.kan_utlose, list):
            self.kan_utlose = [self.kan_utlose] if self.kan_utlose is not None else []
        self.kan_utlose = [v if isinstance(v, OffentligTjenesteId) else OffentligTjenesteId(v) for v in self.kan_utlose]

        if not isinstance(self.tema, list):
            self.tema = [self.tema] if self.tema is not None else []
        self.tema = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.tema]

        if not isinstance(self.er_beskrive_av, list):
            self.er_beskrive_av = [self.er_beskrive_av] if self.er_beskrive_av is not None else []
        self.er_beskrive_av = [v if isinstance(v, URI) else URI(v) for v in self.er_beskrive_av]

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Livshendelse(Hendelse):
    """
    Ei livshending som kan utløyse behov for tenester (t.d. fødsel, ekteskap).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CV["LifeEvent"]
    class_class_curie: ClassVar[str] = "cv:LifeEvent"
    class_name: ClassVar[str] = "Livshendelse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Livshendelse")

    id: Union[str, LivshendelseId] = None
    tittel: Union[str, list[str]] = None
    identifikator_literal: str = None
    har_kontaktpunkt: Union[Union[str, KontaktpunktId], list[Union[str, KontaktpunktId]]] = None
    kan_utlose_behov_for: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LivshendelseId):
            self.id = LivshendelseId(self.id)

        if not isinstance(self.kan_utlose_behov_for, list):
            self.kan_utlose_behov_for = [self.kan_utlose_behov_for] if self.kan_utlose_behov_for is not None else []
        self.kan_utlose_behov_for = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.kan_utlose_behov_for]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Virksomhetshendelse(Hendelse):
    """
    Ei verksemdhending som kan utløyse behov for tenester (t.d. oppstart, konkurs).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CV["BusinessEvent"]
    class_class_curie: ClassVar[str] = "cv:BusinessEvent"
    class_name: ClassVar[str] = "Virksomhetshendelse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Virksomhetshendelse")

    id: Union[str, VirksomhetshendelseId] = None
    tittel: Union[str, list[str]] = None
    identifikator_literal: str = None
    har_kontaktpunkt: Union[Union[str, KontaktpunktId], list[Union[str, KontaktpunktId]]] = None
    kan_utlose_behov_for: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VirksomhetshendelseId):
            self.id = VirksomhetshendelseId(self.id)

        if not isinstance(self.kan_utlose_behov_for, list):
            self.kan_utlose_behov_for = [self.kan_utlose_behov_for] if self.kan_utlose_behov_for is not None else []
        self.kan_utlose_behov_for = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.kan_utlose_behov_for]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aktor(YAMLRoot):
    """
    Ein aktør (person eller organisasjon) relatert til ei teneste.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Agent"]
    class_class_curie: ClassVar[str] = "foaf:Agent"
    class_name: ClassVar[str] = "Aktor"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Aktor")

    id: Union[str, AktorId] = None
    tittel: Union[str, list[str]] = None
    identifikator_literal: str = None
    adresse_ref: Optional[Union[str, AdresseId]] = None
    deltek_i: Optional[Union[Union[str, DeltagelseId], list[Union[str, DeltagelseId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AktorId):
            self.id = AktorId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.identifikator_literal):
            self.MissingRequiredField("identifikator_literal")
        if not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self.adresse_ref is not None and not isinstance(self.adresse_ref, AdresseId):
            self.adresse_ref = AdresseId(self.adresse_ref)

        if not isinstance(self.deltek_i, list):
            self.deltek_i = [self.deltek_i] if self.deltek_i is not None else []
        self.deltek_i = [v if isinstance(v, DeltagelseId) else DeltagelseId(v) for v in self.deltek_i]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OffentligOrganisasjon(Aktor):
    """
    Ein offentleg organisasjon som er ansvarleg for ei teneste.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CV["PublicOrganisation"]
    class_class_curie: ClassVar[str] = "cv:PublicOrganisation"
    class_name: ClassVar[str] = "OffentligOrganisasjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/OffentligOrganisasjon")

    id: Union[str, OffentligOrganisasjonId] = None
    tittel: Union[str, list[str]] = None
    identifikator_literal: str = None
    foretrekt_namn: Union[str, list[str]] = None
    dekningsomraade: Union[Union[str, KonseptId], list[Union[str, KonseptId]]] = None
    heimeside: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    type_concept: Optional[Union[str, KonseptId]] = None
    adresse_ref: Optional[Union[str, AdresseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OffentligOrganisasjonId):
            self.id = OffentligOrganisasjonId(self.id)

        if self._is_empty(self.foretrekt_namn):
            self.MissingRequiredField("foretrekt_namn")
        if not isinstance(self.foretrekt_namn, list):
            self.foretrekt_namn = [self.foretrekt_namn] if self.foretrekt_namn is not None else []
        self.foretrekt_namn = [v if isinstance(v, str) else str(v) for v in self.foretrekt_namn]

        if self._is_empty(self.dekningsomraade):
            self.MissingRequiredField("dekningsomraade")
        if not isinstance(self.dekningsomraade, list):
            self.dekningsomraade = [self.dekningsomraade] if self.dekningsomraade is not None else []
        self.dekningsomraade = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.dekningsomraade]

        if not isinstance(self.heimeside, list):
            self.heimeside = [self.heimeside] if self.heimeside is not None else []
        self.heimeside = [v if isinstance(v, URI) else URI(v) for v in self.heimeside]

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        if self.adresse_ref is not None and not isinstance(self.adresse_ref, AdresseId):
            self.adresse_ref = AdresseId(self.adresse_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontaktpunkt(YAMLRoot):
    """
    Kontaktinformasjon for ei teneste eller ein organisasjon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CV["ContactPoint"]
    class_class_curie: ClassVar[str] = "cv:ContactPoint"
    class_name: ClassVar[str] = "Kontaktpunkt"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Kontaktpunkt")

    id: Union[str, KontaktpunktId] = None
    epost: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    telefon: Optional[Union[str, list[str]]] = empty_list()
    kontaktside: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    opningstider: Optional[Union[str, list[str]]] = empty_list()
    spraak: Optional[Union[str, list[str]]] = empty_list()
    kategori: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KontaktpunktId):
            self.id = KontaktpunktId(self.id)

        if not isinstance(self.epost, list):
            self.epost = [self.epost] if self.epost is not None else []
        self.epost = [v if isinstance(v, URI) else URI(v) for v in self.epost]

        if not isinstance(self.telefon, list):
            self.telefon = [self.telefon] if self.telefon is not None else []
        self.telefon = [v if isinstance(v, str) else str(v) for v in self.telefon]

        if not isinstance(self.kontaktside, list):
            self.kontaktside = [self.kontaktside] if self.kontaktside is not None else []
        self.kontaktside = [v if isinstance(v, URI) else URI(v) for v in self.kontaktside]

        if not isinstance(self.opningstider, list):
            self.opningstider = [self.opningstider] if self.opningstider is not None else []
        self.opningstider = [v if isinstance(v, str) else str(v) for v in self.opningstider]

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

        if not isinstance(self.kategori, list):
            self.kategori = [self.kategori] if self.kategori is not None else []
        self.kategori = [v if isinstance(v, str) else str(v) for v in self.kategori]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tjenestekanal(YAMLRoot):
    """
    Ein kanal for å få tilgang til ei teneste (t.d. nett, telefon, oppmøte).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CV["Channel"]
    class_class_curie: ClassVar[str] = "cv:Channel"
    class_name: ClassVar[str] = "Tjenestekanal"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Tjenestekanal")

    id: Union[str, TjenestekanalId] = None
    identifikator_literal: str = None
    type_concept: Optional[Union[str, KonseptId]] = None
    behandlingstid: Optional[str] = None
    opningstider: Optional[Union[str, list[str]]] = empty_list()
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()
    nettside: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TjenestekanalId):
            self.id = TjenestekanalId(self.id)

        if self._is_empty(self.identifikator_literal):
            self.MissingRequiredField("identifikator_literal")
        if not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        if self.behandlingstid is not None and not isinstance(self.behandlingstid, str):
            self.behandlingstid = str(self.behandlingstid)

        if not isinstance(self.opningstider, list):
            self.opningstider = [self.opningstider] if self.opningstider is not None else []
        self.opningstider = [v if isinstance(v, str) else str(v) for v in self.opningstider]

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if not isinstance(self.nettside, list):
            self.nettside = [self.nettside] if self.nettside is not None else []
        self.nettside = [v if isinstance(v, URI) else URI(v) for v in self.nettside]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dokumentasjonstype(YAMLRoot):
    """
    Ein type dokumentasjon som krevst for å levere ei teneste.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CV["EvidenceType"]
    class_class_curie: ClassVar[str] = "cv:EvidenceType"
    class_name: ClassVar[str] = "Dokumentasjonstype"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Dokumentasjonstype")

    id: Union[str, DokumentasjonstypeId] = None
    tittel: Union[str, list[str]] = None
    beskrivelse: Union[str, list[str]] = None
    identifikator_literal: str = None
    gyldig_i: Optional[str] = None
    godtek_spraak: Optional[Union[str, list[str]]] = empty_list()
    klassifisering: Optional[Union[str, KonseptId]] = None
    er_beskrive_av: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    er_spesifisert_i: Optional[Union[str, URIorCURIE]] = None
    utstedingsstad: Optional[Union[str, KonseptId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DokumentasjonstypeId):
            self.id = DokumentasjonstypeId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.beskrivelse):
            self.MissingRequiredField("beskrivelse")
        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self._is_empty(self.identifikator_literal):
            self.MissingRequiredField("identifikator_literal")
        if not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self.gyldig_i is not None and not isinstance(self.gyldig_i, str):
            self.gyldig_i = str(self.gyldig_i)

        if not isinstance(self.godtek_spraak, list):
            self.godtek_spraak = [self.godtek_spraak] if self.godtek_spraak is not None else []
        self.godtek_spraak = [v if isinstance(v, str) else str(v) for v in self.godtek_spraak]

        if self.klassifisering is not None and not isinstance(self.klassifisering, KonseptId):
            self.klassifisering = KonseptId(self.klassifisering)

        if not isinstance(self.er_beskrive_av, list):
            self.er_beskrive_av = [self.er_beskrive_av] if self.er_beskrive_av is not None else []
        self.er_beskrive_av = [v if isinstance(v, URI) else URI(v) for v in self.er_beskrive_av]

        if self.er_spesifisert_i is not None and not isinstance(self.er_spesifisert_i, URIorCURIE):
            self.er_spesifisert_i = URIorCURIE(self.er_spesifisert_i)

        if self.utstedingsstad is not None and not isinstance(self.utstedingsstad, KonseptId):
            self.utstedingsstad = KonseptId(self.utstedingsstad)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tjenesteresultattype(YAMLRoot):
    """
    Typen resultat som ei teneste produserer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CPSVNO["OutputType"]
    class_class_curie: ClassVar[str] = "cpsvno:OutputType"
    class_name: ClassVar[str] = "Tjenesteresultattype"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Tjenesteresultattype")

    id: Union[str, TjenesteresultattypeId] = None
    tittel: Union[str, list[str]] = None
    beskrivelse: Union[str, list[str]] = None
    identifikator_literal: Optional[str] = None
    mogleg_spraak: Optional[Union[str, list[str]]] = empty_list()
    er_beskrive_av: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    er_spesifisert_i: Optional[Union[str, URIorCURIE]] = None
    kan_skape_hending: Optional[Union[Union[str, HendelseId], list[Union[str, HendelseId]]]] = empty_list()
    type_concept: Optional[Union[str, KonseptId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TjenesteresultattypeId):
            self.id = TjenesteresultattypeId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.beskrivelse):
            self.MissingRequiredField("beskrivelse")
        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if not isinstance(self.mogleg_spraak, list):
            self.mogleg_spraak = [self.mogleg_spraak] if self.mogleg_spraak is not None else []
        self.mogleg_spraak = [v if isinstance(v, str) else str(v) for v in self.mogleg_spraak]

        if not isinstance(self.er_beskrive_av, list):
            self.er_beskrive_av = [self.er_beskrive_av] if self.er_beskrive_av is not None else []
        self.er_beskrive_av = [v if isinstance(v, URI) else URI(v) for v in self.er_beskrive_av]

        if self.er_spesifisert_i is not None and not isinstance(self.er_spesifisert_i, URIorCURIE):
            self.er_spesifisert_i = URIorCURIE(self.er_spesifisert_i)

        if not isinstance(self.kan_skape_hending, list):
            self.kan_skape_hending = [self.kan_skape_hending] if self.kan_skape_hending is not None else []
        self.kan_skape_hending = [v if isinstance(v, HendelseId) else HendelseId(v) for v in self.kan_skape_hending]

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tjenesteresultattypeliste(YAMLRoot):
    """
    Ei liste over moglege tjenesteresultattypar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CPSVNO["OutputTypeList"]
    class_class_curie: ClassVar[str] = "cpsvno:OutputTypeList"
    class_name: ClassVar[str] = "Tjenesteresultattypeliste"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Tjenesteresultattypeliste")

    id: Union[str, TjenesteresultattypelisteId] = None
    tittel: Optional[Union[str, list[str]]] = empty_list()
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TjenesteresultattypelisteId):
            self.id = TjenesteresultattypelisteId(self.id)

        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Gebyr(YAMLRoot):
    """
    Eit gebyr knytt til ei teneste.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CV["Cost"]
    class_class_curie: ClassVar[str] = "cv:Cost"
    class_name: ClassVar[str] = "Gebyr"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Gebyr")

    id: Union[str, GebyrId] = None
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()
    identifikator_literal: Optional[str] = None
    verdi: Optional[float] = None
    valuta: Optional[Union[str, KonseptId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GebyrId):
            self.id = GebyrId(self.id)

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self.verdi is not None and not isinstance(self.verdi, float):
            self.verdi = float(self.verdi)

        if self.valuta is not None and not isinstance(self.valuta, KonseptId):
            self.valuta = KonseptId(self.valuta)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Regel(YAMLRoot):
    """
    Eit regelverk eller retningsliner som styrer levering av ei teneste.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CPSV["Rule"]
    class_class_curie: ClassVar[str] = "cpsv:Rule"
    class_name: ClassVar[str] = "Regel"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Regel")

    id: Union[str, RegelId] = None
    tittel: Optional[Union[str, list[str]]] = empty_list()
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()
    identifikator_literal: Optional[str] = None
    spraak: Optional[Union[str, list[str]]] = empty_list()
    type_concept: Optional[Union[str, KonseptId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegelId):
            self.id = RegelId(self.id)

        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RegulativRessurs(YAMLRoot):
    """
    Ein regulativ ressurs (lov, forskrift o.l.) knytt til ei teneste.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ELI["LegalResource"]
    class_class_curie: ClassVar[str] = "eli:LegalResource"
    class_name: ClassVar[str] = "RegulativRessurs"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/RegulativRessurs")

    id: Union[str, RegulativRessursId] = None
    tittel: Optional[Union[str, list[str]]] = empty_list()
    identifikator_literal: Optional[str] = None
    type_concept: Optional[Union[str, KonseptId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegulativRessursId):
            self.id = RegulativRessursId(self.id)

        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Deltagelse(YAMLRoot):
    """
    Ei rolle ein aktør har i leveringa av ei teneste.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CV["Participation"]
    class_class_curie: ClassVar[str] = "cv:Participation"
    class_name: ClassVar[str] = "Deltagelse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Deltagelse")

    id: Union[str, DeltagelseId] = None
    har_rolle: Optional[Union[str, KonseptId]] = None
    deltakar: Optional[Union[str, AktorId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeltagelseId):
            self.id = DeltagelseId(self.id)

        if self.har_rolle is not None and not isinstance(self.har_rolle, KonseptId):
            self.har_rolle = KonseptId(self.har_rolle)

        if self.deltakar is not None and not isinstance(self.deltakar, AktorId):
            self.deltakar = AktorId(self.deltakar)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Adresse(YAMLRoot):
    """
    Ei postadresse knytt til ein aktør, organisasjon eller kontaktpunkt.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCN["Address"]
    class_class_curie: ClassVar[str] = "locn:Address"
    class_name: ClassVar[str] = "Adresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Adresse")

    id: Union[str, AdresseId] = None
    full_adresse: Optional[Union[str, list[str]]] = empty_list()
    postnummer: Optional[str] = None
    poststad: Optional[Union[str, list[str]]] = empty_list()
    land: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdresseId):
            self.id = AdresseId(self.id)

        if not isinstance(self.full_adresse, list):
            self.full_adresse = [self.full_adresse] if self.full_adresse is not None else []
        self.full_adresse = [v if isinstance(v, str) else str(v) for v in self.full_adresse]

        if self.postnummer is not None and not isinstance(self.postnummer, str):
            self.postnummer = str(self.postnummer)

        if not isinstance(self.poststad, list):
            self.poststad = [self.poststad] if self.poststad is not None else []
        self.poststad = [v if isinstance(v, str) else str(v) for v in self.poststad]

        if self.land is not None and not isinstance(self.land, str):
            self.land = str(self.land)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Katalog(YAMLRoot):
    """
    Ein katalog over offentlege tenester og hendingar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Catalog"]
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "Katalog"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Katalog")

    id: Union[str, KatalogId] = None
    tittel: Union[str, list[str]] = None
    beskrivelse: Union[str, list[str]] = None
    identifikator_literal: str = None
    inneheld_teneste: Union[Union[str, OffentligTjenesteId], list[Union[str, OffentligTjenesteId]]] = None
    har_kontaktpunkt: Union[Union[str, KontaktpunktId], list[Union[str, KontaktpunktId]]] = None
    utgjevar: Union[str, AktorId] = None
    dekningsomraade: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    endringsdato: Optional[Union[str, XSDDate]] = None
    oppdateringsfrekvens: Optional[Union[str, KonseptId]] = None
    heimeside: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    inneheld_hending: Optional[Union[Union[str, HendelseId], list[Union[str, HendelseId]]]] = empty_list()
    lisens: Optional[Union[str, URI]] = None
    spraak: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KatalogId):
            self.id = KatalogId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.beskrivelse):
            self.MissingRequiredField("beskrivelse")
        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self._is_empty(self.identifikator_literal):
            self.MissingRequiredField("identifikator_literal")
        if not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self._is_empty(self.inneheld_teneste):
            self.MissingRequiredField("inneheld_teneste")
        if not isinstance(self.inneheld_teneste, list):
            self.inneheld_teneste = [self.inneheld_teneste] if self.inneheld_teneste is not None else []
        self.inneheld_teneste = [v if isinstance(v, OffentligTjenesteId) else OffentligTjenesteId(v) for v in self.inneheld_teneste]

        if self._is_empty(self.har_kontaktpunkt):
            self.MissingRequiredField("har_kontaktpunkt")
        if not isinstance(self.har_kontaktpunkt, list):
            self.har_kontaktpunkt = [self.har_kontaktpunkt] if self.har_kontaktpunkt is not None else []
        self.har_kontaktpunkt = [v if isinstance(v, KontaktpunktId) else KontaktpunktId(v) for v in self.har_kontaktpunkt]

        if self._is_empty(self.utgjevar):
            self.MissingRequiredField("utgjevar")
        if not isinstance(self.utgjevar, AktorId):
            self.utgjevar = AktorId(self.utgjevar)

        if not isinstance(self.dekningsomraade, list):
            self.dekningsomraade = [self.dekningsomraade] if self.dekningsomraade is not None else []
        self.dekningsomraade = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.dekningsomraade]

        if self.endringsdato is not None and not isinstance(self.endringsdato, XSDDate):
            self.endringsdato = XSDDate(self.endringsdato)

        if self.oppdateringsfrekvens is not None and not isinstance(self.oppdateringsfrekvens, KonseptId):
            self.oppdateringsfrekvens = KonseptId(self.oppdateringsfrekvens)

        if not isinstance(self.heimeside, list):
            self.heimeside = [self.heimeside] if self.heimeside is not None else []
        self.heimeside = [v if isinstance(v, URI) else URI(v) for v in self.heimeside]

        if not isinstance(self.inneheld_hending, list):
            self.inneheld_hending = [self.inneheld_hending] if self.inneheld_hending is not None else []
        self.inneheld_hending = [v if isinstance(v, HendelseId) else HendelseId(v) for v in self.inneheld_hending]

        if self.lisens is not None and not isinstance(self.lisens, URI):
            self.lisens = URI(self.lisens)

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Mediatype")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Konsept")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/cpsv-ap-no/Begrepssamling")

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

slots.har_kontaktpunkt = Slot(uri=CV.contactPoint, name="har_kontaktpunkt", curie=CV.curie('contactPoint'),
                   model_uri=DEFAULT_.har_kontaktpunkt, domain=None, range=Optional[Union[Union[str, KontaktpunktId], list[Union[str, KontaktpunktId]]]])

slots.har_tenesteresultattype = Slot(uri=CPSVNO.hasOutputType, name="har_tenesteresultattype", curie=CPSVNO.curie('hasOutputType'),
                   model_uri=DEFAULT_.har_tenesteresultattype, domain=None, range=Optional[Union[Union[str, TjenesteresultattypeId], list[Union[str, TjenesteresultattypeId]]]])

slots.har_ansvarleg_styremakt = Slot(uri=CV.hasCompetentAuthority, name="har_ansvarleg_styremakt", curie=CV.curie('hasCompetentAuthority'),
                   model_uri=DEFAULT_.har_ansvarleg_styremakt, domain=None, range=Optional[Union[Union[str, OffentligOrganisasjonId], list[Union[str, OffentligOrganisasjonId]]]])

slots.behandlingstid = Slot(uri=CV.processingTime, name="behandlingstid", curie=CV.curie('processingTime'),
                   model_uri=DEFAULT_.behandlingstid, domain=None, range=Optional[str])

slots.er_beskrive_av = Slot(uri=CCCEVNO.isDescribedBy, name="er_beskrive_av", curie=CCCEVNO.curie('isDescribedBy'),
                   model_uri=DEFAULT_.er_beskrive_av, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.har_tenestekanal = Slot(uri=CV.hasChannel, name="har_tenestekanal", curie=CV.curie('hasChannel'),
                   model_uri=DEFAULT_.har_tenestekanal, domain=None, range=Optional[Union[Union[str, TjenestekanalId], list[Union[str, TjenestekanalId]]]])

slots.har_deltaking = Slot(uri=CV.hasParticipation, name="har_deltaking", curie=CV.curie('hasParticipation'),
                   model_uri=DEFAULT_.har_deltaking, domain=None, range=Optional[Union[Union[str, DeltagelseId], list[Union[str, DeltagelseId]]]])

slots.relatert_teneste = Slot(uri=CV.relatedService, name="relatert_teneste", curie=CV.curie('relatedService'),
                   model_uri=DEFAULT_.relatert_teneste, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.er_del_av = Slot(uri=DCT.isPartOf, name="er_del_av", curie=DCT.curie('isPartOf'),
                   model_uri=DEFAULT_.er_del_av, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.har_del = Slot(uri=DCT.hasPart, name="har_del", curie=DCT.curie('hasPart'),
                   model_uri=DEFAULT_.har_del, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.er_gruppert_av = Slot(uri=CV.isGroupedBy, name="er_gruppert_av", curie=CV.curie('isGroupedBy'),
                   model_uri=DEFAULT_.er_gruppert_av, domain=None, range=Optional[Union[Union[str, HendelseId], list[Union[str, HendelseId]]]])

slots.er_klassifisert_av = Slot(uri=CV.isClassifiedBy, name="er_klassifisert_av", curie=CV.curie('isClassifiedBy'),
                   model_uri=DEFAULT_.er_klassifisert_av, domain=None, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.folger = Slot(uri=CPSV.follows, name="folger", curie=CPSV.curie('follows'),
                   model_uri=DEFAULT_.folger, domain=None, range=Optional[Union[Union[str, RegelId], list[Union[str, RegelId]]]])

slots.har_gebyr = Slot(uri=CV.hasCost, name="har_gebyr", curie=CV.curie('hasCost'),
                   model_uri=DEFAULT_.har_gebyr, domain=None, range=Optional[Union[Union[str, GebyrId], list[Union[str, GebyrId]]]])

slots.har_regulativ_ressurs = Slot(uri=CV.hasLegalResource, name="har_regulativ_ressurs", curie=CV.curie('hasLegalResource'),
                   model_uri=DEFAULT_.har_regulativ_ressurs, domain=None, range=Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]])

slots.krev = Slot(uri=DCT.requires, name="krev", curie=DCT.curie('requires'),
                   model_uri=DEFAULT_.krev, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.malgruppe = Slot(uri=DCT.audience, name="malgruppe", curie=DCT.curie('audience'),
                   model_uri=DEFAULT_.malgruppe, domain=None, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.sektor = Slot(uri=CV.sector, name="sektor", curie=CV.curie('sector'),
                   model_uri=DEFAULT_.sektor, domain=None, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.tema = Slot(uri=DCT.subject, name="tema", curie=DCT.curie('subject'),
                   model_uri=DEFAULT_.tema, domain=None, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.temaomrade = Slot(uri=CV.thematicArea, name="temaomrade", curie=CV.curie('thematicArea'),
                   model_uri=DEFAULT_.temaomrade, domain=None, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.har_dokumentasjonstype = Slot(uri=CV.hasInputType, name="har_dokumentasjonstype", curie=CV.curie('hasInputType'),
                   model_uri=DEFAULT_.har_dokumentasjonstype, domain=None, range=Optional[Union[Union[str, DokumentasjonstypeId], list[Union[str, DokumentasjonstypeId]]]])

slots.eigd_av = Slot(uri=CV.ownedBy, name="eigd_av", curie=CV.curie('ownedBy'),
                   model_uri=DEFAULT_.eigd_av, domain=None, range=Optional[Union[Union[str, AktorId], list[Union[str, AktorId]]]])

slots.kan_utlose = Slot(uri=CPSVNO.mayTrigger, name="kan_utlose", curie=CPSVNO.curie('mayTrigger'),
                   model_uri=DEFAULT_.kan_utlose, domain=None, range=Optional[Union[Union[str, OffentligTjenesteId], list[Union[str, OffentligTjenesteId]]]])

slots.kan_utlose_behov_for = Slot(uri=CPSVNO.mayTriggerNeedFor, name="kan_utlose_behov_for", curie=CPSVNO.curie('mayTriggerNeedFor'),
                   model_uri=DEFAULT_.kan_utlose_behov_for, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.foretrekt_namn = Slot(uri=SKOS.prefLabel, name="foretrekt_namn", curie=SKOS.curie('prefLabel'),
                   model_uri=DEFAULT_.foretrekt_namn, domain=None, range=Optional[Union[str, list[str]]])

slots.adresse_ref = Slot(uri=LOCN.address, name="adresse_ref", curie=LOCN.curie('address'),
                   model_uri=DEFAULT_.adresse_ref, domain=None, range=Optional[Union[str, AdresseId]])

slots.deltek_i = Slot(uri=CV.participates, name="deltek_i", curie=CV.curie('participates'),
                   model_uri=DEFAULT_.deltek_i, domain=None, range=Optional[Union[Union[str, DeltagelseId], list[Union[str, DeltagelseId]]]])

slots.har_rolle = Slot(uri=CV.role, name="har_rolle", curie=CV.curie('role'),
                   model_uri=DEFAULT_.har_rolle, domain=None, range=Optional[Union[str, KonseptId]])

slots.deltakar = Slot(uri=CV.participant, name="deltakar", curie=CV.curie('participant'),
                   model_uri=DEFAULT_.deltakar, domain=None, range=Optional[Union[str, AktorId]])

slots.epost = Slot(uri=CV.email, name="epost", curie=CV.curie('email'),
                   model_uri=DEFAULT_.epost, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.telefon = Slot(uri=CV.telephone, name="telefon", curie=CV.curie('telephone'),
                   model_uri=DEFAULT_.telefon, domain=None, range=Optional[Union[str, list[str]]])

slots.kontaktside = Slot(uri=CV.contactPage, name="kontaktside", curie=CV.curie('contactPage'),
                   model_uri=DEFAULT_.kontaktside, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.opningstider = Slot(uri=CV.openingHours, name="opningstider", curie=CV.curie('openingHours'),
                   model_uri=DEFAULT_.opningstider, domain=None, range=Optional[Union[str, list[str]]])

slots.nettside = Slot(uri=VCARD.hasURL, name="nettside", curie=VCARD.curie('hasURL'),
                   model_uri=DEFAULT_.nettside, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.kategori = Slot(uri=VCARD.category, name="kategori", curie=VCARD.curie('category'),
                   model_uri=DEFAULT_.kategori, domain=None, range=Optional[Union[str, list[str]]])

slots.gyldig_i = Slot(uri=CCCEVNO.acceptableValidityDuration, name="gyldig_i", curie=CCCEVNO.curie('acceptableValidityDuration'),
                   model_uri=DEFAULT_.gyldig_i, domain=None, range=Optional[str])

slots.godtek_spraak = Slot(uri=CCCEVNO.acceptableLanguage, name="godtek_spraak", curie=CCCEVNO.curie('acceptableLanguage'),
                   model_uri=DEFAULT_.godtek_spraak, domain=None, range=Optional[Union[str, list[str]]])

slots.klassifisering = Slot(uri=CV.evidenceTypeClassification, name="klassifisering", curie=CV.curie('evidenceTypeClassification'),
                   model_uri=DEFAULT_.klassifisering, domain=None, range=Optional[Union[str, KonseptId]])

slots.er_spesifisert_i = Slot(uri=CV.isSpecifiedIn, name="er_spesifisert_i", curie=CV.curie('isSpecifiedIn'),
                   model_uri=DEFAULT_.er_spesifisert_i, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.utstedingsstad = Slot(uri=CCCEVNO.acceptableIssuingPlace, name="utstedingsstad", curie=CCCEVNO.curie('acceptableIssuingPlace'),
                   model_uri=DEFAULT_.utstedingsstad, domain=None, range=Optional[Union[str, KonseptId]])

slots.mogleg_spraak = Slot(uri=CPSVNO.possibleLanguage, name="mogleg_spraak", curie=CPSVNO.curie('possibleLanguage'),
                   model_uri=DEFAULT_.mogleg_spraak, domain=None, range=Optional[Union[str, list[str]]])

slots.kan_skape_hending = Slot(uri=XKOS.causes, name="kan_skape_hending", curie=XKOS.curie('causes'),
                   model_uri=DEFAULT_.kan_skape_hending, domain=None, range=Optional[Union[Union[str, HendelseId], list[Union[str, HendelseId]]]])

slots.verdi = Slot(uri=CV.value, name="verdi", curie=CV.curie('value'),
                   model_uri=DEFAULT_.verdi, domain=None, range=Optional[float])

slots.full_adresse = Slot(uri=LOCN.fullAddress, name="full_adresse", curie=LOCN.curie('fullAddress'),
                   model_uri=DEFAULT_.full_adresse, domain=None, range=Optional[Union[str, list[str]]])

slots.postnummer = Slot(uri=LOCN.postCode, name="postnummer", curie=LOCN.curie('postCode'),
                   model_uri=DEFAULT_.postnummer, domain=None, range=Optional[str])

slots.poststad = Slot(uri=LOCN.postName, name="poststad", curie=LOCN.curie('postName'),
                   model_uri=DEFAULT_.poststad, domain=None, range=Optional[Union[str, list[str]]])

slots.land = Slot(uri=LOCN.adminUnitL1, name="land", curie=LOCN.curie('adminUnitL1'),
                   model_uri=DEFAULT_.land, domain=None, range=Optional[str])

slots.inneheld_teneste = Slot(uri=DCATNO.containsService, name="inneheld_teneste", curie=DCATNO.curie('containsService'),
                   model_uri=DEFAULT_.inneheld_teneste, domain=None, range=Optional[Union[Union[str, OffentligTjenesteId], list[Union[str, OffentligTjenesteId]]]])

slots.inneheld_hending = Slot(uri=DCATNO.containsEvent, name="inneheld_hending", curie=DCATNO.curie('containsEvent'),
                   model_uri=DEFAULT_.inneheld_hending, domain=None, range=Optional[Union[Union[str, HendelseId], list[Union[str, HendelseId]]]])

slots.utgjevar = Slot(uri=DCT.publisher, name="utgjevar", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.utgjevar, domain=None, range=Optional[Union[str, AktorId]])

slots.oppdateringsfrekvens = Slot(uri=DCT.accrualPeriodicity, name="oppdateringsfrekvens", curie=DCT.curie('accrualPeriodicity'),
                   model_uri=DEFAULT_.oppdateringsfrekvens, domain=None, range=Optional[Union[str, KonseptId]])

slots.lisens = Slot(uri=DCT.license, name="lisens", curie=DCT.curie('license'),
                   model_uri=DEFAULT_.lisens, domain=None, range=Optional[Union[str, URI]])

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

slots.OffentligTjeneste_tittel = Slot(uri=DCT.title, name="OffentligTjeneste_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.OffentligTjeneste_tittel, domain=OffentligTjeneste, range=Union[str, list[str]])

slots.OffentligTjeneste_beskrivelse = Slot(uri=DCT.description, name="OffentligTjeneste_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.OffentligTjeneste_beskrivelse, domain=OffentligTjeneste, range=Union[str, list[str]])

slots.OffentligTjeneste_identifikator_literal = Slot(uri=DCT.identifier, name="OffentligTjeneste_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.OffentligTjeneste_identifikator_literal, domain=OffentligTjeneste, range=str)

slots.OffentligTjeneste_har_kontaktpunkt = Slot(uri=CV.contactPoint, name="OffentligTjeneste_har_kontaktpunkt", curie=CV.curie('contactPoint'),
                   model_uri=DEFAULT_.OffentligTjeneste_har_kontaktpunkt, domain=OffentligTjeneste, range=Union[Union[str, KontaktpunktId], list[Union[str, KontaktpunktId]]])

slots.OffentligTjeneste_har_tenesteresultattype = Slot(uri=CPSVNO.hasOutputType, name="OffentligTjeneste_har_tenesteresultattype", curie=CPSVNO.curie('hasOutputType'),
                   model_uri=DEFAULT_.OffentligTjeneste_har_tenesteresultattype, domain=OffentligTjeneste, range=Union[Union[str, TjenesteresultattypeId], list[Union[str, TjenesteresultattypeId]]])

slots.OffentligTjeneste_har_ansvarleg_styremakt = Slot(uri=CV.hasCompetentAuthority, name="OffentligTjeneste_har_ansvarleg_styremakt", curie=CV.curie('hasCompetentAuthority'),
                   model_uri=DEFAULT_.OffentligTjeneste_har_ansvarleg_styremakt, domain=OffentligTjeneste, range=Union[Union[str, OffentligOrganisasjonId], list[Union[str, OffentligOrganisasjonId]]])

slots.OffentligTjeneste_tema = Slot(uri=DCT.subject, name="OffentligTjeneste_tema", curie=DCT.curie('subject'),
                   model_uri=DEFAULT_.OffentligTjeneste_tema, domain=OffentligTjeneste, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.OffentligTjeneste_dekningsomraade = Slot(uri=DCT.spatial, name="OffentligTjeneste_dekningsomraade", curie=DCT.curie('spatial'),
                   model_uri=DEFAULT_.OffentligTjeneste_dekningsomraade, domain=OffentligTjeneste, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.OffentligTjeneste_har_dokumentasjonstype = Slot(uri=CV.hasInputType, name="OffentligTjeneste_har_dokumentasjonstype", curie=CV.curie('hasInputType'),
                   model_uri=DEFAULT_.OffentligTjeneste_har_dokumentasjonstype, domain=OffentligTjeneste, range=Optional[Union[Union[str, DokumentasjonstypeId], list[Union[str, DokumentasjonstypeId]]]])

slots.OffentligTjeneste_heimeside = Slot(uri=FOAF.homepage, name="OffentligTjeneste_heimeside", curie=FOAF.curie('homepage'),
                   model_uri=DEFAULT_.OffentligTjeneste_heimeside, domain=OffentligTjeneste, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.OffentligTjeneste_type_concept = Slot(uri=DCT.type, name="OffentligTjeneste_type_concept", curie=DCT.curie('type'),
                   model_uri=DEFAULT_.OffentligTjeneste_type_concept, domain=OffentligTjeneste, range=Optional[Union[str, KonseptId]])

slots.OffentligTjeneste_status = Slot(uri=ADMS.status, name="OffentligTjeneste_status", curie=ADMS.curie('status'),
                   model_uri=DEFAULT_.OffentligTjeneste_status, domain=OffentligTjeneste, range=Optional[Union[str, KonseptId]])

slots.OffentligTjeneste_temaomrade = Slot(uri=CV.thematicArea, name="OffentligTjeneste_temaomrade", curie=CV.curie('thematicArea'),
                   model_uri=DEFAULT_.OffentligTjeneste_temaomrade, domain=OffentligTjeneste, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.OffentligTjeneste_behandlingstid = Slot(uri=CV.processingTime, name="OffentligTjeneste_behandlingstid", curie=CV.curie('processingTime'),
                   model_uri=DEFAULT_.OffentligTjeneste_behandlingstid, domain=OffentligTjeneste, range=Optional[str])

slots.OffentligTjeneste_er_beskrive_av = Slot(uri=CCCEVNO.isDescribedBy, name="OffentligTjeneste_er_beskrive_av", curie=CCCEVNO.curie('isDescribedBy'),
                   model_uri=DEFAULT_.OffentligTjeneste_er_beskrive_av, domain=OffentligTjeneste, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.OffentligTjeneste_er_del_av = Slot(uri=DCT.isPartOf, name="OffentligTjeneste_er_del_av", curie=DCT.curie('isPartOf'),
                   model_uri=DEFAULT_.OffentligTjeneste_er_del_av, domain=OffentligTjeneste, range=Optional[Union[str, URIorCURIE]])

slots.OffentligTjeneste_har_del = Slot(uri=DCT.hasPart, name="OffentligTjeneste_har_del", curie=DCT.curie('hasPart'),
                   model_uri=DEFAULT_.OffentligTjeneste_har_del, domain=OffentligTjeneste, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.OffentligTjeneste_har_tenestekanal = Slot(uri=CV.hasChannel, name="OffentligTjeneste_har_tenestekanal", curie=CV.curie('hasChannel'),
                   model_uri=DEFAULT_.OffentligTjeneste_har_tenestekanal, domain=OffentligTjeneste, range=Optional[Union[Union[str, TjenestekanalId], list[Union[str, TjenestekanalId]]]])

slots.OffentligTjeneste_har_deltaking = Slot(uri=CV.hasParticipation, name="OffentligTjeneste_har_deltaking", curie=CV.curie('hasParticipation'),
                   model_uri=DEFAULT_.OffentligTjeneste_har_deltaking, domain=OffentligTjeneste, range=Optional[Union[Union[str, DeltagelseId], list[Union[str, DeltagelseId]]]])

slots.OffentligTjeneste_spraak = Slot(uri=DCT.language, name="OffentligTjeneste_spraak", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.OffentligTjeneste_spraak, domain=OffentligTjeneste, range=Optional[Union[str, list[str]]])

slots.OffentligTjeneste_relatert_teneste = Slot(uri=CV.relatedService, name="OffentligTjeneste_relatert_teneste", curie=CV.curie('relatedService'),
                   model_uri=DEFAULT_.OffentligTjeneste_relatert_teneste, domain=OffentligTjeneste, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.OffentligTjeneste_er_gruppert_av = Slot(uri=CV.isGroupedBy, name="OffentligTjeneste_er_gruppert_av", curie=CV.curie('isGroupedBy'),
                   model_uri=DEFAULT_.OffentligTjeneste_er_gruppert_av, domain=OffentligTjeneste, range=Optional[Union[Union[str, HendelseId], list[Union[str, HendelseId]]]])

slots.OffentligTjeneste_er_klassifisert_av = Slot(uri=CV.isClassifiedBy, name="OffentligTjeneste_er_klassifisert_av", curie=CV.curie('isClassifiedBy'),
                   model_uri=DEFAULT_.OffentligTjeneste_er_klassifisert_av, domain=OffentligTjeneste, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.OffentligTjeneste_folger = Slot(uri=CPSV.follows, name="OffentligTjeneste_folger", curie=CPSV.curie('follows'),
                   model_uri=DEFAULT_.OffentligTjeneste_folger, domain=OffentligTjeneste, range=Optional[Union[Union[str, RegelId], list[Union[str, RegelId]]]])

slots.OffentligTjeneste_har_gebyr = Slot(uri=CV.hasCost, name="OffentligTjeneste_har_gebyr", curie=CV.curie('hasCost'),
                   model_uri=DEFAULT_.OffentligTjeneste_har_gebyr, domain=OffentligTjeneste, range=Optional[Union[Union[str, GebyrId], list[Union[str, GebyrId]]]])

slots.OffentligTjeneste_har_regulativ_ressurs = Slot(uri=CV.hasLegalResource, name="OffentligTjeneste_har_regulativ_ressurs", curie=CV.curie('hasLegalResource'),
                   model_uri=DEFAULT_.OffentligTjeneste_har_regulativ_ressurs, domain=OffentligTjeneste, range=Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]])

slots.OffentligTjeneste_krev = Slot(uri=DCT.requires, name="OffentligTjeneste_krev", curie=DCT.curie('requires'),
                   model_uri=DEFAULT_.OffentligTjeneste_krev, domain=OffentligTjeneste, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.OffentligTjeneste_malgruppe = Slot(uri=DCT.audience, name="OffentligTjeneste_malgruppe", curie=DCT.curie('audience'),
                   model_uri=DEFAULT_.OffentligTjeneste_malgruppe, domain=OffentligTjeneste, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.OffentligTjeneste_nokkelord = Slot(uri=DCAT.keyword, name="OffentligTjeneste_nokkelord", curie=DCAT.curie('keyword'),
                   model_uri=DEFAULT_.OffentligTjeneste_nokkelord, domain=OffentligTjeneste, range=Optional[Union[str, list[str]]])

slots.OffentligTjeneste_sektor = Slot(uri=CV.sector, name="OffentligTjeneste_sektor", curie=CV.curie('sector'),
                   model_uri=DEFAULT_.OffentligTjeneste_sektor, domain=OffentligTjeneste, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Tjeneste_tittel = Slot(uri=DCT.title, name="Tjeneste_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Tjeneste_tittel, domain=Tjeneste, range=Union[str, list[str]])

slots.Tjeneste_beskrivelse = Slot(uri=DCT.description, name="Tjeneste_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.Tjeneste_beskrivelse, domain=Tjeneste, range=Union[str, list[str]])

slots.Tjeneste_identifikator_literal = Slot(uri=DCT.identifier, name="Tjeneste_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Tjeneste_identifikator_literal, domain=Tjeneste, range=str)

slots.Tjeneste_har_kontaktpunkt = Slot(uri=CV.contactPoint, name="Tjeneste_har_kontaktpunkt", curie=CV.curie('contactPoint'),
                   model_uri=DEFAULT_.Tjeneste_har_kontaktpunkt, domain=Tjeneste, range=Union[Union[str, KontaktpunktId], list[Union[str, KontaktpunktId]]])

slots.Tjeneste_har_tenesteresultattype = Slot(uri=CPSVNO.hasOutputType, name="Tjeneste_har_tenesteresultattype", curie=CPSVNO.curie('hasOutputType'),
                   model_uri=DEFAULT_.Tjeneste_har_tenesteresultattype, domain=Tjeneste, range=Union[Union[str, TjenesteresultattypeId], list[Union[str, TjenesteresultattypeId]]])

slots.Tjeneste_eigd_av = Slot(uri=CV.ownedBy, name="Tjeneste_eigd_av", curie=CV.curie('ownedBy'),
                   model_uri=DEFAULT_.Tjeneste_eigd_av, domain=Tjeneste, range=Union[Union[str, AktorId], list[Union[str, AktorId]]])

slots.Tjeneste_tema = Slot(uri=DCT.subject, name="Tjeneste_tema", curie=DCT.curie('subject'),
                   model_uri=DEFAULT_.Tjeneste_tema, domain=Tjeneste, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Tjeneste_dekningsomraade = Slot(uri=DCT.spatial, name="Tjeneste_dekningsomraade", curie=DCT.curie('spatial'),
                   model_uri=DEFAULT_.Tjeneste_dekningsomraade, domain=Tjeneste, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Tjeneste_har_dokumentasjonstype = Slot(uri=CV.hasInputType, name="Tjeneste_har_dokumentasjonstype", curie=CV.curie('hasInputType'),
                   model_uri=DEFAULT_.Tjeneste_har_dokumentasjonstype, domain=Tjeneste, range=Optional[Union[Union[str, DokumentasjonstypeId], list[Union[str, DokumentasjonstypeId]]]])

slots.Tjeneste_heimeside = Slot(uri=FOAF.homepage, name="Tjeneste_heimeside", curie=FOAF.curie('homepage'),
                   model_uri=DEFAULT_.Tjeneste_heimeside, domain=Tjeneste, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Tjeneste_status = Slot(uri=ADMS.status, name="Tjeneste_status", curie=ADMS.curie('status'),
                   model_uri=DEFAULT_.Tjeneste_status, domain=Tjeneste, range=Optional[Union[str, KonseptId]])

slots.Tjeneste_temaomrade = Slot(uri=CV.thematicArea, name="Tjeneste_temaomrade", curie=CV.curie('thematicArea'),
                   model_uri=DEFAULT_.Tjeneste_temaomrade, domain=Tjeneste, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Tjeneste_behandlingstid = Slot(uri=CV.processingTime, name="Tjeneste_behandlingstid", curie=CV.curie('processingTime'),
                   model_uri=DEFAULT_.Tjeneste_behandlingstid, domain=Tjeneste, range=Optional[str])

slots.Tjeneste_er_beskrive_av = Slot(uri=CCCEVNO.isDescribedBy, name="Tjeneste_er_beskrive_av", curie=CCCEVNO.curie('isDescribedBy'),
                   model_uri=DEFAULT_.Tjeneste_er_beskrive_av, domain=Tjeneste, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Tjeneste_er_del_av = Slot(uri=DCT.isPartOf, name="Tjeneste_er_del_av", curie=DCT.curie('isPartOf'),
                   model_uri=DEFAULT_.Tjeneste_er_del_av, domain=Tjeneste, range=Optional[Union[str, URIorCURIE]])

slots.Tjeneste_har_del = Slot(uri=DCT.hasPart, name="Tjeneste_har_del", curie=DCT.curie('hasPart'),
                   model_uri=DEFAULT_.Tjeneste_har_del, domain=Tjeneste, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Tjeneste_har_tenestekanal = Slot(uri=CV.hasChannel, name="Tjeneste_har_tenestekanal", curie=CV.curie('hasChannel'),
                   model_uri=DEFAULT_.Tjeneste_har_tenestekanal, domain=Tjeneste, range=Optional[Union[Union[str, TjenestekanalId], list[Union[str, TjenestekanalId]]]])

slots.Tjeneste_har_deltaking = Slot(uri=CV.hasParticipation, name="Tjeneste_har_deltaking", curie=CV.curie('hasParticipation'),
                   model_uri=DEFAULT_.Tjeneste_har_deltaking, domain=Tjeneste, range=Optional[Union[Union[str, DeltagelseId], list[Union[str, DeltagelseId]]]])

slots.Tjeneste_spraak = Slot(uri=DCT.language, name="Tjeneste_spraak", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.Tjeneste_spraak, domain=Tjeneste, range=Optional[Union[str, list[str]]])

slots.Tjeneste_relatert_teneste = Slot(uri=CV.relatedService, name="Tjeneste_relatert_teneste", curie=CV.curie('relatedService'),
                   model_uri=DEFAULT_.Tjeneste_relatert_teneste, domain=Tjeneste, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Tjeneste_er_gruppert_av = Slot(uri=CV.isGroupedBy, name="Tjeneste_er_gruppert_av", curie=CV.curie('isGroupedBy'),
                   model_uri=DEFAULT_.Tjeneste_er_gruppert_av, domain=Tjeneste, range=Optional[Union[Union[str, HendelseId], list[Union[str, HendelseId]]]])

slots.Tjeneste_er_klassifisert_av = Slot(uri=CV.isClassifiedBy, name="Tjeneste_er_klassifisert_av", curie=CV.curie('isClassifiedBy'),
                   model_uri=DEFAULT_.Tjeneste_er_klassifisert_av, domain=Tjeneste, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Tjeneste_folger = Slot(uri=CPSV.follows, name="Tjeneste_folger", curie=CPSV.curie('follows'),
                   model_uri=DEFAULT_.Tjeneste_folger, domain=Tjeneste, range=Optional[Union[Union[str, RegelId], list[Union[str, RegelId]]]])

slots.Tjeneste_har_gebyr = Slot(uri=CV.hasCost, name="Tjeneste_har_gebyr", curie=CV.curie('hasCost'),
                   model_uri=DEFAULT_.Tjeneste_har_gebyr, domain=Tjeneste, range=Optional[Union[Union[str, GebyrId], list[Union[str, GebyrId]]]])

slots.Tjeneste_har_regulativ_ressurs = Slot(uri=CV.hasLegalResource, name="Tjeneste_har_regulativ_ressurs", curie=CV.curie('hasLegalResource'),
                   model_uri=DEFAULT_.Tjeneste_har_regulativ_ressurs, domain=Tjeneste, range=Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]])

slots.Tjeneste_krev = Slot(uri=DCT.requires, name="Tjeneste_krev", curie=DCT.curie('requires'),
                   model_uri=DEFAULT_.Tjeneste_krev, domain=Tjeneste, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Tjeneste_malgruppe = Slot(uri=DCT.audience, name="Tjeneste_malgruppe", curie=DCT.curie('audience'),
                   model_uri=DEFAULT_.Tjeneste_malgruppe, domain=Tjeneste, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Tjeneste_nokkelord = Slot(uri=DCAT.keyword, name="Tjeneste_nokkelord", curie=DCAT.curie('keyword'),
                   model_uri=DEFAULT_.Tjeneste_nokkelord, domain=Tjeneste, range=Optional[Union[str, list[str]]])

slots.Tjeneste_sektor = Slot(uri=CV.sector, name="Tjeneste_sektor", curie=CV.curie('sector'),
                   model_uri=DEFAULT_.Tjeneste_sektor, domain=Tjeneste, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Hendelse_tittel = Slot(uri=DCT.title, name="Hendelse_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Hendelse_tittel, domain=Hendelse, range=Union[str, list[str]])

slots.Hendelse_identifikator_literal = Slot(uri=DCT.identifier, name="Hendelse_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Hendelse_identifikator_literal, domain=Hendelse, range=str)

slots.Hendelse_har_kontaktpunkt = Slot(uri=CV.contactPoint, name="Hendelse_har_kontaktpunkt", curie=CV.curie('contactPoint'),
                   model_uri=DEFAULT_.Hendelse_har_kontaktpunkt, domain=Hendelse, range=Union[Union[str, KontaktpunktId], list[Union[str, KontaktpunktId]]])

slots.Hendelse_beskrivelse = Slot(uri=DCT.description, name="Hendelse_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.Hendelse_beskrivelse, domain=Hendelse, range=Optional[Union[str, list[str]]])

slots.Hendelse_kan_utlose = Slot(uri=CPSVNO.mayTrigger, name="Hendelse_kan_utlose", curie=CPSVNO.curie('mayTrigger'),
                   model_uri=DEFAULT_.Hendelse_kan_utlose, domain=Hendelse, range=Optional[Union[Union[str, OffentligTjenesteId], list[Union[str, OffentligTjenesteId]]]])

slots.Hendelse_tema = Slot(uri=DCT.subject, name="Hendelse_tema", curie=DCT.curie('subject'),
                   model_uri=DEFAULT_.Hendelse_tema, domain=Hendelse, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Hendelse_er_beskrive_av = Slot(uri=CCCEVNO.isDescribedBy, name="Hendelse_er_beskrive_av", curie=CCCEVNO.curie('isDescribedBy'),
                   model_uri=DEFAULT_.Hendelse_er_beskrive_av, domain=Hendelse, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Hendelse_type_concept = Slot(uri=DCT.type, name="Hendelse_type_concept", curie=DCT.curie('type'),
                   model_uri=DEFAULT_.Hendelse_type_concept, domain=Hendelse, range=Optional[Union[str, KonseptId]])

slots.Livshendelse_kan_utlose_behov_for = Slot(uri=CPSVNO.mayTriggerNeedFor, name="Livshendelse_kan_utlose_behov_for", curie=CPSVNO.curie('mayTriggerNeedFor'),
                   model_uri=DEFAULT_.Livshendelse_kan_utlose_behov_for, domain=Livshendelse, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Virksomhetshendelse_kan_utlose_behov_for = Slot(uri=CPSVNO.mayTriggerNeedFor, name="Virksomhetshendelse_kan_utlose_behov_for", curie=CPSVNO.curie('mayTriggerNeedFor'),
                   model_uri=DEFAULT_.Virksomhetshendelse_kan_utlose_behov_for, domain=Virksomhetshendelse, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Aktor_tittel = Slot(uri=DCT.title, name="Aktor_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Aktor_tittel, domain=Aktor, range=Union[str, list[str]])

slots.Aktor_identifikator_literal = Slot(uri=DCT.identifier, name="Aktor_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Aktor_identifikator_literal, domain=Aktor, range=str)

slots.Aktor_adresse_ref = Slot(uri=LOCN.address, name="Aktor_adresse_ref", curie=LOCN.curie('address'),
                   model_uri=DEFAULT_.Aktor_adresse_ref, domain=Aktor, range=Optional[Union[str, AdresseId]])

slots.Aktor_deltek_i = Slot(uri=CV.participates, name="Aktor_deltek_i", curie=CV.curie('participates'),
                   model_uri=DEFAULT_.Aktor_deltek_i, domain=Aktor, range=Optional[Union[Union[str, DeltagelseId], list[Union[str, DeltagelseId]]]])

slots.OffentligOrganisasjon_dekningsomraade = Slot(uri=DCT.spatial, name="OffentligOrganisasjon_dekningsomraade", curie=DCT.curie('spatial'),
                   model_uri=DEFAULT_.OffentligOrganisasjon_dekningsomraade, domain=OffentligOrganisasjon, range=Union[Union[str, KonseptId], list[Union[str, KonseptId]]])

slots.OffentligOrganisasjon_foretrekt_namn = Slot(uri=SKOS.prefLabel, name="OffentligOrganisasjon_foretrekt_namn", curie=SKOS.curie('prefLabel'),
                   model_uri=DEFAULT_.OffentligOrganisasjon_foretrekt_namn, domain=OffentligOrganisasjon, range=Union[str, list[str]])

slots.OffentligOrganisasjon_type_concept = Slot(uri=DCT.type, name="OffentligOrganisasjon_type_concept", curie=DCT.curie('type'),
                   model_uri=DEFAULT_.OffentligOrganisasjon_type_concept, domain=OffentligOrganisasjon, range=Optional[Union[str, KonseptId]])

slots.OffentligOrganisasjon_heimeside = Slot(uri=FOAF.homepage, name="OffentligOrganisasjon_heimeside", curie=FOAF.curie('homepage'),
                   model_uri=DEFAULT_.OffentligOrganisasjon_heimeside, domain=OffentligOrganisasjon, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.OffentligOrganisasjon_adresse_ref = Slot(uri=LOCN.address, name="OffentligOrganisasjon_adresse_ref", curie=LOCN.curie('address'),
                   model_uri=DEFAULT_.OffentligOrganisasjon_adresse_ref, domain=OffentligOrganisasjon, range=Optional[Union[str, AdresseId]])

slots.Kontaktpunkt_epost = Slot(uri=CV.email, name="Kontaktpunkt_epost", curie=CV.curie('email'),
                   model_uri=DEFAULT_.Kontaktpunkt_epost, domain=Kontaktpunkt, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Kontaktpunkt_telefon = Slot(uri=CV.telephone, name="Kontaktpunkt_telefon", curie=CV.curie('telephone'),
                   model_uri=DEFAULT_.Kontaktpunkt_telefon, domain=Kontaktpunkt, range=Optional[Union[str, list[str]]])

slots.Kontaktpunkt_kontaktside = Slot(uri=CV.contactPage, name="Kontaktpunkt_kontaktside", curie=CV.curie('contactPage'),
                   model_uri=DEFAULT_.Kontaktpunkt_kontaktside, domain=Kontaktpunkt, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Kontaktpunkt_opningstider = Slot(uri=CV.openingHours, name="Kontaktpunkt_opningstider", curie=CV.curie('openingHours'),
                   model_uri=DEFAULT_.Kontaktpunkt_opningstider, domain=Kontaktpunkt, range=Optional[Union[str, list[str]]])

slots.Kontaktpunkt_spraak = Slot(uri=DCT.language, name="Kontaktpunkt_spraak", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.Kontaktpunkt_spraak, domain=Kontaktpunkt, range=Optional[Union[str, list[str]]])

slots.Kontaktpunkt_kategori = Slot(uri=VCARD.category, name="Kontaktpunkt_kategori", curie=VCARD.curie('category'),
                   model_uri=DEFAULT_.Kontaktpunkt_kategori, domain=Kontaktpunkt, range=Optional[Union[str, list[str]]])

slots.Tjenestekanal_identifikator_literal = Slot(uri=DCT.identifier, name="Tjenestekanal_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Tjenestekanal_identifikator_literal, domain=Tjenestekanal, range=str)

slots.Tjenestekanal_type_concept = Slot(uri=DCT.type, name="Tjenestekanal_type_concept", curie=DCT.curie('type'),
                   model_uri=DEFAULT_.Tjenestekanal_type_concept, domain=Tjenestekanal, range=Optional[Union[str, KonseptId]])

slots.Tjenestekanal_behandlingstid = Slot(uri=CV.processingTime, name="Tjenestekanal_behandlingstid", curie=CV.curie('processingTime'),
                   model_uri=DEFAULT_.Tjenestekanal_behandlingstid, domain=Tjenestekanal, range=Optional[str])

slots.Tjenestekanal_opningstider = Slot(uri=CV.openingHours, name="Tjenestekanal_opningstider", curie=CV.curie('openingHours'),
                   model_uri=DEFAULT_.Tjenestekanal_opningstider, domain=Tjenestekanal, range=Optional[Union[str, list[str]]])

slots.Tjenestekanal_beskrivelse = Slot(uri=DCT.description, name="Tjenestekanal_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.Tjenestekanal_beskrivelse, domain=Tjenestekanal, range=Optional[Union[str, list[str]]])

slots.Tjenestekanal_nettside = Slot(uri=VCARD.hasURL, name="Tjenestekanal_nettside", curie=VCARD.curie('hasURL'),
                   model_uri=DEFAULT_.Tjenestekanal_nettside, domain=Tjenestekanal, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Dokumentasjonstype_tittel = Slot(uri=DCT.title, name="Dokumentasjonstype_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Dokumentasjonstype_tittel, domain=Dokumentasjonstype, range=Union[str, list[str]])

slots.Dokumentasjonstype_beskrivelse = Slot(uri=DCT.description, name="Dokumentasjonstype_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.Dokumentasjonstype_beskrivelse, domain=Dokumentasjonstype, range=Union[str, list[str]])

slots.Dokumentasjonstype_identifikator_literal = Slot(uri=DCT.identifier, name="Dokumentasjonstype_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Dokumentasjonstype_identifikator_literal, domain=Dokumentasjonstype, range=str)

slots.Dokumentasjonstype_gyldig_i = Slot(uri=CCCEVNO.acceptableValidityDuration, name="Dokumentasjonstype_gyldig_i", curie=CCCEVNO.curie('acceptableValidityDuration'),
                   model_uri=DEFAULT_.Dokumentasjonstype_gyldig_i, domain=Dokumentasjonstype, range=Optional[str])

slots.Dokumentasjonstype_godtek_spraak = Slot(uri=CCCEVNO.acceptableLanguage, name="Dokumentasjonstype_godtek_spraak", curie=CCCEVNO.curie('acceptableLanguage'),
                   model_uri=DEFAULT_.Dokumentasjonstype_godtek_spraak, domain=Dokumentasjonstype, range=Optional[Union[str, list[str]]])

slots.Dokumentasjonstype_klassifisering = Slot(uri=CV.evidenceTypeClassification, name="Dokumentasjonstype_klassifisering", curie=CV.curie('evidenceTypeClassification'),
                   model_uri=DEFAULT_.Dokumentasjonstype_klassifisering, domain=Dokumentasjonstype, range=Optional[Union[str, KonseptId]])

slots.Dokumentasjonstype_er_beskrive_av = Slot(uri=CCCEVNO.isDescribedBy, name="Dokumentasjonstype_er_beskrive_av", curie=CCCEVNO.curie('isDescribedBy'),
                   model_uri=DEFAULT_.Dokumentasjonstype_er_beskrive_av, domain=Dokumentasjonstype, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Dokumentasjonstype_er_spesifisert_i = Slot(uri=CV.isSpecifiedIn, name="Dokumentasjonstype_er_spesifisert_i", curie=CV.curie('isSpecifiedIn'),
                   model_uri=DEFAULT_.Dokumentasjonstype_er_spesifisert_i, domain=Dokumentasjonstype, range=Optional[Union[str, URIorCURIE]])

slots.Dokumentasjonstype_utstedingsstad = Slot(uri=CCCEVNO.acceptableIssuingPlace, name="Dokumentasjonstype_utstedingsstad", curie=CCCEVNO.curie('acceptableIssuingPlace'),
                   model_uri=DEFAULT_.Dokumentasjonstype_utstedingsstad, domain=Dokumentasjonstype, range=Optional[Union[str, KonseptId]])

slots.Tjenesteresultattype_tittel = Slot(uri=DCT.title, name="Tjenesteresultattype_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Tjenesteresultattype_tittel, domain=Tjenesteresultattype, range=Union[str, list[str]])

slots.Tjenesteresultattype_beskrivelse = Slot(uri=DCT.description, name="Tjenesteresultattype_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.Tjenesteresultattype_beskrivelse, domain=Tjenesteresultattype, range=Union[str, list[str]])

slots.Tjenesteresultattype_mogleg_spraak = Slot(uri=CPSVNO.possibleLanguage, name="Tjenesteresultattype_mogleg_spraak", curie=CPSVNO.curie('possibleLanguage'),
                   model_uri=DEFAULT_.Tjenesteresultattype_mogleg_spraak, domain=Tjenesteresultattype, range=Optional[Union[str, list[str]]])

slots.Tjenesteresultattype_identifikator_literal = Slot(uri=DCT.identifier, name="Tjenesteresultattype_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Tjenesteresultattype_identifikator_literal, domain=Tjenesteresultattype, range=Optional[str])

slots.Tjenesteresultattype_er_beskrive_av = Slot(uri=CCCEVNO.isDescribedBy, name="Tjenesteresultattype_er_beskrive_av", curie=CCCEVNO.curie('isDescribedBy'),
                   model_uri=DEFAULT_.Tjenesteresultattype_er_beskrive_av, domain=Tjenesteresultattype, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Tjenesteresultattype_er_spesifisert_i = Slot(uri=CV.isSpecifiedIn, name="Tjenesteresultattype_er_spesifisert_i", curie=CV.curie('isSpecifiedIn'),
                   model_uri=DEFAULT_.Tjenesteresultattype_er_spesifisert_i, domain=Tjenesteresultattype, range=Optional[Union[str, URIorCURIE]])

slots.Tjenesteresultattype_kan_skape_hending = Slot(uri=XKOS.causes, name="Tjenesteresultattype_kan_skape_hending", curie=XKOS.curie('causes'),
                   model_uri=DEFAULT_.Tjenesteresultattype_kan_skape_hending, domain=Tjenesteresultattype, range=Optional[Union[Union[str, HendelseId], list[Union[str, HendelseId]]]])

slots.Tjenesteresultattype_type_concept = Slot(uri=DCT.type, name="Tjenesteresultattype_type_concept", curie=DCT.curie('type'),
                   model_uri=DEFAULT_.Tjenesteresultattype_type_concept, domain=Tjenesteresultattype, range=Optional[Union[str, KonseptId]])

slots.Gebyr_beskrivelse = Slot(uri=DCT.description, name="Gebyr_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.Gebyr_beskrivelse, domain=Gebyr, range=Optional[Union[str, list[str]]])

slots.Gebyr_identifikator_literal = Slot(uri=DCT.identifier, name="Gebyr_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Gebyr_identifikator_literal, domain=Gebyr, range=Optional[str])

slots.Gebyr_verdi = Slot(uri=CV.value, name="Gebyr_verdi", curie=CV.curie('value'),
                   model_uri=DEFAULT_.Gebyr_verdi, domain=Gebyr, range=Optional[float])

slots.Gebyr_valuta = Slot(uri=CV.currency, name="Gebyr_valuta", curie=CV.curie('currency'),
                   model_uri=DEFAULT_.Gebyr_valuta, domain=Gebyr, range=Optional[Union[str, KonseptId]])

slots.Regel_tittel = Slot(uri=DCT.title, name="Regel_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Regel_tittel, domain=Regel, range=Optional[Union[str, list[str]]])

slots.Regel_beskrivelse = Slot(uri=DCT.description, name="Regel_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.Regel_beskrivelse, domain=Regel, range=Optional[Union[str, list[str]]])

slots.Regel_identifikator_literal = Slot(uri=DCT.identifier, name="Regel_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Regel_identifikator_literal, domain=Regel, range=Optional[str])

slots.Regel_spraak = Slot(uri=DCT.language, name="Regel_spraak", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.Regel_spraak, domain=Regel, range=Optional[Union[str, list[str]]])

slots.Regel_type_concept = Slot(uri=DCT.type, name="Regel_type_concept", curie=DCT.curie('type'),
                   model_uri=DEFAULT_.Regel_type_concept, domain=Regel, range=Optional[Union[str, KonseptId]])

slots.RegulativRessurs_tittel = Slot(uri=DCT.title, name="RegulativRessurs_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.RegulativRessurs_tittel, domain=RegulativRessurs, range=Optional[Union[str, list[str]]])

slots.RegulativRessurs_identifikator_literal = Slot(uri=DCT.identifier, name="RegulativRessurs_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.RegulativRessurs_identifikator_literal, domain=RegulativRessurs, range=Optional[str])

slots.RegulativRessurs_type_concept = Slot(uri=DCT.type, name="RegulativRessurs_type_concept", curie=DCT.curie('type'),
                   model_uri=DEFAULT_.RegulativRessurs_type_concept, domain=RegulativRessurs, range=Optional[Union[str, KonseptId]])

slots.Deltagelse_har_rolle = Slot(uri=CV.role, name="Deltagelse_har_rolle", curie=CV.curie('role'),
                   model_uri=DEFAULT_.Deltagelse_har_rolle, domain=Deltagelse, range=Optional[Union[str, KonseptId]])

slots.Deltagelse_deltakar = Slot(uri=CV.participant, name="Deltagelse_deltakar", curie=CV.curie('participant'),
                   model_uri=DEFAULT_.Deltagelse_deltakar, domain=Deltagelse, range=Optional[Union[str, AktorId]])

slots.Adresse_full_adresse = Slot(uri=LOCN.fullAddress, name="Adresse_full_adresse", curie=LOCN.curie('fullAddress'),
                   model_uri=DEFAULT_.Adresse_full_adresse, domain=Adresse, range=Optional[Union[str, list[str]]])

slots.Adresse_postnummer = Slot(uri=LOCN.postCode, name="Adresse_postnummer", curie=LOCN.curie('postCode'),
                   model_uri=DEFAULT_.Adresse_postnummer, domain=Adresse, range=Optional[str])

slots.Adresse_poststad = Slot(uri=LOCN.postName, name="Adresse_poststad", curie=LOCN.curie('postName'),
                   model_uri=DEFAULT_.Adresse_poststad, domain=Adresse, range=Optional[Union[str, list[str]]])

slots.Adresse_land = Slot(uri=LOCN.adminUnitL1, name="Adresse_land", curie=LOCN.curie('adminUnitL1'),
                   model_uri=DEFAULT_.Adresse_land, domain=Adresse, range=Optional[str])

slots.Katalog_tittel = Slot(uri=DCT.title, name="Katalog_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Katalog_tittel, domain=Katalog, range=Union[str, list[str]])

slots.Katalog_beskrivelse = Slot(uri=DCT.description, name="Katalog_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.Katalog_beskrivelse, domain=Katalog, range=Union[str, list[str]])

slots.Katalog_identifikator_literal = Slot(uri=DCT.identifier, name="Katalog_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Katalog_identifikator_literal, domain=Katalog, range=str)

slots.Katalog_inneheld_teneste = Slot(uri=DCATNO.containsService, name="Katalog_inneheld_teneste", curie=DCATNO.curie('containsService'),
                   model_uri=DEFAULT_.Katalog_inneheld_teneste, domain=Katalog, range=Union[Union[str, OffentligTjenesteId], list[Union[str, OffentligTjenesteId]]])

slots.Katalog_har_kontaktpunkt = Slot(uri=CV.contactPoint, name="Katalog_har_kontaktpunkt", curie=CV.curie('contactPoint'),
                   model_uri=DEFAULT_.Katalog_har_kontaktpunkt, domain=Katalog, range=Union[Union[str, KontaktpunktId], list[Union[str, KontaktpunktId]]])

slots.Katalog_utgjevar = Slot(uri=DCT.publisher, name="Katalog_utgjevar", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.Katalog_utgjevar, domain=Katalog, range=Union[str, AktorId])

slots.Katalog_dekningsomraade = Slot(uri=DCT.spatial, name="Katalog_dekningsomraade", curie=DCT.curie('spatial'),
                   model_uri=DEFAULT_.Katalog_dekningsomraade, domain=Katalog, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Katalog_endringsdato = Slot(uri=DCT.modified, name="Katalog_endringsdato", curie=DCT.curie('modified'),
                   model_uri=DEFAULT_.Katalog_endringsdato, domain=Katalog, range=Optional[Union[str, XSDDate]])

slots.Katalog_oppdateringsfrekvens = Slot(uri=DCT.accrualPeriodicity, name="Katalog_oppdateringsfrekvens", curie=DCT.curie('accrualPeriodicity'),
                   model_uri=DEFAULT_.Katalog_oppdateringsfrekvens, domain=Katalog, range=Optional[Union[str, KonseptId]])

slots.Katalog_heimeside = Slot(uri=FOAF.homepage, name="Katalog_heimeside", curie=FOAF.curie('homepage'),
                   model_uri=DEFAULT_.Katalog_heimeside, domain=Katalog, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Katalog_inneheld_hending = Slot(uri=DCATNO.containsEvent, name="Katalog_inneheld_hending", curie=DCATNO.curie('containsEvent'),
                   model_uri=DEFAULT_.Katalog_inneheld_hending, domain=Katalog, range=Optional[Union[Union[str, HendelseId], list[Union[str, HendelseId]]]])

slots.Katalog_lisens = Slot(uri=DCT.license, name="Katalog_lisens", curie=DCT.curie('license'),
                   model_uri=DEFAULT_.Katalog_lisens, domain=Katalog, range=Optional[Union[str, URI]])

slots.Katalog_spraak = Slot(uri=DCT.language, name="Katalog_spraak", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.Katalog_spraak, domain=Katalog, range=Optional[Union[str, list[str]]])

