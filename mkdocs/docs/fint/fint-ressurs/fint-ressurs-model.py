# Auto generated from fint-ressurs-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-05T13:28:08
# Schema: fint-ressurs
#
# id: https://data.norge.no/linkml/fint-ressurs
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

metamodel_version = "1.7.0"
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
    ressurs: Optional[Union[Union[str, ApplikasjonsressursId], list[Union[str, ApplikasjonsressursId]]]] = empty_list()
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

        if not isinstance(self.ressurs, list):
            self.ressurs = [self.ressurs] if self.ressurs is not None else []
        self.ressurs = [v if isinstance(v, ApplikasjonsressursId) else ApplikasjonsressursId(v) for v in self.ressurs]

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
    ressurs: Union[str, ApplikasjonsressursId] = None
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

        if self._is_empty(self.ressurs):
            self.MissingRequiredField("ressurs")
        if not isinstance(self.ressurs, ApplikasjonsressursId):
            self.ressurs = ApplikasjonsressursId(self.ressurs)

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
    elev: Optional[Union[str, URIorCURIE]] = None
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

        if self.elev is not None and not isinstance(self.elev, URIorCURIE):
            self.elev = URIorCURIE(self.elev)

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
    Ei gruppering av einsarta digitale einingar (t.d. klassesett med iPadar).
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
    Ei namngitt rettighet. Kva rettigheta gir tilgang til er systemspesifikt.
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
    Dei ulike brukartypane som kan nytte lisensen (t.d. Ansatt, Elev).
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
    Type digital eining (t.d. Mobiltelefon, Datamaskin, Nettbrett).
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
    Korleis ulike lisensmodellar kan handhevast (Håndhevingstype).
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
    Plattforma tenesta kan leverast på (t.d. Windows, macOS, iOS, Android).
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
    class_model_uri: ClassVar[URIRef] = RES.Person

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
    class_model_uri: ClassVar[URIRef] = RES.Kontaktperson

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

slots.id = Slot(uri=FINT.id, name="id", curie=FINT.curie('id'),
                   model_uri=RES.id, domain=None, range=URIRef)

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

slots.applikasjon__navn = Slot(uri=RES.navn, name="applikasjon__navn", curie=RES.curie('navn'),
                   model_uri=RES.applikasjon__navn, domain=None, range=str)

slots.applikasjon__beskrivelse = Slot(uri=RES.beskrivelse, name="applikasjon__beskrivelse", curie=RES.curie('beskrivelse'),
                   model_uri=RES.applikasjon__beskrivelse, domain=None, range=Optional[str])

slots.applikasjon__gyldighetsperiode = Slot(uri=RES.gyldighetsperiode, name="applikasjon__gyldighetsperiode", curie=RES.curie('gyldighetsperiode'),
                   model_uri=RES.applikasjon__gyldighetsperiode, domain=None, range=Union[dict, Periode])

slots.applikasjon__plattform = Slot(uri=RES.plattform, name="applikasjon__plattform", curie=RES.curie('plattform'),
                   model_uri=RES.applikasjon__plattform, domain=None, range=Optional[Union[Union[str, PlattformId], list[Union[str, PlattformId]]]])

slots.applikasjon__ressurs = Slot(uri=RES.applikasjonsressurs, name="applikasjon__ressurs", curie=RES.curie('applikasjonsressurs'),
                   model_uri=RES.applikasjon__ressurs, domain=None, range=Optional[Union[Union[str, ApplikasjonsressursId], list[Union[str, ApplikasjonsressursId]]]])

slots.applikasjon__applikasjonskategori = Slot(uri=RES.applikasjonskategori, name="applikasjon__applikasjonskategori", curie=RES.curie('applikasjonskategori'),
                   model_uri=RES.applikasjon__applikasjonskategori, domain=None, range=Optional[Union[Union[str, ApplikasjonskategoriId], list[Union[str, ApplikasjonskategoriId]]]])

slots.applikasjonsressurs__navn = Slot(uri=RES.navn, name="applikasjonsressurs__navn", curie=RES.curie('navn'),
                   model_uri=RES.applikasjonsressurs__navn, domain=None, range=str)

slots.applikasjonsressurs__beskrivelse = Slot(uri=RES.beskrivelse, name="applikasjonsressurs__beskrivelse", curie=RES.curie('beskrivelse'),
                   model_uri=RES.applikasjonsressurs__beskrivelse, domain=None, range=Optional[str])

slots.applikasjonsressurs__gyldighetsperiode = Slot(uri=RES.gyldighetsperiode, name="applikasjonsressurs__gyldighetsperiode", curie=RES.curie('gyldighetsperiode'),
                   model_uri=RES.applikasjonsressurs__gyldighetsperiode, domain=None, range=Union[dict, Periode])

slots.applikasjonsressurs__enhetskostnad = Slot(uri=RES.enhetskostnad, name="applikasjonsressurs__enhetskostnad", curie=RES.curie('enhetskostnad'),
                   model_uri=RES.applikasjonsressurs__enhetskostnad, domain=None, range=Optional[int])

slots.applikasjonsressurs__kreverGodkjenning = Slot(uri=RES.kreverGodkjenning, name="applikasjonsressurs__kreverGodkjenning", curie=RES.curie('kreverGodkjenning'),
                   model_uri=RES.applikasjonsressurs__kreverGodkjenning, domain=None, range=Optional[Union[bool, Bool]])

slots.applikasjonsressurs__lisensantall = Slot(uri=RES.lisensantall, name="applikasjonsressurs__lisensantall", curie=RES.curie('lisensantall'),
                   model_uri=RES.applikasjonsressurs__lisensantall, domain=None, range=Optional[int])

slots.applikasjonsressurs__eier = Slot(uri=RES.eier, name="applikasjonsressurs__eier", curie=RES.curie('eier'),
                   model_uri=RES.applikasjonsressurs__eier, domain=None, range=Union[str, URIorCURIE])

slots.applikasjonsressurs__applikasjon = Slot(uri=RES.applikasjon, name="applikasjonsressurs__applikasjon", curie=RES.curie('applikasjon'),
                   model_uri=RES.applikasjonsressurs__applikasjon, domain=None, range=Union[str, ApplikasjonId])

slots.applikasjonsressurs__brukertype = Slot(uri=RES.brukertype, name="applikasjonsressurs__brukertype", curie=RES.curie('brukertype'),
                   model_uri=RES.applikasjonsressurs__brukertype, domain=None, range=Union[Union[str, BrukertypeId], list[Union[str, BrukertypeId]]])

slots.applikasjonsressurs__handhevingstype = Slot(uri=RES.handhevingstype, name="applikasjonsressurs__handhevingstype", curie=RES.curie('handhevingstype'),
                   model_uri=RES.applikasjonsressurs__handhevingstype, domain=None, range=Optional[Union[str, HandhevingstypeId]])

slots.applikasjonsressurs__lisensmodell = Slot(uri=RES.lisensmodell, name="applikasjonsressurs__lisensmodell", curie=RES.curie('lisensmodell'),
                   model_uri=RES.applikasjonsressurs__lisensmodell, domain=None, range=Optional[Union[str, LisensmodellId]])

slots.applikasjonsressurs__ressurstilgjengelighet = Slot(uri=RES.ressurstilgjengelighet, name="applikasjonsressurs__ressurstilgjengelighet", curie=RES.curie('ressurstilgjengelighet'),
                   model_uri=RES.applikasjonsressurs__ressurstilgjengelighet, domain=None, range=Optional[Union[Union[str, ApplikasjonsressurstilgjengelighetId], list[Union[str, ApplikasjonsressurstilgjengelighetId]]]])

slots.applikasjonsressurstilgjengelighet__gyldighetsperiode = Slot(uri=RES.gyldighetsperiode, name="applikasjonsressurstilgjengelighet__gyldighetsperiode", curie=RES.curie('gyldighetsperiode'),
                   model_uri=RES.applikasjonsressurstilgjengelighet__gyldighetsperiode, domain=None, range=Union[dict, Periode])

slots.applikasjonsressurstilgjengelighet__lisensantall = Slot(uri=RES.lisensantall, name="applikasjonsressurstilgjengelighet__lisensantall", curie=RES.curie('lisensantall'),
                   model_uri=RES.applikasjonsressurstilgjengelighet__lisensantall, domain=None, range=Optional[int])

slots.applikasjonsressurstilgjengelighet__konsument = Slot(uri=RES.konsument, name="applikasjonsressurstilgjengelighet__konsument", curie=RES.curie('konsument'),
                   model_uri=RES.applikasjonsressurstilgjengelighet__konsument, domain=None, range=Union[str, URIorCURIE])

slots.applikasjonsressurstilgjengelighet__ressurs = Slot(uri=RES.ressursRef, name="applikasjonsressurstilgjengelighet__ressurs", curie=RES.curie('ressursRef'),
                   model_uri=RES.applikasjonsressurstilgjengelighet__ressurs, domain=None, range=Union[str, ApplikasjonsressursId])

slots.digitalEnhet__serienummer = Slot(uri=RES.serienummer, name="digitalEnhet__serienummer", curie=RES.curie('serienummer'),
                   model_uri=RES.digitalEnhet__serienummer, domain=None, range=str)

slots.digitalEnhet__navn = Slot(uri=RES.navn, name="digitalEnhet__navn", curie=RES.curie('navn'),
                   model_uri=RES.digitalEnhet__navn, domain=None, range=Optional[str])

slots.digitalEnhet__dataobjektId = Slot(uri=RES.dataobjektId, name="digitalEnhet__dataobjektId", curie=RES.curie('dataobjektId'),
                   model_uri=RES.digitalEnhet__dataobjektId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.digitalEnhet__flerbrukerenhet = Slot(uri=RES.flerbrukerenhet, name="digitalEnhet__flerbrukerenhet", curie=RES.curie('flerbrukerenhet'),
                   model_uri=RES.digitalEnhet__flerbrukerenhet, domain=None, range=Optional[Union[bool, Bool]])

slots.digitalEnhet__privateid = Slot(uri=RES.privateid, name="digitalEnhet__privateid", curie=RES.curie('privateid'),
                   model_uri=RES.digitalEnhet__privateid, domain=None, range=Optional[Union[bool, Bool]])

slots.digitalEnhet__administrator = Slot(uri=RES.administrator, name="digitalEnhet__administrator", curie=RES.curie('administrator'),
                   model_uri=RES.digitalEnhet__administrator, domain=None, range=Union[str, URIorCURIE])

slots.digitalEnhet__eier = Slot(uri=RES.eier, name="digitalEnhet__eier", curie=RES.curie('eier'),
                   model_uri=RES.digitalEnhet__eier, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.digitalEnhet__personalressurs = Slot(uri=RES.personalressurs, name="digitalEnhet__personalressurs", curie=RES.curie('personalressurs'),
                   model_uri=RES.digitalEnhet__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.digitalEnhet__elev = Slot(uri=RES.elev, name="digitalEnhet__elev", curie=RES.curie('elev'),
                   model_uri=RES.digitalEnhet__elev, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.digitalEnhet__status = Slot(uri=RES.status, name="digitalEnhet__status", curie=RES.curie('status'),
                   model_uri=RES.digitalEnhet__status, domain=None, range=Optional[Union[str, StatusId]])

slots.digitalEnhet__enhetstype = Slot(uri=RES.enhetstype, name="digitalEnhet__enhetstype", curie=RES.curie('enhetstype'),
                   model_uri=RES.digitalEnhet__enhetstype, domain=None, range=Union[str, EnhetstypeId])

slots.digitalEnhet__plattform = Slot(uri=RES.plattform, name="digitalEnhet__plattform", curie=RES.curie('plattform'),
                   model_uri=RES.digitalEnhet__plattform, domain=None, range=Union[str, PlattformId])

slots.digitalEnhet__produsent = Slot(uri=RES.produsent, name="digitalEnhet__produsent", curie=RES.curie('produsent'),
                   model_uri=RES.digitalEnhet__produsent, domain=None, range=Optional[Union[str, ProdusentId]])

slots.digitalEnhet__enhetsgruppemedlemskap = Slot(uri=RES.enhetsgruppemedlemskap, name="digitalEnhet__enhetsgruppemedlemskap", curie=RES.curie('enhetsgruppemedlemskap'),
                   model_uri=RES.digitalEnhet__enhetsgruppemedlemskap, domain=None, range=Optional[Union[Union[str, EnhetsgruppemedlemskapId], list[Union[str, EnhetsgruppemedlemskapId]]]])

slots.enhetsgruppe__navn = Slot(uri=RES.navn, name="enhetsgruppe__navn", curie=RES.curie('navn'),
                   model_uri=RES.enhetsgruppe__navn, domain=None, range=str)

slots.enhetsgruppe__organisasjonsenhet = Slot(uri=RES.organisasjonsenhet, name="enhetsgruppe__organisasjonsenhet", curie=RES.curie('organisasjonsenhet'),
                   model_uri=RES.enhetsgruppe__organisasjonsenhet, domain=None, range=Union[str, URIorCURIE])

slots.enhetsgruppe__enhetstype = Slot(uri=RES.enhetstype, name="enhetsgruppe__enhetstype", curie=RES.curie('enhetstype'),
                   model_uri=RES.enhetsgruppe__enhetstype, domain=None, range=Union[str, EnhetstypeId])

slots.enhetsgruppe__plattform = Slot(uri=RES.plattform, name="enhetsgruppe__plattform", curie=RES.curie('plattform'),
                   model_uri=RES.enhetsgruppe__plattform, domain=None, range=Union[str, PlattformId])

slots.enhetsgruppe__enhetsgruppemedlemskap = Slot(uri=RES.enhetsgruppemedlemskap, name="enhetsgruppe__enhetsgruppemedlemskap", curie=RES.curie('enhetsgruppemedlemskap'),
                   model_uri=RES.enhetsgruppe__enhetsgruppemedlemskap, domain=None, range=Optional[Union[Union[str, EnhetsgruppemedlemskapId], list[Union[str, EnhetsgruppemedlemskapId]]]])

slots.enhetsgruppemedlemskap__digitalEnhet = Slot(uri=RES.digitalEnhet, name="enhetsgruppemedlemskap__digitalEnhet", curie=RES.curie('digitalEnhet'),
                   model_uri=RES.enhetsgruppemedlemskap__digitalEnhet, domain=None, range=Union[str, DigitalEnhetId])

slots.enhetsgruppemedlemskap__enhetsgruppe = Slot(uri=RES.enhetsgruppe, name="enhetsgruppemedlemskap__enhetsgruppe", curie=RES.curie('enhetsgruppe'),
                   model_uri=RES.enhetsgruppemedlemskap__enhetsgruppe, domain=None, range=Union[str, EnhetsgruppeId])

slots.identitet__personalressurs = Slot(uri=RES.personalressurs, name="identitet__personalressurs", curie=RES.curie('personalressurs'),
                   model_uri=RES.identitet__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.identitet__rettighet = Slot(uri=RES.rettighet, name="identitet__rettighet", curie=RES.curie('rettighet'),
                   model_uri=RES.identitet__rettighet, domain=None, range=Optional[Union[Union[str, RettighetId], list[Union[str, RettighetId]]]])

slots.rettighet__kode = Slot(uri=RES.kode, name="rettighet__kode", curie=RES.curie('kode'),
                   model_uri=RES.rettighet__kode, domain=None, range=str)

slots.rettighet__navn = Slot(uri=RES.navn, name="rettighet__navn", curie=RES.curie('navn'),
                   model_uri=RES.rettighet__navn, domain=None, range=str)

slots.rettighet__beskrivelse = Slot(uri=RES.beskrivelse, name="rettighet__beskrivelse", curie=RES.curie('beskrivelse'),
                   model_uri=RES.rettighet__beskrivelse, domain=None, range=str)

slots.rettighet__gyldighetsperiode = Slot(uri=RES.gyldighetsperiode, name="rettighet__gyldighetsperiode", curie=RES.curie('gyldighetsperiode'),
                   model_uri=RES.rettighet__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.rettighet__passiv = Slot(uri=RES.passiv, name="rettighet__passiv", curie=RES.curie('passiv'),
                   model_uri=RES.rettighet__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.rettighet__identitet = Slot(uri=RES.identitet, name="rettighet__identitet", curie=RES.curie('identitet'),
                   model_uri=RES.rettighet__identitet, domain=None, range=Optional[Union[Union[str, IdentitetId], list[Union[str, IdentitetId]]]])

slots.applikasjonskategori__kode = Slot(uri=RES.kode, name="applikasjonskategori__kode", curie=RES.curie('kode'),
                   model_uri=RES.applikasjonskategori__kode, domain=None, range=str)

slots.applikasjonskategori__navn = Slot(uri=RES.navn, name="applikasjonskategori__navn", curie=RES.curie('navn'),
                   model_uri=RES.applikasjonskategori__navn, domain=None, range=str)

slots.applikasjonskategori__gyldighetsperiode = Slot(uri=RES.gyldighetsperiode, name="applikasjonskategori__gyldighetsperiode", curie=RES.curie('gyldighetsperiode'),
                   model_uri=RES.applikasjonskategori__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.applikasjonskategori__passiv = Slot(uri=RES.passiv, name="applikasjonskategori__passiv", curie=RES.curie('passiv'),
                   model_uri=RES.applikasjonskategori__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.brukertype__kode = Slot(uri=RES.kode, name="brukertype__kode", curie=RES.curie('kode'),
                   model_uri=RES.brukertype__kode, domain=None, range=str)

slots.brukertype__navn = Slot(uri=RES.navn, name="brukertype__navn", curie=RES.curie('navn'),
                   model_uri=RES.brukertype__navn, domain=None, range=str)

slots.brukertype__gyldighetsperiode = Slot(uri=RES.gyldighetsperiode, name="brukertype__gyldighetsperiode", curie=RES.curie('gyldighetsperiode'),
                   model_uri=RES.brukertype__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.brukertype__passiv = Slot(uri=RES.passiv, name="brukertype__passiv", curie=RES.curie('passiv'),
                   model_uri=RES.brukertype__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.enhetstype__kode = Slot(uri=RES.kode, name="enhetstype__kode", curie=RES.curie('kode'),
                   model_uri=RES.enhetstype__kode, domain=None, range=str)

slots.enhetstype__navn = Slot(uri=RES.navn, name="enhetstype__navn", curie=RES.curie('navn'),
                   model_uri=RES.enhetstype__navn, domain=None, range=str)

slots.enhetstype__gyldighetsperiode = Slot(uri=RES.gyldighetsperiode, name="enhetstype__gyldighetsperiode", curie=RES.curie('gyldighetsperiode'),
                   model_uri=RES.enhetstype__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.enhetstype__passiv = Slot(uri=RES.passiv, name="enhetstype__passiv", curie=RES.curie('passiv'),
                   model_uri=RES.enhetstype__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.handhevingstype__kode = Slot(uri=RES.kode, name="handhevingstype__kode", curie=RES.curie('kode'),
                   model_uri=RES.handhevingstype__kode, domain=None, range=str)

slots.handhevingstype__navn = Slot(uri=RES.navn, name="handhevingstype__navn", curie=RES.curie('navn'),
                   model_uri=RES.handhevingstype__navn, domain=None, range=str)

slots.handhevingstype__gyldighetsperiode = Slot(uri=RES.gyldighetsperiode, name="handhevingstype__gyldighetsperiode", curie=RES.curie('gyldighetsperiode'),
                   model_uri=RES.handhevingstype__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.handhevingstype__passiv = Slot(uri=RES.passiv, name="handhevingstype__passiv", curie=RES.curie('passiv'),
                   model_uri=RES.handhevingstype__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.lisensmodell__kode = Slot(uri=RES.kode, name="lisensmodell__kode", curie=RES.curie('kode'),
                   model_uri=RES.lisensmodell__kode, domain=None, range=str)

slots.lisensmodell__navn = Slot(uri=RES.navn, name="lisensmodell__navn", curie=RES.curie('navn'),
                   model_uri=RES.lisensmodell__navn, domain=None, range=str)

slots.lisensmodell__gyldighetsperiode = Slot(uri=RES.gyldighetsperiode, name="lisensmodell__gyldighetsperiode", curie=RES.curie('gyldighetsperiode'),
                   model_uri=RES.lisensmodell__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.lisensmodell__passiv = Slot(uri=RES.passiv, name="lisensmodell__passiv", curie=RES.curie('passiv'),
                   model_uri=RES.lisensmodell__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.plattform__kode = Slot(uri=RES.kode, name="plattform__kode", curie=RES.curie('kode'),
                   model_uri=RES.plattform__kode, domain=None, range=str)

slots.plattform__navn = Slot(uri=RES.navn, name="plattform__navn", curie=RES.curie('navn'),
                   model_uri=RES.plattform__navn, domain=None, range=str)

slots.plattform__gyldighetsperiode = Slot(uri=RES.gyldighetsperiode, name="plattform__gyldighetsperiode", curie=RES.curie('gyldighetsperiode'),
                   model_uri=RES.plattform__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.plattform__passiv = Slot(uri=RES.passiv, name="plattform__passiv", curie=RES.curie('passiv'),
                   model_uri=RES.plattform__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.produsent__kode = Slot(uri=RES.kode, name="produsent__kode", curie=RES.curie('kode'),
                   model_uri=RES.produsent__kode, domain=None, range=str)

slots.produsent__navn = Slot(uri=RES.navn, name="produsent__navn", curie=RES.curie('navn'),
                   model_uri=RES.produsent__navn, domain=None, range=str)

slots.produsent__gyldighetsperiode = Slot(uri=RES.gyldighetsperiode, name="produsent__gyldighetsperiode", curie=RES.curie('gyldighetsperiode'),
                   model_uri=RES.produsent__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.produsent__passiv = Slot(uri=RES.passiv, name="produsent__passiv", curie=RES.curie('passiv'),
                   model_uri=RES.produsent__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.status__kode = Slot(uri=RES.kode, name="status__kode", curie=RES.curie('kode'),
                   model_uri=RES.status__kode, domain=None, range=str)

slots.status__navn = Slot(uri=RES.navn, name="status__navn", curie=RES.curie('navn'),
                   model_uri=RES.status__navn, domain=None, range=str)

slots.status__gyldighetsperiode = Slot(uri=RES.gyldighetsperiode, name="status__gyldighetsperiode", curie=RES.curie('gyldighetsperiode'),
                   model_uri=RES.status__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.status__passiv = Slot(uri=RES.passiv, name="status__passiv", curie=RES.curie('passiv'),
                   model_uri=RES.status__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.aktoer__kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="aktoer__kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=RES.aktoer__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.aktoer__postadresse = Slot(uri=FINT.postadresse, name="aktoer__postadresse", curie=FINT.curie('postadresse'),
                   model_uri=RES.aktoer__postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.begrep__kode = Slot(uri=FINT.kode, name="begrep__kode", curie=FINT.curie('kode'),
                   model_uri=RES.begrep__kode, domain=None, range=str)

slots.begrep__navn = Slot(uri=FINT.navn, name="begrep__navn", curie=FINT.curie('navn'),
                   model_uri=RES.begrep__navn, domain=None, range=str)

slots.begrep__gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="begrep__gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.begrep__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.begrep__passiv = Slot(uri=FINT.passiv, name="begrep__passiv", curie=FINT.curie('passiv'),
                   model_uri=RES.begrep__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.enhet__forretningsadresse = Slot(uri=FINT.forretningsadresse, name="enhet__forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=RES.enhet__forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.enhet__organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="enhet__organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=RES.enhet__organisasjonsnavn, domain=None, range=Optional[str])

slots.enhet__organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="enhet__organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=RES.enhet__organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.identifikator__identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="identifikator__identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=RES.identifikator__identifikatorverdi, domain=None, range=str)

slots.identifikator__gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="identifikator__gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=RES.identifikator__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.periode__beskrivelse = Slot(uri=FINT.beskrivelse, name="periode__beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=RES.periode__beskrivelse, domain=None, range=Optional[str])

slots.periode__start = Slot(uri=FINT.start, name="periode__start", curie=FINT.curie('start'),
                   model_uri=RES.periode__start, domain=None, range=Union[str, XSDDateTime])

slots.periode__slutt = Slot(uri=FINT.slutt, name="periode__slutt", curie=FINT.curie('slutt'),
                   model_uri=RES.periode__slutt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.personnavn__fornavn = Slot(uri=FINT.fornavn, name="personnavn__fornavn", curie=FINT.curie('fornavn'),
                   model_uri=RES.personnavn__fornavn, domain=None, range=str)

slots.personnavn__mellomnavn = Slot(uri=FINT.mellomnavn, name="personnavn__mellomnavn", curie=FINT.curie('mellomnavn'),
                   model_uri=RES.personnavn__mellomnavn, domain=None, range=Optional[str])

slots.personnavn__etternavn = Slot(uri=FINT.etternavn, name="personnavn__etternavn", curie=FINT.curie('etternavn'),
                   model_uri=RES.personnavn__etternavn, domain=None, range=str)

slots.kontaktinformasjon__epostadresse = Slot(uri=FINT.epostadresse, name="kontaktinformasjon__epostadresse", curie=FINT.curie('epostadresse'),
                   model_uri=RES.kontaktinformasjon__epostadresse, domain=None, range=Optional[str])

slots.kontaktinformasjon__mobiltelefonnummer = Slot(uri=FINT.mobiltelefonnummer, name="kontaktinformasjon__mobiltelefonnummer", curie=FINT.curie('mobiltelefonnummer'),
                   model_uri=RES.kontaktinformasjon__mobiltelefonnummer, domain=None, range=Optional[str])

slots.kontaktinformasjon__nettsted = Slot(uri=FINT.nettsted, name="kontaktinformasjon__nettsted", curie=FINT.curie('nettsted'),
                   model_uri=RES.kontaktinformasjon__nettsted, domain=None, range=Optional[str])

slots.kontaktinformasjon__sip = Slot(uri=FINT.sip, name="kontaktinformasjon__sip", curie=FINT.curie('sip'),
                   model_uri=RES.kontaktinformasjon__sip, domain=None, range=Optional[str])

slots.kontaktinformasjon__telefonnummer = Slot(uri=FINT.telefonnummer, name="kontaktinformasjon__telefonnummer", curie=FINT.curie('telefonnummer'),
                   model_uri=RES.kontaktinformasjon__telefonnummer, domain=None, range=Optional[str])

slots.adresse__adresselinje = Slot(uri=FINT.adresselinje, name="adresse__adresselinje", curie=FINT.curie('adresselinje'),
                   model_uri=RES.adresse__adresselinje, domain=None, range=Optional[Union[str, list[str]]])

slots.adresse__postnummer = Slot(uri=FINT.postnummer, name="adresse__postnummer", curie=FINT.curie('postnummer'),
                   model_uri=RES.adresse__postnummer, domain=None, range=Optional[str])

slots.adresse__poststed = Slot(uri=FINT.poststed, name="adresse__poststed", curie=FINT.curie('poststed'),
                   model_uri=RES.adresse__poststed, domain=None, range=Optional[str])

slots.adresse__land = Slot(uri=FINT.land, name="adresse__land", curie=FINT.curie('land'),
                   model_uri=RES.adresse__land, domain=None, range=Optional[Union[str, LandkodeId]])

slots.matrikkelnummer__adresse = Slot(uri=FINT.adresse, name="matrikkelnummer__adresse", curie=FINT.curie('adresse'),
                   model_uri=RES.matrikkelnummer__adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.matrikkelnummer__bruksnummer = Slot(uri=FINT.bruksnummer, name="matrikkelnummer__bruksnummer", curie=FINT.curie('bruksnummer'),
                   model_uri=RES.matrikkelnummer__bruksnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__festenummer = Slot(uri=FINT.festenummer, name="matrikkelnummer__festenummer", curie=FINT.curie('festenummer'),
                   model_uri=RES.matrikkelnummer__festenummer, domain=None, range=Optional[str])

slots.matrikkelnummer__gaardsnummer = Slot(uri=FINT.gaardsnummer, name="matrikkelnummer__gaardsnummer", curie=FINT.curie('gaardsnummer'),
                   model_uri=RES.matrikkelnummer__gaardsnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__seksjonsnummer = Slot(uri=FINT.seksjonsnummer, name="matrikkelnummer__seksjonsnummer", curie=FINT.curie('seksjonsnummer'),
                   model_uri=RES.matrikkelnummer__seksjonsnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__kommunenummer = Slot(uri=FINT.kommunenummer, name="matrikkelnummer__kommunenummer", curie=FINT.curie('kommunenummer'),
                   model_uri=RES.matrikkelnummer__kommunenummer, domain=None, range=Optional[Union[str, KommuneId]])

slots.fylke__kommune = Slot(uri=FINT.kommune, name="fylke__kommune", curie=FINT.curie('kommune'),
                   model_uri=RES.fylke__kommune, domain=None, range=Optional[Union[Union[str, KommuneId], list[Union[str, KommuneId]]]])

slots.kommune__fylke = Slot(uri=FINT.fylke, name="kommune__fylke", curie=FINT.curie('fylke'),
                   model_uri=RES.kommune__fylke, domain=None, range=Union[str, FylkeId])

slots.valuta__bokstavkode = Slot(uri=FINT.bokstavkode, name="valuta__bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=RES.valuta__bokstavkode, domain=None, range=Union[dict, Identifikator])

slots.valuta__navn = Slot(uri=FINT.valutaNavn, name="valuta__navn", curie=FINT.curie('valutaNavn'),
                   model_uri=RES.valuta__navn, domain=None, range=str)

slots.valuta__nummerkode = Slot(uri=FINT.nummerkode, name="valuta__nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=RES.valuta__nummerkode, domain=None, range=Union[dict, Identifikator])

slots.person__bilde = Slot(uri=FINT.bilde, name="person__bilde", curie=FINT.curie('bilde'),
                   model_uri=RES.person__bilde, domain=None, range=Optional[str])

slots.person__bostedsadresse = Slot(uri=FINT.bostedsadresse, name="person__bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=RES.person__bostedsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.person__fodselsdato = Slot(uri=FINT.fodselsdato, name="person__fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=RES.person__fodselsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.person__fodselsnummer = Slot(uri=FINT.fodselsnummer, name="person__fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=RES.person__fodselsnummer, domain=None, range=Union[dict, Identifikator])

slots.person__navn = Slot(uri=FINT.personNavn, name="person__navn", curie=FINT.curie('personNavn'),
                   model_uri=RES.person__navn, domain=None, range=Union[dict, Personnavn])

slots.person__parorende = Slot(uri=FINT.parorende, name="person__parorende", curie=FINT.curie('parorende'),
                   model_uri=RES.person__parorende, domain=None, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.person__statsborgerskap = Slot(uri=FINT.statsborgerskap, name="person__statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=RES.person__statsborgerskap, domain=None, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.person__kommune = Slot(uri=FINT.kommune, name="person__kommune", curie=FINT.curie('kommune'),
                   model_uri=RES.person__kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.person__kjonn = Slot(uri=FINT.kjonn, name="person__kjonn", curie=FINT.curie('kjonn'),
                   model_uri=RES.person__kjonn, domain=None, range=Optional[Union[str, KjonnId]])

slots.person__foreldreansvar = Slot(uri=FINT.foreldreansvar, name="person__foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=RES.person__foreldreansvar, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.person__foreldre = Slot(uri=FINT.foreldre, name="person__foreldre", curie=FINT.curie('foreldre'),
                   model_uri=RES.person__foreldre, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.person__maalform = Slot(uri=FINT.maalform, name="person__maalform", curie=FINT.curie('maalform'),
                   model_uri=RES.person__maalform, domain=None, range=Optional[Union[str, SpraakId]])

slots.person__personalressurs = Slot(uri=FINT.personalressurs, name="person__personalressurs", curie=FINT.curie('personalressurs'),
                   model_uri=RES.person__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.person__morsmaal = Slot(uri=FINT.morsmaal, name="person__morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=RES.person__morsmaal, domain=None, range=Optional[Union[str, SpraakId]])

slots.person__laerling = Slot(uri=FINT.laerling, name="person__laerling", curie=FINT.curie('laerling'),
                   model_uri=RES.person__laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.person__elev = Slot(uri=FINT.elev, name="person__elev", curie=FINT.curie('elev'),
                   model_uri=RES.person__elev, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.person__otungdom = Slot(uri=FINT.otungdom, name="person__otungdom", curie=FINT.curie('otungdom'),
                   model_uri=RES.person__otungdom, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kontaktperson__kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="kontaktperson__kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=RES.kontaktperson__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.kontaktperson__navn = Slot(uri=FINT.kontaktpersonNavn, name="kontaktperson__navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=RES.kontaktperson__navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.kontaktperson__type = Slot(uri=FINT.type, name="kontaktperson__type", curie=FINT.curie('type'),
                   model_uri=RES.kontaktperson__type, domain=None, range=str)

slots.kontaktperson__kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="kontaktperson__kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=RES.kontaktperson__kontaktperson, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.virksomhet__virksomhetsId = Slot(uri=FINT.virksomhetsId, name="virksomhet__virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=RES.virksomhet__virksomhetsId, domain=None, range=Union[dict, Identifikator])

slots.virksomhet__laerling = Slot(uri=FINT.laerling, name="virksomhet__laerling", curie=FINT.curie('laerling'),
                   model_uri=RES.virksomhet__laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

