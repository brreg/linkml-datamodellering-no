# Auto generated from fint-okonomi-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-05T13:28:00
# Schema: fint-okonomi
#
# id: https://data.norge.no/linkml/fint-okonomi
# description: FINT-domenemodell for økonomi. Dekkjer tre sub-pakkar: okonomi.faktura (faktura, fakturagrunnlag, fakturautsteder), okonomi.regnskap (transaksjonar, posteringar, bilag, leverandørar) og okonomi.kodeverk (vare, merverdiavgift, valuta).
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

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.7.0"
version = "4.0.20"

# Namespaces
FINT = CurieNamespace('fint', 'https://schema.fintlabs.no/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OKN = CurieNamespace('okn', 'https://schema.fintlabs.no/okonomi/')
DEFAULT_ = OKN


# Types

# Class references
class FakturaId(URIorCURIE):
    pass


class FakturagrunnlagId(URIorCURIE):
    pass


class FakturautstederId(URIorCURIE):
    pass


class TransaksjonId(URIorCURIE):
    pass


class PosteringId(URIorCURIE):
    pass


class LeverandorId(URIorCURIE):
    pass


class LeverandorgruppeId(URIorCURIE):
    pass


class VareId(URIorCURIE):
    pass


class MerverdiavgiftId(URIorCURIE):
    pass


class OkonomiValutaId(URIorCURIE):
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
class OkonomiContainer(YAMLRoot):
    """
    Rotcontainer for FINT Økonomi-instansar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["OkonomiContainer"]
    class_class_curie: ClassVar[str] = "okn:OkonomiContainer"
    class_name: ClassVar[str] = "OkonomiContainer"
    class_model_uri: ClassVar[URIRef] = OKN.OkonomiContainer

    fakturaer: Optional[Union[dict[Union[str, FakturaId], Union[dict, "Faktura"]], list[Union[dict, "Faktura"]]]] = empty_dict()
    fakturagrunnlag: Optional[Union[dict[Union[str, FakturagrunnlagId], Union[dict, "Fakturagrunnlag"]], list[Union[dict, "Fakturagrunnlag"]]]] = empty_dict()
    fakturautstederear: Optional[Union[dict[Union[str, FakturautstederId], Union[dict, "Fakturautsteder"]], list[Union[dict, "Fakturautsteder"]]]] = empty_dict()
    transaksjonar: Optional[Union[dict[Union[str, TransaksjonId], Union[dict, "Transaksjon"]], list[Union[dict, "Transaksjon"]]]] = empty_dict()
    posteringar: Optional[Union[dict[Union[str, PosteringId], Union[dict, "Postering"]], list[Union[dict, "Postering"]]]] = empty_dict()
    leverandorar: Optional[Union[dict[Union[str, LeverandorId], Union[dict, "Leverandor"]], list[Union[dict, "Leverandor"]]]] = empty_dict()
    leverandorgrupper: Optional[Union[dict[Union[str, LeverandorgruppeId], Union[dict, "Leverandorgruppe"]], list[Union[dict, "Leverandorgruppe"]]]] = empty_dict()
    varer: Optional[Union[dict[Union[str, VareId], Union[dict, "Vare"]], list[Union[dict, "Vare"]]]] = empty_dict()
    merverdiavgifter: Optional[Union[dict[Union[str, MerverdiavgiftId], Union[dict, "Merverdiavgift"]], list[Union[dict, "Merverdiavgift"]]]] = empty_dict()
    valutaer: Optional[Union[dict[Union[str, OkonomiValutaId], Union[dict, "OkonomiValuta"]], list[Union[dict, "OkonomiValuta"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fakturaer", slot_type=Faktura, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fakturagrunnlag", slot_type=Fakturagrunnlag, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fakturautstederear", slot_type=Fakturautsteder, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="transaksjonar", slot_type=Transaksjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="posteringar", slot_type=Postering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="leverandorar", slot_type=Leverandor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="leverandorgrupper", slot_type=Leverandorgruppe, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="varer", slot_type=Vare, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="merverdiavgifter", slot_type=Merverdiavgift, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="valutaer", slot_type=OkonomiValuta, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Faktura(YAMLRoot):
    """
    Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Faktura"]
    class_class_curie: ClassVar[str] = "okn:Faktura"
    class_name: ClassVar[str] = "Faktura"
    class_model_uri: ClassVar[URIRef] = OKN.Faktura

    id: Union[str, FakturaId] = None
    fakturanummer: Union[dict, "Identifikator"] = None
    dato: Union[str, XSDDate] = None
    forfallsdato: Union[str, XSDDate] = None
    belop: int = None
    mottaker: str = None
    fakturagrunnlag: Union[str, FakturagrunnlagId] = None
    adresse: Optional[Union[dict, "Adresse"]] = None
    betalt: Optional[Union[bool, Bool]] = None
    fakturert: Optional[Union[bool, Bool]] = None
    kreditert: Optional[Union[bool, Bool]] = None
    restbelop: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FakturaId):
            self.id = FakturaId(self.id)

        if self._is_empty(self.fakturanummer):
            self.MissingRequiredField("fakturanummer")
        if not isinstance(self.fakturanummer, Identifikator):
            self.fakturanummer = Identifikator(**as_dict(self.fakturanummer))

        if self._is_empty(self.dato):
            self.MissingRequiredField("dato")
        if not isinstance(self.dato, XSDDate):
            self.dato = XSDDate(self.dato)

        if self._is_empty(self.forfallsdato):
            self.MissingRequiredField("forfallsdato")
        if not isinstance(self.forfallsdato, XSDDate):
            self.forfallsdato = XSDDate(self.forfallsdato)

        if self._is_empty(self.belop):
            self.MissingRequiredField("belop")
        if not isinstance(self.belop, int):
            self.belop = int(self.belop)

        if self._is_empty(self.mottaker):
            self.MissingRequiredField("mottaker")
        if not isinstance(self.mottaker, str):
            self.mottaker = str(self.mottaker)

        if self._is_empty(self.fakturagrunnlag):
            self.MissingRequiredField("fakturagrunnlag")
        if not isinstance(self.fakturagrunnlag, FakturagrunnlagId):
            self.fakturagrunnlag = FakturagrunnlagId(self.fakturagrunnlag)

        if self.adresse is not None and not isinstance(self.adresse, Adresse):
            self.adresse = Adresse(**as_dict(self.adresse))

        if self.betalt is not None and not isinstance(self.betalt, Bool):
            self.betalt = Bool(self.betalt)

        if self.fakturert is not None and not isinstance(self.fakturert, Bool):
            self.fakturert = Bool(self.fakturert)

        if self.kreditert is not None and not isinstance(self.kreditert, Bool):
            self.kreditert = Bool(self.kreditert)

        if self.restbelop is not None and not isinstance(self.restbelop, int):
            self.restbelop = int(self.restbelop)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fakturagrunnlag(YAMLRoot):
    """
    Grunnlag for fakturering.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Fakturagrunnlag"]
    class_class_curie: ClassVar[str] = "okn:Fakturagrunnlag"
    class_name: ClassVar[str] = "Fakturagrunnlag"
    class_model_uri: ClassVar[URIRef] = OKN.Fakturagrunnlag

    id: Union[str, FakturagrunnlagId] = None
    ordrenummer: Union[dict, "Identifikator"] = None
    mottaker: Union[dict, "Fakturamottaker"] = None
    fakturalinjer: Union[Union[dict, "Fakturalinje"], list[Union[dict, "Fakturalinje"]]] = None
    fakturautsteder: Union[str, FakturautstederId] = None
    leveringsdato: Optional[Union[str, XSDDate]] = None
    nettobelop: Optional[int] = None
    avgiftsbelop: Optional[int] = None
    totalbelop: Optional[int] = None
    faktura: Optional[Union[Union[str, FakturaId], list[Union[str, FakturaId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FakturagrunnlagId):
            self.id = FakturagrunnlagId(self.id)

        if self._is_empty(self.ordrenummer):
            self.MissingRequiredField("ordrenummer")
        if not isinstance(self.ordrenummer, Identifikator):
            self.ordrenummer = Identifikator(**as_dict(self.ordrenummer))

        if self._is_empty(self.mottaker):
            self.MissingRequiredField("mottaker")
        if not isinstance(self.mottaker, Fakturamottaker):
            self.mottaker = Fakturamottaker(**as_dict(self.mottaker))

        if self._is_empty(self.fakturalinjer):
            self.MissingRequiredField("fakturalinjer")
        self._normalize_inlined_as_list(slot_name="fakturalinjer", slot_type=Fakturalinje, key_name="antall", keyed=False)

        if self._is_empty(self.fakturautsteder):
            self.MissingRequiredField("fakturautsteder")
        if not isinstance(self.fakturautsteder, FakturautstederId):
            self.fakturautsteder = FakturautstederId(self.fakturautsteder)

        if self.leveringsdato is not None and not isinstance(self.leveringsdato, XSDDate):
            self.leveringsdato = XSDDate(self.leveringsdato)

        if self.nettobelop is not None and not isinstance(self.nettobelop, int):
            self.nettobelop = int(self.nettobelop)

        if self.avgiftsbelop is not None and not isinstance(self.avgiftsbelop, int):
            self.avgiftsbelop = int(self.avgiftsbelop)

        if self.totalbelop is not None and not isinstance(self.totalbelop, int):
            self.totalbelop = int(self.totalbelop)

        if not isinstance(self.faktura, list):
            self.faktura = [self.faktura] if self.faktura is not None else []
        self.faktura = [v if isinstance(v, FakturaId) else FakturaId(v) for v in self.faktura]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fakturautsteder(YAMLRoot):
    """
    Eining som utformar og oversender faktura og mottar betaling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Fakturautsteder"]
    class_class_curie: ClassVar[str] = "okn:Fakturautsteder"
    class_name: ClassVar[str] = "Fakturautsteder"
    class_model_uri: ClassVar[URIRef] = OKN.Fakturautsteder

    id: Union[str, FakturautstederId] = None
    navn: str = None
    fakturagrunnlag: Optional[Union[Union[str, FakturagrunnlagId], list[Union[str, FakturagrunnlagId]]]] = empty_list()
    organisasjonselement: Optional[Union[str, URIorCURIE]] = None
    vare: Optional[Union[Union[str, VareId], list[Union[str, VareId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FakturautstederId):
            self.id = FakturautstederId(self.id)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if not isinstance(self.fakturagrunnlag, list):
            self.fakturagrunnlag = [self.fakturagrunnlag] if self.fakturagrunnlag is not None else []
        self.fakturagrunnlag = [v if isinstance(v, FakturagrunnlagId) else FakturagrunnlagId(v) for v in self.fakturagrunnlag]

        if self.organisasjonselement is not None and not isinstance(self.organisasjonselement, URIorCURIE):
            self.organisasjonselement = URIorCURIE(self.organisasjonselement)

        if not isinstance(self.vare, list):
            self.vare = [self.vare] if self.vare is not None else []
        self.vare = [v if isinstance(v, VareId) else VareId(v) for v in self.vare]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fakturamottaker(YAMLRoot):
    """
    Aktør som skal betale faktura (kompleks datatype).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Fakturamottaker"]
    class_class_curie: ClassVar[str] = "okn:Fakturamottaker"
    class_name: ClassVar[str] = "Fakturamottaker"
    class_model_uri: ClassVar[URIRef] = OKN.Fakturamottaker

    person: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.person):
            self.MissingRequiredField("person")
        if not isinstance(self.person, URIorCURIE):
            self.person = URIorCURIE(self.person)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fakturalinje(YAMLRoot):
    """
    Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Fakturalinje"]
    class_class_curie: ClassVar[str] = "okn:Fakturalinje"
    class_name: ClassVar[str] = "Fakturalinje"
    class_model_uri: ClassVar[URIRef] = OKN.Fakturalinje

    antall: float = None
    pris: int = None
    vare: Union[str, VareId] = None
    fritekst: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.antall):
            self.MissingRequiredField("antall")
        if not isinstance(self.antall, float):
            self.antall = float(self.antall)

        if self._is_empty(self.pris):
            self.MissingRequiredField("pris")
        if not isinstance(self.pris, int):
            self.pris = int(self.pris)

        if self._is_empty(self.vare):
            self.MissingRequiredField("vare")
        if not isinstance(self.vare, VareId):
            self.vare = VareId(self.vare)

        if not isinstance(self.fritekst, list):
            self.fritekst = [self.fritekst] if self.fritekst is not None else []
        self.fritekst = [v if isinstance(v, str) else str(v) for v in self.fritekst]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Transaksjon(YAMLRoot):
    """
    Overføring av pengar til eller frå eksterne partar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Transaksjon"]
    class_class_curie: ClassVar[str] = "okn:Transaksjon"
    class_name: ClassVar[str] = "Transaksjon"
    class_model_uri: ClassVar[URIRef] = OKN.Transaksjon

    id: Union[str, TransaksjonId] = None
    transaksjonsId: Union[dict, "Identifikator"] = None
    belop: int = None
    forfallsdato: Union[str, XSDDate] = None
    postering: Union[Union[str, PosteringId], list[Union[str, PosteringId]]] = None
    valuta: Union[str, OkonomiValutaId] = None
    beskrivelse: Optional[str] = None
    bilag: Optional[Union[Union[dict, "Bilag"], list[Union[dict, "Bilag"]]]] = empty_list()
    transaksjonstidspunkt: Optional[Union[str, XSDDateTime]] = None
    oppdateringstidspunkt: Optional[Union[str, XSDDateTime]] = None
    leverandor: Optional[Union[str, LeverandorId]] = None
    ansvarlig: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TransaksjonId):
            self.id = TransaksjonId(self.id)

        if self._is_empty(self.transaksjonsId):
            self.MissingRequiredField("transaksjonsId")
        if not isinstance(self.transaksjonsId, Identifikator):
            self.transaksjonsId = Identifikator(**as_dict(self.transaksjonsId))

        if self._is_empty(self.belop):
            self.MissingRequiredField("belop")
        if not isinstance(self.belop, int):
            self.belop = int(self.belop)

        if self._is_empty(self.forfallsdato):
            self.MissingRequiredField("forfallsdato")
        if not isinstance(self.forfallsdato, XSDDate):
            self.forfallsdato = XSDDate(self.forfallsdato)

        if self._is_empty(self.postering):
            self.MissingRequiredField("postering")
        if not isinstance(self.postering, list):
            self.postering = [self.postering] if self.postering is not None else []
        self.postering = [v if isinstance(v, PosteringId) else PosteringId(v) for v in self.postering]

        if self._is_empty(self.valuta):
            self.MissingRequiredField("valuta")
        if not isinstance(self.valuta, OkonomiValutaId):
            self.valuta = OkonomiValutaId(self.valuta)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        self._normalize_inlined_as_list(slot_name="bilag", slot_type=Bilag, key_name="bilagsdato", keyed=False)

        if self.transaksjonstidspunkt is not None and not isinstance(self.transaksjonstidspunkt, XSDDateTime):
            self.transaksjonstidspunkt = XSDDateTime(self.transaksjonstidspunkt)

        if self.oppdateringstidspunkt is not None and not isinstance(self.oppdateringstidspunkt, XSDDateTime):
            self.oppdateringstidspunkt = XSDDateTime(self.oppdateringstidspunkt)

        if self.leverandor is not None and not isinstance(self.leverandor, LeverandorId):
            self.leverandor = LeverandorId(self.leverandor)

        if self.ansvarlig is not None and not isinstance(self.ansvarlig, URIorCURIE):
            self.ansvarlig = URIorCURIE(self.ansvarlig)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Postering(YAMLRoot):
    """
    Føring på ein konto i rekneskapet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Postering"]
    class_class_curie: ClassVar[str] = "okn:Postering"
    class_name: ClassVar[str] = "Postering"
    class_model_uri: ClassVar[URIRef] = OKN.Postering

    id: Union[str, PosteringId] = None
    posteringsId: Union[dict, "Identifikator"] = None
    belop: int = None
    debet: Union[bool, Bool] = None
    kontering: Union[dict, "Kontostreng"] = None
    transaksjon: Optional[Union[str, TransaksjonId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PosteringId):
            self.id = PosteringId(self.id)

        if self._is_empty(self.posteringsId):
            self.MissingRequiredField("posteringsId")
        if not isinstance(self.posteringsId, Identifikator):
            self.posteringsId = Identifikator(**as_dict(self.posteringsId))

        if self._is_empty(self.belop):
            self.MissingRequiredField("belop")
        if not isinstance(self.belop, int):
            self.belop = int(self.belop)

        if self._is_empty(self.debet):
            self.MissingRequiredField("debet")
        if not isinstance(self.debet, Bool):
            self.debet = Bool(self.debet)

        if self._is_empty(self.kontering):
            self.MissingRequiredField("kontering")
        if not isinstance(self.kontering, Kontostreng):
            self.kontering = Kontostreng(**as_dict(self.kontering))

        if self.transaksjon is not None and not isinstance(self.transaksjon, TransaksjonId):
            self.transaksjon = TransaksjonId(self.transaksjon)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Leverandor(YAMLRoot):
    """
    Person eller verksemd som leverer produkt eller tenester (Leverandør).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Leverandor"]
    class_class_curie: ClassVar[str] = "okn:Leverandor"
    class_name: ClassVar[str] = "Leverandor"
    class_model_uri: ClassVar[URIRef] = OKN.Leverandor

    id: Union[str, LeverandorId] = None
    kontonummer: Optional[str] = None
    leverandornummer: Optional[Union[dict, "Identifikator"]] = None
    person: Optional[Union[str, URIorCURIE]] = None
    leverandorgruppe: Optional[Union[str, LeverandorgruppeId]] = None
    virksomhet: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LeverandorId):
            self.id = LeverandorId(self.id)

        if self.kontonummer is not None and not isinstance(self.kontonummer, str):
            self.kontonummer = str(self.kontonummer)

        if self.leverandornummer is not None and not isinstance(self.leverandornummer, Identifikator):
            self.leverandornummer = Identifikator(**as_dict(self.leverandornummer))

        if self.person is not None and not isinstance(self.person, URIorCURIE):
            self.person = URIorCURIE(self.person)

        if self.leverandorgruppe is not None and not isinstance(self.leverandorgruppe, LeverandorgruppeId):
            self.leverandorgruppe = LeverandorgruppeId(self.leverandorgruppe)

        if self.virksomhet is not None and not isinstance(self.virksomhet, URIorCURIE):
            self.virksomhet = URIorCURIE(self.virksomhet)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Leverandorgruppe(YAMLRoot):
    """
    Gruppering av leverandørar (Leverandørgruppe).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Leverandorgruppe"]
    class_class_curie: ClassVar[str] = "okn:Leverandorgruppe"
    class_name: ClassVar[str] = "Leverandorgruppe"
    class_model_uri: ClassVar[URIRef] = OKN.Leverandorgruppe

    id: Union[str, LeverandorgruppeId] = None
    navn: str = None
    leverandor: Optional[Union[Union[str, LeverandorId], list[Union[str, LeverandorId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LeverandorgruppeId):
            self.id = LeverandorgruppeId(self.id)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if not isinstance(self.leverandor, list):
            self.leverandor = [self.leverandor] if self.leverandor is not None else []
        self.leverandor = [v if isinstance(v, LeverandorId) else LeverandorId(v) for v in self.leverandor]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bilag(YAMLRoot):
    """
    Dokumentasjon til ein transaksjon (kompleks datatype).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Bilag"]
    class_class_curie: ClassVar[str] = "okn:Bilag"
    class_name: ClassVar[str] = "Bilag"
    class_model_uri: ClassVar[URIRef] = OKN.Bilag

    bilagsdato: Union[str, XSDDate] = None
    bilagsnummer: Optional[str] = None
    referanse: Optional[str] = None
    url: Optional[str] = None
    filnavn: Optional[str] = None
    data: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.bilagsdato):
            self.MissingRequiredField("bilagsdato")
        if not isinstance(self.bilagsdato, XSDDate):
            self.bilagsdato = XSDDate(self.bilagsdato)

        if self.bilagsnummer is not None and not isinstance(self.bilagsnummer, str):
            self.bilagsnummer = str(self.bilagsnummer)

        if self.referanse is not None and not isinstance(self.referanse, str):
            self.referanse = str(self.referanse)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.filnavn is not None and not isinstance(self.filnavn, str):
            self.filnavn = str(self.filnavn)

        if self.data is not None and not isinstance(self.data, str):
            self.data = str(self.data)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontostreng(YAMLRoot):
    """
    Kontodimensjonar for ei postering (kompleks datatype).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Kontostreng"]
    class_class_curie: ClassVar[str] = "okn:Kontostreng"
    class_name: ClassVar[str] = "Kontostreng"
    class_model_uri: ClassVar[URIRef] = OKN.Kontostreng

    art: Optional[str] = None
    funksjon: Optional[str] = None
    ansvar: Optional[str] = None
    prosjekt: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.art is not None and not isinstance(self.art, str):
            self.art = str(self.art)

        if self.funksjon is not None and not isinstance(self.funksjon, str):
            self.funksjon = str(self.funksjon)

        if self.ansvar is not None and not isinstance(self.ansvar, str):
            self.ansvar = str(self.ansvar)

        if self.prosjekt is not None and not isinstance(self.prosjekt, str):
            self.prosjekt = str(self.prosjekt)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Vare(YAMLRoot):
    """
    Vare eller teneste som kan leverast og fakturerast.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Vare"]
    class_class_curie: ClassVar[str] = "okn:Vare"
    class_name: ClassVar[str] = "Vare"
    class_model_uri: ClassVar[URIRef] = OKN.Vare

    id: Union[str, VareId] = None
    kode: str = None
    navn: str = None
    enhet: str = None
    pris: int = None
    fakturautsteder: Union[str, FakturautstederId] = None
    merverdiavgift: Union[str, MerverdiavgiftId] = None
    kontering: Optional[Union[dict, Kontostreng]] = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VareId):
            self.id = VareId(self.id)

        if self._is_empty(self.kode):
            self.MissingRequiredField("kode")
        if not isinstance(self.kode, str):
            self.kode = str(self.kode)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self._is_empty(self.enhet):
            self.MissingRequiredField("enhet")
        if not isinstance(self.enhet, str):
            self.enhet = str(self.enhet)

        if self._is_empty(self.pris):
            self.MissingRequiredField("pris")
        if not isinstance(self.pris, int):
            self.pris = int(self.pris)

        if self._is_empty(self.fakturautsteder):
            self.MissingRequiredField("fakturautsteder")
        if not isinstance(self.fakturautsteder, FakturautstederId):
            self.fakturautsteder = FakturautstederId(self.fakturautsteder)

        if self._is_empty(self.merverdiavgift):
            self.MissingRequiredField("merverdiavgift")
        if not isinstance(self.merverdiavgift, MerverdiavgiftId):
            self.merverdiavgift = MerverdiavgiftId(self.merverdiavgift)

        if self.kontering is not None and not isinstance(self.kontering, Kontostreng):
            self.kontering = Kontostreng(**as_dict(self.kontering))

        if self.gyldighetsperiode is not None and not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self.passiv is not None and not isinstance(self.passiv, Bool):
            self.passiv = Bool(self.passiv)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Merverdiavgift(YAMLRoot):
    """
    Kodeverk for merverdiavgifter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Merverdiavgift"]
    class_class_curie: ClassVar[str] = "okn:Merverdiavgift"
    class_name: ClassVar[str] = "Merverdiavgift"
    class_model_uri: ClassVar[URIRef] = OKN.Merverdiavgift

    id: Union[str, MerverdiavgiftId] = None
    kode: str = None
    navn: str = None
    sats: int = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MerverdiavgiftId):
            self.id = MerverdiavgiftId(self.id)

        if self._is_empty(self.kode):
            self.MissingRequiredField("kode")
        if not isinstance(self.kode, str):
            self.kode = str(self.kode)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self._is_empty(self.sats):
            self.MissingRequiredField("sats")
        if not isinstance(self.sats, int):
            self.sats = int(self.sats)

        if self.gyldighetsperiode is not None and not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self.passiv is not None and not isinstance(self.passiv, Bool):
            self.passiv = Bool(self.passiv)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OkonomiValuta(YAMLRoot):
    """
    Valuta for transaksjonsbeløp.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Valuta"]
    class_class_curie: ClassVar[str] = "okn:Valuta"
    class_name: ClassVar[str] = "OkonomiValuta"
    class_model_uri: ClassVar[URIRef] = OKN.OkonomiValuta

    id: Union[str, OkonomiValutaId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OkonomiValutaId):
            self.id = OkonomiValutaId(self.id)

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
    class_model_uri: ClassVar[URIRef] = OKN.Aktoer

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
    class_model_uri: ClassVar[URIRef] = OKN.Begrep

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
    class_model_uri: ClassVar[URIRef] = OKN.Enhet

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
    class_model_uri: ClassVar[URIRef] = OKN.Identifikator

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
    class_model_uri: ClassVar[URIRef] = OKN.Periode

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
    class_model_uri: ClassVar[URIRef] = OKN.Personnavn

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
    class_model_uri: ClassVar[URIRef] = OKN.Kontaktinformasjon

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
    class_model_uri: ClassVar[URIRef] = OKN.Adresse

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
    class_model_uri: ClassVar[URIRef] = OKN.Matrikkelnummer

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
    class_model_uri: ClassVar[URIRef] = OKN.Landkode

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
    class_model_uri: ClassVar[URIRef] = OKN.Kjonn

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
    class_model_uri: ClassVar[URIRef] = OKN.Fylke

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
    class_model_uri: ClassVar[URIRef] = OKN.Kommune

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
    class_model_uri: ClassVar[URIRef] = OKN.Spraak

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
    class_model_uri: ClassVar[URIRef] = OKN.Valuta

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
    class_model_uri: ClassVar[URIRef] = OKN.Person

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
    class_model_uri: ClassVar[URIRef] = OKN.Kontaktperson

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
    class_model_uri: ClassVar[URIRef] = OKN.Virksomhet

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
                   model_uri=OKN.id, domain=None, range=URIRef)

slots.okonomiContainer__fakturaer = Slot(uri=OKN.fakturaer, name="okonomiContainer__fakturaer", curie=OKN.curie('fakturaer'),
                   model_uri=OKN.okonomiContainer__fakturaer, domain=None, range=Optional[Union[dict[Union[str, FakturaId], Union[dict, Faktura]], list[Union[dict, Faktura]]]])

slots.okonomiContainer__fakturagrunnlag = Slot(uri=OKN.fakturagrunnlag, name="okonomiContainer__fakturagrunnlag", curie=OKN.curie('fakturagrunnlag'),
                   model_uri=OKN.okonomiContainer__fakturagrunnlag, domain=None, range=Optional[Union[dict[Union[str, FakturagrunnlagId], Union[dict, Fakturagrunnlag]], list[Union[dict, Fakturagrunnlag]]]])

slots.okonomiContainer__fakturautstederear = Slot(uri=OKN.fakturautstederear, name="okonomiContainer__fakturautstederear", curie=OKN.curie('fakturautstederear'),
                   model_uri=OKN.okonomiContainer__fakturautstederear, domain=None, range=Optional[Union[dict[Union[str, FakturautstederId], Union[dict, Fakturautsteder]], list[Union[dict, Fakturautsteder]]]])

slots.okonomiContainer__transaksjonar = Slot(uri=OKN.transaksjonar, name="okonomiContainer__transaksjonar", curie=OKN.curie('transaksjonar'),
                   model_uri=OKN.okonomiContainer__transaksjonar, domain=None, range=Optional[Union[dict[Union[str, TransaksjonId], Union[dict, Transaksjon]], list[Union[dict, Transaksjon]]]])

slots.okonomiContainer__posteringar = Slot(uri=OKN.posteringar, name="okonomiContainer__posteringar", curie=OKN.curie('posteringar'),
                   model_uri=OKN.okonomiContainer__posteringar, domain=None, range=Optional[Union[dict[Union[str, PosteringId], Union[dict, Postering]], list[Union[dict, Postering]]]])

slots.okonomiContainer__leverandorar = Slot(uri=OKN.leverandorar, name="okonomiContainer__leverandorar", curie=OKN.curie('leverandorar'),
                   model_uri=OKN.okonomiContainer__leverandorar, domain=None, range=Optional[Union[dict[Union[str, LeverandorId], Union[dict, Leverandor]], list[Union[dict, Leverandor]]]])

slots.okonomiContainer__leverandorgrupper = Slot(uri=OKN.leverandorgrupper, name="okonomiContainer__leverandorgrupper", curie=OKN.curie('leverandorgrupper'),
                   model_uri=OKN.okonomiContainer__leverandorgrupper, domain=None, range=Optional[Union[dict[Union[str, LeverandorgruppeId], Union[dict, Leverandorgruppe]], list[Union[dict, Leverandorgruppe]]]])

slots.okonomiContainer__varer = Slot(uri=OKN.varer, name="okonomiContainer__varer", curie=OKN.curie('varer'),
                   model_uri=OKN.okonomiContainer__varer, domain=None, range=Optional[Union[dict[Union[str, VareId], Union[dict, Vare]], list[Union[dict, Vare]]]])

slots.okonomiContainer__merverdiavgifter = Slot(uri=OKN.merverdiavgifter, name="okonomiContainer__merverdiavgifter", curie=OKN.curie('merverdiavgifter'),
                   model_uri=OKN.okonomiContainer__merverdiavgifter, domain=None, range=Optional[Union[dict[Union[str, MerverdiavgiftId], Union[dict, Merverdiavgift]], list[Union[dict, Merverdiavgift]]]])

slots.okonomiContainer__valutaer = Slot(uri=OKN.valutaer, name="okonomiContainer__valutaer", curie=OKN.curie('valutaer'),
                   model_uri=OKN.okonomiContainer__valutaer, domain=None, range=Optional[Union[dict[Union[str, OkonomiValutaId], Union[dict, OkonomiValuta]], list[Union[dict, OkonomiValuta]]]])

slots.faktura__fakturanummer = Slot(uri=OKN.fakturanummer, name="faktura__fakturanummer", curie=OKN.curie('fakturanummer'),
                   model_uri=OKN.faktura__fakturanummer, domain=None, range=Union[dict, Identifikator])

slots.faktura__dato = Slot(uri=OKN.dato, name="faktura__dato", curie=OKN.curie('dato'),
                   model_uri=OKN.faktura__dato, domain=None, range=Union[str, XSDDate])

slots.faktura__forfallsdato = Slot(uri=OKN.forfallsdato, name="faktura__forfallsdato", curie=OKN.curie('forfallsdato'),
                   model_uri=OKN.faktura__forfallsdato, domain=None, range=Union[str, XSDDate])

slots.faktura__belop = Slot(uri=OKN.belop, name="faktura__belop", curie=OKN.curie('belop'),
                   model_uri=OKN.faktura__belop, domain=None, range=int)

slots.faktura__mottaker = Slot(uri=OKN.mottaker, name="faktura__mottaker", curie=OKN.curie('mottaker'),
                   model_uri=OKN.faktura__mottaker, domain=None, range=str)

slots.faktura__adresse = Slot(uri=OKN.adresse, name="faktura__adresse", curie=OKN.curie('adresse'),
                   model_uri=OKN.faktura__adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.faktura__betalt = Slot(uri=OKN.betalt, name="faktura__betalt", curie=OKN.curie('betalt'),
                   model_uri=OKN.faktura__betalt, domain=None, range=Optional[Union[bool, Bool]])

slots.faktura__fakturert = Slot(uri=OKN.fakturert, name="faktura__fakturert", curie=OKN.curie('fakturert'),
                   model_uri=OKN.faktura__fakturert, domain=None, range=Optional[Union[bool, Bool]])

slots.faktura__kreditert = Slot(uri=OKN.kreditert, name="faktura__kreditert", curie=OKN.curie('kreditert'),
                   model_uri=OKN.faktura__kreditert, domain=None, range=Optional[Union[bool, Bool]])

slots.faktura__restbelop = Slot(uri=OKN.restbelop, name="faktura__restbelop", curie=OKN.curie('restbelop'),
                   model_uri=OKN.faktura__restbelop, domain=None, range=Optional[int])

slots.faktura__fakturagrunnlag = Slot(uri=OKN.fakturagrunnlag, name="faktura__fakturagrunnlag", curie=OKN.curie('fakturagrunnlag'),
                   model_uri=OKN.faktura__fakturagrunnlag, domain=None, range=Union[str, FakturagrunnlagId])

slots.fakturagrunnlag__ordrenummer = Slot(uri=OKN.ordrenummer, name="fakturagrunnlag__ordrenummer", curie=OKN.curie('ordrenummer'),
                   model_uri=OKN.fakturagrunnlag__ordrenummer, domain=None, range=Union[dict, Identifikator])

slots.fakturagrunnlag__mottaker = Slot(uri=OKN.fakturamottaker, name="fakturagrunnlag__mottaker", curie=OKN.curie('fakturamottaker'),
                   model_uri=OKN.fakturagrunnlag__mottaker, domain=None, range=Union[dict, Fakturamottaker])

slots.fakturagrunnlag__fakturalinjer = Slot(uri=OKN.fakturalinjer, name="fakturagrunnlag__fakturalinjer", curie=OKN.curie('fakturalinjer'),
                   model_uri=OKN.fakturagrunnlag__fakturalinjer, domain=None, range=Union[Union[dict, Fakturalinje], list[Union[dict, Fakturalinje]]])

slots.fakturagrunnlag__leveringsdato = Slot(uri=OKN.leveringsdato, name="fakturagrunnlag__leveringsdato", curie=OKN.curie('leveringsdato'),
                   model_uri=OKN.fakturagrunnlag__leveringsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.fakturagrunnlag__nettobelop = Slot(uri=OKN.nettobelop, name="fakturagrunnlag__nettobelop", curie=OKN.curie('nettobelop'),
                   model_uri=OKN.fakturagrunnlag__nettobelop, domain=None, range=Optional[int])

slots.fakturagrunnlag__avgiftsbelop = Slot(uri=OKN.avgiftsbelop, name="fakturagrunnlag__avgiftsbelop", curie=OKN.curie('avgiftsbelop'),
                   model_uri=OKN.fakturagrunnlag__avgiftsbelop, domain=None, range=Optional[int])

slots.fakturagrunnlag__totalbelop = Slot(uri=OKN.totalbelop, name="fakturagrunnlag__totalbelop", curie=OKN.curie('totalbelop'),
                   model_uri=OKN.fakturagrunnlag__totalbelop, domain=None, range=Optional[int])

slots.fakturagrunnlag__faktura = Slot(uri=OKN.faktura, name="fakturagrunnlag__faktura", curie=OKN.curie('faktura'),
                   model_uri=OKN.fakturagrunnlag__faktura, domain=None, range=Optional[Union[Union[str, FakturaId], list[Union[str, FakturaId]]]])

slots.fakturagrunnlag__fakturautsteder = Slot(uri=OKN.fakturautsteder, name="fakturagrunnlag__fakturautsteder", curie=OKN.curie('fakturautsteder'),
                   model_uri=OKN.fakturagrunnlag__fakturautsteder, domain=None, range=Union[str, FakturautstederId])

slots.fakturautsteder__navn = Slot(uri=OKN.navn, name="fakturautsteder__navn", curie=OKN.curie('navn'),
                   model_uri=OKN.fakturautsteder__navn, domain=None, range=str)

slots.fakturautsteder__fakturagrunnlag = Slot(uri=OKN.fakturagrunnlag, name="fakturautsteder__fakturagrunnlag", curie=OKN.curie('fakturagrunnlag'),
                   model_uri=OKN.fakturautsteder__fakturagrunnlag, domain=None, range=Optional[Union[Union[str, FakturagrunnlagId], list[Union[str, FakturagrunnlagId]]]])

slots.fakturautsteder__organisasjonselement = Slot(uri=OKN.organisasjonselement, name="fakturautsteder__organisasjonselement", curie=OKN.curie('organisasjonselement'),
                   model_uri=OKN.fakturautsteder__organisasjonselement, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.fakturautsteder__vare = Slot(uri=OKN.vare, name="fakturautsteder__vare", curie=OKN.curie('vare'),
                   model_uri=OKN.fakturautsteder__vare, domain=None, range=Optional[Union[Union[str, VareId], list[Union[str, VareId]]]])

slots.fakturamottaker__person = Slot(uri=OKN.person, name="fakturamottaker__person", curie=OKN.curie('person'),
                   model_uri=OKN.fakturamottaker__person, domain=None, range=Union[str, URIorCURIE])

slots.fakturalinje__antall = Slot(uri=OKN.antall, name="fakturalinje__antall", curie=OKN.curie('antall'),
                   model_uri=OKN.fakturalinje__antall, domain=None, range=float)

slots.fakturalinje__pris = Slot(uri=OKN.pris, name="fakturalinje__pris", curie=OKN.curie('pris'),
                   model_uri=OKN.fakturalinje__pris, domain=None, range=int)

slots.fakturalinje__fritekst = Slot(uri=OKN.fritekst, name="fakturalinje__fritekst", curie=OKN.curie('fritekst'),
                   model_uri=OKN.fakturalinje__fritekst, domain=None, range=Optional[Union[str, list[str]]])

slots.fakturalinje__vare = Slot(uri=OKN.vare, name="fakturalinje__vare", curie=OKN.curie('vare'),
                   model_uri=OKN.fakturalinje__vare, domain=None, range=Union[str, VareId])

slots.transaksjon__transaksjonsId = Slot(uri=OKN.transaksjonsId, name="transaksjon__transaksjonsId", curie=OKN.curie('transaksjonsId'),
                   model_uri=OKN.transaksjon__transaksjonsId, domain=None, range=Union[dict, Identifikator])

slots.transaksjon__belop = Slot(uri=OKN.belop, name="transaksjon__belop", curie=OKN.curie('belop'),
                   model_uri=OKN.transaksjon__belop, domain=None, range=int)

slots.transaksjon__forfallsdato = Slot(uri=OKN.forfallsdato, name="transaksjon__forfallsdato", curie=OKN.curie('forfallsdato'),
                   model_uri=OKN.transaksjon__forfallsdato, domain=None, range=Union[str, XSDDate])

slots.transaksjon__beskrivelse = Slot(uri=OKN.beskrivelse, name="transaksjon__beskrivelse", curie=OKN.curie('beskrivelse'),
                   model_uri=OKN.transaksjon__beskrivelse, domain=None, range=Optional[str])

slots.transaksjon__bilag = Slot(uri=OKN.bilag, name="transaksjon__bilag", curie=OKN.curie('bilag'),
                   model_uri=OKN.transaksjon__bilag, domain=None, range=Optional[Union[Union[dict, Bilag], list[Union[dict, Bilag]]]])

slots.transaksjon__transaksjonstidspunkt = Slot(uri=OKN.transaksjonstidspunkt, name="transaksjon__transaksjonstidspunkt", curie=OKN.curie('transaksjonstidspunkt'),
                   model_uri=OKN.transaksjon__transaksjonstidspunkt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.transaksjon__oppdateringstidspunkt = Slot(uri=OKN.oppdateringstidspunkt, name="transaksjon__oppdateringstidspunkt", curie=OKN.curie('oppdateringstidspunkt'),
                   model_uri=OKN.transaksjon__oppdateringstidspunkt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.transaksjon__leverandor = Slot(uri=OKN.leverandor, name="transaksjon__leverandor", curie=OKN.curie('leverandor'),
                   model_uri=OKN.transaksjon__leverandor, domain=None, range=Optional[Union[str, LeverandorId]])

slots.transaksjon__postering = Slot(uri=OKN.postering, name="transaksjon__postering", curie=OKN.curie('postering'),
                   model_uri=OKN.transaksjon__postering, domain=None, range=Union[Union[str, PosteringId], list[Union[str, PosteringId]]])

slots.transaksjon__ansvarlig = Slot(uri=OKN.ansvarlig, name="transaksjon__ansvarlig", curie=OKN.curie('ansvarlig'),
                   model_uri=OKN.transaksjon__ansvarlig, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.transaksjon__valuta = Slot(uri=OKN.valuta, name="transaksjon__valuta", curie=OKN.curie('valuta'),
                   model_uri=OKN.transaksjon__valuta, domain=None, range=Union[str, OkonomiValutaId])

slots.postering__posteringsId = Slot(uri=OKN.posteringsId, name="postering__posteringsId", curie=OKN.curie('posteringsId'),
                   model_uri=OKN.postering__posteringsId, domain=None, range=Union[dict, Identifikator])

slots.postering__belop = Slot(uri=OKN.belop, name="postering__belop", curie=OKN.curie('belop'),
                   model_uri=OKN.postering__belop, domain=None, range=int)

slots.postering__debet = Slot(uri=OKN.debet, name="postering__debet", curie=OKN.curie('debet'),
                   model_uri=OKN.postering__debet, domain=None, range=Union[bool, Bool])

slots.postering__kontering = Slot(uri=OKN.kontering, name="postering__kontering", curie=OKN.curie('kontering'),
                   model_uri=OKN.postering__kontering, domain=None, range=Union[dict, Kontostreng])

slots.postering__transaksjon = Slot(uri=OKN.transaksjon, name="postering__transaksjon", curie=OKN.curie('transaksjon'),
                   model_uri=OKN.postering__transaksjon, domain=None, range=Optional[Union[str, TransaksjonId]])

slots.leverandor__kontonummer = Slot(uri=OKN.kontonummer, name="leverandor__kontonummer", curie=OKN.curie('kontonummer'),
                   model_uri=OKN.leverandor__kontonummer, domain=None, range=Optional[str])

slots.leverandor__leverandornummer = Slot(uri=OKN.leverandornummer, name="leverandor__leverandornummer", curie=OKN.curie('leverandornummer'),
                   model_uri=OKN.leverandor__leverandornummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.leverandor__person = Slot(uri=OKN.person, name="leverandor__person", curie=OKN.curie('person'),
                   model_uri=OKN.leverandor__person, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.leverandor__leverandorgruppe = Slot(uri=OKN.leverandorgruppe, name="leverandor__leverandorgruppe", curie=OKN.curie('leverandorgruppe'),
                   model_uri=OKN.leverandor__leverandorgruppe, domain=None, range=Optional[Union[str, LeverandorgruppeId]])

slots.leverandor__virksomhet = Slot(uri=OKN.virksomhet, name="leverandor__virksomhet", curie=OKN.curie('virksomhet'),
                   model_uri=OKN.leverandor__virksomhet, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.leverandorgruppe__navn = Slot(uri=OKN.navn, name="leverandorgruppe__navn", curie=OKN.curie('navn'),
                   model_uri=OKN.leverandorgruppe__navn, domain=None, range=str)

slots.leverandorgruppe__leverandor = Slot(uri=OKN.leverandor, name="leverandorgruppe__leverandor", curie=OKN.curie('leverandor'),
                   model_uri=OKN.leverandorgruppe__leverandor, domain=None, range=Optional[Union[Union[str, LeverandorId], list[Union[str, LeverandorId]]]])

slots.bilag__bilagsdato = Slot(uri=OKN.bilagsdato, name="bilag__bilagsdato", curie=OKN.curie('bilagsdato'),
                   model_uri=OKN.bilag__bilagsdato, domain=None, range=Union[str, XSDDate])

slots.bilag__bilagsnummer = Slot(uri=OKN.bilagsnummer, name="bilag__bilagsnummer", curie=OKN.curie('bilagsnummer'),
                   model_uri=OKN.bilag__bilagsnummer, domain=None, range=Optional[str])

slots.bilag__referanse = Slot(uri=OKN.referanse, name="bilag__referanse", curie=OKN.curie('referanse'),
                   model_uri=OKN.bilag__referanse, domain=None, range=Optional[str])

slots.bilag__url = Slot(uri=OKN.url, name="bilag__url", curie=OKN.curie('url'),
                   model_uri=OKN.bilag__url, domain=None, range=Optional[str])

slots.bilag__filnavn = Slot(uri=OKN.filnavn, name="bilag__filnavn", curie=OKN.curie('filnavn'),
                   model_uri=OKN.bilag__filnavn, domain=None, range=Optional[str])

slots.bilag__data = Slot(uri=OKN.data, name="bilag__data", curie=OKN.curie('data'),
                   model_uri=OKN.bilag__data, domain=None, range=Optional[str])

slots.kontostreng__art = Slot(uri=OKN.art, name="kontostreng__art", curie=OKN.curie('art'),
                   model_uri=OKN.kontostreng__art, domain=None, range=Optional[str])

slots.kontostreng__funksjon = Slot(uri=OKN.funksjon, name="kontostreng__funksjon", curie=OKN.curie('funksjon'),
                   model_uri=OKN.kontostreng__funksjon, domain=None, range=Optional[str])

slots.kontostreng__ansvar = Slot(uri=OKN.ansvar, name="kontostreng__ansvar", curie=OKN.curie('ansvar'),
                   model_uri=OKN.kontostreng__ansvar, domain=None, range=Optional[str])

slots.kontostreng__prosjekt = Slot(uri=OKN.prosjekt, name="kontostreng__prosjekt", curie=OKN.curie('prosjekt'),
                   model_uri=OKN.kontostreng__prosjekt, domain=None, range=Optional[str])

slots.vare__kode = Slot(uri=OKN.kode, name="vare__kode", curie=OKN.curie('kode'),
                   model_uri=OKN.vare__kode, domain=None, range=str)

slots.vare__navn = Slot(uri=OKN.navn, name="vare__navn", curie=OKN.curie('navn'),
                   model_uri=OKN.vare__navn, domain=None, range=str)

slots.vare__enhet = Slot(uri=OKN.enhet, name="vare__enhet", curie=OKN.curie('enhet'),
                   model_uri=OKN.vare__enhet, domain=None, range=str)

slots.vare__pris = Slot(uri=OKN.pris, name="vare__pris", curie=OKN.curie('pris'),
                   model_uri=OKN.vare__pris, domain=None, range=int)

slots.vare__kontering = Slot(uri=OKN.kontering, name="vare__kontering", curie=OKN.curie('kontering'),
                   model_uri=OKN.vare__kontering, domain=None, range=Optional[Union[dict, Kontostreng]])

slots.vare__gyldighetsperiode = Slot(uri=OKN.gyldighetsperiode, name="vare__gyldighetsperiode", curie=OKN.curie('gyldighetsperiode'),
                   model_uri=OKN.vare__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.vare__passiv = Slot(uri=OKN.passiv, name="vare__passiv", curie=OKN.curie('passiv'),
                   model_uri=OKN.vare__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.vare__fakturautsteder = Slot(uri=OKN.fakturautsteder, name="vare__fakturautsteder", curie=OKN.curie('fakturautsteder'),
                   model_uri=OKN.vare__fakturautsteder, domain=None, range=Union[str, FakturautstederId])

slots.vare__merverdiavgift = Slot(uri=OKN.merverdiavgift, name="vare__merverdiavgift", curie=OKN.curie('merverdiavgift'),
                   model_uri=OKN.vare__merverdiavgift, domain=None, range=Union[str, MerverdiavgiftId])

slots.merverdiavgift__kode = Slot(uri=OKN.kode, name="merverdiavgift__kode", curie=OKN.curie('kode'),
                   model_uri=OKN.merverdiavgift__kode, domain=None, range=str)

slots.merverdiavgift__navn = Slot(uri=OKN.navn, name="merverdiavgift__navn", curie=OKN.curie('navn'),
                   model_uri=OKN.merverdiavgift__navn, domain=None, range=str)

slots.merverdiavgift__sats = Slot(uri=OKN.sats, name="merverdiavgift__sats", curie=OKN.curie('sats'),
                   model_uri=OKN.merverdiavgift__sats, domain=None, range=int)

slots.merverdiavgift__gyldighetsperiode = Slot(uri=OKN.gyldighetsperiode, name="merverdiavgift__gyldighetsperiode", curie=OKN.curie('gyldighetsperiode'),
                   model_uri=OKN.merverdiavgift__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.merverdiavgift__passiv = Slot(uri=OKN.passiv, name="merverdiavgift__passiv", curie=OKN.curie('passiv'),
                   model_uri=OKN.merverdiavgift__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.okonomiValuta__kode = Slot(uri=OKN.kode, name="okonomiValuta__kode", curie=OKN.curie('kode'),
                   model_uri=OKN.okonomiValuta__kode, domain=None, range=str)

slots.okonomiValuta__navn = Slot(uri=OKN.namn, name="okonomiValuta__navn", curie=OKN.curie('namn'),
                   model_uri=OKN.okonomiValuta__navn, domain=None, range=str)

slots.okonomiValuta__gyldighetsperiode = Slot(uri=OKN.gyldighetsperiode, name="okonomiValuta__gyldighetsperiode", curie=OKN.curie('gyldighetsperiode'),
                   model_uri=OKN.okonomiValuta__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.okonomiValuta__passiv = Slot(uri=OKN.passiv, name="okonomiValuta__passiv", curie=OKN.curie('passiv'),
                   model_uri=OKN.okonomiValuta__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.aktoer__kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="aktoer__kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=OKN.aktoer__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.aktoer__postadresse = Slot(uri=FINT.postadresse, name="aktoer__postadresse", curie=FINT.curie('postadresse'),
                   model_uri=OKN.aktoer__postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.begrep__kode = Slot(uri=FINT.kode, name="begrep__kode", curie=FINT.curie('kode'),
                   model_uri=OKN.begrep__kode, domain=None, range=str)

slots.begrep__navn = Slot(uri=FINT.navn, name="begrep__navn", curie=FINT.curie('navn'),
                   model_uri=OKN.begrep__navn, domain=None, range=str)

slots.begrep__gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="begrep__gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=OKN.begrep__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.begrep__passiv = Slot(uri=FINT.passiv, name="begrep__passiv", curie=FINT.curie('passiv'),
                   model_uri=OKN.begrep__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.enhet__forretningsadresse = Slot(uri=FINT.forretningsadresse, name="enhet__forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=OKN.enhet__forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.enhet__organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="enhet__organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=OKN.enhet__organisasjonsnavn, domain=None, range=Optional[str])

slots.enhet__organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="enhet__organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=OKN.enhet__organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.identifikator__identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="identifikator__identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=OKN.identifikator__identifikatorverdi, domain=None, range=str)

slots.identifikator__gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="identifikator__gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=OKN.identifikator__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.periode__beskrivelse = Slot(uri=FINT.beskrivelse, name="periode__beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=OKN.periode__beskrivelse, domain=None, range=Optional[str])

slots.periode__start = Slot(uri=FINT.start, name="periode__start", curie=FINT.curie('start'),
                   model_uri=OKN.periode__start, domain=None, range=Union[str, XSDDateTime])

slots.periode__slutt = Slot(uri=FINT.slutt, name="periode__slutt", curie=FINT.curie('slutt'),
                   model_uri=OKN.periode__slutt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.personnavn__fornavn = Slot(uri=FINT.fornavn, name="personnavn__fornavn", curie=FINT.curie('fornavn'),
                   model_uri=OKN.personnavn__fornavn, domain=None, range=str)

slots.personnavn__mellomnavn = Slot(uri=FINT.mellomnavn, name="personnavn__mellomnavn", curie=FINT.curie('mellomnavn'),
                   model_uri=OKN.personnavn__mellomnavn, domain=None, range=Optional[str])

slots.personnavn__etternavn = Slot(uri=FINT.etternavn, name="personnavn__etternavn", curie=FINT.curie('etternavn'),
                   model_uri=OKN.personnavn__etternavn, domain=None, range=str)

slots.kontaktinformasjon__epostadresse = Slot(uri=FINT.epostadresse, name="kontaktinformasjon__epostadresse", curie=FINT.curie('epostadresse'),
                   model_uri=OKN.kontaktinformasjon__epostadresse, domain=None, range=Optional[str])

slots.kontaktinformasjon__mobiltelefonnummer = Slot(uri=FINT.mobiltelefonnummer, name="kontaktinformasjon__mobiltelefonnummer", curie=FINT.curie('mobiltelefonnummer'),
                   model_uri=OKN.kontaktinformasjon__mobiltelefonnummer, domain=None, range=Optional[str])

slots.kontaktinformasjon__nettsted = Slot(uri=FINT.nettsted, name="kontaktinformasjon__nettsted", curie=FINT.curie('nettsted'),
                   model_uri=OKN.kontaktinformasjon__nettsted, domain=None, range=Optional[str])

slots.kontaktinformasjon__sip = Slot(uri=FINT.sip, name="kontaktinformasjon__sip", curie=FINT.curie('sip'),
                   model_uri=OKN.kontaktinformasjon__sip, domain=None, range=Optional[str])

slots.kontaktinformasjon__telefonnummer = Slot(uri=FINT.telefonnummer, name="kontaktinformasjon__telefonnummer", curie=FINT.curie('telefonnummer'),
                   model_uri=OKN.kontaktinformasjon__telefonnummer, domain=None, range=Optional[str])

slots.adresse__adresselinje = Slot(uri=FINT.adresselinje, name="adresse__adresselinje", curie=FINT.curie('adresselinje'),
                   model_uri=OKN.adresse__adresselinje, domain=None, range=Optional[Union[str, list[str]]])

slots.adresse__postnummer = Slot(uri=FINT.postnummer, name="adresse__postnummer", curie=FINT.curie('postnummer'),
                   model_uri=OKN.adresse__postnummer, domain=None, range=Optional[str])

slots.adresse__poststed = Slot(uri=FINT.poststed, name="adresse__poststed", curie=FINT.curie('poststed'),
                   model_uri=OKN.adresse__poststed, domain=None, range=Optional[str])

slots.adresse__land = Slot(uri=FINT.land, name="adresse__land", curie=FINT.curie('land'),
                   model_uri=OKN.adresse__land, domain=None, range=Optional[Union[str, LandkodeId]])

slots.matrikkelnummer__adresse = Slot(uri=FINT.adresse, name="matrikkelnummer__adresse", curie=FINT.curie('adresse'),
                   model_uri=OKN.matrikkelnummer__adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.matrikkelnummer__bruksnummer = Slot(uri=FINT.bruksnummer, name="matrikkelnummer__bruksnummer", curie=FINT.curie('bruksnummer'),
                   model_uri=OKN.matrikkelnummer__bruksnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__festenummer = Slot(uri=FINT.festenummer, name="matrikkelnummer__festenummer", curie=FINT.curie('festenummer'),
                   model_uri=OKN.matrikkelnummer__festenummer, domain=None, range=Optional[str])

slots.matrikkelnummer__gaardsnummer = Slot(uri=FINT.gaardsnummer, name="matrikkelnummer__gaardsnummer", curie=FINT.curie('gaardsnummer'),
                   model_uri=OKN.matrikkelnummer__gaardsnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__seksjonsnummer = Slot(uri=FINT.seksjonsnummer, name="matrikkelnummer__seksjonsnummer", curie=FINT.curie('seksjonsnummer'),
                   model_uri=OKN.matrikkelnummer__seksjonsnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__kommunenummer = Slot(uri=FINT.kommunenummer, name="matrikkelnummer__kommunenummer", curie=FINT.curie('kommunenummer'),
                   model_uri=OKN.matrikkelnummer__kommunenummer, domain=None, range=Optional[Union[str, KommuneId]])

slots.fylke__kommune = Slot(uri=FINT.kommune, name="fylke__kommune", curie=FINT.curie('kommune'),
                   model_uri=OKN.fylke__kommune, domain=None, range=Optional[Union[Union[str, KommuneId], list[Union[str, KommuneId]]]])

slots.kommune__fylke = Slot(uri=FINT.fylke, name="kommune__fylke", curie=FINT.curie('fylke'),
                   model_uri=OKN.kommune__fylke, domain=None, range=Union[str, FylkeId])

slots.valuta__bokstavkode = Slot(uri=FINT.bokstavkode, name="valuta__bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=OKN.valuta__bokstavkode, domain=None, range=Union[dict, Identifikator])

slots.valuta__navn = Slot(uri=FINT.valutaNavn, name="valuta__navn", curie=FINT.curie('valutaNavn'),
                   model_uri=OKN.valuta__navn, domain=None, range=str)

slots.valuta__nummerkode = Slot(uri=FINT.nummerkode, name="valuta__nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=OKN.valuta__nummerkode, domain=None, range=Union[dict, Identifikator])

slots.person__bilde = Slot(uri=FINT.bilde, name="person__bilde", curie=FINT.curie('bilde'),
                   model_uri=OKN.person__bilde, domain=None, range=Optional[str])

slots.person__bostedsadresse = Slot(uri=FINT.bostedsadresse, name="person__bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=OKN.person__bostedsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.person__fodselsdato = Slot(uri=FINT.fodselsdato, name="person__fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=OKN.person__fodselsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.person__fodselsnummer = Slot(uri=FINT.fodselsnummer, name="person__fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=OKN.person__fodselsnummer, domain=None, range=Union[dict, Identifikator])

slots.person__navn = Slot(uri=FINT.personNavn, name="person__navn", curie=FINT.curie('personNavn'),
                   model_uri=OKN.person__navn, domain=None, range=Union[dict, Personnavn])

slots.person__parorende = Slot(uri=FINT.parorende, name="person__parorende", curie=FINT.curie('parorende'),
                   model_uri=OKN.person__parorende, domain=None, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.person__statsborgerskap = Slot(uri=FINT.statsborgerskap, name="person__statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=OKN.person__statsborgerskap, domain=None, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.person__kommune = Slot(uri=FINT.kommune, name="person__kommune", curie=FINT.curie('kommune'),
                   model_uri=OKN.person__kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.person__kjonn = Slot(uri=FINT.kjonn, name="person__kjonn", curie=FINT.curie('kjonn'),
                   model_uri=OKN.person__kjonn, domain=None, range=Optional[Union[str, KjonnId]])

slots.person__foreldreansvar = Slot(uri=FINT.foreldreansvar, name="person__foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=OKN.person__foreldreansvar, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.person__foreldre = Slot(uri=FINT.foreldre, name="person__foreldre", curie=FINT.curie('foreldre'),
                   model_uri=OKN.person__foreldre, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.person__maalform = Slot(uri=FINT.maalform, name="person__maalform", curie=FINT.curie('maalform'),
                   model_uri=OKN.person__maalform, domain=None, range=Optional[Union[str, SpraakId]])

slots.person__personalressurs = Slot(uri=FINT.personalressurs, name="person__personalressurs", curie=FINT.curie('personalressurs'),
                   model_uri=OKN.person__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.person__morsmaal = Slot(uri=FINT.morsmaal, name="person__morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=OKN.person__morsmaal, domain=None, range=Optional[Union[str, SpraakId]])

slots.person__laerling = Slot(uri=FINT.laerling, name="person__laerling", curie=FINT.curie('laerling'),
                   model_uri=OKN.person__laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.person__elev = Slot(uri=FINT.elev, name="person__elev", curie=FINT.curie('elev'),
                   model_uri=OKN.person__elev, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.person__otungdom = Slot(uri=FINT.otungdom, name="person__otungdom", curie=FINT.curie('otungdom'),
                   model_uri=OKN.person__otungdom, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kontaktperson__kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="kontaktperson__kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=OKN.kontaktperson__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.kontaktperson__navn = Slot(uri=FINT.kontaktpersonNavn, name="kontaktperson__navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=OKN.kontaktperson__navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.kontaktperson__type = Slot(uri=FINT.type, name="kontaktperson__type", curie=FINT.curie('type'),
                   model_uri=OKN.kontaktperson__type, domain=None, range=str)

slots.kontaktperson__kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="kontaktperson__kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=OKN.kontaktperson__kontaktperson, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.virksomhet__virksomhetsId = Slot(uri=FINT.virksomhetsId, name="virksomhet__virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=OKN.virksomhet__virksomhetsId, domain=None, range=Union[dict, Identifikator])

slots.virksomhet__laerling = Slot(uri=FINT.laerling, name="virksomhet__laerling", curie=FINT.curie('laerling'),
                   model_uri=OKN.virksomhet__laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

