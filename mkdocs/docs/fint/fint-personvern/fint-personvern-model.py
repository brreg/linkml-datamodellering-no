# Auto generated from fint-personvern-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-05T13:28:04
# Schema: fint-personvern
#
# id: https://data.norge.no/linkml/fint-personvern
# description: FINT-domenemodell for personvern. Dekkjer behandling av personopplysningar, samtykke, tenester og kodeverk for behandlingsgrunnlag og personopplysningstypar.
#
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

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.7.0"
version = "4.0.20"

# Namespaces
FINT = CurieNamespace('fint', 'https://schema.fintlabs.no/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PVN = CurieNamespace('pvn', 'https://schema.fintlabs.no/personvern/')
DEFAULT_ = PVN


# Types

# Class references
class BehandlingId(URIorCURIE):
    pass


class SamtykkeId(URIorCURIE):
    pass


class TjenesteId(URIorCURIE):
    pass


class BehandlingsgrunnlagId(URIorCURIE):
    pass


class PersonopplysningId(URIorCURIE):
    pass


class BegrepId(URIorCURIE):
    pass


class LandkodeId(BegrepId):
    pass


class KjonnId(BegrepId):
    pass


class FylkeId(BegrepId):
    pass


class KommuneId(BegrepId):
    pass


class SpraakId(BegrepId):
    pass


class ValutaId(URIorCURIE):
    pass


class PersonId(URIorCURIE):
    pass


class KontaktpersonId(URIorCURIE):
    pass


class VirksomhetId(URIorCURIE):
    pass


@dataclass(repr=False)
class PersonvernContainer(YAMLRoot):
    """
    Rotcontainer for FINT Personvern-instansar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PVN["PersonvernContainer"]
    class_class_curie: ClassVar[str] = "pvn:PersonvernContainer"
    class_name: ClassVar[str] = "PersonvernContainer"
    class_model_uri: ClassVar[URIRef] = PVN.PersonvernContainer

    behandlingar: Optional[Union[dict[Union[str, BehandlingId], Union[dict, "Behandling"]], list[Union[dict, "Behandling"]]]] = empty_dict()
    samtykker: Optional[Union[dict[Union[str, SamtykkeId], Union[dict, "Samtykke"]], list[Union[dict, "Samtykke"]]]] = empty_dict()
    tenester: Optional[Union[dict[Union[str, TjenesteId], Union[dict, "Tjeneste"]], list[Union[dict, "Tjeneste"]]]] = empty_dict()
    behandlingsgrunnlag: Optional[Union[dict[Union[str, BehandlingsgrunnlagId], Union[dict, "Behandlingsgrunnlag"]], list[Union[dict, "Behandlingsgrunnlag"]]]] = empty_dict()
    personopplysningar: Optional[Union[dict[Union[str, PersonopplysningId], Union[dict, "Personopplysning"]], list[Union[dict, "Personopplysning"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="behandlingar", slot_type=Behandling, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="samtykker", slot_type=Samtykke, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tenester", slot_type=Tjeneste, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="behandlingsgrunnlag", slot_type=Behandlingsgrunnlag, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="personopplysningar", slot_type=Personopplysning, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Behandling(YAMLRoot):
    """
    All bruk av personopplysningar (behandlingsaktivitet).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PVN["Behandling"]
    class_class_curie: ClassVar[str] = "pvn:Behandling"
    class_name: ClassVar[str] = "Behandling"
    class_model_uri: ClassVar[URIRef] = PVN.Behandling

    id: Union[str, BehandlingId] = None
    aktiv: Union[bool, Bool] = None
    formal: str = None
    behandlingsgrunnlag: Union[str, BehandlingsgrunnlagId] = None
    personopplysning: Union[str, PersonopplysningId] = None
    tjeneste: Union[str, TjenesteId] = None
    slettet: Optional[Union[str, XSDDateTime]] = None
    samtykke: Optional[Union[Union[str, SamtykkeId], list[Union[str, SamtykkeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehandlingId):
            self.id = BehandlingId(self.id)

        if self._is_empty(self.aktiv):
            self.MissingRequiredField("aktiv")
        if not isinstance(self.aktiv, Bool):
            self.aktiv = Bool(self.aktiv)

        if self._is_empty(self.formal):
            self.MissingRequiredField("formal")
        if not isinstance(self.formal, str):
            self.formal = str(self.formal)

        if self._is_empty(self.behandlingsgrunnlag):
            self.MissingRequiredField("behandlingsgrunnlag")
        if not isinstance(self.behandlingsgrunnlag, BehandlingsgrunnlagId):
            self.behandlingsgrunnlag = BehandlingsgrunnlagId(self.behandlingsgrunnlag)

        if self._is_empty(self.personopplysning):
            self.MissingRequiredField("personopplysning")
        if not isinstance(self.personopplysning, PersonopplysningId):
            self.personopplysning = PersonopplysningId(self.personopplysning)

        if self._is_empty(self.tjeneste):
            self.MissingRequiredField("tjeneste")
        if not isinstance(self.tjeneste, TjenesteId):
            self.tjeneste = TjenesteId(self.tjeneste)

        if self.slettet is not None and not isinstance(self.slettet, XSDDateTime):
            self.slettet = XSDDateTime(self.slettet)

        if not isinstance(self.samtykke, list):
            self.samtykke = [self.samtykke] if self.samtykke is not None else []
        self.samtykke = [v if isinstance(v, SamtykkeId) else SamtykkeId(v) for v in self.samtykke]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Samtykke(YAMLRoot):
    """
    Tillating til behandling av personopplysning.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PVN["Samtykke"]
    class_class_curie: ClassVar[str] = "pvn:Samtykke"
    class_name: ClassVar[str] = "Samtykke"
    class_model_uri: ClassVar[URIRef] = PVN.Samtykke

    id: Union[str, SamtykkeId] = None
    gyldighetsperiode: Union[dict, "Periode"] = None
    opprettet: Union[str, XSDDateTime] = None
    behandling: Union[str, BehandlingId] = None
    person: Union[str, URIorCURIE] = None
    organisasjonselement: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SamtykkeId):
            self.id = SamtykkeId(self.id)

        if self._is_empty(self.gyldighetsperiode):
            self.MissingRequiredField("gyldighetsperiode")
        if not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self._is_empty(self.opprettet):
            self.MissingRequiredField("opprettet")
        if not isinstance(self.opprettet, XSDDateTime):
            self.opprettet = XSDDateTime(self.opprettet)

        if self._is_empty(self.behandling):
            self.MissingRequiredField("behandling")
        if not isinstance(self.behandling, BehandlingId):
            self.behandling = BehandlingId(self.behandling)

        if self._is_empty(self.person):
            self.MissingRequiredField("person")
        if not isinstance(self.person, URIorCURIE):
            self.person = URIorCURIE(self.person)

        if self.organisasjonselement is not None and not isinstance(self.organisasjonselement, URIorCURIE):
            self.organisasjonselement = URIorCURIE(self.organisasjonselement)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tjeneste(YAMLRoot):
    """
    Teneste eller system som behandlar personopplysningar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PVN["Tjeneste"]
    class_class_curie: ClassVar[str] = "pvn:Tjeneste"
    class_name: ClassVar[str] = "Tjeneste"
    class_model_uri: ClassVar[URIRef] = PVN.Tjeneste

    id: Union[str, TjenesteId] = None
    navn: str = None
    slettet: Optional[Union[str, XSDDateTime]] = None
    behandling: Optional[Union[Union[str, BehandlingId], list[Union[str, BehandlingId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TjenesteId):
            self.id = TjenesteId(self.id)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.slettet is not None and not isinstance(self.slettet, XSDDateTime):
            self.slettet = XSDDateTime(self.slettet)

        if not isinstance(self.behandling, list):
            self.behandling = [self.behandling] if self.behandling is not None else []
        self.behandling = [v if isinstance(v, BehandlingId) else BehandlingId(v) for v in self.behandling]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Behandlingsgrunnlag(YAMLRoot):
    """
    Rettsleg grunnlag for behandling av personopplysningar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PVN["Behandlingsgrunnlag"]
    class_class_curie: ClassVar[str] = "pvn:Behandlingsgrunnlag"
    class_name: ClassVar[str] = "Behandlingsgrunnlag"
    class_model_uri: ClassVar[URIRef] = PVN.Behandlingsgrunnlag

    id: Union[str, BehandlingsgrunnlagId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehandlingsgrunnlagId):
            self.id = BehandlingsgrunnlagId(self.id)

        if self._is_empty(self.kode):
            self.MissingRequiredField("kode")
        if not isinstance(self.kode, str):
            self.kode = str(self.kode)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.gyldighetsperiode is not None and not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self.passiv is not None and not isinstance(self.passiv, Bool):
            self.passiv = Bool(self.passiv)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Personopplysning(YAMLRoot):
    """
    Opplysningar og vurderingar som kan knytast til enkeltpersonar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PVN["Personopplysning"]
    class_class_curie: ClassVar[str] = "pvn:Personopplysning"
    class_name: ClassVar[str] = "Personopplysning"
    class_model_uri: ClassVar[URIRef] = PVN.Personopplysning

    id: Union[str, PersonopplysningId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonopplysningId):
            self.id = PersonopplysningId(self.id)

        if self._is_empty(self.kode):
            self.MissingRequiredField("kode")
        if not isinstance(self.kode, str):
            self.kode = str(self.kode)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.gyldighetsperiode is not None and not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self.passiv is not None and not isinstance(self.passiv, Bool):
            self.passiv = Bool(self.passiv)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aktoer(YAMLRoot):
    """
    Abstrakt base for person eller eining vi samhandlar med.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Aktoer"]
    class_class_curie: ClassVar[str] = "fint:Aktoer"
    class_name: ClassVar[str] = "Aktoer"
    class_model_uri: ClassVar[URIRef] = PVN.Aktoer

    kontaktinformasjon: Optional[Union[dict, "Kontaktinformasjon"]] = None
    postadresse: Optional[Union[dict, "Adresse"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.kontaktinformasjon is not None and not isinstance(self.kontaktinformasjon, Kontaktinformasjon):
            self.kontaktinformasjon = Kontaktinformasjon(**as_dict(self.kontaktinformasjon))

        if self.postadresse is not None and not isinstance(self.postadresse, Adresse):
            self.postadresse = Adresse(**as_dict(self.postadresse))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Begrep(YAMLRoot):
    """
    Abstrakt fellesbase for alle FINT-kodeverk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Begrep"]
    class_class_curie: ClassVar[str] = "fint:Begrep"
    class_name: ClassVar[str] = "Begrep"
    class_model_uri: ClassVar[URIRef] = PVN.Begrep

    id: Union[str, BegrepId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BegrepId):
            self.id = BegrepId(self.id)

        if self._is_empty(self.kode):
            self.MissingRequiredField("kode")
        if not isinstance(self.kode, str):
            self.kode = str(self.kode)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.gyldighetsperiode is not None and not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self.passiv is not None and not isinstance(self.passiv, Bool):
            self.passiv = Bool(self.passiv)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Enhet(Aktoer):
    """
    Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd identifisert med organisasjonsnummer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Enhet"]
    class_class_curie: ClassVar[str] = "fint:Enhet"
    class_name: ClassVar[str] = "Enhet"
    class_model_uri: ClassVar[URIRef] = PVN.Enhet

    forretningsadresse: Optional[Union[dict, "Adresse"]] = None
    organisasjonsnavn: Optional[str] = None
    organisasjonsnummer: Optional[Union[dict, "Identifikator"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.forretningsadresse is not None and not isinstance(self.forretningsadresse, Adresse):
            self.forretningsadresse = Adresse(**as_dict(self.forretningsadresse))

        if self.organisasjonsnavn is not None and not isinstance(self.organisasjonsnavn, str):
            self.organisasjonsnavn = str(self.organisasjonsnavn)

        if self.organisasjonsnummer is not None and not isinstance(self.organisasjonsnummer, Identifikator):
            self.organisasjonsnummer = Identifikator(**as_dict(self.organisasjonsnummer))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Identifikator(YAMLRoot):
    """
    Unik identifikasjon til eit objekt.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Identifikator"]
    class_class_curie: ClassVar[str] = "fint:Identifikator"
    class_name: ClassVar[str] = "Identifikator"
    class_model_uri: ClassVar[URIRef] = PVN.Identifikator

    identifikatorverdi: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikatorverdi):
            self.MissingRequiredField("identifikatorverdi")
        if not isinstance(self.identifikatorverdi, str):
            self.identifikatorverdi = str(self.identifikatorverdi)

        if self.gyldighetsperiode is not None and not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Periode(YAMLRoot):
    """
    Tidsperiode med obligatorisk start og valfri slutt.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Periode"]
    class_class_curie: ClassVar[str] = "fint:Periode"
    class_name: ClassVar[str] = "Periode"
    class_model_uri: ClassVar[URIRef] = PVN.Periode

    start: Union[str, XSDDateTime] = None
    beskrivelse: Optional[str] = None
    slutt: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, XSDDateTime):
            self.start = XSDDateTime(self.start)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if self.slutt is not None and not isinstance(self.slutt, XSDDateTime):
            self.slutt = XSDDateTime(self.slutt)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Personnavn(YAMLRoot):
    """
    Namn på ein person.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Personnavn"]
    class_class_curie: ClassVar[str] = "fint:Personnavn"
    class_name: ClassVar[str] = "Personnavn"
    class_model_uri: ClassVar[URIRef] = PVN.Personnavn

    fornavn: str = None
    etternavn: str = None
    mellomnavn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fornavn):
            self.MissingRequiredField("fornavn")
        if not isinstance(self.fornavn, str):
            self.fornavn = str(self.fornavn)

        if self._is_empty(self.etternavn):
            self.MissingRequiredField("etternavn")
        if not isinstance(self.etternavn, str):
            self.etternavn = str(self.etternavn)

        if self.mellomnavn is not None and not isinstance(self.mellomnavn, str):
            self.mellomnavn = str(self.mellomnavn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontaktinformasjon(YAMLRoot):
    """
    Informasjon som kan brukast for å oppnå kontakt.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Kontaktinformasjon"]
    class_class_curie: ClassVar[str] = "fint:Kontaktinformasjon"
    class_name: ClassVar[str] = "Kontaktinformasjon"
    class_model_uri: ClassVar[URIRef] = PVN.Kontaktinformasjon

    epostadresse: Optional[str] = None
    mobiltelefonnummer: Optional[str] = None
    nettsted: Optional[str] = None
    sip: Optional[str] = None
    telefonnummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.epostadresse is not None and not isinstance(self.epostadresse, str):
            self.epostadresse = str(self.epostadresse)

        if self.mobiltelefonnummer is not None and not isinstance(self.mobiltelefonnummer, str):
            self.mobiltelefonnummer = str(self.mobiltelefonnummer)

        if self.nettsted is not None and not isinstance(self.nettsted, str):
            self.nettsted = str(self.nettsted)

        if self.sip is not None and not isinstance(self.sip, str):
            self.sip = str(self.sip)

        if self.telefonnummer is not None and not isinstance(self.telefonnummer, str):
            self.telefonnummer = str(self.telefonnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Adresse(YAMLRoot):
    """
    Fysisk adresse eller postadresse.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Adresse"]
    class_class_curie: ClassVar[str] = "fint:Adresse"
    class_name: ClassVar[str] = "Adresse"
    class_model_uri: ClassVar[URIRef] = PVN.Adresse

    adresselinje: Optional[Union[str, list[str]]] = empty_list()
    postnummer: Optional[str] = None
    poststed: Optional[str] = None
    land: Optional[Union[str, LandkodeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.adresselinje, list):
            self.adresselinje = [self.adresselinje] if self.adresselinje is not None else []
        self.adresselinje = [v if isinstance(v, str) else str(v) for v in self.adresselinje]

        if self.postnummer is not None and not isinstance(self.postnummer, str):
            self.postnummer = str(self.postnummer)

        if self.poststed is not None and not isinstance(self.poststed, str):
            self.poststed = str(self.poststed)

        if self.land is not None and not isinstance(self.land, LandkodeId):
            self.land = LandkodeId(self.land)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Matrikkelnummer(YAMLRoot):
    """
    Eintydleg identifisering av matrikkeleining innanfor kommune.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Matrikkelnummer"]
    class_class_curie: ClassVar[str] = "fint:Matrikkelnummer"
    class_name: ClassVar[str] = "Matrikkelnummer"
    class_model_uri: ClassVar[URIRef] = PVN.Matrikkelnummer

    adresse: Optional[Union[dict, Adresse]] = None
    bruksnummer: Optional[str] = None
    festenummer: Optional[str] = None
    gaardsnummer: Optional[str] = None
    seksjonsnummer: Optional[str] = None
    kommunenummer: Optional[Union[str, KommuneId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.adresse is not None and not isinstance(self.adresse, Adresse):
            self.adresse = Adresse(**as_dict(self.adresse))

        if self.bruksnummer is not None and not isinstance(self.bruksnummer, str):
            self.bruksnummer = str(self.bruksnummer)

        if self.festenummer is not None and not isinstance(self.festenummer, str):
            self.festenummer = str(self.festenummer)

        if self.gaardsnummer is not None and not isinstance(self.gaardsnummer, str):
            self.gaardsnummer = str(self.gaardsnummer)

        if self.seksjonsnummer is not None and not isinstance(self.seksjonsnummer, str):
            self.seksjonsnummer = str(self.seksjonsnummer)

        if self.kommunenummer is not None and not isinstance(self.kommunenummer, KommuneId):
            self.kommunenummer = KommuneId(self.kommunenummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Landkode(Begrep):
    """
    Landskode i ISO 3166-1 alpha-2 format.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Landkode"]
    class_class_curie: ClassVar[str] = "fint:Landkode"
    class_name: ClassVar[str] = "Landkode"
    class_model_uri: ClassVar[URIRef] = PVN.Landkode

    id: Union[str, LandkodeId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LandkodeId):
            self.id = LandkodeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kjonn(Begrep):
    """
    Verdiar for kjønn basert på ISO/IEC 5218.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Kjonn"]
    class_class_curie: ClassVar[str] = "fint:Kjonn"
    class_name: ClassVar[str] = "Kjonn"
    class_model_uri: ClassVar[URIRef] = PVN.Kjonn

    id: Union[str, KjonnId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KjonnId):
            self.id = KjonnId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fylke(Begrep):
    """
    Liste over Norges fylker.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Fylke"]
    class_class_curie: ClassVar[str] = "fint:Fylke"
    class_name: ClassVar[str] = "Fylke"
    class_model_uri: ClassVar[URIRef] = PVN.Fylke

    id: Union[str, FylkeId] = None
    kode: str = None
    navn: str = None
    kommune: Optional[Union[Union[str, KommuneId], list[Union[str, KommuneId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FylkeId):
            self.id = FylkeId(self.id)

        if not isinstance(self.kommune, list):
            self.kommune = [self.kommune] if self.kommune is not None else []
        self.kommune = [v if isinstance(v, KommuneId) else KommuneId(v) for v in self.kommune]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kommune(Begrep):
    """
    Liste over Norges kommunar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Kommune"]
    class_class_curie: ClassVar[str] = "fint:Kommune"
    class_name: ClassVar[str] = "Kommune"
    class_model_uri: ClassVar[URIRef] = PVN.Kommune

    id: Union[str, KommuneId] = None
    kode: str = None
    navn: str = None
    fylke: Union[str, FylkeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KommuneId):
            self.id = KommuneId(self.id)

        if self._is_empty(self.fylke):
            self.MissingRequiredField("fylke")
        if not isinstance(self.fylke, FylkeId):
            self.fylke = FylkeId(self.fylke)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Spraak(Begrep):
    """
    Verdiar for språk (2 bokstavar).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Spraak"]
    class_class_curie: ClassVar[str] = "fint:Spraak"
    class_name: ClassVar[str] = "Spraak"
    class_model_uri: ClassVar[URIRef] = PVN.Spraak

    id: Union[str, SpraakId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpraakId):
            self.id = SpraakId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Valuta(YAMLRoot):
    """
    Valutakodar for offisielle valutaer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Valuta"]
    class_class_curie: ClassVar[str] = "fint:Valuta"
    class_name: ClassVar[str] = "Valuta"
    class_model_uri: ClassVar[URIRef] = PVN.Valuta

    id: Union[str, ValutaId] = None
    bokstavkode: Union[dict, Identifikator] = None
    navn: str = None
    nummerkode: Union[dict, Identifikator] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ValutaId):
            self.id = ValutaId(self.id)

        if self._is_empty(self.bokstavkode):
            self.MissingRequiredField("bokstavkode")
        if not isinstance(self.bokstavkode, Identifikator):
            self.bokstavkode = Identifikator(**as_dict(self.bokstavkode))

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self._is_empty(self.nummerkode):
            self.MissingRequiredField("nummerkode")
        if not isinstance(self.nummerkode, Identifikator):
            self.nummerkode = Identifikator(**as_dict(self.nummerkode))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(Aktoer):
    """
    Fysiske private personar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Person"]
    class_class_curie: ClassVar[str] = "fint:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = PVN.Person

    id: Union[str, PersonId] = None
    fodselsnummer: Union[dict, Identifikator] = None
    navn: Union[dict, Personnavn] = None
    bilde: Optional[str] = None
    bostedsadresse: Optional[Union[dict, Adresse]] = None
    fodselsdato: Optional[Union[str, XSDDate]] = None
    parorende: Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]] = empty_list()
    statsborgerskap: Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]] = empty_list()
    kommune: Optional[Union[str, KommuneId]] = None
    kjonn: Optional[Union[str, KjonnId]] = None
    foreldreansvar: Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]] = empty_list()
    foreldre: Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]] = empty_list()
    maalform: Optional[Union[str, SpraakId]] = None
    personalressurs: Optional[Union[str, URIorCURIE]] = None
    morsmaal: Optional[Union[str, SpraakId]] = None
    laerling: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    elev: Optional[Union[str, URIorCURIE]] = None
    otungdom: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.fodselsnummer):
            self.MissingRequiredField("fodselsnummer")
        if not isinstance(self.fodselsnummer, Identifikator):
            self.fodselsnummer = Identifikator(**as_dict(self.fodselsnummer))

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, Personnavn):
            self.navn = Personnavn(**as_dict(self.navn))

        if self.bilde is not None and not isinstance(self.bilde, str):
            self.bilde = str(self.bilde)

        if self.bostedsadresse is not None and not isinstance(self.bostedsadresse, Adresse):
            self.bostedsadresse = Adresse(**as_dict(self.bostedsadresse))

        if self.fodselsdato is not None and not isinstance(self.fodselsdato, XSDDate):
            self.fodselsdato = XSDDate(self.fodselsdato)

        if not isinstance(self.parorende, list):
            self.parorende = [self.parorende] if self.parorende is not None else []
        self.parorende = [v if isinstance(v, KontaktpersonId) else KontaktpersonId(v) for v in self.parorende]

        if not isinstance(self.statsborgerskap, list):
            self.statsborgerskap = [self.statsborgerskap] if self.statsborgerskap is not None else []
        self.statsborgerskap = [v if isinstance(v, LandkodeId) else LandkodeId(v) for v in self.statsborgerskap]

        if self.kommune is not None and not isinstance(self.kommune, KommuneId):
            self.kommune = KommuneId(self.kommune)

        if self.kjonn is not None and not isinstance(self.kjonn, KjonnId):
            self.kjonn = KjonnId(self.kjonn)

        if not isinstance(self.foreldreansvar, list):
            self.foreldreansvar = [self.foreldreansvar] if self.foreldreansvar is not None else []
        self.foreldreansvar = [v if isinstance(v, PersonId) else PersonId(v) for v in self.foreldreansvar]

        if not isinstance(self.foreldre, list):
            self.foreldre = [self.foreldre] if self.foreldre is not None else []
        self.foreldre = [v if isinstance(v, PersonId) else PersonId(v) for v in self.foreldre]

        if self.maalform is not None and not isinstance(self.maalform, SpraakId):
            self.maalform = SpraakId(self.maalform)

        if self.personalressurs is not None and not isinstance(self.personalressurs, URIorCURIE):
            self.personalressurs = URIorCURIE(self.personalressurs)

        if self.morsmaal is not None and not isinstance(self.morsmaal, SpraakId):
            self.morsmaal = SpraakId(self.morsmaal)

        if not isinstance(self.laerling, list):
            self.laerling = [self.laerling] if self.laerling is not None else []
        self.laerling = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.laerling]

        if self.elev is not None and not isinstance(self.elev, URIorCURIE):
            self.elev = URIorCURIE(self.elev)

        if self.otungdom is not None and not isinstance(self.otungdom, URIorCURIE):
            self.otungdom = URIorCURIE(self.otungdom)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontaktperson(YAMLRoot):
    """
    Kontaktperson (pårørande) til ein person.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Kontaktperson"]
    class_class_curie: ClassVar[str] = "fint:Kontaktperson"
    class_name: ClassVar[str] = "Kontaktperson"
    class_model_uri: ClassVar[URIRef] = PVN.Kontaktperson

    id: Union[str, KontaktpersonId] = None
    type: str = None
    kontaktinformasjon: Optional[Union[dict, Kontaktinformasjon]] = None
    navn: Optional[Union[dict, Personnavn]] = None
    kontaktperson: Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KontaktpersonId):
            self.id = KontaktpersonId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.kontaktinformasjon is not None and not isinstance(self.kontaktinformasjon, Kontaktinformasjon):
            self.kontaktinformasjon = Kontaktinformasjon(**as_dict(self.kontaktinformasjon))

        if self.navn is not None and not isinstance(self.navn, Personnavn):
            self.navn = Personnavn(**as_dict(self.navn))

        if not isinstance(self.kontaktperson, list):
            self.kontaktperson = [self.kontaktperson] if self.kontaktperson is not None else []
        self.kontaktperson = [v if isinstance(v, PersonId) else PersonId(v) for v in self.kontaktperson]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Virksomhet(Enhet):
    """
    Ein juridisk organisasjon som produserer varer eller tenester.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Virksomhet"]
    class_class_curie: ClassVar[str] = "fint:Virksomhet"
    class_name: ClassVar[str] = "Virksomhet"
    class_model_uri: ClassVar[URIRef] = PVN.Virksomhet

    id: Union[str, VirksomhetId] = None
    virksomhetsId: Union[dict, Identifikator] = None
    laerling: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VirksomhetId):
            self.id = VirksomhetId(self.id)

        if self._is_empty(self.virksomhetsId):
            self.MissingRequiredField("virksomhetsId")
        if not isinstance(self.virksomhetsId, Identifikator):
            self.virksomhetsId = Identifikator(**as_dict(self.virksomhetsId))

        if not isinstance(self.laerling, list):
            self.laerling = [self.laerling] if self.laerling is not None else []
        self.laerling = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.laerling]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=FINT.id, name="id", curie=FINT.curie('id'),
                   model_uri=PVN.id, domain=None, range=URIRef)

slots.personvernContainer__behandlingar = Slot(uri=PVN.behandlingar, name="personvernContainer__behandlingar", curie=PVN.curie('behandlingar'),
                   model_uri=PVN.personvernContainer__behandlingar, domain=None, range=Optional[Union[dict[Union[str, BehandlingId], Union[dict, Behandling]], list[Union[dict, Behandling]]]])

slots.personvernContainer__samtykker = Slot(uri=PVN.samtykker, name="personvernContainer__samtykker", curie=PVN.curie('samtykker'),
                   model_uri=PVN.personvernContainer__samtykker, domain=None, range=Optional[Union[dict[Union[str, SamtykkeId], Union[dict, Samtykke]], list[Union[dict, Samtykke]]]])

slots.personvernContainer__tenester = Slot(uri=PVN.tenester, name="personvernContainer__tenester", curie=PVN.curie('tenester'),
                   model_uri=PVN.personvernContainer__tenester, domain=None, range=Optional[Union[dict[Union[str, TjenesteId], Union[dict, Tjeneste]], list[Union[dict, Tjeneste]]]])

slots.personvernContainer__behandlingsgrunnlag = Slot(uri=PVN.behandlingsgrunnlag, name="personvernContainer__behandlingsgrunnlag", curie=PVN.curie('behandlingsgrunnlag'),
                   model_uri=PVN.personvernContainer__behandlingsgrunnlag, domain=None, range=Optional[Union[dict[Union[str, BehandlingsgrunnlagId], Union[dict, Behandlingsgrunnlag]], list[Union[dict, Behandlingsgrunnlag]]]])

slots.personvernContainer__personopplysningar = Slot(uri=PVN.personopplysningar, name="personvernContainer__personopplysningar", curie=PVN.curie('personopplysningar'),
                   model_uri=PVN.personvernContainer__personopplysningar, domain=None, range=Optional[Union[dict[Union[str, PersonopplysningId], Union[dict, Personopplysning]], list[Union[dict, Personopplysning]]]])

slots.behandling__aktiv = Slot(uri=PVN.aktiv, name="behandling__aktiv", curie=PVN.curie('aktiv'),
                   model_uri=PVN.behandling__aktiv, domain=None, range=Union[bool, Bool])

slots.behandling__formal = Slot(uri=PVN.formal, name="behandling__formal", curie=PVN.curie('formal'),
                   model_uri=PVN.behandling__formal, domain=None, range=str)

slots.behandling__slettet = Slot(uri=PVN.slettet, name="behandling__slettet", curie=PVN.curie('slettet'),
                   model_uri=PVN.behandling__slettet, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.behandling__behandlingsgrunnlag = Slot(uri=PVN.behandlingsgrunnlag, name="behandling__behandlingsgrunnlag", curie=PVN.curie('behandlingsgrunnlag'),
                   model_uri=PVN.behandling__behandlingsgrunnlag, domain=None, range=Union[str, BehandlingsgrunnlagId])

slots.behandling__personopplysning = Slot(uri=PVN.personopplysning, name="behandling__personopplysning", curie=PVN.curie('personopplysning'),
                   model_uri=PVN.behandling__personopplysning, domain=None, range=Union[str, PersonopplysningId])

slots.behandling__samtykke = Slot(uri=PVN.samtykke, name="behandling__samtykke", curie=PVN.curie('samtykke'),
                   model_uri=PVN.behandling__samtykke, domain=None, range=Optional[Union[Union[str, SamtykkeId], list[Union[str, SamtykkeId]]]])

slots.behandling__tjeneste = Slot(uri=PVN.tjeneste, name="behandling__tjeneste", curie=PVN.curie('tjeneste'),
                   model_uri=PVN.behandling__tjeneste, domain=None, range=Union[str, TjenesteId])

slots.samtykke__gyldighetsperiode = Slot(uri=PVN.gyldighetsperiode, name="samtykke__gyldighetsperiode", curie=PVN.curie('gyldighetsperiode'),
                   model_uri=PVN.samtykke__gyldighetsperiode, domain=None, range=Union[dict, Periode])

slots.samtykke__opprettet = Slot(uri=PVN.opprettet, name="samtykke__opprettet", curie=PVN.curie('opprettet'),
                   model_uri=PVN.samtykke__opprettet, domain=None, range=Union[str, XSDDateTime])

slots.samtykke__behandling = Slot(uri=PVN.behandling, name="samtykke__behandling", curie=PVN.curie('behandling'),
                   model_uri=PVN.samtykke__behandling, domain=None, range=Union[str, BehandlingId])

slots.samtykke__person = Slot(uri=PVN.person, name="samtykke__person", curie=PVN.curie('person'),
                   model_uri=PVN.samtykke__person, domain=None, range=Union[str, URIorCURIE])

slots.samtykke__organisasjonselement = Slot(uri=PVN.organisasjonselement, name="samtykke__organisasjonselement", curie=PVN.curie('organisasjonselement'),
                   model_uri=PVN.samtykke__organisasjonselement, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.tjeneste__navn = Slot(uri=PVN.navn, name="tjeneste__navn", curie=PVN.curie('navn'),
                   model_uri=PVN.tjeneste__navn, domain=None, range=str)

slots.tjeneste__slettet = Slot(uri=PVN.slettet, name="tjeneste__slettet", curie=PVN.curie('slettet'),
                   model_uri=PVN.tjeneste__slettet, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.tjeneste__behandling = Slot(uri=PVN.behandling, name="tjeneste__behandling", curie=PVN.curie('behandling'),
                   model_uri=PVN.tjeneste__behandling, domain=None, range=Optional[Union[Union[str, BehandlingId], list[Union[str, BehandlingId]]]])

slots.behandlingsgrunnlag__kode = Slot(uri=PVN.kode, name="behandlingsgrunnlag__kode", curie=PVN.curie('kode'),
                   model_uri=PVN.behandlingsgrunnlag__kode, domain=None, range=str)

slots.behandlingsgrunnlag__navn = Slot(uri=PVN.navn, name="behandlingsgrunnlag__navn", curie=PVN.curie('navn'),
                   model_uri=PVN.behandlingsgrunnlag__navn, domain=None, range=str)

slots.behandlingsgrunnlag__gyldighetsperiode = Slot(uri=PVN.gyldighetsperiode, name="behandlingsgrunnlag__gyldighetsperiode", curie=PVN.curie('gyldighetsperiode'),
                   model_uri=PVN.behandlingsgrunnlag__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.behandlingsgrunnlag__passiv = Slot(uri=PVN.passiv, name="behandlingsgrunnlag__passiv", curie=PVN.curie('passiv'),
                   model_uri=PVN.behandlingsgrunnlag__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.personopplysning__kode = Slot(uri=PVN.kode, name="personopplysning__kode", curie=PVN.curie('kode'),
                   model_uri=PVN.personopplysning__kode, domain=None, range=str)

slots.personopplysning__navn = Slot(uri=PVN.navn, name="personopplysning__navn", curie=PVN.curie('navn'),
                   model_uri=PVN.personopplysning__navn, domain=None, range=str)

slots.personopplysning__gyldighetsperiode = Slot(uri=PVN.gyldighetsperiode, name="personopplysning__gyldighetsperiode", curie=PVN.curie('gyldighetsperiode'),
                   model_uri=PVN.personopplysning__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.personopplysning__passiv = Slot(uri=PVN.passiv, name="personopplysning__passiv", curie=PVN.curie('passiv'),
                   model_uri=PVN.personopplysning__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.aktoer__kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="aktoer__kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=PVN.aktoer__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.aktoer__postadresse = Slot(uri=FINT.postadresse, name="aktoer__postadresse", curie=FINT.curie('postadresse'),
                   model_uri=PVN.aktoer__postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.begrep__kode = Slot(uri=FINT.kode, name="begrep__kode", curie=FINT.curie('kode'),
                   model_uri=PVN.begrep__kode, domain=None, range=str)

slots.begrep__navn = Slot(uri=FINT.navn, name="begrep__navn", curie=FINT.curie('navn'),
                   model_uri=PVN.begrep__navn, domain=None, range=str)

slots.begrep__gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="begrep__gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=PVN.begrep__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.begrep__passiv = Slot(uri=FINT.passiv, name="begrep__passiv", curie=FINT.curie('passiv'),
                   model_uri=PVN.begrep__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.enhet__forretningsadresse = Slot(uri=FINT.forretningsadresse, name="enhet__forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=PVN.enhet__forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.enhet__organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="enhet__organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=PVN.enhet__organisasjonsnavn, domain=None, range=Optional[str])

slots.enhet__organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="enhet__organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=PVN.enhet__organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.identifikator__identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="identifikator__identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=PVN.identifikator__identifikatorverdi, domain=None, range=str)

slots.identifikator__gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="identifikator__gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=PVN.identifikator__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.periode__beskrivelse = Slot(uri=FINT.beskrivelse, name="periode__beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=PVN.periode__beskrivelse, domain=None, range=Optional[str])

slots.periode__start = Slot(uri=FINT.start, name="periode__start", curie=FINT.curie('start'),
                   model_uri=PVN.periode__start, domain=None, range=Union[str, XSDDateTime])

slots.periode__slutt = Slot(uri=FINT.slutt, name="periode__slutt", curie=FINT.curie('slutt'),
                   model_uri=PVN.periode__slutt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.personnavn__fornavn = Slot(uri=FINT.fornavn, name="personnavn__fornavn", curie=FINT.curie('fornavn'),
                   model_uri=PVN.personnavn__fornavn, domain=None, range=str)

slots.personnavn__mellomnavn = Slot(uri=FINT.mellomnavn, name="personnavn__mellomnavn", curie=FINT.curie('mellomnavn'),
                   model_uri=PVN.personnavn__mellomnavn, domain=None, range=Optional[str])

slots.personnavn__etternavn = Slot(uri=FINT.etternavn, name="personnavn__etternavn", curie=FINT.curie('etternavn'),
                   model_uri=PVN.personnavn__etternavn, domain=None, range=str)

slots.kontaktinformasjon__epostadresse = Slot(uri=FINT.epostadresse, name="kontaktinformasjon__epostadresse", curie=FINT.curie('epostadresse'),
                   model_uri=PVN.kontaktinformasjon__epostadresse, domain=None, range=Optional[str])

slots.kontaktinformasjon__mobiltelefonnummer = Slot(uri=FINT.mobiltelefonnummer, name="kontaktinformasjon__mobiltelefonnummer", curie=FINT.curie('mobiltelefonnummer'),
                   model_uri=PVN.kontaktinformasjon__mobiltelefonnummer, domain=None, range=Optional[str])

slots.kontaktinformasjon__nettsted = Slot(uri=FINT.nettsted, name="kontaktinformasjon__nettsted", curie=FINT.curie('nettsted'),
                   model_uri=PVN.kontaktinformasjon__nettsted, domain=None, range=Optional[str])

slots.kontaktinformasjon__sip = Slot(uri=FINT.sip, name="kontaktinformasjon__sip", curie=FINT.curie('sip'),
                   model_uri=PVN.kontaktinformasjon__sip, domain=None, range=Optional[str])

slots.kontaktinformasjon__telefonnummer = Slot(uri=FINT.telefonnummer, name="kontaktinformasjon__telefonnummer", curie=FINT.curie('telefonnummer'),
                   model_uri=PVN.kontaktinformasjon__telefonnummer, domain=None, range=Optional[str])

slots.adresse__adresselinje = Slot(uri=FINT.adresselinje, name="adresse__adresselinje", curie=FINT.curie('adresselinje'),
                   model_uri=PVN.adresse__adresselinje, domain=None, range=Optional[Union[str, list[str]]])

slots.adresse__postnummer = Slot(uri=FINT.postnummer, name="adresse__postnummer", curie=FINT.curie('postnummer'),
                   model_uri=PVN.adresse__postnummer, domain=None, range=Optional[str])

slots.adresse__poststed = Slot(uri=FINT.poststed, name="adresse__poststed", curie=FINT.curie('poststed'),
                   model_uri=PVN.adresse__poststed, domain=None, range=Optional[str])

slots.adresse__land = Slot(uri=FINT.land, name="adresse__land", curie=FINT.curie('land'),
                   model_uri=PVN.adresse__land, domain=None, range=Optional[Union[str, LandkodeId]])

slots.matrikkelnummer__adresse = Slot(uri=FINT.adresse, name="matrikkelnummer__adresse", curie=FINT.curie('adresse'),
                   model_uri=PVN.matrikkelnummer__adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.matrikkelnummer__bruksnummer = Slot(uri=FINT.bruksnummer, name="matrikkelnummer__bruksnummer", curie=FINT.curie('bruksnummer'),
                   model_uri=PVN.matrikkelnummer__bruksnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__festenummer = Slot(uri=FINT.festenummer, name="matrikkelnummer__festenummer", curie=FINT.curie('festenummer'),
                   model_uri=PVN.matrikkelnummer__festenummer, domain=None, range=Optional[str])

slots.matrikkelnummer__gaardsnummer = Slot(uri=FINT.gaardsnummer, name="matrikkelnummer__gaardsnummer", curie=FINT.curie('gaardsnummer'),
                   model_uri=PVN.matrikkelnummer__gaardsnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__seksjonsnummer = Slot(uri=FINT.seksjonsnummer, name="matrikkelnummer__seksjonsnummer", curie=FINT.curie('seksjonsnummer'),
                   model_uri=PVN.matrikkelnummer__seksjonsnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__kommunenummer = Slot(uri=FINT.kommunenummer, name="matrikkelnummer__kommunenummer", curie=FINT.curie('kommunenummer'),
                   model_uri=PVN.matrikkelnummer__kommunenummer, domain=None, range=Optional[Union[str, KommuneId]])

slots.fylke__kommune = Slot(uri=FINT.kommune, name="fylke__kommune", curie=FINT.curie('kommune'),
                   model_uri=PVN.fylke__kommune, domain=None, range=Optional[Union[Union[str, KommuneId], list[Union[str, KommuneId]]]])

slots.kommune__fylke = Slot(uri=FINT.fylke, name="kommune__fylke", curie=FINT.curie('fylke'),
                   model_uri=PVN.kommune__fylke, domain=None, range=Union[str, FylkeId])

slots.valuta__bokstavkode = Slot(uri=FINT.bokstavkode, name="valuta__bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=PVN.valuta__bokstavkode, domain=None, range=Union[dict, Identifikator])

slots.valuta__navn = Slot(uri=FINT.valutaNavn, name="valuta__navn", curie=FINT.curie('valutaNavn'),
                   model_uri=PVN.valuta__navn, domain=None, range=str)

slots.valuta__nummerkode = Slot(uri=FINT.nummerkode, name="valuta__nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=PVN.valuta__nummerkode, domain=None, range=Union[dict, Identifikator])

slots.person__bilde = Slot(uri=FINT.bilde, name="person__bilde", curie=FINT.curie('bilde'),
                   model_uri=PVN.person__bilde, domain=None, range=Optional[str])

slots.person__bostedsadresse = Slot(uri=FINT.bostedsadresse, name="person__bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=PVN.person__bostedsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.person__fodselsdato = Slot(uri=FINT.fodselsdato, name="person__fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=PVN.person__fodselsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.person__fodselsnummer = Slot(uri=FINT.fodselsnummer, name="person__fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=PVN.person__fodselsnummer, domain=None, range=Union[dict, Identifikator])

slots.person__navn = Slot(uri=FINT.personNavn, name="person__navn", curie=FINT.curie('personNavn'),
                   model_uri=PVN.person__navn, domain=None, range=Union[dict, Personnavn])

slots.person__parorende = Slot(uri=FINT.parorende, name="person__parorende", curie=FINT.curie('parorende'),
                   model_uri=PVN.person__parorende, domain=None, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.person__statsborgerskap = Slot(uri=FINT.statsborgerskap, name="person__statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=PVN.person__statsborgerskap, domain=None, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.person__kommune = Slot(uri=FINT.kommune, name="person__kommune", curie=FINT.curie('kommune'),
                   model_uri=PVN.person__kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.person__kjonn = Slot(uri=FINT.kjonn, name="person__kjonn", curie=FINT.curie('kjonn'),
                   model_uri=PVN.person__kjonn, domain=None, range=Optional[Union[str, KjonnId]])

slots.person__foreldreansvar = Slot(uri=FINT.foreldreansvar, name="person__foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=PVN.person__foreldreansvar, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.person__foreldre = Slot(uri=FINT.foreldre, name="person__foreldre", curie=FINT.curie('foreldre'),
                   model_uri=PVN.person__foreldre, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.person__maalform = Slot(uri=FINT.maalform, name="person__maalform", curie=FINT.curie('maalform'),
                   model_uri=PVN.person__maalform, domain=None, range=Optional[Union[str, SpraakId]])

slots.person__personalressurs = Slot(uri=FINT.personalressurs, name="person__personalressurs", curie=FINT.curie('personalressurs'),
                   model_uri=PVN.person__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.person__morsmaal = Slot(uri=FINT.morsmaal, name="person__morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=PVN.person__morsmaal, domain=None, range=Optional[Union[str, SpraakId]])

slots.person__laerling = Slot(uri=FINT.laerling, name="person__laerling", curie=FINT.curie('laerling'),
                   model_uri=PVN.person__laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.person__elev = Slot(uri=FINT.elev, name="person__elev", curie=FINT.curie('elev'),
                   model_uri=PVN.person__elev, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.person__otungdom = Slot(uri=FINT.otungdom, name="person__otungdom", curie=FINT.curie('otungdom'),
                   model_uri=PVN.person__otungdom, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kontaktperson__kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="kontaktperson__kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=PVN.kontaktperson__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.kontaktperson__navn = Slot(uri=FINT.kontaktpersonNavn, name="kontaktperson__navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=PVN.kontaktperson__navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.kontaktperson__type = Slot(uri=FINT.type, name="kontaktperson__type", curie=FINT.curie('type'),
                   model_uri=PVN.kontaktperson__type, domain=None, range=str)

slots.kontaktperson__kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="kontaktperson__kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=PVN.kontaktperson__kontaktperson, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.virksomhet__virksomhetsId = Slot(uri=FINT.virksomhetsId, name="virksomhet__virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=PVN.virksomhet__virksomhetsId, domain=None, range=Union[dict, Identifikator])

slots.virksomhet__laerling = Slot(uri=FINT.laerling, name="virksomhet__laerling", curie=FINT.curie('laerling'),
                   model_uri=PVN.virksomhet__laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

