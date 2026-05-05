# Auto generated from fint-administrasjon-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-05T13:27:51
# Schema: fint-administrasjon
#
# id: https://data.norge.no/linkml/fint-administrasjon
# description: FINT-domenemodell for administrasjon og HR. Dekkjer personalressursar, arbeidsforhold, fullmakter og organisasjonsstruktur.
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
ADM = CurieNamespace('adm', 'https://schema.fintlabs.no/administrasjon/')
FINT = CurieNamespace('fint', 'https://schema.fintlabs.no/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = ADM


# Types

# Class references
class LonnId(URIorCURIE):
    pass


class FastlonnId(LonnId):
    pass


class FasttilleggId(LonnId):
    pass


class VariabellonnId(LonnId):
    pass


class FravaerId(URIorCURIE):
    pass


class FullmaktId(URIorCURIE):
    pass


class RolleId(URIorCURIE):
    pass


class ArbeidslokasjonId(URIorCURIE):
    pass


class OrganisasjonselementId(URIorCURIE):
    pass


class PersonalressursId(URIorCURIE):
    pass


class ArbeidsforholdId(URIorCURIE):
    pass


class BegrepId(URIorCURIE):
    pass


class AktivitetId(BegrepId):
    pass


class AnleggId(BegrepId):
    pass


class AnsvarId(BegrepId):
    pass


class ArtId(BegrepId):
    pass


class ArbeidsforholdstypeId(BegrepId):
    pass


class DiverseId(BegrepId):
    pass


class FormaalId(BegrepId):
    pass


class FravaersgrunnId(BegrepId):
    pass


class FravaerstypeId(BegrepId):
    pass


class FunksjonId(BegrepId):
    pass


class KontraktId(BegrepId):
    pass


class LonsartId(BegrepId):
    pass


class LopenummerId(BegrepId):
    pass


class ObjektId(BegrepId):
    pass


class OrganisasjonstypeId(BegrepId):
    pass


class PersonalressurskategoriId(BegrepId):
    pass


class ProsjektId(BegrepId):
    pass


class ProsjektartId(BegrepId):
    pass


class RammeId(BegrepId):
    pass


class StillingskodeId(BegrepId):
    pass


class UketimetallId(BegrepId):
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
class AdministrasjonContainer(YAMLRoot):
    """
    Rotcontainer for FINT Administrasjon-instansar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["AdministrasjonContainer"]
    class_class_curie: ClassVar[str] = "adm:AdministrasjonContainer"
    class_name: ClassVar[str] = "AdministrasjonContainer"
    class_model_uri: ClassVar[URIRef] = ADM.AdministrasjonContainer

    personar: Optional[Union[dict[Union[str, PersonId], Union[dict, "Person"]], list[Union[dict, "Person"]]]] = empty_dict()
    kontaktpersonar: Optional[Union[dict[Union[str, KontaktpersonId], Union[dict, "Kontaktperson"]], list[Union[dict, "Kontaktperson"]]]] = empty_dict()
    virksomhetar: Optional[Union[dict[Union[str, VirksomhetId], Union[dict, "Virksomhet"]], list[Union[dict, "Virksomhet"]]]] = empty_dict()
    landkodar: Optional[Union[dict[Union[str, LandkodeId], Union[dict, "Landkode"]], list[Union[dict, "Landkode"]]]] = empty_dict()
    kjonn: Optional[Union[dict[Union[str, KjonnId], Union[dict, "Kjonn"]], list[Union[dict, "Kjonn"]]]] = empty_dict()
    fylke: Optional[Union[dict[Union[str, FylkeId], Union[dict, "Fylke"]], list[Union[dict, "Fylke"]]]] = empty_dict()
    kommunar: Optional[Union[dict[Union[str, KommuneId], Union[dict, "Kommune"]], list[Union[dict, "Kommune"]]]] = empty_dict()
    spraak: Optional[Union[dict[Union[str, SpraakId], Union[dict, "Spraak"]], list[Union[dict, "Spraak"]]]] = empty_dict()
    valuta: Optional[Union[dict[Union[str, ValutaId], Union[dict, "Valuta"]], list[Union[dict, "Valuta"]]]] = empty_dict()
    personalressursar: Optional[Union[dict[Union[str, PersonalressursId], Union[dict, "Personalressurs"]], list[Union[dict, "Personalressurs"]]]] = empty_dict()
    arbeidsforhold: Optional[Union[dict[Union[str, ArbeidsforholdId], Union[dict, "Arbeidsforhold"]], list[Union[dict, "Arbeidsforhold"]]]] = empty_dict()
    arbeidslokasjoner: Optional[Union[dict[Union[str, ArbeidslokasjonId], Union[dict, "Arbeidslokasjon"]], list[Union[dict, "Arbeidslokasjon"]]]] = empty_dict()
    fastlonn: Optional[Union[dict[Union[str, FastlonnId], Union[dict, "Fastlonn"]], list[Union[dict, "Fastlonn"]]]] = empty_dict()
    fasttillegg: Optional[Union[dict[Union[str, FasttilleggId], Union[dict, "Fasttillegg"]], list[Union[dict, "Fasttillegg"]]]] = empty_dict()
    fravaer: Optional[Union[dict[Union[str, FravaerId], Union[dict, "Fravaer"]], list[Union[dict, "Fravaer"]]]] = empty_dict()
    fullmakter: Optional[Union[dict[Union[str, FullmaktId], Union[dict, "Fullmakt"]], list[Union[dict, "Fullmakt"]]]] = empty_dict()
    organisasjonselement: Optional[Union[dict[Union[str, OrganisasjonselementId], Union[dict, "Organisasjonselement"]], list[Union[dict, "Organisasjonselement"]]]] = empty_dict()
    rollar: Optional[Union[dict[Union[str, RolleId], Union[dict, "Rolle"]], list[Union[dict, "Rolle"]]]] = empty_dict()
    variabellonn: Optional[Union[dict[Union[str, VariabellonnId], Union[dict, "Variabellonn"]], list[Union[dict, "Variabellonn"]]]] = empty_dict()
    aktivitetar: Optional[Union[dict[Union[str, AktivitetId], Union[dict, "Aktivitet"]], list[Union[dict, "Aktivitet"]]]] = empty_dict()
    anlegg: Optional[Union[dict[Union[str, AnleggId], Union[dict, "Anlegg"]], list[Union[dict, "Anlegg"]]]] = empty_dict()
    ansvar: Optional[Union[dict[Union[str, AnsvarId], Union[dict, "Ansvar"]], list[Union[dict, "Ansvar"]]]] = empty_dict()
    artar: Optional[Union[dict[Union[str, ArtId], Union[dict, "Art"]], list[Union[dict, "Art"]]]] = empty_dict()
    arbeidsforholdstypar: Optional[Union[dict[Union[str, ArbeidsforholdstypeId], Union[dict, "Arbeidsforholdstype"]], list[Union[dict, "Arbeidsforholdstype"]]]] = empty_dict()
    diverse: Optional[Union[dict[Union[str, DiverseId], Union[dict, "Diverse"]], list[Union[dict, "Diverse"]]]] = empty_dict()
    formaal: Optional[Union[dict[Union[str, FormaalId], Union[dict, "Formaal"]], list[Union[dict, "Formaal"]]]] = empty_dict()
    fravaersgrunnar: Optional[Union[dict[Union[str, FravaersgrunnId], Union[dict, "Fravaersgrunn"]], list[Union[dict, "Fravaersgrunn"]]]] = empty_dict()
    fravaerstypar: Optional[Union[dict[Union[str, FravaerstypeId], Union[dict, "Fravaerstype"]], list[Union[dict, "Fravaerstype"]]]] = empty_dict()
    funksjonar: Optional[Union[dict[Union[str, FunksjonId], Union[dict, "Funksjon"]], list[Union[dict, "Funksjon"]]]] = empty_dict()
    kontrakter: Optional[Union[dict[Union[str, KontraktId], Union[dict, "Kontrakt"]], list[Union[dict, "Kontrakt"]]]] = empty_dict()
    lonsartar: Optional[Union[dict[Union[str, LonsartId], Union[dict, "Lonsart"]], list[Union[dict, "Lonsart"]]]] = empty_dict()
    lopenummer: Optional[Union[dict[Union[str, LopenummerId], Union[dict, "Lopenummer"]], list[Union[dict, "Lopenummer"]]]] = empty_dict()
    objekt: Optional[Union[dict[Union[str, ObjektId], Union[dict, "Objekt"]], list[Union[dict, "Objekt"]]]] = empty_dict()
    organisasjonstypar: Optional[Union[dict[Union[str, OrganisasjonstypeId], Union[dict, "Organisasjonstype"]], list[Union[dict, "Organisasjonstype"]]]] = empty_dict()
    personalressurskategoriar: Optional[Union[dict[Union[str, PersonalressurskategoriId], Union[dict, "Personalressurskategori"]], list[Union[dict, "Personalressurskategori"]]]] = empty_dict()
    prosjekt: Optional[Union[dict[Union[str, ProsjektId], Union[dict, "Prosjekt"]], list[Union[dict, "Prosjekt"]]]] = empty_dict()
    prosjektartar: Optional[Union[dict[Union[str, ProsjektartId], Union[dict, "Prosjektart"]], list[Union[dict, "Prosjektart"]]]] = empty_dict()
    rammer: Optional[Union[dict[Union[str, RammeId], Union[dict, "Ramme"]], list[Union[dict, "Ramme"]]]] = empty_dict()
    stillingskoder: Optional[Union[dict[Union[str, StillingskodeId], Union[dict, "Stillingskode"]], list[Union[dict, "Stillingskode"]]]] = empty_dict()
    uketimetall: Optional[Union[dict[Union[str, UketimetallId], Union[dict, "Uketimetall"]], list[Union[dict, "Uketimetall"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="personar", slot_type=Person, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kontaktpersonar", slot_type=Kontaktperson, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="virksomhetar", slot_type=Virksomhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="landkodar", slot_type=Landkode, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kjonn", slot_type=Kjonn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fylke", slot_type=Fylke, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kommunar", slot_type=Kommune, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="spraak", slot_type=Spraak, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="valuta", slot_type=Valuta, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="personalressursar", slot_type=Personalressurs, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="arbeidsforhold", slot_type=Arbeidsforhold, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="arbeidslokasjoner", slot_type=Arbeidslokasjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fastlonn", slot_type=Fastlonn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fasttillegg", slot_type=Fasttillegg, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fravaer", slot_type=Fravaer, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fullmakter", slot_type=Fullmakt, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="organisasjonselement", slot_type=Organisasjonselement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rollar", slot_type=Rolle, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="variabellonn", slot_type=Variabellonn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aktivitetar", slot_type=Aktivitet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="anlegg", slot_type=Anlegg, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ansvar", slot_type=Ansvar, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="artar", slot_type=Art, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="arbeidsforholdstypar", slot_type=Arbeidsforholdstype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="diverse", slot_type=Diverse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="formaal", slot_type=Formaal, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fravaersgrunnar", slot_type=Fravaersgrunn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fravaerstypar", slot_type=Fravaerstype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="funksjonar", slot_type=Funksjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kontrakter", slot_type=Kontrakt, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="lonsartar", slot_type=Lonsart, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="lopenummer", slot_type=Lopenummer, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="objekt", slot_type=Objekt, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="organisasjonstypar", slot_type=Organisasjonstype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="personalressurskategoriar", slot_type=Personalressurskategori, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="prosjekt", slot_type=Prosjekt, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="prosjektartar", slot_type=Prosjektart, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rammer", slot_type=Ramme, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="stillingskoder", slot_type=Stillingskode, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="uketimetall", slot_type=Uketimetall, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Lonn(YAMLRoot):
    """
    Informasjon om lønn for eit arbeidsforhold (abstrakt base).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Lonn"]
    class_class_curie: ClassVar[str] = "adm:Lonn"
    class_name: ClassVar[str] = "Lonn"
    class_model_uri: ClassVar[URIRef] = ADM.Lonn

    id: Union[str, LonnId] = None
    beskrivelse: str = None
    kontostreng: Union[dict, "Kontostreng"] = None
    periode: Union[dict, "Periode"] = None
    anvist: Optional[Union[str, XSDDateTime]] = None
    attestert: Optional[Union[str, XSDDateTime]] = None
    kildesystemId: Optional[Union[dict, "Identifikator"]] = None
    kontert: Optional[Union[str, XSDDateTime]] = None
    opptjent: Optional[Union[dict, "Periode"]] = None
    anviser: Optional[Union[str, PersonalressursId]] = None
    konterer: Optional[Union[str, PersonalressursId]] = None
    attestant: Optional[Union[str, PersonalressursId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LonnId):
            self.id = LonnId(self.id)

        if self._is_empty(self.beskrivelse):
            self.MissingRequiredField("beskrivelse")
        if not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if self._is_empty(self.kontostreng):
            self.MissingRequiredField("kontostreng")
        if not isinstance(self.kontostreng, Kontostreng):
            self.kontostreng = Kontostreng(**as_dict(self.kontostreng))

        if self._is_empty(self.periode):
            self.MissingRequiredField("periode")
        if not isinstance(self.periode, Periode):
            self.periode = Periode(**as_dict(self.periode))

        if self.anvist is not None and not isinstance(self.anvist, XSDDateTime):
            self.anvist = XSDDateTime(self.anvist)

        if self.attestert is not None and not isinstance(self.attestert, XSDDateTime):
            self.attestert = XSDDateTime(self.attestert)

        if self.kildesystemId is not None and not isinstance(self.kildesystemId, Identifikator):
            self.kildesystemId = Identifikator(**as_dict(self.kildesystemId))

        if self.kontert is not None and not isinstance(self.kontert, XSDDateTime):
            self.kontert = XSDDateTime(self.kontert)

        if self.opptjent is not None and not isinstance(self.opptjent, Periode):
            self.opptjent = Periode(**as_dict(self.opptjent))

        if self.anviser is not None and not isinstance(self.anviser, PersonalressursId):
            self.anviser = PersonalressursId(self.anviser)

        if self.konterer is not None and not isinstance(self.konterer, PersonalressursId):
            self.konterer = PersonalressursId(self.konterer)

        if self.attestant is not None and not isinstance(self.attestant, PersonalressursId):
            self.attestant = PersonalressursId(self.attestant)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontostreng(YAMLRoot):
    """
    Sammensetning av kontodimensjonar for bokføring.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Kontostreng"]
    class_class_curie: ClassVar[str] = "adm:Kontostreng"
    class_name: ClassVar[str] = "Kontostreng"
    class_model_uri: ClassVar[URIRef] = ADM.Kontostreng

    ansvar: Union[str, AnsvarId] = None
    art: Union[str, ArtId] = None
    funksjon: Union[str, FunksjonId] = None
    aktivitet: Optional[Union[str, AktivitetId]] = None
    anlegg: Optional[Union[str, AnleggId]] = None
    diverse: Optional[Union[str, DiverseId]] = None
    formaal: Optional[Union[str, FormaalId]] = None
    kontrakt: Optional[Union[str, KontraktId]] = None
    lopenummer: Optional[Union[str, LopenummerId]] = None
    objekt: Optional[Union[str, ObjektId]] = None
    prosjekt: Optional[Union[str, ProsjektId]] = None
    prosjektart: Optional[Union[str, ProsjektartId]] = None
    ramme: Optional[Union[str, RammeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ansvar):
            self.MissingRequiredField("ansvar")
        if not isinstance(self.ansvar, AnsvarId):
            self.ansvar = AnsvarId(self.ansvar)

        if self._is_empty(self.art):
            self.MissingRequiredField("art")
        if not isinstance(self.art, ArtId):
            self.art = ArtId(self.art)

        if self._is_empty(self.funksjon):
            self.MissingRequiredField("funksjon")
        if not isinstance(self.funksjon, FunksjonId):
            self.funksjon = FunksjonId(self.funksjon)

        if self.aktivitet is not None and not isinstance(self.aktivitet, AktivitetId):
            self.aktivitet = AktivitetId(self.aktivitet)

        if self.anlegg is not None and not isinstance(self.anlegg, AnleggId):
            self.anlegg = AnleggId(self.anlegg)

        if self.diverse is not None and not isinstance(self.diverse, DiverseId):
            self.diverse = DiverseId(self.diverse)

        if self.formaal is not None and not isinstance(self.formaal, FormaalId):
            self.formaal = FormaalId(self.formaal)

        if self.kontrakt is not None and not isinstance(self.kontrakt, KontraktId):
            self.kontrakt = KontraktId(self.kontrakt)

        if self.lopenummer is not None and not isinstance(self.lopenummer, LopenummerId):
            self.lopenummer = LopenummerId(self.lopenummer)

        if self.objekt is not None and not isinstance(self.objekt, ObjektId):
            self.objekt = ObjektId(self.objekt)

        if self.prosjekt is not None and not isinstance(self.prosjekt, ProsjektId):
            self.prosjekt = ProsjektId(self.prosjekt)

        if self.prosjektart is not None and not isinstance(self.prosjektart, ProsjektartId):
            self.prosjektart = ProsjektartId(self.prosjektart)

        if self.ramme is not None and not isinstance(self.ramme, RammeId):
            self.ramme = RammeId(self.ramme)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fastlonn(Lonn):
    """
    Informasjon om fast lønnsbeordring.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Fastlonn"]
    class_class_curie: ClassVar[str] = "adm:Fastlonn"
    class_name: ClassVar[str] = "Fastlonn"
    class_model_uri: ClassVar[URIRef] = ADM.Fastlonn

    id: Union[str, FastlonnId] = None
    beskrivelse: str = None
    kontostreng: Union[dict, Kontostreng] = None
    periode: Union[dict, "Periode"] = None
    prosent: int = None
    arbeidsforhold: Union[str, ArbeidsforholdId] = None
    lonsart: Optional[Union[str, LonsartId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FastlonnId):
            self.id = FastlonnId(self.id)

        if self._is_empty(self.prosent):
            self.MissingRequiredField("prosent")
        if not isinstance(self.prosent, int):
            self.prosent = int(self.prosent)

        if self._is_empty(self.arbeidsforhold):
            self.MissingRequiredField("arbeidsforhold")
        if not isinstance(self.arbeidsforhold, ArbeidsforholdId):
            self.arbeidsforhold = ArbeidsforholdId(self.arbeidsforhold)

        if self.lonsart is not None and not isinstance(self.lonsart, LonsartId):
            self.lonsart = LonsartId(self.lonsart)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fasttillegg(Lonn):
    """
    Faste tillegg til utbetaling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Fasttillegg"]
    class_class_curie: ClassVar[str] = "adm:Fasttillegg"
    class_name: ClassVar[str] = "Fasttillegg"
    class_model_uri: ClassVar[URIRef] = ADM.Fasttillegg

    id: Union[str, FasttilleggId] = None
    beskrivelse: str = None
    kontostreng: Union[dict, Kontostreng] = None
    periode: Union[dict, "Periode"] = None
    belop: int = None
    lonsart: Union[str, LonsartId] = None
    arbeidsforhold: Union[str, ArbeidsforholdId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FasttilleggId):
            self.id = FasttilleggId(self.id)

        if self._is_empty(self.belop):
            self.MissingRequiredField("belop")
        if not isinstance(self.belop, int):
            self.belop = int(self.belop)

        if self._is_empty(self.lonsart):
            self.MissingRequiredField("lonsart")
        if not isinstance(self.lonsart, LonsartId):
            self.lonsart = LonsartId(self.lonsart)

        if self._is_empty(self.arbeidsforhold):
            self.MissingRequiredField("arbeidsforhold")
        if not isinstance(self.arbeidsforhold, ArbeidsforholdId):
            self.arbeidsforhold = ArbeidsforholdId(self.arbeidsforhold)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Variabellonn(Lonn):
    """
    Informasjon om variabel lønn.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Variabellonn"]
    class_class_curie: ClassVar[str] = "adm:Variabellonn"
    class_name: ClassVar[str] = "Variabellonn"
    class_model_uri: ClassVar[URIRef] = ADM.Variabellonn

    id: Union[str, VariabellonnId] = None
    beskrivelse: str = None
    kontostreng: Union[dict, Kontostreng] = None
    periode: Union[dict, "Periode"] = None
    antall: int = None
    lonsart: Union[str, LonsartId] = None
    arbeidsforhold: Union[str, ArbeidsforholdId] = None
    belop: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariabellonnId):
            self.id = VariabellonnId(self.id)

        if self._is_empty(self.antall):
            self.MissingRequiredField("antall")
        if not isinstance(self.antall, int):
            self.antall = int(self.antall)

        if self._is_empty(self.lonsart):
            self.MissingRequiredField("lonsart")
        if not isinstance(self.lonsart, LonsartId):
            self.lonsart = LonsartId(self.lonsart)

        if self._is_empty(self.arbeidsforhold):
            self.MissingRequiredField("arbeidsforhold")
        if not isinstance(self.arbeidsforhold, ArbeidsforholdId):
            self.arbeidsforhold = ArbeidsforholdId(self.arbeidsforhold)

        if self.belop is not None and not isinstance(self.belop, int):
            self.belop = int(self.belop)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fravaer(YAMLRoot):
    """
    Fråvær frå eit arbeidsforhold.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Fravaer"]
    class_class_curie: ClassVar[str] = "adm:Fravaer"
    class_name: ClassVar[str] = "Fravaer"
    class_model_uri: ClassVar[URIRef] = ADM.Fravaer

    id: Union[str, FravaerId] = None
    periode: Union[dict, "Periode"] = None
    prosent: int = None
    fravaerstype: Union[str, FravaerstypeId] = None
    arbeidsforhold: Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]] = None
    godkjent: Optional[Union[str, XSDDateTime]] = None
    kildesystemId: Optional[Union[dict, "Identifikator"]] = None
    fravaersgrunn: Optional[Union[str, FravaersgrunnId]] = None
    fortsettelse: Optional[Union[str, FravaerId]] = None
    fortsetter: Optional[Union[str, FravaerId]] = None
    godkjenner: Optional[Union[str, PersonalressursId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FravaerId):
            self.id = FravaerId(self.id)

        if self._is_empty(self.periode):
            self.MissingRequiredField("periode")
        if not isinstance(self.periode, Periode):
            self.periode = Periode(**as_dict(self.periode))

        if self._is_empty(self.prosent):
            self.MissingRequiredField("prosent")
        if not isinstance(self.prosent, int):
            self.prosent = int(self.prosent)

        if self._is_empty(self.fravaerstype):
            self.MissingRequiredField("fravaerstype")
        if not isinstance(self.fravaerstype, FravaerstypeId):
            self.fravaerstype = FravaerstypeId(self.fravaerstype)

        if self._is_empty(self.arbeidsforhold):
            self.MissingRequiredField("arbeidsforhold")
        if not isinstance(self.arbeidsforhold, list):
            self.arbeidsforhold = [self.arbeidsforhold] if self.arbeidsforhold is not None else []
        self.arbeidsforhold = [v if isinstance(v, ArbeidsforholdId) else ArbeidsforholdId(v) for v in self.arbeidsforhold]

        if self.godkjent is not None and not isinstance(self.godkjent, XSDDateTime):
            self.godkjent = XSDDateTime(self.godkjent)

        if self.kildesystemId is not None and not isinstance(self.kildesystemId, Identifikator):
            self.kildesystemId = Identifikator(**as_dict(self.kildesystemId))

        if self.fravaersgrunn is not None and not isinstance(self.fravaersgrunn, FravaersgrunnId):
            self.fravaersgrunn = FravaersgrunnId(self.fravaersgrunn)

        if self.fortsettelse is not None and not isinstance(self.fortsettelse, FravaerId):
            self.fortsettelse = FravaerId(self.fortsettelse)

        if self.fortsetter is not None and not isinstance(self.fortsetter, FravaerId):
            self.fortsetter = FravaerId(self.fortsetter)

        if self.godkjenner is not None and not isinstance(self.godkjenner, PersonalressursId):
            self.godkjenner = PersonalressursId(self.godkjenner)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fullmakt(YAMLRoot):
    """
    Fullmakt til å gjere handlingar i høve til ei gjeven Rolle.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Fullmakt"]
    class_class_curie: ClassVar[str] = "adm:Fullmakt"
    class_name: ClassVar[str] = "Fullmakt"
    class_model_uri: ClassVar[URIRef] = ADM.Fullmakt

    id: Union[str, FullmaktId] = None
    gyldighetsperiode: Union[dict, "Periode"] = None
    rolle: Union[str, RolleId] = None
    ramme: Optional[Union[str, RammeId]] = None
    funksjon: Optional[Union[str, FunksjonId]] = None
    objekt: Optional[Union[str, ObjektId]] = None
    organisasjonselement: Optional[Union[str, OrganisasjonselementId]] = None
    art: Optional[Union[str, ArtId]] = None
    anlegg: Optional[Union[str, AnleggId]] = None
    diverse: Optional[Union[str, DiverseId]] = None
    aktivitet: Optional[Union[str, AktivitetId]] = None
    ansvar: Optional[Union[str, AnsvarId]] = None
    stedfortreder: Optional[Union[str, PersonalressursId]] = None
    kontrakt: Optional[Union[str, KontraktId]] = None
    fullmektig: Optional[Union[str, PersonalressursId]] = None
    prosjekt: Optional[Union[str, ProsjektId]] = None
    formaal: Optional[Union[str, FormaalId]] = None
    lopenummer: Optional[Union[str, LopenummerId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FullmaktId):
            self.id = FullmaktId(self.id)

        if self._is_empty(self.gyldighetsperiode):
            self.MissingRequiredField("gyldighetsperiode")
        if not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self._is_empty(self.rolle):
            self.MissingRequiredField("rolle")
        if not isinstance(self.rolle, RolleId):
            self.rolle = RolleId(self.rolle)

        if self.ramme is not None and not isinstance(self.ramme, RammeId):
            self.ramme = RammeId(self.ramme)

        if self.funksjon is not None and not isinstance(self.funksjon, FunksjonId):
            self.funksjon = FunksjonId(self.funksjon)

        if self.objekt is not None and not isinstance(self.objekt, ObjektId):
            self.objekt = ObjektId(self.objekt)

        if self.organisasjonselement is not None and not isinstance(self.organisasjonselement, OrganisasjonselementId):
            self.organisasjonselement = OrganisasjonselementId(self.organisasjonselement)

        if self.art is not None and not isinstance(self.art, ArtId):
            self.art = ArtId(self.art)

        if self.anlegg is not None and not isinstance(self.anlegg, AnleggId):
            self.anlegg = AnleggId(self.anlegg)

        if self.diverse is not None and not isinstance(self.diverse, DiverseId):
            self.diverse = DiverseId(self.diverse)

        if self.aktivitet is not None and not isinstance(self.aktivitet, AktivitetId):
            self.aktivitet = AktivitetId(self.aktivitet)

        if self.ansvar is not None and not isinstance(self.ansvar, AnsvarId):
            self.ansvar = AnsvarId(self.ansvar)

        if self.stedfortreder is not None and not isinstance(self.stedfortreder, PersonalressursId):
            self.stedfortreder = PersonalressursId(self.stedfortreder)

        if self.kontrakt is not None and not isinstance(self.kontrakt, KontraktId):
            self.kontrakt = KontraktId(self.kontrakt)

        if self.fullmektig is not None and not isinstance(self.fullmektig, PersonalressursId):
            self.fullmektig = PersonalressursId(self.fullmektig)

        if self.prosjekt is not None and not isinstance(self.prosjekt, ProsjektId):
            self.prosjekt = ProsjektId(self.prosjekt)

        if self.formaal is not None and not isinstance(self.formaal, FormaalId):
            self.formaal = FormaalId(self.formaal)

        if self.lopenummer is not None and not isinstance(self.lopenummer, LopenummerId):
            self.lopenummer = LopenummerId(self.lopenummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rolle(YAMLRoot):
    """
    Rettighet eller type fullmakt.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Rolle"]
    class_class_curie: ClassVar[str] = "adm:Rolle"
    class_name: ClassVar[str] = "Rolle"
    class_model_uri: ClassVar[URIRef] = ADM.Rolle

    id: Union[str, RolleId] = None
    rolleNavn: Union[dict, "Identifikator"] = None
    beskrivelse: str = None
    fullmakt: Union[Union[str, FullmaktId], list[Union[str, FullmaktId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RolleId):
            self.id = RolleId(self.id)

        if self._is_empty(self.rolleNavn):
            self.MissingRequiredField("rolleNavn")
        if not isinstance(self.rolleNavn, Identifikator):
            self.rolleNavn = Identifikator(**as_dict(self.rolleNavn))

        if self._is_empty(self.beskrivelse):
            self.MissingRequiredField("beskrivelse")
        if not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if self._is_empty(self.fullmakt):
            self.MissingRequiredField("fullmakt")
        if not isinstance(self.fullmakt, list):
            self.fullmakt = [self.fullmakt] if self.fullmakt is not None else []
        self.fullmakt = [v if isinstance(v, FullmaktId) else FullmaktId(v) for v in self.fullmakt]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Arbeidslokasjon(YAMLRoot):
    """
    Fysisk lokasjon der ein tilsett har sitt arbeidsstad.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Arbeidslokasjon"]
    class_class_curie: ClassVar[str] = "adm:Arbeidslokasjon"
    class_name: ClassVar[str] = "Arbeidslokasjon"
    class_model_uri: ClassVar[URIRef] = ADM.Arbeidslokasjon

    id: Union[str, ArbeidslokasjonId] = None
    lokasjonskode: Union[dict, "Identifikator"] = None
    lokasjonsnavn: Optional[str] = None
    forretningsadresse: Optional[Union[dict, "Adresse"]] = None
    organisasjonsnavn: Optional[str] = None
    organisasjonsnummer: Optional[Union[dict, "Identifikator"]] = None
    kontaktinformasjon: Optional[Union[dict, "Kontaktinformasjon"]] = None
    postadresse: Optional[Union[dict, "Adresse"]] = None
    arbeidsforhold: Optional[Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArbeidslokasjonId):
            self.id = ArbeidslokasjonId(self.id)

        if self._is_empty(self.lokasjonskode):
            self.MissingRequiredField("lokasjonskode")
        if not isinstance(self.lokasjonskode, Identifikator):
            self.lokasjonskode = Identifikator(**as_dict(self.lokasjonskode))

        if self.lokasjonsnavn is not None and not isinstance(self.lokasjonsnavn, str):
            self.lokasjonsnavn = str(self.lokasjonsnavn)

        if self.forretningsadresse is not None and not isinstance(self.forretningsadresse, Adresse):
            self.forretningsadresse = Adresse(**as_dict(self.forretningsadresse))

        if self.organisasjonsnavn is not None and not isinstance(self.organisasjonsnavn, str):
            self.organisasjonsnavn = str(self.organisasjonsnavn)

        if self.organisasjonsnummer is not None and not isinstance(self.organisasjonsnummer, Identifikator):
            self.organisasjonsnummer = Identifikator(**as_dict(self.organisasjonsnummer))

        if self.kontaktinformasjon is not None and not isinstance(self.kontaktinformasjon, Kontaktinformasjon):
            self.kontaktinformasjon = Kontaktinformasjon(**as_dict(self.kontaktinformasjon))

        if self.postadresse is not None and not isinstance(self.postadresse, Adresse):
            self.postadresse = Adresse(**as_dict(self.postadresse))

        if not isinstance(self.arbeidsforhold, list):
            self.arbeidsforhold = [self.arbeidsforhold] if self.arbeidsforhold is not None else []
        self.arbeidsforhold = [v if isinstance(v, ArbeidsforholdId) else ArbeidsforholdId(v) for v in self.arbeidsforhold]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organisasjonselement(YAMLRoot):
    """
    Eit element i organisasjonsstrukturen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Organisasjonselement"]
    class_class_curie: ClassVar[str] = "adm:Organisasjonselement"
    class_name: ClassVar[str] = "Organisasjonselement"
    class_model_uri: ClassVar[URIRef] = ADM.Organisasjonselement

    id: Union[str, OrganisasjonselementId] = None
    organisasjonsId: Union[dict, "Identifikator"] = None
    organisasjonsKode: Union[dict, "Identifikator"] = None
    overordnet: Union[str, OrganisasjonselementId] = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    kortnavn: Optional[str] = None
    navn: Optional[str] = None
    forretningsadresse: Optional[Union[dict, "Adresse"]] = None
    organisasjonsnavn: Optional[str] = None
    organisasjonsnummer: Optional[Union[dict, "Identifikator"]] = None
    kontaktinformasjon: Optional[Union[dict, "Kontaktinformasjon"]] = None
    postadresse: Optional[Union[dict, "Adresse"]] = None
    ansvar: Optional[Union[Union[str, AnsvarId], list[Union[str, AnsvarId]]]] = empty_list()
    organisasjonstype: Optional[Union[str, OrganisasjonstypeId]] = None
    leder: Optional[Union[str, PersonalressursId]] = None
    underordnet: Optional[Union[Union[str, OrganisasjonselementId], list[Union[str, OrganisasjonselementId]]]] = empty_list()
    skole: Optional[Union[str, URIorCURIE]] = None
    arbeidsforhold: Optional[Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganisasjonselementId):
            self.id = OrganisasjonselementId(self.id)

        if self._is_empty(self.organisasjonsId):
            self.MissingRequiredField("organisasjonsId")
        if not isinstance(self.organisasjonsId, Identifikator):
            self.organisasjonsId = Identifikator(**as_dict(self.organisasjonsId))

        if self._is_empty(self.organisasjonsKode):
            self.MissingRequiredField("organisasjonsKode")
        if not isinstance(self.organisasjonsKode, Identifikator):
            self.organisasjonsKode = Identifikator(**as_dict(self.organisasjonsKode))

        if self._is_empty(self.overordnet):
            self.MissingRequiredField("overordnet")
        if not isinstance(self.overordnet, OrganisasjonselementId):
            self.overordnet = OrganisasjonselementId(self.overordnet)

        if self.gyldighetsperiode is not None and not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self.kortnavn is not None and not isinstance(self.kortnavn, str):
            self.kortnavn = str(self.kortnavn)

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.forretningsadresse is not None and not isinstance(self.forretningsadresse, Adresse):
            self.forretningsadresse = Adresse(**as_dict(self.forretningsadresse))

        if self.organisasjonsnavn is not None and not isinstance(self.organisasjonsnavn, str):
            self.organisasjonsnavn = str(self.organisasjonsnavn)

        if self.organisasjonsnummer is not None and not isinstance(self.organisasjonsnummer, Identifikator):
            self.organisasjonsnummer = Identifikator(**as_dict(self.organisasjonsnummer))

        if self.kontaktinformasjon is not None and not isinstance(self.kontaktinformasjon, Kontaktinformasjon):
            self.kontaktinformasjon = Kontaktinformasjon(**as_dict(self.kontaktinformasjon))

        if self.postadresse is not None and not isinstance(self.postadresse, Adresse):
            self.postadresse = Adresse(**as_dict(self.postadresse))

        if not isinstance(self.ansvar, list):
            self.ansvar = [self.ansvar] if self.ansvar is not None else []
        self.ansvar = [v if isinstance(v, AnsvarId) else AnsvarId(v) for v in self.ansvar]

        if self.organisasjonstype is not None and not isinstance(self.organisasjonstype, OrganisasjonstypeId):
            self.organisasjonstype = OrganisasjonstypeId(self.organisasjonstype)

        if self.leder is not None and not isinstance(self.leder, PersonalressursId):
            self.leder = PersonalressursId(self.leder)

        if not isinstance(self.underordnet, list):
            self.underordnet = [self.underordnet] if self.underordnet is not None else []
        self.underordnet = [v if isinstance(v, OrganisasjonselementId) else OrganisasjonselementId(v) for v in self.underordnet]

        if self.skole is not None and not isinstance(self.skole, URIorCURIE):
            self.skole = URIorCURIE(self.skole)

        if not isinstance(self.arbeidsforhold, list):
            self.arbeidsforhold = [self.arbeidsforhold] if self.arbeidsforhold is not None else []
        self.arbeidsforhold = [v if isinstance(v, ArbeidsforholdId) else ArbeidsforholdId(v) for v in self.arbeidsforhold]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Personalressurs(YAMLRoot):
    """
    Arbeidstakar eller oppdragstakar i organisasjonen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Personalressurs"]
    class_class_curie: ClassVar[str] = "adm:Personalressurs"
    class_name: ClassVar[str] = "Personalressurs"
    class_model_uri: ClassVar[URIRef] = ADM.Personalressurs

    id: Union[str, PersonalressursId] = None
    ansattnummer: Union[dict, "Identifikator"] = None
    ansettelsesperiode: Union[dict, "Periode"] = None
    person: Union[str, PersonId] = None
    personalressurskategori: Union[str, PersonalressurskategoriId] = None
    ansiennitet: Optional[Union[str, XSDDate]] = None
    brukernavn: Optional[Union[dict, "Identifikator"]] = None
    jobbtittel: Optional[str] = None
    kontaktinformasjon: Optional[Union[dict, "Kontaktinformasjon"]] = None
    stedfortreder: Optional[Union[Union[str, FullmaktId], list[Union[str, FullmaktId]]]] = empty_list()
    fullmakt: Optional[Union[Union[str, FullmaktId], list[Union[str, FullmaktId]]]] = empty_list()
    lederFor: Optional[Union[Union[str, OrganisasjonselementId], list[Union[str, OrganisasjonselementId]]]] = empty_list()
    arbeidsforhold: Optional[Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]]] = empty_list()
    personalansvar: Optional[Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]]] = empty_list()
    skoleressurs: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonalressursId):
            self.id = PersonalressursId(self.id)

        if self._is_empty(self.ansattnummer):
            self.MissingRequiredField("ansattnummer")
        if not isinstance(self.ansattnummer, Identifikator):
            self.ansattnummer = Identifikator(**as_dict(self.ansattnummer))

        if self._is_empty(self.ansettelsesperiode):
            self.MissingRequiredField("ansettelsesperiode")
        if not isinstance(self.ansettelsesperiode, Periode):
            self.ansettelsesperiode = Periode(**as_dict(self.ansettelsesperiode))

        if self._is_empty(self.person):
            self.MissingRequiredField("person")
        if not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

        if self._is_empty(self.personalressurskategori):
            self.MissingRequiredField("personalressurskategori")
        if not isinstance(self.personalressurskategori, PersonalressurskategoriId):
            self.personalressurskategori = PersonalressurskategoriId(self.personalressurskategori)

        if self.ansiennitet is not None and not isinstance(self.ansiennitet, XSDDate):
            self.ansiennitet = XSDDate(self.ansiennitet)

        if self.brukernavn is not None and not isinstance(self.brukernavn, Identifikator):
            self.brukernavn = Identifikator(**as_dict(self.brukernavn))

        if self.jobbtittel is not None and not isinstance(self.jobbtittel, str):
            self.jobbtittel = str(self.jobbtittel)

        if self.kontaktinformasjon is not None and not isinstance(self.kontaktinformasjon, Kontaktinformasjon):
            self.kontaktinformasjon = Kontaktinformasjon(**as_dict(self.kontaktinformasjon))

        if not isinstance(self.stedfortreder, list):
            self.stedfortreder = [self.stedfortreder] if self.stedfortreder is not None else []
        self.stedfortreder = [v if isinstance(v, FullmaktId) else FullmaktId(v) for v in self.stedfortreder]

        if not isinstance(self.fullmakt, list):
            self.fullmakt = [self.fullmakt] if self.fullmakt is not None else []
        self.fullmakt = [v if isinstance(v, FullmaktId) else FullmaktId(v) for v in self.fullmakt]

        if not isinstance(self.lederFor, list):
            self.lederFor = [self.lederFor] if self.lederFor is not None else []
        self.lederFor = [v if isinstance(v, OrganisasjonselementId) else OrganisasjonselementId(v) for v in self.lederFor]

        if not isinstance(self.arbeidsforhold, list):
            self.arbeidsforhold = [self.arbeidsforhold] if self.arbeidsforhold is not None else []
        self.arbeidsforhold = [v if isinstance(v, ArbeidsforholdId) else ArbeidsforholdId(v) for v in self.arbeidsforhold]

        if not isinstance(self.personalansvar, list):
            self.personalansvar = [self.personalansvar] if self.personalansvar is not None else []
        self.personalansvar = [v if isinstance(v, ArbeidsforholdId) else ArbeidsforholdId(v) for v in self.personalansvar]

        if self.skoleressurs is not None and not isinstance(self.skoleressurs, URIorCURIE):
            self.skoleressurs = URIorCURIE(self.skoleressurs)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Arbeidsforhold(YAMLRoot):
    """
    Eit avtaleforhold mellom personalressurs og arbeidsgjevar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Arbeidsforhold"]
    class_class_curie: ClassVar[str] = "adm:Arbeidsforhold"
    class_name: ClassVar[str] = "Arbeidsforhold"
    class_model_uri: ClassVar[URIRef] = ADM.Arbeidsforhold

    id: Union[str, ArbeidsforholdId] = None
    ansettelsesprosent: int = None
    aarslonn: int = None
    gyldighetsperiode: Union[dict, "Periode"] = None
    hovedstilling: Union[bool, Bool] = None
    lonnsprosent: int = None
    stillingsnummer: str = None
    tilstedeprosent: int = None
    arbeidssted: Union[str, OrganisasjonselementId] = None
    personalressurs: Union[str, PersonalressursId] = None
    arbeidsforholdsperiode: Optional[Union[dict, "Periode"]] = None
    stillingstittel: Optional[str] = None
    aktivitet: Optional[Union[str, AktivitetId]] = None
    anlegg: Optional[Union[str, AnleggId]] = None
    ansvar: Optional[Union[str, AnsvarId]] = None
    arbeidsforholdstype: Optional[Union[str, ArbeidsforholdstypeId]] = None
    art: Optional[Union[str, ArtId]] = None
    diverse: Optional[Union[str, DiverseId]] = None
    formaal: Optional[Union[str, FormaalId]] = None
    funksjon: Optional[Union[str, FunksjonId]] = None
    kontrakt: Optional[Union[str, KontraktId]] = None
    lopenummer: Optional[Union[str, LopenummerId]] = None
    objekt: Optional[Union[str, ObjektId]] = None
    prosjekt: Optional[Union[str, ProsjektId]] = None
    ramme: Optional[Union[str, RammeId]] = None
    stillingskode: Optional[Union[str, StillingskodeId]] = None
    timerPerUke: Optional[Union[str, UketimetallId]] = None
    arbeidslokasjon: Optional[Union[str, ArbeidslokasjonId]] = None
    fastlonn: Optional[Union[Union[str, FastlonnId], list[Union[str, FastlonnId]]]] = empty_list()
    fasttillegg: Optional[Union[Union[str, FasttilleggId], list[Union[str, FasttilleggId]]]] = empty_list()
    fravaer: Optional[Union[Union[str, FravaerId], list[Union[str, FravaerId]]]] = empty_list()
    variabellonn: Optional[Union[Union[str, VariabellonnId], list[Union[str, VariabellonnId]]]] = empty_list()
    personalleder: Optional[Union[str, PersonalressursId]] = None
    undervisningsforhold: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArbeidsforholdId):
            self.id = ArbeidsforholdId(self.id)

        if self._is_empty(self.ansettelsesprosent):
            self.MissingRequiredField("ansettelsesprosent")
        if not isinstance(self.ansettelsesprosent, int):
            self.ansettelsesprosent = int(self.ansettelsesprosent)

        if self._is_empty(self.aarslonn):
            self.MissingRequiredField("aarslonn")
        if not isinstance(self.aarslonn, int):
            self.aarslonn = int(self.aarslonn)

        if self._is_empty(self.gyldighetsperiode):
            self.MissingRequiredField("gyldighetsperiode")
        if not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self._is_empty(self.hovedstilling):
            self.MissingRequiredField("hovedstilling")
        if not isinstance(self.hovedstilling, Bool):
            self.hovedstilling = Bool(self.hovedstilling)

        if self._is_empty(self.lonnsprosent):
            self.MissingRequiredField("lonnsprosent")
        if not isinstance(self.lonnsprosent, int):
            self.lonnsprosent = int(self.lonnsprosent)

        if self._is_empty(self.stillingsnummer):
            self.MissingRequiredField("stillingsnummer")
        if not isinstance(self.stillingsnummer, str):
            self.stillingsnummer = str(self.stillingsnummer)

        if self._is_empty(self.tilstedeprosent):
            self.MissingRequiredField("tilstedeprosent")
        if not isinstance(self.tilstedeprosent, int):
            self.tilstedeprosent = int(self.tilstedeprosent)

        if self._is_empty(self.arbeidssted):
            self.MissingRequiredField("arbeidssted")
        if not isinstance(self.arbeidssted, OrganisasjonselementId):
            self.arbeidssted = OrganisasjonselementId(self.arbeidssted)

        if self._is_empty(self.personalressurs):
            self.MissingRequiredField("personalressurs")
        if not isinstance(self.personalressurs, PersonalressursId):
            self.personalressurs = PersonalressursId(self.personalressurs)

        if self.arbeidsforholdsperiode is not None and not isinstance(self.arbeidsforholdsperiode, Periode):
            self.arbeidsforholdsperiode = Periode(**as_dict(self.arbeidsforholdsperiode))

        if self.stillingstittel is not None and not isinstance(self.stillingstittel, str):
            self.stillingstittel = str(self.stillingstittel)

        if self.aktivitet is not None and not isinstance(self.aktivitet, AktivitetId):
            self.aktivitet = AktivitetId(self.aktivitet)

        if self.anlegg is not None and not isinstance(self.anlegg, AnleggId):
            self.anlegg = AnleggId(self.anlegg)

        if self.ansvar is not None and not isinstance(self.ansvar, AnsvarId):
            self.ansvar = AnsvarId(self.ansvar)

        if self.arbeidsforholdstype is not None and not isinstance(self.arbeidsforholdstype, ArbeidsforholdstypeId):
            self.arbeidsforholdstype = ArbeidsforholdstypeId(self.arbeidsforholdstype)

        if self.art is not None and not isinstance(self.art, ArtId):
            self.art = ArtId(self.art)

        if self.diverse is not None and not isinstance(self.diverse, DiverseId):
            self.diverse = DiverseId(self.diverse)

        if self.formaal is not None and not isinstance(self.formaal, FormaalId):
            self.formaal = FormaalId(self.formaal)

        if self.funksjon is not None and not isinstance(self.funksjon, FunksjonId):
            self.funksjon = FunksjonId(self.funksjon)

        if self.kontrakt is not None and not isinstance(self.kontrakt, KontraktId):
            self.kontrakt = KontraktId(self.kontrakt)

        if self.lopenummer is not None and not isinstance(self.lopenummer, LopenummerId):
            self.lopenummer = LopenummerId(self.lopenummer)

        if self.objekt is not None and not isinstance(self.objekt, ObjektId):
            self.objekt = ObjektId(self.objekt)

        if self.prosjekt is not None and not isinstance(self.prosjekt, ProsjektId):
            self.prosjekt = ProsjektId(self.prosjekt)

        if self.ramme is not None and not isinstance(self.ramme, RammeId):
            self.ramme = RammeId(self.ramme)

        if self.stillingskode is not None and not isinstance(self.stillingskode, StillingskodeId):
            self.stillingskode = StillingskodeId(self.stillingskode)

        if self.timerPerUke is not None and not isinstance(self.timerPerUke, UketimetallId):
            self.timerPerUke = UketimetallId(self.timerPerUke)

        if self.arbeidslokasjon is not None and not isinstance(self.arbeidslokasjon, ArbeidslokasjonId):
            self.arbeidslokasjon = ArbeidslokasjonId(self.arbeidslokasjon)

        if not isinstance(self.fastlonn, list):
            self.fastlonn = [self.fastlonn] if self.fastlonn is not None else []
        self.fastlonn = [v if isinstance(v, FastlonnId) else FastlonnId(v) for v in self.fastlonn]

        if not isinstance(self.fasttillegg, list):
            self.fasttillegg = [self.fasttillegg] if self.fasttillegg is not None else []
        self.fasttillegg = [v if isinstance(v, FasttilleggId) else FasttilleggId(v) for v in self.fasttillegg]

        if not isinstance(self.fravaer, list):
            self.fravaer = [self.fravaer] if self.fravaer is not None else []
        self.fravaer = [v if isinstance(v, FravaerId) else FravaerId(v) for v in self.fravaer]

        if not isinstance(self.variabellonn, list):
            self.variabellonn = [self.variabellonn] if self.variabellonn is not None else []
        self.variabellonn = [v if isinstance(v, VariabellonnId) else VariabellonnId(v) for v in self.variabellonn]

        if self.personalleder is not None and not isinstance(self.personalleder, PersonalressursId):
            self.personalleder = PersonalressursId(self.personalleder)

        if self.undervisningsforhold is not None and not isinstance(self.undervisningsforhold, URIorCURIE):
            self.undervisningsforhold = URIorCURIE(self.undervisningsforhold)

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
    class_model_uri: ClassVar[URIRef] = ADM.Aktoer

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
    class_model_uri: ClassVar[URIRef] = ADM.Begrep

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
class Aktivitet(Begrep):
    """
    Del av kontostrengen og detaljering av funksjon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Aktivitet"]
    class_class_curie: ClassVar[str] = "adm:Aktivitet"
    class_name: ClassVar[str] = "Aktivitet"
    class_model_uri: ClassVar[URIRef] = ADM.Aktivitet

    id: Union[str, AktivitetId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AktivitetId):
            self.id = AktivitetId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Anlegg(Begrep):
    """
    Del av kontostrengen; objekt som skal aktiverast eller avskrivast.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Anlegg"]
    class_class_curie: ClassVar[str] = "adm:Anlegg"
    class_name: ClassVar[str] = "Anlegg"
    class_model_uri: ClassVar[URIRef] = ADM.Anlegg

    id: Union[str, AnleggId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnleggId):
            self.id = AnleggId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ansvar(Begrep):
    """
    Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller inntekt.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Ansvar"]
    class_class_curie: ClassVar[str] = "adm:Ansvar"
    class_name: ClassVar[str] = "Ansvar"
    class_model_uri: ClassVar[URIRef] = ADM.Ansvar

    id: Union[str, AnsvarId] = None
    kode: str = None
    navn: str = None
    overordnet: Optional[Union[str, AnsvarId]] = None
    underordnet: Optional[Union[Union[str, AnsvarId], list[Union[str, AnsvarId]]]] = empty_list()
    organisasjonselement: Optional[Union[Union[str, OrganisasjonselementId], list[Union[str, OrganisasjonselementId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnsvarId):
            self.id = AnsvarId(self.id)

        if self.overordnet is not None and not isinstance(self.overordnet, AnsvarId):
            self.overordnet = AnsvarId(self.overordnet)

        if not isinstance(self.underordnet, list):
            self.underordnet = [self.underordnet] if self.underordnet is not None else []
        self.underordnet = [v if isinstance(v, AnsvarId) else AnsvarId(v) for v in self.underordnet]

        if not isinstance(self.organisasjonselement, list):
            self.organisasjonselement = [self.organisasjonselement] if self.organisasjonselement is not None else []
        self.organisasjonselement = [v if isinstance(v, OrganisasjonselementId) else OrganisasjonselementId(v) for v in self.organisasjonselement]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Art(Begrep):
    """
    Del av kontostrengen som beskriv kva slags inntekter og utgifter det gjeld.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Art"]
    class_class_curie: ClassVar[str] = "adm:Art"
    class_name: ClassVar[str] = "Art"
    class_model_uri: ClassVar[URIRef] = ADM.Art

    id: Union[str, ArtId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArtId):
            self.id = ArtId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Arbeidsforholdstype(Begrep):
    """
    Viser kva behov hos arbeidsgjevar arbeidsforholdet dekkjer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Arbeidsforholdstype"]
    class_class_curie: ClassVar[str] = "adm:Arbeidsforholdstype"
    class_name: ClassVar[str] = "Arbeidsforholdstype"
    class_model_uri: ClassVar[URIRef] = ADM.Arbeidsforholdstype

    id: Union[str, ArbeidsforholdstypeId] = None
    kode: str = None
    navn: str = None
    forelder: Optional[Union[str, ArbeidsforholdstypeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArbeidsforholdstypeId):
            self.id = ArbeidsforholdstypeId(self.id)

        if self.forelder is not None and not isinstance(self.forelder, ArbeidsforholdstypeId):
            self.forelder = ArbeidsforholdstypeId(self.forelder)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Diverse(Begrep):
    """
    Del av kontostrengen; supplement til øvrige dimensjonar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Diverse"]
    class_class_curie: ClassVar[str] = "adm:Diverse"
    class_name: ClassVar[str] = "Diverse"
    class_model_uri: ClassVar[URIRef] = ADM.Diverse

    id: Union[str, DiverseId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiverseId):
            self.id = DiverseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Formaal(Begrep):
    """
    Del av kontostrengen som detaljerer inntekter og utgifter ved drift.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Formaal"]
    class_class_curie: ClassVar[str] = "adm:Formaal"
    class_name: ClassVar[str] = "Formaal"
    class_model_uri: ClassVar[URIRef] = ADM.Formaal

    id: Union[str, FormaalId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FormaalId):
            self.id = FormaalId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fravaersgrunn(Begrep):
    """
    Grunn til fråvær.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Fravaersgrunn"]
    class_class_curie: ClassVar[str] = "adm:Fravaersgrunn"
    class_name: ClassVar[str] = "Fravaersgrunn"
    class_model_uri: ClassVar[URIRef] = ADM.Fravaersgrunn

    id: Union[str, FravaersgrunnId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FravaersgrunnId):
            self.id = FravaersgrunnId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fravaerstype(Begrep):
    """
    Type fråvær.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Fravaerstype"]
    class_class_curie: ClassVar[str] = "adm:Fravaerstype"
    class_name: ClassVar[str] = "Fravaerstype"
    class_model_uri: ClassVar[URIRef] = ADM.Fravaerstype

    id: Union[str, FravaerstypeId] = None
    kode: str = None
    navn: str = None
    overfores: Optional[Union[bool, Bool]] = None
    lonsart: Optional[Union[str, LonsartId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FravaerstypeId):
            self.id = FravaerstypeId(self.id)

        if self.overfores is not None and not isinstance(self.overfores, Bool):
            self.overfores = Bool(self.overfores)

        if self.lonsart is not None and not isinstance(self.lonsart, LonsartId):
            self.lonsart = LonsartId(self.lonsart)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Funksjon(Begrep):
    """
    Del av kontostrengen som beskriv kva som vert produsert.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Funksjon"]
    class_class_curie: ClassVar[str] = "adm:Funksjon"
    class_name: ClassVar[str] = "Funksjon"
    class_model_uri: ClassVar[URIRef] = ADM.Funksjon

    id: Union[str, FunksjonId] = None
    kode: str = None
    navn: str = None
    overordnet: Optional[Union[str, FunksjonId]] = None
    underordnet: Optional[Union[Union[str, FunksjonId], list[Union[str, FunksjonId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FunksjonId):
            self.id = FunksjonId(self.id)

        if self.overordnet is not None and not isinstance(self.overordnet, FunksjonId):
            self.overordnet = FunksjonId(self.overordnet)

        if not isinstance(self.underordnet, list):
            self.underordnet = [self.underordnet] if self.underordnet is not None else []
        self.underordnet = [v if isinstance(v, FunksjonId) else FunksjonId(v) for v in self.underordnet]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontrakt(Begrep):
    """
    Kontrakt transaksjonen er knytt til.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Kontrakt"]
    class_class_curie: ClassVar[str] = "adm:Kontrakt"
    class_name: ClassVar[str] = "Kontrakt"
    class_model_uri: ClassVar[URIRef] = ADM.Kontrakt

    id: Union[str, KontraktId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KontraktId):
            self.id = KontraktId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Lonsart(Begrep):
    """
    Type ytelse.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Lonsart"]
    class_class_curie: ClassVar[str] = "adm:Lonsart"
    class_name: ClassVar[str] = "Lonsart"
    class_model_uri: ClassVar[URIRef] = ADM.Lonsart

    id: Union[str, LonsartId] = None
    kode: str = None
    navn: str = None
    kategori: Optional[str] = None
    art: Optional[Union[str, ArtId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LonsartId):
            self.id = LonsartId(self.id)

        if self.kategori is not None and not isinstance(self.kategori, str):
            self.kategori = str(self.kategori)

        if self.art is not None and not isinstance(self.art, ArtId):
            self.art = ArtId(self.art)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Lopenummer(Begrep):
    """
    Løpenummer i ei nummerserie.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Lopenummer"]
    class_class_curie: ClassVar[str] = "adm:Lopenummer"
    class_name: ClassVar[str] = "Lopenummer"
    class_model_uri: ClassVar[URIRef] = ADM.Lopenummer

    id: Union[str, LopenummerId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LopenummerId):
            self.id = LopenummerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Objekt(Begrep):
    """
    Eit bygg, ein veg eller ein mottakar av ei teneste eller eit tilskott.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Objekt"]
    class_class_curie: ClassVar[str] = "adm:Objekt"
    class_name: ClassVar[str] = "Objekt"
    class_model_uri: ClassVar[URIRef] = ADM.Objekt

    id: Union[str, ObjektId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObjektId):
            self.id = ObjektId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organisasjonstype(Begrep):
    """
    Typen til eit organisasjonselement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Organisasjonstype"]
    class_class_curie: ClassVar[str] = "adm:Organisasjonstype"
    class_name: ClassVar[str] = "Organisasjonstype"
    class_model_uri: ClassVar[URIRef] = ADM.Organisasjonstype

    id: Union[str, OrganisasjonstypeId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganisasjonstypeId):
            self.id = OrganisasjonstypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Personalressurskategori(Begrep):
    """
    Ansettelsesform til eit arbeidsforhold.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Personalressurskategori"]
    class_class_curie: ClassVar[str] = "adm:Personalressurskategori"
    class_name: ClassVar[str] = "Personalressurskategori"
    class_model_uri: ClassVar[URIRef] = ADM.Personalressurskategori

    id: Union[str, PersonalressurskategoriId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonalressurskategoriId):
            self.id = PersonalressurskategoriId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Prosjekt(Begrep):
    """
    Del av kontostrengen som peikar på løpande prosjekt.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Prosjekt"]
    class_class_curie: ClassVar[str] = "adm:Prosjekt"
    class_name: ClassVar[str] = "Prosjekt"
    class_model_uri: ClassVar[URIRef] = ADM.Prosjekt

    id: Union[str, ProsjektId] = None
    kode: str = None
    navn: str = None
    prosjektart: Optional[Union[Union[str, ProsjektartId], list[Union[str, ProsjektartId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProsjektId):
            self.id = ProsjektId(self.id)

        if not isinstance(self.prosjektart, list):
            self.prosjektart = [self.prosjektart] if self.prosjektart is not None else []
        self.prosjektart = [v if isinstance(v, ProsjektartId) else ProsjektartId(v) for v in self.prosjektart]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Prosjektart(Begrep):
    """
    Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Prosjektart"]
    class_class_curie: ClassVar[str] = "adm:Prosjektart"
    class_name: ClassVar[str] = "Prosjektart"
    class_model_uri: ClassVar[URIRef] = ADM.Prosjektart

    id: Union[str, ProsjektartId] = None
    kode: str = None
    navn: str = None
    prosjekt: Optional[Union[str, ProsjektId]] = None
    overordnet: Optional[Union[str, ProsjektartId]] = None
    underordnet: Optional[Union[Union[str, ProsjektartId], list[Union[str, ProsjektartId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProsjektartId):
            self.id = ProsjektartId(self.id)

        if self.prosjekt is not None and not isinstance(self.prosjekt, ProsjektId):
            self.prosjekt = ProsjektId(self.prosjekt)

        if self.overordnet is not None and not isinstance(self.overordnet, ProsjektartId):
            self.overordnet = ProsjektartId(self.overordnet)

        if not isinstance(self.underordnet, list):
            self.underordnet = [self.underordnet] if self.underordnet is not None else []
        self.underordnet = [v if isinstance(v, ProsjektartId) else ProsjektartId(v) for v in self.underordnet]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ramme(Begrep):
    """
    Del av kontostrengen som viser kva budsjettramme som skal bere kostnadane.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Ramme"]
    class_class_curie: ClassVar[str] = "adm:Ramme"
    class_name: ClassVar[str] = "Ramme"
    class_model_uri: ClassVar[URIRef] = ADM.Ramme

    id: Union[str, RammeId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RammeId):
            self.id = RammeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Stillingskode(Begrep):
    """
    Felles kodeverk for stillingar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Stillingskode"]
    class_class_curie: ClassVar[str] = "adm:Stillingskode"
    class_name: ClassVar[str] = "Stillingskode"
    class_model_uri: ClassVar[URIRef] = ADM.Stillingskode

    id: Union[str, StillingskodeId] = None
    kode: str = None
    navn: str = None
    forelder: Optional[Union[str, StillingskodeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StillingskodeId):
            self.id = StillingskodeId(self.id)

        if self.forelder is not None and not isinstance(self.forelder, StillingskodeId):
            self.forelder = StillingskodeId(self.forelder)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Uketimetall(Begrep):
    """
    Timer per veke i 100 % stilling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADM["Uketimetall"]
    class_class_curie: ClassVar[str] = "adm:Uketimetall"
    class_name: ClassVar[str] = "Uketimetall"
    class_model_uri: ClassVar[URIRef] = ADM.Uketimetall

    id: Union[str, UketimetallId] = None
    kode: str = None
    navn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UketimetallId):
            self.id = UketimetallId(self.id)

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
    class_model_uri: ClassVar[URIRef] = ADM.Enhet

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
    class_model_uri: ClassVar[URIRef] = ADM.Identifikator

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
    class_model_uri: ClassVar[URIRef] = ADM.Periode

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
    class_model_uri: ClassVar[URIRef] = ADM.Personnavn

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
    class_model_uri: ClassVar[URIRef] = ADM.Kontaktinformasjon

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
    class_model_uri: ClassVar[URIRef] = ADM.Adresse

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
    class_model_uri: ClassVar[URIRef] = ADM.Matrikkelnummer

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
    class_model_uri: ClassVar[URIRef] = ADM.Landkode

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
    class_model_uri: ClassVar[URIRef] = ADM.Kjonn

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
    class_model_uri: ClassVar[URIRef] = ADM.Fylke

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
    class_model_uri: ClassVar[URIRef] = ADM.Kommune

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
    class_model_uri: ClassVar[URIRef] = ADM.Spraak

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
    class_model_uri: ClassVar[URIRef] = ADM.Valuta

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
    class_model_uri: ClassVar[URIRef] = ADM.Person

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
    class_model_uri: ClassVar[URIRef] = ADM.Kontaktperson

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
    class_model_uri: ClassVar[URIRef] = ADM.Virksomhet

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
                   model_uri=ADM.id, domain=None, range=URIRef)

slots.administrasjonContainer__personar = Slot(uri=ADM.personar, name="administrasjonContainer__personar", curie=ADM.curie('personar'),
                   model_uri=ADM.administrasjonContainer__personar, domain=None, range=Optional[Union[dict[Union[str, PersonId], Union[dict, Person]], list[Union[dict, Person]]]])

slots.administrasjonContainer__kontaktpersonar = Slot(uri=ADM.kontaktpersonar, name="administrasjonContainer__kontaktpersonar", curie=ADM.curie('kontaktpersonar'),
                   model_uri=ADM.administrasjonContainer__kontaktpersonar, domain=None, range=Optional[Union[dict[Union[str, KontaktpersonId], Union[dict, Kontaktperson]], list[Union[dict, Kontaktperson]]]])

slots.administrasjonContainer__virksomhetar = Slot(uri=ADM.virksomhetar, name="administrasjonContainer__virksomhetar", curie=ADM.curie('virksomhetar'),
                   model_uri=ADM.administrasjonContainer__virksomhetar, domain=None, range=Optional[Union[dict[Union[str, VirksomhetId], Union[dict, Virksomhet]], list[Union[dict, Virksomhet]]]])

slots.administrasjonContainer__landkodar = Slot(uri=ADM.landkodar, name="administrasjonContainer__landkodar", curie=ADM.curie('landkodar'),
                   model_uri=ADM.administrasjonContainer__landkodar, domain=None, range=Optional[Union[dict[Union[str, LandkodeId], Union[dict, Landkode]], list[Union[dict, Landkode]]]])

slots.administrasjonContainer__kjonn = Slot(uri=ADM.kjonn, name="administrasjonContainer__kjonn", curie=ADM.curie('kjonn'),
                   model_uri=ADM.administrasjonContainer__kjonn, domain=None, range=Optional[Union[dict[Union[str, KjonnId], Union[dict, Kjonn]], list[Union[dict, Kjonn]]]])

slots.administrasjonContainer__fylke = Slot(uri=ADM.fylke, name="administrasjonContainer__fylke", curie=ADM.curie('fylke'),
                   model_uri=ADM.administrasjonContainer__fylke, domain=None, range=Optional[Union[dict[Union[str, FylkeId], Union[dict, Fylke]], list[Union[dict, Fylke]]]])

slots.administrasjonContainer__kommunar = Slot(uri=ADM.kommunar, name="administrasjonContainer__kommunar", curie=ADM.curie('kommunar'),
                   model_uri=ADM.administrasjonContainer__kommunar, domain=None, range=Optional[Union[dict[Union[str, KommuneId], Union[dict, Kommune]], list[Union[dict, Kommune]]]])

slots.administrasjonContainer__spraak = Slot(uri=ADM.spraak, name="administrasjonContainer__spraak", curie=ADM.curie('spraak'),
                   model_uri=ADM.administrasjonContainer__spraak, domain=None, range=Optional[Union[dict[Union[str, SpraakId], Union[dict, Spraak]], list[Union[dict, Spraak]]]])

slots.administrasjonContainer__valuta = Slot(uri=ADM.valuta, name="administrasjonContainer__valuta", curie=ADM.curie('valuta'),
                   model_uri=ADM.administrasjonContainer__valuta, domain=None, range=Optional[Union[dict[Union[str, ValutaId], Union[dict, Valuta]], list[Union[dict, Valuta]]]])

slots.administrasjonContainer__personalressursar = Slot(uri=ADM.personalressursar, name="administrasjonContainer__personalressursar", curie=ADM.curie('personalressursar'),
                   model_uri=ADM.administrasjonContainer__personalressursar, domain=None, range=Optional[Union[dict[Union[str, PersonalressursId], Union[dict, Personalressurs]], list[Union[dict, Personalressurs]]]])

slots.administrasjonContainer__arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="administrasjonContainer__arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.administrasjonContainer__arbeidsforhold, domain=None, range=Optional[Union[dict[Union[str, ArbeidsforholdId], Union[dict, Arbeidsforhold]], list[Union[dict, Arbeidsforhold]]]])

slots.administrasjonContainer__arbeidslokasjoner = Slot(uri=ADM.arbeidslokasjoner, name="administrasjonContainer__arbeidslokasjoner", curie=ADM.curie('arbeidslokasjoner'),
                   model_uri=ADM.administrasjonContainer__arbeidslokasjoner, domain=None, range=Optional[Union[dict[Union[str, ArbeidslokasjonId], Union[dict, Arbeidslokasjon]], list[Union[dict, Arbeidslokasjon]]]])

slots.administrasjonContainer__fastlonn = Slot(uri=ADM.fastlonn, name="administrasjonContainer__fastlonn", curie=ADM.curie('fastlonn'),
                   model_uri=ADM.administrasjonContainer__fastlonn, domain=None, range=Optional[Union[dict[Union[str, FastlonnId], Union[dict, Fastlonn]], list[Union[dict, Fastlonn]]]])

slots.administrasjonContainer__fasttillegg = Slot(uri=ADM.fasttillegg, name="administrasjonContainer__fasttillegg", curie=ADM.curie('fasttillegg'),
                   model_uri=ADM.administrasjonContainer__fasttillegg, domain=None, range=Optional[Union[dict[Union[str, FasttilleggId], Union[dict, Fasttillegg]], list[Union[dict, Fasttillegg]]]])

slots.administrasjonContainer__fravaer = Slot(uri=ADM.fravaer, name="administrasjonContainer__fravaer", curie=ADM.curie('fravaer'),
                   model_uri=ADM.administrasjonContainer__fravaer, domain=None, range=Optional[Union[dict[Union[str, FravaerId], Union[dict, Fravaer]], list[Union[dict, Fravaer]]]])

slots.administrasjonContainer__fullmakter = Slot(uri=ADM.fullmakter, name="administrasjonContainer__fullmakter", curie=ADM.curie('fullmakter'),
                   model_uri=ADM.administrasjonContainer__fullmakter, domain=None, range=Optional[Union[dict[Union[str, FullmaktId], Union[dict, Fullmakt]], list[Union[dict, Fullmakt]]]])

slots.administrasjonContainer__organisasjonselement = Slot(uri=ADM.organisasjonselement, name="administrasjonContainer__organisasjonselement", curie=ADM.curie('organisasjonselement'),
                   model_uri=ADM.administrasjonContainer__organisasjonselement, domain=None, range=Optional[Union[dict[Union[str, OrganisasjonselementId], Union[dict, Organisasjonselement]], list[Union[dict, Organisasjonselement]]]])

slots.administrasjonContainer__rollar = Slot(uri=ADM.rollar, name="administrasjonContainer__rollar", curie=ADM.curie('rollar'),
                   model_uri=ADM.administrasjonContainer__rollar, domain=None, range=Optional[Union[dict[Union[str, RolleId], Union[dict, Rolle]], list[Union[dict, Rolle]]]])

slots.administrasjonContainer__variabellonn = Slot(uri=ADM.variabellonn, name="administrasjonContainer__variabellonn", curie=ADM.curie('variabellonn'),
                   model_uri=ADM.administrasjonContainer__variabellonn, domain=None, range=Optional[Union[dict[Union[str, VariabellonnId], Union[dict, Variabellonn]], list[Union[dict, Variabellonn]]]])

slots.administrasjonContainer__aktivitetar = Slot(uri=ADM.aktivitetar, name="administrasjonContainer__aktivitetar", curie=ADM.curie('aktivitetar'),
                   model_uri=ADM.administrasjonContainer__aktivitetar, domain=None, range=Optional[Union[dict[Union[str, AktivitetId], Union[dict, Aktivitet]], list[Union[dict, Aktivitet]]]])

slots.administrasjonContainer__anlegg = Slot(uri=ADM.anlegg, name="administrasjonContainer__anlegg", curie=ADM.curie('anlegg'),
                   model_uri=ADM.administrasjonContainer__anlegg, domain=None, range=Optional[Union[dict[Union[str, AnleggId], Union[dict, Anlegg]], list[Union[dict, Anlegg]]]])

slots.administrasjonContainer__ansvar = Slot(uri=ADM.ansvar, name="administrasjonContainer__ansvar", curie=ADM.curie('ansvar'),
                   model_uri=ADM.administrasjonContainer__ansvar, domain=None, range=Optional[Union[dict[Union[str, AnsvarId], Union[dict, Ansvar]], list[Union[dict, Ansvar]]]])

slots.administrasjonContainer__artar = Slot(uri=ADM.artar, name="administrasjonContainer__artar", curie=ADM.curie('artar'),
                   model_uri=ADM.administrasjonContainer__artar, domain=None, range=Optional[Union[dict[Union[str, ArtId], Union[dict, Art]], list[Union[dict, Art]]]])

slots.administrasjonContainer__arbeidsforholdstypar = Slot(uri=ADM.arbeidsforholdstypar, name="administrasjonContainer__arbeidsforholdstypar", curie=ADM.curie('arbeidsforholdstypar'),
                   model_uri=ADM.administrasjonContainer__arbeidsforholdstypar, domain=None, range=Optional[Union[dict[Union[str, ArbeidsforholdstypeId], Union[dict, Arbeidsforholdstype]], list[Union[dict, Arbeidsforholdstype]]]])

slots.administrasjonContainer__diverse = Slot(uri=ADM.diverse, name="administrasjonContainer__diverse", curie=ADM.curie('diverse'),
                   model_uri=ADM.administrasjonContainer__diverse, domain=None, range=Optional[Union[dict[Union[str, DiverseId], Union[dict, Diverse]], list[Union[dict, Diverse]]]])

slots.administrasjonContainer__formaal = Slot(uri=ADM.formaal, name="administrasjonContainer__formaal", curie=ADM.curie('formaal'),
                   model_uri=ADM.administrasjonContainer__formaal, domain=None, range=Optional[Union[dict[Union[str, FormaalId], Union[dict, Formaal]], list[Union[dict, Formaal]]]])

slots.administrasjonContainer__fravaersgrunnar = Slot(uri=ADM.fravaersgrunnar, name="administrasjonContainer__fravaersgrunnar", curie=ADM.curie('fravaersgrunnar'),
                   model_uri=ADM.administrasjonContainer__fravaersgrunnar, domain=None, range=Optional[Union[dict[Union[str, FravaersgrunnId], Union[dict, Fravaersgrunn]], list[Union[dict, Fravaersgrunn]]]])

slots.administrasjonContainer__fravaerstypar = Slot(uri=ADM.fravaerstypar, name="administrasjonContainer__fravaerstypar", curie=ADM.curie('fravaerstypar'),
                   model_uri=ADM.administrasjonContainer__fravaerstypar, domain=None, range=Optional[Union[dict[Union[str, FravaerstypeId], Union[dict, Fravaerstype]], list[Union[dict, Fravaerstype]]]])

slots.administrasjonContainer__funksjonar = Slot(uri=ADM.funksjonar, name="administrasjonContainer__funksjonar", curie=ADM.curie('funksjonar'),
                   model_uri=ADM.administrasjonContainer__funksjonar, domain=None, range=Optional[Union[dict[Union[str, FunksjonId], Union[dict, Funksjon]], list[Union[dict, Funksjon]]]])

slots.administrasjonContainer__kontrakter = Slot(uri=ADM.kontrakter, name="administrasjonContainer__kontrakter", curie=ADM.curie('kontrakter'),
                   model_uri=ADM.administrasjonContainer__kontrakter, domain=None, range=Optional[Union[dict[Union[str, KontraktId], Union[dict, Kontrakt]], list[Union[dict, Kontrakt]]]])

slots.administrasjonContainer__lonsartar = Slot(uri=ADM.lonsartar, name="administrasjonContainer__lonsartar", curie=ADM.curie('lonsartar'),
                   model_uri=ADM.administrasjonContainer__lonsartar, domain=None, range=Optional[Union[dict[Union[str, LonsartId], Union[dict, Lonsart]], list[Union[dict, Lonsart]]]])

slots.administrasjonContainer__lopenummer = Slot(uri=ADM.lopenummer, name="administrasjonContainer__lopenummer", curie=ADM.curie('lopenummer'),
                   model_uri=ADM.administrasjonContainer__lopenummer, domain=None, range=Optional[Union[dict[Union[str, LopenummerId], Union[dict, Lopenummer]], list[Union[dict, Lopenummer]]]])

slots.administrasjonContainer__objekt = Slot(uri=ADM.objekt, name="administrasjonContainer__objekt", curie=ADM.curie('objekt'),
                   model_uri=ADM.administrasjonContainer__objekt, domain=None, range=Optional[Union[dict[Union[str, ObjektId], Union[dict, Objekt]], list[Union[dict, Objekt]]]])

slots.administrasjonContainer__organisasjonstypar = Slot(uri=ADM.organisasjonstypar, name="administrasjonContainer__organisasjonstypar", curie=ADM.curie('organisasjonstypar'),
                   model_uri=ADM.administrasjonContainer__organisasjonstypar, domain=None, range=Optional[Union[dict[Union[str, OrganisasjonstypeId], Union[dict, Organisasjonstype]], list[Union[dict, Organisasjonstype]]]])

slots.administrasjonContainer__personalressurskategoriar = Slot(uri=ADM.personalressurskategoriar, name="administrasjonContainer__personalressurskategoriar", curie=ADM.curie('personalressurskategoriar'),
                   model_uri=ADM.administrasjonContainer__personalressurskategoriar, domain=None, range=Optional[Union[dict[Union[str, PersonalressurskategoriId], Union[dict, Personalressurskategori]], list[Union[dict, Personalressurskategori]]]])

slots.administrasjonContainer__prosjekt = Slot(uri=ADM.prosjekt, name="administrasjonContainer__prosjekt", curie=ADM.curie('prosjekt'),
                   model_uri=ADM.administrasjonContainer__prosjekt, domain=None, range=Optional[Union[dict[Union[str, ProsjektId], Union[dict, Prosjekt]], list[Union[dict, Prosjekt]]]])

slots.administrasjonContainer__prosjektartar = Slot(uri=ADM.prosjektartar, name="administrasjonContainer__prosjektartar", curie=ADM.curie('prosjektartar'),
                   model_uri=ADM.administrasjonContainer__prosjektartar, domain=None, range=Optional[Union[dict[Union[str, ProsjektartId], Union[dict, Prosjektart]], list[Union[dict, Prosjektart]]]])

slots.administrasjonContainer__rammer = Slot(uri=ADM.rammer, name="administrasjonContainer__rammer", curie=ADM.curie('rammer'),
                   model_uri=ADM.administrasjonContainer__rammer, domain=None, range=Optional[Union[dict[Union[str, RammeId], Union[dict, Ramme]], list[Union[dict, Ramme]]]])

slots.administrasjonContainer__stillingskoder = Slot(uri=ADM.stillingskoder, name="administrasjonContainer__stillingskoder", curie=ADM.curie('stillingskoder'),
                   model_uri=ADM.administrasjonContainer__stillingskoder, domain=None, range=Optional[Union[dict[Union[str, StillingskodeId], Union[dict, Stillingskode]], list[Union[dict, Stillingskode]]]])

slots.administrasjonContainer__uketimetall = Slot(uri=ADM.uketimetall, name="administrasjonContainer__uketimetall", curie=ADM.curie('uketimetall'),
                   model_uri=ADM.administrasjonContainer__uketimetall, domain=None, range=Optional[Union[dict[Union[str, UketimetallId], Union[dict, Uketimetall]], list[Union[dict, Uketimetall]]]])

slots.lonn__anvist = Slot(uri=ADM.anvist, name="lonn__anvist", curie=ADM.curie('anvist'),
                   model_uri=ADM.lonn__anvist, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.lonn__attestert = Slot(uri=ADM.attestert, name="lonn__attestert", curie=ADM.curie('attestert'),
                   model_uri=ADM.lonn__attestert, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.lonn__beskrivelse = Slot(uri=ADM.beskrivelse, name="lonn__beskrivelse", curie=ADM.curie('beskrivelse'),
                   model_uri=ADM.lonn__beskrivelse, domain=None, range=str)

slots.lonn__kildesystemId = Slot(uri=ADM.kildesystemId, name="lonn__kildesystemId", curie=ADM.curie('kildesystemId'),
                   model_uri=ADM.lonn__kildesystemId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.lonn__kontert = Slot(uri=ADM.kontert, name="lonn__kontert", curie=ADM.curie('kontert'),
                   model_uri=ADM.lonn__kontert, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.lonn__kontostreng = Slot(uri=ADM.kontostreng, name="lonn__kontostreng", curie=ADM.curie('kontostreng'),
                   model_uri=ADM.lonn__kontostreng, domain=None, range=Union[dict, Kontostreng])

slots.lonn__opptjent = Slot(uri=ADM.opptjent, name="lonn__opptjent", curie=ADM.curie('opptjent'),
                   model_uri=ADM.lonn__opptjent, domain=None, range=Optional[Union[dict, Periode]])

slots.lonn__periode = Slot(uri=ADM.periode, name="lonn__periode", curie=ADM.curie('periode'),
                   model_uri=ADM.lonn__periode, domain=None, range=Union[dict, Periode])

slots.lonn__anviser = Slot(uri=ADM.anviser, name="lonn__anviser", curie=ADM.curie('anviser'),
                   model_uri=ADM.lonn__anviser, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.lonn__konterer = Slot(uri=ADM.konterer, name="lonn__konterer", curie=ADM.curie('konterer'),
                   model_uri=ADM.lonn__konterer, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.lonn__attestant = Slot(uri=ADM.attestant, name="lonn__attestant", curie=ADM.curie('attestant'),
                   model_uri=ADM.lonn__attestant, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.kontostreng__aktivitet = Slot(uri=ADM.aktivitet, name="kontostreng__aktivitet", curie=ADM.curie('aktivitet'),
                   model_uri=ADM.kontostreng__aktivitet, domain=None, range=Optional[Union[str, AktivitetId]])

slots.kontostreng__anlegg = Slot(uri=ADM.anlegg, name="kontostreng__anlegg", curie=ADM.curie('anlegg'),
                   model_uri=ADM.kontostreng__anlegg, domain=None, range=Optional[Union[str, AnleggId]])

slots.kontostreng__ansvar = Slot(uri=ADM.ansvar, name="kontostreng__ansvar", curie=ADM.curie('ansvar'),
                   model_uri=ADM.kontostreng__ansvar, domain=None, range=Union[str, AnsvarId])

slots.kontostreng__art = Slot(uri=ADM.art, name="kontostreng__art", curie=ADM.curie('art'),
                   model_uri=ADM.kontostreng__art, domain=None, range=Union[str, ArtId])

slots.kontostreng__diverse = Slot(uri=ADM.diverse, name="kontostreng__diverse", curie=ADM.curie('diverse'),
                   model_uri=ADM.kontostreng__diverse, domain=None, range=Optional[Union[str, DiverseId]])

slots.kontostreng__formaal = Slot(uri=ADM.formaal, name="kontostreng__formaal", curie=ADM.curie('formaal'),
                   model_uri=ADM.kontostreng__formaal, domain=None, range=Optional[Union[str, FormaalId]])

slots.kontostreng__funksjon = Slot(uri=ADM.funksjon, name="kontostreng__funksjon", curie=ADM.curie('funksjon'),
                   model_uri=ADM.kontostreng__funksjon, domain=None, range=Union[str, FunksjonId])

slots.kontostreng__kontrakt = Slot(uri=ADM.kontrakt, name="kontostreng__kontrakt", curie=ADM.curie('kontrakt'),
                   model_uri=ADM.kontostreng__kontrakt, domain=None, range=Optional[Union[str, KontraktId]])

slots.kontostreng__lopenummer = Slot(uri=ADM.lopenummer, name="kontostreng__lopenummer", curie=ADM.curie('lopenummer'),
                   model_uri=ADM.kontostreng__lopenummer, domain=None, range=Optional[Union[str, LopenummerId]])

slots.kontostreng__objekt = Slot(uri=ADM.objekt, name="kontostreng__objekt", curie=ADM.curie('objekt'),
                   model_uri=ADM.kontostreng__objekt, domain=None, range=Optional[Union[str, ObjektId]])

slots.kontostreng__prosjekt = Slot(uri=ADM.prosjekt, name="kontostreng__prosjekt", curie=ADM.curie('prosjekt'),
                   model_uri=ADM.kontostreng__prosjekt, domain=None, range=Optional[Union[str, ProsjektId]])

slots.kontostreng__prosjektart = Slot(uri=ADM.prosjektart, name="kontostreng__prosjektart", curie=ADM.curie('prosjektart'),
                   model_uri=ADM.kontostreng__prosjektart, domain=None, range=Optional[Union[str, ProsjektartId]])

slots.kontostreng__ramme = Slot(uri=ADM.ramme, name="kontostreng__ramme", curie=ADM.curie('ramme'),
                   model_uri=ADM.kontostreng__ramme, domain=None, range=Optional[Union[str, RammeId]])

slots.ansvar__overordnet = Slot(uri=ADM.overordnet, name="ansvar__overordnet", curie=ADM.curie('overordnet'),
                   model_uri=ADM.ansvar__overordnet, domain=None, range=Optional[Union[str, AnsvarId]])

slots.ansvar__underordnet = Slot(uri=ADM.underordnet, name="ansvar__underordnet", curie=ADM.curie('underordnet'),
                   model_uri=ADM.ansvar__underordnet, domain=None, range=Optional[Union[Union[str, AnsvarId], list[Union[str, AnsvarId]]]])

slots.ansvar__organisasjonselement = Slot(uri=ADM.organisasjonselement, name="ansvar__organisasjonselement", curie=ADM.curie('organisasjonselement'),
                   model_uri=ADM.ansvar__organisasjonselement, domain=None, range=Optional[Union[Union[str, OrganisasjonselementId], list[Union[str, OrganisasjonselementId]]]])

slots.arbeidsforholdstype__forelder = Slot(uri=ADM.forelder, name="arbeidsforholdstype__forelder", curie=ADM.curie('forelder'),
                   model_uri=ADM.arbeidsforholdstype__forelder, domain=None, range=Optional[Union[str, ArbeidsforholdstypeId]])

slots.fravaerstype__overfores = Slot(uri=ADM.overfores, name="fravaerstype__overfores", curie=ADM.curie('overfores'),
                   model_uri=ADM.fravaerstype__overfores, domain=None, range=Optional[Union[bool, Bool]])

slots.fravaerstype__lonsart = Slot(uri=ADM.lonsart, name="fravaerstype__lonsart", curie=ADM.curie('lonsart'),
                   model_uri=ADM.fravaerstype__lonsart, domain=None, range=Optional[Union[str, LonsartId]])

slots.funksjon__overordnet = Slot(uri=ADM.overordnet, name="funksjon__overordnet", curie=ADM.curie('overordnet'),
                   model_uri=ADM.funksjon__overordnet, domain=None, range=Optional[Union[str, FunksjonId]])

slots.funksjon__underordnet = Slot(uri=ADM.underordnet, name="funksjon__underordnet", curie=ADM.curie('underordnet'),
                   model_uri=ADM.funksjon__underordnet, domain=None, range=Optional[Union[Union[str, FunksjonId], list[Union[str, FunksjonId]]]])

slots.lonsart__kategori = Slot(uri=ADM.kategori, name="lonsart__kategori", curie=ADM.curie('kategori'),
                   model_uri=ADM.lonsart__kategori, domain=None, range=Optional[str])

slots.lonsart__art = Slot(uri=ADM.art, name="lonsart__art", curie=ADM.curie('art'),
                   model_uri=ADM.lonsart__art, domain=None, range=Optional[Union[str, ArtId]])

slots.prosjekt__prosjektart = Slot(uri=ADM.prosjektart, name="prosjekt__prosjektart", curie=ADM.curie('prosjektart'),
                   model_uri=ADM.prosjekt__prosjektart, domain=None, range=Optional[Union[Union[str, ProsjektartId], list[Union[str, ProsjektartId]]]])

slots.prosjektart__prosjekt = Slot(uri=ADM.prosjekt, name="prosjektart__prosjekt", curie=ADM.curie('prosjekt'),
                   model_uri=ADM.prosjektart__prosjekt, domain=None, range=Optional[Union[str, ProsjektId]])

slots.prosjektart__overordnet = Slot(uri=ADM.overordnet, name="prosjektart__overordnet", curie=ADM.curie('overordnet'),
                   model_uri=ADM.prosjektart__overordnet, domain=None, range=Optional[Union[str, ProsjektartId]])

slots.prosjektart__underordnet = Slot(uri=ADM.underordnet, name="prosjektart__underordnet", curie=ADM.curie('underordnet'),
                   model_uri=ADM.prosjektart__underordnet, domain=None, range=Optional[Union[Union[str, ProsjektartId], list[Union[str, ProsjektartId]]]])

slots.stillingskode__forelder = Slot(uri=ADM.forelder, name="stillingskode__forelder", curie=ADM.curie('forelder'),
                   model_uri=ADM.stillingskode__forelder, domain=None, range=Optional[Union[str, StillingskodeId]])

slots.fastlonn__prosent = Slot(uri=ADM.prosent, name="fastlonn__prosent", curie=ADM.curie('prosent'),
                   model_uri=ADM.fastlonn__prosent, domain=None, range=int)

slots.fastlonn__lonsart = Slot(uri=ADM.lonsart, name="fastlonn__lonsart", curie=ADM.curie('lonsart'),
                   model_uri=ADM.fastlonn__lonsart, domain=None, range=Optional[Union[str, LonsartId]])

slots.fastlonn__arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="fastlonn__arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.fastlonn__arbeidsforhold, domain=None, range=Union[str, ArbeidsforholdId])

slots.fasttillegg__belop = Slot(uri=ADM.belop, name="fasttillegg__belop", curie=ADM.curie('belop'),
                   model_uri=ADM.fasttillegg__belop, domain=None, range=int)

slots.fasttillegg__lonsart = Slot(uri=ADM.lonsart, name="fasttillegg__lonsart", curie=ADM.curie('lonsart'),
                   model_uri=ADM.fasttillegg__lonsart, domain=None, range=Union[str, LonsartId])

slots.fasttillegg__arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="fasttillegg__arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.fasttillegg__arbeidsforhold, domain=None, range=Union[str, ArbeidsforholdId])

slots.variabellonn__antall = Slot(uri=ADM.antall, name="variabellonn__antall", curie=ADM.curie('antall'),
                   model_uri=ADM.variabellonn__antall, domain=None, range=int)

slots.variabellonn__belop = Slot(uri=ADM.belop, name="variabellonn__belop", curie=ADM.curie('belop'),
                   model_uri=ADM.variabellonn__belop, domain=None, range=Optional[int])

slots.variabellonn__lonsart = Slot(uri=ADM.lonsart, name="variabellonn__lonsart", curie=ADM.curie('lonsart'),
                   model_uri=ADM.variabellonn__lonsart, domain=None, range=Union[str, LonsartId])

slots.variabellonn__arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="variabellonn__arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.variabellonn__arbeidsforhold, domain=None, range=Union[str, ArbeidsforholdId])

slots.fravaer__godkjent = Slot(uri=ADM.godkjent, name="fravaer__godkjent", curie=ADM.curie('godkjent'),
                   model_uri=ADM.fravaer__godkjent, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.fravaer__kildesystemId = Slot(uri=ADM.kildesystemId, name="fravaer__kildesystemId", curie=ADM.curie('kildesystemId'),
                   model_uri=ADM.fravaer__kildesystemId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.fravaer__periode = Slot(uri=ADM.periode, name="fravaer__periode", curie=ADM.curie('periode'),
                   model_uri=ADM.fravaer__periode, domain=None, range=Union[dict, Periode])

slots.fravaer__prosent = Slot(uri=ADM.prosent, name="fravaer__prosent", curie=ADM.curie('prosent'),
                   model_uri=ADM.fravaer__prosent, domain=None, range=int)

slots.fravaer__fravaersgrunn = Slot(uri=ADM.fravaersgrunn, name="fravaer__fravaersgrunn", curie=ADM.curie('fravaersgrunn'),
                   model_uri=ADM.fravaer__fravaersgrunn, domain=None, range=Optional[Union[str, FravaersgrunnId]])

slots.fravaer__fravaerstype = Slot(uri=ADM.fravaerstype, name="fravaer__fravaerstype", curie=ADM.curie('fravaerstype'),
                   model_uri=ADM.fravaer__fravaerstype, domain=None, range=Union[str, FravaerstypeId])

slots.fravaer__arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="fravaer__arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.fravaer__arbeidsforhold, domain=None, range=Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]])

slots.fravaer__fortsettelse = Slot(uri=ADM.fortsettelse, name="fravaer__fortsettelse", curie=ADM.curie('fortsettelse'),
                   model_uri=ADM.fravaer__fortsettelse, domain=None, range=Optional[Union[str, FravaerId]])

slots.fravaer__fortsetter = Slot(uri=ADM.fortsetter, name="fravaer__fortsetter", curie=ADM.curie('fortsetter'),
                   model_uri=ADM.fravaer__fortsetter, domain=None, range=Optional[Union[str, FravaerId]])

slots.fravaer__godkjenner = Slot(uri=ADM.godkjenner, name="fravaer__godkjenner", curie=ADM.curie('godkjenner'),
                   model_uri=ADM.fravaer__godkjenner, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.fullmakt__gyldighetsperiode = Slot(uri=ADM.gyldighetsperiode, name="fullmakt__gyldighetsperiode", curie=ADM.curie('gyldighetsperiode'),
                   model_uri=ADM.fullmakt__gyldighetsperiode, domain=None, range=Union[dict, Periode])

slots.fullmakt__ramme = Slot(uri=ADM.ramme, name="fullmakt__ramme", curie=ADM.curie('ramme'),
                   model_uri=ADM.fullmakt__ramme, domain=None, range=Optional[Union[str, RammeId]])

slots.fullmakt__funksjon = Slot(uri=ADM.funksjon, name="fullmakt__funksjon", curie=ADM.curie('funksjon'),
                   model_uri=ADM.fullmakt__funksjon, domain=None, range=Optional[Union[str, FunksjonId]])

slots.fullmakt__objekt = Slot(uri=ADM.objekt, name="fullmakt__objekt", curie=ADM.curie('objekt'),
                   model_uri=ADM.fullmakt__objekt, domain=None, range=Optional[Union[str, ObjektId]])

slots.fullmakt__organisasjonselement = Slot(uri=ADM.organisasjonselement, name="fullmakt__organisasjonselement", curie=ADM.curie('organisasjonselement'),
                   model_uri=ADM.fullmakt__organisasjonselement, domain=None, range=Optional[Union[str, OrganisasjonselementId]])

slots.fullmakt__art = Slot(uri=ADM.art, name="fullmakt__art", curie=ADM.curie('art'),
                   model_uri=ADM.fullmakt__art, domain=None, range=Optional[Union[str, ArtId]])

slots.fullmakt__anlegg = Slot(uri=ADM.anlegg, name="fullmakt__anlegg", curie=ADM.curie('anlegg'),
                   model_uri=ADM.fullmakt__anlegg, domain=None, range=Optional[Union[str, AnleggId]])

slots.fullmakt__diverse = Slot(uri=ADM.diverse, name="fullmakt__diverse", curie=ADM.curie('diverse'),
                   model_uri=ADM.fullmakt__diverse, domain=None, range=Optional[Union[str, DiverseId]])

slots.fullmakt__aktivitet = Slot(uri=ADM.aktivitet, name="fullmakt__aktivitet", curie=ADM.curie('aktivitet'),
                   model_uri=ADM.fullmakt__aktivitet, domain=None, range=Optional[Union[str, AktivitetId]])

slots.fullmakt__ansvar = Slot(uri=ADM.ansvar, name="fullmakt__ansvar", curie=ADM.curie('ansvar'),
                   model_uri=ADM.fullmakt__ansvar, domain=None, range=Optional[Union[str, AnsvarId]])

slots.fullmakt__stedfortreder = Slot(uri=ADM.stedfortreder, name="fullmakt__stedfortreder", curie=ADM.curie('stedfortreder'),
                   model_uri=ADM.fullmakt__stedfortreder, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.fullmakt__kontrakt = Slot(uri=ADM.kontrakt, name="fullmakt__kontrakt", curie=ADM.curie('kontrakt'),
                   model_uri=ADM.fullmakt__kontrakt, domain=None, range=Optional[Union[str, KontraktId]])

slots.fullmakt__fullmektig = Slot(uri=ADM.fullmektig, name="fullmakt__fullmektig", curie=ADM.curie('fullmektig'),
                   model_uri=ADM.fullmakt__fullmektig, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.fullmakt__prosjekt = Slot(uri=ADM.prosjekt, name="fullmakt__prosjekt", curie=ADM.curie('prosjekt'),
                   model_uri=ADM.fullmakt__prosjekt, domain=None, range=Optional[Union[str, ProsjektId]])

slots.fullmakt__formaal = Slot(uri=ADM.formaal, name="fullmakt__formaal", curie=ADM.curie('formaal'),
                   model_uri=ADM.fullmakt__formaal, domain=None, range=Optional[Union[str, FormaalId]])

slots.fullmakt__rolle = Slot(uri=ADM.rolle, name="fullmakt__rolle", curie=ADM.curie('rolle'),
                   model_uri=ADM.fullmakt__rolle, domain=None, range=Union[str, RolleId])

slots.fullmakt__lopenummer = Slot(uri=ADM.lopenummer, name="fullmakt__lopenummer", curie=ADM.curie('lopenummer'),
                   model_uri=ADM.fullmakt__lopenummer, domain=None, range=Optional[Union[str, LopenummerId]])

slots.rolle__rolleNavn = Slot(uri=ADM.rolleNavn, name="rolle__rolleNavn", curie=ADM.curie('rolleNavn'),
                   model_uri=ADM.rolle__rolleNavn, domain=None, range=Union[dict, Identifikator])

slots.rolle__beskrivelse = Slot(uri=ADM.beskrivelse, name="rolle__beskrivelse", curie=ADM.curie('beskrivelse'),
                   model_uri=ADM.rolle__beskrivelse, domain=None, range=str)

slots.rolle__fullmakt = Slot(uri=ADM.fullmakt, name="rolle__fullmakt", curie=ADM.curie('fullmakt'),
                   model_uri=ADM.rolle__fullmakt, domain=None, range=Union[Union[str, FullmaktId], list[Union[str, FullmaktId]]])

slots.arbeidslokasjon__lokasjonskode = Slot(uri=ADM.lokasjonskode, name="arbeidslokasjon__lokasjonskode", curie=ADM.curie('lokasjonskode'),
                   model_uri=ADM.arbeidslokasjon__lokasjonskode, domain=None, range=Union[dict, Identifikator])

slots.arbeidslokasjon__lokasjonsnavn = Slot(uri=ADM.lokasjonsnavn, name="arbeidslokasjon__lokasjonsnavn", curie=ADM.curie('lokasjonsnavn'),
                   model_uri=ADM.arbeidslokasjon__lokasjonsnavn, domain=None, range=Optional[str])

slots.arbeidslokasjon__forretningsadresse = Slot(uri=ADM.forretningsadresse, name="arbeidslokasjon__forretningsadresse", curie=ADM.curie('forretningsadresse'),
                   model_uri=ADM.arbeidslokasjon__forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.arbeidslokasjon__organisasjonsnavn = Slot(uri=ADM.organisasjonsnavn, name="arbeidslokasjon__organisasjonsnavn", curie=ADM.curie('organisasjonsnavn'),
                   model_uri=ADM.arbeidslokasjon__organisasjonsnavn, domain=None, range=Optional[str])

slots.arbeidslokasjon__organisasjonsnummer = Slot(uri=ADM.organisasjonsnummer, name="arbeidslokasjon__organisasjonsnummer", curie=ADM.curie('organisasjonsnummer'),
                   model_uri=ADM.arbeidslokasjon__organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.arbeidslokasjon__kontaktinformasjon = Slot(uri=ADM.kontaktinformasjon, name="arbeidslokasjon__kontaktinformasjon", curie=ADM.curie('kontaktinformasjon'),
                   model_uri=ADM.arbeidslokasjon__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.arbeidslokasjon__postadresse = Slot(uri=ADM.postadresse, name="arbeidslokasjon__postadresse", curie=ADM.curie('postadresse'),
                   model_uri=ADM.arbeidslokasjon__postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.arbeidslokasjon__arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="arbeidslokasjon__arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.arbeidslokasjon__arbeidsforhold, domain=None, range=Optional[Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]]])

slots.organisasjonselement__gyldighetsperiode = Slot(uri=ADM.gyldighetsperiode, name="organisasjonselement__gyldighetsperiode", curie=ADM.curie('gyldighetsperiode'),
                   model_uri=ADM.organisasjonselement__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.organisasjonselement__kortnavn = Slot(uri=ADM.kortnavn, name="organisasjonselement__kortnavn", curie=ADM.curie('kortnavn'),
                   model_uri=ADM.organisasjonselement__kortnavn, domain=None, range=Optional[str])

slots.organisasjonselement__navn = Slot(uri=ADM.namn, name="organisasjonselement__navn", curie=ADM.curie('namn'),
                   model_uri=ADM.organisasjonselement__navn, domain=None, range=Optional[str])

slots.organisasjonselement__organisasjonsId = Slot(uri=ADM.organisasjonsId, name="organisasjonselement__organisasjonsId", curie=ADM.curie('organisasjonsId'),
                   model_uri=ADM.organisasjonselement__organisasjonsId, domain=None, range=Union[dict, Identifikator])

slots.organisasjonselement__organisasjonsKode = Slot(uri=ADM.organisasjonsKode, name="organisasjonselement__organisasjonsKode", curie=ADM.curie('organisasjonsKode'),
                   model_uri=ADM.organisasjonselement__organisasjonsKode, domain=None, range=Union[dict, Identifikator])

slots.organisasjonselement__forretningsadresse = Slot(uri=ADM.forretningsadresse, name="organisasjonselement__forretningsadresse", curie=ADM.curie('forretningsadresse'),
                   model_uri=ADM.organisasjonselement__forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.organisasjonselement__organisasjonsnavn = Slot(uri=ADM.organisasjonsnavn, name="organisasjonselement__organisasjonsnavn", curie=ADM.curie('organisasjonsnavn'),
                   model_uri=ADM.organisasjonselement__organisasjonsnavn, domain=None, range=Optional[str])

slots.organisasjonselement__organisasjonsnummer = Slot(uri=ADM.organisasjonsnummer, name="organisasjonselement__organisasjonsnummer", curie=ADM.curie('organisasjonsnummer'),
                   model_uri=ADM.organisasjonselement__organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.organisasjonselement__kontaktinformasjon = Slot(uri=ADM.kontaktinformasjon, name="organisasjonselement__kontaktinformasjon", curie=ADM.curie('kontaktinformasjon'),
                   model_uri=ADM.organisasjonselement__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.organisasjonselement__postadresse = Slot(uri=ADM.postadresse, name="organisasjonselement__postadresse", curie=ADM.curie('postadresse'),
                   model_uri=ADM.organisasjonselement__postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.organisasjonselement__ansvar = Slot(uri=ADM.ansvar, name="organisasjonselement__ansvar", curie=ADM.curie('ansvar'),
                   model_uri=ADM.organisasjonselement__ansvar, domain=None, range=Optional[Union[Union[str, AnsvarId], list[Union[str, AnsvarId]]]])

slots.organisasjonselement__organisasjonstype = Slot(uri=ADM.organisasjonstype, name="organisasjonselement__organisasjonstype", curie=ADM.curie('organisasjonstype'),
                   model_uri=ADM.organisasjonselement__organisasjonstype, domain=None, range=Optional[Union[str, OrganisasjonstypeId]])

slots.organisasjonselement__leder = Slot(uri=ADM.leder, name="organisasjonselement__leder", curie=ADM.curie('leder'),
                   model_uri=ADM.organisasjonselement__leder, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.organisasjonselement__overordnet = Slot(uri=ADM.overordnet, name="organisasjonselement__overordnet", curie=ADM.curie('overordnet'),
                   model_uri=ADM.organisasjonselement__overordnet, domain=None, range=Union[str, OrganisasjonselementId])

slots.organisasjonselement__underordnet = Slot(uri=ADM.underordnet, name="organisasjonselement__underordnet", curie=ADM.curie('underordnet'),
                   model_uri=ADM.organisasjonselement__underordnet, domain=None, range=Optional[Union[Union[str, OrganisasjonselementId], list[Union[str, OrganisasjonselementId]]]])

slots.organisasjonselement__skole = Slot(uri=ADM.skole, name="organisasjonselement__skole", curie=ADM.curie('skole'),
                   model_uri=ADM.organisasjonselement__skole, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.organisasjonselement__arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="organisasjonselement__arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.organisasjonselement__arbeidsforhold, domain=None, range=Optional[Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]]])

slots.personalressurs__ansattnummer = Slot(uri=ADM.ansattnummer, name="personalressurs__ansattnummer", curie=ADM.curie('ansattnummer'),
                   model_uri=ADM.personalressurs__ansattnummer, domain=None, range=Union[dict, Identifikator])

slots.personalressurs__ansettelsesperiode = Slot(uri=ADM.ansettelsesperiode, name="personalressurs__ansettelsesperiode", curie=ADM.curie('ansettelsesperiode'),
                   model_uri=ADM.personalressurs__ansettelsesperiode, domain=None, range=Union[dict, Periode])

slots.personalressurs__ansiennitet = Slot(uri=ADM.ansiennitet, name="personalressurs__ansiennitet", curie=ADM.curie('ansiennitet'),
                   model_uri=ADM.personalressurs__ansiennitet, domain=None, range=Optional[Union[str, XSDDate]])

slots.personalressurs__brukernavn = Slot(uri=ADM.brukernavn, name="personalressurs__brukernavn", curie=ADM.curie('brukernavn'),
                   model_uri=ADM.personalressurs__brukernavn, domain=None, range=Optional[Union[dict, Identifikator]])

slots.personalressurs__jobbtittel = Slot(uri=ADM.jobbtittel, name="personalressurs__jobbtittel", curie=ADM.curie('jobbtittel'),
                   model_uri=ADM.personalressurs__jobbtittel, domain=None, range=Optional[str])

slots.personalressurs__kontaktinformasjon = Slot(uri=ADM.kontaktinformasjon, name="personalressurs__kontaktinformasjon", curie=ADM.curie('kontaktinformasjon'),
                   model_uri=ADM.personalressurs__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.personalressurs__person = Slot(uri=ADM.person, name="personalressurs__person", curie=ADM.curie('person'),
                   model_uri=ADM.personalressurs__person, domain=None, range=Union[str, PersonId])

slots.personalressurs__stedfortreder = Slot(uri=ADM.stedfortreder, name="personalressurs__stedfortreder", curie=ADM.curie('stedfortreder'),
                   model_uri=ADM.personalressurs__stedfortreder, domain=None, range=Optional[Union[Union[str, FullmaktId], list[Union[str, FullmaktId]]]])

slots.personalressurs__fullmakt = Slot(uri=ADM.fullmakt, name="personalressurs__fullmakt", curie=ADM.curie('fullmakt'),
                   model_uri=ADM.personalressurs__fullmakt, domain=None, range=Optional[Union[Union[str, FullmaktId], list[Union[str, FullmaktId]]]])

slots.personalressurs__personalressurskategori = Slot(uri=ADM.personalressurskategori, name="personalressurs__personalressurskategori", curie=ADM.curie('personalressurskategori'),
                   model_uri=ADM.personalressurs__personalressurskategori, domain=None, range=Union[str, PersonalressurskategoriId])

slots.personalressurs__lederFor = Slot(uri=ADM.lederFor, name="personalressurs__lederFor", curie=ADM.curie('lederFor'),
                   model_uri=ADM.personalressurs__lederFor, domain=None, range=Optional[Union[Union[str, OrganisasjonselementId], list[Union[str, OrganisasjonselementId]]]])

slots.personalressurs__arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="personalressurs__arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.personalressurs__arbeidsforhold, domain=None, range=Optional[Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]]])

slots.personalressurs__personalansvar = Slot(uri=ADM.personalansvar, name="personalressurs__personalansvar", curie=ADM.curie('personalansvar'),
                   model_uri=ADM.personalressurs__personalansvar, domain=None, range=Optional[Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]]])

slots.personalressurs__skoleressurs = Slot(uri=ADM.skoleressurs, name="personalressurs__skoleressurs", curie=ADM.curie('skoleressurs'),
                   model_uri=ADM.personalressurs__skoleressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.arbeidsforhold__ansettelsesprosent = Slot(uri=ADM.ansettelsesprosent, name="arbeidsforhold__ansettelsesprosent", curie=ADM.curie('ansettelsesprosent'),
                   model_uri=ADM.arbeidsforhold__ansettelsesprosent, domain=None, range=int)

slots.arbeidsforhold__arbeidsforholdsperiode = Slot(uri=ADM.arbeidsforholdsperiode, name="arbeidsforhold__arbeidsforholdsperiode", curie=ADM.curie('arbeidsforholdsperiode'),
                   model_uri=ADM.arbeidsforhold__arbeidsforholdsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.arbeidsforhold__aarslonn = Slot(uri=ADM.aarslonn, name="arbeidsforhold__aarslonn", curie=ADM.curie('aarslonn'),
                   model_uri=ADM.arbeidsforhold__aarslonn, domain=None, range=int)

slots.arbeidsforhold__gyldighetsperiode = Slot(uri=ADM.gyldighetsperiode, name="arbeidsforhold__gyldighetsperiode", curie=ADM.curie('gyldighetsperiode'),
                   model_uri=ADM.arbeidsforhold__gyldighetsperiode, domain=None, range=Union[dict, Periode])

slots.arbeidsforhold__hovedstilling = Slot(uri=ADM.hovedstilling, name="arbeidsforhold__hovedstilling", curie=ADM.curie('hovedstilling'),
                   model_uri=ADM.arbeidsforhold__hovedstilling, domain=None, range=Union[bool, Bool])

slots.arbeidsforhold__lonnsprosent = Slot(uri=ADM.lonnsprosent, name="arbeidsforhold__lonnsprosent", curie=ADM.curie('lonnsprosent'),
                   model_uri=ADM.arbeidsforhold__lonnsprosent, domain=None, range=int)

slots.arbeidsforhold__stillingsnummer = Slot(uri=ADM.stillingsnummer, name="arbeidsforhold__stillingsnummer", curie=ADM.curie('stillingsnummer'),
                   model_uri=ADM.arbeidsforhold__stillingsnummer, domain=None, range=str)

slots.arbeidsforhold__stillingstittel = Slot(uri=ADM.stillingstittel, name="arbeidsforhold__stillingstittel", curie=ADM.curie('stillingstittel'),
                   model_uri=ADM.arbeidsforhold__stillingstittel, domain=None, range=Optional[str])

slots.arbeidsforhold__tilstedeprosent = Slot(uri=ADM.tilstedeprosent, name="arbeidsforhold__tilstedeprosent", curie=ADM.curie('tilstedeprosent'),
                   model_uri=ADM.arbeidsforhold__tilstedeprosent, domain=None, range=int)

slots.arbeidsforhold__aktivitet = Slot(uri=ADM.aktivitet, name="arbeidsforhold__aktivitet", curie=ADM.curie('aktivitet'),
                   model_uri=ADM.arbeidsforhold__aktivitet, domain=None, range=Optional[Union[str, AktivitetId]])

slots.arbeidsforhold__anlegg = Slot(uri=ADM.anlegg, name="arbeidsforhold__anlegg", curie=ADM.curie('anlegg'),
                   model_uri=ADM.arbeidsforhold__anlegg, domain=None, range=Optional[Union[str, AnleggId]])

slots.arbeidsforhold__ansvar = Slot(uri=ADM.ansvar, name="arbeidsforhold__ansvar", curie=ADM.curie('ansvar'),
                   model_uri=ADM.arbeidsforhold__ansvar, domain=None, range=Optional[Union[str, AnsvarId]])

slots.arbeidsforhold__arbeidsforholdstype = Slot(uri=ADM.arbeidsforholdstype, name="arbeidsforhold__arbeidsforholdstype", curie=ADM.curie('arbeidsforholdstype'),
                   model_uri=ADM.arbeidsforhold__arbeidsforholdstype, domain=None, range=Optional[Union[str, ArbeidsforholdstypeId]])

slots.arbeidsforhold__art = Slot(uri=ADM.art, name="arbeidsforhold__art", curie=ADM.curie('art'),
                   model_uri=ADM.arbeidsforhold__art, domain=None, range=Optional[Union[str, ArtId]])

slots.arbeidsforhold__diverse = Slot(uri=ADM.diverse, name="arbeidsforhold__diverse", curie=ADM.curie('diverse'),
                   model_uri=ADM.arbeidsforhold__diverse, domain=None, range=Optional[Union[str, DiverseId]])

slots.arbeidsforhold__formaal = Slot(uri=ADM.formaal, name="arbeidsforhold__formaal", curie=ADM.curie('formaal'),
                   model_uri=ADM.arbeidsforhold__formaal, domain=None, range=Optional[Union[str, FormaalId]])

slots.arbeidsforhold__funksjon = Slot(uri=ADM.funksjon, name="arbeidsforhold__funksjon", curie=ADM.curie('funksjon'),
                   model_uri=ADM.arbeidsforhold__funksjon, domain=None, range=Optional[Union[str, FunksjonId]])

slots.arbeidsforhold__kontrakt = Slot(uri=ADM.kontrakt, name="arbeidsforhold__kontrakt", curie=ADM.curie('kontrakt'),
                   model_uri=ADM.arbeidsforhold__kontrakt, domain=None, range=Optional[Union[str, KontraktId]])

slots.arbeidsforhold__lopenummer = Slot(uri=ADM.lopenummer, name="arbeidsforhold__lopenummer", curie=ADM.curie('lopenummer'),
                   model_uri=ADM.arbeidsforhold__lopenummer, domain=None, range=Optional[Union[str, LopenummerId]])

slots.arbeidsforhold__objekt = Slot(uri=ADM.objekt, name="arbeidsforhold__objekt", curie=ADM.curie('objekt'),
                   model_uri=ADM.arbeidsforhold__objekt, domain=None, range=Optional[Union[str, ObjektId]])

slots.arbeidsforhold__prosjekt = Slot(uri=ADM.prosjekt, name="arbeidsforhold__prosjekt", curie=ADM.curie('prosjekt'),
                   model_uri=ADM.arbeidsforhold__prosjekt, domain=None, range=Optional[Union[str, ProsjektId]])

slots.arbeidsforhold__ramme = Slot(uri=ADM.ramme, name="arbeidsforhold__ramme", curie=ADM.curie('ramme'),
                   model_uri=ADM.arbeidsforhold__ramme, domain=None, range=Optional[Union[str, RammeId]])

slots.arbeidsforhold__stillingskode = Slot(uri=ADM.stillingskode, name="arbeidsforhold__stillingskode", curie=ADM.curie('stillingskode'),
                   model_uri=ADM.arbeidsforhold__stillingskode, domain=None, range=Optional[Union[str, StillingskodeId]])

slots.arbeidsforhold__timerPerUke = Slot(uri=ADM.timerPerUke, name="arbeidsforhold__timerPerUke", curie=ADM.curie('timerPerUke'),
                   model_uri=ADM.arbeidsforhold__timerPerUke, domain=None, range=Optional[Union[str, UketimetallId]])

slots.arbeidsforhold__arbeidslokasjon = Slot(uri=ADM.arbeidslokasjon, name="arbeidsforhold__arbeidslokasjon", curie=ADM.curie('arbeidslokasjon'),
                   model_uri=ADM.arbeidsforhold__arbeidslokasjon, domain=None, range=Optional[Union[str, ArbeidslokasjonId]])

slots.arbeidsforhold__arbeidssted = Slot(uri=ADM.arbeidssted, name="arbeidsforhold__arbeidssted", curie=ADM.curie('arbeidssted'),
                   model_uri=ADM.arbeidsforhold__arbeidssted, domain=None, range=Union[str, OrganisasjonselementId])

slots.arbeidsforhold__fastlonn = Slot(uri=ADM.fastlonn, name="arbeidsforhold__fastlonn", curie=ADM.curie('fastlonn'),
                   model_uri=ADM.arbeidsforhold__fastlonn, domain=None, range=Optional[Union[Union[str, FastlonnId], list[Union[str, FastlonnId]]]])

slots.arbeidsforhold__fasttillegg = Slot(uri=ADM.fasttillegg, name="arbeidsforhold__fasttillegg", curie=ADM.curie('fasttillegg'),
                   model_uri=ADM.arbeidsforhold__fasttillegg, domain=None, range=Optional[Union[Union[str, FasttilleggId], list[Union[str, FasttilleggId]]]])

slots.arbeidsforhold__fravaer = Slot(uri=ADM.fravaer, name="arbeidsforhold__fravaer", curie=ADM.curie('fravaer'),
                   model_uri=ADM.arbeidsforhold__fravaer, domain=None, range=Optional[Union[Union[str, FravaerId], list[Union[str, FravaerId]]]])

slots.arbeidsforhold__variabellonn = Slot(uri=ADM.variabellonn, name="arbeidsforhold__variabellonn", curie=ADM.curie('variabellonn'),
                   model_uri=ADM.arbeidsforhold__variabellonn, domain=None, range=Optional[Union[Union[str, VariabellonnId], list[Union[str, VariabellonnId]]]])

slots.arbeidsforhold__personalressurs = Slot(uri=ADM.personalressurs, name="arbeidsforhold__personalressurs", curie=ADM.curie('personalressurs'),
                   model_uri=ADM.arbeidsforhold__personalressurs, domain=None, range=Union[str, PersonalressursId])

slots.arbeidsforhold__personalleder = Slot(uri=ADM.personalleder, name="arbeidsforhold__personalleder", curie=ADM.curie('personalleder'),
                   model_uri=ADM.arbeidsforhold__personalleder, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.arbeidsforhold__undervisningsforhold = Slot(uri=ADM.undervisningsforhold, name="arbeidsforhold__undervisningsforhold", curie=ADM.curie('undervisningsforhold'),
                   model_uri=ADM.arbeidsforhold__undervisningsforhold, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.aktoer__kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="aktoer__kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ADM.aktoer__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.aktoer__postadresse = Slot(uri=FINT.postadresse, name="aktoer__postadresse", curie=FINT.curie('postadresse'),
                   model_uri=ADM.aktoer__postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.begrep__kode = Slot(uri=FINT.kode, name="begrep__kode", curie=FINT.curie('kode'),
                   model_uri=ADM.begrep__kode, domain=None, range=str)

slots.begrep__navn = Slot(uri=FINT.navn, name="begrep__navn", curie=FINT.curie('navn'),
                   model_uri=ADM.begrep__navn, domain=None, range=str)

slots.begrep__gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="begrep__gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ADM.begrep__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.begrep__passiv = Slot(uri=FINT.passiv, name="begrep__passiv", curie=FINT.curie('passiv'),
                   model_uri=ADM.begrep__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.enhet__forretningsadresse = Slot(uri=FINT.forretningsadresse, name="enhet__forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=ADM.enhet__forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.enhet__organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="enhet__organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=ADM.enhet__organisasjonsnavn, domain=None, range=Optional[str])

slots.enhet__organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="enhet__organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=ADM.enhet__organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.identifikator__identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="identifikator__identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=ADM.identifikator__identifikatorverdi, domain=None, range=str)

slots.identifikator__gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="identifikator__gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ADM.identifikator__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.periode__beskrivelse = Slot(uri=FINT.beskrivelse, name="periode__beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=ADM.periode__beskrivelse, domain=None, range=Optional[str])

slots.periode__start = Slot(uri=FINT.start, name="periode__start", curie=FINT.curie('start'),
                   model_uri=ADM.periode__start, domain=None, range=Union[str, XSDDateTime])

slots.periode__slutt = Slot(uri=FINT.slutt, name="periode__slutt", curie=FINT.curie('slutt'),
                   model_uri=ADM.periode__slutt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.personnavn__fornavn = Slot(uri=FINT.fornavn, name="personnavn__fornavn", curie=FINT.curie('fornavn'),
                   model_uri=ADM.personnavn__fornavn, domain=None, range=str)

slots.personnavn__mellomnavn = Slot(uri=FINT.mellomnavn, name="personnavn__mellomnavn", curie=FINT.curie('mellomnavn'),
                   model_uri=ADM.personnavn__mellomnavn, domain=None, range=Optional[str])

slots.personnavn__etternavn = Slot(uri=FINT.etternavn, name="personnavn__etternavn", curie=FINT.curie('etternavn'),
                   model_uri=ADM.personnavn__etternavn, domain=None, range=str)

slots.kontaktinformasjon__epostadresse = Slot(uri=FINT.epostadresse, name="kontaktinformasjon__epostadresse", curie=FINT.curie('epostadresse'),
                   model_uri=ADM.kontaktinformasjon__epostadresse, domain=None, range=Optional[str])

slots.kontaktinformasjon__mobiltelefonnummer = Slot(uri=FINT.mobiltelefonnummer, name="kontaktinformasjon__mobiltelefonnummer", curie=FINT.curie('mobiltelefonnummer'),
                   model_uri=ADM.kontaktinformasjon__mobiltelefonnummer, domain=None, range=Optional[str])

slots.kontaktinformasjon__nettsted = Slot(uri=FINT.nettsted, name="kontaktinformasjon__nettsted", curie=FINT.curie('nettsted'),
                   model_uri=ADM.kontaktinformasjon__nettsted, domain=None, range=Optional[str])

slots.kontaktinformasjon__sip = Slot(uri=FINT.sip, name="kontaktinformasjon__sip", curie=FINT.curie('sip'),
                   model_uri=ADM.kontaktinformasjon__sip, domain=None, range=Optional[str])

slots.kontaktinformasjon__telefonnummer = Slot(uri=FINT.telefonnummer, name="kontaktinformasjon__telefonnummer", curie=FINT.curie('telefonnummer'),
                   model_uri=ADM.kontaktinformasjon__telefonnummer, domain=None, range=Optional[str])

slots.adresse__adresselinje = Slot(uri=FINT.adresselinje, name="adresse__adresselinje", curie=FINT.curie('adresselinje'),
                   model_uri=ADM.adresse__adresselinje, domain=None, range=Optional[Union[str, list[str]]])

slots.adresse__postnummer = Slot(uri=FINT.postnummer, name="adresse__postnummer", curie=FINT.curie('postnummer'),
                   model_uri=ADM.adresse__postnummer, domain=None, range=Optional[str])

slots.adresse__poststed = Slot(uri=FINT.poststed, name="adresse__poststed", curie=FINT.curie('poststed'),
                   model_uri=ADM.adresse__poststed, domain=None, range=Optional[str])

slots.adresse__land = Slot(uri=FINT.land, name="adresse__land", curie=FINT.curie('land'),
                   model_uri=ADM.adresse__land, domain=None, range=Optional[Union[str, LandkodeId]])

slots.matrikkelnummer__adresse = Slot(uri=FINT.adresse, name="matrikkelnummer__adresse", curie=FINT.curie('adresse'),
                   model_uri=ADM.matrikkelnummer__adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.matrikkelnummer__bruksnummer = Slot(uri=FINT.bruksnummer, name="matrikkelnummer__bruksnummer", curie=FINT.curie('bruksnummer'),
                   model_uri=ADM.matrikkelnummer__bruksnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__festenummer = Slot(uri=FINT.festenummer, name="matrikkelnummer__festenummer", curie=FINT.curie('festenummer'),
                   model_uri=ADM.matrikkelnummer__festenummer, domain=None, range=Optional[str])

slots.matrikkelnummer__gaardsnummer = Slot(uri=FINT.gaardsnummer, name="matrikkelnummer__gaardsnummer", curie=FINT.curie('gaardsnummer'),
                   model_uri=ADM.matrikkelnummer__gaardsnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__seksjonsnummer = Slot(uri=FINT.seksjonsnummer, name="matrikkelnummer__seksjonsnummer", curie=FINT.curie('seksjonsnummer'),
                   model_uri=ADM.matrikkelnummer__seksjonsnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__kommunenummer = Slot(uri=FINT.kommunenummer, name="matrikkelnummer__kommunenummer", curie=FINT.curie('kommunenummer'),
                   model_uri=ADM.matrikkelnummer__kommunenummer, domain=None, range=Optional[Union[str, KommuneId]])

slots.fylke__kommune = Slot(uri=FINT.kommune, name="fylke__kommune", curie=FINT.curie('kommune'),
                   model_uri=ADM.fylke__kommune, domain=None, range=Optional[Union[Union[str, KommuneId], list[Union[str, KommuneId]]]])

slots.kommune__fylke = Slot(uri=FINT.fylke, name="kommune__fylke", curie=FINT.curie('fylke'),
                   model_uri=ADM.kommune__fylke, domain=None, range=Union[str, FylkeId])

slots.valuta__bokstavkode = Slot(uri=FINT.bokstavkode, name="valuta__bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=ADM.valuta__bokstavkode, domain=None, range=Union[dict, Identifikator])

slots.valuta__navn = Slot(uri=FINT.valutaNavn, name="valuta__navn", curie=FINT.curie('valutaNavn'),
                   model_uri=ADM.valuta__navn, domain=None, range=str)

slots.valuta__nummerkode = Slot(uri=FINT.nummerkode, name="valuta__nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=ADM.valuta__nummerkode, domain=None, range=Union[dict, Identifikator])

slots.person__bilde = Slot(uri=FINT.bilde, name="person__bilde", curie=FINT.curie('bilde'),
                   model_uri=ADM.person__bilde, domain=None, range=Optional[str])

slots.person__bostedsadresse = Slot(uri=FINT.bostedsadresse, name="person__bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=ADM.person__bostedsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.person__fodselsdato = Slot(uri=FINT.fodselsdato, name="person__fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=ADM.person__fodselsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.person__fodselsnummer = Slot(uri=FINT.fodselsnummer, name="person__fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=ADM.person__fodselsnummer, domain=None, range=Union[dict, Identifikator])

slots.person__navn = Slot(uri=FINT.personNavn, name="person__navn", curie=FINT.curie('personNavn'),
                   model_uri=ADM.person__navn, domain=None, range=Union[dict, Personnavn])

slots.person__parorende = Slot(uri=FINT.parorende, name="person__parorende", curie=FINT.curie('parorende'),
                   model_uri=ADM.person__parorende, domain=None, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.person__statsborgerskap = Slot(uri=FINT.statsborgerskap, name="person__statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=ADM.person__statsborgerskap, domain=None, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.person__kommune = Slot(uri=FINT.kommune, name="person__kommune", curie=FINT.curie('kommune'),
                   model_uri=ADM.person__kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.person__kjonn = Slot(uri=FINT.kjonn, name="person__kjonn", curie=FINT.curie('kjonn'),
                   model_uri=ADM.person__kjonn, domain=None, range=Optional[Union[str, KjonnId]])

slots.person__foreldreansvar = Slot(uri=FINT.foreldreansvar, name="person__foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=ADM.person__foreldreansvar, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.person__foreldre = Slot(uri=FINT.foreldre, name="person__foreldre", curie=FINT.curie('foreldre'),
                   model_uri=ADM.person__foreldre, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.person__maalform = Slot(uri=FINT.maalform, name="person__maalform", curie=FINT.curie('maalform'),
                   model_uri=ADM.person__maalform, domain=None, range=Optional[Union[str, SpraakId]])

slots.person__personalressurs = Slot(uri=FINT.personalressurs, name="person__personalressurs", curie=FINT.curie('personalressurs'),
                   model_uri=ADM.person__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.person__morsmaal = Slot(uri=FINT.morsmaal, name="person__morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=ADM.person__morsmaal, domain=None, range=Optional[Union[str, SpraakId]])

slots.person__laerling = Slot(uri=FINT.laerling, name="person__laerling", curie=FINT.curie('laerling'),
                   model_uri=ADM.person__laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.person__elev = Slot(uri=FINT.elev, name="person__elev", curie=FINT.curie('elev'),
                   model_uri=ADM.person__elev, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.person__otungdom = Slot(uri=FINT.otungdom, name="person__otungdom", curie=FINT.curie('otungdom'),
                   model_uri=ADM.person__otungdom, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kontaktperson__kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="kontaktperson__kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ADM.kontaktperson__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.kontaktperson__navn = Slot(uri=FINT.kontaktpersonNavn, name="kontaktperson__navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=ADM.kontaktperson__navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.kontaktperson__type = Slot(uri=FINT.type, name="kontaktperson__type", curie=FINT.curie('type'),
                   model_uri=ADM.kontaktperson__type, domain=None, range=str)

slots.kontaktperson__kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="kontaktperson__kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=ADM.kontaktperson__kontaktperson, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.virksomhet__virksomhetsId = Slot(uri=FINT.virksomhetsId, name="virksomhet__virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=ADM.virksomhet__virksomhetsId, domain=None, range=Union[dict, Identifikator])

slots.virksomhet__laerling = Slot(uri=FINT.laerling, name="virksomhet__laerling", curie=FINT.curie('laerling'),
                   model_uri=ADM.virksomhet__laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

