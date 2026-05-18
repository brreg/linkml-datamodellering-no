# Auto generated from fint-okonomi-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-18T09:10:56
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
    fakturamottaker: Union[dict, "Fakturamottaker"] = None
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

        if self._is_empty(self.fakturamottaker):
            self.MissingRequiredField("fakturamottaker")
        if not isinstance(self.fakturamottaker, Fakturamottaker):
            self.fakturamottaker = Fakturamottaker(**as_dict(self.fakturamottaker))

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

    person: Union[str, PersonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.person):
            self.MissingRequiredField("person")
        if not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

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
    Person eller verksemd som leverer produkt eller tenester.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKN["Leverandor"]
    class_class_curie: ClassVar[str] = "okn:Leverandor"
    class_name: ClassVar[str] = "Leverandor"
    class_model_uri: ClassVar[URIRef] = OKN.Leverandor

    id: Union[str, LeverandorId] = None
    kontonummer: Optional[str] = None
    leverandornummer: Optional[Union[dict, "Identifikator"]] = None
    person: Optional[Union[str, PersonId]] = None
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

        if self.person is not None and not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

        if self.leverandorgruppe is not None and not isinstance(self.leverandorgruppe, LeverandorgruppeId):
            self.leverandorgruppe = LeverandorgruppeId(self.leverandorgruppe)

        if self.virksomhet is not None and not isinstance(self.virksomhet, URIorCURIE):
            self.virksomhet = URIorCURIE(self.virksomhet)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Leverandorgruppe(YAMLRoot):
    """
    Gruppering av leverandørar.
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
class Elev(YAMLRoot):
    """
    Ein elev registrert i skulesystemet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Elev"]
    class_class_curie: ClassVar[str] = "fint:Elev"
    class_name: ClassVar[str] = "Elev"
    class_model_uri: ClassVar[URIRef] = OKN.Elev

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
    class_model_uri: ClassVar[URIRef] = OKN.Person

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
    class_model_uri: ClassVar[URIRef] = OKN.Kontaktperson

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

slots.fakturaer = Slot(uri=OKN.fakturaer, name="fakturaer", curie=OKN.curie('fakturaer'),
                   model_uri=OKN.fakturaer, domain=None, range=Optional[Union[dict[Union[str, FakturaId], Union[dict, Faktura]], list[Union[dict, Faktura]]]])

slots.fakturautstederear = Slot(uri=OKN.fakturautstederear, name="fakturautstederear", curie=OKN.curie('fakturautstederear'),
                   model_uri=OKN.fakturautstederear, domain=None, range=Optional[Union[dict[Union[str, FakturautstederId], Union[dict, Fakturautsteder]], list[Union[dict, Fakturautsteder]]]])

slots.transaksjonar = Slot(uri=OKN.transaksjonar, name="transaksjonar", curie=OKN.curie('transaksjonar'),
                   model_uri=OKN.transaksjonar, domain=None, range=Optional[Union[dict[Union[str, TransaksjonId], Union[dict, Transaksjon]], list[Union[dict, Transaksjon]]]])

slots.posteringar = Slot(uri=OKN.posteringar, name="posteringar", curie=OKN.curie('posteringar'),
                   model_uri=OKN.posteringar, domain=None, range=Optional[Union[dict[Union[str, PosteringId], Union[dict, Postering]], list[Union[dict, Postering]]]])

slots.leverandorar = Slot(uri=OKN.leverandorar, name="leverandorar", curie=OKN.curie('leverandorar'),
                   model_uri=OKN.leverandorar, domain=None, range=Optional[Union[dict[Union[str, LeverandorId], Union[dict, Leverandor]], list[Union[dict, Leverandor]]]])

slots.leverandorgrupper = Slot(uri=OKN.leverandorgrupper, name="leverandorgrupper", curie=OKN.curie('leverandorgrupper'),
                   model_uri=OKN.leverandorgrupper, domain=None, range=Optional[Union[dict[Union[str, LeverandorgruppeId], Union[dict, Leverandorgruppe]], list[Union[dict, Leverandorgruppe]]]])

slots.varer = Slot(uri=OKN.varer, name="varer", curie=OKN.curie('varer'),
                   model_uri=OKN.varer, domain=None, range=Optional[Union[dict[Union[str, VareId], Union[dict, Vare]], list[Union[dict, Vare]]]])

slots.merverdiavgifter = Slot(uri=OKN.merverdiavgifter, name="merverdiavgifter", curie=OKN.curie('merverdiavgifter'),
                   model_uri=OKN.merverdiavgifter, domain=None, range=Optional[Union[dict[Union[str, MerverdiavgiftId], Union[dict, Merverdiavgift]], list[Union[dict, Merverdiavgift]]]])

slots.valutaer = Slot(uri=OKN.valutaer, name="valutaer", curie=OKN.curie('valutaer'),
                   model_uri=OKN.valutaer, domain=None, range=Optional[Union[dict[Union[str, OkonomiValutaId], Union[dict, OkonomiValuta]], list[Union[dict, OkonomiValuta]]]])

slots.fakturagrunnlag = Slot(uri=OKN.fakturagrunnlag, name="fakturagrunnlag", curie=OKN.curie('fakturagrunnlag'),
                   model_uri=OKN.fakturagrunnlag, domain=None, range=Optional[Union[str, FakturagrunnlagId]])

slots.fakturautsteder = Slot(uri=OKN.fakturautsteder, name="fakturautsteder", curie=OKN.curie('fakturautsteder'),
                   model_uri=OKN.fakturautsteder, domain=None, range=Optional[Union[str, FakturautstederId]])

slots.belop = Slot(uri=OKN.belop, name="belop", curie=OKN.curie('belop'),
                   model_uri=OKN.belop, domain=None, range=Optional[int])

slots.forfallsdato = Slot(uri=OKN.forfallsdato, name="forfallsdato", curie=OKN.curie('forfallsdato'),
                   model_uri=OKN.forfallsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.pris = Slot(uri=OKN.pris, name="pris", curie=OKN.curie('pris'),
                   model_uri=OKN.pris, domain=None, range=Optional[int])

slots.kontering = Slot(uri=OKN.kontering, name="kontering", curie=OKN.curie('kontering'),
                   model_uri=OKN.kontering, domain=None, range=Optional[Union[dict, Kontostreng]])

slots.vare = Slot(uri=OKN.vare, name="vare", curie=OKN.curie('vare'),
                   model_uri=OKN.vare, domain=None, range=Optional[Union[str, VareId]])

slots.leverandor = Slot(uri=OKN.leverandor, name="leverandor", curie=OKN.curie('leverandor'),
                   model_uri=OKN.leverandor, domain=None, range=Optional[Union[str, LeverandorId]])

slots.fakturanummer = Slot(uri=OKN.fakturanummer, name="fakturanummer", curie=OKN.curie('fakturanummer'),
                   model_uri=OKN.fakturanummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.dato = Slot(uri=OKN.dato, name="dato", curie=OKN.curie('dato'),
                   model_uri=OKN.dato, domain=None, range=Optional[Union[str, XSDDate]])

slots.mottaker = Slot(uri=OKN.mottaker, name="mottaker", curie=OKN.curie('mottaker'),
                   model_uri=OKN.mottaker, domain=None, range=Optional[str])

slots.betalt = Slot(uri=OKN.betalt, name="betalt", curie=OKN.curie('betalt'),
                   model_uri=OKN.betalt, domain=None, range=Optional[Union[bool, Bool]])

slots.fakturert = Slot(uri=OKN.fakturert, name="fakturert", curie=OKN.curie('fakturert'),
                   model_uri=OKN.fakturert, domain=None, range=Optional[Union[bool, Bool]])

slots.kreditert = Slot(uri=OKN.kreditert, name="kreditert", curie=OKN.curie('kreditert'),
                   model_uri=OKN.kreditert, domain=None, range=Optional[Union[bool, Bool]])

slots.restbelop = Slot(uri=OKN.restbelop, name="restbelop", curie=OKN.curie('restbelop'),
                   model_uri=OKN.restbelop, domain=None, range=Optional[int])

slots.ordrenummer = Slot(uri=OKN.ordrenummer, name="ordrenummer", curie=OKN.curie('ordrenummer'),
                   model_uri=OKN.ordrenummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.fakturamottaker = Slot(uri=OKN.fakturamottaker, name="fakturamottaker", curie=OKN.curie('fakturamottaker'),
                   model_uri=OKN.fakturamottaker, domain=None, range=Optional[Union[dict, Fakturamottaker]])

slots.fakturalinjer = Slot(uri=OKN.fakturalinjer, name="fakturalinjer", curie=OKN.curie('fakturalinjer'),
                   model_uri=OKN.fakturalinjer, domain=None, range=Optional[Union[Union[dict, Fakturalinje], list[Union[dict, Fakturalinje]]]])

slots.leveringsdato = Slot(uri=OKN.leveringsdato, name="leveringsdato", curie=OKN.curie('leveringsdato'),
                   model_uri=OKN.leveringsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.nettobelop = Slot(uri=OKN.nettobelop, name="nettobelop", curie=OKN.curie('nettobelop'),
                   model_uri=OKN.nettobelop, domain=None, range=Optional[int])

slots.avgiftsbelop = Slot(uri=OKN.avgiftsbelop, name="avgiftsbelop", curie=OKN.curie('avgiftsbelop'),
                   model_uri=OKN.avgiftsbelop, domain=None, range=Optional[int])

slots.totalbelop = Slot(uri=OKN.totalbelop, name="totalbelop", curie=OKN.curie('totalbelop'),
                   model_uri=OKN.totalbelop, domain=None, range=Optional[int])

slots.faktura = Slot(uri=OKN.faktura, name="faktura", curie=OKN.curie('faktura'),
                   model_uri=OKN.faktura, domain=None, range=Optional[Union[Union[str, FakturaId], list[Union[str, FakturaId]]]])

slots.organisasjonselement = Slot(uri=OKN.organisasjonselement, name="organisasjonselement", curie=OKN.curie('organisasjonselement'),
                   model_uri=OKN.organisasjonselement, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.antall = Slot(uri=OKN.antall, name="antall", curie=OKN.curie('antall'),
                   model_uri=OKN.antall, domain=None, range=Optional[float])

slots.fritekst = Slot(uri=OKN.fritekst, name="fritekst", curie=OKN.curie('fritekst'),
                   model_uri=OKN.fritekst, domain=None, range=Optional[Union[str, list[str]]])

slots.transaksjonsId = Slot(uri=OKN.transaksjonsId, name="transaksjonsId", curie=OKN.curie('transaksjonsId'),
                   model_uri=OKN.transaksjonsId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.bilag = Slot(uri=OKN.bilag, name="bilag", curie=OKN.curie('bilag'),
                   model_uri=OKN.bilag, domain=None, range=Optional[Union[Union[dict, Bilag], list[Union[dict, Bilag]]]])

slots.transaksjonstidspunkt = Slot(uri=OKN.transaksjonstidspunkt, name="transaksjonstidspunkt", curie=OKN.curie('transaksjonstidspunkt'),
                   model_uri=OKN.transaksjonstidspunkt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.oppdateringstidspunkt = Slot(uri=OKN.oppdateringstidspunkt, name="oppdateringstidspunkt", curie=OKN.curie('oppdateringstidspunkt'),
                   model_uri=OKN.oppdateringstidspunkt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.postering = Slot(uri=OKN.postering, name="postering", curie=OKN.curie('postering'),
                   model_uri=OKN.postering, domain=None, range=Optional[Union[Union[str, PosteringId], list[Union[str, PosteringId]]]])

slots.ansvarlig = Slot(uri=OKN.ansvarlig, name="ansvarlig", curie=OKN.curie('ansvarlig'),
                   model_uri=OKN.ansvarlig, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.valuta = Slot(uri=OKN.valuta, name="valuta", curie=OKN.curie('valuta'),
                   model_uri=OKN.valuta, domain=None, range=Optional[Union[str, OkonomiValutaId]])

slots.posteringsId = Slot(uri=OKN.posteringsId, name="posteringsId", curie=OKN.curie('posteringsId'),
                   model_uri=OKN.posteringsId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.debet = Slot(uri=OKN.debet, name="debet", curie=OKN.curie('debet'),
                   model_uri=OKN.debet, domain=None, range=Optional[Union[bool, Bool]])

slots.transaksjon = Slot(uri=OKN.transaksjon, name="transaksjon", curie=OKN.curie('transaksjon'),
                   model_uri=OKN.transaksjon, domain=None, range=Optional[Union[str, TransaksjonId]])

slots.kontonummer = Slot(uri=OKN.kontonummer, name="kontonummer", curie=OKN.curie('kontonummer'),
                   model_uri=OKN.kontonummer, domain=None, range=Optional[str])

slots.leverandornummer = Slot(uri=OKN.leverandornummer, name="leverandornummer", curie=OKN.curie('leverandornummer'),
                   model_uri=OKN.leverandornummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.leverandorgruppe = Slot(uri=OKN.leverandorgruppe, name="leverandorgruppe", curie=OKN.curie('leverandorgruppe'),
                   model_uri=OKN.leverandorgruppe, domain=None, range=Optional[Union[str, LeverandorgruppeId]])

slots.virksomhet = Slot(uri=OKN.virksomhet, name="virksomhet", curie=OKN.curie('virksomhet'),
                   model_uri=OKN.virksomhet, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.bilagsdato = Slot(uri=OKN.bilagsdato, name="bilagsdato", curie=OKN.curie('bilagsdato'),
                   model_uri=OKN.bilagsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.bilagsnummer = Slot(uri=OKN.bilagsnummer, name="bilagsnummer", curie=OKN.curie('bilagsnummer'),
                   model_uri=OKN.bilagsnummer, domain=None, range=Optional[str])

slots.referanse = Slot(uri=OKN.referanse, name="referanse", curie=OKN.curie('referanse'),
                   model_uri=OKN.referanse, domain=None, range=Optional[str])

slots.url = Slot(uri=OKN.url, name="url", curie=OKN.curie('url'),
                   model_uri=OKN.url, domain=None, range=Optional[str])

slots.filnavn = Slot(uri=OKN.filnavn, name="filnavn", curie=OKN.curie('filnavn'),
                   model_uri=OKN.filnavn, domain=None, range=Optional[str])

slots.data = Slot(uri=OKN.data, name="data", curie=OKN.curie('data'),
                   model_uri=OKN.data, domain=None, range=Optional[str])

slots.art = Slot(uri=OKN.art, name="art", curie=OKN.curie('art'),
                   model_uri=OKN.art, domain=None, range=Optional[str])

slots.funksjon = Slot(uri=OKN.funksjon, name="funksjon", curie=OKN.curie('funksjon'),
                   model_uri=OKN.funksjon, domain=None, range=Optional[str])

slots.ansvar = Slot(uri=OKN.ansvar, name="ansvar", curie=OKN.curie('ansvar'),
                   model_uri=OKN.ansvar, domain=None, range=Optional[str])

slots.prosjekt = Slot(uri=OKN.prosjekt, name="prosjekt", curie=OKN.curie('prosjekt'),
                   model_uri=OKN.prosjekt, domain=None, range=Optional[str])

slots.enhet = Slot(uri=OKN.enhet, name="enhet", curie=OKN.curie('enhet'),
                   model_uri=OKN.enhet, domain=None, range=Optional[str])

slots.merverdiavgift = Slot(uri=OKN.merverdiavgift, name="merverdiavgift", curie=OKN.curie('merverdiavgift'),
                   model_uri=OKN.merverdiavgift, domain=None, range=Optional[Union[str, MerverdiavgiftId]])

slots.sats = Slot(uri=OKN.sats, name="sats", curie=OKN.curie('sats'),
                   model_uri=OKN.sats, domain=None, range=Optional[int])

slots.id = Slot(uri=FINT.id, name="id", curie=FINT.curie('id'),
                   model_uri=OKN.id, domain=None, range=URIRef)

slots.gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=OKN.gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=OKN.kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.postadresse = Slot(uri=FINT.postadresse, name="postadresse", curie=FINT.curie('postadresse'),
                   model_uri=OKN.postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.forretningsadresse = Slot(uri=FINT.forretningsadresse, name="forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=OKN.forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=OKN.organisasjonsnavn, domain=None, range=Optional[str])

slots.organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=OKN.organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.kode = Slot(uri=FINT.kode, name="kode", curie=FINT.curie('kode'),
                   model_uri=OKN.kode, domain=None, range=Optional[str])

slots.navn = Slot(uri=FINT.navn, name="navn", curie=FINT.curie('navn'),
                   model_uri=OKN.navn, domain=None, range=Optional[str])

slots.passiv = Slot(uri=FINT.passiv, name="passiv", curie=FINT.curie('passiv'),
                   model_uri=OKN.passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=OKN.identifikatorverdi, domain=None, range=Optional[str])

slots.beskrivelse = Slot(uri=FINT.beskrivelse, name="beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=OKN.beskrivelse, domain=None, range=Optional[str])

slots.start = Slot(uri=FINT.start, name="start", curie=FINT.curie('start'),
                   model_uri=OKN.start, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.slutt = Slot(uri=FINT.slutt, name="slutt", curie=FINT.curie('slutt'),
                   model_uri=OKN.slutt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.fornavn = Slot(uri=FINT.fornavn, name="fornavn", curie=FINT.curie('fornavn'),
                   model_uri=OKN.fornavn, domain=None, range=Optional[str])

slots.mellomnavn = Slot(uri=FINT.mellomnavn, name="mellomnavn", curie=FINT.curie('mellomnavn'),
                   model_uri=OKN.mellomnavn, domain=None, range=Optional[str])

slots.etternavn = Slot(uri=FINT.etternavn, name="etternavn", curie=FINT.curie('etternavn'),
                   model_uri=OKN.etternavn, domain=None, range=Optional[str])

slots.epostadresse = Slot(uri=FINT.epostadresse, name="epostadresse", curie=FINT.curie('epostadresse'),
                   model_uri=OKN.epostadresse, domain=None, range=Optional[str])

slots.mobiltelefonnummer = Slot(uri=FINT.mobiltelefonnummer, name="mobiltelefonnummer", curie=FINT.curie('mobiltelefonnummer'),
                   model_uri=OKN.mobiltelefonnummer, domain=None, range=Optional[str])

slots.nettsted = Slot(uri=FINT.nettsted, name="nettsted", curie=FINT.curie('nettsted'),
                   model_uri=OKN.nettsted, domain=None, range=Optional[str])

slots.sip = Slot(uri=FINT.sip, name="sip", curie=FINT.curie('sip'),
                   model_uri=OKN.sip, domain=None, range=Optional[str])

slots.telefonnummer = Slot(uri=FINT.telefonnummer, name="telefonnummer", curie=FINT.curie('telefonnummer'),
                   model_uri=OKN.telefonnummer, domain=None, range=Optional[str])

slots.adresselinje = Slot(uri=FINT.adresselinje, name="adresselinje", curie=FINT.curie('adresselinje'),
                   model_uri=OKN.adresselinje, domain=None, range=Optional[Union[str, list[str]]])

slots.postnummer = Slot(uri=FINT.postnummer, name="postnummer", curie=FINT.curie('postnummer'),
                   model_uri=OKN.postnummer, domain=None, range=Optional[str])

slots.poststed = Slot(uri=FINT.poststed, name="poststed", curie=FINT.curie('poststed'),
                   model_uri=OKN.poststed, domain=None, range=Optional[str])

slots.land = Slot(uri=FINT.land, name="land", curie=FINT.curie('land'),
                   model_uri=OKN.land, domain=None, range=Optional[Union[str, LandkodeId]])

slots.adresse = Slot(uri=FINT.adresse, name="adresse", curie=FINT.curie('adresse'),
                   model_uri=OKN.adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.bruksnummer = Slot(uri=FINT.bruksnummer, name="bruksnummer", curie=FINT.curie('bruksnummer'),
                   model_uri=OKN.bruksnummer, domain=None, range=Optional[str])

slots.festenummer = Slot(uri=FINT.festenummer, name="festenummer", curie=FINT.curie('festenummer'),
                   model_uri=OKN.festenummer, domain=None, range=Optional[str])

slots.gaardsnummer = Slot(uri=FINT.gaardsnummer, name="gaardsnummer", curie=FINT.curie('gaardsnummer'),
                   model_uri=OKN.gaardsnummer, domain=None, range=Optional[str])

slots.seksjonsnummer = Slot(uri=FINT.seksjonsnummer, name="seksjonsnummer", curie=FINT.curie('seksjonsnummer'),
                   model_uri=OKN.seksjonsnummer, domain=None, range=Optional[str])

slots.kommunenummer = Slot(uri=FINT.kommunenummer, name="kommunenummer", curie=FINT.curie('kommunenummer'),
                   model_uri=OKN.kommunenummer, domain=None, range=Optional[Union[str, KommuneId]])

slots.fylke = Slot(uri=FINT.fylke, name="fylke", curie=FINT.curie('fylke'),
                   model_uri=OKN.fylke, domain=None, range=Optional[Union[str, FylkeId]])

slots.kommune = Slot(uri=FINT.kommune, name="kommune", curie=FINT.curie('kommune'),
                   model_uri=OKN.kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.kjonn = Slot(uri=FINT.kjonn, name="kjonn", curie=FINT.curie('kjonn'),
                   model_uri=OKN.kjonn, domain=None, range=Optional[Union[str, KjonnId]])

slots.bokstavkode = Slot(uri=FINT.bokstavkode, name="bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=OKN.bokstavkode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.valuta_navn = Slot(uri=FINT.valutaNavn, name="valuta_navn", curie=FINT.curie('valutaNavn'),
                   model_uri=OKN.valuta_navn, domain=None, range=Optional[str])

slots.nummerkode = Slot(uri=FINT.nummerkode, name="nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=OKN.nummerkode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.bilde = Slot(uri=FINT.bilde, name="bilde", curie=FINT.curie('bilde'),
                   model_uri=OKN.bilde, domain=None, range=Optional[str])

slots.bostedsadresse = Slot(uri=FINT.bostedsadresse, name="bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=OKN.bostedsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.fodselsdato = Slot(uri=FINT.fodselsdato, name="fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=OKN.fodselsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.fodselsnummer = Slot(uri=FINT.fodselsnummer, name="fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=OKN.fodselsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person_navn = Slot(uri=FINT.personNavn, name="person_navn", curie=FINT.curie('personNavn'),
                   model_uri=OKN.person_navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.parorende = Slot(uri=FINT.parorende, name="parorende", curie=FINT.curie('parorende'),
                   model_uri=OKN.parorende, domain=None, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.statsborgerskap = Slot(uri=FINT.statsborgerskap, name="statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=OKN.statsborgerskap, domain=None, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.foreldreansvar = Slot(uri=FINT.foreldreansvar, name="foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=OKN.foreldreansvar, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.foreldre = Slot(uri=FINT.foreldre, name="foreldre", curie=FINT.curie('foreldre'),
                   model_uri=OKN.foreldre, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.maalform = Slot(uri=FINT.maalform, name="maalform", curie=FINT.curie('maalform'),
                   model_uri=OKN.maalform, domain=None, range=Optional[Union[str, SpraakId]])

slots.morsmaal = Slot(uri=FINT.morsmaal, name="morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=OKN.morsmaal, domain=None, range=Optional[Union[str, SpraakId]])

slots.laerling = Slot(uri=FINT.laerling, name="laerling", curie=FINT.curie('laerling'),
                   model_uri=OKN.laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.elev = Slot(uri=FINT.elev, name="elev", curie=FINT.curie('elev'),
                   model_uri=OKN.elev, domain=None, range=Optional[Union[str, ElevId]])

slots.elevnummer = Slot(uri=FINT.elevnummer, name="elevnummer", curie=FINT.curie('elevnummer'),
                   model_uri=OKN.elevnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person = Slot(uri=FINT.person, name="person", curie=FINT.curie('person'),
                   model_uri=OKN.person, domain=None, range=Optional[Union[str, PersonId]])

slots.otungdom = Slot(uri=FINT.otungdom, name="otungdom", curie=FINT.curie('otungdom'),
                   model_uri=OKN.otungdom, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kontaktperson_navn = Slot(uri=FINT.kontaktpersonNavn, name="kontaktperson_navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=OKN.kontaktperson_navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.type = Slot(uri=FINT.type, name="type", curie=FINT.curie('type'),
                   model_uri=OKN.type, domain=None, range=Optional[str])

slots.kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=OKN.kontaktperson, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.virksomhetsId = Slot(uri=FINT.virksomhetsId, name="virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=OKN.virksomhetsId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person__personalressurs = Slot(uri=FINT.personalressurs, name="person__personalressurs", curie=FINT.curie('personalressurs'),
                   model_uri=OKN.person__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.OkonomiContainer_fakturagrunnlag = Slot(uri=OKN.fakturagrunnlag, name="OkonomiContainer_fakturagrunnlag", curie=OKN.curie('fakturagrunnlag'),
                   model_uri=OKN.OkonomiContainer_fakturagrunnlag, domain=OkonomiContainer, range=Optional[Union[dict[Union[str, FakturagrunnlagId], Union[dict, "Fakturagrunnlag"]], list[Union[dict, "Fakturagrunnlag"]]]])

slots.Faktura_fakturanummer = Slot(uri=OKN.fakturanummer, name="Faktura_fakturanummer", curie=OKN.curie('fakturanummer'),
                   model_uri=OKN.Faktura_fakturanummer, domain=Faktura, range=Union[dict, "Identifikator"])

slots.Faktura_dato = Slot(uri=OKN.dato, name="Faktura_dato", curie=OKN.curie('dato'),
                   model_uri=OKN.Faktura_dato, domain=Faktura, range=Union[str, XSDDate])

slots.Faktura_forfallsdato = Slot(uri=OKN.forfallsdato, name="Faktura_forfallsdato", curie=OKN.curie('forfallsdato'),
                   model_uri=OKN.Faktura_forfallsdato, domain=Faktura, range=Union[str, XSDDate])

slots.Faktura_belop = Slot(uri=OKN.belop, name="Faktura_belop", curie=OKN.curie('belop'),
                   model_uri=OKN.Faktura_belop, domain=Faktura, range=int)

slots.Faktura_mottaker = Slot(uri=OKN.mottaker, name="Faktura_mottaker", curie=OKN.curie('mottaker'),
                   model_uri=OKN.Faktura_mottaker, domain=Faktura, range=str)

slots.Faktura_adresse = Slot(uri=FINT.adresse, name="Faktura_adresse", curie=FINT.curie('adresse'),
                   model_uri=OKN.Faktura_adresse, domain=Faktura, range=Optional[Union[dict, "Adresse"]])

slots.Faktura_betalt = Slot(uri=OKN.betalt, name="Faktura_betalt", curie=OKN.curie('betalt'),
                   model_uri=OKN.Faktura_betalt, domain=Faktura, range=Optional[Union[bool, Bool]])

slots.Faktura_fakturert = Slot(uri=OKN.fakturert, name="Faktura_fakturert", curie=OKN.curie('fakturert'),
                   model_uri=OKN.Faktura_fakturert, domain=Faktura, range=Optional[Union[bool, Bool]])

slots.Faktura_kreditert = Slot(uri=OKN.kreditert, name="Faktura_kreditert", curie=OKN.curie('kreditert'),
                   model_uri=OKN.Faktura_kreditert, domain=Faktura, range=Optional[Union[bool, Bool]])

slots.Faktura_restbelop = Slot(uri=OKN.restbelop, name="Faktura_restbelop", curie=OKN.curie('restbelop'),
                   model_uri=OKN.Faktura_restbelop, domain=Faktura, range=Optional[int])

slots.Faktura_fakturagrunnlag = Slot(uri=OKN.fakturagrunnlag, name="Faktura_fakturagrunnlag", curie=OKN.curie('fakturagrunnlag'),
                   model_uri=OKN.Faktura_fakturagrunnlag, domain=Faktura, range=Union[str, FakturagrunnlagId])

slots.Fakturagrunnlag_ordrenummer = Slot(uri=OKN.ordrenummer, name="Fakturagrunnlag_ordrenummer", curie=OKN.curie('ordrenummer'),
                   model_uri=OKN.Fakturagrunnlag_ordrenummer, domain=Fakturagrunnlag, range=Union[dict, "Identifikator"])

slots.Fakturagrunnlag_fakturamottaker = Slot(uri=OKN.fakturamottaker, name="Fakturagrunnlag_fakturamottaker", curie=OKN.curie('fakturamottaker'),
                   model_uri=OKN.Fakturagrunnlag_fakturamottaker, domain=Fakturagrunnlag, range=Union[dict, "Fakturamottaker"])

slots.Fakturagrunnlag_fakturalinjer = Slot(uri=OKN.fakturalinjer, name="Fakturagrunnlag_fakturalinjer", curie=OKN.curie('fakturalinjer'),
                   model_uri=OKN.Fakturagrunnlag_fakturalinjer, domain=Fakturagrunnlag, range=Union[Union[dict, "Fakturalinje"], list[Union[dict, "Fakturalinje"]]])

slots.Fakturagrunnlag_leveringsdato = Slot(uri=OKN.leveringsdato, name="Fakturagrunnlag_leveringsdato", curie=OKN.curie('leveringsdato'),
                   model_uri=OKN.Fakturagrunnlag_leveringsdato, domain=Fakturagrunnlag, range=Optional[Union[str, XSDDate]])

slots.Fakturagrunnlag_nettobelop = Slot(uri=OKN.nettobelop, name="Fakturagrunnlag_nettobelop", curie=OKN.curie('nettobelop'),
                   model_uri=OKN.Fakturagrunnlag_nettobelop, domain=Fakturagrunnlag, range=Optional[int])

slots.Fakturagrunnlag_avgiftsbelop = Slot(uri=OKN.avgiftsbelop, name="Fakturagrunnlag_avgiftsbelop", curie=OKN.curie('avgiftsbelop'),
                   model_uri=OKN.Fakturagrunnlag_avgiftsbelop, domain=Fakturagrunnlag, range=Optional[int])

slots.Fakturagrunnlag_totalbelop = Slot(uri=OKN.totalbelop, name="Fakturagrunnlag_totalbelop", curie=OKN.curie('totalbelop'),
                   model_uri=OKN.Fakturagrunnlag_totalbelop, domain=Fakturagrunnlag, range=Optional[int])

slots.Fakturagrunnlag_faktura = Slot(uri=OKN.faktura, name="Fakturagrunnlag_faktura", curie=OKN.curie('faktura'),
                   model_uri=OKN.Fakturagrunnlag_faktura, domain=Fakturagrunnlag, range=Optional[Union[Union[str, FakturaId], list[Union[str, FakturaId]]]])

slots.Fakturagrunnlag_fakturautsteder = Slot(uri=OKN.fakturautsteder, name="Fakturagrunnlag_fakturautsteder", curie=OKN.curie('fakturautsteder'),
                   model_uri=OKN.Fakturagrunnlag_fakturautsteder, domain=Fakturagrunnlag, range=Union[str, FakturautstederId])

slots.Fakturautsteder_navn = Slot(uri=FINT.navn, name="Fakturautsteder_navn", curie=FINT.curie('navn'),
                   model_uri=OKN.Fakturautsteder_navn, domain=Fakturautsteder, range=str)

slots.Fakturautsteder_fakturagrunnlag = Slot(uri=OKN.fakturagrunnlag, name="Fakturautsteder_fakturagrunnlag", curie=OKN.curie('fakturagrunnlag'),
                   model_uri=OKN.Fakturautsteder_fakturagrunnlag, domain=Fakturautsteder, range=Optional[Union[Union[str, FakturagrunnlagId], list[Union[str, FakturagrunnlagId]]]])

slots.Fakturautsteder_organisasjonselement = Slot(uri=OKN.organisasjonselement, name="Fakturautsteder_organisasjonselement", curie=OKN.curie('organisasjonselement'),
                   model_uri=OKN.Fakturautsteder_organisasjonselement, domain=Fakturautsteder, range=Optional[Union[str, URIorCURIE]])

slots.Fakturautsteder_vare = Slot(uri=OKN.vare, name="Fakturautsteder_vare", curie=OKN.curie('vare'),
                   model_uri=OKN.Fakturautsteder_vare, domain=Fakturautsteder, range=Optional[Union[Union[str, VareId], list[Union[str, VareId]]]])

slots.Fakturamottaker_person = Slot(uri=FINT.person, name="Fakturamottaker_person", curie=FINT.curie('person'),
                   model_uri=OKN.Fakturamottaker_person, domain=Fakturamottaker, range=Union[str, PersonId])

slots.Fakturalinje_antall = Slot(uri=OKN.antall, name="Fakturalinje_antall", curie=OKN.curie('antall'),
                   model_uri=OKN.Fakturalinje_antall, domain=Fakturalinje, range=float)

slots.Fakturalinje_pris = Slot(uri=OKN.pris, name="Fakturalinje_pris", curie=OKN.curie('pris'),
                   model_uri=OKN.Fakturalinje_pris, domain=Fakturalinje, range=int)

slots.Fakturalinje_fritekst = Slot(uri=OKN.fritekst, name="Fakturalinje_fritekst", curie=OKN.curie('fritekst'),
                   model_uri=OKN.Fakturalinje_fritekst, domain=Fakturalinje, range=Optional[Union[str, list[str]]])

slots.Fakturalinje_vare = Slot(uri=OKN.vare, name="Fakturalinje_vare", curie=OKN.curie('vare'),
                   model_uri=OKN.Fakturalinje_vare, domain=Fakturalinje, range=Union[str, VareId])

slots.Transaksjon_transaksjonsId = Slot(uri=OKN.transaksjonsId, name="Transaksjon_transaksjonsId", curie=OKN.curie('transaksjonsId'),
                   model_uri=OKN.Transaksjon_transaksjonsId, domain=Transaksjon, range=Union[dict, "Identifikator"])

slots.Transaksjon_belop = Slot(uri=OKN.belop, name="Transaksjon_belop", curie=OKN.curie('belop'),
                   model_uri=OKN.Transaksjon_belop, domain=Transaksjon, range=int)

slots.Transaksjon_forfallsdato = Slot(uri=OKN.forfallsdato, name="Transaksjon_forfallsdato", curie=OKN.curie('forfallsdato'),
                   model_uri=OKN.Transaksjon_forfallsdato, domain=Transaksjon, range=Union[str, XSDDate])

slots.Transaksjon_beskrivelse = Slot(uri=FINT.beskrivelse, name="Transaksjon_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=OKN.Transaksjon_beskrivelse, domain=Transaksjon, range=Optional[str])

slots.Transaksjon_bilag = Slot(uri=OKN.bilag, name="Transaksjon_bilag", curie=OKN.curie('bilag'),
                   model_uri=OKN.Transaksjon_bilag, domain=Transaksjon, range=Optional[Union[Union[dict, "Bilag"], list[Union[dict, "Bilag"]]]])

slots.Transaksjon_transaksjonstidspunkt = Slot(uri=OKN.transaksjonstidspunkt, name="Transaksjon_transaksjonstidspunkt", curie=OKN.curie('transaksjonstidspunkt'),
                   model_uri=OKN.Transaksjon_transaksjonstidspunkt, domain=Transaksjon, range=Optional[Union[str, XSDDateTime]])

slots.Transaksjon_oppdateringstidspunkt = Slot(uri=OKN.oppdateringstidspunkt, name="Transaksjon_oppdateringstidspunkt", curie=OKN.curie('oppdateringstidspunkt'),
                   model_uri=OKN.Transaksjon_oppdateringstidspunkt, domain=Transaksjon, range=Optional[Union[str, XSDDateTime]])

slots.Transaksjon_leverandor = Slot(uri=OKN.leverandor, name="Transaksjon_leverandor", curie=OKN.curie('leverandor'),
                   model_uri=OKN.Transaksjon_leverandor, domain=Transaksjon, range=Optional[Union[str, LeverandorId]])

slots.Transaksjon_postering = Slot(uri=OKN.postering, name="Transaksjon_postering", curie=OKN.curie('postering'),
                   model_uri=OKN.Transaksjon_postering, domain=Transaksjon, range=Union[Union[str, PosteringId], list[Union[str, PosteringId]]])

slots.Transaksjon_ansvarlig = Slot(uri=OKN.ansvarlig, name="Transaksjon_ansvarlig", curie=OKN.curie('ansvarlig'),
                   model_uri=OKN.Transaksjon_ansvarlig, domain=Transaksjon, range=Optional[Union[str, URIorCURIE]])

slots.Transaksjon_valuta = Slot(uri=OKN.valuta, name="Transaksjon_valuta", curie=OKN.curie('valuta'),
                   model_uri=OKN.Transaksjon_valuta, domain=Transaksjon, range=Union[str, OkonomiValutaId])

slots.Postering_posteringsId = Slot(uri=OKN.posteringsId, name="Postering_posteringsId", curie=OKN.curie('posteringsId'),
                   model_uri=OKN.Postering_posteringsId, domain=Postering, range=Union[dict, "Identifikator"])

slots.Postering_belop = Slot(uri=OKN.belop, name="Postering_belop", curie=OKN.curie('belop'),
                   model_uri=OKN.Postering_belop, domain=Postering, range=int)

slots.Postering_debet = Slot(uri=OKN.debet, name="Postering_debet", curie=OKN.curie('debet'),
                   model_uri=OKN.Postering_debet, domain=Postering, range=Union[bool, Bool])

slots.Postering_kontering = Slot(uri=OKN.kontering, name="Postering_kontering", curie=OKN.curie('kontering'),
                   model_uri=OKN.Postering_kontering, domain=Postering, range=Union[dict, "Kontostreng"])

slots.Postering_transaksjon = Slot(uri=OKN.transaksjon, name="Postering_transaksjon", curie=OKN.curie('transaksjon'),
                   model_uri=OKN.Postering_transaksjon, domain=Postering, range=Optional[Union[str, TransaksjonId]])

slots.Leverandor_kontonummer = Slot(uri=OKN.kontonummer, name="Leverandor_kontonummer", curie=OKN.curie('kontonummer'),
                   model_uri=OKN.Leverandor_kontonummer, domain=Leverandor, range=Optional[str])

slots.Leverandor_leverandornummer = Slot(uri=OKN.leverandornummer, name="Leverandor_leverandornummer", curie=OKN.curie('leverandornummer'),
                   model_uri=OKN.Leverandor_leverandornummer, domain=Leverandor, range=Optional[Union[dict, "Identifikator"]])

slots.Leverandor_person = Slot(uri=FINT.person, name="Leverandor_person", curie=FINT.curie('person'),
                   model_uri=OKN.Leverandor_person, domain=Leverandor, range=Optional[Union[str, PersonId]])

slots.Leverandor_leverandorgruppe = Slot(uri=OKN.leverandorgruppe, name="Leverandor_leverandorgruppe", curie=OKN.curie('leverandorgruppe'),
                   model_uri=OKN.Leverandor_leverandorgruppe, domain=Leverandor, range=Optional[Union[str, LeverandorgruppeId]])

slots.Leverandor_virksomhet = Slot(uri=OKN.virksomhet, name="Leverandor_virksomhet", curie=OKN.curie('virksomhet'),
                   model_uri=OKN.Leverandor_virksomhet, domain=Leverandor, range=Optional[Union[str, URIorCURIE]])

slots.Leverandorgruppe_navn = Slot(uri=FINT.navn, name="Leverandorgruppe_navn", curie=FINT.curie('navn'),
                   model_uri=OKN.Leverandorgruppe_navn, domain=Leverandorgruppe, range=str)

slots.Leverandorgruppe_leverandor = Slot(uri=OKN.leverandor, name="Leverandorgruppe_leverandor", curie=OKN.curie('leverandor'),
                   model_uri=OKN.Leverandorgruppe_leverandor, domain=Leverandorgruppe, range=Optional[Union[Union[str, LeverandorId], list[Union[str, LeverandorId]]]])

slots.Bilag_bilagsdato = Slot(uri=OKN.bilagsdato, name="Bilag_bilagsdato", curie=OKN.curie('bilagsdato'),
                   model_uri=OKN.Bilag_bilagsdato, domain=Bilag, range=Union[str, XSDDate])

slots.Bilag_bilagsnummer = Slot(uri=OKN.bilagsnummer, name="Bilag_bilagsnummer", curie=OKN.curie('bilagsnummer'),
                   model_uri=OKN.Bilag_bilagsnummer, domain=Bilag, range=Optional[str])

slots.Bilag_referanse = Slot(uri=OKN.referanse, name="Bilag_referanse", curie=OKN.curie('referanse'),
                   model_uri=OKN.Bilag_referanse, domain=Bilag, range=Optional[str])

slots.Bilag_url = Slot(uri=OKN.url, name="Bilag_url", curie=OKN.curie('url'),
                   model_uri=OKN.Bilag_url, domain=Bilag, range=Optional[str])

slots.Bilag_filnavn = Slot(uri=OKN.filnavn, name="Bilag_filnavn", curie=OKN.curie('filnavn'),
                   model_uri=OKN.Bilag_filnavn, domain=Bilag, range=Optional[str])

slots.Bilag_data = Slot(uri=OKN.data, name="Bilag_data", curie=OKN.curie('data'),
                   model_uri=OKN.Bilag_data, domain=Bilag, range=Optional[str])

slots.Kontostreng_art = Slot(uri=OKN.art, name="Kontostreng_art", curie=OKN.curie('art'),
                   model_uri=OKN.Kontostreng_art, domain=Kontostreng, range=Optional[str])

slots.Kontostreng_funksjon = Slot(uri=OKN.funksjon, name="Kontostreng_funksjon", curie=OKN.curie('funksjon'),
                   model_uri=OKN.Kontostreng_funksjon, domain=Kontostreng, range=Optional[str])

slots.Kontostreng_ansvar = Slot(uri=OKN.ansvar, name="Kontostreng_ansvar", curie=OKN.curie('ansvar'),
                   model_uri=OKN.Kontostreng_ansvar, domain=Kontostreng, range=Optional[str])

slots.Kontostreng_prosjekt = Slot(uri=OKN.prosjekt, name="Kontostreng_prosjekt", curie=OKN.curie('prosjekt'),
                   model_uri=OKN.Kontostreng_prosjekt, domain=Kontostreng, range=Optional[str])

slots.Vare_kode = Slot(uri=FINT.kode, name="Vare_kode", curie=FINT.curie('kode'),
                   model_uri=OKN.Vare_kode, domain=Vare, range=str)

slots.Vare_navn = Slot(uri=FINT.navn, name="Vare_navn", curie=FINT.curie('navn'),
                   model_uri=OKN.Vare_navn, domain=Vare, range=str)

slots.Vare_enhet = Slot(uri=OKN.enhet, name="Vare_enhet", curie=OKN.curie('enhet'),
                   model_uri=OKN.Vare_enhet, domain=Vare, range=str)

slots.Vare_pris = Slot(uri=OKN.pris, name="Vare_pris", curie=OKN.curie('pris'),
                   model_uri=OKN.Vare_pris, domain=Vare, range=int)

slots.Vare_kontering = Slot(uri=OKN.kontering, name="Vare_kontering", curie=OKN.curie('kontering'),
                   model_uri=OKN.Vare_kontering, domain=Vare, range=Optional[Union[dict, Kontostreng]])

slots.Vare_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Vare_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=OKN.Vare_gyldighetsperiode, domain=Vare, range=Optional[Union[dict, "Periode"]])

slots.Vare_passiv = Slot(uri=FINT.passiv, name="Vare_passiv", curie=FINT.curie('passiv'),
                   model_uri=OKN.Vare_passiv, domain=Vare, range=Optional[Union[bool, Bool]])

slots.Vare_fakturautsteder = Slot(uri=OKN.fakturautsteder, name="Vare_fakturautsteder", curie=OKN.curie('fakturautsteder'),
                   model_uri=OKN.Vare_fakturautsteder, domain=Vare, range=Union[str, FakturautstederId])

slots.Vare_merverdiavgift = Slot(uri=OKN.merverdiavgift, name="Vare_merverdiavgift", curie=OKN.curie('merverdiavgift'),
                   model_uri=OKN.Vare_merverdiavgift, domain=Vare, range=Union[str, MerverdiavgiftId])

slots.Merverdiavgift_kode = Slot(uri=FINT.kode, name="Merverdiavgift_kode", curie=FINT.curie('kode'),
                   model_uri=OKN.Merverdiavgift_kode, domain=Merverdiavgift, range=str)

slots.Merverdiavgift_navn = Slot(uri=FINT.navn, name="Merverdiavgift_navn", curie=FINT.curie('navn'),
                   model_uri=OKN.Merverdiavgift_navn, domain=Merverdiavgift, range=str)

slots.Merverdiavgift_sats = Slot(uri=OKN.sats, name="Merverdiavgift_sats", curie=OKN.curie('sats'),
                   model_uri=OKN.Merverdiavgift_sats, domain=Merverdiavgift, range=int)

slots.Merverdiavgift_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Merverdiavgift_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=OKN.Merverdiavgift_gyldighetsperiode, domain=Merverdiavgift, range=Optional[Union[dict, "Periode"]])

slots.Merverdiavgift_passiv = Slot(uri=FINT.passiv, name="Merverdiavgift_passiv", curie=FINT.curie('passiv'),
                   model_uri=OKN.Merverdiavgift_passiv, domain=Merverdiavgift, range=Optional[Union[bool, Bool]])

slots.OkonomiValuta_kode = Slot(uri=FINT.kode, name="OkonomiValuta_kode", curie=FINT.curie('kode'),
                   model_uri=OKN.OkonomiValuta_kode, domain=OkonomiValuta, range=str)

slots.OkonomiValuta_navn = Slot(uri=FINT.navn, name="OkonomiValuta_navn", curie=FINT.curie('navn'),
                   model_uri=OKN.OkonomiValuta_navn, domain=OkonomiValuta, range=str)

slots.OkonomiValuta_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="OkonomiValuta_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=OKN.OkonomiValuta_gyldighetsperiode, domain=OkonomiValuta, range=Optional[Union[dict, "Periode"]])

slots.OkonomiValuta_passiv = Slot(uri=FINT.passiv, name="OkonomiValuta_passiv", curie=FINT.curie('passiv'),
                   model_uri=OKN.OkonomiValuta_passiv, domain=OkonomiValuta, range=Optional[Union[bool, Bool]])

slots.Aktoer_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Aktoer_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=OKN.Aktoer_kontaktinformasjon, domain=Aktoer, range=Optional[Union[dict, "Kontaktinformasjon"]])

slots.Aktoer_postadresse = Slot(uri=FINT.postadresse, name="Aktoer_postadresse", curie=FINT.curie('postadresse'),
                   model_uri=OKN.Aktoer_postadresse, domain=Aktoer, range=Optional[Union[dict, "Adresse"]])

slots.Begrep_kode = Slot(uri=FINT.kode, name="Begrep_kode", curie=FINT.curie('kode'),
                   model_uri=OKN.Begrep_kode, domain=Begrep, range=str)

slots.Begrep_navn = Slot(uri=FINT.navn, name="Begrep_navn", curie=FINT.curie('navn'),
                   model_uri=OKN.Begrep_navn, domain=Begrep, range=str)

slots.Begrep_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Begrep_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=OKN.Begrep_gyldighetsperiode, domain=Begrep, range=Optional[Union[dict, "Periode"]])

slots.Begrep_passiv = Slot(uri=FINT.passiv, name="Begrep_passiv", curie=FINT.curie('passiv'),
                   model_uri=OKN.Begrep_passiv, domain=Begrep, range=Optional[Union[bool, Bool]])

slots.Elev_elevnummer = Slot(uri=FINT.elevnummer, name="Elev_elevnummer", curie=FINT.curie('elevnummer'),
                   model_uri=OKN.Elev_elevnummer, domain=Elev, range=Optional[Union[dict, "Identifikator"]])

slots.Elev_person = Slot(uri=FINT.person, name="Elev_person", curie=FINT.curie('person'),
                   model_uri=OKN.Elev_person, domain=Elev, range=Optional[Union[str, PersonId]])

slots.Enhet_forretningsadresse = Slot(uri=FINT.forretningsadresse, name="Enhet_forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=OKN.Enhet_forretningsadresse, domain=Enhet, range=Optional[Union[dict, "Adresse"]])

slots.Enhet_organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="Enhet_organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=OKN.Enhet_organisasjonsnavn, domain=Enhet, range=Optional[str])

slots.Enhet_organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="Enhet_organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=OKN.Enhet_organisasjonsnummer, domain=Enhet, range=Optional[Union[dict, "Identifikator"]])

slots.Identifikator_identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="Identifikator_identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=OKN.Identifikator_identifikatorverdi, domain=Identifikator, range=str)

slots.Periode_start = Slot(uri=FINT.start, name="Periode_start", curie=FINT.curie('start'),
                   model_uri=OKN.Periode_start, domain=Periode, range=Union[str, XSDDateTime])

slots.Personnavn_fornavn = Slot(uri=FINT.fornavn, name="Personnavn_fornavn", curie=FINT.curie('fornavn'),
                   model_uri=OKN.Personnavn_fornavn, domain=Personnavn, range=str)

slots.Personnavn_etternavn = Slot(uri=FINT.etternavn, name="Personnavn_etternavn", curie=FINT.curie('etternavn'),
                   model_uri=OKN.Personnavn_etternavn, domain=Personnavn, range=str)

slots.Fylke_kommune = Slot(uri=FINT.kommune, name="Fylke_kommune", curie=FINT.curie('kommune'),
                   model_uri=OKN.Fylke_kommune, domain=Fylke, range=Optional[Union[Union[str, KommuneId], list[Union[str, KommuneId]]]])

slots.Kommune_fylke = Slot(uri=FINT.fylke, name="Kommune_fylke", curie=FINT.curie('fylke'),
                   model_uri=OKN.Kommune_fylke, domain=Kommune, range=Union[str, FylkeId])

slots.Valuta_bokstavkode = Slot(uri=FINT.bokstavkode, name="Valuta_bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=OKN.Valuta_bokstavkode, domain=Valuta, range=Union[dict, Identifikator])

slots.Valuta_valuta_navn = Slot(uri=FINT.valutaNavn, name="Valuta_valuta_navn", curie=FINT.curie('valutaNavn'),
                   model_uri=OKN.Valuta_valuta_navn, domain=Valuta, range=str)

slots.Valuta_nummerkode = Slot(uri=FINT.nummerkode, name="Valuta_nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=OKN.Valuta_nummerkode, domain=Valuta, range=Union[dict, Identifikator])

slots.Person_fodselsnummer = Slot(uri=FINT.fodselsnummer, name="Person_fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=OKN.Person_fodselsnummer, domain=Person, range=Union[dict, Identifikator])

slots.Person_person_navn = Slot(uri=FINT.personNavn, name="Person_person_navn", curie=FINT.curie('personNavn'),
                   model_uri=OKN.Person_person_navn, domain=Person, range=Union[dict, Personnavn])

slots.Person_bilde = Slot(uri=FINT.bilde, name="Person_bilde", curie=FINT.curie('bilde'),
                   model_uri=OKN.Person_bilde, domain=Person, range=Optional[str])

slots.Person_bostedsadresse = Slot(uri=FINT.bostedsadresse, name="Person_bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=OKN.Person_bostedsadresse, domain=Person, range=Optional[Union[dict, Adresse]])

slots.Person_fodselsdato = Slot(uri=FINT.fodselsdato, name="Person_fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=OKN.Person_fodselsdato, domain=Person, range=Optional[Union[str, XSDDate]])

slots.Person_parorende = Slot(uri=FINT.parorende, name="Person_parorende", curie=FINT.curie('parorende'),
                   model_uri=OKN.Person_parorende, domain=Person, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.Person_statsborgerskap = Slot(uri=FINT.statsborgerskap, name="Person_statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=OKN.Person_statsborgerskap, domain=Person, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.Person_kommune = Slot(uri=FINT.kommune, name="Person_kommune", curie=FINT.curie('kommune'),
                   model_uri=OKN.Person_kommune, domain=Person, range=Optional[Union[str, KommuneId]])

slots.Person_kjonn = Slot(uri=FINT.kjonn, name="Person_kjonn", curie=FINT.curie('kjonn'),
                   model_uri=OKN.Person_kjonn, domain=Person, range=Optional[Union[str, KjonnId]])

slots.Person_foreldreansvar = Slot(uri=FINT.foreldreansvar, name="Person_foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=OKN.Person_foreldreansvar, domain=Person, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Person_foreldre = Slot(uri=FINT.foreldre, name="Person_foreldre", curie=FINT.curie('foreldre'),
                   model_uri=OKN.Person_foreldre, domain=Person, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Person_maalform = Slot(uri=FINT.maalform, name="Person_maalform", curie=FINT.curie('maalform'),
                   model_uri=OKN.Person_maalform, domain=Person, range=Optional[Union[str, SpraakId]])

slots.Person_morsmaal = Slot(uri=FINT.morsmaal, name="Person_morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=OKN.Person_morsmaal, domain=Person, range=Optional[Union[str, SpraakId]])

slots.Person_laerling = Slot(uri=FINT.laerling, name="Person_laerling", curie=FINT.curie('laerling'),
                   model_uri=OKN.Person_laerling, domain=Person, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Person_elev = Slot(uri=FINT.elev, name="Person_elev", curie=FINT.curie('elev'),
                   model_uri=OKN.Person_elev, domain=Person, range=Optional[Union[str, ElevId]])

slots.Person_otungdom = Slot(uri=FINT.otungdom, name="Person_otungdom", curie=FINT.curie('otungdom'),
                   model_uri=OKN.Person_otungdom, domain=Person, range=Optional[Union[str, URIorCURIE]])

slots.Kontaktperson_type = Slot(uri=FINT.type, name="Kontaktperson_type", curie=FINT.curie('type'),
                   model_uri=OKN.Kontaktperson_type, domain=Kontaktperson, range=str)

slots.Kontaktperson_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Kontaktperson_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=OKN.Kontaktperson_kontaktinformasjon, domain=Kontaktperson, range=Optional[Union[dict, Kontaktinformasjon]])

slots.Kontaktperson_kontaktperson_navn = Slot(uri=FINT.kontaktpersonNavn, name="Kontaktperson_kontaktperson_navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=OKN.Kontaktperson_kontaktperson_navn, domain=Kontaktperson, range=Optional[Union[dict, Personnavn]])

slots.Kontaktperson_kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="Kontaktperson_kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=OKN.Kontaktperson_kontaktperson, domain=Kontaktperson, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Virksomhet_virksomhetsId = Slot(uri=FINT.virksomhetsId, name="Virksomhet_virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=OKN.Virksomhet_virksomhetsId, domain=Virksomhet, range=Union[dict, Identifikator])

slots.Virksomhet_laerling = Slot(uri=FINT.laerling, name="Virksomhet_laerling", curie=FINT.curie('laerling'),
                   model_uri=OKN.Virksomhet_laerling, domain=Virksomhet, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

