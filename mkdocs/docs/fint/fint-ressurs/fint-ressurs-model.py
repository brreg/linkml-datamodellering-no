# Auto generated from fint-ressurs-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-27T14:51:36
# Schema: fint-ressurs
#
# id: https://data.norge.no/fint/fint-ressurs
# description: FINT-domenemodell for ressursstyring. Dekkjer tre sub-pakkar: ressurs.eiendel (applikasjonar og lisensressursar), ressurs.datautstyr (digitale einingar og einingsgrupper) og ressurs.tilgang (identitetar og rettigheiter).
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

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.11.0"
version = "4.0.20"

# Namespaces
FINT = CurieNamespace('fint', 'https://schema.fintlabs.no/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RES = CurieNamespace('res', 'https://schema.fintlabs.no/ressurs/')
DEFAULT_ = RES


# Types

# Class references
class ApplikasjonId(URIorCURIE):
    pass


class ApplikasjonsressursId(URIorCURIE):
    pass


class ApplikasjonsressurstilgjengelighetId(URIorCURIE):
    pass


class DigitalEnhetId(URIorCURIE):
    pass


class EnhetsgruppeId(URIorCURIE):
    pass


class EnhetsgruppemedlemskapId(URIorCURIE):
    pass


class IdentitetId(URIorCURIE):
    pass


class RettighetId(URIorCURIE):
    pass


class ApplikasjonskategoriId(URIorCURIE):
    pass


class BrukertypeId(URIorCURIE):
    pass


class EnhetstypeId(URIorCURIE):
    pass


class HandhevingstypeId(URIorCURIE):
    pass


class LisensmodellId(URIorCURIE):
    pass


class PlattformId(URIorCURIE):
    pass


class ProdusentId(URIorCURIE):
    pass


class StatusId(URIorCURIE):
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
class RessursContainer(YAMLRoot):
    """
    Rotcontainer for FINT Ressurs-instansar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["RessursContainer"]
    class_class_curie: ClassVar[str] = "res:RessursContainer"
    class_name: ClassVar[str] = "RessursContainer"
    class_model_uri: ClassVar[URIRef] = RES.RessursContainer

    applikasjonar: Optional[Union[dict[Union[str, ApplikasjonId], Union[dict, "Applikasjon"]], list[Union[dict, "Applikasjon"]]]] = empty_dict()
    applikasjonsressursar: Optional[Union[dict[Union[str, ApplikasjonsressursId], Union[dict, "Applikasjonsressurs"]], list[Union[dict, "Applikasjonsressurs"]]]] = empty_dict()
    applikasjonsressurstilgjengelegheit: Optional[Union[dict[Union[str, ApplikasjonsressurstilgjengelighetId], Union[dict, "Applikasjonsressurstilgjengelighet"]], list[Union[dict, "Applikasjonsressurstilgjengelighet"]]]] = empty_dict()
    digitaleEiningar: Optional[Union[dict[Union[str, DigitalEnhetId], Union[dict, "DigitalEnhet"]], list[Union[dict, "DigitalEnhet"]]]] = empty_dict()
    einingsgrupper: Optional[Union[dict[Union[str, EnhetsgruppeId], Union[dict, "Enhetsgruppe"]], list[Union[dict, "Enhetsgruppe"]]]] = empty_dict()
    einingsgruppedmedlemskap: Optional[Union[dict[Union[str, EnhetsgruppemedlemskapId], Union[dict, "Enhetsgruppemedlemskap"]], list[Union[dict, "Enhetsgruppemedlemskap"]]]] = empty_dict()
    identitetar: Optional[Union[dict[Union[str, IdentitetId], Union[dict, "Identitet"]], list[Union[dict, "Identitet"]]]] = empty_dict()
    rettigheiter: Optional[Union[dict[Union[str, RettighetId], Union[dict, "Rettighet"]], list[Union[dict, "Rettighet"]]]] = empty_dict()
    applikasjonskategoriar: Optional[Union[dict[Union[str, ApplikasjonskategoriId], Union[dict, "Applikasjonskategori"]], list[Union[dict, "Applikasjonskategori"]]]] = empty_dict()
    brukertypar: Optional[Union[dict[Union[str, BrukertypeId], Union[dict, "Brukertype"]], list[Union[dict, "Brukertype"]]]] = empty_dict()
    einingstypar: Optional[Union[dict[Union[str, EnhetstypeId], Union[dict, "Enhetstype"]], list[Union[dict, "Enhetstype"]]]] = empty_dict()
    handhaevingstypar: Optional[Union[dict[Union[str, HandhevingstypeId], Union[dict, "Handhevingstype"]], list[Union[dict, "Handhevingstype"]]]] = empty_dict()
    lisensmodellar: Optional[Union[dict[Union[str, LisensmodellId], Union[dict, "Lisensmodell"]], list[Union[dict, "Lisensmodell"]]]] = empty_dict()
    plattformar: Optional[Union[dict[Union[str, PlattformId], Union[dict, "Plattform"]], list[Union[dict, "Plattform"]]]] = empty_dict()
    produsentar: Optional[Union[dict[Union[str, ProdusentId], Union[dict, "Produsent"]], list[Union[dict, "Produsent"]]]] = empty_dict()
    statusar: Optional[Union[dict[Union[str, StatusId], Union[dict, "Status"]], list[Union[dict, "Status"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="applikasjonar", slot_type=Applikasjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="applikasjonsressursar", slot_type=Applikasjonsressurs, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="applikasjonsressurstilgjengelegheit", slot_type=Applikasjonsressurstilgjengelighet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="digitaleEiningar", slot_type=DigitalEnhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="einingsgrupper", slot_type=Enhetsgruppe, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="einingsgruppedmedlemskap", slot_type=Enhetsgruppemedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="identitetar", slot_type=Identitet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rettigheiter", slot_type=Rettighet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="applikasjonskategoriar", slot_type=Applikasjonskategori, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="brukertypar", slot_type=Brukertype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="einingstypar", slot_type=Enhetstype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="handhaevingstypar", slot_type=Handhevingstype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="lisensmodellar", slot_type=Lisensmodell, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="plattformar", slot_type=Plattform, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="produsentar", slot_type=Produsent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="statusar", slot_type=Status, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Applikasjon(YAMLRoot):
    """
    Ein applikasjon med tilhøyrande ressursar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Applikasjon"]
    class_class_curie: ClassVar[str] = "res:Applikasjon"
    class_name: ClassVar[str] = "Applikasjon"
    class_model_uri: ClassVar[URIRef] = RES.Applikasjon

    id: Union[str, ApplikasjonId] = None
    navn: str = None
    gyldighetsperiode: Union[dict, "Periode"] = None
    beskrivelse: Optional[str] = None
    plattform: Optional[Union[Union[str, PlattformId], list[Union[str, PlattformId]]]] = empty_list()
    applikasjonsressurs: Optional[Union[Union[str, ApplikasjonsressursId], list[Union[str, ApplikasjonsressursId]]]] = empty_list()
    applikasjonskategori: Optional[Union[Union[str, ApplikasjonskategoriId], list[Union[str, ApplikasjonskategoriId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ApplikasjonId):
            self.id = ApplikasjonId(self.id)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self._is_empty(self.gyldighetsperiode):
            self.MissingRequiredField("gyldighetsperiode")
        if not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if not isinstance(self.plattform, list):
            self.plattform = [self.plattform] if self.plattform is not None else []
        self.plattform = [v if isinstance(v, PlattformId) else PlattformId(v) for v in self.plattform]

        if not isinstance(self.applikasjonsressurs, list):
            self.applikasjonsressurs = [self.applikasjonsressurs] if self.applikasjonsressurs is not None else []
        self.applikasjonsressurs = [v if isinstance(v, ApplikasjonsressursId) else ApplikasjonsressursId(v) for v in self.applikasjonsressurs]

        if not isinstance(self.applikasjonskategori, list):
            self.applikasjonskategori = [self.applikasjonskategori] if self.applikasjonskategori is not None else []
        self.applikasjonskategori = [v if isinstance(v, ApplikasjonskategoriId) else ApplikasjonskategoriId(v) for v in self.applikasjonskategori]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Applikasjonsressurs(YAMLRoot):
    """
    Informasjon om kor ein applikasjon kan nyttast (lisensressurs).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Applikasjonsressurs"]
    class_class_curie: ClassVar[str] = "res:Applikasjonsressurs"
    class_name: ClassVar[str] = "Applikasjonsressurs"
    class_model_uri: ClassVar[URIRef] = RES.Applikasjonsressurs

    id: Union[str, ApplikasjonsressursId] = None
    navn: str = None
    gyldighetsperiode: Union[dict, "Periode"] = None
    eier: Union[str, URIorCURIE] = None
    applikasjon: Union[str, ApplikasjonId] = None
    brukertype: Union[Union[str, BrukertypeId], list[Union[str, BrukertypeId]]] = None
    beskrivelse: Optional[str] = None
    enhetskostnad: Optional[int] = None
    kreverGodkjenning: Optional[Union[bool, Bool]] = None
    lisensantall: Optional[int] = None
    handhevingstype: Optional[Union[str, HandhevingstypeId]] = None
    lisensmodell: Optional[Union[str, LisensmodellId]] = None
    ressurstilgjengelighet: Optional[Union[Union[str, ApplikasjonsressurstilgjengelighetId], list[Union[str, ApplikasjonsressurstilgjengelighetId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ApplikasjonsressursId):
            self.id = ApplikasjonsressursId(self.id)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self._is_empty(self.gyldighetsperiode):
            self.MissingRequiredField("gyldighetsperiode")
        if not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self._is_empty(self.eier):
            self.MissingRequiredField("eier")
        if not isinstance(self.eier, URIorCURIE):
            self.eier = URIorCURIE(self.eier)

        if self._is_empty(self.applikasjon):
            self.MissingRequiredField("applikasjon")
        if not isinstance(self.applikasjon, ApplikasjonId):
            self.applikasjon = ApplikasjonId(self.applikasjon)

        if self._is_empty(self.brukertype):
            self.MissingRequiredField("brukertype")
        if not isinstance(self.brukertype, list):
            self.brukertype = [self.brukertype] if self.brukertype is not None else []
        self.brukertype = [v if isinstance(v, BrukertypeId) else BrukertypeId(v) for v in self.brukertype]

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if self.enhetskostnad is not None and not isinstance(self.enhetskostnad, int):
            self.enhetskostnad = int(self.enhetskostnad)

        if self.kreverGodkjenning is not None and not isinstance(self.kreverGodkjenning, Bool):
            self.kreverGodkjenning = Bool(self.kreverGodkjenning)

        if self.lisensantall is not None and not isinstance(self.lisensantall, int):
            self.lisensantall = int(self.lisensantall)

        if self.handhevingstype is not None and not isinstance(self.handhevingstype, HandhevingstypeId):
            self.handhevingstype = HandhevingstypeId(self.handhevingstype)

        if self.lisensmodell is not None and not isinstance(self.lisensmodell, LisensmodellId):
            self.lisensmodell = LisensmodellId(self.lisensmodell)

        if not isinstance(self.ressurstilgjengelighet, list):
            self.ressurstilgjengelighet = [self.ressurstilgjengelighet] if self.ressurstilgjengelighet is not None else []
        self.ressurstilgjengelighet = [v if isinstance(v, ApplikasjonsressurstilgjengelighetId) else ApplikasjonsressurstilgjengelighetId(v) for v in self.ressurstilgjengelighet]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Applikasjonsressurstilgjengelighet(YAMLRoot):
    """
    Kva organisasjonselements brukarar som har tilgang til ein ressurs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Applikasjonsressurstilgjengelighet"]
    class_class_curie: ClassVar[str] = "res:Applikasjonsressurstilgjengelighet"
    class_name: ClassVar[str] = "Applikasjonsressurstilgjengelighet"
    class_model_uri: ClassVar[URIRef] = RES.Applikasjonsressurstilgjengelighet

    id: Union[str, ApplikasjonsressurstilgjengelighetId] = None
    gyldighetsperiode: Union[dict, "Periode"] = None
    konsument: Union[str, URIorCURIE] = None
    ressursRef: Union[str, ApplikasjonsressursId] = None
    lisensantall: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ApplikasjonsressurstilgjengelighetId):
            self.id = ApplikasjonsressurstilgjengelighetId(self.id)

        if self._is_empty(self.gyldighetsperiode):
            self.MissingRequiredField("gyldighetsperiode")
        if not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self._is_empty(self.konsument):
            self.MissingRequiredField("konsument")
        if not isinstance(self.konsument, URIorCURIE):
            self.konsument = URIorCURIE(self.konsument)

        if self._is_empty(self.ressursRef):
            self.MissingRequiredField("ressursRef")
        if not isinstance(self.ressursRef, ApplikasjonsressursId):
            self.ressursRef = ApplikasjonsressursId(self.ressursRef)

        if self.lisensantall is not None and not isinstance(self.lisensantall, int):
            self.lisensantall = int(self.lisensantall)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DigitalEnhet(YAMLRoot):
    """
    Ei digital eining som t.d. PC, nettbrett eller mobil.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["DigitalEnhet"]
    class_class_curie: ClassVar[str] = "res:DigitalEnhet"
    class_name: ClassVar[str] = "DigitalEnhet"
    class_model_uri: ClassVar[URIRef] = RES.DigitalEnhet

    id: Union[str, DigitalEnhetId] = None
    serienummer: str = None
    administrator: Union[str, URIorCURIE] = None
    enhetstype: Union[str, EnhetstypeId] = None
    plattform: Union[str, PlattformId] = None
    navn: Optional[str] = None
    dataobjektId: Optional[Union[dict, "Identifikator"]] = None
    flerbrukerenhet: Optional[Union[bool, Bool]] = None
    privateid: Optional[Union[bool, Bool]] = None
    eier: Optional[Union[str, URIorCURIE]] = None
    personalressurs: Optional[Union[str, URIorCURIE]] = None
    elev: Optional[Union[str, ElevId]] = None
    status: Optional[Union[str, StatusId]] = None
    produsent: Optional[Union[str, ProdusentId]] = None
    enhetsgruppemedlemskap: Optional[Union[Union[str, EnhetsgruppemedlemskapId], list[Union[str, EnhetsgruppemedlemskapId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DigitalEnhetId):
            self.id = DigitalEnhetId(self.id)

        if self._is_empty(self.serienummer):
            self.MissingRequiredField("serienummer")
        if not isinstance(self.serienummer, str):
            self.serienummer = str(self.serienummer)

        if self._is_empty(self.administrator):
            self.MissingRequiredField("administrator")
        if not isinstance(self.administrator, URIorCURIE):
            self.administrator = URIorCURIE(self.administrator)

        if self._is_empty(self.enhetstype):
            self.MissingRequiredField("enhetstype")
        if not isinstance(self.enhetstype, EnhetstypeId):
            self.enhetstype = EnhetstypeId(self.enhetstype)

        if self._is_empty(self.plattform):
            self.MissingRequiredField("plattform")
        if not isinstance(self.plattform, PlattformId):
            self.plattform = PlattformId(self.plattform)

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.dataobjektId is not None and not isinstance(self.dataobjektId, Identifikator):
            self.dataobjektId = Identifikator(**as_dict(self.dataobjektId))

        if self.flerbrukerenhet is not None and not isinstance(self.flerbrukerenhet, Bool):
            self.flerbrukerenhet = Bool(self.flerbrukerenhet)

        if self.privateid is not None and not isinstance(self.privateid, Bool):
            self.privateid = Bool(self.privateid)

        if self.eier is not None and not isinstance(self.eier, URIorCURIE):
            self.eier = URIorCURIE(self.eier)

        if self.personalressurs is not None and not isinstance(self.personalressurs, URIorCURIE):
            self.personalressurs = URIorCURIE(self.personalressurs)

        if self.elev is not None and not isinstance(self.elev, ElevId):
            self.elev = ElevId(self.elev)

        if self.status is not None and not isinstance(self.status, StatusId):
            self.status = StatusId(self.status)

        if self.produsent is not None and not isinstance(self.produsent, ProdusentId):
            self.produsent = ProdusentId(self.produsent)

        if not isinstance(self.enhetsgruppemedlemskap, list):
            self.enhetsgruppemedlemskap = [self.enhetsgruppemedlemskap] if self.enhetsgruppemedlemskap is not None else []
        self.enhetsgruppemedlemskap = [v if isinstance(v, EnhetsgruppemedlemskapId) else EnhetsgruppemedlemskapId(v) for v in self.enhetsgruppemedlemskap]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Enhetsgruppe(YAMLRoot):
    """
    Ei gruppering av einsarta digitale einingar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Enhetsgruppe"]
    class_class_curie: ClassVar[str] = "res:Enhetsgruppe"
    class_name: ClassVar[str] = "Enhetsgruppe"
    class_model_uri: ClassVar[URIRef] = RES.Enhetsgruppe

    id: Union[str, EnhetsgruppeId] = None
    navn: str = None
    organisasjonsenhet: Union[str, URIorCURIE] = None
    enhetstype: Union[str, EnhetstypeId] = None
    plattform: Union[str, PlattformId] = None
    enhetsgruppemedlemskap: Optional[Union[Union[str, EnhetsgruppemedlemskapId], list[Union[str, EnhetsgruppemedlemskapId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnhetsgruppeId):
            self.id = EnhetsgruppeId(self.id)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self._is_empty(self.organisasjonsenhet):
            self.MissingRequiredField("organisasjonsenhet")
        if not isinstance(self.organisasjonsenhet, URIorCURIE):
            self.organisasjonsenhet = URIorCURIE(self.organisasjonsenhet)

        if self._is_empty(self.enhetstype):
            self.MissingRequiredField("enhetstype")
        if not isinstance(self.enhetstype, EnhetstypeId):
            self.enhetstype = EnhetstypeId(self.enhetstype)

        if self._is_empty(self.plattform):
            self.MissingRequiredField("plattform")
        if not isinstance(self.plattform, PlattformId):
            self.plattform = PlattformId(self.plattform)

        if not isinstance(self.enhetsgruppemedlemskap, list):
            self.enhetsgruppemedlemskap = [self.enhetsgruppemedlemskap] if self.enhetsgruppemedlemskap is not None else []
        self.enhetsgruppemedlemskap = [v if isinstance(v, EnhetsgruppemedlemskapId) else EnhetsgruppemedlemskapId(v) for v in self.enhetsgruppemedlemskap]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Enhetsgruppemedlemskap(YAMLRoot):
    """
    Medlemskap mellom ei digital eining og ei einingsgruppe.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Enhetsgruppemedlemskap"]
    class_class_curie: ClassVar[str] = "res:Enhetsgruppemedlemskap"
    class_name: ClassVar[str] = "Enhetsgruppemedlemskap"
    class_model_uri: ClassVar[URIRef] = RES.Enhetsgruppemedlemskap

    id: Union[str, EnhetsgruppemedlemskapId] = None
    digitalEnhet: Union[str, DigitalEnhetId] = None
    enhetsgruppe: Union[str, EnhetsgruppeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnhetsgruppemedlemskapId):
            self.id = EnhetsgruppemedlemskapId(self.id)

        if self._is_empty(self.digitalEnhet):
            self.MissingRequiredField("digitalEnhet")
        if not isinstance(self.digitalEnhet, DigitalEnhetId):
            self.digitalEnhet = DigitalEnhetId(self.digitalEnhet)

        if self._is_empty(self.enhetsgruppe):
            self.MissingRequiredField("enhetsgruppe")
        if not isinstance(self.enhetsgruppe, EnhetsgruppeId):
            self.enhetsgruppe = EnhetsgruppeId(self.enhetsgruppe)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Identitet(YAMLRoot):
    """
    Identitet som identifiserer innehavaren av rettigheiter i organisasjonen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Identitet"]
    class_class_curie: ClassVar[str] = "res:Identitet"
    class_name: ClassVar[str] = "Identitet"
    class_model_uri: ClassVar[URIRef] = RES.Identitet

    id: Union[str, IdentitetId] = None
    personalressurs: Optional[Union[str, URIorCURIE]] = None
    rettighet: Optional[Union[Union[str, RettighetId], list[Union[str, RettighetId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentitetId):
            self.id = IdentitetId(self.id)

        if self.personalressurs is not None and not isinstance(self.personalressurs, URIorCURIE):
            self.personalressurs = URIorCURIE(self.personalressurs)

        if not isinstance(self.rettighet, list):
            self.rettighet = [self.rettighet] if self.rettighet is not None else []
        self.rettighet = [v if isinstance(v, RettighetId) else RettighetId(v) for v in self.rettighet]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rettighet(YAMLRoot):
    """
    Ei namngitt rettighet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Rettighet"]
    class_class_curie: ClassVar[str] = "res:Rettighet"
    class_name: ClassVar[str] = "Rettighet"
    class_model_uri: ClassVar[URIRef] = RES.Rettighet

    id: Union[str, RettighetId] = None
    kode: str = None
    navn: str = None
    beskrivelse: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None
    identitet: Optional[Union[Union[str, IdentitetId], list[Union[str, IdentitetId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RettighetId):
            self.id = RettighetId(self.id)

        if self._is_empty(self.kode):
            self.MissingRequiredField("kode")
        if not isinstance(self.kode, str):
            self.kode = str(self.kode)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self._is_empty(self.beskrivelse):
            self.MissingRequiredField("beskrivelse")
        if not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if self.gyldighetsperiode is not None and not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self.passiv is not None and not isinstance(self.passiv, Bool):
            self.passiv = Bool(self.passiv)

        if not isinstance(self.identitet, list):
            self.identitet = [self.identitet] if self.identitet is not None else []
        self.identitet = [v if isinstance(v, IdentitetId) else IdentitetId(v) for v in self.identitet]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Applikasjonskategori(YAMLRoot):
    """
    Kategori av applikasjonar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Applikasjonskategori"]
    class_class_curie: ClassVar[str] = "res:Applikasjonskategori"
    class_name: ClassVar[str] = "Applikasjonskategori"
    class_model_uri: ClassVar[URIRef] = RES.Applikasjonskategori

    id: Union[str, ApplikasjonskategoriId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ApplikasjonskategoriId):
            self.id = ApplikasjonskategoriId(self.id)

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
class Brukertype(YAMLRoot):
    """
    Dei ulike brukartypane som kan nytte lisensen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Brukertype"]
    class_class_curie: ClassVar[str] = "res:Brukertype"
    class_name: ClassVar[str] = "Brukertype"
    class_model_uri: ClassVar[URIRef] = RES.Brukertype

    id: Union[str, BrukertypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BrukertypeId):
            self.id = BrukertypeId(self.id)

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
class Enhetstype(YAMLRoot):
    """
    Type digital eining.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Enhetstype"]
    class_class_curie: ClassVar[str] = "res:Enhetstype"
    class_name: ClassVar[str] = "Enhetstype"
    class_model_uri: ClassVar[URIRef] = RES.Enhetstype

    id: Union[str, EnhetstypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnhetstypeId):
            self.id = EnhetstypeId(self.id)

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
class Handhevingstype(YAMLRoot):
    """
    Korleis ulike lisensmodellar kan handhevast.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Handhevingstype"]
    class_class_curie: ClassVar[str] = "res:Handhevingstype"
    class_name: ClassVar[str] = "Handhevingstype"
    class_model_uri: ClassVar[URIRef] = RES.Handhevingstype

    id: Union[str, HandhevingstypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HandhevingstypeId):
            self.id = HandhevingstypeId(self.id)

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
class Lisensmodell(YAMLRoot):
    """
    Lisensmodellar som kan knytast til ein lisens.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Lisensmodell"]
    class_class_curie: ClassVar[str] = "res:Lisensmodell"
    class_name: ClassVar[str] = "Lisensmodell"
    class_model_uri: ClassVar[URIRef] = RES.Lisensmodell

    id: Union[str, LisensmodellId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LisensmodellId):
            self.id = LisensmodellId(self.id)

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
class Plattform(YAMLRoot):
    """
    Plattforma tenesta kan leverast på.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Plattform"]
    class_class_curie: ClassVar[str] = "res:Plattform"
    class_name: ClassVar[str] = "Plattform"
    class_model_uri: ClassVar[URIRef] = RES.Plattform

    id: Union[str, PlattformId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlattformId):
            self.id = PlattformId(self.id)

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
class Produsent(YAMLRoot):
    """
    Produsent av ei digital eining.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Produsent"]
    class_class_curie: ClassVar[str] = "res:Produsent"
    class_name: ClassVar[str] = "Produsent"
    class_model_uri: ClassVar[URIRef] = RES.Produsent

    id: Union[str, ProdusentId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProdusentId):
            self.id = ProdusentId(self.id)

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
class Status(YAMLRoot):
    """
    Status på ei digital eining i fagsystemet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RES["Status"]
    class_class_curie: ClassVar[str] = "res:Status"
    class_name: ClassVar[str] = "Status"
    class_model_uri: ClassVar[URIRef] = RES.Status

    id: Union[str, StatusId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StatusId):
            self.id = StatusId(self.id)

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
    class_model_uri: ClassVar[URIRef] = RES.Aktoer

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
    class_model_uri: ClassVar[URIRef] = RES.Begrep

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
    class_model_uri: ClassVar[URIRef] = RES.Elev

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
    class_model_uri: ClassVar[URIRef] = RES.Enhet

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
    class_model_uri: ClassVar[URIRef] = RES.Identifikator

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
    class_model_uri: ClassVar[URIRef] = RES.Periode

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
    class_model_uri: ClassVar[URIRef] = RES.Personnavn

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
    class_model_uri: ClassVar[URIRef] = RES.Kontaktinformasjon

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
    class_model_uri: ClassVar[URIRef] = RES.Adresse

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
    class_model_uri: ClassVar[URIRef] = RES.Matrikkelnummer

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
    class_model_uri: ClassVar[URIRef] = RES.Landkode

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
    class_model_uri: ClassVar[URIRef] = RES.Kjonn

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
    class_model_uri: ClassVar[URIRef] = RES.Fylke

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
    class_model_uri: ClassVar[URIRef] = RES.Kommune

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
    class_model_uri: ClassVar[URIRef] = RES.Spraak

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
    class_model_uri: ClassVar[URIRef] = RES.Valuta

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
    class_model_uri: ClassVar[URIRef] = RES.Person

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
    class_model_uri: ClassVar[URIRef] = RES.Kontaktperson

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
    class_model_uri: ClassVar[URIRef] = RES.Virksomhet

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

slots.plattform = Slot(uri=RES.plattform, name="plattform", curie=RES.curie('plattform'),
                   model_uri=RES.plattform, domain=None, range=Optional[Union[str, PlattformId]])

slots.enhetstype = Slot(uri=RES.enhetstype, name="enhetstype", curie=RES.curie('enhetstype'),
                   model_uri=RES.enhetstype, domain=None, range=Optional[Union[str, EnhetstypeId]])

slots.enhetsgruppemedlemskap = Slot(uri=RES.enhetsgruppemedlemskap, name="enhetsgruppemedlemskap", curie=RES.curie('enhetsgruppemedlemskap'),
                   model_uri=RES.enhetsgruppemedlemskap, domain=None, range=Optional[Union[Union[str, EnhetsgruppemedlemskapId], list[Union[str, EnhetsgruppemedlemskapId]]]])

slots.personalressurs = Slot(uri=RES.personalressurs, name="personalressurs", curie=RES.curie('personalressurs'),
                   model_uri=RES.personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.eier = Slot(uri=RES.eier, name="eier", curie=RES.curie('eier'),
                   model_uri=RES.eier, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.lisensantall = Slot(uri=RES.lisensantall, name="lisensantall", curie=RES.curie('lisensantall'),
                   model_uri=RES.lisensantall, domain=None, range=Optional[int])

slots.applikasjonsressurs = Slot(uri=RES.applikasjonsressurs, name="applikasjonsressurs", curie=RES.curie('applikasjonsressurs'),
                   model_uri=RES.applikasjonsressurs, domain=None, range=Optional[Union[Union[str, ApplikasjonsressursId], list[Union[str, ApplikasjonsressursId]]]])

slots.applikasjonskategori = Slot(uri=RES.applikasjonskategori, name="applikasjonskategori", curie=RES.curie('applikasjonskategori'),
                   model_uri=RES.applikasjonskategori, domain=None, range=Optional[Union[Union[str, ApplikasjonskategoriId], list[Union[str, ApplikasjonskategoriId]]]])

slots.applikasjon = Slot(uri=RES.applikasjon, name="applikasjon", curie=RES.curie('applikasjon'),
                   model_uri=RES.applikasjon, domain=None, range=Optional[Union[str, ApplikasjonId]])

slots.brukertype = Slot(uri=RES.brukertype, name="brukertype", curie=RES.curie('brukertype'),
                   model_uri=RES.brukertype, domain=None, range=Optional[Union[Union[str, BrukertypeId], list[Union[str, BrukertypeId]]]])

slots.handhevingstype = Slot(uri=RES.handhevingstype, name="handhevingstype", curie=RES.curie('handhevingstype'),
                   model_uri=RES.handhevingstype, domain=None, range=Optional[Union[str, HandhevingstypeId]])

slots.lisensmodell = Slot(uri=RES.lisensmodell, name="lisensmodell", curie=RES.curie('lisensmodell'),
                   model_uri=RES.lisensmodell, domain=None, range=Optional[Union[str, LisensmodellId]])

slots.ressurstilgjengelighet = Slot(uri=RES.ressurstilgjengelighet, name="ressurstilgjengelighet", curie=RES.curie('ressurstilgjengelighet'),
                   model_uri=RES.ressurstilgjengelighet, domain=None, range=Optional[Union[Union[str, ApplikasjonsressurstilgjengelighetId], list[Union[str, ApplikasjonsressurstilgjengelighetId]]]])

slots.enhetskostnad = Slot(uri=RES.enhetskostnad, name="enhetskostnad", curie=RES.curie('enhetskostnad'),
                   model_uri=RES.enhetskostnad, domain=None, range=Optional[int])

slots.kreverGodkjenning = Slot(uri=RES.kreverGodkjenning, name="kreverGodkjenning", curie=RES.curie('kreverGodkjenning'),
                   model_uri=RES.kreverGodkjenning, domain=None, range=Optional[Union[bool, Bool]])

slots.konsument = Slot(uri=RES.konsument, name="konsument", curie=RES.curie('konsument'),
                   model_uri=RES.konsument, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.ressursRef = Slot(uri=RES.ressursRef, name="ressursRef", curie=RES.curie('ressursRef'),
                   model_uri=RES.ressursRef, domain=None, range=Optional[Union[str, ApplikasjonsressursId]])

slots.serienummer = Slot(uri=RES.serienummer, name="serienummer", curie=RES.curie('serienummer'),
                   model_uri=RES.serienummer, domain=None, range=Optional[str])

slots.dataobjektId = Slot(uri=RES.dataobjektId, name="dataobjektId", curie=RES.curie('dataobjektId'),
                   model_uri=RES.dataobjektId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.flerbrukerenhet = Slot(uri=RES.flerbrukerenhet, name="flerbrukerenhet", curie=RES.curie('flerbrukerenhet'),
                   model_uri=RES.flerbrukerenhet, domain=None, range=Optional[Union[bool, Bool]])

slots.privateid = Slot(uri=RES.privateid, name="privateid", curie=RES.curie('privateid'),
                   model_uri=RES.privateid, domain=None, range=Optional[Union[bool, Bool]])

slots.administrator = Slot(uri=RES.administrator, name="administrator", curie=RES.curie('administrator'),
                   model_uri=RES.administrator, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.status = Slot(uri=RES.status, name="status", curie=RES.curie('status'),
                   model_uri=RES.status, domain=None, range=Optional[Union[str, StatusId]])

slots.produsent = Slot(uri=RES.produsent, name="produsent", curie=RES.curie('produsent'),
                   model_uri=RES.produsent, domain=None, range=Optional[Union[str, ProdusentId]])

slots.organisasjonsenhet = Slot(uri=RES.organisasjonsenhet, name="organisasjonsenhet", curie=RES.curie('organisasjonsenhet'),
                   model_uri=RES.organisasjonsenhet, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.digitalEnhet = Slot(uri=RES.digitalEnhet, name="digitalEnhet", curie=RES.curie('digitalEnhet'),
                   model_uri=RES.digitalEnhet, domain=None, range=Optional[Union[str, DigitalEnhetId]])

slots.enhetsgruppe = Slot(uri=RES.enhetsgruppe, name="enhetsgruppe", curie=RES.curie('enhetsgruppe'),
                   model_uri=RES.enhetsgruppe, domain=None, range=Optional[Union[str, EnhetsgruppeId]])

slots.rettighet = Slot(uri=RES.rettighet, name="rettighet", curie=RES.curie('rettighet'),
                   model_uri=RES.rettighet, domain=None, range=Optional[Union[Union[str, RettighetId], list[Union[str, RettighetId]]]])

slots.identitet = Slot(uri=RES.identitet, name="identitet", curie=RES.curie('identitet'),
                   model_uri=RES.identitet, domain=None, range=Optional[Union[Union[str, IdentitetId], list[Union[str, IdentitetId]]]])

slots.id = Slot(uri=FINT.id, name="id", curie=FINT.curie('id'),
                   model_uri=RES.id, domain=None, range=URIRef)

slots.gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=RES.kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.postadresse = Slot(uri=FINT.postadresse, name="postadresse", curie=FINT.curie('postadresse'),
                   model_uri=RES.postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.forretningsadresse = Slot(uri=FINT.forretningsadresse, name="forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=RES.forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=RES.organisasjonsnavn, domain=None, range=Optional[str])

slots.organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=RES.organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.kode = Slot(uri=FINT.kode, name="kode", curie=FINT.curie('kode'),
                   model_uri=RES.kode, domain=None, range=Optional[str])

slots.navn = Slot(uri=FINT.navn, name="navn", curie=FINT.curie('navn'),
                   model_uri=RES.navn, domain=None, range=Optional[str])

slots.passiv = Slot(uri=FINT.passiv, name="passiv", curie=FINT.curie('passiv'),
                   model_uri=RES.passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=RES.identifikatorverdi, domain=None, range=Optional[str])

slots.beskrivelse = Slot(uri=FINT.beskrivelse, name="beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=RES.beskrivelse, domain=None, range=Optional[str])

slots.start = Slot(uri=FINT.start, name="start", curie=FINT.curie('start'),
                   model_uri=RES.start, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.slutt = Slot(uri=FINT.slutt, name="slutt", curie=FINT.curie('slutt'),
                   model_uri=RES.slutt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.fornavn = Slot(uri=FINT.fornavn, name="fornavn", curie=FINT.curie('fornavn'),
                   model_uri=RES.fornavn, domain=None, range=Optional[str])

slots.mellomnavn = Slot(uri=FINT.mellomnavn, name="mellomnavn", curie=FINT.curie('mellomnavn'),
                   model_uri=RES.mellomnavn, domain=None, range=Optional[str])

slots.etternavn = Slot(uri=FINT.etternavn, name="etternavn", curie=FINT.curie('etternavn'),
                   model_uri=RES.etternavn, domain=None, range=Optional[str])

slots.epostadresse = Slot(uri=FINT.epostadresse, name="epostadresse", curie=FINT.curie('epostadresse'),
                   model_uri=RES.epostadresse, domain=None, range=Optional[str])

slots.mobiltelefonnummer = Slot(uri=FINT.mobiltelefonnummer, name="mobiltelefonnummer", curie=FINT.curie('mobiltelefonnummer'),
                   model_uri=RES.mobiltelefonnummer, domain=None, range=Optional[str])

slots.nettsted = Slot(uri=FINT.nettsted, name="nettsted", curie=FINT.curie('nettsted'),
                   model_uri=RES.nettsted, domain=None, range=Optional[str])

slots.sip = Slot(uri=FINT.sip, name="sip", curie=FINT.curie('sip'),
                   model_uri=RES.sip, domain=None, range=Optional[str])

slots.telefonnummer = Slot(uri=FINT.telefonnummer, name="telefonnummer", curie=FINT.curie('telefonnummer'),
                   model_uri=RES.telefonnummer, domain=None, range=Optional[str])

slots.adresselinje = Slot(uri=FINT.adresselinje, name="adresselinje", curie=FINT.curie('adresselinje'),
                   model_uri=RES.adresselinje, domain=None, range=Optional[Union[str, list[str]]])

slots.postnummer = Slot(uri=FINT.postnummer, name="postnummer", curie=FINT.curie('postnummer'),
                   model_uri=RES.postnummer, domain=None, range=Optional[str])

slots.poststed = Slot(uri=FINT.poststed, name="poststed", curie=FINT.curie('poststed'),
                   model_uri=RES.poststed, domain=None, range=Optional[str])

slots.land = Slot(uri=FINT.land, name="land", curie=FINT.curie('land'),
                   model_uri=RES.land, domain=None, range=Optional[Union[str, LandkodeId]])

slots.adresse = Slot(uri=FINT.adresse, name="adresse", curie=FINT.curie('adresse'),
                   model_uri=RES.adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.bruksnummer = Slot(uri=FINT.bruksnummer, name="bruksnummer", curie=FINT.curie('bruksnummer'),
                   model_uri=RES.bruksnummer, domain=None, range=Optional[str])

slots.festenummer = Slot(uri=FINT.festenummer, name="festenummer", curie=FINT.curie('festenummer'),
                   model_uri=RES.festenummer, domain=None, range=Optional[str])

slots.gaardsnummer = Slot(uri=FINT.gaardsnummer, name="gaardsnummer", curie=FINT.curie('gaardsnummer'),
                   model_uri=RES.gaardsnummer, domain=None, range=Optional[str])

slots.seksjonsnummer = Slot(uri=FINT.seksjonsnummer, name="seksjonsnummer", curie=FINT.curie('seksjonsnummer'),
                   model_uri=RES.seksjonsnummer, domain=None, range=Optional[str])

slots.kommunenummer = Slot(uri=FINT.kommunenummer, name="kommunenummer", curie=FINT.curie('kommunenummer'),
                   model_uri=RES.kommunenummer, domain=None, range=Optional[Union[str, KommuneId]])

slots.fylke = Slot(uri=FINT.fylke, name="fylke", curie=FINT.curie('fylke'),
                   model_uri=RES.fylke, domain=None, range=Optional[Union[str, FylkeId]])

slots.kommune = Slot(uri=FINT.kommune, name="kommune", curie=FINT.curie('kommune'),
                   model_uri=RES.kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.kjonn = Slot(uri=FINT.kjonn, name="kjonn", curie=FINT.curie('kjonn'),
                   model_uri=RES.kjonn, domain=None, range=Optional[Union[str, KjonnId]])

slots.bokstavkode = Slot(uri=FINT.bokstavkode, name="bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=RES.bokstavkode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.valuta_navn = Slot(uri=FINT.valutaNavn, name="valuta_navn", curie=FINT.curie('valutaNavn'),
                   model_uri=RES.valuta_navn, domain=None, range=Optional[str])

slots.nummerkode = Slot(uri=FINT.nummerkode, name="nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=RES.nummerkode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.bilde = Slot(uri=FINT.bilde, name="bilde", curie=FINT.curie('bilde'),
                   model_uri=RES.bilde, domain=None, range=Optional[str])

slots.bostedsadresse = Slot(uri=FINT.bostedsadresse, name="bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=RES.bostedsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.fodselsdato = Slot(uri=FINT.fodselsdato, name="fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=RES.fodselsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.fodselsnummer = Slot(uri=FINT.fodselsnummer, name="fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=RES.fodselsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person_navn = Slot(uri=FINT.personNavn, name="person_navn", curie=FINT.curie('personNavn'),
                   model_uri=RES.person_navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.parorende = Slot(uri=FINT.parorende, name="parorende", curie=FINT.curie('parorende'),
                   model_uri=RES.parorende, domain=None, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.statsborgerskap = Slot(uri=FINT.statsborgerskap, name="statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=RES.statsborgerskap, domain=None, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.foreldreansvar = Slot(uri=FINT.foreldreansvar, name="foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=RES.foreldreansvar, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.foreldre = Slot(uri=FINT.foreldre, name="foreldre", curie=FINT.curie('foreldre'),
                   model_uri=RES.foreldre, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.maalform = Slot(uri=FINT.maalform, name="maalform", curie=FINT.curie('maalform'),
                   model_uri=RES.maalform, domain=None, range=Optional[Union[str, SpraakId]])

slots.morsmaal = Slot(uri=FINT.morsmaal, name="morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=RES.morsmaal, domain=None, range=Optional[Union[str, SpraakId]])

slots.laerling = Slot(uri=FINT.laerling, name="laerling", curie=FINT.curie('laerling'),
                   model_uri=RES.laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.elev = Slot(uri=FINT.elev, name="elev", curie=FINT.curie('elev'),
                   model_uri=RES.elev, domain=None, range=Optional[Union[str, ElevId]])

slots.elevnummer = Slot(uri=FINT.elevnummer, name="elevnummer", curie=FINT.curie('elevnummer'),
                   model_uri=RES.elevnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person = Slot(uri=FINT.person, name="person", curie=FINT.curie('person'),
                   model_uri=RES.person, domain=None, range=Optional[Union[str, PersonId]])

slots.otungdom = Slot(uri=FINT.otungdom, name="otungdom", curie=FINT.curie('otungdom'),
                   model_uri=RES.otungdom, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kontaktperson_navn = Slot(uri=FINT.kontaktpersonNavn, name="kontaktperson_navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=RES.kontaktperson_navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.type = Slot(uri=FINT.type, name="type", curie=FINT.curie('type'),
                   model_uri=RES.type, domain=None, range=Optional[str])

slots.kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=RES.kontaktperson, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.virksomhetsId = Slot(uri=FINT.virksomhetsId, name="virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=RES.virksomhetsId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.ressursContainer__applikasjonar = Slot(uri=RES.applikasjonar, name="ressursContainer__applikasjonar", curie=RES.curie('applikasjonar'),
                   model_uri=RES.ressursContainer__applikasjonar, domain=None, range=Optional[Union[dict[Union[str, ApplikasjonId], Union[dict, Applikasjon]], list[Union[dict, Applikasjon]]]])

slots.ressursContainer__applikasjonsressursar = Slot(uri=RES.applikasjonsressursar, name="ressursContainer__applikasjonsressursar", curie=RES.curie('applikasjonsressursar'),
                   model_uri=RES.ressursContainer__applikasjonsressursar, domain=None, range=Optional[Union[dict[Union[str, ApplikasjonsressursId], Union[dict, Applikasjonsressurs]], list[Union[dict, Applikasjonsressurs]]]])

slots.ressursContainer__applikasjonsressurstilgjengelegheit = Slot(uri=RES.applikasjonsressurstilgjengelegheit, name="ressursContainer__applikasjonsressurstilgjengelegheit", curie=RES.curie('applikasjonsressurstilgjengelegheit'),
                   model_uri=RES.ressursContainer__applikasjonsressurstilgjengelegheit, domain=None, range=Optional[Union[dict[Union[str, ApplikasjonsressurstilgjengelighetId], Union[dict, Applikasjonsressurstilgjengelighet]], list[Union[dict, Applikasjonsressurstilgjengelighet]]]])

slots.ressursContainer__digitaleEiningar = Slot(uri=RES.digitaleEiningar, name="ressursContainer__digitaleEiningar", curie=RES.curie('digitaleEiningar'),
                   model_uri=RES.ressursContainer__digitaleEiningar, domain=None, range=Optional[Union[dict[Union[str, DigitalEnhetId], Union[dict, DigitalEnhet]], list[Union[dict, DigitalEnhet]]]])

slots.ressursContainer__einingsgrupper = Slot(uri=RES.einingsgrupper, name="ressursContainer__einingsgrupper", curie=RES.curie('einingsgrupper'),
                   model_uri=RES.ressursContainer__einingsgrupper, domain=None, range=Optional[Union[dict[Union[str, EnhetsgruppeId], Union[dict, Enhetsgruppe]], list[Union[dict, Enhetsgruppe]]]])

slots.ressursContainer__einingsgruppedmedlemskap = Slot(uri=RES.einingsgruppedmedlemskap, name="ressursContainer__einingsgruppedmedlemskap", curie=RES.curie('einingsgruppedmedlemskap'),
                   model_uri=RES.ressursContainer__einingsgruppedmedlemskap, domain=None, range=Optional[Union[dict[Union[str, EnhetsgruppemedlemskapId], Union[dict, Enhetsgruppemedlemskap]], list[Union[dict, Enhetsgruppemedlemskap]]]])

slots.ressursContainer__identitetar = Slot(uri=RES.identitetar, name="ressursContainer__identitetar", curie=RES.curie('identitetar'),
                   model_uri=RES.ressursContainer__identitetar, domain=None, range=Optional[Union[dict[Union[str, IdentitetId], Union[dict, Identitet]], list[Union[dict, Identitet]]]])

slots.ressursContainer__rettigheiter = Slot(uri=RES.rettigheiter, name="ressursContainer__rettigheiter", curie=RES.curie('rettigheiter'),
                   model_uri=RES.ressursContainer__rettigheiter, domain=None, range=Optional[Union[dict[Union[str, RettighetId], Union[dict, Rettighet]], list[Union[dict, Rettighet]]]])

slots.ressursContainer__applikasjonskategoriar = Slot(uri=RES.applikasjonskategoriar, name="ressursContainer__applikasjonskategoriar", curie=RES.curie('applikasjonskategoriar'),
                   model_uri=RES.ressursContainer__applikasjonskategoriar, domain=None, range=Optional[Union[dict[Union[str, ApplikasjonskategoriId], Union[dict, Applikasjonskategori]], list[Union[dict, Applikasjonskategori]]]])

slots.ressursContainer__brukertypar = Slot(uri=RES.brukertypar, name="ressursContainer__brukertypar", curie=RES.curie('brukertypar'),
                   model_uri=RES.ressursContainer__brukertypar, domain=None, range=Optional[Union[dict[Union[str, BrukertypeId], Union[dict, Brukertype]], list[Union[dict, Brukertype]]]])

slots.ressursContainer__einingstypar = Slot(uri=RES.einingstypar, name="ressursContainer__einingstypar", curie=RES.curie('einingstypar'),
                   model_uri=RES.ressursContainer__einingstypar, domain=None, range=Optional[Union[dict[Union[str, EnhetstypeId], Union[dict, Enhetstype]], list[Union[dict, Enhetstype]]]])

slots.ressursContainer__handhaevingstypar = Slot(uri=RES.handhaevingstypar, name="ressursContainer__handhaevingstypar", curie=RES.curie('handhaevingstypar'),
                   model_uri=RES.ressursContainer__handhaevingstypar, domain=None, range=Optional[Union[dict[Union[str, HandhevingstypeId], Union[dict, Handhevingstype]], list[Union[dict, Handhevingstype]]]])

slots.ressursContainer__lisensmodellar = Slot(uri=RES.lisensmodellar, name="ressursContainer__lisensmodellar", curie=RES.curie('lisensmodellar'),
                   model_uri=RES.ressursContainer__lisensmodellar, domain=None, range=Optional[Union[dict[Union[str, LisensmodellId], Union[dict, Lisensmodell]], list[Union[dict, Lisensmodell]]]])

slots.ressursContainer__plattformar = Slot(uri=RES.plattformar, name="ressursContainer__plattformar", curie=RES.curie('plattformar'),
                   model_uri=RES.ressursContainer__plattformar, domain=None, range=Optional[Union[dict[Union[str, PlattformId], Union[dict, Plattform]], list[Union[dict, Plattform]]]])

slots.ressursContainer__produsentar = Slot(uri=RES.produsentar, name="ressursContainer__produsentar", curie=RES.curie('produsentar'),
                   model_uri=RES.ressursContainer__produsentar, domain=None, range=Optional[Union[dict[Union[str, ProdusentId], Union[dict, Produsent]], list[Union[dict, Produsent]]]])

slots.ressursContainer__statusar = Slot(uri=RES.statusar, name="ressursContainer__statusar", curie=RES.curie('statusar'),
                   model_uri=RES.ressursContainer__statusar, domain=None, range=Optional[Union[dict[Union[str, StatusId], Union[dict, Status]], list[Union[dict, Status]]]])

slots.person__personalressurs = Slot(uri=FINT.personalressurs, name="person__personalressurs", curie=FINT.curie('personalressurs'),
                   model_uri=RES.person__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.Applikasjon_navn = Slot(uri=FINT.navn, name="Applikasjon_navn", curie=FINT.curie('navn'),
                   model_uri=RES.Applikasjon_navn, domain=Applikasjon, range=str)

slots.Applikasjon_beskrivelse = Slot(uri=FINT.beskrivelse, name="Applikasjon_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=RES.Applikasjon_beskrivelse, domain=Applikasjon, range=Optional[str])

slots.Applikasjon_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Applikasjon_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.Applikasjon_gyldighetsperiode, domain=Applikasjon, range=Union[dict, "Periode"])

slots.Applikasjon_plattform = Slot(uri=RES.plattform, name="Applikasjon_plattform", curie=RES.curie('plattform'),
                   model_uri=RES.Applikasjon_plattform, domain=Applikasjon, range=Optional[Union[Union[str, PlattformId], list[Union[str, PlattformId]]]])

slots.Applikasjon_applikasjonsressurs = Slot(uri=RES.applikasjonsressurs, name="Applikasjon_applikasjonsressurs", curie=RES.curie('applikasjonsressurs'),
                   model_uri=RES.Applikasjon_applikasjonsressurs, domain=Applikasjon, range=Optional[Union[Union[str, ApplikasjonsressursId], list[Union[str, ApplikasjonsressursId]]]])

slots.Applikasjon_applikasjonskategori = Slot(uri=RES.applikasjonskategori, name="Applikasjon_applikasjonskategori", curie=RES.curie('applikasjonskategori'),
                   model_uri=RES.Applikasjon_applikasjonskategori, domain=Applikasjon, range=Optional[Union[Union[str, ApplikasjonskategoriId], list[Union[str, ApplikasjonskategoriId]]]])

slots.Applikasjonsressurs_navn = Slot(uri=FINT.navn, name="Applikasjonsressurs_navn", curie=FINT.curie('navn'),
                   model_uri=RES.Applikasjonsressurs_navn, domain=Applikasjonsressurs, range=str)

slots.Applikasjonsressurs_beskrivelse = Slot(uri=FINT.beskrivelse, name="Applikasjonsressurs_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=RES.Applikasjonsressurs_beskrivelse, domain=Applikasjonsressurs, range=Optional[str])

slots.Applikasjonsressurs_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Applikasjonsressurs_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.Applikasjonsressurs_gyldighetsperiode, domain=Applikasjonsressurs, range=Union[dict, "Periode"])

slots.Applikasjonsressurs_enhetskostnad = Slot(uri=RES.enhetskostnad, name="Applikasjonsressurs_enhetskostnad", curie=RES.curie('enhetskostnad'),
                   model_uri=RES.Applikasjonsressurs_enhetskostnad, domain=Applikasjonsressurs, range=Optional[int])

slots.Applikasjonsressurs_kreverGodkjenning = Slot(uri=RES.kreverGodkjenning, name="Applikasjonsressurs_kreverGodkjenning", curie=RES.curie('kreverGodkjenning'),
                   model_uri=RES.Applikasjonsressurs_kreverGodkjenning, domain=Applikasjonsressurs, range=Optional[Union[bool, Bool]])

slots.Applikasjonsressurs_lisensantall = Slot(uri=RES.lisensantall, name="Applikasjonsressurs_lisensantall", curie=RES.curie('lisensantall'),
                   model_uri=RES.Applikasjonsressurs_lisensantall, domain=Applikasjonsressurs, range=Optional[int])

slots.Applikasjonsressurs_eier = Slot(uri=RES.eier, name="Applikasjonsressurs_eier", curie=RES.curie('eier'),
                   model_uri=RES.Applikasjonsressurs_eier, domain=Applikasjonsressurs, range=Union[str, URIorCURIE])

slots.Applikasjonsressurs_applikasjon = Slot(uri=RES.applikasjon, name="Applikasjonsressurs_applikasjon", curie=RES.curie('applikasjon'),
                   model_uri=RES.Applikasjonsressurs_applikasjon, domain=Applikasjonsressurs, range=Union[str, ApplikasjonId])

slots.Applikasjonsressurs_brukertype = Slot(uri=RES.brukertype, name="Applikasjonsressurs_brukertype", curie=RES.curie('brukertype'),
                   model_uri=RES.Applikasjonsressurs_brukertype, domain=Applikasjonsressurs, range=Union[Union[str, BrukertypeId], list[Union[str, BrukertypeId]]])

slots.Applikasjonsressurs_handhevingstype = Slot(uri=RES.handhevingstype, name="Applikasjonsressurs_handhevingstype", curie=RES.curie('handhevingstype'),
                   model_uri=RES.Applikasjonsressurs_handhevingstype, domain=Applikasjonsressurs, range=Optional[Union[str, HandhevingstypeId]])

slots.Applikasjonsressurs_lisensmodell = Slot(uri=RES.lisensmodell, name="Applikasjonsressurs_lisensmodell", curie=RES.curie('lisensmodell'),
                   model_uri=RES.Applikasjonsressurs_lisensmodell, domain=Applikasjonsressurs, range=Optional[Union[str, LisensmodellId]])

slots.Applikasjonsressurs_ressurstilgjengelighet = Slot(uri=RES.ressurstilgjengelighet, name="Applikasjonsressurs_ressurstilgjengelighet", curie=RES.curie('ressurstilgjengelighet'),
                   model_uri=RES.Applikasjonsressurs_ressurstilgjengelighet, domain=Applikasjonsressurs, range=Optional[Union[Union[str, ApplikasjonsressurstilgjengelighetId], list[Union[str, ApplikasjonsressurstilgjengelighetId]]]])

slots.Applikasjonsressurstilgjengelighet_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Applikasjonsressurstilgjengelighet_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.Applikasjonsressurstilgjengelighet_gyldighetsperiode, domain=Applikasjonsressurstilgjengelighet, range=Union[dict, "Periode"])

slots.Applikasjonsressurstilgjengelighet_lisensantall = Slot(uri=RES.lisensantall, name="Applikasjonsressurstilgjengelighet_lisensantall", curie=RES.curie('lisensantall'),
                   model_uri=RES.Applikasjonsressurstilgjengelighet_lisensantall, domain=Applikasjonsressurstilgjengelighet, range=Optional[int])

slots.Applikasjonsressurstilgjengelighet_konsument = Slot(uri=RES.konsument, name="Applikasjonsressurstilgjengelighet_konsument", curie=RES.curie('konsument'),
                   model_uri=RES.Applikasjonsressurstilgjengelighet_konsument, domain=Applikasjonsressurstilgjengelighet, range=Union[str, URIorCURIE])

slots.Applikasjonsressurstilgjengelighet_ressursRef = Slot(uri=RES.ressursRef, name="Applikasjonsressurstilgjengelighet_ressursRef", curie=RES.curie('ressursRef'),
                   model_uri=RES.Applikasjonsressurstilgjengelighet_ressursRef, domain=Applikasjonsressurstilgjengelighet, range=Union[str, ApplikasjonsressursId])

slots.DigitalEnhet_serienummer = Slot(uri=RES.serienummer, name="DigitalEnhet_serienummer", curie=RES.curie('serienummer'),
                   model_uri=RES.DigitalEnhet_serienummer, domain=DigitalEnhet, range=str)

slots.DigitalEnhet_navn = Slot(uri=FINT.navn, name="DigitalEnhet_navn", curie=FINT.curie('navn'),
                   model_uri=RES.DigitalEnhet_navn, domain=DigitalEnhet, range=Optional[str])

slots.DigitalEnhet_dataobjektId = Slot(uri=RES.dataobjektId, name="DigitalEnhet_dataobjektId", curie=RES.curie('dataobjektId'),
                   model_uri=RES.DigitalEnhet_dataobjektId, domain=DigitalEnhet, range=Optional[Union[dict, "Identifikator"]])

slots.DigitalEnhet_flerbrukerenhet = Slot(uri=RES.flerbrukerenhet, name="DigitalEnhet_flerbrukerenhet", curie=RES.curie('flerbrukerenhet'),
                   model_uri=RES.DigitalEnhet_flerbrukerenhet, domain=DigitalEnhet, range=Optional[Union[bool, Bool]])

slots.DigitalEnhet_privateid = Slot(uri=RES.privateid, name="DigitalEnhet_privateid", curie=RES.curie('privateid'),
                   model_uri=RES.DigitalEnhet_privateid, domain=DigitalEnhet, range=Optional[Union[bool, Bool]])

slots.DigitalEnhet_administrator = Slot(uri=RES.administrator, name="DigitalEnhet_administrator", curie=RES.curie('administrator'),
                   model_uri=RES.DigitalEnhet_administrator, domain=DigitalEnhet, range=Union[str, URIorCURIE])

slots.DigitalEnhet_eier = Slot(uri=RES.eier, name="DigitalEnhet_eier", curie=RES.curie('eier'),
                   model_uri=RES.DigitalEnhet_eier, domain=DigitalEnhet, range=Optional[Union[str, URIorCURIE]])

slots.DigitalEnhet_personalressurs = Slot(uri=RES.personalressurs, name="DigitalEnhet_personalressurs", curie=RES.curie('personalressurs'),
                   model_uri=RES.DigitalEnhet_personalressurs, domain=DigitalEnhet, range=Optional[Union[str, URIorCURIE]])

slots.DigitalEnhet_elev = Slot(uri=FINT.elev, name="DigitalEnhet_elev", curie=FINT.curie('elev'),
                   model_uri=RES.DigitalEnhet_elev, domain=DigitalEnhet, range=Optional[Union[str, ElevId]])

slots.DigitalEnhet_status = Slot(uri=RES.status, name="DigitalEnhet_status", curie=RES.curie('status'),
                   model_uri=RES.DigitalEnhet_status, domain=DigitalEnhet, range=Optional[Union[str, StatusId]])

slots.DigitalEnhet_enhetstype = Slot(uri=RES.enhetstype, name="DigitalEnhet_enhetstype", curie=RES.curie('enhetstype'),
                   model_uri=RES.DigitalEnhet_enhetstype, domain=DigitalEnhet, range=Union[str, EnhetstypeId])

slots.DigitalEnhet_plattform = Slot(uri=RES.plattform, name="DigitalEnhet_plattform", curie=RES.curie('plattform'),
                   model_uri=RES.DigitalEnhet_plattform, domain=DigitalEnhet, range=Union[str, PlattformId])

slots.DigitalEnhet_produsent = Slot(uri=RES.produsent, name="DigitalEnhet_produsent", curie=RES.curie('produsent'),
                   model_uri=RES.DigitalEnhet_produsent, domain=DigitalEnhet, range=Optional[Union[str, ProdusentId]])

slots.DigitalEnhet_enhetsgruppemedlemskap = Slot(uri=RES.enhetsgruppemedlemskap, name="DigitalEnhet_enhetsgruppemedlemskap", curie=RES.curie('enhetsgruppemedlemskap'),
                   model_uri=RES.DigitalEnhet_enhetsgruppemedlemskap, domain=DigitalEnhet, range=Optional[Union[Union[str, EnhetsgruppemedlemskapId], list[Union[str, EnhetsgruppemedlemskapId]]]])

slots.Enhetsgruppe_navn = Slot(uri=FINT.navn, name="Enhetsgruppe_navn", curie=FINT.curie('navn'),
                   model_uri=RES.Enhetsgruppe_navn, domain=Enhetsgruppe, range=str)

slots.Enhetsgruppe_organisasjonsenhet = Slot(uri=RES.organisasjonsenhet, name="Enhetsgruppe_organisasjonsenhet", curie=RES.curie('organisasjonsenhet'),
                   model_uri=RES.Enhetsgruppe_organisasjonsenhet, domain=Enhetsgruppe, range=Union[str, URIorCURIE])

slots.Enhetsgruppe_enhetstype = Slot(uri=RES.enhetstype, name="Enhetsgruppe_enhetstype", curie=RES.curie('enhetstype'),
                   model_uri=RES.Enhetsgruppe_enhetstype, domain=Enhetsgruppe, range=Union[str, EnhetstypeId])

slots.Enhetsgruppe_plattform = Slot(uri=RES.plattform, name="Enhetsgruppe_plattform", curie=RES.curie('plattform'),
                   model_uri=RES.Enhetsgruppe_plattform, domain=Enhetsgruppe, range=Union[str, PlattformId])

slots.Enhetsgruppe_enhetsgruppemedlemskap = Slot(uri=RES.enhetsgruppemedlemskap, name="Enhetsgruppe_enhetsgruppemedlemskap", curie=RES.curie('enhetsgruppemedlemskap'),
                   model_uri=RES.Enhetsgruppe_enhetsgruppemedlemskap, domain=Enhetsgruppe, range=Optional[Union[Union[str, EnhetsgruppemedlemskapId], list[Union[str, EnhetsgruppemedlemskapId]]]])

slots.Enhetsgruppemedlemskap_digitalEnhet = Slot(uri=RES.digitalEnhet, name="Enhetsgruppemedlemskap_digitalEnhet", curie=RES.curie('digitalEnhet'),
                   model_uri=RES.Enhetsgruppemedlemskap_digitalEnhet, domain=Enhetsgruppemedlemskap, range=Union[str, DigitalEnhetId])

slots.Enhetsgruppemedlemskap_enhetsgruppe = Slot(uri=RES.enhetsgruppe, name="Enhetsgruppemedlemskap_enhetsgruppe", curie=RES.curie('enhetsgruppe'),
                   model_uri=RES.Enhetsgruppemedlemskap_enhetsgruppe, domain=Enhetsgruppemedlemskap, range=Union[str, EnhetsgruppeId])

slots.Identitet_personalressurs = Slot(uri=RES.personalressurs, name="Identitet_personalressurs", curie=RES.curie('personalressurs'),
                   model_uri=RES.Identitet_personalressurs, domain=Identitet, range=Optional[Union[str, URIorCURIE]])

slots.Identitet_rettighet = Slot(uri=RES.rettighet, name="Identitet_rettighet", curie=RES.curie('rettighet'),
                   model_uri=RES.Identitet_rettighet, domain=Identitet, range=Optional[Union[Union[str, RettighetId], list[Union[str, RettighetId]]]])

slots.Rettighet_kode = Slot(uri=FINT.kode, name="Rettighet_kode", curie=FINT.curie('kode'),
                   model_uri=RES.Rettighet_kode, domain=Rettighet, range=str)

slots.Rettighet_navn = Slot(uri=FINT.navn, name="Rettighet_navn", curie=FINT.curie('navn'),
                   model_uri=RES.Rettighet_navn, domain=Rettighet, range=str)

slots.Rettighet_beskrivelse = Slot(uri=FINT.beskrivelse, name="Rettighet_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=RES.Rettighet_beskrivelse, domain=Rettighet, range=str)

slots.Rettighet_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Rettighet_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.Rettighet_gyldighetsperiode, domain=Rettighet, range=Optional[Union[dict, "Periode"]])

slots.Rettighet_passiv = Slot(uri=FINT.passiv, name="Rettighet_passiv", curie=FINT.curie('passiv'),
                   model_uri=RES.Rettighet_passiv, domain=Rettighet, range=Optional[Union[bool, Bool]])

slots.Rettighet_identitet = Slot(uri=RES.identitet, name="Rettighet_identitet", curie=RES.curie('identitet'),
                   model_uri=RES.Rettighet_identitet, domain=Rettighet, range=Optional[Union[Union[str, IdentitetId], list[Union[str, IdentitetId]]]])

slots.Applikasjonskategori_kode = Slot(uri=FINT.kode, name="Applikasjonskategori_kode", curie=FINT.curie('kode'),
                   model_uri=RES.Applikasjonskategori_kode, domain=Applikasjonskategori, range=str)

slots.Applikasjonskategori_navn = Slot(uri=FINT.navn, name="Applikasjonskategori_navn", curie=FINT.curie('navn'),
                   model_uri=RES.Applikasjonskategori_navn, domain=Applikasjonskategori, range=str)

slots.Applikasjonskategori_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Applikasjonskategori_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.Applikasjonskategori_gyldighetsperiode, domain=Applikasjonskategori, range=Optional[Union[dict, "Periode"]])

slots.Applikasjonskategori_passiv = Slot(uri=FINT.passiv, name="Applikasjonskategori_passiv", curie=FINT.curie('passiv'),
                   model_uri=RES.Applikasjonskategori_passiv, domain=Applikasjonskategori, range=Optional[Union[bool, Bool]])

slots.Brukertype_kode = Slot(uri=FINT.kode, name="Brukertype_kode", curie=FINT.curie('kode'),
                   model_uri=RES.Brukertype_kode, domain=Brukertype, range=str)

slots.Brukertype_navn = Slot(uri=FINT.navn, name="Brukertype_navn", curie=FINT.curie('navn'),
                   model_uri=RES.Brukertype_navn, domain=Brukertype, range=str)

slots.Brukertype_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Brukertype_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.Brukertype_gyldighetsperiode, domain=Brukertype, range=Optional[Union[dict, "Periode"]])

slots.Brukertype_passiv = Slot(uri=FINT.passiv, name="Brukertype_passiv", curie=FINT.curie('passiv'),
                   model_uri=RES.Brukertype_passiv, domain=Brukertype, range=Optional[Union[bool, Bool]])

slots.Enhetstype_kode = Slot(uri=FINT.kode, name="Enhetstype_kode", curie=FINT.curie('kode'),
                   model_uri=RES.Enhetstype_kode, domain=Enhetstype, range=str)

slots.Enhetstype_navn = Slot(uri=FINT.navn, name="Enhetstype_navn", curie=FINT.curie('navn'),
                   model_uri=RES.Enhetstype_navn, domain=Enhetstype, range=str)

slots.Enhetstype_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Enhetstype_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.Enhetstype_gyldighetsperiode, domain=Enhetstype, range=Optional[Union[dict, "Periode"]])

slots.Enhetstype_passiv = Slot(uri=FINT.passiv, name="Enhetstype_passiv", curie=FINT.curie('passiv'),
                   model_uri=RES.Enhetstype_passiv, domain=Enhetstype, range=Optional[Union[bool, Bool]])

slots.Handhevingstype_kode = Slot(uri=FINT.kode, name="Handhevingstype_kode", curie=FINT.curie('kode'),
                   model_uri=RES.Handhevingstype_kode, domain=Handhevingstype, range=str)

slots.Handhevingstype_navn = Slot(uri=FINT.navn, name="Handhevingstype_navn", curie=FINT.curie('navn'),
                   model_uri=RES.Handhevingstype_navn, domain=Handhevingstype, range=str)

slots.Handhevingstype_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Handhevingstype_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.Handhevingstype_gyldighetsperiode, domain=Handhevingstype, range=Optional[Union[dict, "Periode"]])

slots.Handhevingstype_passiv = Slot(uri=FINT.passiv, name="Handhevingstype_passiv", curie=FINT.curie('passiv'),
                   model_uri=RES.Handhevingstype_passiv, domain=Handhevingstype, range=Optional[Union[bool, Bool]])

slots.Lisensmodell_kode = Slot(uri=FINT.kode, name="Lisensmodell_kode", curie=FINT.curie('kode'),
                   model_uri=RES.Lisensmodell_kode, domain=Lisensmodell, range=str)

slots.Lisensmodell_navn = Slot(uri=FINT.navn, name="Lisensmodell_navn", curie=FINT.curie('navn'),
                   model_uri=RES.Lisensmodell_navn, domain=Lisensmodell, range=str)

slots.Lisensmodell_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Lisensmodell_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.Lisensmodell_gyldighetsperiode, domain=Lisensmodell, range=Optional[Union[dict, "Periode"]])

slots.Lisensmodell_passiv = Slot(uri=FINT.passiv, name="Lisensmodell_passiv", curie=FINT.curie('passiv'),
                   model_uri=RES.Lisensmodell_passiv, domain=Lisensmodell, range=Optional[Union[bool, Bool]])

slots.Plattform_kode = Slot(uri=FINT.kode, name="Plattform_kode", curie=FINT.curie('kode'),
                   model_uri=RES.Plattform_kode, domain=Plattform, range=str)

slots.Plattform_navn = Slot(uri=FINT.navn, name="Plattform_navn", curie=FINT.curie('navn'),
                   model_uri=RES.Plattform_navn, domain=Plattform, range=str)

slots.Plattform_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Plattform_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.Plattform_gyldighetsperiode, domain=Plattform, range=Optional[Union[dict, "Periode"]])

slots.Plattform_passiv = Slot(uri=FINT.passiv, name="Plattform_passiv", curie=FINT.curie('passiv'),
                   model_uri=RES.Plattform_passiv, domain=Plattform, range=Optional[Union[bool, Bool]])

slots.Produsent_kode = Slot(uri=FINT.kode, name="Produsent_kode", curie=FINT.curie('kode'),
                   model_uri=RES.Produsent_kode, domain=Produsent, range=str)

slots.Produsent_navn = Slot(uri=FINT.navn, name="Produsent_navn", curie=FINT.curie('navn'),
                   model_uri=RES.Produsent_navn, domain=Produsent, range=str)

slots.Produsent_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Produsent_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.Produsent_gyldighetsperiode, domain=Produsent, range=Optional[Union[dict, "Periode"]])

slots.Produsent_passiv = Slot(uri=FINT.passiv, name="Produsent_passiv", curie=FINT.curie('passiv'),
                   model_uri=RES.Produsent_passiv, domain=Produsent, range=Optional[Union[bool, Bool]])

slots.Status_kode = Slot(uri=FINT.kode, name="Status_kode", curie=FINT.curie('kode'),
                   model_uri=RES.Status_kode, domain=Status, range=str)

slots.Status_navn = Slot(uri=FINT.navn, name="Status_navn", curie=FINT.curie('navn'),
                   model_uri=RES.Status_navn, domain=Status, range=str)

slots.Status_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Status_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.Status_gyldighetsperiode, domain=Status, range=Optional[Union[dict, "Periode"]])

slots.Status_passiv = Slot(uri=FINT.passiv, name="Status_passiv", curie=FINT.curie('passiv'),
                   model_uri=RES.Status_passiv, domain=Status, range=Optional[Union[bool, Bool]])

slots.Aktoer_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Aktoer_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=RES.Aktoer_kontaktinformasjon, domain=Aktoer, range=Optional[Union[dict, "Kontaktinformasjon"]])

slots.Aktoer_postadresse = Slot(uri=FINT.postadresse, name="Aktoer_postadresse", curie=FINT.curie('postadresse'),
                   model_uri=RES.Aktoer_postadresse, domain=Aktoer, range=Optional[Union[dict, "Adresse"]])

slots.Begrep_kode = Slot(uri=FINT.kode, name="Begrep_kode", curie=FINT.curie('kode'),
                   model_uri=RES.Begrep_kode, domain=Begrep, range=str)

slots.Begrep_navn = Slot(uri=FINT.navn, name="Begrep_navn", curie=FINT.curie('navn'),
                   model_uri=RES.Begrep_navn, domain=Begrep, range=str)

slots.Begrep_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Begrep_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.Begrep_gyldighetsperiode, domain=Begrep, range=Optional[Union[dict, "Periode"]])

slots.Begrep_passiv = Slot(uri=FINT.passiv, name="Begrep_passiv", curie=FINT.curie('passiv'),
                   model_uri=RES.Begrep_passiv, domain=Begrep, range=Optional[Union[bool, Bool]])

slots.Elev_elevnummer = Slot(uri=FINT.elevnummer, name="Elev_elevnummer", curie=FINT.curie('elevnummer'),
                   model_uri=RES.Elev_elevnummer, domain=Elev, range=Optional[Union[dict, "Identifikator"]])

slots.Elev_person = Slot(uri=FINT.person, name="Elev_person", curie=FINT.curie('person'),
                   model_uri=RES.Elev_person, domain=Elev, range=Optional[Union[str, PersonId]])

slots.Enhet_forretningsadresse = Slot(uri=FINT.forretningsadresse, name="Enhet_forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=RES.Enhet_forretningsadresse, domain=Enhet, range=Optional[Union[dict, "Adresse"]])

slots.Enhet_organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="Enhet_organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=RES.Enhet_organisasjonsnavn, domain=Enhet, range=Optional[str])

slots.Enhet_organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="Enhet_organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=RES.Enhet_organisasjonsnummer, domain=Enhet, range=Optional[Union[dict, "Identifikator"]])

slots.Identifikator_identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="Identifikator_identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=RES.Identifikator_identifikatorverdi, domain=Identifikator, range=str)

slots.Periode_start = Slot(uri=FINT.start, name="Periode_start", curie=FINT.curie('start'),
                   model_uri=RES.Periode_start, domain=Periode, range=Union[str, XSDDateTime])

slots.Personnavn_fornavn = Slot(uri=FINT.fornavn, name="Personnavn_fornavn", curie=FINT.curie('fornavn'),
                   model_uri=RES.Personnavn_fornavn, domain=Personnavn, range=str)

slots.Personnavn_etternavn = Slot(uri=FINT.etternavn, name="Personnavn_etternavn", curie=FINT.curie('etternavn'),
                   model_uri=RES.Personnavn_etternavn, domain=Personnavn, range=str)

slots.Fylke_kommune = Slot(uri=FINT.kommune, name="Fylke_kommune", curie=FINT.curie('kommune'),
                   model_uri=RES.Fylke_kommune, domain=Fylke, range=Optional[Union[Union[str, KommuneId], list[Union[str, KommuneId]]]])

slots.Kommune_fylke = Slot(uri=FINT.fylke, name="Kommune_fylke", curie=FINT.curie('fylke'),
                   model_uri=RES.Kommune_fylke, domain=Kommune, range=Union[str, FylkeId])

slots.Valuta_bokstavkode = Slot(uri=FINT.bokstavkode, name="Valuta_bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=RES.Valuta_bokstavkode, domain=Valuta, range=Union[dict, Identifikator])

slots.Valuta_valuta_navn = Slot(uri=FINT.valutaNavn, name="Valuta_valuta_navn", curie=FINT.curie('valutaNavn'),
                   model_uri=RES.Valuta_valuta_navn, domain=Valuta, range=str)

slots.Valuta_nummerkode = Slot(uri=FINT.nummerkode, name="Valuta_nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=RES.Valuta_nummerkode, domain=Valuta, range=Union[dict, Identifikator])

slots.Person_fodselsnummer = Slot(uri=FINT.fodselsnummer, name="Person_fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=RES.Person_fodselsnummer, domain=Person, range=Union[dict, Identifikator])

slots.Person_person_navn = Slot(uri=FINT.personNavn, name="Person_person_navn", curie=FINT.curie('personNavn'),
                   model_uri=RES.Person_person_navn, domain=Person, range=Union[dict, Personnavn])

slots.Person_bilde = Slot(uri=FINT.bilde, name="Person_bilde", curie=FINT.curie('bilde'),
                   model_uri=RES.Person_bilde, domain=Person, range=Optional[str])

slots.Person_bostedsadresse = Slot(uri=FINT.bostedsadresse, name="Person_bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=RES.Person_bostedsadresse, domain=Person, range=Optional[Union[dict, Adresse]])

slots.Person_fodselsdato = Slot(uri=FINT.fodselsdato, name="Person_fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=RES.Person_fodselsdato, domain=Person, range=Optional[Union[str, XSDDate]])

slots.Person_parorende = Slot(uri=FINT.parorende, name="Person_parorende", curie=FINT.curie('parorende'),
                   model_uri=RES.Person_parorende, domain=Person, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.Person_statsborgerskap = Slot(uri=FINT.statsborgerskap, name="Person_statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=RES.Person_statsborgerskap, domain=Person, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.Person_kommune = Slot(uri=FINT.kommune, name="Person_kommune", curie=FINT.curie('kommune'),
                   model_uri=RES.Person_kommune, domain=Person, range=Optional[Union[str, KommuneId]])

slots.Person_kjonn = Slot(uri=FINT.kjonn, name="Person_kjonn", curie=FINT.curie('kjonn'),
                   model_uri=RES.Person_kjonn, domain=Person, range=Optional[Union[str, KjonnId]])

slots.Person_foreldreansvar = Slot(uri=FINT.foreldreansvar, name="Person_foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=RES.Person_foreldreansvar, domain=Person, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Person_foreldre = Slot(uri=FINT.foreldre, name="Person_foreldre", curie=FINT.curie('foreldre'),
                   model_uri=RES.Person_foreldre, domain=Person, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Person_maalform = Slot(uri=FINT.maalform, name="Person_maalform", curie=FINT.curie('maalform'),
                   model_uri=RES.Person_maalform, domain=Person, range=Optional[Union[str, SpraakId]])

slots.Person_morsmaal = Slot(uri=FINT.morsmaal, name="Person_morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=RES.Person_morsmaal, domain=Person, range=Optional[Union[str, SpraakId]])

slots.Person_laerling = Slot(uri=FINT.laerling, name="Person_laerling", curie=FINT.curie('laerling'),
                   model_uri=RES.Person_laerling, domain=Person, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Person_elev = Slot(uri=FINT.elev, name="Person_elev", curie=FINT.curie('elev'),
                   model_uri=RES.Person_elev, domain=Person, range=Optional[Union[str, ElevId]])

slots.Person_otungdom = Slot(uri=FINT.otungdom, name="Person_otungdom", curie=FINT.curie('otungdom'),
                   model_uri=RES.Person_otungdom, domain=Person, range=Optional[Union[str, URIorCURIE]])

slots.Kontaktperson_type = Slot(uri=FINT.type, name="Kontaktperson_type", curie=FINT.curie('type'),
                   model_uri=RES.Kontaktperson_type, domain=Kontaktperson, range=str)

slots.Kontaktperson_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Kontaktperson_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=RES.Kontaktperson_kontaktinformasjon, domain=Kontaktperson, range=Optional[Union[dict, Kontaktinformasjon]])

slots.Kontaktperson_kontaktperson_navn = Slot(uri=FINT.kontaktpersonNavn, name="Kontaktperson_kontaktperson_navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=RES.Kontaktperson_kontaktperson_navn, domain=Kontaktperson, range=Optional[Union[dict, Personnavn]])

slots.Kontaktperson_kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="Kontaktperson_kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=RES.Kontaktperson_kontaktperson, domain=Kontaktperson, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Virksomhet_virksomhetsId = Slot(uri=FINT.virksomhetsId, name="Virksomhet_virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=RES.Virksomhet_virksomhetsId, domain=Virksomhet, range=Union[dict, Identifikator])

slots.Virksomhet_laerling = Slot(uri=FINT.laerling, name="Virksomhet_laerling", curie=FINT.curie('laerling'),
                   model_uri=RES.Virksomhet_laerling, domain=Virksomhet, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

