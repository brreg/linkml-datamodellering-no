# Auto generated from fint-personvern-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-18T09:10:47
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


class ElevId(URIorCURIE):
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
    person: Union[str, PersonId] = None
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
        if not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

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
class Elev(YAMLRoot):
    """
    Ein elev registrert i skulesystemet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Elev"]
    class_class_curie: ClassVar[str] = "fint:Elev"
    class_name: ClassVar[str] = "Elev"
    class_model_uri: ClassVar[URIRef] = PVN.Elev

    id: Union[str, ElevId] = None
    elevnummer: Optional[Union[dict, "Identifikator"]] = None
    person: Optional[Union[str, PersonId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElevId):
            self.id = ElevId(self.id)

        if self.elevnummer is not None and not isinstance(self.elevnummer, Identifikator):
            self.elevnummer = Identifikator(**as_dict(self.elevnummer))

        if self.person is not None and not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

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
    valuta_navn: str = None
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

        if self._is_empty(self.valuta_navn):
            self.MissingRequiredField("valuta_navn")
        if not isinstance(self.valuta_navn, str):
            self.valuta_navn = str(self.valuta_navn)

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
    person_navn: Union[dict, Personnavn] = None
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
    morsmaal: Optional[Union[str, SpraakId]] = None
    laerling: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    elev: Optional[Union[str, ElevId]] = None
    otungdom: Optional[Union[str, URIorCURIE]] = None
    personalressurs: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.fodselsnummer):
            self.MissingRequiredField("fodselsnummer")
        if not isinstance(self.fodselsnummer, Identifikator):
            self.fodselsnummer = Identifikator(**as_dict(self.fodselsnummer))

        if self._is_empty(self.person_navn):
            self.MissingRequiredField("person_navn")
        if not isinstance(self.person_navn, Personnavn):
            self.person_navn = Personnavn(**as_dict(self.person_navn))

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

        if self.morsmaal is not None and not isinstance(self.morsmaal, SpraakId):
            self.morsmaal = SpraakId(self.morsmaal)

        if not isinstance(self.laerling, list):
            self.laerling = [self.laerling] if self.laerling is not None else []
        self.laerling = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.laerling]

        if self.elev is not None and not isinstance(self.elev, ElevId):
            self.elev = ElevId(self.elev)

        if self.otungdom is not None and not isinstance(self.otungdom, URIorCURIE):
            self.otungdom = URIorCURIE(self.otungdom)

        if self.personalressurs is not None and not isinstance(self.personalressurs, URIorCURIE):
            self.personalressurs = URIorCURIE(self.personalressurs)

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
    kontaktperson_navn: Optional[Union[dict, Personnavn]] = None
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

        if self.kontaktperson_navn is not None and not isinstance(self.kontaktperson_navn, Personnavn):
            self.kontaktperson_navn = Personnavn(**as_dict(self.kontaktperson_navn))

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

slots.behandlingar = Slot(uri=PVN.behandlingar, name="behandlingar", curie=PVN.curie('behandlingar'),
                   model_uri=PVN.behandlingar, domain=None, range=Optional[Union[dict[Union[str, BehandlingId], Union[dict, Behandling]], list[Union[dict, Behandling]]]])

slots.samtykker = Slot(uri=PVN.samtykker, name="samtykker", curie=PVN.curie('samtykker'),
                   model_uri=PVN.samtykker, domain=None, range=Optional[Union[dict[Union[str, SamtykkeId], Union[dict, Samtykke]], list[Union[dict, Samtykke]]]])

slots.tenester = Slot(uri=PVN.tenester, name="tenester", curie=PVN.curie('tenester'),
                   model_uri=PVN.tenester, domain=None, range=Optional[Union[dict[Union[str, TjenesteId], Union[dict, Tjeneste]], list[Union[dict, Tjeneste]]]])

slots.personopplysningar = Slot(uri=PVN.personopplysningar, name="personopplysningar", curie=PVN.curie('personopplysningar'),
                   model_uri=PVN.personopplysningar, domain=None, range=Optional[Union[dict[Union[str, PersonopplysningId], Union[dict, Personopplysning]], list[Union[dict, Personopplysning]]]])

slots.behandlingsgrunnlag = Slot(uri=PVN.behandlingsgrunnlag, name="behandlingsgrunnlag", curie=PVN.curie('behandlingsgrunnlag'),
                   model_uri=PVN.behandlingsgrunnlag, domain=None, range=Optional[Union[str, BehandlingsgrunnlagId]])

slots.behandling = Slot(uri=PVN.behandling, name="behandling", curie=PVN.curie('behandling'),
                   model_uri=PVN.behandling, domain=None, range=Optional[Union[str, BehandlingId]])

slots.slettet = Slot(uri=PVN.slettet, name="slettet", curie=PVN.curie('slettet'),
                   model_uri=PVN.slettet, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.aktiv = Slot(uri=PVN.aktiv, name="aktiv", curie=PVN.curie('aktiv'),
                   model_uri=PVN.aktiv, domain=None, range=Optional[Union[bool, Bool]])

slots.formal = Slot(uri=PVN.formal, name="formal", curie=PVN.curie('formal'),
                   model_uri=PVN.formal, domain=None, range=Optional[str])

slots.personopplysning = Slot(uri=PVN.personopplysning, name="personopplysning", curie=PVN.curie('personopplysning'),
                   model_uri=PVN.personopplysning, domain=None, range=Optional[Union[str, PersonopplysningId]])

slots.samtykke = Slot(uri=PVN.samtykke, name="samtykke", curie=PVN.curie('samtykke'),
                   model_uri=PVN.samtykke, domain=None, range=Optional[Union[Union[str, SamtykkeId], list[Union[str, SamtykkeId]]]])

slots.tjeneste = Slot(uri=PVN.tjeneste, name="tjeneste", curie=PVN.curie('tjeneste'),
                   model_uri=PVN.tjeneste, domain=None, range=Optional[Union[str, TjenesteId]])

slots.opprettet = Slot(uri=PVN.opprettet, name="opprettet", curie=PVN.curie('opprettet'),
                   model_uri=PVN.opprettet, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.organisasjonselement = Slot(uri=PVN.organisasjonselement, name="organisasjonselement", curie=PVN.curie('organisasjonselement'),
                   model_uri=PVN.organisasjonselement, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.id = Slot(uri=FINT.id, name="id", curie=FINT.curie('id'),
                   model_uri=PVN.id, domain=None, range=URIRef)

slots.gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=PVN.gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=PVN.kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.postadresse = Slot(uri=FINT.postadresse, name="postadresse", curie=FINT.curie('postadresse'),
                   model_uri=PVN.postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.forretningsadresse = Slot(uri=FINT.forretningsadresse, name="forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=PVN.forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=PVN.organisasjonsnavn, domain=None, range=Optional[str])

slots.organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=PVN.organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.kode = Slot(uri=FINT.kode, name="kode", curie=FINT.curie('kode'),
                   model_uri=PVN.kode, domain=None, range=Optional[str])

slots.navn = Slot(uri=FINT.navn, name="navn", curie=FINT.curie('navn'),
                   model_uri=PVN.navn, domain=None, range=Optional[str])

slots.passiv = Slot(uri=FINT.passiv, name="passiv", curie=FINT.curie('passiv'),
                   model_uri=PVN.passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=PVN.identifikatorverdi, domain=None, range=Optional[str])

slots.beskrivelse = Slot(uri=FINT.beskrivelse, name="beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=PVN.beskrivelse, domain=None, range=Optional[str])

slots.start = Slot(uri=FINT.start, name="start", curie=FINT.curie('start'),
                   model_uri=PVN.start, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.slutt = Slot(uri=FINT.slutt, name="slutt", curie=FINT.curie('slutt'),
                   model_uri=PVN.slutt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.fornavn = Slot(uri=FINT.fornavn, name="fornavn", curie=FINT.curie('fornavn'),
                   model_uri=PVN.fornavn, domain=None, range=Optional[str])

slots.mellomnavn = Slot(uri=FINT.mellomnavn, name="mellomnavn", curie=FINT.curie('mellomnavn'),
                   model_uri=PVN.mellomnavn, domain=None, range=Optional[str])

slots.etternavn = Slot(uri=FINT.etternavn, name="etternavn", curie=FINT.curie('etternavn'),
                   model_uri=PVN.etternavn, domain=None, range=Optional[str])

slots.epostadresse = Slot(uri=FINT.epostadresse, name="epostadresse", curie=FINT.curie('epostadresse'),
                   model_uri=PVN.epostadresse, domain=None, range=Optional[str])

slots.mobiltelefonnummer = Slot(uri=FINT.mobiltelefonnummer, name="mobiltelefonnummer", curie=FINT.curie('mobiltelefonnummer'),
                   model_uri=PVN.mobiltelefonnummer, domain=None, range=Optional[str])

slots.nettsted = Slot(uri=FINT.nettsted, name="nettsted", curie=FINT.curie('nettsted'),
                   model_uri=PVN.nettsted, domain=None, range=Optional[str])

slots.sip = Slot(uri=FINT.sip, name="sip", curie=FINT.curie('sip'),
                   model_uri=PVN.sip, domain=None, range=Optional[str])

slots.telefonnummer = Slot(uri=FINT.telefonnummer, name="telefonnummer", curie=FINT.curie('telefonnummer'),
                   model_uri=PVN.telefonnummer, domain=None, range=Optional[str])

slots.adresselinje = Slot(uri=FINT.adresselinje, name="adresselinje", curie=FINT.curie('adresselinje'),
                   model_uri=PVN.adresselinje, domain=None, range=Optional[Union[str, list[str]]])

slots.postnummer = Slot(uri=FINT.postnummer, name="postnummer", curie=FINT.curie('postnummer'),
                   model_uri=PVN.postnummer, domain=None, range=Optional[str])

slots.poststed = Slot(uri=FINT.poststed, name="poststed", curie=FINT.curie('poststed'),
                   model_uri=PVN.poststed, domain=None, range=Optional[str])

slots.land = Slot(uri=FINT.land, name="land", curie=FINT.curie('land'),
                   model_uri=PVN.land, domain=None, range=Optional[Union[str, LandkodeId]])

slots.adresse = Slot(uri=FINT.adresse, name="adresse", curie=FINT.curie('adresse'),
                   model_uri=PVN.adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.bruksnummer = Slot(uri=FINT.bruksnummer, name="bruksnummer", curie=FINT.curie('bruksnummer'),
                   model_uri=PVN.bruksnummer, domain=None, range=Optional[str])

slots.festenummer = Slot(uri=FINT.festenummer, name="festenummer", curie=FINT.curie('festenummer'),
                   model_uri=PVN.festenummer, domain=None, range=Optional[str])

slots.gaardsnummer = Slot(uri=FINT.gaardsnummer, name="gaardsnummer", curie=FINT.curie('gaardsnummer'),
                   model_uri=PVN.gaardsnummer, domain=None, range=Optional[str])

slots.seksjonsnummer = Slot(uri=FINT.seksjonsnummer, name="seksjonsnummer", curie=FINT.curie('seksjonsnummer'),
                   model_uri=PVN.seksjonsnummer, domain=None, range=Optional[str])

slots.kommunenummer = Slot(uri=FINT.kommunenummer, name="kommunenummer", curie=FINT.curie('kommunenummer'),
                   model_uri=PVN.kommunenummer, domain=None, range=Optional[Union[str, KommuneId]])

slots.fylke = Slot(uri=FINT.fylke, name="fylke", curie=FINT.curie('fylke'),
                   model_uri=PVN.fylke, domain=None, range=Optional[Union[str, FylkeId]])

slots.kommune = Slot(uri=FINT.kommune, name="kommune", curie=FINT.curie('kommune'),
                   model_uri=PVN.kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.kjonn = Slot(uri=FINT.kjonn, name="kjonn", curie=FINT.curie('kjonn'),
                   model_uri=PVN.kjonn, domain=None, range=Optional[Union[str, KjonnId]])

slots.bokstavkode = Slot(uri=FINT.bokstavkode, name="bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=PVN.bokstavkode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.valuta_navn = Slot(uri=FINT.valutaNavn, name="valuta_navn", curie=FINT.curie('valutaNavn'),
                   model_uri=PVN.valuta_navn, domain=None, range=Optional[str])

slots.nummerkode = Slot(uri=FINT.nummerkode, name="nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=PVN.nummerkode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.bilde = Slot(uri=FINT.bilde, name="bilde", curie=FINT.curie('bilde'),
                   model_uri=PVN.bilde, domain=None, range=Optional[str])

slots.bostedsadresse = Slot(uri=FINT.bostedsadresse, name="bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=PVN.bostedsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.fodselsdato = Slot(uri=FINT.fodselsdato, name="fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=PVN.fodselsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.fodselsnummer = Slot(uri=FINT.fodselsnummer, name="fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=PVN.fodselsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person_navn = Slot(uri=FINT.personNavn, name="person_navn", curie=FINT.curie('personNavn'),
                   model_uri=PVN.person_navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.parorende = Slot(uri=FINT.parorende, name="parorende", curie=FINT.curie('parorende'),
                   model_uri=PVN.parorende, domain=None, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.statsborgerskap = Slot(uri=FINT.statsborgerskap, name="statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=PVN.statsborgerskap, domain=None, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.foreldreansvar = Slot(uri=FINT.foreldreansvar, name="foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=PVN.foreldreansvar, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.foreldre = Slot(uri=FINT.foreldre, name="foreldre", curie=FINT.curie('foreldre'),
                   model_uri=PVN.foreldre, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.maalform = Slot(uri=FINT.maalform, name="maalform", curie=FINT.curie('maalform'),
                   model_uri=PVN.maalform, domain=None, range=Optional[Union[str, SpraakId]])

slots.morsmaal = Slot(uri=FINT.morsmaal, name="morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=PVN.morsmaal, domain=None, range=Optional[Union[str, SpraakId]])

slots.laerling = Slot(uri=FINT.laerling, name="laerling", curie=FINT.curie('laerling'),
                   model_uri=PVN.laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.elev = Slot(uri=FINT.elev, name="elev", curie=FINT.curie('elev'),
                   model_uri=PVN.elev, domain=None, range=Optional[Union[str, ElevId]])

slots.elevnummer = Slot(uri=FINT.elevnummer, name="elevnummer", curie=FINT.curie('elevnummer'),
                   model_uri=PVN.elevnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person = Slot(uri=FINT.person, name="person", curie=FINT.curie('person'),
                   model_uri=PVN.person, domain=None, range=Optional[Union[str, PersonId]])

slots.otungdom = Slot(uri=FINT.otungdom, name="otungdom", curie=FINT.curie('otungdom'),
                   model_uri=PVN.otungdom, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kontaktperson_navn = Slot(uri=FINT.kontaktpersonNavn, name="kontaktperson_navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=PVN.kontaktperson_navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.type = Slot(uri=FINT.type, name="type", curie=FINT.curie('type'),
                   model_uri=PVN.type, domain=None, range=Optional[str])

slots.kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=PVN.kontaktperson, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.virksomhetsId = Slot(uri=FINT.virksomhetsId, name="virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=PVN.virksomhetsId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person__personalressurs = Slot(uri=FINT.personalressurs, name="person__personalressurs", curie=FINT.curie('personalressurs'),
                   model_uri=PVN.person__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.PersonvernContainer_behandlingsgrunnlag = Slot(uri=PVN.behandlingsgrunnlag, name="PersonvernContainer_behandlingsgrunnlag", curie=PVN.curie('behandlingsgrunnlag'),
                   model_uri=PVN.PersonvernContainer_behandlingsgrunnlag, domain=PersonvernContainer, range=Optional[Union[dict[Union[str, BehandlingsgrunnlagId], Union[dict, "Behandlingsgrunnlag"]], list[Union[dict, "Behandlingsgrunnlag"]]]])

slots.Behandling_aktiv = Slot(uri=PVN.aktiv, name="Behandling_aktiv", curie=PVN.curie('aktiv'),
                   model_uri=PVN.Behandling_aktiv, domain=Behandling, range=Union[bool, Bool])

slots.Behandling_formal = Slot(uri=PVN.formal, name="Behandling_formal", curie=PVN.curie('formal'),
                   model_uri=PVN.Behandling_formal, domain=Behandling, range=str)

slots.Behandling_slettet = Slot(uri=PVN.slettet, name="Behandling_slettet", curie=PVN.curie('slettet'),
                   model_uri=PVN.Behandling_slettet, domain=Behandling, range=Optional[Union[str, XSDDateTime]])

slots.Behandling_behandlingsgrunnlag = Slot(uri=PVN.behandlingsgrunnlag, name="Behandling_behandlingsgrunnlag", curie=PVN.curie('behandlingsgrunnlag'),
                   model_uri=PVN.Behandling_behandlingsgrunnlag, domain=Behandling, range=Union[str, BehandlingsgrunnlagId])

slots.Behandling_personopplysning = Slot(uri=PVN.personopplysning, name="Behandling_personopplysning", curie=PVN.curie('personopplysning'),
                   model_uri=PVN.Behandling_personopplysning, domain=Behandling, range=Union[str, PersonopplysningId])

slots.Behandling_samtykke = Slot(uri=PVN.samtykke, name="Behandling_samtykke", curie=PVN.curie('samtykke'),
                   model_uri=PVN.Behandling_samtykke, domain=Behandling, range=Optional[Union[Union[str, SamtykkeId], list[Union[str, SamtykkeId]]]])

slots.Behandling_tjeneste = Slot(uri=PVN.tjeneste, name="Behandling_tjeneste", curie=PVN.curie('tjeneste'),
                   model_uri=PVN.Behandling_tjeneste, domain=Behandling, range=Union[str, TjenesteId])

slots.Samtykke_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Samtykke_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=PVN.Samtykke_gyldighetsperiode, domain=Samtykke, range=Union[dict, "Periode"])

slots.Samtykke_opprettet = Slot(uri=PVN.opprettet, name="Samtykke_opprettet", curie=PVN.curie('opprettet'),
                   model_uri=PVN.Samtykke_opprettet, domain=Samtykke, range=Union[str, XSDDateTime])

slots.Samtykke_behandling = Slot(uri=PVN.behandling, name="Samtykke_behandling", curie=PVN.curie('behandling'),
                   model_uri=PVN.Samtykke_behandling, domain=Samtykke, range=Union[str, BehandlingId])

slots.Samtykke_person = Slot(uri=FINT.person, name="Samtykke_person", curie=FINT.curie('person'),
                   model_uri=PVN.Samtykke_person, domain=Samtykke, range=Union[str, PersonId])

slots.Samtykke_organisasjonselement = Slot(uri=PVN.organisasjonselement, name="Samtykke_organisasjonselement", curie=PVN.curie('organisasjonselement'),
                   model_uri=PVN.Samtykke_organisasjonselement, domain=Samtykke, range=Optional[Union[str, URIorCURIE]])

slots.Tjeneste_navn = Slot(uri=FINT.navn, name="Tjeneste_navn", curie=FINT.curie('navn'),
                   model_uri=PVN.Tjeneste_navn, domain=Tjeneste, range=str)

slots.Tjeneste_slettet = Slot(uri=PVN.slettet, name="Tjeneste_slettet", curie=PVN.curie('slettet'),
                   model_uri=PVN.Tjeneste_slettet, domain=Tjeneste, range=Optional[Union[str, XSDDateTime]])

slots.Tjeneste_behandling = Slot(uri=PVN.behandling, name="Tjeneste_behandling", curie=PVN.curie('behandling'),
                   model_uri=PVN.Tjeneste_behandling, domain=Tjeneste, range=Optional[Union[Union[str, BehandlingId], list[Union[str, BehandlingId]]]])

slots.Behandlingsgrunnlag_kode = Slot(uri=FINT.kode, name="Behandlingsgrunnlag_kode", curie=FINT.curie('kode'),
                   model_uri=PVN.Behandlingsgrunnlag_kode, domain=Behandlingsgrunnlag, range=str)

slots.Behandlingsgrunnlag_navn = Slot(uri=FINT.navn, name="Behandlingsgrunnlag_navn", curie=FINT.curie('navn'),
                   model_uri=PVN.Behandlingsgrunnlag_navn, domain=Behandlingsgrunnlag, range=str)

slots.Behandlingsgrunnlag_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Behandlingsgrunnlag_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=PVN.Behandlingsgrunnlag_gyldighetsperiode, domain=Behandlingsgrunnlag, range=Optional[Union[dict, "Periode"]])

slots.Behandlingsgrunnlag_passiv = Slot(uri=FINT.passiv, name="Behandlingsgrunnlag_passiv", curie=FINT.curie('passiv'),
                   model_uri=PVN.Behandlingsgrunnlag_passiv, domain=Behandlingsgrunnlag, range=Optional[Union[bool, Bool]])

slots.Personopplysning_kode = Slot(uri=FINT.kode, name="Personopplysning_kode", curie=FINT.curie('kode'),
                   model_uri=PVN.Personopplysning_kode, domain=Personopplysning, range=str)

slots.Personopplysning_navn = Slot(uri=FINT.navn, name="Personopplysning_navn", curie=FINT.curie('navn'),
                   model_uri=PVN.Personopplysning_navn, domain=Personopplysning, range=str)

slots.Personopplysning_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Personopplysning_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=PVN.Personopplysning_gyldighetsperiode, domain=Personopplysning, range=Optional[Union[dict, "Periode"]])

slots.Personopplysning_passiv = Slot(uri=FINT.passiv, name="Personopplysning_passiv", curie=FINT.curie('passiv'),
                   model_uri=PVN.Personopplysning_passiv, domain=Personopplysning, range=Optional[Union[bool, Bool]])

slots.Aktoer_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Aktoer_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=PVN.Aktoer_kontaktinformasjon, domain=Aktoer, range=Optional[Union[dict, "Kontaktinformasjon"]])

slots.Aktoer_postadresse = Slot(uri=FINT.postadresse, name="Aktoer_postadresse", curie=FINT.curie('postadresse'),
                   model_uri=PVN.Aktoer_postadresse, domain=Aktoer, range=Optional[Union[dict, "Adresse"]])

slots.Begrep_kode = Slot(uri=FINT.kode, name="Begrep_kode", curie=FINT.curie('kode'),
                   model_uri=PVN.Begrep_kode, domain=Begrep, range=str)

slots.Begrep_navn = Slot(uri=FINT.navn, name="Begrep_navn", curie=FINT.curie('navn'),
                   model_uri=PVN.Begrep_navn, domain=Begrep, range=str)

slots.Begrep_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Begrep_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=PVN.Begrep_gyldighetsperiode, domain=Begrep, range=Optional[Union[dict, "Periode"]])

slots.Begrep_passiv = Slot(uri=FINT.passiv, name="Begrep_passiv", curie=FINT.curie('passiv'),
                   model_uri=PVN.Begrep_passiv, domain=Begrep, range=Optional[Union[bool, Bool]])

slots.Elev_elevnummer = Slot(uri=FINT.elevnummer, name="Elev_elevnummer", curie=FINT.curie('elevnummer'),
                   model_uri=PVN.Elev_elevnummer, domain=Elev, range=Optional[Union[dict, "Identifikator"]])

slots.Elev_person = Slot(uri=FINT.person, name="Elev_person", curie=FINT.curie('person'),
                   model_uri=PVN.Elev_person, domain=Elev, range=Optional[Union[str, PersonId]])

slots.Enhet_forretningsadresse = Slot(uri=FINT.forretningsadresse, name="Enhet_forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=PVN.Enhet_forretningsadresse, domain=Enhet, range=Optional[Union[dict, "Adresse"]])

slots.Enhet_organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="Enhet_organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=PVN.Enhet_organisasjonsnavn, domain=Enhet, range=Optional[str])

slots.Enhet_organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="Enhet_organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=PVN.Enhet_organisasjonsnummer, domain=Enhet, range=Optional[Union[dict, "Identifikator"]])

slots.Identifikator_identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="Identifikator_identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=PVN.Identifikator_identifikatorverdi, domain=Identifikator, range=str)

slots.Periode_start = Slot(uri=FINT.start, name="Periode_start", curie=FINT.curie('start'),
                   model_uri=PVN.Periode_start, domain=Periode, range=Union[str, XSDDateTime])

slots.Personnavn_fornavn = Slot(uri=FINT.fornavn, name="Personnavn_fornavn", curie=FINT.curie('fornavn'),
                   model_uri=PVN.Personnavn_fornavn, domain=Personnavn, range=str)

slots.Personnavn_etternavn = Slot(uri=FINT.etternavn, name="Personnavn_etternavn", curie=FINT.curie('etternavn'),
                   model_uri=PVN.Personnavn_etternavn, domain=Personnavn, range=str)

slots.Fylke_kommune = Slot(uri=FINT.kommune, name="Fylke_kommune", curie=FINT.curie('kommune'),
                   model_uri=PVN.Fylke_kommune, domain=Fylke, range=Optional[Union[Union[str, KommuneId], list[Union[str, KommuneId]]]])

slots.Kommune_fylke = Slot(uri=FINT.fylke, name="Kommune_fylke", curie=FINT.curie('fylke'),
                   model_uri=PVN.Kommune_fylke, domain=Kommune, range=Union[str, FylkeId])

slots.Valuta_bokstavkode = Slot(uri=FINT.bokstavkode, name="Valuta_bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=PVN.Valuta_bokstavkode, domain=Valuta, range=Union[dict, Identifikator])

slots.Valuta_valuta_navn = Slot(uri=FINT.valutaNavn, name="Valuta_valuta_navn", curie=FINT.curie('valutaNavn'),
                   model_uri=PVN.Valuta_valuta_navn, domain=Valuta, range=str)

slots.Valuta_nummerkode = Slot(uri=FINT.nummerkode, name="Valuta_nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=PVN.Valuta_nummerkode, domain=Valuta, range=Union[dict, Identifikator])

slots.Person_fodselsnummer = Slot(uri=FINT.fodselsnummer, name="Person_fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=PVN.Person_fodselsnummer, domain=Person, range=Union[dict, Identifikator])

slots.Person_person_navn = Slot(uri=FINT.personNavn, name="Person_person_navn", curie=FINT.curie('personNavn'),
                   model_uri=PVN.Person_person_navn, domain=Person, range=Union[dict, Personnavn])

slots.Person_bilde = Slot(uri=FINT.bilde, name="Person_bilde", curie=FINT.curie('bilde'),
                   model_uri=PVN.Person_bilde, domain=Person, range=Optional[str])

slots.Person_bostedsadresse = Slot(uri=FINT.bostedsadresse, name="Person_bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=PVN.Person_bostedsadresse, domain=Person, range=Optional[Union[dict, Adresse]])

slots.Person_fodselsdato = Slot(uri=FINT.fodselsdato, name="Person_fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=PVN.Person_fodselsdato, domain=Person, range=Optional[Union[str, XSDDate]])

slots.Person_parorende = Slot(uri=FINT.parorende, name="Person_parorende", curie=FINT.curie('parorende'),
                   model_uri=PVN.Person_parorende, domain=Person, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.Person_statsborgerskap = Slot(uri=FINT.statsborgerskap, name="Person_statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=PVN.Person_statsborgerskap, domain=Person, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.Person_kommune = Slot(uri=FINT.kommune, name="Person_kommune", curie=FINT.curie('kommune'),
                   model_uri=PVN.Person_kommune, domain=Person, range=Optional[Union[str, KommuneId]])

slots.Person_kjonn = Slot(uri=FINT.kjonn, name="Person_kjonn", curie=FINT.curie('kjonn'),
                   model_uri=PVN.Person_kjonn, domain=Person, range=Optional[Union[str, KjonnId]])

slots.Person_foreldreansvar = Slot(uri=FINT.foreldreansvar, name="Person_foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=PVN.Person_foreldreansvar, domain=Person, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Person_foreldre = Slot(uri=FINT.foreldre, name="Person_foreldre", curie=FINT.curie('foreldre'),
                   model_uri=PVN.Person_foreldre, domain=Person, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Person_maalform = Slot(uri=FINT.maalform, name="Person_maalform", curie=FINT.curie('maalform'),
                   model_uri=PVN.Person_maalform, domain=Person, range=Optional[Union[str, SpraakId]])

slots.Person_morsmaal = Slot(uri=FINT.morsmaal, name="Person_morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=PVN.Person_morsmaal, domain=Person, range=Optional[Union[str, SpraakId]])

slots.Person_laerling = Slot(uri=FINT.laerling, name="Person_laerling", curie=FINT.curie('laerling'),
                   model_uri=PVN.Person_laerling, domain=Person, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Person_elev = Slot(uri=FINT.elev, name="Person_elev", curie=FINT.curie('elev'),
                   model_uri=PVN.Person_elev, domain=Person, range=Optional[Union[str, ElevId]])

slots.Person_otungdom = Slot(uri=FINT.otungdom, name="Person_otungdom", curie=FINT.curie('otungdom'),
                   model_uri=PVN.Person_otungdom, domain=Person, range=Optional[Union[str, URIorCURIE]])

slots.Kontaktperson_type = Slot(uri=FINT.type, name="Kontaktperson_type", curie=FINT.curie('type'),
                   model_uri=PVN.Kontaktperson_type, domain=Kontaktperson, range=str)

slots.Kontaktperson_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Kontaktperson_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=PVN.Kontaktperson_kontaktinformasjon, domain=Kontaktperson, range=Optional[Union[dict, Kontaktinformasjon]])

slots.Kontaktperson_kontaktperson_navn = Slot(uri=FINT.kontaktpersonNavn, name="Kontaktperson_kontaktperson_navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=PVN.Kontaktperson_kontaktperson_navn, domain=Kontaktperson, range=Optional[Union[dict, Personnavn]])

slots.Kontaktperson_kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="Kontaktperson_kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=PVN.Kontaktperson_kontaktperson, domain=Kontaktperson, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Virksomhet_virksomhetsId = Slot(uri=FINT.virksomhetsId, name="Virksomhet_virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=PVN.Virksomhet_virksomhetsId, domain=Virksomhet, range=Union[dict, Identifikator])

slots.Virksomhet_laerling = Slot(uri=FINT.laerling, name="Virksomhet_laerling", curie=FINT.curie('laerling'),
                   model_uri=PVN.Virksomhet_laerling, domain=Virksomhet, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

