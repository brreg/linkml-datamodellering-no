# Auto generated from samt-bu-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-23T14:09:09
# Schema: skole_ontologi
#
# id: https://example.no/ontology/samt-bu-skole
# description: Ontodia-vennlig LinkML-modell for skoler
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

from linkml_runtime.linkml_model.types import Date, Datetime, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.11.0"
version = None

# Namespaces
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms#')
CAPNO = CurieNamespace('capno', 'https://data.norge.no/linkml/common-ap-no/')
CV = CurieNamespace('cv', 'http://data.europa.eu/m8g/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCATAP = CurieNamespace('dcatap', 'http://data.europa.eu/r5r/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DQV = CurieNamespace('dqv', 'http://www.w3.org/ns/dqv#')
DQVNO = CurieNamespace('dqvno', 'https://data.norge.no/vocabulary/dqvno#')
ELI = CurieNamespace('eli', 'http://data.europa.eu/eli/ontology#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OA = CurieNamespace('oa', 'http://www.w3.org/ns/oa#')
ODRL = CurieNamespace('odrl', 'http://www.w3.org/ns/odrl/2/')
ODRS = CurieNamespace('odrs', 'http://schema.theodi.org/odrs#')
ORG = CurieNamespace('org', 'http://www.w3.org/ns/org#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SAMTBUSKOLE = CurieNamespace('samtbuskole', 'https://example.no/ontology/skole#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SPDX = CurieNamespace('spdx', 'http://spdx.org/rdf/terms#')
TIME = CurieNamespace('time', 'http://www.w3.org/6006/time#')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = SAMTBUSKOLE


# Types
class Spraak(str):
    """ Språk """
    type_class_uri = DCT["language"]
    type_class_curie = "dct:language"
    type_name = "Spraak"
    type_model_uri = SAMTBUSKOLE.Spraak


class LangString(str):
    """ Språktagget streng (rdf:langString). """
    type_class_uri = RDF["langString"]
    type_class_curie = "rdf:langString"
    type_name = "LangString"
    type_model_uri = SAMTBUSKOLE.LangString


class NonNegativeInteger(int):
    """ Ikkje-negativ heltalsverdi (xsd:nonNegativeInteger). """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "NonNegativeInteger"
    type_model_uri = SAMTBUSKOLE.NonNegativeInteger


class Duration(str):
    """ ISO 8601-varigheit (xsd:duration), t.d. PT15M. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "Duration"
    type_model_uri = SAMTBUSKOLE.Duration


class GYear(str):
    """ Gregorisk årstal (xsd:gYear), t.d. 2024. """
    type_class_uri = XSD["gYear"]
    type_class_curie = "xsd:gYear"
    type_name = "GYear"
    type_model_uri = SAMTBUSKOLE.GYear


# Class references
class SkoleId(URIorCURIE):
    pass


class SkoleeierId(URIorCURIE):
    pass


class KommuneId(SkoleeierId):
    pass


class FylkeId(SkoleeierId):
    pass


class PrivatVirksomhetId(SkoleeierId):
    pass


class BasisgruppeId(URIorCURIE):
    pass


class PersonId(URIorCURIE):
    pass


class ElevId(PersonId):
    pass


class RektorId(PersonId):
    pass


class KontaktlaererId(PersonId):
    pass


class KatalogisertRessursId(URIorCURIE):
    pass


class AktorId(URIorCURIE):
    pass


class KontaktopplysningId(URIorCURIE):
    pass


class TidsromId(URIorCURIE):
    pass


class RegulativRessursId(URIorCURIE):
    pass


class IdentifikatorId(URIorCURIE):
    pass


class RettighetserklaringId(URIorCURIE):
    pass


class SjekksumId(URIorCURIE):
    pass


class GebyrId(URIorCURIE):
    pass


class RelasjonId(URIorCURIE):
    pass


class DistribusjonId(URIorCURIE):
    pass


class DatasettId(KatalogisertRessursId):
    pass


class DatasettserieId(KatalogisertRessursId):
    pass


class DatatjenesteId(KatalogisertRessursId):
    pass


class KatalogpostId(URIorCURIE):
    pass


class KatalogId(KatalogisertRessursId):
    pass


class KvalitetsdimensjonId(URIorCURIE):
    pass


class KvalitetsdeldimensjonId(KvalitetsdimensjonId):
    pass


class KvalitetsmaalId(URIorCURIE):
    pass


class KvalitetsmerknadId(URIorCURIE):
    pass


class BrukartilbakemeldingId(KvalitetsmerknadId):
    pass


class KvalitetssertifikatId(KvalitetsmerknadId):
    pass


class KvalitetsmaalingId(URIorCURIE):
    pass


class StandardId(URIorCURIE):
    pass


class TekstdelId(URIorCURIE):
    pass


class MediatypeId(URIorCURIE):
    pass


class KonseptId(URIorCURIE):
    pass


class BegrepssamlingId(URIorCURIE):
    pass


@dataclass(repr=False)
class SamtBuContainer(YAMLRoot):
    """
    Containerklasse for alle klasser som kan inngå i datasettet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMTBUSKOLE["SamtBuContainer"]
    class_class_curie: ClassVar[str] = "samtbuskole:SamtBuContainer"
    class_name: ClassVar[str] = "SamtBuContainer"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.SamtBuContainer

    kontaktpunkter: Optional[Union[dict[Union[str, KontaktopplysningId], Union[dict, "Kontaktopplysning"]], list[Union[dict, "Kontaktopplysning"]]]] = empty_dict()
    utgivere: Optional[Union[dict[Union[str, AktorId], Union[dict, "Aktor"]], list[Union[dict, "Aktor"]]]] = empty_dict()
    organisasjoner: Optional[Union[dict[Union[str, AktorId], Union[dict, "Aktor"]], list[Union[dict, "Aktor"]]]] = empty_dict()
    gjeldende_lovgivninger: Optional[Union[dict[Union[str, RegulativRessursId], Union[dict, "RegulativRessurs"]], list[Union[dict, "RegulativRessurs"]]]] = empty_dict()
    datasettdistribusjoner: Optional[Union[dict[Union[str, DistribusjonId], Union[dict, "Distribusjon"]], list[Union[dict, "Distribusjon"]]]] = empty_dict()
    dataset_metadata: Optional[Union[dict[Union[str, DatasettId], Union[dict, "Datasett"]], list[Union[dict, "Datasett"]]]] = empty_dict()
    kvalitetsmerknader: Optional[Union[dict[Union[str, KvalitetsmerknadId], Union[dict, "Kvalitetsmerknad"]], list[Union[dict, "Kvalitetsmerknad"]]]] = empty_dict()
    brukertilbakemeldinger: Optional[Union[dict[Union[str, BrukartilbakemeldingId], Union[dict, "Brukartilbakemelding"]], list[Union[dict, "Brukartilbakemelding"]]]] = empty_dict()
    kvalitetsmaalinger: Optional[Union[dict[Union[str, KvalitetsmaalingId], Union[dict, "Kvalitetsmaaling"]], list[Union[dict, "Kvalitetsmaaling"]]]] = empty_dict()
    grupper: Optional[Union[dict[Union[str, AktorId], Union[dict, "Aktor"]], list[Union[dict, "Aktor"]]]] = empty_dict()
    standarder: Optional[Union[dict[Union[str, StandardId], Union[dict, "Standard"]], list[Union[dict, "Standard"]]]] = empty_dict()
    kvalitetsdimensjoner: Optional[Union[dict[Union[str, KvalitetsdimensjonId], Union[dict, "Kvalitetsdimensjon"]], list[Union[dict, "Kvalitetsdimensjon"]]]] = empty_dict()
    tidsromer: Optional[Union[dict[Union[str, TidsromId], Union[dict, "Tidsrom"]], list[Union[dict, "Tidsrom"]]]] = empty_dict()
    tekstdeler: Optional[Union[dict[Union[str, TekstdelId], Union[dict, "Tekstdel"]], list[Union[dict, "Tekstdel"]]]] = empty_dict()
    id: Optional[str] = None
    skoler: Optional[Union[dict[Union[str, SkoleId], Union[dict, "Skole"]], list[Union[dict, "Skole"]]]] = empty_dict()
    kommuner: Optional[Union[dict[Union[str, KommuneId], Union[dict, "Kommune"]], list[Union[dict, "Kommune"]]]] = empty_dict()
    fylker: Optional[Union[dict[Union[str, FylkeId], Union[dict, "Fylke"]], list[Union[dict, "Fylke"]]]] = empty_dict()
    private_virksomheter: Optional[Union[dict[Union[str, PrivatVirksomhetId], Union[dict, "PrivatVirksomhet"]], list[Union[dict, "PrivatVirksomhet"]]]] = empty_dict()
    basisgrupper: Optional[Union[dict[Union[str, BasisgruppeId], Union[dict, "Basisgruppe"]], list[Union[dict, "Basisgruppe"]]]] = empty_dict()
    elever: Optional[Union[dict[Union[str, ElevId], Union[dict, "Elev"]], list[Union[dict, "Elev"]]]] = empty_dict()
    rektorer: Optional[Union[dict[Union[str, RektorId], Union[dict, "Rektor"]], list[Union[dict, "Rektor"]]]] = empty_dict()
    kontaktlaerere: Optional[Union[dict[Union[str, KontaktlaererId], Union[dict, "Kontaktlaerer"]], list[Union[dict, "Kontaktlaerer"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="kontaktpunkter", slot_type=Kontaktopplysning, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="utgivere", slot_type=Aktor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="organisasjoner", slot_type=Aktor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="gjeldende_lovgivninger", slot_type=RegulativRessurs, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="datasettdistribusjoner", slot_type=Distribusjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dataset_metadata", slot_type=Datasett, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kvalitetsmerknader", slot_type=Kvalitetsmerknad, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="brukertilbakemeldinger", slot_type=Brukartilbakemelding, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kvalitetsmaalinger", slot_type=Kvalitetsmaaling, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="grupper", slot_type=Aktor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="standarder", slot_type=Standard, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kvalitetsdimensjoner", slot_type=Kvalitetsdimensjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tidsromer", slot_type=Tidsrom, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tekstdeler", slot_type=Tekstdel, key_name="id", keyed=True)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        self._normalize_inlined_as_list(slot_name="skoler", slot_type=Skole, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kommuner", slot_type=Kommune, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fylker", slot_type=Fylke, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="private_virksomheter", slot_type=PrivatVirksomhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="basisgrupper", slot_type=Basisgruppe, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="elever", slot_type=Elev, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rektorer", slot_type=Rektor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kontaktlaerere", slot_type=Kontaktlaerer, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Skole(YAMLRoot):
    """
    En skole er en privat eller offentlig institusjon eller et lærested hvor lærere underviser i ulike fag, oftest som
    grunnlag for videre utdannelse og yrkesliv.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMTBUSKOLE["Skole"]
    class_class_curie: ClassVar[str] = "samtbuskole:Skole"
    class_name: ClassVar[str] = "Skole"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Skole

    id: Union[str, SkoleId] = None
    navn: Optional[str] = None
    har_skoleeier: Optional[Union[str, SkoleeierId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SkoleId):
            self.id = SkoleId(self.id)

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.har_skoleeier is not None and not isinstance(self.har_skoleeier, SkoleeierId):
            self.har_skoleeier = SkoleeierId(self.har_skoleeier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Skoleeier(YAMLRoot):
    """
    Superklasse for alle typer skoleeiere.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMTBUSKOLE["Skoleeier"]
    class_class_curie: ClassVar[str] = "samtbuskole:Skoleeier"
    class_name: ClassVar[str] = "Skoleeier"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Skoleeier

    id: Union[str, SkoleeierId] = None
    navn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SkoleeierId):
            self.id = SkoleeierId(self.id)

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kommune(Skoleeier):
    """
    En kommune er et geografisk avgrenset område som utgjør en egen politisk og administrativ enhet innen en
    statsdannelse.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMTBUSKOLE["Kommune"]
    class_class_curie: ClassVar[str] = "samtbuskole:Kommune"
    class_name: ClassVar[str] = "Kommune"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Kommune

    id: Union[str, KommuneId] = None
    kommunenummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KommuneId):
            self.id = KommuneId(self.id)

        if self.kommunenummer is not None and not isinstance(self.kommunenummer, str):
            self.kommunenummer = str(self.kommunenummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fylke(Skoleeier):
    """
    Fylke (etter norrønt fylki) er en betegnelse på et undernasjonalt, regionalt geografisk område, tilsvarende amt og
    len.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMTBUSKOLE["Fylke"]
    class_class_curie: ClassVar[str] = "samtbuskole:Fylke"
    class_name: ClassVar[str] = "Fylke"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Fylke

    id: Union[str, FylkeId] = None
    fylkesnummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FylkeId):
            self.id = FylkeId(self.id)

        if self.fylkesnummer is not None and not isinstance(self.fylkesnummer, str):
            self.fylkesnummer = str(self.fylkesnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivatVirksomhet(Skoleeier):
    """
    Virksomhet, eller foretak, er betegnelser for en juridisk person eller en organisasjon som produserer varer eller
    tjenester.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMTBUSKOLE["PrivatVirksomhet"]
    class_class_curie: ClassVar[str] = "samtbuskole:PrivatVirksomhet"
    class_name: ClassVar[str] = "PrivatVirksomhet"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.PrivatVirksomhet

    id: Union[str, PrivatVirksomhetId] = None
    organisasjonsnummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivatVirksomhetId):
            self.id = PrivatVirksomhetId(self.id)

        if self.organisasjonsnummer is not None and not isinstance(self.organisasjonsnummer, str):
            self.organisasjonsnummer = str(self.organisasjonsnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Basisgruppe(YAMLRoot):
    """
    Skoleklasse som hovedsaklig samler elever i ulike fag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMTBUSKOLE["Basisgruppe"]
    class_class_curie: ClassVar[str] = "samtbuskole:Basisgruppe"
    class_name: ClassVar[str] = "Basisgruppe"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Basisgruppe

    id: Union[str, BasisgruppeId] = None
    navn: Optional[str] = None
    trinniva: Optional[str] = None
    del_av_skole: Optional[Union[str, SkoleId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BasisgruppeId):
            self.id = BasisgruppeId(self.id)

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.trinniva is not None and not isinstance(self.trinniva, str):
            self.trinniva = str(self.trinniva)

        if self.del_av_skole is not None and not isinstance(self.del_av_skole, SkoleId):
            self.del_av_skole = SkoleId(self.del_av_skole)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    """
    Eit menneske individ
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMTBUSKOLE["Person"]
    class_class_curie: ClassVar[str] = "samtbuskole:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Person

    id: Union[str, PersonId] = None
    navn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Elev(Person):
    """
    En person som går på skole
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMTBUSKOLE["Elev"]
    class_class_curie: ClassVar[str] = "samtbuskole:Elev"
    class_name: ClassVar[str] = "Elev"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Elev

    id: Union[str, ElevId] = None
    horer_til_basisgruppe: Optional[Union[str, BasisgruppeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElevId):
            self.id = ElevId(self.id)

        if self.horer_til_basisgruppe is not None and not isinstance(self.horer_til_basisgruppe, BasisgruppeId):
            self.horer_til_basisgruppe = BasisgruppeId(self.horer_til_basisgruppe)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rektor(Person):
    """
    Høgaste akademiske leder av en skole
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMTBUSKOLE["Rektor"]
    class_class_curie: ClassVar[str] = "samtbuskole:Rektor"
    class_name: ClassVar[str] = "Rektor"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Rektor

    id: Union[str, RektorId] = None
    enhetsleder_for: Optional[Union[str, SkoleId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RektorId):
            self.id = RektorId(self.id)

        if self.enhetsleder_for is not None and not isinstance(self.enhetsleder_for, SkoleId):
            self.enhetsleder_for = SkoleId(self.enhetsleder_for)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontaktlaerer(Person):
    """
    En lærer med ansvar for ei basisgruppe og er skolens kontaktpunkt for elevane i basisgruppa
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMTBUSKOLE["Kontaktlaerer"]
    class_class_curie: ClassVar[str] = "samtbuskole:Kontaktlaerer"
    class_name: ClassVar[str] = "Kontaktlaerer"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Kontaktlaerer

    id: Union[str, KontaktlaererId] = None
    tilknyttet_basisgruppe: Optional[Union[str, BasisgruppeId]] = None
    har_saerlig_ansvar_for: Optional[Union[str, ElevId]] = None
    jobber_paa_skole: Optional[Union[str, SkoleId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KontaktlaererId):
            self.id = KontaktlaererId(self.id)

        if self.tilknyttet_basisgruppe is not None and not isinstance(self.tilknyttet_basisgruppe, BasisgruppeId):
            self.tilknyttet_basisgruppe = BasisgruppeId(self.tilknyttet_basisgruppe)

        if self.har_saerlig_ansvar_for is not None and not isinstance(self.har_saerlig_ansvar_for, ElevId):
            self.har_saerlig_ansvar_for = ElevId(self.har_saerlig_ansvar_for)

        if self.jobber_paa_skole is not None and not isinstance(self.jobber_paa_skole, SkoleId):
            self.jobber_paa_skole = SkoleId(self.jobber_paa_skole)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KatalogisertRessurs(YAMLRoot):
    """
    Basisklasse for ressursar som kan katalogiserast.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Resource"]
    class_class_curie: ClassVar[str] = "dcat:Resource"
    class_name: ClassVar[str] = "KatalogisertRessurs"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.KatalogisertRessurs

    id: Union[str, KatalogisertRessursId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KatalogisertRessursId):
            self.id = KatalogisertRessursId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aktor(YAMLRoot):
    """
    Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Agent"]
    class_class_curie: ClassVar[str] = "foaf:Agent"
    class_name: ClassVar[str] = "Aktor"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Aktor

    id: Union[str, AktorId] = None
    navn_aktor: Union[str, list[str]] = None
    identifikator_literal: Optional[str] = None
    type_concept: Optional[Union[str, KonseptId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AktorId):
            self.id = AktorId(self.id)

        if self._is_empty(self.navn_aktor):
            self.MissingRequiredField("navn_aktor")
        if not isinstance(self.navn_aktor, list):
            self.navn_aktor = [self.navn_aktor] if self.navn_aktor is not None else []
        self.navn_aktor = [v if isinstance(v, str) else str(v) for v in self.navn_aktor]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontaktopplysning(YAMLRoot):
    """
    Kontaktinformasjon for ein aktør.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VCARD["Kind"]
    class_class_curie: ClassVar[str] = "vcard:Kind"
    class_name: ClassVar[str] = "Kontaktopplysning"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Kontaktopplysning

    id: Union[str, KontaktopplysningId] = None
    navn_vcard: Union[str, list[str]] = None
    har_epost: Optional[str] = None
    har_kontaktside: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KontaktopplysningId):
            self.id = KontaktopplysningId(self.id)

        if self._is_empty(self.navn_vcard):
            self.MissingRequiredField("navn_vcard")
        if not isinstance(self.navn_vcard, list):
            self.navn_vcard = [self.navn_vcard] if self.navn_vcard is not None else []
        self.navn_vcard = [v if isinstance(v, str) else str(v) for v in self.navn_vcard]

        if self.har_epost is not None and not isinstance(self.har_epost, str):
            self.har_epost = str(self.har_epost)

        if self.har_kontaktside is not None and not isinstance(self.har_kontaktside, str):
            self.har_kontaktside = str(self.har_kontaktside)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tidsrom(YAMLRoot):
    """
    Eit tidsintervall med start- og sluttdato.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["PeriodOfTime"]
    class_class_curie: ClassVar[str] = "dct:PeriodOfTime"
    class_name: ClassVar[str] = "Tidsrom"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Tidsrom

    id: Union[str, TidsromId] = None
    startdato: Optional[Union[str, XSDDate]] = None
    sluttdato: Optional[Union[str, XSDDate]] = None
    begynnelse: Optional[Union[str, XSDDateTime]] = None
    slutt: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TidsromId):
            self.id = TidsromId(self.id)

        if self.startdato is not None and not isinstance(self.startdato, XSDDate):
            self.startdato = XSDDate(self.startdato)

        if self.sluttdato is not None and not isinstance(self.sluttdato, XSDDate):
            self.sluttdato = XSDDate(self.sluttdato)

        if self.begynnelse is not None and not isinstance(self.begynnelse, XSDDateTime):
            self.begynnelse = XSDDateTime(self.begynnelse)

        if self.slutt is not None and not isinstance(self.slutt, XSDDateTime):
            self.slutt = XSDDateTime(self.slutt)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RegulativRessurs(YAMLRoot):
    """
    Ein regulativ ressurs (lov, forskrift o.l.) som gjeld for ein ressurs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ELI["LegalResource"]
    class_class_curie: ClassVar[str] = "eli:LegalResource"
    class_name: ClassVar[str] = "RegulativRessurs"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.RegulativRessurs

    id: Union[str, RegulativRessursId] = None
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()
    identifikator_literal: Optional[str] = None
    har_referanse: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    spraak: Optional[Union[str, list[str]]] = empty_list()
    tittel: Optional[Union[str, list[str]]] = empty_list()
    type_concept: Optional[Union[str, KonseptId]] = None
    relatert_regulativ_ressurs: Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegulativRessursId):
            self.id = RegulativRessursId(self.id)

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if not isinstance(self.har_referanse, list):
            self.har_referanse = [self.har_referanse] if self.har_referanse is not None else []
        self.har_referanse = [v if isinstance(v, URI) else URI(v) for v in self.har_referanse]

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        if not isinstance(self.relatert_regulativ_ressurs, list):
            self.relatert_regulativ_ressurs = [self.relatert_regulativ_ressurs] if self.relatert_regulativ_ressurs is not None else []
        self.relatert_regulativ_ressurs = [v if isinstance(v, RegulativRessursId) else RegulativRessursId(v) for v in self.relatert_regulativ_ressurs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Identifikator(YAMLRoot):
    """
    Ein alternativ identifikator for ein ressurs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADMS["Identifier"]
    class_class_curie: ClassVar[str] = "adms:Identifier"
    class_name: ClassVar[str] = "Identifikator"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Identifikator

    id: Union[str, IdentifikatorId] = None
    notasjon: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentifikatorId):
            self.id = IdentifikatorId(self.id)

        if self._is_empty(self.notasjon):
            self.MissingRequiredField("notasjon")
        if not isinstance(self.notasjon, str):
            self.notasjon = str(self.notasjon)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rettighetserklaring(YAMLRoot):
    """
    Ei erklæring om rettar til ein ressurs (ODRS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["RightsStatement"]
    class_class_curie: ClassVar[str] = "dct:RightsStatement"
    class_name: ClassVar[str] = "Rettighetserklaring"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Rettighetserklaring

    id: Union[str, RettighetserklaringId] = None
    anvendelsesretningslinjer: Optional[str] = None
    jurisdiksjon: Optional[str] = None
    krediteringstekst: Optional[str] = None
    krediteringsurl: Optional[Union[str, URI]] = None
    opphavsrettserklaring: Optional[str] = None
    opphavsrettsinnehaver: Optional[str] = None
    opphavsrettsnotis: Optional[str] = None
    opphavsrettsaar: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RettighetserklaringId):
            self.id = RettighetserklaringId(self.id)

        if self.anvendelsesretningslinjer is not None and not isinstance(self.anvendelsesretningslinjer, str):
            self.anvendelsesretningslinjer = str(self.anvendelsesretningslinjer)

        if self.jurisdiksjon is not None and not isinstance(self.jurisdiksjon, str):
            self.jurisdiksjon = str(self.jurisdiksjon)

        if self.krediteringstekst is not None and not isinstance(self.krediteringstekst, str):
            self.krediteringstekst = str(self.krediteringstekst)

        if self.krediteringsurl is not None and not isinstance(self.krediteringsurl, URI):
            self.krediteringsurl = URI(self.krediteringsurl)

        if self.opphavsrettserklaring is not None and not isinstance(self.opphavsrettserklaring, str):
            self.opphavsrettserklaring = str(self.opphavsrettserklaring)

        if self.opphavsrettsinnehaver is not None and not isinstance(self.opphavsrettsinnehaver, str):
            self.opphavsrettsinnehaver = str(self.opphavsrettsinnehaver)

        if self.opphavsrettsnotis is not None and not isinstance(self.opphavsrettsnotis, str):
            self.opphavsrettsnotis = str(self.opphavsrettsnotis)

        if self.opphavsrettsaar is not None and not isinstance(self.opphavsrettsaar, str):
            self.opphavsrettsaar = str(self.opphavsrettsaar)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sjekksum(YAMLRoot):
    """
    Ein sjekksum for ein distribusjon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX["Checksum"]
    class_class_curie: ClassVar[str] = "spdx:Checksum"
    class_name: ClassVar[str] = "Sjekksum"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Sjekksum

    id: Union[str, SjekksumId] = None
    algoritme: str = None
    sjekksumverdi: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SjekksumId):
            self.id = SjekksumId(self.id)

        if self._is_empty(self.algoritme):
            self.MissingRequiredField("algoritme")
        if not isinstance(self.algoritme, str):
            self.algoritme = str(self.algoritme)

        if self._is_empty(self.sjekksumverdi):
            self.MissingRequiredField("sjekksumverdi")
        if not isinstance(self.sjekksumverdi, str):
            self.sjekksumverdi = str(self.sjekksumverdi)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Gebyr(YAMLRoot):
    """
    Eit gebyr knytt til bruk av ein datatjeneste.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CV["Cost"]
    class_class_curie: ClassVar[str] = "cv:Cost"
    class_name: ClassVar[str] = "Gebyr"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Gebyr

    id: Union[str, GebyrId] = None
    belop: Optional[str] = None
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()
    dokumentasjon: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    valuta: Optional[Union[str, KonseptId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GebyrId):
            self.id = GebyrId(self.id)

        if self.belop is not None and not isinstance(self.belop, str):
            self.belop = str(self.belop)

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if not isinstance(self.dokumentasjon, list):
            self.dokumentasjon = [self.dokumentasjon] if self.dokumentasjon is not None else []
        self.dokumentasjon = [v if isinstance(v, URI) else URI(v) for v in self.dokumentasjon]

        if self.valuta is not None and not isinstance(self.valuta, KonseptId):
            self.valuta = KonseptId(self.valuta)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relasjon(YAMLRoot):
    """
    Ein kvalifisert relasjon mellom to ressursar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Relationship"]
    class_class_curie: ClassVar[str] = "dcat:Relationship"
    class_name: ClassVar[str] = "Relasjon"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Relasjon

    id: Union[str, RelasjonId] = None
    har_rolle: str = None
    relasjon_til: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelasjonId):
            self.id = RelasjonId(self.id)

        if self._is_empty(self.har_rolle):
            self.MissingRequiredField("har_rolle")
        if not isinstance(self.har_rolle, str):
            self.har_rolle = str(self.har_rolle)

        if self._is_empty(self.relasjon_til):
            self.MissingRequiredField("relasjon_til")
        if not isinstance(self.relasjon_til, URI):
            self.relasjon_til = URI(self.relasjon_til)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Distribusjon(YAMLRoot):
    """
    Ein spesifikk representasjon/nedlastbar form av eit datasett.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Distribution"]
    class_class_curie: ClassVar[str] = "dcat:Distribution"
    class_name: ClassVar[str] = "Distribusjon"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Distribusjon

    id: Union[str, DistribusjonId] = None
    tilgangs_url: Union[Union[str, URI], list[Union[str, URI]]] = None
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()
    format: Optional[str] = None
    lisens: Optional[str] = None
    status: Optional[Union[str, KonseptId]] = None
    tilgjengelighet: Optional[str] = None
    dokumentasjon: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    endringsdato: Optional[Union[str, XSDDate]] = None
    filstorrelse: Optional[int] = None
    gjeldende_lovgivning: Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]] = empty_list()
    i_samsvar_med: Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]] = empty_list()
    komprimeringsformat: Optional[Union[str, MediatypeId]] = None
    medietype: Optional[Union[str, MediatypeId]] = None
    nedlastningslenke: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    pakkeformat: Optional[Union[str, MediatypeId]] = None
    policy: Optional[str] = None
    rettigheter: Optional[Union[str, RettighetserklaringId]] = None
    sjekksum: Optional[Union[str, SjekksumId]] = None
    spraak: Optional[Union[str, list[str]]] = empty_list()
    tidsopplosning: Optional[str] = None
    tilgangstjeneste: Optional[Union[Union[str, DatatjenesteId], list[Union[str, DatatjenesteId]]]] = empty_list()
    tittel: Optional[Union[str, list[str]]] = empty_list()
    utgivelsesdato: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DistribusjonId):
            self.id = DistribusjonId(self.id)

        if self._is_empty(self.tilgangs_url):
            self.MissingRequiredField("tilgangs_url")
        if not isinstance(self.tilgangs_url, list):
            self.tilgangs_url = [self.tilgangs_url] if self.tilgangs_url is not None else []
        self.tilgangs_url = [v if isinstance(v, URI) else URI(v) for v in self.tilgangs_url]

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.lisens is not None and not isinstance(self.lisens, str):
            self.lisens = str(self.lisens)

        if self.status is not None and not isinstance(self.status, KonseptId):
            self.status = KonseptId(self.status)

        if self.tilgjengelighet is not None and not isinstance(self.tilgjengelighet, str):
            self.tilgjengelighet = str(self.tilgjengelighet)

        if not isinstance(self.dokumentasjon, list):
            self.dokumentasjon = [self.dokumentasjon] if self.dokumentasjon is not None else []
        self.dokumentasjon = [v if isinstance(v, URI) else URI(v) for v in self.dokumentasjon]

        if self.endringsdato is not None and not isinstance(self.endringsdato, XSDDate):
            self.endringsdato = XSDDate(self.endringsdato)

        if self.filstorrelse is not None and not isinstance(self.filstorrelse, int):
            self.filstorrelse = int(self.filstorrelse)

        if not isinstance(self.gjeldende_lovgivning, list):
            self.gjeldende_lovgivning = [self.gjeldende_lovgivning] if self.gjeldende_lovgivning is not None else []
        self.gjeldende_lovgivning = [v if isinstance(v, RegulativRessursId) else RegulativRessursId(v) for v in self.gjeldende_lovgivning]

        if not isinstance(self.i_samsvar_med, list):
            self.i_samsvar_med = [self.i_samsvar_med] if self.i_samsvar_med is not None else []
        self.i_samsvar_med = [v if isinstance(v, StandardId) else StandardId(v) for v in self.i_samsvar_med]

        if self.komprimeringsformat is not None and not isinstance(self.komprimeringsformat, MediatypeId):
            self.komprimeringsformat = MediatypeId(self.komprimeringsformat)

        if self.medietype is not None and not isinstance(self.medietype, MediatypeId):
            self.medietype = MediatypeId(self.medietype)

        if not isinstance(self.nedlastningslenke, list):
            self.nedlastningslenke = [self.nedlastningslenke] if self.nedlastningslenke is not None else []
        self.nedlastningslenke = [v if isinstance(v, URI) else URI(v) for v in self.nedlastningslenke]

        if self.pakkeformat is not None and not isinstance(self.pakkeformat, MediatypeId):
            self.pakkeformat = MediatypeId(self.pakkeformat)

        if self.policy is not None and not isinstance(self.policy, str):
            self.policy = str(self.policy)

        if self.rettigheter is not None and not isinstance(self.rettigheter, RettighetserklaringId):
            self.rettigheter = RettighetserklaringId(self.rettigheter)

        if self.sjekksum is not None and not isinstance(self.sjekksum, SjekksumId):
            self.sjekksum = SjekksumId(self.sjekksum)

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

        if self.tidsopplosning is not None and not isinstance(self.tidsopplosning, str):
            self.tidsopplosning = str(self.tidsopplosning)

        if not isinstance(self.tilgangstjeneste, list):
            self.tilgangstjeneste = [self.tilgangstjeneste] if self.tilgangstjeneste is not None else []
        self.tilgangstjeneste = [v if isinstance(v, DatatjenesteId) else DatatjenesteId(v) for v in self.tilgangstjeneste]

        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self.utgivelsesdato is not None and not isinstance(self.utgivelsesdato, XSDDate):
            self.utgivelsesdato = XSDDate(self.utgivelsesdato)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Datasett(KatalogisertRessurs):
    """
    Ei samling av data utgjeven eller kuratert av éin aktør.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "Datasett"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Datasett

    id: Union[str, DatasettId] = None
    beskrivelse: Union[str, list[str]] = None
    kontaktpunkt: Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]] = None
    tema: Union[str, list[str]] = None
    tittel: Union[str, list[str]] = None
    utgiver: Union[str, AktorId] = None
    begrep: Optional[Union[str, list[str]]] = empty_list()
    ble_generert_ved: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    datasettdistribusjon: Optional[Union[Union[str, DistribusjonId], list[Union[str, DistribusjonId]]]] = empty_list()
    dekningsomraade: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    gjeldende_lovgivning: Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]] = empty_list()
    nokkelord: Optional[Union[str, list[str]]] = empty_list()
    tidsrom: Optional[Union[Union[str, TidsromId], list[Union[str, TidsromId]]]] = empty_list()
    tilgangsrettigheter: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    annen_ansvarlig_aktor: Optional[Union[str, list[str]]] = empty_list()
    annen_identifikator: Optional[Union[Union[str, IdentifikatorId], list[Union[str, IdentifikatorId]]]] = empty_list()
    annen_spesifikk_relasjon: Optional[Union[Union[str, RelasjonId], list[Union[str, RelasjonId]]]] = empty_list()
    dokumentasjon: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    eierskapshistorikk: Optional[Union[str, list[str]]] = empty_list()
    eksempeldata: Optional[Union[Union[str, DistribusjonId], list[Union[str, DistribusjonId]]]] = empty_list()
    endringsdato: Optional[Union[str, XSDDate]] = None
    identifikator_literal: Optional[str] = None
    i_samsvar_med: Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]] = empty_list()
    i_serie: Optional[Union[Union[str, DatasettserieId], list[Union[str, DatasettserieId]]]] = empty_list()
    kilde_datasett: Optional[Union[Union[str, DatasettId], list[Union[str, DatasettId]]]] = empty_list()
    landingsside: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    produsent: Optional[Union[str, AktorId]] = None
    relatert_ressurs: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    spraak: Optional[Union[str, list[str]]] = empty_list()
    type_concept: Optional[Union[str, KonseptId]] = None
    utgivelsesdato: Optional[Union[str, XSDDate]] = None
    versjon: Optional[str] = None
    versjonsmerknad: Optional[Union[str, list[str]]] = empty_list()
    har_kvalitetsmerknad: Optional[Union[Union[str, KvalitetsmerknadId], list[Union[str, KvalitetsmerknadId]]]] = empty_list()
    har_kvalitetsmaaling: Optional[Union[Union[str, KvalitetsmaalingId], list[Union[str, KvalitetsmaalingId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasettId):
            self.id = DatasettId(self.id)

        if self._is_empty(self.beskrivelse):
            self.MissingRequiredField("beskrivelse")
        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self._is_empty(self.kontaktpunkt):
            self.MissingRequiredField("kontaktpunkt")
        if not isinstance(self.kontaktpunkt, list):
            self.kontaktpunkt = [self.kontaktpunkt] if self.kontaktpunkt is not None else []
        self.kontaktpunkt = [v if isinstance(v, KontaktopplysningId) else KontaktopplysningId(v) for v in self.kontaktpunkt]

        if self._is_empty(self.tema):
            self.MissingRequiredField("tema")
        if not isinstance(self.tema, list):
            self.tema = [self.tema] if self.tema is not None else []
        self.tema = [v if isinstance(v, str) else str(v) for v in self.tema]

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.utgiver):
            self.MissingRequiredField("utgiver")
        if not isinstance(self.utgiver, AktorId):
            self.utgiver = AktorId(self.utgiver)

        if not isinstance(self.begrep, list):
            self.begrep = [self.begrep] if self.begrep is not None else []
        self.begrep = [v if isinstance(v, str) else str(v) for v in self.begrep]

        if not isinstance(self.ble_generert_ved, list):
            self.ble_generert_ved = [self.ble_generert_ved] if self.ble_generert_ved is not None else []
        self.ble_generert_ved = [v if isinstance(v, URI) else URI(v) for v in self.ble_generert_ved]

        if not isinstance(self.datasettdistribusjon, list):
            self.datasettdistribusjon = [self.datasettdistribusjon] if self.datasettdistribusjon is not None else []
        self.datasettdistribusjon = [v if isinstance(v, DistribusjonId) else DistribusjonId(v) for v in self.datasettdistribusjon]

        if not isinstance(self.dekningsomraade, list):
            self.dekningsomraade = [self.dekningsomraade] if self.dekningsomraade is not None else []
        self.dekningsomraade = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.dekningsomraade]

        if not isinstance(self.gjeldende_lovgivning, list):
            self.gjeldende_lovgivning = [self.gjeldende_lovgivning] if self.gjeldende_lovgivning is not None else []
        self.gjeldende_lovgivning = [v if isinstance(v, RegulativRessursId) else RegulativRessursId(v) for v in self.gjeldende_lovgivning]

        if not isinstance(self.nokkelord, list):
            self.nokkelord = [self.nokkelord] if self.nokkelord is not None else []
        self.nokkelord = [v if isinstance(v, str) else str(v) for v in self.nokkelord]

        if not isinstance(self.tidsrom, list):
            self.tidsrom = [self.tidsrom] if self.tidsrom is not None else []
        self.tidsrom = [v if isinstance(v, TidsromId) else TidsromId(v) for v in self.tidsrom]

        if not isinstance(self.tilgangsrettigheter, list):
            self.tilgangsrettigheter = [self.tilgangsrettigheter] if self.tilgangsrettigheter is not None else []
        self.tilgangsrettigheter = [v if isinstance(v, URI) else URI(v) for v in self.tilgangsrettigheter]

        if not isinstance(self.annen_ansvarlig_aktor, list):
            self.annen_ansvarlig_aktor = [self.annen_ansvarlig_aktor] if self.annen_ansvarlig_aktor is not None else []
        self.annen_ansvarlig_aktor = [v if isinstance(v, str) else str(v) for v in self.annen_ansvarlig_aktor]

        if not isinstance(self.annen_identifikator, list):
            self.annen_identifikator = [self.annen_identifikator] if self.annen_identifikator is not None else []
        self.annen_identifikator = [v if isinstance(v, IdentifikatorId) else IdentifikatorId(v) for v in self.annen_identifikator]

        if not isinstance(self.annen_spesifikk_relasjon, list):
            self.annen_spesifikk_relasjon = [self.annen_spesifikk_relasjon] if self.annen_spesifikk_relasjon is not None else []
        self.annen_spesifikk_relasjon = [v if isinstance(v, RelasjonId) else RelasjonId(v) for v in self.annen_spesifikk_relasjon]

        if not isinstance(self.dokumentasjon, list):
            self.dokumentasjon = [self.dokumentasjon] if self.dokumentasjon is not None else []
        self.dokumentasjon = [v if isinstance(v, URI) else URI(v) for v in self.dokumentasjon]

        if not isinstance(self.eierskapshistorikk, list):
            self.eierskapshistorikk = [self.eierskapshistorikk] if self.eierskapshistorikk is not None else []
        self.eierskapshistorikk = [v if isinstance(v, str) else str(v) for v in self.eierskapshistorikk]

        if not isinstance(self.eksempeldata, list):
            self.eksempeldata = [self.eksempeldata] if self.eksempeldata is not None else []
        self.eksempeldata = [v if isinstance(v, DistribusjonId) else DistribusjonId(v) for v in self.eksempeldata]

        if self.endringsdato is not None and not isinstance(self.endringsdato, XSDDate):
            self.endringsdato = XSDDate(self.endringsdato)

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if not isinstance(self.i_samsvar_med, list):
            self.i_samsvar_med = [self.i_samsvar_med] if self.i_samsvar_med is not None else []
        self.i_samsvar_med = [v if isinstance(v, StandardId) else StandardId(v) for v in self.i_samsvar_med]

        if not isinstance(self.i_serie, list):
            self.i_serie = [self.i_serie] if self.i_serie is not None else []
        self.i_serie = [v if isinstance(v, DatasettserieId) else DatasettserieId(v) for v in self.i_serie]

        if not isinstance(self.kilde_datasett, list):
            self.kilde_datasett = [self.kilde_datasett] if self.kilde_datasett is not None else []
        self.kilde_datasett = [v if isinstance(v, DatasettId) else DatasettId(v) for v in self.kilde_datasett]

        if not isinstance(self.landingsside, list):
            self.landingsside = [self.landingsside] if self.landingsside is not None else []
        self.landingsside = [v if isinstance(v, URI) else URI(v) for v in self.landingsside]

        if self.produsent is not None and not isinstance(self.produsent, AktorId):
            self.produsent = AktorId(self.produsent)

        if not isinstance(self.relatert_ressurs, list):
            self.relatert_ressurs = [self.relatert_ressurs] if self.relatert_ressurs is not None else []
        self.relatert_ressurs = [v if isinstance(v, URI) else URI(v) for v in self.relatert_ressurs]

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        if self.utgivelsesdato is not None and not isinstance(self.utgivelsesdato, XSDDate):
            self.utgivelsesdato = XSDDate(self.utgivelsesdato)

        if self.versjon is not None and not isinstance(self.versjon, str):
            self.versjon = str(self.versjon)

        if not isinstance(self.versjonsmerknad, list):
            self.versjonsmerknad = [self.versjonsmerknad] if self.versjonsmerknad is not None else []
        self.versjonsmerknad = [v if isinstance(v, str) else str(v) for v in self.versjonsmerknad]

        if not isinstance(self.har_kvalitetsmerknad, list):
            self.har_kvalitetsmerknad = [self.har_kvalitetsmerknad] if self.har_kvalitetsmerknad is not None else []
        self.har_kvalitetsmerknad = [v if isinstance(v, KvalitetsmerknadId) else KvalitetsmerknadId(v) for v in self.har_kvalitetsmerknad]

        if not isinstance(self.har_kvalitetsmaaling, list):
            self.har_kvalitetsmaaling = [self.har_kvalitetsmaaling] if self.har_kvalitetsmaaling is not None else []
        self.har_kvalitetsmaaling = [v if isinstance(v, KvalitetsmaalingId) else KvalitetsmaalingId(v) for v in self.har_kvalitetsmaaling]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Datasettserie(KatalogisertRessurs):
    """
    Ei serie av relaterte datasett publisert separat men med felles metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["DatasetSeries"]
    class_class_curie: ClassVar[str] = "dcat:DatasetSeries"
    class_name: ClassVar[str] = "Datasettserie"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Datasettserie

    id: Union[str, DatasettserieId] = None
    beskrivelse: Union[str, list[str]] = None
    kontaktpunkt: Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]] = None
    tema: Union[str, list[str]] = None
    tittel: Union[str, list[str]] = None
    utgiver: Union[str, AktorId] = None
    dekningsomraade: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    gjeldende_lovgivning: Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]] = empty_list()
    siste: Optional[Union[str, DatasettId]] = None
    tidsrom: Optional[Union[Union[str, TidsromId], list[Union[str, TidsromId]]]] = empty_list()
    endringsdato: Optional[Union[str, XSDDate]] = None
    frekvens: Optional[str] = None
    forste: Optional[Union[str, DatasettId]] = None
    utgivelsesdato: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasettserieId):
            self.id = DatasettserieId(self.id)

        if self._is_empty(self.beskrivelse):
            self.MissingRequiredField("beskrivelse")
        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self._is_empty(self.kontaktpunkt):
            self.MissingRequiredField("kontaktpunkt")
        if not isinstance(self.kontaktpunkt, list):
            self.kontaktpunkt = [self.kontaktpunkt] if self.kontaktpunkt is not None else []
        self.kontaktpunkt = [v if isinstance(v, KontaktopplysningId) else KontaktopplysningId(v) for v in self.kontaktpunkt]

        if self._is_empty(self.tema):
            self.MissingRequiredField("tema")
        if not isinstance(self.tema, list):
            self.tema = [self.tema] if self.tema is not None else []
        self.tema = [v if isinstance(v, str) else str(v) for v in self.tema]

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.utgiver):
            self.MissingRequiredField("utgiver")
        if not isinstance(self.utgiver, AktorId):
            self.utgiver = AktorId(self.utgiver)

        if not isinstance(self.dekningsomraade, list):
            self.dekningsomraade = [self.dekningsomraade] if self.dekningsomraade is not None else []
        self.dekningsomraade = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.dekningsomraade]

        if not isinstance(self.gjeldende_lovgivning, list):
            self.gjeldende_lovgivning = [self.gjeldende_lovgivning] if self.gjeldende_lovgivning is not None else []
        self.gjeldende_lovgivning = [v if isinstance(v, RegulativRessursId) else RegulativRessursId(v) for v in self.gjeldende_lovgivning]

        if self.siste is not None and not isinstance(self.siste, DatasettId):
            self.siste = DatasettId(self.siste)

        if not isinstance(self.tidsrom, list):
            self.tidsrom = [self.tidsrom] if self.tidsrom is not None else []
        self.tidsrom = [v if isinstance(v, TidsromId) else TidsromId(v) for v in self.tidsrom]

        if self.endringsdato is not None and not isinstance(self.endringsdato, XSDDate):
            self.endringsdato = XSDDate(self.endringsdato)

        if self.frekvens is not None and not isinstance(self.frekvens, str):
            self.frekvens = str(self.frekvens)

        if self.forste is not None and not isinstance(self.forste, DatasettId):
            self.forste = DatasettId(self.forste)

        if self.utgivelsesdato is not None and not isinstance(self.utgivelsesdato, XSDDate):
            self.utgivelsesdato = XSDDate(self.utgivelsesdato)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Datatjeneste(KatalogisertRessurs):
    """
    Ei samling operasjonar tilgjengeleg via eit API-grensesnitt.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["DataService"]
    class_class_curie: ClassVar[str] = "dcat:DataService"
    class_name: ClassVar[str] = "Datatjeneste"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Datatjeneste

    id: Union[str, DatatjenesteId] = None
    endepunkts_url: Union[Union[str, URI], list[Union[str, URI]]] = None
    kontaktpunkt: Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]] = None
    tittel: Union[str, list[str]] = None
    utgiver: Union[str, AktorId] = None
    endepunktsbeskrivelse: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    format: Optional[str] = None
    gjeldende_lovgivning: Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]] = empty_list()
    i_samsvar_med: Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]] = empty_list()
    nokkelord: Optional[Union[str, list[str]]] = empty_list()
    tema: Optional[Union[str, list[str]]] = empty_list()
    tilgjengeliggjor_datasett: Optional[Union[Union[str, DatasettId], list[Union[str, DatasettId]]]] = empty_list()
    tilgjengelighet: Optional[str] = None
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()
    dokumentasjon: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    har_gebyr: Optional[Union[Union[str, GebyrId], list[Union[str, GebyrId]]]] = empty_list()
    identifikator_literal: Optional[str] = None
    landingsside: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    lisens: Optional[str] = None
    rettigheter: Optional[Union[str, RettighetserklaringId]] = None
    status: Optional[Union[str, KonseptId]] = None
    tilgangsrettigheter: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    versjon: Optional[str] = None
    versjonsmerknad: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatatjenesteId):
            self.id = DatatjenesteId(self.id)

        if self._is_empty(self.endepunkts_url):
            self.MissingRequiredField("endepunkts_url")
        if not isinstance(self.endepunkts_url, list):
            self.endepunkts_url = [self.endepunkts_url] if self.endepunkts_url is not None else []
        self.endepunkts_url = [v if isinstance(v, URI) else URI(v) for v in self.endepunkts_url]

        if self._is_empty(self.kontaktpunkt):
            self.MissingRequiredField("kontaktpunkt")
        if not isinstance(self.kontaktpunkt, list):
            self.kontaktpunkt = [self.kontaktpunkt] if self.kontaktpunkt is not None else []
        self.kontaktpunkt = [v if isinstance(v, KontaktopplysningId) else KontaktopplysningId(v) for v in self.kontaktpunkt]

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.utgiver):
            self.MissingRequiredField("utgiver")
        if not isinstance(self.utgiver, AktorId):
            self.utgiver = AktorId(self.utgiver)

        if not isinstance(self.endepunktsbeskrivelse, list):
            self.endepunktsbeskrivelse = [self.endepunktsbeskrivelse] if self.endepunktsbeskrivelse is not None else []
        self.endepunktsbeskrivelse = [v if isinstance(v, URI) else URI(v) for v in self.endepunktsbeskrivelse]

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if not isinstance(self.gjeldende_lovgivning, list):
            self.gjeldende_lovgivning = [self.gjeldende_lovgivning] if self.gjeldende_lovgivning is not None else []
        self.gjeldende_lovgivning = [v if isinstance(v, RegulativRessursId) else RegulativRessursId(v) for v in self.gjeldende_lovgivning]

        if not isinstance(self.i_samsvar_med, list):
            self.i_samsvar_med = [self.i_samsvar_med] if self.i_samsvar_med is not None else []
        self.i_samsvar_med = [v if isinstance(v, StandardId) else StandardId(v) for v in self.i_samsvar_med]

        if not isinstance(self.nokkelord, list):
            self.nokkelord = [self.nokkelord] if self.nokkelord is not None else []
        self.nokkelord = [v if isinstance(v, str) else str(v) for v in self.nokkelord]

        if not isinstance(self.tema, list):
            self.tema = [self.tema] if self.tema is not None else []
        self.tema = [v if isinstance(v, str) else str(v) for v in self.tema]

        if not isinstance(self.tilgjengeliggjor_datasett, list):
            self.tilgjengeliggjor_datasett = [self.tilgjengeliggjor_datasett] if self.tilgjengeliggjor_datasett is not None else []
        self.tilgjengeliggjor_datasett = [v if isinstance(v, DatasettId) else DatasettId(v) for v in self.tilgjengeliggjor_datasett]

        if self.tilgjengelighet is not None and not isinstance(self.tilgjengelighet, str):
            self.tilgjengelighet = str(self.tilgjengelighet)

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if not isinstance(self.dokumentasjon, list):
            self.dokumentasjon = [self.dokumentasjon] if self.dokumentasjon is not None else []
        self.dokumentasjon = [v if isinstance(v, URI) else URI(v) for v in self.dokumentasjon]

        if not isinstance(self.har_gebyr, list):
            self.har_gebyr = [self.har_gebyr] if self.har_gebyr is not None else []
        self.har_gebyr = [v if isinstance(v, GebyrId) else GebyrId(v) for v in self.har_gebyr]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if not isinstance(self.landingsside, list):
            self.landingsside = [self.landingsside] if self.landingsside is not None else []
        self.landingsside = [v if isinstance(v, URI) else URI(v) for v in self.landingsside]

        if self.lisens is not None and not isinstance(self.lisens, str):
            self.lisens = str(self.lisens)

        if self.rettigheter is not None and not isinstance(self.rettigheter, RettighetserklaringId):
            self.rettigheter = RettighetserklaringId(self.rettigheter)

        if self.status is not None and not isinstance(self.status, KonseptId):
            self.status = KonseptId(self.status)

        if not isinstance(self.tilgangsrettigheter, list):
            self.tilgangsrettigheter = [self.tilgangsrettigheter] if self.tilgangsrettigheter is not None else []
        self.tilgangsrettigheter = [v if isinstance(v, URI) else URI(v) for v in self.tilgangsrettigheter]

        if self.versjon is not None and not isinstance(self.versjon, str):
            self.versjon = str(self.versjon)

        if not isinstance(self.versjonsmerknad, list):
            self.versjonsmerknad = [self.versjonsmerknad] if self.versjonsmerknad is not None else []
        self.versjonsmerknad = [v if isinstance(v, str) else str(v) for v in self.versjonsmerknad]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Katalogpost(YAMLRoot):
    """
    Ein katalogpost som beskriv ein ressurs i katalogen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["CatalogRecord"]
    class_class_curie: ClassVar[str] = "dcat:CatalogRecord"
    class_name: ClassVar[str] = "Katalogpost"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Katalogpost

    id: Union[str, KatalogpostId] = None
    endringsdato: Union[str, XSDDate] = None
    primaertema: Union[str, KatalogisertRessursId] = None
    i_samsvar_med: Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]] = empty_list()
    status: Optional[Union[str, KonseptId]] = None
    utgivelsesdato: Optional[Union[str, XSDDate]] = None
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()
    kilde_post: Optional[Union[str, URI]] = None
    spraak: Optional[Union[str, list[str]]] = empty_list()
    tittel: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KatalogpostId):
            self.id = KatalogpostId(self.id)

        if self._is_empty(self.endringsdato):
            self.MissingRequiredField("endringsdato")
        if not isinstance(self.endringsdato, XSDDate):
            self.endringsdato = XSDDate(self.endringsdato)

        if self._is_empty(self.primaertema):
            self.MissingRequiredField("primaertema")
        if not isinstance(self.primaertema, KatalogisertRessursId):
            self.primaertema = KatalogisertRessursId(self.primaertema)

        if not isinstance(self.i_samsvar_med, list):
            self.i_samsvar_med = [self.i_samsvar_med] if self.i_samsvar_med is not None else []
        self.i_samsvar_med = [v if isinstance(v, StandardId) else StandardId(v) for v in self.i_samsvar_med]

        if self.status is not None and not isinstance(self.status, KonseptId):
            self.status = KonseptId(self.status)

        if self.utgivelsesdato is not None and not isinstance(self.utgivelsesdato, XSDDate):
            self.utgivelsesdato = XSDDate(self.utgivelsesdato)

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self.kilde_post is not None and not isinstance(self.kilde_post, URI):
            self.kilde_post = URI(self.kilde_post)

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Katalog(KatalogisertRessurs):
    """
    Ei kuratert samling av metadata om datasett, datatenestar og/eller andre katalogar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Catalog"]
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "Katalog"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Katalog

    id: Union[str, KatalogId] = None
    beskrivelse: Union[str, list[str]] = None
    kontaktpunkt: Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]] = None
    tittel: Union[str, list[str]] = None
    utgiver: Union[str, AktorId] = None
    datasett: Optional[Union[Union[str, DatasettId], list[Union[str, DatasettId]]]] = empty_list()
    datatjeneste: Optional[Union[Union[str, DatatjenesteId], list[Union[str, DatatjenesteId]]]] = empty_list()
    dekningsomraade: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    endringsdato: Optional[Union[str, XSDDate]] = None
    heimeside: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    lisens: Optional[str] = None
    spraak: Optional[Union[str, list[str]]] = empty_list()
    temaer: Optional[Union[Union[str, BegrepssamlingId], list[Union[str, BegrepssamlingId]]]] = empty_list()
    utgivelsesdato: Optional[Union[str, XSDDate]] = None
    gjeldende_lovgivning: Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]] = empty_list()
    har_del: Optional[Union[Union[str, KatalogId], list[Union[str, KatalogId]]]] = empty_list()
    identifikator_literal: Optional[str] = None
    underkatalog: Optional[Union[Union[str, KatalogId], list[Union[str, KatalogId]]]] = empty_list()
    katalogpost: Optional[Union[Union[str, KatalogpostId], list[Union[str, KatalogpostId]]]] = empty_list()
    produsent: Optional[Union[str, AktorId]] = None
    rettigheter: Optional[Union[str, RettighetserklaringId]] = None
    tidsrom: Optional[Union[Union[str, TidsromId], list[Union[str, TidsromId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KatalogId):
            self.id = KatalogId(self.id)

        if self._is_empty(self.beskrivelse):
            self.MissingRequiredField("beskrivelse")
        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self._is_empty(self.kontaktpunkt):
            self.MissingRequiredField("kontaktpunkt")
        if not isinstance(self.kontaktpunkt, list):
            self.kontaktpunkt = [self.kontaktpunkt] if self.kontaktpunkt is not None else []
        self.kontaktpunkt = [v if isinstance(v, KontaktopplysningId) else KontaktopplysningId(v) for v in self.kontaktpunkt]

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.utgiver):
            self.MissingRequiredField("utgiver")
        if not isinstance(self.utgiver, AktorId):
            self.utgiver = AktorId(self.utgiver)

        if not isinstance(self.datasett, list):
            self.datasett = [self.datasett] if self.datasett is not None else []
        self.datasett = [v if isinstance(v, DatasettId) else DatasettId(v) for v in self.datasett]

        if not isinstance(self.datatjeneste, list):
            self.datatjeneste = [self.datatjeneste] if self.datatjeneste is not None else []
        self.datatjeneste = [v if isinstance(v, DatatjenesteId) else DatatjenesteId(v) for v in self.datatjeneste]

        if not isinstance(self.dekningsomraade, list):
            self.dekningsomraade = [self.dekningsomraade] if self.dekningsomraade is not None else []
        self.dekningsomraade = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.dekningsomraade]

        if self.endringsdato is not None and not isinstance(self.endringsdato, XSDDate):
            self.endringsdato = XSDDate(self.endringsdato)

        if not isinstance(self.heimeside, list):
            self.heimeside = [self.heimeside] if self.heimeside is not None else []
        self.heimeside = [v if isinstance(v, URI) else URI(v) for v in self.heimeside]

        if self.lisens is not None and not isinstance(self.lisens, str):
            self.lisens = str(self.lisens)

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

        if not isinstance(self.temaer, list):
            self.temaer = [self.temaer] if self.temaer is not None else []
        self.temaer = [v if isinstance(v, BegrepssamlingId) else BegrepssamlingId(v) for v in self.temaer]

        if self.utgivelsesdato is not None and not isinstance(self.utgivelsesdato, XSDDate):
            self.utgivelsesdato = XSDDate(self.utgivelsesdato)

        if not isinstance(self.gjeldende_lovgivning, list):
            self.gjeldende_lovgivning = [self.gjeldende_lovgivning] if self.gjeldende_lovgivning is not None else []
        self.gjeldende_lovgivning = [v if isinstance(v, RegulativRessursId) else RegulativRessursId(v) for v in self.gjeldende_lovgivning]

        if not isinstance(self.har_del, list):
            self.har_del = [self.har_del] if self.har_del is not None else []
        self.har_del = [v if isinstance(v, KatalogId) else KatalogId(v) for v in self.har_del]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if not isinstance(self.underkatalog, list):
            self.underkatalog = [self.underkatalog] if self.underkatalog is not None else []
        self.underkatalog = [v if isinstance(v, KatalogId) else KatalogId(v) for v in self.underkatalog]

        if not isinstance(self.katalogpost, list):
            self.katalogpost = [self.katalogpost] if self.katalogpost is not None else []
        self.katalogpost = [v if isinstance(v, KatalogpostId) else KatalogpostId(v) for v in self.katalogpost]

        if self.produsent is not None and not isinstance(self.produsent, AktorId):
            self.produsent = AktorId(self.produsent)

        if self.rettigheter is not None and not isinstance(self.rettigheter, RettighetserklaringId):
            self.rettigheter = RettighetserklaringId(self.rettigheter)

        if not isinstance(self.tidsrom, list):
            self.tidsrom = [self.tidsrom] if self.tidsrom is not None else []
        self.tidsrom = [v if isinstance(v, TidsromId) else TidsromId(v) for v in self.tidsrom]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kvalitetsdimensjon(YAMLRoot):
    """
    Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQV["Dimension"]
    class_class_curie: ClassVar[str] = "dqv:Dimension"
    class_name: ClassVar[str] = "Kvalitetsdimensjon"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Kvalitetsdimensjon

    id: Union[str, KvalitetsdimensjonId] = None
    har_anbefalt_term: Optional[Union[str, list[str]]] = empty_list()
    har_definisjon: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KvalitetsdimensjonId):
            self.id = KvalitetsdimensjonId(self.id)

        if not isinstance(self.har_anbefalt_term, list):
            self.har_anbefalt_term = [self.har_anbefalt_term] if self.har_anbefalt_term is not None else []
        self.har_anbefalt_term = [v if isinstance(v, str) else str(v) for v in self.har_anbefalt_term]

        if not isinstance(self.har_definisjon, list):
            self.har_definisjon = [self.har_definisjon] if self.har_definisjon is not None else []
        self.har_definisjon = [v if isinstance(v, str) else str(v) for v in self.har_definisjon]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kvalitetsdeldimensjon(Kvalitetsdimensjon):
    """
    Ein deldimensjon av ein kvalitetsdimensjon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQVNO["SubDimension"]
    class_class_curie: ClassVar[str] = "dqvno:SubDimension"
    class_name: ClassVar[str] = "Kvalitetsdeldimensjon"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Kvalitetsdeldimensjon

    id: Union[str, KvalitetsdeldimensjonId] = None
    er_deldimensjon_av: Union[str, KvalitetsdimensjonId] = None
    har_anbefalt_term: Optional[Union[str, list[str]]] = empty_list()
    har_definisjon: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KvalitetsdeldimensjonId):
            self.id = KvalitetsdeldimensjonId(self.id)

        if self._is_empty(self.er_deldimensjon_av):
            self.MissingRequiredField("er_deldimensjon_av")
        if not isinstance(self.er_deldimensjon_av, KvalitetsdimensjonId):
            self.er_deldimensjon_av = KvalitetsdimensjonId(self.er_deldimensjon_av)

        if not isinstance(self.har_anbefalt_term, list):
            self.har_anbefalt_term = [self.har_anbefalt_term] if self.har_anbefalt_term is not None else []
        self.har_anbefalt_term = [v if isinstance(v, str) else str(v) for v in self.har_anbefalt_term]

        if not isinstance(self.har_definisjon, list):
            self.har_definisjon = [self.har_definisjon] if self.har_definisjon is not None else []
        self.har_definisjon = [v if isinstance(v, str) else str(v) for v in self.har_definisjon]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kvalitetsmaal(YAMLRoot):
    """
    Eit kvalitetsmål som operasjonaliserer ein kvalitetsdeldimensjon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQV["Metric"]
    class_class_curie: ClassVar[str] = "dqv:Metric"
    class_name: ClassVar[str] = "Kvalitetsmaal"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Kvalitetsmaal

    id: Union[str, KvalitetsmaalId] = None
    er_i_kvalitetsdeldimensjon: Union[str, KvalitetsdeldimensjonId] = None
    har_forventet_datatype: Optional[Union[str, URIorCURIE]] = None
    har_anbefalt_term: Optional[Union[str, list[str]]] = empty_list()
    har_definisjon: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KvalitetsmaalId):
            self.id = KvalitetsmaalId(self.id)

        if self._is_empty(self.er_i_kvalitetsdeldimensjon):
            self.MissingRequiredField("er_i_kvalitetsdeldimensjon")
        if not isinstance(self.er_i_kvalitetsdeldimensjon, KvalitetsdeldimensjonId):
            self.er_i_kvalitetsdeldimensjon = KvalitetsdeldimensjonId(self.er_i_kvalitetsdeldimensjon)

        if self.har_forventet_datatype is not None and not isinstance(self.har_forventet_datatype, URIorCURIE):
            self.har_forventet_datatype = URIorCURIE(self.har_forventet_datatype)

        if not isinstance(self.har_anbefalt_term, list):
            self.har_anbefalt_term = [self.har_anbefalt_term] if self.har_anbefalt_term is not None else []
        self.har_anbefalt_term = [v if isinstance(v, str) else str(v) for v in self.har_anbefalt_term]

        if not isinstance(self.har_definisjon, list):
            self.har_definisjon = [self.har_definisjon] if self.har_definisjon is not None else []
        self.har_definisjon = [v if isinstance(v, str) else str(v) for v in self.har_definisjon]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kvalitetsmerknad(YAMLRoot):
    """
    Ein merknad om kvaliteten til eit datasett.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQV["QualityAnnotation"]
    class_class_curie: ClassVar[str] = "dqv:QualityAnnotation"
    class_name: ClassVar[str] = "Kvalitetsmerknad"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Kvalitetsmerknad

    id: Union[str, KvalitetsmerknadId] = None
    er_motivert_av: Union[str, URIorCURIE] = None
    er_i_kvalitetsdimensjon: Optional[Union[Union[str, KvalitetsdimensjonId], list[Union[str, KvalitetsdimensjonId]]]] = empty_list()
    har_tekstdel: Optional[Union[str, TekstdelId]] = None
    har_merknad: Optional[Union[str, list[str]]] = empty_list()
    har_maal: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KvalitetsmerknadId):
            self.id = KvalitetsmerknadId(self.id)

        if self._is_empty(self.er_motivert_av):
            self.MissingRequiredField("er_motivert_av")
        if not isinstance(self.er_motivert_av, URIorCURIE):
            self.er_motivert_av = URIorCURIE(self.er_motivert_av)

        if not isinstance(self.er_i_kvalitetsdimensjon, list):
            self.er_i_kvalitetsdimensjon = [self.er_i_kvalitetsdimensjon] if self.er_i_kvalitetsdimensjon is not None else []
        self.er_i_kvalitetsdimensjon = [v if isinstance(v, KvalitetsdimensjonId) else KvalitetsdimensjonId(v) for v in self.er_i_kvalitetsdimensjon]

        if self.har_tekstdel is not None and not isinstance(self.har_tekstdel, TekstdelId):
            self.har_tekstdel = TekstdelId(self.har_tekstdel)

        if not isinstance(self.har_merknad, list):
            self.har_merknad = [self.har_merknad] if self.har_merknad is not None else []
        self.har_merknad = [v if isinstance(v, str) else str(v) for v in self.har_merknad]

        if self.har_maal is not None and not isinstance(self.har_maal, URI):
            self.har_maal = URI(self.har_maal)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Brukartilbakemelding(Kvalitetsmerknad):
    """
    Tilbakemelding frå ein brukar om kvaliteten til eit datasett.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQV["UserQualityFeedback"]
    class_class_curie: ClassVar[str] = "dqv:UserQualityFeedback"
    class_name: ClassVar[str] = "Brukartilbakemelding"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Brukartilbakemelding

    id: Union[str, BrukartilbakemeldingId] = None
    er_motivert_av: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BrukartilbakemeldingId):
            self.id = BrukartilbakemeldingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kvalitetssertifikat(Kvalitetsmerknad):
    """
    Eit sertifikat som stadfester kvaliteten til eit datasett.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQV["QualityCertificate"]
    class_class_curie: ClassVar[str] = "dqv:QualityCertificate"
    class_name: ClassVar[str] = "Kvalitetssertifikat"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Kvalitetssertifikat

    id: Union[str, KvalitetssertifikatId] = None
    er_motivert_av: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KvalitetssertifikatId):
            self.id = KvalitetssertifikatId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kvalitetsmaaling(YAMLRoot):
    """
    Ei konkret måling av eit kvalitetsmål for eit datasett.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQV["QualityMeasurement"]
    class_class_curie: ClassVar[str] = "dqv:QualityMeasurement"
    class_name: ClassVar[str] = "Kvalitetsmaaling"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Kvalitetsmaaling

    id: Union[str, KvalitetsmaalingId] = None
    er_kvalitetsmaaling_av: Union[str, KvalitetsmaalId] = None
    har_verdi: Optional[str] = None
    har_merknad: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KvalitetsmaalingId):
            self.id = KvalitetsmaalingId(self.id)

        if self._is_empty(self.er_kvalitetsmaaling_av):
            self.MissingRequiredField("er_kvalitetsmaaling_av")
        if not isinstance(self.er_kvalitetsmaaling_av, KvalitetsmaalId):
            self.er_kvalitetsmaaling_av = KvalitetsmaalId(self.er_kvalitetsmaaling_av)

        if self.har_verdi is not None and not isinstance(self.har_verdi, str):
            self.har_verdi = str(self.har_verdi)

        if not isinstance(self.har_merknad, list):
            self.har_merknad = [self.har_merknad] if self.har_merknad is not None else []
        self.har_merknad = [v if isinstance(v, str) else str(v) for v in self.har_merknad]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Standard(YAMLRoot):
    """
    Ein standard eller spesifikasjon som eit datasett er i samsvar med.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["Standard"]
    class_class_curie: ClassVar[str] = "dct:Standard"
    class_name: ClassVar[str] = "Standard"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Standard

    id: Union[str, StandardId] = None
    tittel: Union[str, list[str]] = None
    er_i_kvalitetsdimensjon: Optional[Union[Union[str, KvalitetsdimensjonId], list[Union[str, KvalitetsdimensjonId]]]] = empty_list()
    har_referanse: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    har_merknad: Optional[Union[str, list[str]]] = empty_list()
    har_versjonsnummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StandardId):
            self.id = StandardId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if not isinstance(self.er_i_kvalitetsdimensjon, list):
            self.er_i_kvalitetsdimensjon = [self.er_i_kvalitetsdimensjon] if self.er_i_kvalitetsdimensjon is not None else []
        self.er_i_kvalitetsdimensjon = [v if isinstance(v, KvalitetsdimensjonId) else KvalitetsdimensjonId(v) for v in self.er_i_kvalitetsdimensjon]

        if not isinstance(self.har_referanse, list):
            self.har_referanse = [self.har_referanse] if self.har_referanse is not None else []
        self.har_referanse = [v if isinstance(v, URI) else URI(v) for v in self.har_referanse]

        if not isinstance(self.har_merknad, list):
            self.har_merknad = [self.har_merknad] if self.har_merknad is not None else []
        self.har_merknad = [v if isinstance(v, str) else str(v) for v in self.har_merknad]

        if self.har_versjonsnummer is not None and not isinstance(self.har_versjonsnummer, str):
            self.har_versjonsnummer = str(self.har_versjonsnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tekstdel(YAMLRoot):
    """
    Ein tekstleg del av ein kvalitetsmerknad (Web Annotation).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OA["TextualBody"]
    class_class_curie: ClassVar[str] = "oa:TextualBody"
    class_name: ClassVar[str] = "Tekstdel"
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Tekstdel

    id: Union[str, TekstdelId] = None
    har_verdi_tekstdel: str = None
    format: Optional[str] = None
    spraak: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TekstdelId):
            self.id = TekstdelId(self.id)

        if self._is_empty(self.har_verdi_tekstdel):
            self.MissingRequiredField("har_verdi_tekstdel")
        if not isinstance(self.har_verdi_tekstdel, str):
            self.har_verdi_tekstdel = str(self.har_verdi_tekstdel)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

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
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Mediatype

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
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Konsept

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
    class_model_uri: ClassVar[URIRef] = SAMTBUSKOLE.Begrepssamling

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

slots.navn = Slot(uri=SAMTBUSKOLE.navn, name="navn", curie=SAMTBUSKOLE.curie('navn'),
                   model_uri=SAMTBUSKOLE.navn, domain=None, range=Optional[str])

slots.kommunenummer = Slot(uri=DCAT.identifier, name="kommunenummer", curie=DCAT.curie('identifier'),
                   model_uri=SAMTBUSKOLE.kommunenummer, domain=None, range=Optional[str])

slots.fylkesnummer = Slot(uri=DCAT.identifier, name="fylkesnummer", curie=DCAT.curie('identifier'),
                   model_uri=SAMTBUSKOLE.fylkesnummer, domain=None, range=Optional[str])

slots.organisasjonsnummer = Slot(uri=DCT.identifier, name="organisasjonsnummer", curie=DCT.curie('identifier'),
                   model_uri=SAMTBUSKOLE.organisasjonsnummer, domain=None, range=Optional[str])

slots.trinniva = Slot(uri=SAMTBUSKOLE.trinniva, name="trinniva", curie=SAMTBUSKOLE.curie('trinniva'),
                   model_uri=SAMTBUSKOLE.trinniva, domain=None, range=Optional[str])

slots.har_skoleeier = Slot(uri=SAMTBUSKOLE.har_skoleeier, name="har_skoleeier", curie=SAMTBUSKOLE.curie('har_skoleeier'),
                   model_uri=SAMTBUSKOLE.har_skoleeier, domain=Skole, range=Optional[Union[str, SkoleeierId]])

slots.del_av_skole = Slot(uri=ORG.unitOf, name="del_av_skole", curie=ORG.curie('unitOf'),
                   model_uri=SAMTBUSKOLE.del_av_skole, domain=Basisgruppe, range=Optional[Union[str, SkoleId]])

slots.horer_til_basisgruppe = Slot(uri=SAMTBUSKOLE.horer_til_basisgruppe, name="horer_til_basisgruppe", curie=SAMTBUSKOLE.curie('horer_til_basisgruppe'),
                   model_uri=SAMTBUSKOLE.horer_til_basisgruppe, domain=Elev, range=Optional[Union[str, BasisgruppeId]])

slots.enhetsleder_for = Slot(uri=SAMTBUSKOLE.enhetsleder_for, name="enhetsleder_for", curie=SAMTBUSKOLE.curie('enhetsleder_for'),
                   model_uri=SAMTBUSKOLE.enhetsleder_for, domain=Rektor, range=Optional[Union[str, SkoleId]])

slots.tilknyttet_basisgruppe = Slot(uri=SAMTBUSKOLE.tilknyttet_basisgruppe, name="tilknyttet_basisgruppe", curie=SAMTBUSKOLE.curie('tilknyttet_basisgruppe'),
                   model_uri=SAMTBUSKOLE.tilknyttet_basisgruppe, domain=Kontaktlaerer, range=Optional[Union[str, BasisgruppeId]])

slots.har_saerlig_ansvar_for = Slot(uri=SAMTBUSKOLE.har_saerlig_ansvar_for, name="har_saerlig_ansvar_for", curie=SAMTBUSKOLE.curie('har_saerlig_ansvar_for'),
                   model_uri=SAMTBUSKOLE.har_saerlig_ansvar_for, domain=Kontaktlaerer, range=Optional[Union[str, ElevId]])

slots.jobber_paa_skole = Slot(uri=SAMTBUSKOLE.jobber_paa_skole, name="jobber_paa_skole", curie=SAMTBUSKOLE.curie('jobber_paa_skole'),
                   model_uri=SAMTBUSKOLE.jobber_paa_skole, domain=Kontaktlaerer, range=Optional[Union[str, SkoleId]])

slots.tittel_literal = Slot(uri=DCT.title, name="tittel_literal", curie=DCT.curie('title'),
                   model_uri=SAMTBUSKOLE.tittel_literal, domain=None, range=Optional[Union[str, list[str]]])

slots.notasjon = Slot(uri=SKOS.notation, name="notasjon", curie=SKOS.curie('notation'),
                   model_uri=SAMTBUSKOLE.notasjon, domain=None, range=Optional[str])

slots.versjon = Slot(uri=DCAT.version, name="versjon", curie=DCAT.curie('version'),
                   model_uri=SAMTBUSKOLE.versjon, domain=None, range=Optional[str])

slots.navn_aktor = Slot(uri=FOAF.name, name="navn_aktor", curie=FOAF.curie('name'),
                   model_uri=SAMTBUSKOLE.navn_aktor, domain=None, range=Optional[Union[str, list[str]]])

slots.navn_vcard = Slot(uri=VCARD.fn, name="navn_vcard", curie=VCARD.curie('fn'),
                   model_uri=SAMTBUSKOLE.navn_vcard, domain=None, range=Optional[Union[str, list[str]]])

slots.algoritme = Slot(uri=SPDX.algorithm, name="algoritme", curie=SPDX.curie('algorithm'),
                   model_uri=SAMTBUSKOLE.algoritme, domain=None, range=Optional[str])

slots.sjekksumverdi = Slot(uri=SPDX.checksumValue, name="sjekksumverdi", curie=SPDX.curie('checksumValue'),
                   model_uri=SAMTBUSKOLE.sjekksumverdi, domain=None, range=Optional[str])

slots.belop = Slot(uri=CV.hasValue, name="belop", curie=CV.curie('hasValue'),
                   model_uri=SAMTBUSKOLE.belop, domain=None, range=Optional[str])

slots.startdato = Slot(uri=DCAT.startDate, name="startdato", curie=DCAT.curie('startDate'),
                   model_uri=SAMTBUSKOLE.startdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.sluttdato = Slot(uri=DCAT.endDate, name="sluttdato", curie=DCAT.curie('endDate'),
                   model_uri=SAMTBUSKOLE.sluttdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.tidsopplosning = Slot(uri=DCAT.temporalResolution, name="tidsopplosning", curie=DCAT.curie('temporalResolution'),
                   model_uri=SAMTBUSKOLE.tidsopplosning, domain=None, range=Optional[str])

slots.endepunkts_url = Slot(uri=DCAT.endpointURL, name="endepunkts_url", curie=DCAT.curie('endpointURL'),
                   model_uri=SAMTBUSKOLE.endepunkts_url, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.endepunktsbeskrivelse = Slot(uri=DCAT.endpointDescription, name="endepunktsbeskrivelse", curie=DCAT.curie('endpointDescription'),
                   model_uri=SAMTBUSKOLE.endepunktsbeskrivelse, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.tilgangs_url = Slot(uri=DCAT.accessURL, name="tilgangs_url", curie=DCAT.curie('accessURL'),
                   model_uri=SAMTBUSKOLE.tilgangs_url, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.nedlastningslenke = Slot(uri=DCAT.downloadURL, name="nedlastningslenke", curie=DCAT.curie('downloadURL'),
                   model_uri=SAMTBUSKOLE.nedlastningslenke, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.landingsside = Slot(uri=DCAT.landingPage, name="landingsside", curie=DCAT.curie('landingPage'),
                   model_uri=SAMTBUSKOLE.landingsside, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.har_epost = Slot(uri=VCARD.hasEmail, name="har_epost", curie=VCARD.curie('hasEmail'),
                   model_uri=SAMTBUSKOLE.har_epost, domain=None, range=Optional[str])

slots.har_kontaktside = Slot(uri=VCARD.hasURL, name="har_kontaktside", curie=VCARD.curie('hasURL'),
                   model_uri=SAMTBUSKOLE.har_kontaktside, domain=None, range=Optional[str])

slots.dokumentasjon = Slot(uri=FOAF.page, name="dokumentasjon", curie=FOAF.curie('page'),
                   model_uri=SAMTBUSKOLE.dokumentasjon, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.referanse = Slot(uri=RDFS.seeAlso, name="referanse", curie=RDFS.curie('seeAlso'),
                   model_uri=SAMTBUSKOLE.referanse, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.relatert_ressurs = Slot(uri=DCT.relation, name="relatert_ressurs", curie=DCT.curie('relation'),
                   model_uri=SAMTBUSKOLE.relatert_ressurs, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.kilde_post = Slot(uri=DCT.source, name="kilde_post", curie=DCT.curie('source'),
                   model_uri=SAMTBUSKOLE.kilde_post, domain=None, range=Optional[Union[str, URI]])

slots.krediteringsurl = Slot(uri=ODRS.attributionURL, name="krediteringsurl", curie=ODRS.curie('attributionURL'),
                   model_uri=SAMTBUSKOLE.krediteringsurl, domain=None, range=Optional[Union[str, URI]])

slots.filstorrelse = Slot(uri=DCAT.byteSize, name="filstorrelse", curie=DCAT.curie('byteSize'),
                   model_uri=SAMTBUSKOLE.filstorrelse, domain=None, range=Optional[int])

slots.har_kvalitetsmerknad = Slot(uri=DQV.hasQualityAnnotation, name="har_kvalitetsmerknad", curie=DQV.curie('hasQualityAnnotation'),
                   model_uri=SAMTBUSKOLE.har_kvalitetsmerknad, domain=None, range=Optional[Union[Union[str, KvalitetsmerknadId], list[Union[str, KvalitetsmerknadId]]]])

slots.anvendelsesretningslinjer = Slot(uri=ODRS.reuserGuidelines, name="anvendelsesretningslinjer", curie=ODRS.curie('reuserGuidelines'),
                   model_uri=SAMTBUSKOLE.anvendelsesretningslinjer, domain=None, range=Optional[str])

slots.jurisdiksjon = Slot(uri=ODRS.jurisdiction, name="jurisdiksjon", curie=ODRS.curie('jurisdiction'),
                   model_uri=SAMTBUSKOLE.jurisdiksjon, domain=None, range=Optional[str])

slots.krediteringstekst = Slot(uri=ODRS.attributionText, name="krediteringstekst", curie=ODRS.curie('attributionText'),
                   model_uri=SAMTBUSKOLE.krediteringstekst, domain=None, range=Optional[str])

slots.opphavsrettserklaring = Slot(uri=ODRS.copyrightStatement, name="opphavsrettserklaring", curie=ODRS.curie('copyrightStatement'),
                   model_uri=SAMTBUSKOLE.opphavsrettserklaring, domain=None, range=Optional[str])

slots.opphavsrettsinnehaver = Slot(uri=ODRS.copyrightHolder, name="opphavsrettsinnehaver", curie=ODRS.curie('copyrightHolder'),
                   model_uri=SAMTBUSKOLE.opphavsrettsinnehaver, domain=None, range=Optional[str])

slots.opphavsrettsnotis = Slot(uri=ODRS.copyrightNotice, name="opphavsrettsnotis", curie=ODRS.curie('copyrightNotice'),
                   model_uri=SAMTBUSKOLE.opphavsrettsnotis, domain=None, range=Optional[str])

slots.opphavsrettsaar = Slot(uri=ODRS.copyrightYear, name="opphavsrettsaar", curie=ODRS.curie('copyrightYear'),
                   model_uri=SAMTBUSKOLE.opphavsrettsaar, domain=None, range=Optional[str])

slots.utgiver = Slot(uri=DCT.publisher, name="utgiver", curie=DCT.curie('publisher'),
                   model_uri=SAMTBUSKOLE.utgiver, domain=None, range=Optional[Union[str, AktorId]])

slots.produsent = Slot(uri=DCT.creator, name="produsent", curie=DCT.curie('creator'),
                   model_uri=SAMTBUSKOLE.produsent, domain=None, range=Optional[Union[str, AktorId]])

slots.kontaktpunkt = Slot(uri=DCAT.contactPoint, name="kontaktpunkt", curie=DCAT.curie('contactPoint'),
                   model_uri=SAMTBUSKOLE.kontaktpunkt, domain=None, range=Optional[Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]]])

slots.tema = Slot(uri=DCAT.theme, name="tema", curie=DCAT.curie('theme'),
                   model_uri=SAMTBUSKOLE.tema, domain=None, range=Optional[Union[str, list[str]]])

slots.temaer = Slot(uri=DCAT.themeTaxonomy, name="temaer", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=SAMTBUSKOLE.temaer, domain=None, range=Optional[Union[Union[str, BegrepssamlingId], list[Union[str, BegrepssamlingId]]]])

slots.begrep = Slot(uri=DCT.subject, name="begrep", curie=DCT.curie('subject'),
                   model_uri=SAMTBUSKOLE.begrep, domain=None, range=Optional[Union[str, list[str]]])

slots.medietype = Slot(uri=DCAT.mediaType, name="medietype", curie=DCAT.curie('mediaType'),
                   model_uri=SAMTBUSKOLE.medietype, domain=None, range=Optional[Union[str, MediatypeId]])

slots.komprimeringsformat = Slot(uri=DCAT.compressFormat, name="komprimeringsformat", curie=DCAT.curie('compressFormat'),
                   model_uri=SAMTBUSKOLE.komprimeringsformat, domain=None, range=Optional[Union[str, MediatypeId]])

slots.pakkeformat = Slot(uri=DCAT.packageFormat, name="pakkeformat", curie=DCAT.curie('packageFormat'),
                   model_uri=SAMTBUSKOLE.pakkeformat, domain=None, range=Optional[Union[str, MediatypeId]])

slots.frekvens = Slot(uri=DCT.accrualPeriodicity, name="frekvens", curie=DCT.curie('accrualPeriodicity'),
                   model_uri=SAMTBUSKOLE.frekvens, domain=None, range=Optional[str])

slots.tilgjengelighet = Slot(uri=DCATAP.availability, name="tilgjengelighet", curie=DCATAP.curie('availability'),
                   model_uri=SAMTBUSKOLE.tilgjengelighet, domain=None, range=Optional[str])

slots.har_rolle = Slot(uri=DCAT.hadRole, name="har_rolle", curie=DCAT.curie('hadRole'),
                   model_uri=SAMTBUSKOLE.har_rolle, domain=None, range=Optional[str])

slots.lisens = Slot(uri=DCT.license, name="lisens", curie=DCT.curie('license'),
                   model_uri=SAMTBUSKOLE.lisens, domain=None, range=Optional[str])

slots.gjeldende_lovgivning = Slot(uri=DCATAP.applicableLegislation, name="gjeldende_lovgivning", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=SAMTBUSKOLE.gjeldende_lovgivning, domain=None, range=Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]])

slots.tidsrom = Slot(uri=DCT.temporal, name="tidsrom", curie=DCT.curie('temporal'),
                   model_uri=SAMTBUSKOLE.tidsrom, domain=None, range=Optional[Union[Union[str, TidsromId], list[Union[str, TidsromId]]]])

slots.tilgangsrettigheter = Slot(uri=DCT.accessRights, name="tilgangsrettigheter", curie=DCT.curie('accessRights'),
                   model_uri=SAMTBUSKOLE.tilgangsrettigheter, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.rettigheter = Slot(uri=DCT.rights, name="rettigheter", curie=DCT.curie('rights'),
                   model_uri=SAMTBUSKOLE.rettigheter, domain=None, range=Optional[Union[str, RettighetserklaringId]])

slots.i_samsvar_med = Slot(uri=DCT.conformsTo, name="i_samsvar_med", curie=DCT.curie('conformsTo'),
                   model_uri=SAMTBUSKOLE.i_samsvar_med, domain=None, range=Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]])

slots.sjekksum = Slot(uri=SPDX.checksum, name="sjekksum", curie=SPDX.curie('checksum'),
                   model_uri=SAMTBUSKOLE.sjekksum, domain=None, range=Optional[Union[str, SjekksumId]])

slots.policy = Slot(uri=ODRL.hasPolicy, name="policy", curie=ODRL.curie('hasPolicy'),
                   model_uri=SAMTBUSKOLE.policy, domain=None, range=Optional[str])

slots.eierskapshistorikk = Slot(uri=DCT.provenance, name="eierskapshistorikk", curie=DCT.curie('provenance'),
                   model_uri=SAMTBUSKOLE.eierskapshistorikk, domain=None, range=Optional[Union[str, list[str]]])

slots.ble_generert_ved = Slot(uri=PROV.wasGeneratedBy, name="ble_generert_ved", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=SAMTBUSKOLE.ble_generert_ved, domain=Datasett, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.annen_ansvarlig_aktor = Slot(uri=PROV.qualifiedAttribution, name="annen_ansvarlig_aktor", curie=PROV.curie('qualifiedAttribution'),
                   model_uri=SAMTBUSKOLE.annen_ansvarlig_aktor, domain=None, range=Optional[Union[str, list[str]]])

slots.annen_identifikator = Slot(uri=ADMS.identifier, name="annen_identifikator", curie=ADMS.curie('identifier'),
                   model_uri=SAMTBUSKOLE.annen_identifikator, domain=None, range=Optional[Union[Union[str, IdentifikatorId], list[Union[str, IdentifikatorId]]]])

slots.annen_spesifikk_relasjon = Slot(uri=DCAT.qualifiedRelation, name="annen_spesifikk_relasjon", curie=DCAT.curie('qualifiedRelation'),
                   model_uri=SAMTBUSKOLE.annen_spesifikk_relasjon, domain=None, range=Optional[Union[Union[str, RelasjonId], list[Union[str, RelasjonId]]]])

slots.relasjon_til = Slot(uri=DCT.relation, name="relasjon_til", curie=DCT.curie('relation'),
                   model_uri=SAMTBUSKOLE.relasjon_til, domain=None, range=Optional[Union[str, URI]])

slots.primaertema = Slot(uri=FOAF.primaryTopic, name="primaertema", curie=FOAF.curie('primaryTopic'),
                   model_uri=SAMTBUSKOLE.primaertema, domain=None, range=Optional[Union[str, KatalogisertRessursId]])

slots.datasettdistribusjon = Slot(uri=DCAT.distribution, name="datasettdistribusjon", curie=DCAT.curie('distribution'),
                   model_uri=SAMTBUSKOLE.datasettdistribusjon, domain=None, range=Optional[Union[Union[str, DistribusjonId], list[Union[str, DistribusjonId]]]])

slots.eksempeldata = Slot(uri=ADMS.sample, name="eksempeldata", curie=ADMS.curie('sample'),
                   model_uri=SAMTBUSKOLE.eksempeldata, domain=None, range=Optional[Union[Union[str, DistribusjonId], list[Union[str, DistribusjonId]]]])

slots.tilgangstjeneste = Slot(uri=DCAT.accessService, name="tilgangstjeneste", curie=DCAT.curie('accessService'),
                   model_uri=SAMTBUSKOLE.tilgangstjeneste, domain=None, range=Optional[Union[Union[str, DatatjenesteId], list[Union[str, DatatjenesteId]]]])

slots.tilgjengeliggjor_datasett = Slot(uri=DCAT.servesDataset, name="tilgjengeliggjor_datasett", curie=DCAT.curie('servesDataset'),
                   model_uri=SAMTBUSKOLE.tilgjengeliggjor_datasett, domain=None, range=Optional[Union[Union[str, DatasettId], list[Union[str, DatasettId]]]])

slots.har_gebyr = Slot(uri=CV.hasCost, name="har_gebyr", curie=CV.curie('hasCost'),
                   model_uri=SAMTBUSKOLE.har_gebyr, domain=None, range=Optional[Union[Union[str, GebyrId], list[Union[str, GebyrId]]]])

slots.kilde_datasett = Slot(uri=DCT.source, name="kilde_datasett", curie=DCT.curie('source'),
                   model_uri=SAMTBUSKOLE.kilde_datasett, domain=None, range=Optional[Union[Union[str, DatasettId], list[Union[str, DatasettId]]]])

slots.i_serie = Slot(uri=DCAT.inSeries, name="i_serie", curie=DCAT.curie('inSeries'),
                   model_uri=SAMTBUSKOLE.i_serie, domain=None, range=Optional[Union[Union[str, DatasettserieId], list[Union[str, DatasettserieId]]]])

slots.siste = Slot(uri=DCAT.last, name="siste", curie=DCAT.curie('last'),
                   model_uri=SAMTBUSKOLE.siste, domain=None, range=Optional[Union[str, DatasettId]])

slots.forste = Slot(uri=DCAT.first, name="forste", curie=DCAT.curie('first'),
                   model_uri=SAMTBUSKOLE.forste, domain=None, range=Optional[Union[str, DatasettId]])

slots.relatert_regulativ_ressurs = Slot(uri=DCT.relation, name="relatert_regulativ_ressurs", curie=DCT.curie('relation'),
                   model_uri=SAMTBUSKOLE.relatert_regulativ_ressurs, domain=None, range=Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]])

slots.datasett = Slot(uri=DCAT.dataset, name="datasett", curie=DCAT.curie('dataset'),
                   model_uri=SAMTBUSKOLE.datasett, domain=None, range=Optional[Union[Union[str, DatasettId], list[Union[str, DatasettId]]]])

slots.datatjeneste = Slot(uri=DCAT.service, name="datatjeneste", curie=DCAT.curie('service'),
                   model_uri=SAMTBUSKOLE.datatjeneste, domain=None, range=Optional[Union[Union[str, DatatjenesteId], list[Union[str, DatatjenesteId]]]])

slots.har_del = Slot(uri=DCT.hasPart, name="har_del", curie=DCT.curie('hasPart'),
                   model_uri=SAMTBUSKOLE.har_del, domain=None, range=Optional[Union[Union[str, KatalogId], list[Union[str, KatalogId]]]])

slots.underkatalog = Slot(uri=DCAT.catalog, name="underkatalog", curie=DCAT.curie('catalog'),
                   model_uri=SAMTBUSKOLE.underkatalog, domain=None, range=Optional[Union[Union[str, KatalogId], list[Union[str, KatalogId]]]])

slots.katalogpost = Slot(uri=DCAT.record, name="katalogpost", curie=DCAT.curie('record'),
                   model_uri=SAMTBUSKOLE.katalogpost, domain=None, range=Optional[Union[Union[str, KatalogpostId], list[Union[str, KatalogpostId]]]])

slots.begynnelse = Slot(uri=TIME.hasBeginning, name="begynnelse", curie=TIME.curie('hasBeginning'),
                   model_uri=SAMTBUSKOLE.begynnelse, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.slutt = Slot(uri=TIME.hasEnd, name="slutt", curie=TIME.curie('hasEnd'),
                   model_uri=SAMTBUSKOLE.slutt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.har_kvalitetsmaaling = Slot(uri=DQV.hasQualityMeasurement, name="har_kvalitetsmaaling", curie=DQV.curie('hasQualityMeasurement'),
                   model_uri=SAMTBUSKOLE.har_kvalitetsmaaling, domain=None, range=Optional[Union[Union[str, KvalitetsmaalingId], list[Union[str, KvalitetsmaalingId]]]])

slots.er_deldimensjon_av = Slot(uri=SKOS.broader, name="er_deldimensjon_av", curie=SKOS.curie('broader'),
                   model_uri=SAMTBUSKOLE.er_deldimensjon_av, domain=None, range=Optional[Union[str, KvalitetsdimensjonId]])

slots.har_anbefalt_term = Slot(uri=SKOS.prefLabel, name="har_anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=SAMTBUSKOLE.har_anbefalt_term, domain=None, range=Optional[Union[str, list[str]]])

slots.har_definisjon = Slot(uri=SKOS.definition, name="har_definisjon", curie=SKOS.curie('definition'),
                   model_uri=SAMTBUSKOLE.har_definisjon, domain=None, range=Optional[Union[str, list[str]]])

slots.er_i_kvalitetsdeldimensjon = Slot(uri=DQVNO.inSubDimension, name="er_i_kvalitetsdeldimensjon", curie=DQVNO.curie('inSubDimension'),
                   model_uri=SAMTBUSKOLE.er_i_kvalitetsdeldimensjon, domain=None, range=Optional[Union[str, KvalitetsdeldimensjonId]])

slots.har_forventet_datatype = Slot(uri=DQV.expectedDataType, name="har_forventet_datatype", curie=DQV.curie('expectedDataType'),
                   model_uri=SAMTBUSKOLE.har_forventet_datatype, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.er_motivert_av = Slot(uri=OA.motivatedBy, name="er_motivert_av", curie=OA.curie('motivatedBy'),
                   model_uri=SAMTBUSKOLE.er_motivert_av, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.er_i_kvalitetsdimensjon = Slot(uri=DQV.inDimension, name="er_i_kvalitetsdimensjon", curie=DQV.curie('inDimension'),
                   model_uri=SAMTBUSKOLE.er_i_kvalitetsdimensjon, domain=None, range=Optional[Union[Union[str, KvalitetsdimensjonId], list[Union[str, KvalitetsdimensjonId]]]])

slots.har_tekstdel = Slot(uri=OA.hasBody, name="har_tekstdel", curie=OA.curie('hasBody'),
                   model_uri=SAMTBUSKOLE.har_tekstdel, domain=None, range=Optional[Union[str, TekstdelId]])

slots.har_maal = Slot(uri=OA.hasTarget, name="har_maal", curie=OA.curie('hasTarget'),
                   model_uri=SAMTBUSKOLE.har_maal, domain=None, range=Optional[Union[str, URI]])

slots.er_kvalitetsmaaling_av = Slot(uri=DQV.isMeasurementOf, name="er_kvalitetsmaaling_av", curie=DQV.curie('isMeasurementOf'),
                   model_uri=SAMTBUSKOLE.er_kvalitetsmaaling_av, domain=None, range=Optional[Union[str, KvalitetsmaalId]])

slots.har_verdi = Slot(uri=DQV.value, name="har_verdi", curie=DQV.curie('value'),
                   model_uri=SAMTBUSKOLE.har_verdi, domain=None, range=Optional[str])

slots.har_verdi_tekstdel = Slot(uri=RDFS.value, name="har_verdi_tekstdel", curie=RDFS.curie('value'),
                   model_uri=SAMTBUSKOLE.har_verdi_tekstdel, domain=None, range=Optional[str])

slots.id = Slot(uri=CAPNO.id, name="id", curie=CAPNO.curie('id'),
                   model_uri=SAMTBUSKOLE.id, domain=None, range=URIRef)

slots.tittel = Slot(uri=DCT.title, name="tittel", curie=DCT.curie('title'),
                   model_uri=SAMTBUSKOLE.tittel, domain=None, range=Optional[Union[str, list[str]]])

slots.beskrivelse = Slot(uri=DCT.description, name="beskrivelse", curie=DCT.curie('description'),
                   model_uri=SAMTBUSKOLE.beskrivelse, domain=None, range=Optional[Union[str, list[str]]])

slots.identifikator_literal = Slot(uri=DCT.identifier, name="identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=SAMTBUSKOLE.identifikator_literal, domain=None, range=Optional[str])

slots.type_concept = Slot(uri=DCT.type, name="type_concept", curie=DCT.curie('type'),
                   model_uri=SAMTBUSKOLE.type_concept, domain=None, range=Optional[Union[str, KonseptId]])

slots.endringsdato = Slot(uri=DCT.modified, name="endringsdato", curie=DCT.curie('modified'),
                   model_uri=SAMTBUSKOLE.endringsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.utgivelsesdato = Slot(uri=DCT.issued, name="utgivelsesdato", curie=DCT.curie('issued'),
                   model_uri=SAMTBUSKOLE.utgivelsesdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.spraak = Slot(uri=DCT.language, name="spraak", curie=DCT.curie('language'),
                   model_uri=SAMTBUSKOLE.spraak, domain=None, range=Optional[Union[str, list[str]]])

slots.format = Slot(uri=DCT.format, name="format", curie=DCT.curie('format'),
                   model_uri=SAMTBUSKOLE.format, domain=None, range=Optional[str])

slots.har_referanse = Slot(uri=RDFS.seeAlso, name="har_referanse", curie=RDFS.curie('seeAlso'),
                   model_uri=SAMTBUSKOLE.har_referanse, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.har_merknad = Slot(uri=RDFS.comment, name="har_merknad", curie=RDFS.curie('comment'),
                   model_uri=SAMTBUSKOLE.har_merknad, domain=None, range=Optional[Union[str, list[str]]])

slots.har_versjonsnummer = Slot(uri=OWL.versionInfo, name="har_versjonsnummer", curie=OWL.curie('versionInfo'),
                   model_uri=SAMTBUSKOLE.har_versjonsnummer, domain=None, range=Optional[str])

slots.nokkelord = Slot(uri=DCAT.keyword, name="nokkelord", curie=DCAT.curie('keyword'),
                   model_uri=SAMTBUSKOLE.nokkelord, domain=None, range=Optional[Union[str, list[str]]])

slots.dekningsomraade = Slot(uri=DCT.spatial, name="dekningsomraade", curie=DCT.curie('spatial'),
                   model_uri=SAMTBUSKOLE.dekningsomraade, domain=None, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.status = Slot(uri=ADMS.status, name="status", curie=ADMS.curie('status'),
                   model_uri=SAMTBUSKOLE.status, domain=None, range=Optional[Union[str, KonseptId]])

slots.valuta = Slot(uri=CV.currency, name="valuta", curie=CV.curie('currency'),
                   model_uri=SAMTBUSKOLE.valuta, domain=None, range=Optional[Union[str, KonseptId]])

slots.heimeside = Slot(uri=FOAF.homepage, name="heimeside", curie=FOAF.curie('homepage'),
                   model_uri=SAMTBUSKOLE.heimeside, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.anbefalt_term = Slot(uri=SKOS.prefLabel, name="anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=SAMTBUSKOLE.anbefalt_term, domain=None, range=Optional[Union[str, list[str]]])

slots.versjonsmerknad = Slot(uri=ADMS.versionNotes, name="versjonsmerknad", curie=ADMS.curie('versionNotes'),
                   model_uri=SAMTBUSKOLE.versjonsmerknad, domain=None, range=Optional[Union[str, list[str]]])

slots.samtBuContainer__kontaktpunkter = Slot(uri=SAMTBUSKOLE.kontaktpunkter, name="samtBuContainer__kontaktpunkter", curie=SAMTBUSKOLE.curie('kontaktpunkter'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__kontaktpunkter, domain=None, range=Optional[Union[dict[Union[str, KontaktopplysningId], Union[dict, Kontaktopplysning]], list[Union[dict, Kontaktopplysning]]]])

slots.samtBuContainer__utgivere = Slot(uri=SAMTBUSKOLE.utgivere, name="samtBuContainer__utgivere", curie=SAMTBUSKOLE.curie('utgivere'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__utgivere, domain=None, range=Optional[Union[dict[Union[str, AktorId], Union[dict, Aktor]], list[Union[dict, Aktor]]]])

slots.samtBuContainer__organisasjoner = Slot(uri=SAMTBUSKOLE.organisasjoner, name="samtBuContainer__organisasjoner", curie=SAMTBUSKOLE.curie('organisasjoner'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__organisasjoner, domain=None, range=Optional[Union[dict[Union[str, AktorId], Union[dict, Aktor]], list[Union[dict, Aktor]]]])

slots.samtBuContainer__gjeldende_lovgivninger = Slot(uri=SAMTBUSKOLE.gjeldende_lovgivninger, name="samtBuContainer__gjeldende_lovgivninger", curie=SAMTBUSKOLE.curie('gjeldende_lovgivninger'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__gjeldende_lovgivninger, domain=None, range=Optional[Union[dict[Union[str, RegulativRessursId], Union[dict, RegulativRessurs]], list[Union[dict, RegulativRessurs]]]])

slots.samtBuContainer__datasettdistribusjoner = Slot(uri=SAMTBUSKOLE.datasettdistribusjoner, name="samtBuContainer__datasettdistribusjoner", curie=SAMTBUSKOLE.curie('datasettdistribusjoner'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__datasettdistribusjoner, domain=None, range=Optional[Union[dict[Union[str, DistribusjonId], Union[dict, Distribusjon]], list[Union[dict, Distribusjon]]]])

slots.samtBuContainer__dataset_metadata = Slot(uri=SAMTBUSKOLE.dataset_metadata, name="samtBuContainer__dataset_metadata", curie=SAMTBUSKOLE.curie('dataset_metadata'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__dataset_metadata, domain=None, range=Optional[Union[dict[Union[str, DatasettId], Union[dict, Datasett]], list[Union[dict, Datasett]]]])

slots.samtBuContainer__kvalitetsmerknader = Slot(uri=SAMTBUSKOLE.kvalitetsmerknader, name="samtBuContainer__kvalitetsmerknader", curie=SAMTBUSKOLE.curie('kvalitetsmerknader'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__kvalitetsmerknader, domain=None, range=Optional[Union[dict[Union[str, KvalitetsmerknadId], Union[dict, Kvalitetsmerknad]], list[Union[dict, Kvalitetsmerknad]]]])

slots.samtBuContainer__brukertilbakemeldinger = Slot(uri=SAMTBUSKOLE.brukertilbakemeldinger, name="samtBuContainer__brukertilbakemeldinger", curie=SAMTBUSKOLE.curie('brukertilbakemeldinger'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__brukertilbakemeldinger, domain=None, range=Optional[Union[dict[Union[str, BrukartilbakemeldingId], Union[dict, Brukartilbakemelding]], list[Union[dict, Brukartilbakemelding]]]])

slots.samtBuContainer__kvalitetsmaalinger = Slot(uri=SAMTBUSKOLE.kvalitetsmaalinger, name="samtBuContainer__kvalitetsmaalinger", curie=SAMTBUSKOLE.curie('kvalitetsmaalinger'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__kvalitetsmaalinger, domain=None, range=Optional[Union[dict[Union[str, KvalitetsmaalingId], Union[dict, Kvalitetsmaaling]], list[Union[dict, Kvalitetsmaaling]]]])

slots.samtBuContainer__grupper = Slot(uri=SAMTBUSKOLE.grupper, name="samtBuContainer__grupper", curie=SAMTBUSKOLE.curie('grupper'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__grupper, domain=None, range=Optional[Union[dict[Union[str, AktorId], Union[dict, Aktor]], list[Union[dict, Aktor]]]])

slots.samtBuContainer__standarder = Slot(uri=SAMTBUSKOLE.standarder, name="samtBuContainer__standarder", curie=SAMTBUSKOLE.curie('standarder'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__standarder, domain=None, range=Optional[Union[dict[Union[str, StandardId], Union[dict, Standard]], list[Union[dict, Standard]]]])

slots.samtBuContainer__kvalitetsdimensjoner = Slot(uri=SAMTBUSKOLE.kvalitetsdimensjoner, name="samtBuContainer__kvalitetsdimensjoner", curie=SAMTBUSKOLE.curie('kvalitetsdimensjoner'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__kvalitetsdimensjoner, domain=None, range=Optional[Union[dict[Union[str, KvalitetsdimensjonId], Union[dict, Kvalitetsdimensjon]], list[Union[dict, Kvalitetsdimensjon]]]])

slots.samtBuContainer__tidsromer = Slot(uri=SAMTBUSKOLE.tidsromer, name="samtBuContainer__tidsromer", curie=SAMTBUSKOLE.curie('tidsromer'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__tidsromer, domain=None, range=Optional[Union[dict[Union[str, TidsromId], Union[dict, Tidsrom]], list[Union[dict, Tidsrom]]]])

slots.samtBuContainer__tekstdeler = Slot(uri=SAMTBUSKOLE.tekstdeler, name="samtBuContainer__tekstdeler", curie=SAMTBUSKOLE.curie('tekstdeler'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__tekstdeler, domain=None, range=Optional[Union[dict[Union[str, TekstdelId], Union[dict, Tekstdel]], list[Union[dict, Tekstdel]]]])

slots.samtBuContainer__id = Slot(uri=SAMTBUSKOLE.id, name="samtBuContainer__id", curie=SAMTBUSKOLE.curie('id'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__id, domain=None, range=Optional[str])

slots.samtBuContainer__skoler = Slot(uri=SAMTBUSKOLE.skoler, name="samtBuContainer__skoler", curie=SAMTBUSKOLE.curie('skoler'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__skoler, domain=None, range=Optional[Union[dict[Union[str, SkoleId], Union[dict, Skole]], list[Union[dict, Skole]]]])

slots.samtBuContainer__kommuner = Slot(uri=SAMTBUSKOLE.kommuner, name="samtBuContainer__kommuner", curie=SAMTBUSKOLE.curie('kommuner'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__kommuner, domain=None, range=Optional[Union[dict[Union[str, KommuneId], Union[dict, Kommune]], list[Union[dict, Kommune]]]])

slots.samtBuContainer__fylker = Slot(uri=SAMTBUSKOLE.fylker, name="samtBuContainer__fylker", curie=SAMTBUSKOLE.curie('fylker'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__fylker, domain=None, range=Optional[Union[dict[Union[str, FylkeId], Union[dict, Fylke]], list[Union[dict, Fylke]]]])

slots.samtBuContainer__private_virksomheter = Slot(uri=SAMTBUSKOLE.private_virksomheter, name="samtBuContainer__private_virksomheter", curie=SAMTBUSKOLE.curie('private_virksomheter'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__private_virksomheter, domain=None, range=Optional[Union[dict[Union[str, PrivatVirksomhetId], Union[dict, PrivatVirksomhet]], list[Union[dict, PrivatVirksomhet]]]])

slots.samtBuContainer__basisgrupper = Slot(uri=SAMTBUSKOLE.basisgrupper, name="samtBuContainer__basisgrupper", curie=SAMTBUSKOLE.curie('basisgrupper'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__basisgrupper, domain=None, range=Optional[Union[dict[Union[str, BasisgruppeId], Union[dict, Basisgruppe]], list[Union[dict, Basisgruppe]]]])

slots.samtBuContainer__elever = Slot(uri=SAMTBUSKOLE.elever, name="samtBuContainer__elever", curie=SAMTBUSKOLE.curie('elever'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__elever, domain=None, range=Optional[Union[dict[Union[str, ElevId], Union[dict, Elev]], list[Union[dict, Elev]]]])

slots.samtBuContainer__rektorer = Slot(uri=SAMTBUSKOLE.rektorer, name="samtBuContainer__rektorer", curie=SAMTBUSKOLE.curie('rektorer'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__rektorer, domain=None, range=Optional[Union[dict[Union[str, RektorId], Union[dict, Rektor]], list[Union[dict, Rektor]]]])

slots.samtBuContainer__kontaktlaerere = Slot(uri=SAMTBUSKOLE.kontaktlaerere, name="samtBuContainer__kontaktlaerere", curie=SAMTBUSKOLE.curie('kontaktlaerere'),
                   model_uri=SAMTBUSKOLE.samtBuContainer__kontaktlaerere, domain=None, range=Optional[Union[dict[Union[str, KontaktlaererId], Union[dict, Kontaktlaerer]], list[Union[dict, Kontaktlaerer]]]])

slots.Aktor_navn_aktor = Slot(uri=FOAF.name, name="Aktor_navn_aktor", curie=FOAF.curie('name'),
                   model_uri=SAMTBUSKOLE.Aktor_navn_aktor, domain=Aktor, range=Union[str, list[str]])

slots.Kontaktopplysning_navn_vcard = Slot(uri=VCARD.fn, name="Kontaktopplysning_navn_vcard", curie=VCARD.curie('fn'),
                   model_uri=SAMTBUSKOLE.Kontaktopplysning_navn_vcard, domain=Kontaktopplysning, range=Union[str, list[str]])

slots.Identifikator_notasjon = Slot(uri=SKOS.notation, name="Identifikator_notasjon", curie=SKOS.curie('notation'),
                   model_uri=SAMTBUSKOLE.Identifikator_notasjon, domain=Identifikator, range=str)

slots.Sjekksum_algoritme = Slot(uri=SPDX.algorithm, name="Sjekksum_algoritme", curie=SPDX.curie('algorithm'),
                   model_uri=SAMTBUSKOLE.Sjekksum_algoritme, domain=Sjekksum, range=str)

slots.Sjekksum_sjekksumverdi = Slot(uri=SPDX.checksumValue, name="Sjekksum_sjekksumverdi", curie=SPDX.curie('checksumValue'),
                   model_uri=SAMTBUSKOLE.Sjekksum_sjekksumverdi, domain=Sjekksum, range=str)

slots.Relasjon_har_rolle = Slot(uri=DCAT.hadRole, name="Relasjon_har_rolle", curie=DCAT.curie('hadRole'),
                   model_uri=SAMTBUSKOLE.Relasjon_har_rolle, domain=Relasjon, range=str)

slots.Relasjon_relasjon_til = Slot(uri=DCT.relation, name="Relasjon_relasjon_til", curie=DCT.curie('relation'),
                   model_uri=SAMTBUSKOLE.Relasjon_relasjon_til, domain=Relasjon, range=Union[str, URI])

slots.Distribusjon_tilgangs_url = Slot(uri=DCAT.accessURL, name="Distribusjon_tilgangs_url", curie=DCAT.curie('accessURL'),
                   model_uri=SAMTBUSKOLE.Distribusjon_tilgangs_url, domain=Distribusjon, range=Union[Union[str, URI], list[Union[str, URI]]])

slots.Distribusjon_beskrivelse = Slot(uri=DCT.description, name="Distribusjon_beskrivelse", curie=DCT.curie('description'),
                   model_uri=SAMTBUSKOLE.Distribusjon_beskrivelse, domain=Distribusjon, range=Optional[Union[str, list[str]]])

slots.Distribusjon_format = Slot(uri=DCT.format, name="Distribusjon_format", curie=DCT.curie('format'),
                   model_uri=SAMTBUSKOLE.Distribusjon_format, domain=Distribusjon, range=Optional[str])

slots.Distribusjon_lisens = Slot(uri=DCT.license, name="Distribusjon_lisens", curie=DCT.curie('license'),
                   model_uri=SAMTBUSKOLE.Distribusjon_lisens, domain=Distribusjon, range=Optional[str])

slots.Distribusjon_status = Slot(uri=ADMS.status, name="Distribusjon_status", curie=ADMS.curie('status'),
                   model_uri=SAMTBUSKOLE.Distribusjon_status, domain=Distribusjon, range=Optional[Union[str, KonseptId]])

slots.Distribusjon_tilgjengelighet = Slot(uri=DCATAP.availability, name="Distribusjon_tilgjengelighet", curie=DCATAP.curie('availability'),
                   model_uri=SAMTBUSKOLE.Distribusjon_tilgjengelighet, domain=Distribusjon, range=Optional[str])

slots.Datasett_har_kvalitetsmerknad = Slot(uri=DQV.hasQualityAnnotation, name="Datasett_har_kvalitetsmerknad", curie=DQV.curie('hasQualityAnnotation'),
                   model_uri=SAMTBUSKOLE.Datasett_har_kvalitetsmerknad, domain=Datasett, range=Optional[Union[Union[str, KvalitetsmerknadId], list[Union[str, KvalitetsmerknadId]]]])

slots.Datasett_har_kvalitetsmaaling = Slot(uri=DQV.hasQualityMeasurement, name="Datasett_har_kvalitetsmaaling", curie=DQV.curie('hasQualityMeasurement'),
                   model_uri=SAMTBUSKOLE.Datasett_har_kvalitetsmaaling, domain=Datasett, range=Optional[Union[Union[str, KvalitetsmaalingId], list[Union[str, KvalitetsmaalingId]]]])

slots.Datasett_beskrivelse = Slot(uri=DCT.description, name="Datasett_beskrivelse", curie=DCT.curie('description'),
                   model_uri=SAMTBUSKOLE.Datasett_beskrivelse, domain=Datasett, range=Union[str, list[str]])

slots.Datasett_kontaktpunkt = Slot(uri=DCAT.contactPoint, name="Datasett_kontaktpunkt", curie=DCAT.curie('contactPoint'),
                   model_uri=SAMTBUSKOLE.Datasett_kontaktpunkt, domain=Datasett, range=Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]])

slots.Datasett_tema = Slot(uri=DCAT.theme, name="Datasett_tema", curie=DCAT.curie('theme'),
                   model_uri=SAMTBUSKOLE.Datasett_tema, domain=Datasett, range=Union[str, list[str]])

slots.Datasett_tittel = Slot(uri=DCT.title, name="Datasett_tittel", curie=DCT.curie('title'),
                   model_uri=SAMTBUSKOLE.Datasett_tittel, domain=Datasett, range=Union[str, list[str]])

slots.Datasett_utgiver = Slot(uri=DCT.publisher, name="Datasett_utgiver", curie=DCT.curie('publisher'),
                   model_uri=SAMTBUSKOLE.Datasett_utgiver, domain=Datasett, range=Union[str, AktorId])

slots.Datasett_begrep = Slot(uri=DCT.subject, name="Datasett_begrep", curie=DCT.curie('subject'),
                   model_uri=SAMTBUSKOLE.Datasett_begrep, domain=Datasett, range=Optional[Union[str, list[str]]])

slots.Datasett_ble_generert_ved = Slot(uri=PROV.wasGeneratedBy, name="Datasett_ble_generert_ved", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=SAMTBUSKOLE.Datasett_ble_generert_ved, domain=Datasett, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Datasett_datasettdistribusjon = Slot(uri=DCAT.distribution, name="Datasett_datasettdistribusjon", curie=DCAT.curie('distribution'),
                   model_uri=SAMTBUSKOLE.Datasett_datasettdistribusjon, domain=Datasett, range=Optional[Union[Union[str, DistribusjonId], list[Union[str, DistribusjonId]]]])

slots.Datasett_dekningsomraade = Slot(uri=DCT.spatial, name="Datasett_dekningsomraade", curie=DCT.curie('spatial'),
                   model_uri=SAMTBUSKOLE.Datasett_dekningsomraade, domain=Datasett, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Datasett_gjeldende_lovgivning = Slot(uri=DCATAP.applicableLegislation, name="Datasett_gjeldende_lovgivning", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=SAMTBUSKOLE.Datasett_gjeldende_lovgivning, domain=Datasett, range=Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]])

slots.Datasett_nokkelord = Slot(uri=DCAT.keyword, name="Datasett_nokkelord", curie=DCAT.curie('keyword'),
                   model_uri=SAMTBUSKOLE.Datasett_nokkelord, domain=Datasett, range=Optional[Union[str, list[str]]])

slots.Datasett_tidsrom = Slot(uri=DCT.temporal, name="Datasett_tidsrom", curie=DCT.curie('temporal'),
                   model_uri=SAMTBUSKOLE.Datasett_tidsrom, domain=Datasett, range=Optional[Union[Union[str, TidsromId], list[Union[str, TidsromId]]]])

slots.Datasett_tilgangsrettigheter = Slot(uri=DCT.accessRights, name="Datasett_tilgangsrettigheter", curie=DCT.curie('accessRights'),
                   model_uri=SAMTBUSKOLE.Datasett_tilgangsrettigheter, domain=Datasett, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Datasettserie_beskrivelse = Slot(uri=DCT.description, name="Datasettserie_beskrivelse", curie=DCT.curie('description'),
                   model_uri=SAMTBUSKOLE.Datasettserie_beskrivelse, domain=Datasettserie, range=Union[str, list[str]])

slots.Datasettserie_kontaktpunkt = Slot(uri=DCAT.contactPoint, name="Datasettserie_kontaktpunkt", curie=DCAT.curie('contactPoint'),
                   model_uri=SAMTBUSKOLE.Datasettserie_kontaktpunkt, domain=Datasettserie, range=Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]])

slots.Datasettserie_tema = Slot(uri=DCAT.theme, name="Datasettserie_tema", curie=DCAT.curie('theme'),
                   model_uri=SAMTBUSKOLE.Datasettserie_tema, domain=Datasettserie, range=Union[str, list[str]])

slots.Datasettserie_tittel = Slot(uri=DCT.title, name="Datasettserie_tittel", curie=DCT.curie('title'),
                   model_uri=SAMTBUSKOLE.Datasettserie_tittel, domain=Datasettserie, range=Union[str, list[str]])

slots.Datasettserie_utgiver = Slot(uri=DCT.publisher, name="Datasettserie_utgiver", curie=DCT.curie('publisher'),
                   model_uri=SAMTBUSKOLE.Datasettserie_utgiver, domain=Datasettserie, range=Union[str, AktorId])

slots.Datasettserie_dekningsomraade = Slot(uri=DCT.spatial, name="Datasettserie_dekningsomraade", curie=DCT.curie('spatial'),
                   model_uri=SAMTBUSKOLE.Datasettserie_dekningsomraade, domain=Datasettserie, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Datasettserie_gjeldende_lovgivning = Slot(uri=DCATAP.applicableLegislation, name="Datasettserie_gjeldende_lovgivning", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=SAMTBUSKOLE.Datasettserie_gjeldende_lovgivning, domain=Datasettserie, range=Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]])

slots.Datasettserie_siste = Slot(uri=DCAT.last, name="Datasettserie_siste", curie=DCAT.curie('last'),
                   model_uri=SAMTBUSKOLE.Datasettserie_siste, domain=Datasettserie, range=Optional[Union[str, DatasettId]])

slots.Datasettserie_tidsrom = Slot(uri=DCT.temporal, name="Datasettserie_tidsrom", curie=DCT.curie('temporal'),
                   model_uri=SAMTBUSKOLE.Datasettserie_tidsrom, domain=Datasettserie, range=Optional[Union[Union[str, TidsromId], list[Union[str, TidsromId]]]])

slots.Datatjeneste_endepunkts_url = Slot(uri=DCAT.endpointURL, name="Datatjeneste_endepunkts_url", curie=DCAT.curie('endpointURL'),
                   model_uri=SAMTBUSKOLE.Datatjeneste_endepunkts_url, domain=Datatjeneste, range=Union[Union[str, URI], list[Union[str, URI]]])

slots.Datatjeneste_kontaktpunkt = Slot(uri=DCAT.contactPoint, name="Datatjeneste_kontaktpunkt", curie=DCAT.curie('contactPoint'),
                   model_uri=SAMTBUSKOLE.Datatjeneste_kontaktpunkt, domain=Datatjeneste, range=Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]])

slots.Datatjeneste_tittel = Slot(uri=DCT.title, name="Datatjeneste_tittel", curie=DCT.curie('title'),
                   model_uri=SAMTBUSKOLE.Datatjeneste_tittel, domain=Datatjeneste, range=Union[str, list[str]])

slots.Datatjeneste_utgiver = Slot(uri=DCT.publisher, name="Datatjeneste_utgiver", curie=DCT.curie('publisher'),
                   model_uri=SAMTBUSKOLE.Datatjeneste_utgiver, domain=Datatjeneste, range=Union[str, AktorId])

slots.Datatjeneste_endepunktsbeskrivelse = Slot(uri=DCAT.endpointDescription, name="Datatjeneste_endepunktsbeskrivelse", curie=DCAT.curie('endpointDescription'),
                   model_uri=SAMTBUSKOLE.Datatjeneste_endepunktsbeskrivelse, domain=Datatjeneste, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Datatjeneste_format = Slot(uri=DCT.format, name="Datatjeneste_format", curie=DCT.curie('format'),
                   model_uri=SAMTBUSKOLE.Datatjeneste_format, domain=Datatjeneste, range=Optional[str])

slots.Datatjeneste_gjeldende_lovgivning = Slot(uri=DCATAP.applicableLegislation, name="Datatjeneste_gjeldende_lovgivning", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=SAMTBUSKOLE.Datatjeneste_gjeldende_lovgivning, domain=Datatjeneste, range=Optional[Union[Union[str, RegulativRessursId], list[Union[str, RegulativRessursId]]]])

slots.Datatjeneste_i_samsvar_med = Slot(uri=DCT.conformsTo, name="Datatjeneste_i_samsvar_med", curie=DCT.curie('conformsTo'),
                   model_uri=SAMTBUSKOLE.Datatjeneste_i_samsvar_med, domain=Datatjeneste, range=Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]])

slots.Datatjeneste_nokkelord = Slot(uri=DCAT.keyword, name="Datatjeneste_nokkelord", curie=DCAT.curie('keyword'),
                   model_uri=SAMTBUSKOLE.Datatjeneste_nokkelord, domain=Datatjeneste, range=Optional[Union[str, list[str]]])

slots.Datatjeneste_tema = Slot(uri=DCAT.theme, name="Datatjeneste_tema", curie=DCAT.curie('theme'),
                   model_uri=SAMTBUSKOLE.Datatjeneste_tema, domain=Datatjeneste, range=Optional[Union[str, list[str]]])

slots.Datatjeneste_tilgjengeliggjor_datasett = Slot(uri=DCAT.servesDataset, name="Datatjeneste_tilgjengeliggjor_datasett", curie=DCAT.curie('servesDataset'),
                   model_uri=SAMTBUSKOLE.Datatjeneste_tilgjengeliggjor_datasett, domain=Datatjeneste, range=Optional[Union[Union[str, DatasettId], list[Union[str, DatasettId]]]])

slots.Datatjeneste_tilgjengelighet = Slot(uri=DCATAP.availability, name="Datatjeneste_tilgjengelighet", curie=DCATAP.curie('availability'),
                   model_uri=SAMTBUSKOLE.Datatjeneste_tilgjengelighet, domain=Datatjeneste, range=Optional[str])

slots.Katalogpost_endringsdato = Slot(uri=DCT.modified, name="Katalogpost_endringsdato", curie=DCT.curie('modified'),
                   model_uri=SAMTBUSKOLE.Katalogpost_endringsdato, domain=Katalogpost, range=Union[str, XSDDate])

slots.Katalogpost_primaertema = Slot(uri=FOAF.primaryTopic, name="Katalogpost_primaertema", curie=FOAF.curie('primaryTopic'),
                   model_uri=SAMTBUSKOLE.Katalogpost_primaertema, domain=Katalogpost, range=Union[str, KatalogisertRessursId])

slots.Katalogpost_i_samsvar_med = Slot(uri=DCT.conformsTo, name="Katalogpost_i_samsvar_med", curie=DCT.curie('conformsTo'),
                   model_uri=SAMTBUSKOLE.Katalogpost_i_samsvar_med, domain=Katalogpost, range=Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]])

slots.Katalogpost_status = Slot(uri=ADMS.status, name="Katalogpost_status", curie=ADMS.curie('status'),
                   model_uri=SAMTBUSKOLE.Katalogpost_status, domain=Katalogpost, range=Optional[Union[str, KonseptId]])

slots.Katalogpost_utgivelsesdato = Slot(uri=DCT.issued, name="Katalogpost_utgivelsesdato", curie=DCT.curie('issued'),
                   model_uri=SAMTBUSKOLE.Katalogpost_utgivelsesdato, domain=Katalogpost, range=Optional[Union[str, XSDDate]])

slots.Katalog_beskrivelse = Slot(uri=DCT.description, name="Katalog_beskrivelse", curie=DCT.curie('description'),
                   model_uri=SAMTBUSKOLE.Katalog_beskrivelse, domain=Katalog, range=Union[str, list[str]])

slots.Katalog_kontaktpunkt = Slot(uri=DCAT.contactPoint, name="Katalog_kontaktpunkt", curie=DCAT.curie('contactPoint'),
                   model_uri=SAMTBUSKOLE.Katalog_kontaktpunkt, domain=Katalog, range=Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]])

slots.Katalog_tittel = Slot(uri=DCT.title, name="Katalog_tittel", curie=DCT.curie('title'),
                   model_uri=SAMTBUSKOLE.Katalog_tittel, domain=Katalog, range=Union[str, list[str]])

slots.Katalog_utgiver = Slot(uri=DCT.publisher, name="Katalog_utgiver", curie=DCT.curie('publisher'),
                   model_uri=SAMTBUSKOLE.Katalog_utgiver, domain=Katalog, range=Union[str, AktorId])

slots.Katalog_datasett = Slot(uri=DCAT.dataset, name="Katalog_datasett", curie=DCAT.curie('dataset'),
                   model_uri=SAMTBUSKOLE.Katalog_datasett, domain=Katalog, range=Optional[Union[Union[str, DatasettId], list[Union[str, DatasettId]]]])

slots.Katalog_datatjeneste = Slot(uri=DCAT.service, name="Katalog_datatjeneste", curie=DCAT.curie('service'),
                   model_uri=SAMTBUSKOLE.Katalog_datatjeneste, domain=Katalog, range=Optional[Union[Union[str, DatatjenesteId], list[Union[str, DatatjenesteId]]]])

slots.Katalog_dekningsomraade = Slot(uri=DCT.spatial, name="Katalog_dekningsomraade", curie=DCT.curie('spatial'),
                   model_uri=SAMTBUSKOLE.Katalog_dekningsomraade, domain=Katalog, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Katalog_endringsdato = Slot(uri=DCT.modified, name="Katalog_endringsdato", curie=DCT.curie('modified'),
                   model_uri=SAMTBUSKOLE.Katalog_endringsdato, domain=Katalog, range=Optional[Union[str, XSDDate]])

slots.Katalog_heimeside = Slot(uri=FOAF.homepage, name="Katalog_heimeside", curie=FOAF.curie('homepage'),
                   model_uri=SAMTBUSKOLE.Katalog_heimeside, domain=Katalog, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Katalog_lisens = Slot(uri=DCT.license, name="Katalog_lisens", curie=DCT.curie('license'),
                   model_uri=SAMTBUSKOLE.Katalog_lisens, domain=Katalog, range=Optional[str])

slots.Katalog_spraak = Slot(uri=DCT.language, name="Katalog_spraak", curie=DCT.curie('language'),
                   model_uri=SAMTBUSKOLE.Katalog_spraak, domain=Katalog, range=Optional[Union[str, list[str]]])

slots.Katalog_temaer = Slot(uri=DCAT.themeTaxonomy, name="Katalog_temaer", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=SAMTBUSKOLE.Katalog_temaer, domain=Katalog, range=Optional[Union[Union[str, BegrepssamlingId], list[Union[str, BegrepssamlingId]]]])

slots.Katalog_utgivelsesdato = Slot(uri=DCT.issued, name="Katalog_utgivelsesdato", curie=DCT.curie('issued'),
                   model_uri=SAMTBUSKOLE.Katalog_utgivelsesdato, domain=Katalog, range=Optional[Union[str, XSDDate]])

slots.Kvalitetsdimensjon_har_anbefalt_term = Slot(uri=SKOS.prefLabel, name="Kvalitetsdimensjon_har_anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=SAMTBUSKOLE.Kvalitetsdimensjon_har_anbefalt_term, domain=Kvalitetsdimensjon, range=Optional[Union[str, list[str]]])

slots.Kvalitetsdimensjon_har_definisjon = Slot(uri=SKOS.definition, name="Kvalitetsdimensjon_har_definisjon", curie=SKOS.curie('definition'),
                   model_uri=SAMTBUSKOLE.Kvalitetsdimensjon_har_definisjon, domain=Kvalitetsdimensjon, range=Optional[Union[str, list[str]]])

slots.Kvalitetsdeldimensjon_er_deldimensjon_av = Slot(uri=SKOS.broader, name="Kvalitetsdeldimensjon_er_deldimensjon_av", curie=SKOS.curie('broader'),
                   model_uri=SAMTBUSKOLE.Kvalitetsdeldimensjon_er_deldimensjon_av, domain=Kvalitetsdeldimensjon, range=Union[str, KvalitetsdimensjonId])

slots.Kvalitetsdeldimensjon_har_anbefalt_term = Slot(uri=SKOS.prefLabel, name="Kvalitetsdeldimensjon_har_anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=SAMTBUSKOLE.Kvalitetsdeldimensjon_har_anbefalt_term, domain=Kvalitetsdeldimensjon, range=Optional[Union[str, list[str]]])

slots.Kvalitetsdeldimensjon_har_definisjon = Slot(uri=SKOS.definition, name="Kvalitetsdeldimensjon_har_definisjon", curie=SKOS.curie('definition'),
                   model_uri=SAMTBUSKOLE.Kvalitetsdeldimensjon_har_definisjon, domain=Kvalitetsdeldimensjon, range=Optional[Union[str, list[str]]])

slots.Kvalitetsmaal_er_i_kvalitetsdeldimensjon = Slot(uri=DQVNO.inSubDimension, name="Kvalitetsmaal_er_i_kvalitetsdeldimensjon", curie=DQVNO.curie('inSubDimension'),
                   model_uri=SAMTBUSKOLE.Kvalitetsmaal_er_i_kvalitetsdeldimensjon, domain=Kvalitetsmaal, range=Union[str, KvalitetsdeldimensjonId])

slots.Kvalitetsmaal_har_forventet_datatype = Slot(uri=DQV.expectedDataType, name="Kvalitetsmaal_har_forventet_datatype", curie=DQV.curie('expectedDataType'),
                   model_uri=SAMTBUSKOLE.Kvalitetsmaal_har_forventet_datatype, domain=Kvalitetsmaal, range=Optional[Union[str, URIorCURIE]])

slots.Kvalitetsmaal_har_anbefalt_term = Slot(uri=SKOS.prefLabel, name="Kvalitetsmaal_har_anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=SAMTBUSKOLE.Kvalitetsmaal_har_anbefalt_term, domain=Kvalitetsmaal, range=Optional[Union[str, list[str]]])

slots.Kvalitetsmaal_har_definisjon = Slot(uri=SKOS.definition, name="Kvalitetsmaal_har_definisjon", curie=SKOS.curie('definition'),
                   model_uri=SAMTBUSKOLE.Kvalitetsmaal_har_definisjon, domain=Kvalitetsmaal, range=Optional[Union[str, list[str]]])

slots.Kvalitetsmerknad_er_motivert_av = Slot(uri=OA.motivatedBy, name="Kvalitetsmerknad_er_motivert_av", curie=OA.curie('motivatedBy'),
                   model_uri=SAMTBUSKOLE.Kvalitetsmerknad_er_motivert_av, domain=Kvalitetsmerknad, range=Union[str, URIorCURIE])

slots.Kvalitetsmerknad_er_i_kvalitetsdimensjon = Slot(uri=DQV.inDimension, name="Kvalitetsmerknad_er_i_kvalitetsdimensjon", curie=DQV.curie('inDimension'),
                   model_uri=SAMTBUSKOLE.Kvalitetsmerknad_er_i_kvalitetsdimensjon, domain=Kvalitetsmerknad, range=Optional[Union[Union[str, KvalitetsdimensjonId], list[Union[str, KvalitetsdimensjonId]]]])

slots.Kvalitetsmerknad_har_tekstdel = Slot(uri=OA.hasBody, name="Kvalitetsmerknad_har_tekstdel", curie=OA.curie('hasBody'),
                   model_uri=SAMTBUSKOLE.Kvalitetsmerknad_har_tekstdel, domain=Kvalitetsmerknad, range=Optional[Union[str, TekstdelId]])

slots.Kvalitetsmerknad_har_merknad = Slot(uri=RDFS.comment, name="Kvalitetsmerknad_har_merknad", curie=RDFS.curie('comment'),
                   model_uri=SAMTBUSKOLE.Kvalitetsmerknad_har_merknad, domain=Kvalitetsmerknad, range=Optional[Union[str, list[str]]])

slots.Kvalitetsmerknad_har_maal = Slot(uri=OA.hasTarget, name="Kvalitetsmerknad_har_maal", curie=OA.curie('hasTarget'),
                   model_uri=SAMTBUSKOLE.Kvalitetsmerknad_har_maal, domain=Kvalitetsmerknad, range=Optional[Union[str, URI]])

slots.Kvalitetsmaaling_er_kvalitetsmaaling_av = Slot(uri=DQV.isMeasurementOf, name="Kvalitetsmaaling_er_kvalitetsmaaling_av", curie=DQV.curie('isMeasurementOf'),
                   model_uri=SAMTBUSKOLE.Kvalitetsmaaling_er_kvalitetsmaaling_av, domain=Kvalitetsmaaling, range=Union[str, KvalitetsmaalId])

slots.Kvalitetsmaaling_har_verdi = Slot(uri=DQV.value, name="Kvalitetsmaaling_har_verdi", curie=DQV.curie('value'),
                   model_uri=SAMTBUSKOLE.Kvalitetsmaaling_har_verdi, domain=Kvalitetsmaaling, range=Optional[str])

slots.Kvalitetsmaaling_har_merknad = Slot(uri=RDFS.comment, name="Kvalitetsmaaling_har_merknad", curie=RDFS.curie('comment'),
                   model_uri=SAMTBUSKOLE.Kvalitetsmaaling_har_merknad, domain=Kvalitetsmaaling, range=Optional[Union[str, list[str]]])

slots.Standard_tittel = Slot(uri=DCT.title, name="Standard_tittel", curie=DCT.curie('title'),
                   model_uri=SAMTBUSKOLE.Standard_tittel, domain=Standard, range=Union[str, list[str]])

slots.Standard_er_i_kvalitetsdimensjon = Slot(uri=DQV.inDimension, name="Standard_er_i_kvalitetsdimensjon", curie=DQV.curie('inDimension'),
                   model_uri=SAMTBUSKOLE.Standard_er_i_kvalitetsdimensjon, domain=Standard, range=Optional[Union[Union[str, KvalitetsdimensjonId], list[Union[str, KvalitetsdimensjonId]]]])

slots.Standard_har_referanse = Slot(uri=RDFS.seeAlso, name="Standard_har_referanse", curie=RDFS.curie('seeAlso'),
                   model_uri=SAMTBUSKOLE.Standard_har_referanse, domain=Standard, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Standard_har_merknad = Slot(uri=RDFS.comment, name="Standard_har_merknad", curie=RDFS.curie('comment'),
                   model_uri=SAMTBUSKOLE.Standard_har_merknad, domain=Standard, range=Optional[Union[str, list[str]]])

slots.Standard_har_versjonsnummer = Slot(uri=OWL.versionInfo, name="Standard_har_versjonsnummer", curie=OWL.curie('versionInfo'),
                   model_uri=SAMTBUSKOLE.Standard_har_versjonsnummer, domain=Standard, range=Optional[str])

slots.Tekstdel_har_verdi_tekstdel = Slot(uri=RDFS.value, name="Tekstdel_har_verdi_tekstdel", curie=RDFS.curie('value'),
                   model_uri=SAMTBUSKOLE.Tekstdel_har_verdi_tekstdel, domain=Tekstdel, range=str)

slots.Tekstdel_format = Slot(uri=DCT.format, name="Tekstdel_format", curie=DCT.curie('format'),
                   model_uri=SAMTBUSKOLE.Tekstdel_format, domain=Tekstdel, range=Optional[str])

slots.Tekstdel_spraak = Slot(uri=DCT.language, name="Tekstdel_spraak", curie=DCT.curie('language'),
                   model_uri=SAMTBUSKOLE.Tekstdel_spraak, domain=Tekstdel, range=Optional[Union[str, list[str]]])

