# Auto generated from fint-administrasjon-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-27T14:51:45
# Schema: fint-administrasjon
#
# id: https://data.norge.no/fint/fint-administrasjon
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

metamodel_version = "1.11.0"
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
    kjonn: Optional[str] = None
    fylke: Optional[str] = None
    kommunar: Optional[Union[dict[Union[str, KommuneId], Union[dict, "Kommune"]], list[Union[dict, "Kommune"]]]] = empty_dict()
    spraak: Optional[Union[dict[Union[str, SpraakId], Union[dict, "Spraak"]], list[Union[dict, "Spraak"]]]] = empty_dict()
    valuta: Optional[Union[dict[Union[str, ValutaId], Union[dict, "Valuta"]], list[Union[dict, "Valuta"]]]] = empty_dict()
    personalressursar: Optional[Union[dict[Union[str, PersonalressursId], Union[dict, "Personalressurs"]], list[Union[dict, "Personalressurs"]]]] = empty_dict()
    arbeidsforhold: Optional[Union[str, ArbeidsforholdId]] = None
    arbeidslokasjoner: Optional[Union[dict[Union[str, ArbeidslokasjonId], Union[dict, "Arbeidslokasjon"]], list[Union[dict, "Arbeidslokasjon"]]]] = empty_dict()
    fastlonn: Optional[Union[str, FastlonnId]] = None
    fasttillegg: Optional[Union[str, FasttilleggId]] = None
    fravaer: Optional[Union[str, FravaerId]] = None
    fullmakter: Optional[Union[dict[Union[str, FullmaktId], Union[dict, "Fullmakt"]], list[Union[dict, "Fullmakt"]]]] = empty_dict()
    organisasjonselement: Optional[Union[str, OrganisasjonselementId]] = None
    rollar: Optional[Union[dict[Union[str, RolleId], Union[dict, "Rolle"]], list[Union[dict, "Rolle"]]]] = empty_dict()
    variabellonn: Optional[Union[str, VariabellonnId]] = None
    aktivitetar: Optional[Union[dict[Union[str, AktivitetId], Union[dict, "Aktivitet"]], list[Union[dict, "Aktivitet"]]]] = empty_dict()
    anlegg: Optional[Union[str, AnleggId]] = None
    ansvar: Optional[Union[str, AnsvarId]] = None
    artar: Optional[Union[dict[Union[str, ArtId], Union[dict, "Art"]], list[Union[dict, "Art"]]]] = empty_dict()
    arbeidsforholdstypar: Optional[Union[dict[Union[str, ArbeidsforholdstypeId], Union[dict, "Arbeidsforholdstype"]], list[Union[dict, "Arbeidsforholdstype"]]]] = empty_dict()
    diverse: Optional[Union[str, DiverseId]] = None
    formaal: Optional[Union[str, FormaalId]] = None
    fravaersgrunnar: Optional[Union[dict[Union[str, FravaersgrunnId], Union[dict, "Fravaersgrunn"]], list[Union[dict, "Fravaersgrunn"]]]] = empty_dict()
    fravaerstypar: Optional[Union[dict[Union[str, FravaerstypeId], Union[dict, "Fravaerstype"]], list[Union[dict, "Fravaerstype"]]]] = empty_dict()
    funksjonar: Optional[Union[dict[Union[str, FunksjonId], Union[dict, "Funksjon"]], list[Union[dict, "Funksjon"]]]] = empty_dict()
    kontrakter: Optional[Union[dict[Union[str, KontraktId], Union[dict, "Kontrakt"]], list[Union[dict, "Kontrakt"]]]] = empty_dict()
    lonsartar: Optional[Union[dict[Union[str, LonsartId], Union[dict, "Lonsart"]], list[Union[dict, "Lonsart"]]]] = empty_dict()
    lopenummer: Optional[Union[str, LopenummerId]] = None
    objekt: Optional[Union[str, ObjektId]] = None
    organisasjonstypar: Optional[Union[dict[Union[str, OrganisasjonstypeId], Union[dict, "Organisasjonstype"]], list[Union[dict, "Organisasjonstype"]]]] = empty_dict()
    personalressurskategoriar: Optional[Union[dict[Union[str, PersonalressurskategoriId], Union[dict, "Personalressurskategori"]], list[Union[dict, "Personalressurskategori"]]]] = empty_dict()
    prosjekt: Optional[Union[str, ProsjektId]] = None
    prosjektartar: Optional[Union[dict[Union[str, ProsjektartId], Union[dict, "Prosjektart"]], list[Union[dict, "Prosjektart"]]]] = empty_dict()
    rammer: Optional[Union[dict[Union[str, RammeId], Union[dict, "Ramme"]], list[Union[dict, "Ramme"]]]] = empty_dict()
    stillingskoder: Optional[Union[dict[Union[str, StillingskodeId], Union[dict, "Stillingskode"]], list[Union[dict, "Stillingskode"]]]] = empty_dict()
    uketimetall: Optional[Union[dict[Union[str, UketimetallId], Union[dict, "Uketimetall"]], list[Union[dict, "Uketimetall"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="personar", slot_type=Person, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kontaktpersonar", slot_type=Kontaktperson, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="virksomhetar", slot_type=Virksomhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="landkodar", slot_type=Landkode, key_name="id", keyed=True)

        if self.kjonn is not None and not isinstance(self.kjonn, str):
            self.kjonn = str(self.kjonn)

        if self.fylke is not None and not isinstance(self.fylke, str):
            self.fylke = str(self.fylke)

        self._normalize_inlined_as_list(slot_name="kommunar", slot_type=Kommune, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="spraak", slot_type=Spraak, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="valuta", slot_type=Valuta, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="personalressursar", slot_type=Personalressurs, key_name="id", keyed=True)

        if self.arbeidsforhold is not None and not isinstance(self.arbeidsforhold, ArbeidsforholdId):
            self.arbeidsforhold = ArbeidsforholdId(self.arbeidsforhold)

        self._normalize_inlined_as_list(slot_name="arbeidslokasjoner", slot_type=Arbeidslokasjon, key_name="id", keyed=True)

        if self.fastlonn is not None and not isinstance(self.fastlonn, FastlonnId):
            self.fastlonn = FastlonnId(self.fastlonn)

        if self.fasttillegg is not None and not isinstance(self.fasttillegg, FasttilleggId):
            self.fasttillegg = FasttilleggId(self.fasttillegg)

        if self.fravaer is not None and not isinstance(self.fravaer, FravaerId):
            self.fravaer = FravaerId(self.fravaer)

        self._normalize_inlined_as_list(slot_name="fullmakter", slot_type=Fullmakt, key_name="id", keyed=True)

        if self.organisasjonselement is not None and not isinstance(self.organisasjonselement, OrganisasjonselementId):
            self.organisasjonselement = OrganisasjonselementId(self.organisasjonselement)

        self._normalize_inlined_as_list(slot_name="rollar", slot_type=Rolle, key_name="id", keyed=True)

        if self.variabellonn is not None and not isinstance(self.variabellonn, VariabellonnId):
            self.variabellonn = VariabellonnId(self.variabellonn)

        self._normalize_inlined_as_list(slot_name="aktivitetar", slot_type=Aktivitet, key_name="id", keyed=True)

        if self.anlegg is not None and not isinstance(self.anlegg, AnleggId):
            self.anlegg = AnleggId(self.anlegg)

        if self.ansvar is not None and not isinstance(self.ansvar, AnsvarId):
            self.ansvar = AnsvarId(self.ansvar)

        self._normalize_inlined_as_list(slot_name="artar", slot_type=Art, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="arbeidsforholdstypar", slot_type=Arbeidsforholdstype, key_name="id", keyed=True)

        if self.diverse is not None and not isinstance(self.diverse, DiverseId):
            self.diverse = DiverseId(self.diverse)

        if self.formaal is not None and not isinstance(self.formaal, FormaalId):
            self.formaal = FormaalId(self.formaal)

        self._normalize_inlined_as_list(slot_name="fravaersgrunnar", slot_type=Fravaersgrunn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fravaerstypar", slot_type=Fravaerstype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="funksjonar", slot_type=Funksjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kontrakter", slot_type=Kontrakt, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="lonsartar", slot_type=Lonsart, key_name="id", keyed=True)

        if self.lopenummer is not None and not isinstance(self.lopenummer, LopenummerId):
            self.lopenummer = LopenummerId(self.lopenummer)

        if self.objekt is not None and not isinstance(self.objekt, ObjektId):
            self.objekt = ObjektId(self.objekt)

        self._normalize_inlined_as_list(slot_name="organisasjonstypar", slot_type=Organisasjonstype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="personalressurskategoriar", slot_type=Personalressurskategori, key_name="id", keyed=True)

        if self.prosjekt is not None and not isinstance(self.prosjekt, ProsjektId):
            self.prosjekt = ProsjektId(self.prosjekt)

        self._normalize_inlined_as_list(slot_name="prosjektartar", slot_type=Prosjektart, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rammer", slot_type=Ramme, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="stillingskoder", slot_type=Stillingskode, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="uketimetall", slot_type=Uketimetall, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="arbeidsforhold", slot_type=Arbeidsforhold, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fastlonn", slot_type=Fastlonn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fasttillegg", slot_type=Fasttillegg, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fravaer", slot_type=Fravaer, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="organisasjonselement", slot_type=Organisasjonselement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="variabellonn", slot_type=Variabellonn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="anlegg", slot_type=Anlegg, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ansvar", slot_type=Ansvar, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="diverse", slot_type=Diverse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="formaal", slot_type=Formaal, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="lopenummer", slot_type=Lopenummer, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="objekt", slot_type=Objekt, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="prosjekt", slot_type=Prosjekt, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kjonn", slot_type=Kjonn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fylke", slot_type=Fylke, key_name="id", keyed=True)

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
class Elev(YAMLRoot):
    """
    Ein elev registrert i skulesystemet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Elev"]
    class_class_curie: ClassVar[str] = "fint:Elev"
    class_name: ClassVar[str] = "Elev"
    class_model_uri: ClassVar[URIRef] = ADM.Elev

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
    class_model_uri: ClassVar[URIRef] = ADM.Person

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
    class_model_uri: ClassVar[URIRef] = ADM.Kontaktperson

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

slots.anvist = Slot(uri=ADM.anvist, name="anvist", curie=ADM.curie('anvist'),
                   model_uri=ADM.anvist, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.attestert = Slot(uri=ADM.attestert, name="attestert", curie=ADM.curie('attestert'),
                   model_uri=ADM.attestert, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.kildesystemId = Slot(uri=ADM.kildesystemId, name="kildesystemId", curie=ADM.curie('kildesystemId'),
                   model_uri=ADM.kildesystemId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.kontert = Slot(uri=ADM.kontert, name="kontert", curie=ADM.curie('kontert'),
                   model_uri=ADM.kontert, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.kontostreng = Slot(uri=ADM.kontostreng, name="kontostreng", curie=ADM.curie('kontostreng'),
                   model_uri=ADM.kontostreng, domain=None, range=Optional[Union[dict, Kontostreng]])

slots.opptjent = Slot(uri=ADM.opptjent, name="opptjent", curie=ADM.curie('opptjent'),
                   model_uri=ADM.opptjent, domain=None, range=Optional[Union[dict, Periode]])

slots.periode = Slot(uri=ADM.periode, name="periode", curie=ADM.curie('periode'),
                   model_uri=ADM.periode, domain=None, range=Optional[Union[dict, Periode]])

slots.anviser = Slot(uri=ADM.anviser, name="anviser", curie=ADM.curie('anviser'),
                   model_uri=ADM.anviser, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.konterer = Slot(uri=ADM.konterer, name="konterer", curie=ADM.curie('konterer'),
                   model_uri=ADM.konterer, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.attestant = Slot(uri=ADM.attestant, name="attestant", curie=ADM.curie('attestant'),
                   model_uri=ADM.attestant, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.prosent = Slot(uri=ADM.prosent, name="prosent", curie=ADM.curie('prosent'),
                   model_uri=ADM.prosent, domain=None, range=Optional[int])

slots.antall = Slot(uri=ADM.antall, name="antall", curie=ADM.curie('antall'),
                   model_uri=ADM.antall, domain=None, range=Optional[int])

slots.belop = Slot(uri=ADM.belop, name="belop", curie=ADM.curie('belop'),
                   model_uri=ADM.belop, domain=None, range=Optional[int])

slots.lonsart = Slot(uri=ADM.lonsart, name="lonsart", curie=ADM.curie('lonsart'),
                   model_uri=ADM.lonsart, domain=None, range=Optional[Union[str, LonsartId]])

slots.aktivitet = Slot(uri=ADM.aktivitet, name="aktivitet", curie=ADM.curie('aktivitet'),
                   model_uri=ADM.aktivitet, domain=None, range=Optional[Union[str, AktivitetId]])

slots.anlegg = Slot(uri=ADM.anlegg, name="anlegg", curie=ADM.curie('anlegg'),
                   model_uri=ADM.anlegg, domain=None, range=Optional[Union[str, AnleggId]])

slots.ansvar = Slot(uri=ADM.ansvar, name="ansvar", curie=ADM.curie('ansvar'),
                   model_uri=ADM.ansvar, domain=None, range=Optional[Union[str, AnsvarId]])

slots.art = Slot(uri=ADM.art, name="art", curie=ADM.curie('art'),
                   model_uri=ADM.art, domain=None, range=Optional[Union[str, ArtId]])

slots.diverse = Slot(uri=ADM.diverse, name="diverse", curie=ADM.curie('diverse'),
                   model_uri=ADM.diverse, domain=None, range=Optional[Union[str, DiverseId]])

slots.formaal = Slot(uri=ADM.formaal, name="formaal", curie=ADM.curie('formaal'),
                   model_uri=ADM.formaal, domain=None, range=Optional[Union[str, FormaalId]])

slots.funksjon = Slot(uri=ADM.funksjon, name="funksjon", curie=ADM.curie('funksjon'),
                   model_uri=ADM.funksjon, domain=None, range=Optional[Union[str, FunksjonId]])

slots.kontrakt = Slot(uri=ADM.kontrakt, name="kontrakt", curie=ADM.curie('kontrakt'),
                   model_uri=ADM.kontrakt, domain=None, range=Optional[Union[str, KontraktId]])

slots.lopenummer = Slot(uri=ADM.lopenummer, name="lopenummer", curie=ADM.curie('lopenummer'),
                   model_uri=ADM.lopenummer, domain=None, range=Optional[Union[str, LopenummerId]])

slots.objekt = Slot(uri=ADM.objekt, name="objekt", curie=ADM.curie('objekt'),
                   model_uri=ADM.objekt, domain=None, range=Optional[Union[str, ObjektId]])

slots.prosjekt = Slot(uri=ADM.prosjekt, name="prosjekt", curie=ADM.curie('prosjekt'),
                   model_uri=ADM.prosjekt, domain=None, range=Optional[Union[str, ProsjektId]])

slots.prosjektart = Slot(uri=ADM.prosjektart, name="prosjektart", curie=ADM.curie('prosjektart'),
                   model_uri=ADM.prosjektart, domain=None, range=Optional[Union[str, ProsjektartId]])

slots.ramme = Slot(uri=ADM.ramme, name="ramme", curie=ADM.curie('ramme'),
                   model_uri=ADM.ramme, domain=None, range=Optional[Union[str, RammeId]])

slots.overordnet = Slot(uri=ADM.overordnet, name="overordnet", curie=ADM.curie('overordnet'),
                   model_uri=ADM.overordnet, domain=None, range=Optional[str])

slots.underordnet = Slot(uri=ADM.underordnet, name="underordnet", curie=ADM.curie('underordnet'),
                   model_uri=ADM.underordnet, domain=None, range=Optional[Union[str, list[str]]])

slots.forelder = Slot(uri=ADM.forelder, name="forelder", curie=ADM.curie('forelder'),
                   model_uri=ADM.forelder, domain=None, range=Optional[str])

slots.overfores = Slot(uri=ADM.overfores, name="overfores", curie=ADM.curie('overfores'),
                   model_uri=ADM.overfores, domain=None, range=Optional[Union[bool, Bool]])

slots.kategori = Slot(uri=ADM.kategori, name="kategori", curie=ADM.curie('kategori'),
                   model_uri=ADM.kategori, domain=None, range=Optional[str])

slots.godkjent = Slot(uri=ADM.godkjent, name="godkjent", curie=ADM.curie('godkjent'),
                   model_uri=ADM.godkjent, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.fravaersgrunn = Slot(uri=ADM.fravaersgrunn, name="fravaersgrunn", curie=ADM.curie('fravaersgrunn'),
                   model_uri=ADM.fravaersgrunn, domain=None, range=Optional[Union[str, FravaersgrunnId]])

slots.fravaerstype = Slot(uri=ADM.fravaerstype, name="fravaerstype", curie=ADM.curie('fravaerstype'),
                   model_uri=ADM.fravaerstype, domain=None, range=Optional[Union[str, FravaerstypeId]])

slots.fortsettelse = Slot(uri=ADM.fortsettelse, name="fortsettelse", curie=ADM.curie('fortsettelse'),
                   model_uri=ADM.fortsettelse, domain=None, range=Optional[Union[str, FravaerId]])

slots.fortsetter = Slot(uri=ADM.fortsetter, name="fortsetter", curie=ADM.curie('fortsetter'),
                   model_uri=ADM.fortsetter, domain=None, range=Optional[Union[str, FravaerId]])

slots.godkjenner = Slot(uri=ADM.godkjenner, name="godkjenner", curie=ADM.curie('godkjenner'),
                   model_uri=ADM.godkjenner, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.rolle = Slot(uri=ADM.rolle, name="rolle", curie=ADM.curie('rolle'),
                   model_uri=ADM.rolle, domain=None, range=Optional[Union[str, RolleId]])

slots.rolleNavn = Slot(uri=ADM.rolleNavn, name="rolleNavn", curie=ADM.curie('rolleNavn'),
                   model_uri=ADM.rolleNavn, domain=None, range=Optional[Union[dict, Identifikator]])

slots.fullmakt = Slot(uri=ADM.fullmakt, name="fullmakt", curie=ADM.curie('fullmakt'),
                   model_uri=ADM.fullmakt, domain=None, range=Optional[Union[str, FullmaktId]])

slots.fullmektig = Slot(uri=ADM.fullmektig, name="fullmektig", curie=ADM.curie('fullmektig'),
                   model_uri=ADM.fullmektig, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.stedfortreder = Slot(uri=ADM.stedfortreder, name="stedfortreder", curie=ADM.curie('stedfortreder'),
                   model_uri=ADM.stedfortreder, domain=None, range=Optional[str])

slots.organisasjonselement = Slot(uri=ADM.organisasjonselement, name="organisasjonselement", curie=ADM.curie('organisasjonselement'),
                   model_uri=ADM.organisasjonselement, domain=None, range=Optional[Union[str, OrganisasjonselementId]])

slots.lokasjonskode = Slot(uri=ADM.lokasjonskode, name="lokasjonskode", curie=ADM.curie('lokasjonskode'),
                   model_uri=ADM.lokasjonskode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.lokasjonsnavn = Slot(uri=ADM.lokasjonsnavn, name="lokasjonsnavn", curie=ADM.curie('lokasjonsnavn'),
                   model_uri=ADM.lokasjonsnavn, domain=None, range=Optional[str])

slots.kortnavn = Slot(uri=ADM.kortnavn, name="kortnavn", curie=ADM.curie('kortnavn'),
                   model_uri=ADM.kortnavn, domain=None, range=Optional[str])

slots.organisasjonsId = Slot(uri=ADM.organisasjonsId, name="organisasjonsId", curie=ADM.curie('organisasjonsId'),
                   model_uri=ADM.organisasjonsId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.organisasjonsKode = Slot(uri=ADM.organisasjonsKode, name="organisasjonsKode", curie=ADM.curie('organisasjonsKode'),
                   model_uri=ADM.organisasjonsKode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.organisasjonstype = Slot(uri=ADM.organisasjonstype, name="organisasjonstype", curie=ADM.curie('organisasjonstype'),
                   model_uri=ADM.organisasjonstype, domain=None, range=Optional[Union[str, OrganisasjonstypeId]])

slots.leder = Slot(uri=ADM.leder, name="leder", curie=ADM.curie('leder'),
                   model_uri=ADM.leder, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.skole = Slot(uri=ADM.skole, name="skole", curie=ADM.curie('skole'),
                   model_uri=ADM.skole, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.ansattnummer = Slot(uri=ADM.ansattnummer, name="ansattnummer", curie=ADM.curie('ansattnummer'),
                   model_uri=ADM.ansattnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.ansettelsesperiode = Slot(uri=ADM.ansettelsesperiode, name="ansettelsesperiode", curie=ADM.curie('ansettelsesperiode'),
                   model_uri=ADM.ansettelsesperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.ansiennitet = Slot(uri=ADM.ansiennitet, name="ansiennitet", curie=ADM.curie('ansiennitet'),
                   model_uri=ADM.ansiennitet, domain=None, range=Optional[Union[str, XSDDate]])

slots.brukernavn = Slot(uri=ADM.brukernavn, name="brukernavn", curie=ADM.curie('brukernavn'),
                   model_uri=ADM.brukernavn, domain=None, range=Optional[Union[dict, Identifikator]])

slots.jobbtittel = Slot(uri=ADM.jobbtittel, name="jobbtittel", curie=ADM.curie('jobbtittel'),
                   model_uri=ADM.jobbtittel, domain=None, range=Optional[str])

slots.personalressurskategori = Slot(uri=ADM.personalressurskategori, name="personalressurskategori", curie=ADM.curie('personalressurskategori'),
                   model_uri=ADM.personalressurskategori, domain=None, range=Optional[Union[str, PersonalressurskategoriId]])

slots.lederFor = Slot(uri=ADM.lederFor, name="lederFor", curie=ADM.curie('lederFor'),
                   model_uri=ADM.lederFor, domain=None, range=Optional[Union[Union[str, OrganisasjonselementId], list[Union[str, OrganisasjonselementId]]]])

slots.personalansvar = Slot(uri=ADM.personalansvar, name="personalansvar", curie=ADM.curie('personalansvar'),
                   model_uri=ADM.personalansvar, domain=None, range=Optional[Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]]])

slots.skoleressurs = Slot(uri=ADM.skoleressurs, name="skoleressurs", curie=ADM.curie('skoleressurs'),
                   model_uri=ADM.skoleressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.ansettelsesprosent = Slot(uri=ADM.ansettelsesprosent, name="ansettelsesprosent", curie=ADM.curie('ansettelsesprosent'),
                   model_uri=ADM.ansettelsesprosent, domain=None, range=Optional[int])

slots.arbeidsforholdsperiode = Slot(uri=ADM.arbeidsforholdsperiode, name="arbeidsforholdsperiode", curie=ADM.curie('arbeidsforholdsperiode'),
                   model_uri=ADM.arbeidsforholdsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.aarslonn = Slot(uri=ADM.aarslonn, name="aarslonn", curie=ADM.curie('aarslonn'),
                   model_uri=ADM.aarslonn, domain=None, range=Optional[int])

slots.hovedstilling = Slot(uri=ADM.hovedstilling, name="hovedstilling", curie=ADM.curie('hovedstilling'),
                   model_uri=ADM.hovedstilling, domain=None, range=Optional[Union[bool, Bool]])

slots.lonnsprosent = Slot(uri=ADM.lonnsprosent, name="lonnsprosent", curie=ADM.curie('lonnsprosent'),
                   model_uri=ADM.lonnsprosent, domain=None, range=Optional[int])

slots.stillingsnummer = Slot(uri=ADM.stillingsnummer, name="stillingsnummer", curie=ADM.curie('stillingsnummer'),
                   model_uri=ADM.stillingsnummer, domain=None, range=Optional[str])

slots.stillingstittel = Slot(uri=ADM.stillingstittel, name="stillingstittel", curie=ADM.curie('stillingstittel'),
                   model_uri=ADM.stillingstittel, domain=None, range=Optional[str])

slots.tilstedeprosent = Slot(uri=ADM.tilstedeprosent, name="tilstedeprosent", curie=ADM.curie('tilstedeprosent'),
                   model_uri=ADM.tilstedeprosent, domain=None, range=Optional[int])

slots.arbeidsforholdstype = Slot(uri=ADM.arbeidsforholdstype, name="arbeidsforholdstype", curie=ADM.curie('arbeidsforholdstype'),
                   model_uri=ADM.arbeidsforholdstype, domain=None, range=Optional[Union[str, ArbeidsforholdstypeId]])

slots.stillingskode = Slot(uri=ADM.stillingskode, name="stillingskode", curie=ADM.curie('stillingskode'),
                   model_uri=ADM.stillingskode, domain=None, range=Optional[Union[str, StillingskodeId]])

slots.timerPerUke = Slot(uri=ADM.timerPerUke, name="timerPerUke", curie=ADM.curie('timerPerUke'),
                   model_uri=ADM.timerPerUke, domain=None, range=Optional[Union[str, UketimetallId]])

slots.arbeidslokasjon = Slot(uri=ADM.arbeidslokasjon, name="arbeidslokasjon", curie=ADM.curie('arbeidslokasjon'),
                   model_uri=ADM.arbeidslokasjon, domain=None, range=Optional[Union[str, ArbeidslokasjonId]])

slots.arbeidssted = Slot(uri=ADM.arbeidssted, name="arbeidssted", curie=ADM.curie('arbeidssted'),
                   model_uri=ADM.arbeidssted, domain=None, range=Optional[Union[str, OrganisasjonselementId]])

slots.arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.arbeidsforhold, domain=None, range=Optional[Union[str, ArbeidsforholdId]])

slots.fastlonn = Slot(uri=ADM.fastlonn, name="fastlonn", curie=ADM.curie('fastlonn'),
                   model_uri=ADM.fastlonn, domain=None, range=Optional[Union[str, FastlonnId]])

slots.fasttillegg = Slot(uri=ADM.fasttillegg, name="fasttillegg", curie=ADM.curie('fasttillegg'),
                   model_uri=ADM.fasttillegg, domain=None, range=Optional[Union[str, FasttilleggId]])

slots.fravaer = Slot(uri=ADM.fravaer, name="fravaer", curie=ADM.curie('fravaer'),
                   model_uri=ADM.fravaer, domain=None, range=Optional[Union[str, FravaerId]])

slots.variabellonn = Slot(uri=ADM.variabellonn, name="variabellonn", curie=ADM.curie('variabellonn'),
                   model_uri=ADM.variabellonn, domain=None, range=Optional[Union[str, VariabellonnId]])

slots.personalressurs = Slot(uri=ADM.personalressurs, name="personalressurs", curie=ADM.curie('personalressurs'),
                   model_uri=ADM.personalressurs, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.personalleder = Slot(uri=ADM.personalleder, name="personalleder", curie=ADM.curie('personalleder'),
                   model_uri=ADM.personalleder, domain=None, range=Optional[Union[str, PersonalressursId]])

slots.undervisningsforhold = Slot(uri=ADM.undervisningsforhold, name="undervisningsforhold", curie=ADM.curie('undervisningsforhold'),
                   model_uri=ADM.undervisningsforhold, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.id = Slot(uri=FINT.id, name="id", curie=FINT.curie('id'),
                   model_uri=ADM.id, domain=None, range=URIRef)

slots.gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ADM.gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ADM.kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.postadresse = Slot(uri=FINT.postadresse, name="postadresse", curie=FINT.curie('postadresse'),
                   model_uri=ADM.postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.forretningsadresse = Slot(uri=FINT.forretningsadresse, name="forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=ADM.forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=ADM.organisasjonsnavn, domain=None, range=Optional[str])

slots.organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=ADM.organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.kode = Slot(uri=FINT.kode, name="kode", curie=FINT.curie('kode'),
                   model_uri=ADM.kode, domain=None, range=Optional[str])

slots.navn = Slot(uri=FINT.navn, name="navn", curie=FINT.curie('navn'),
                   model_uri=ADM.navn, domain=None, range=Optional[str])

slots.passiv = Slot(uri=FINT.passiv, name="passiv", curie=FINT.curie('passiv'),
                   model_uri=ADM.passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=ADM.identifikatorverdi, domain=None, range=Optional[str])

slots.beskrivelse = Slot(uri=FINT.beskrivelse, name="beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=ADM.beskrivelse, domain=None, range=Optional[str])

slots.start = Slot(uri=FINT.start, name="start", curie=FINT.curie('start'),
                   model_uri=ADM.start, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.slutt = Slot(uri=FINT.slutt, name="slutt", curie=FINT.curie('slutt'),
                   model_uri=ADM.slutt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.fornavn = Slot(uri=FINT.fornavn, name="fornavn", curie=FINT.curie('fornavn'),
                   model_uri=ADM.fornavn, domain=None, range=Optional[str])

slots.mellomnavn = Slot(uri=FINT.mellomnavn, name="mellomnavn", curie=FINT.curie('mellomnavn'),
                   model_uri=ADM.mellomnavn, domain=None, range=Optional[str])

slots.etternavn = Slot(uri=FINT.etternavn, name="etternavn", curie=FINT.curie('etternavn'),
                   model_uri=ADM.etternavn, domain=None, range=Optional[str])

slots.epostadresse = Slot(uri=FINT.epostadresse, name="epostadresse", curie=FINT.curie('epostadresse'),
                   model_uri=ADM.epostadresse, domain=None, range=Optional[str])

slots.mobiltelefonnummer = Slot(uri=FINT.mobiltelefonnummer, name="mobiltelefonnummer", curie=FINT.curie('mobiltelefonnummer'),
                   model_uri=ADM.mobiltelefonnummer, domain=None, range=Optional[str])

slots.nettsted = Slot(uri=FINT.nettsted, name="nettsted", curie=FINT.curie('nettsted'),
                   model_uri=ADM.nettsted, domain=None, range=Optional[str])

slots.sip = Slot(uri=FINT.sip, name="sip", curie=FINT.curie('sip'),
                   model_uri=ADM.sip, domain=None, range=Optional[str])

slots.telefonnummer = Slot(uri=FINT.telefonnummer, name="telefonnummer", curie=FINT.curie('telefonnummer'),
                   model_uri=ADM.telefonnummer, domain=None, range=Optional[str])

slots.adresselinje = Slot(uri=FINT.adresselinje, name="adresselinje", curie=FINT.curie('adresselinje'),
                   model_uri=ADM.adresselinje, domain=None, range=Optional[Union[str, list[str]]])

slots.postnummer = Slot(uri=FINT.postnummer, name="postnummer", curie=FINT.curie('postnummer'),
                   model_uri=ADM.postnummer, domain=None, range=Optional[str])

slots.poststed = Slot(uri=FINT.poststed, name="poststed", curie=FINT.curie('poststed'),
                   model_uri=ADM.poststed, domain=None, range=Optional[str])

slots.land = Slot(uri=FINT.land, name="land", curie=FINT.curie('land'),
                   model_uri=ADM.land, domain=None, range=Optional[Union[str, LandkodeId]])

slots.adresse = Slot(uri=FINT.adresse, name="adresse", curie=FINT.curie('adresse'),
                   model_uri=ADM.adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.bruksnummer = Slot(uri=FINT.bruksnummer, name="bruksnummer", curie=FINT.curie('bruksnummer'),
                   model_uri=ADM.bruksnummer, domain=None, range=Optional[str])

slots.festenummer = Slot(uri=FINT.festenummer, name="festenummer", curie=FINT.curie('festenummer'),
                   model_uri=ADM.festenummer, domain=None, range=Optional[str])

slots.gaardsnummer = Slot(uri=FINT.gaardsnummer, name="gaardsnummer", curie=FINT.curie('gaardsnummer'),
                   model_uri=ADM.gaardsnummer, domain=None, range=Optional[str])

slots.seksjonsnummer = Slot(uri=FINT.seksjonsnummer, name="seksjonsnummer", curie=FINT.curie('seksjonsnummer'),
                   model_uri=ADM.seksjonsnummer, domain=None, range=Optional[str])

slots.kommunenummer = Slot(uri=FINT.kommunenummer, name="kommunenummer", curie=FINT.curie('kommunenummer'),
                   model_uri=ADM.kommunenummer, domain=None, range=Optional[Union[str, KommuneId]])

slots.fylke = Slot(uri=FINT.fylke, name="fylke", curie=FINT.curie('fylke'),
                   model_uri=ADM.fylke, domain=None, range=Optional[Union[str, FylkeId]])

slots.kommune = Slot(uri=FINT.kommune, name="kommune", curie=FINT.curie('kommune'),
                   model_uri=ADM.kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.kjonn = Slot(uri=FINT.kjonn, name="kjonn", curie=FINT.curie('kjonn'),
                   model_uri=ADM.kjonn, domain=None, range=Optional[Union[str, KjonnId]])

slots.bokstavkode = Slot(uri=FINT.bokstavkode, name="bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=ADM.bokstavkode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.valuta_navn = Slot(uri=FINT.valutaNavn, name="valuta_navn", curie=FINT.curie('valutaNavn'),
                   model_uri=ADM.valuta_navn, domain=None, range=Optional[str])

slots.nummerkode = Slot(uri=FINT.nummerkode, name="nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=ADM.nummerkode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.bilde = Slot(uri=FINT.bilde, name="bilde", curie=FINT.curie('bilde'),
                   model_uri=ADM.bilde, domain=None, range=Optional[str])

slots.bostedsadresse = Slot(uri=FINT.bostedsadresse, name="bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=ADM.bostedsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.fodselsdato = Slot(uri=FINT.fodselsdato, name="fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=ADM.fodselsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.fodselsnummer = Slot(uri=FINT.fodselsnummer, name="fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=ADM.fodselsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person_navn = Slot(uri=FINT.personNavn, name="person_navn", curie=FINT.curie('personNavn'),
                   model_uri=ADM.person_navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.parorende = Slot(uri=FINT.parorende, name="parorende", curie=FINT.curie('parorende'),
                   model_uri=ADM.parorende, domain=None, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.statsborgerskap = Slot(uri=FINT.statsborgerskap, name="statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=ADM.statsborgerskap, domain=None, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.foreldreansvar = Slot(uri=FINT.foreldreansvar, name="foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=ADM.foreldreansvar, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.foreldre = Slot(uri=FINT.foreldre, name="foreldre", curie=FINT.curie('foreldre'),
                   model_uri=ADM.foreldre, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.maalform = Slot(uri=FINT.maalform, name="maalform", curie=FINT.curie('maalform'),
                   model_uri=ADM.maalform, domain=None, range=Optional[Union[str, SpraakId]])

slots.morsmaal = Slot(uri=FINT.morsmaal, name="morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=ADM.morsmaal, domain=None, range=Optional[Union[str, SpraakId]])

slots.laerling = Slot(uri=FINT.laerling, name="laerling", curie=FINT.curie('laerling'),
                   model_uri=ADM.laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.elev = Slot(uri=FINT.elev, name="elev", curie=FINT.curie('elev'),
                   model_uri=ADM.elev, domain=None, range=Optional[Union[str, ElevId]])

slots.elevnummer = Slot(uri=FINT.elevnummer, name="elevnummer", curie=FINT.curie('elevnummer'),
                   model_uri=ADM.elevnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person = Slot(uri=FINT.person, name="person", curie=FINT.curie('person'),
                   model_uri=ADM.person, domain=None, range=Optional[Union[str, PersonId]])

slots.otungdom = Slot(uri=FINT.otungdom, name="otungdom", curie=FINT.curie('otungdom'),
                   model_uri=ADM.otungdom, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kontaktperson_navn = Slot(uri=FINT.kontaktpersonNavn, name="kontaktperson_navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=ADM.kontaktperson_navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.type = Slot(uri=FINT.type, name="type", curie=FINT.curie('type'),
                   model_uri=ADM.type, domain=None, range=Optional[str])

slots.kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=ADM.kontaktperson, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.virksomhetsId = Slot(uri=FINT.virksomhetsId, name="virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=ADM.virksomhetsId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.administrasjonContainer__personar = Slot(uri=ADM.personar, name="administrasjonContainer__personar", curie=ADM.curie('personar'),
                   model_uri=ADM.administrasjonContainer__personar, domain=None, range=Optional[Union[dict[Union[str, PersonId], Union[dict, Person]], list[Union[dict, Person]]]])

slots.administrasjonContainer__kontaktpersonar = Slot(uri=ADM.kontaktpersonar, name="administrasjonContainer__kontaktpersonar", curie=ADM.curie('kontaktpersonar'),
                   model_uri=ADM.administrasjonContainer__kontaktpersonar, domain=None, range=Optional[Union[dict[Union[str, KontaktpersonId], Union[dict, Kontaktperson]], list[Union[dict, Kontaktperson]]]])

slots.administrasjonContainer__virksomhetar = Slot(uri=ADM.virksomhetar, name="administrasjonContainer__virksomhetar", curie=ADM.curie('virksomhetar'),
                   model_uri=ADM.administrasjonContainer__virksomhetar, domain=None, range=Optional[Union[dict[Union[str, VirksomhetId], Union[dict, Virksomhet]], list[Union[dict, Virksomhet]]]])

slots.administrasjonContainer__landkodar = Slot(uri=ADM.landkodar, name="administrasjonContainer__landkodar", curie=ADM.curie('landkodar'),
                   model_uri=ADM.administrasjonContainer__landkodar, domain=None, range=Optional[Union[dict[Union[str, LandkodeId], Union[dict, Landkode]], list[Union[dict, Landkode]]]])

slots.administrasjonContainer__kjonn = Slot(uri=ADM.kjonn, name="administrasjonContainer__kjonn", curie=ADM.curie('kjonn'),
                   model_uri=ADM.administrasjonContainer__kjonn, domain=None, range=Optional[str])

slots.administrasjonContainer__fylke = Slot(uri=ADM.fylke, name="administrasjonContainer__fylke", curie=ADM.curie('fylke'),
                   model_uri=ADM.administrasjonContainer__fylke, domain=None, range=Optional[str])

slots.administrasjonContainer__kommunar = Slot(uri=ADM.kommunar, name="administrasjonContainer__kommunar", curie=ADM.curie('kommunar'),
                   model_uri=ADM.administrasjonContainer__kommunar, domain=None, range=Optional[Union[dict[Union[str, KommuneId], Union[dict, Kommune]], list[Union[dict, Kommune]]]])

slots.administrasjonContainer__spraak = Slot(uri=ADM.spraak, name="administrasjonContainer__spraak", curie=ADM.curie('spraak'),
                   model_uri=ADM.administrasjonContainer__spraak, domain=None, range=Optional[Union[dict[Union[str, SpraakId], Union[dict, Spraak]], list[Union[dict, Spraak]]]])

slots.administrasjonContainer__valuta = Slot(uri=ADM.valuta, name="administrasjonContainer__valuta", curie=ADM.curie('valuta'),
                   model_uri=ADM.administrasjonContainer__valuta, domain=None, range=Optional[Union[dict[Union[str, ValutaId], Union[dict, Valuta]], list[Union[dict, Valuta]]]])

slots.administrasjonContainer__personalressursar = Slot(uri=ADM.personalressursar, name="administrasjonContainer__personalressursar", curie=ADM.curie('personalressursar'),
                   model_uri=ADM.administrasjonContainer__personalressursar, domain=None, range=Optional[Union[dict[Union[str, PersonalressursId], Union[dict, Personalressurs]], list[Union[dict, Personalressurs]]]])

slots.administrasjonContainer__arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="administrasjonContainer__arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.administrasjonContainer__arbeidsforhold, domain=None, range=Optional[Union[str, ArbeidsforholdId]])

slots.administrasjonContainer__arbeidslokasjoner = Slot(uri=ADM.arbeidslokasjoner, name="administrasjonContainer__arbeidslokasjoner", curie=ADM.curie('arbeidslokasjoner'),
                   model_uri=ADM.administrasjonContainer__arbeidslokasjoner, domain=None, range=Optional[Union[dict[Union[str, ArbeidslokasjonId], Union[dict, Arbeidslokasjon]], list[Union[dict, Arbeidslokasjon]]]])

slots.administrasjonContainer__fastlonn = Slot(uri=ADM.fastlonn, name="administrasjonContainer__fastlonn", curie=ADM.curie('fastlonn'),
                   model_uri=ADM.administrasjonContainer__fastlonn, domain=None, range=Optional[Union[str, FastlonnId]])

slots.administrasjonContainer__fasttillegg = Slot(uri=ADM.fasttillegg, name="administrasjonContainer__fasttillegg", curie=ADM.curie('fasttillegg'),
                   model_uri=ADM.administrasjonContainer__fasttillegg, domain=None, range=Optional[Union[str, FasttilleggId]])

slots.administrasjonContainer__fravaer = Slot(uri=ADM.fravaer, name="administrasjonContainer__fravaer", curie=ADM.curie('fravaer'),
                   model_uri=ADM.administrasjonContainer__fravaer, domain=None, range=Optional[Union[str, FravaerId]])

slots.administrasjonContainer__fullmakter = Slot(uri=ADM.fullmakter, name="administrasjonContainer__fullmakter", curie=ADM.curie('fullmakter'),
                   model_uri=ADM.administrasjonContainer__fullmakter, domain=None, range=Optional[Union[dict[Union[str, FullmaktId], Union[dict, Fullmakt]], list[Union[dict, Fullmakt]]]])

slots.administrasjonContainer__organisasjonselement = Slot(uri=ADM.organisasjonselement, name="administrasjonContainer__organisasjonselement", curie=ADM.curie('organisasjonselement'),
                   model_uri=ADM.administrasjonContainer__organisasjonselement, domain=None, range=Optional[Union[str, OrganisasjonselementId]])

slots.administrasjonContainer__rollar = Slot(uri=ADM.rollar, name="administrasjonContainer__rollar", curie=ADM.curie('rollar'),
                   model_uri=ADM.administrasjonContainer__rollar, domain=None, range=Optional[Union[dict[Union[str, RolleId], Union[dict, Rolle]], list[Union[dict, Rolle]]]])

slots.administrasjonContainer__variabellonn = Slot(uri=ADM.variabellonn, name="administrasjonContainer__variabellonn", curie=ADM.curie('variabellonn'),
                   model_uri=ADM.administrasjonContainer__variabellonn, domain=None, range=Optional[Union[str, VariabellonnId]])

slots.administrasjonContainer__aktivitetar = Slot(uri=ADM.aktivitetar, name="administrasjonContainer__aktivitetar", curie=ADM.curie('aktivitetar'),
                   model_uri=ADM.administrasjonContainer__aktivitetar, domain=None, range=Optional[Union[dict[Union[str, AktivitetId], Union[dict, Aktivitet]], list[Union[dict, Aktivitet]]]])

slots.administrasjonContainer__anlegg = Slot(uri=ADM.anlegg, name="administrasjonContainer__anlegg", curie=ADM.curie('anlegg'),
                   model_uri=ADM.administrasjonContainer__anlegg, domain=None, range=Optional[Union[str, AnleggId]])

slots.administrasjonContainer__ansvar = Slot(uri=ADM.ansvar, name="administrasjonContainer__ansvar", curie=ADM.curie('ansvar'),
                   model_uri=ADM.administrasjonContainer__ansvar, domain=None, range=Optional[Union[str, AnsvarId]])

slots.administrasjonContainer__artar = Slot(uri=ADM.artar, name="administrasjonContainer__artar", curie=ADM.curie('artar'),
                   model_uri=ADM.administrasjonContainer__artar, domain=None, range=Optional[Union[dict[Union[str, ArtId], Union[dict, Art]], list[Union[dict, Art]]]])

slots.administrasjonContainer__arbeidsforholdstypar = Slot(uri=ADM.arbeidsforholdstypar, name="administrasjonContainer__arbeidsforholdstypar", curie=ADM.curie('arbeidsforholdstypar'),
                   model_uri=ADM.administrasjonContainer__arbeidsforholdstypar, domain=None, range=Optional[Union[dict[Union[str, ArbeidsforholdstypeId], Union[dict, Arbeidsforholdstype]], list[Union[dict, Arbeidsforholdstype]]]])

slots.administrasjonContainer__diverse = Slot(uri=ADM.diverse, name="administrasjonContainer__diverse", curie=ADM.curie('diverse'),
                   model_uri=ADM.administrasjonContainer__diverse, domain=None, range=Optional[Union[str, DiverseId]])

slots.administrasjonContainer__formaal = Slot(uri=ADM.formaal, name="administrasjonContainer__formaal", curie=ADM.curie('formaal'),
                   model_uri=ADM.administrasjonContainer__formaal, domain=None, range=Optional[Union[str, FormaalId]])

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
                   model_uri=ADM.administrasjonContainer__lopenummer, domain=None, range=Optional[Union[str, LopenummerId]])

slots.administrasjonContainer__objekt = Slot(uri=ADM.objekt, name="administrasjonContainer__objekt", curie=ADM.curie('objekt'),
                   model_uri=ADM.administrasjonContainer__objekt, domain=None, range=Optional[Union[str, ObjektId]])

slots.administrasjonContainer__organisasjonstypar = Slot(uri=ADM.organisasjonstypar, name="administrasjonContainer__organisasjonstypar", curie=ADM.curie('organisasjonstypar'),
                   model_uri=ADM.administrasjonContainer__organisasjonstypar, domain=None, range=Optional[Union[dict[Union[str, OrganisasjonstypeId], Union[dict, Organisasjonstype]], list[Union[dict, Organisasjonstype]]]])

slots.administrasjonContainer__personalressurskategoriar = Slot(uri=ADM.personalressurskategoriar, name="administrasjonContainer__personalressurskategoriar", curie=ADM.curie('personalressurskategoriar'),
                   model_uri=ADM.administrasjonContainer__personalressurskategoriar, domain=None, range=Optional[Union[dict[Union[str, PersonalressurskategoriId], Union[dict, Personalressurskategori]], list[Union[dict, Personalressurskategori]]]])

slots.administrasjonContainer__prosjekt = Slot(uri=ADM.prosjekt, name="administrasjonContainer__prosjekt", curie=ADM.curie('prosjekt'),
                   model_uri=ADM.administrasjonContainer__prosjekt, domain=None, range=Optional[Union[str, ProsjektId]])

slots.administrasjonContainer__prosjektartar = Slot(uri=ADM.prosjektartar, name="administrasjonContainer__prosjektartar", curie=ADM.curie('prosjektartar'),
                   model_uri=ADM.administrasjonContainer__prosjektartar, domain=None, range=Optional[Union[dict[Union[str, ProsjektartId], Union[dict, Prosjektart]], list[Union[dict, Prosjektart]]]])

slots.administrasjonContainer__rammer = Slot(uri=ADM.rammer, name="administrasjonContainer__rammer", curie=ADM.curie('rammer'),
                   model_uri=ADM.administrasjonContainer__rammer, domain=None, range=Optional[Union[dict[Union[str, RammeId], Union[dict, Ramme]], list[Union[dict, Ramme]]]])

slots.administrasjonContainer__stillingskoder = Slot(uri=ADM.stillingskoder, name="administrasjonContainer__stillingskoder", curie=ADM.curie('stillingskoder'),
                   model_uri=ADM.administrasjonContainer__stillingskoder, domain=None, range=Optional[Union[dict[Union[str, StillingskodeId], Union[dict, Stillingskode]], list[Union[dict, Stillingskode]]]])

slots.administrasjonContainer__uketimetall = Slot(uri=ADM.uketimetall, name="administrasjonContainer__uketimetall", curie=ADM.curie('uketimetall'),
                   model_uri=ADM.administrasjonContainer__uketimetall, domain=None, range=Optional[Union[dict[Union[str, UketimetallId], Union[dict, Uketimetall]], list[Union[dict, Uketimetall]]]])

slots.person__personalressurs = Slot(uri=FINT.personalressurs, name="person__personalressurs", curie=FINT.curie('personalressurs'),
                   model_uri=ADM.person__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.AdministrasjonContainer_arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="AdministrasjonContainer_arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.AdministrasjonContainer_arbeidsforhold, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, ArbeidsforholdId], Union[dict, "Arbeidsforhold"]], list[Union[dict, "Arbeidsforhold"]]]])

slots.AdministrasjonContainer_fastlonn = Slot(uri=ADM.fastlonn, name="AdministrasjonContainer_fastlonn", curie=ADM.curie('fastlonn'),
                   model_uri=ADM.AdministrasjonContainer_fastlonn, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, FastlonnId], Union[dict, "Fastlonn"]], list[Union[dict, "Fastlonn"]]]])

slots.AdministrasjonContainer_fasttillegg = Slot(uri=ADM.fasttillegg, name="AdministrasjonContainer_fasttillegg", curie=ADM.curie('fasttillegg'),
                   model_uri=ADM.AdministrasjonContainer_fasttillegg, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, FasttilleggId], Union[dict, "Fasttillegg"]], list[Union[dict, "Fasttillegg"]]]])

slots.AdministrasjonContainer_fravaer = Slot(uri=ADM.fravaer, name="AdministrasjonContainer_fravaer", curie=ADM.curie('fravaer'),
                   model_uri=ADM.AdministrasjonContainer_fravaer, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, FravaerId], Union[dict, "Fravaer"]], list[Union[dict, "Fravaer"]]]])

slots.AdministrasjonContainer_organisasjonselement = Slot(uri=ADM.organisasjonselement, name="AdministrasjonContainer_organisasjonselement", curie=ADM.curie('organisasjonselement'),
                   model_uri=ADM.AdministrasjonContainer_organisasjonselement, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, OrganisasjonselementId], Union[dict, "Organisasjonselement"]], list[Union[dict, "Organisasjonselement"]]]])

slots.AdministrasjonContainer_variabellonn = Slot(uri=ADM.variabellonn, name="AdministrasjonContainer_variabellonn", curie=ADM.curie('variabellonn'),
                   model_uri=ADM.AdministrasjonContainer_variabellonn, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, VariabellonnId], Union[dict, "Variabellonn"]], list[Union[dict, "Variabellonn"]]]])

slots.AdministrasjonContainer_anlegg = Slot(uri=ADM.anlegg, name="AdministrasjonContainer_anlegg", curie=ADM.curie('anlegg'),
                   model_uri=ADM.AdministrasjonContainer_anlegg, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, AnleggId], Union[dict, "Anlegg"]], list[Union[dict, "Anlegg"]]]])

slots.AdministrasjonContainer_ansvar = Slot(uri=ADM.ansvar, name="AdministrasjonContainer_ansvar", curie=ADM.curie('ansvar'),
                   model_uri=ADM.AdministrasjonContainer_ansvar, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, AnsvarId], Union[dict, "Ansvar"]], list[Union[dict, "Ansvar"]]]])

slots.AdministrasjonContainer_diverse = Slot(uri=ADM.diverse, name="AdministrasjonContainer_diverse", curie=ADM.curie('diverse'),
                   model_uri=ADM.AdministrasjonContainer_diverse, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, DiverseId], Union[dict, "Diverse"]], list[Union[dict, "Diverse"]]]])

slots.AdministrasjonContainer_formaal = Slot(uri=ADM.formaal, name="AdministrasjonContainer_formaal", curie=ADM.curie('formaal'),
                   model_uri=ADM.AdministrasjonContainer_formaal, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, FormaalId], Union[dict, "Formaal"]], list[Union[dict, "Formaal"]]]])

slots.AdministrasjonContainer_lopenummer = Slot(uri=ADM.lopenummer, name="AdministrasjonContainer_lopenummer", curie=ADM.curie('lopenummer'),
                   model_uri=ADM.AdministrasjonContainer_lopenummer, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, LopenummerId], Union[dict, "Lopenummer"]], list[Union[dict, "Lopenummer"]]]])

slots.AdministrasjonContainer_objekt = Slot(uri=ADM.objekt, name="AdministrasjonContainer_objekt", curie=ADM.curie('objekt'),
                   model_uri=ADM.AdministrasjonContainer_objekt, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, ObjektId], Union[dict, "Objekt"]], list[Union[dict, "Objekt"]]]])

slots.AdministrasjonContainer_prosjekt = Slot(uri=ADM.prosjekt, name="AdministrasjonContainer_prosjekt", curie=ADM.curie('prosjekt'),
                   model_uri=ADM.AdministrasjonContainer_prosjekt, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, ProsjektId], Union[dict, "Prosjekt"]], list[Union[dict, "Prosjekt"]]]])

slots.AdministrasjonContainer_kjonn = Slot(uri=FINT.kjonn, name="AdministrasjonContainer_kjonn", curie=FINT.curie('kjonn'),
                   model_uri=ADM.AdministrasjonContainer_kjonn, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, KjonnId], Union[dict, "Kjonn"]], list[Union[dict, "Kjonn"]]]])

slots.AdministrasjonContainer_fylke = Slot(uri=FINT.fylke, name="AdministrasjonContainer_fylke", curie=FINT.curie('fylke'),
                   model_uri=ADM.AdministrasjonContainer_fylke, domain=AdministrasjonContainer, range=Optional[Union[dict[Union[str, FylkeId], Union[dict, "Fylke"]], list[Union[dict, "Fylke"]]]])

slots.Lonn_beskrivelse = Slot(uri=FINT.beskrivelse, name="Lonn_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=ADM.Lonn_beskrivelse, domain=Lonn, range=str)

slots.Lonn_kontostreng = Slot(uri=ADM.kontostreng, name="Lonn_kontostreng", curie=ADM.curie('kontostreng'),
                   model_uri=ADM.Lonn_kontostreng, domain=Lonn, range=Union[dict, "Kontostreng"])

slots.Lonn_periode = Slot(uri=ADM.periode, name="Lonn_periode", curie=ADM.curie('periode'),
                   model_uri=ADM.Lonn_periode, domain=Lonn, range=Union[dict, "Periode"])

slots.Lonn_anvist = Slot(uri=ADM.anvist, name="Lonn_anvist", curie=ADM.curie('anvist'),
                   model_uri=ADM.Lonn_anvist, domain=Lonn, range=Optional[Union[str, XSDDateTime]])

slots.Lonn_attestert = Slot(uri=ADM.attestert, name="Lonn_attestert", curie=ADM.curie('attestert'),
                   model_uri=ADM.Lonn_attestert, domain=Lonn, range=Optional[Union[str, XSDDateTime]])

slots.Lonn_kildesystemId = Slot(uri=ADM.kildesystemId, name="Lonn_kildesystemId", curie=ADM.curie('kildesystemId'),
                   model_uri=ADM.Lonn_kildesystemId, domain=Lonn, range=Optional[Union[dict, "Identifikator"]])

slots.Lonn_kontert = Slot(uri=ADM.kontert, name="Lonn_kontert", curie=ADM.curie('kontert'),
                   model_uri=ADM.Lonn_kontert, domain=Lonn, range=Optional[Union[str, XSDDateTime]])

slots.Lonn_opptjent = Slot(uri=ADM.opptjent, name="Lonn_opptjent", curie=ADM.curie('opptjent'),
                   model_uri=ADM.Lonn_opptjent, domain=Lonn, range=Optional[Union[dict, "Periode"]])

slots.Lonn_anviser = Slot(uri=ADM.anviser, name="Lonn_anviser", curie=ADM.curie('anviser'),
                   model_uri=ADM.Lonn_anviser, domain=Lonn, range=Optional[Union[str, PersonalressursId]])

slots.Lonn_konterer = Slot(uri=ADM.konterer, name="Lonn_konterer", curie=ADM.curie('konterer'),
                   model_uri=ADM.Lonn_konterer, domain=Lonn, range=Optional[Union[str, PersonalressursId]])

slots.Lonn_attestant = Slot(uri=ADM.attestant, name="Lonn_attestant", curie=ADM.curie('attestant'),
                   model_uri=ADM.Lonn_attestant, domain=Lonn, range=Optional[Union[str, PersonalressursId]])

slots.Kontostreng_ansvar = Slot(uri=ADM.ansvar, name="Kontostreng_ansvar", curie=ADM.curie('ansvar'),
                   model_uri=ADM.Kontostreng_ansvar, domain=Kontostreng, range=Union[str, AnsvarId])

slots.Kontostreng_art = Slot(uri=ADM.art, name="Kontostreng_art", curie=ADM.curie('art'),
                   model_uri=ADM.Kontostreng_art, domain=Kontostreng, range=Union[str, ArtId])

slots.Kontostreng_funksjon = Slot(uri=ADM.funksjon, name="Kontostreng_funksjon", curie=ADM.curie('funksjon'),
                   model_uri=ADM.Kontostreng_funksjon, domain=Kontostreng, range=Union[str, FunksjonId])

slots.Kontostreng_aktivitet = Slot(uri=ADM.aktivitet, name="Kontostreng_aktivitet", curie=ADM.curie('aktivitet'),
                   model_uri=ADM.Kontostreng_aktivitet, domain=Kontostreng, range=Optional[Union[str, AktivitetId]])

slots.Kontostreng_anlegg = Slot(uri=ADM.anlegg, name="Kontostreng_anlegg", curie=ADM.curie('anlegg'),
                   model_uri=ADM.Kontostreng_anlegg, domain=Kontostreng, range=Optional[Union[str, AnleggId]])

slots.Kontostreng_diverse = Slot(uri=ADM.diverse, name="Kontostreng_diverse", curie=ADM.curie('diverse'),
                   model_uri=ADM.Kontostreng_diverse, domain=Kontostreng, range=Optional[Union[str, DiverseId]])

slots.Kontostreng_formaal = Slot(uri=ADM.formaal, name="Kontostreng_formaal", curie=ADM.curie('formaal'),
                   model_uri=ADM.Kontostreng_formaal, domain=Kontostreng, range=Optional[Union[str, FormaalId]])

slots.Kontostreng_kontrakt = Slot(uri=ADM.kontrakt, name="Kontostreng_kontrakt", curie=ADM.curie('kontrakt'),
                   model_uri=ADM.Kontostreng_kontrakt, domain=Kontostreng, range=Optional[Union[str, KontraktId]])

slots.Kontostreng_lopenummer = Slot(uri=ADM.lopenummer, name="Kontostreng_lopenummer", curie=ADM.curie('lopenummer'),
                   model_uri=ADM.Kontostreng_lopenummer, domain=Kontostreng, range=Optional[Union[str, LopenummerId]])

slots.Kontostreng_objekt = Slot(uri=ADM.objekt, name="Kontostreng_objekt", curie=ADM.curie('objekt'),
                   model_uri=ADM.Kontostreng_objekt, domain=Kontostreng, range=Optional[Union[str, ObjektId]])

slots.Kontostreng_prosjekt = Slot(uri=ADM.prosjekt, name="Kontostreng_prosjekt", curie=ADM.curie('prosjekt'),
                   model_uri=ADM.Kontostreng_prosjekt, domain=Kontostreng, range=Optional[Union[str, ProsjektId]])

slots.Kontostreng_prosjektart = Slot(uri=ADM.prosjektart, name="Kontostreng_prosjektart", curie=ADM.curie('prosjektart'),
                   model_uri=ADM.Kontostreng_prosjektart, domain=Kontostreng, range=Optional[Union[str, ProsjektartId]])

slots.Kontostreng_ramme = Slot(uri=ADM.ramme, name="Kontostreng_ramme", curie=ADM.curie('ramme'),
                   model_uri=ADM.Kontostreng_ramme, domain=Kontostreng, range=Optional[Union[str, RammeId]])

slots.Ansvar_overordnet = Slot(uri=ADM.overordnet, name="Ansvar_overordnet", curie=ADM.curie('overordnet'),
                   model_uri=ADM.Ansvar_overordnet, domain=Ansvar, range=Optional[Union[str, AnsvarId]])

slots.Ansvar_underordnet = Slot(uri=ADM.underordnet, name="Ansvar_underordnet", curie=ADM.curie('underordnet'),
                   model_uri=ADM.Ansvar_underordnet, domain=Ansvar, range=Optional[Union[Union[str, AnsvarId], list[Union[str, AnsvarId]]]])

slots.Ansvar_organisasjonselement = Slot(uri=ADM.organisasjonselement, name="Ansvar_organisasjonselement", curie=ADM.curie('organisasjonselement'),
                   model_uri=ADM.Ansvar_organisasjonselement, domain=Ansvar, range=Optional[Union[Union[str, OrganisasjonselementId], list[Union[str, OrganisasjonselementId]]]])

slots.Arbeidsforholdstype_forelder = Slot(uri=ADM.forelder, name="Arbeidsforholdstype_forelder", curie=ADM.curie('forelder'),
                   model_uri=ADM.Arbeidsforholdstype_forelder, domain=Arbeidsforholdstype, range=Optional[Union[str, ArbeidsforholdstypeId]])

slots.Fravaerstype_overfores = Slot(uri=ADM.overfores, name="Fravaerstype_overfores", curie=ADM.curie('overfores'),
                   model_uri=ADM.Fravaerstype_overfores, domain=Fravaerstype, range=Optional[Union[bool, Bool]])

slots.Fravaerstype_lonsart = Slot(uri=ADM.lonsart, name="Fravaerstype_lonsart", curie=ADM.curie('lonsart'),
                   model_uri=ADM.Fravaerstype_lonsart, domain=Fravaerstype, range=Optional[Union[str, LonsartId]])

slots.Funksjon_overordnet = Slot(uri=ADM.overordnet, name="Funksjon_overordnet", curie=ADM.curie('overordnet'),
                   model_uri=ADM.Funksjon_overordnet, domain=Funksjon, range=Optional[Union[str, FunksjonId]])

slots.Funksjon_underordnet = Slot(uri=ADM.underordnet, name="Funksjon_underordnet", curie=ADM.curie('underordnet'),
                   model_uri=ADM.Funksjon_underordnet, domain=Funksjon, range=Optional[Union[Union[str, FunksjonId], list[Union[str, FunksjonId]]]])

slots.Lonsart_kategori = Slot(uri=ADM.kategori, name="Lonsart_kategori", curie=ADM.curie('kategori'),
                   model_uri=ADM.Lonsart_kategori, domain=Lonsart, range=Optional[str])

slots.Lonsart_art = Slot(uri=ADM.art, name="Lonsart_art", curie=ADM.curie('art'),
                   model_uri=ADM.Lonsart_art, domain=Lonsart, range=Optional[Union[str, ArtId]])

slots.Prosjekt_prosjektart = Slot(uri=ADM.prosjektart, name="Prosjekt_prosjektart", curie=ADM.curie('prosjektart'),
                   model_uri=ADM.Prosjekt_prosjektart, domain=Prosjekt, range=Optional[Union[Union[str, ProsjektartId], list[Union[str, ProsjektartId]]]])

slots.Prosjektart_prosjekt = Slot(uri=ADM.prosjekt, name="Prosjektart_prosjekt", curie=ADM.curie('prosjekt'),
                   model_uri=ADM.Prosjektart_prosjekt, domain=Prosjektart, range=Optional[Union[str, ProsjektId]])

slots.Prosjektart_overordnet = Slot(uri=ADM.overordnet, name="Prosjektart_overordnet", curie=ADM.curie('overordnet'),
                   model_uri=ADM.Prosjektart_overordnet, domain=Prosjektart, range=Optional[Union[str, ProsjektartId]])

slots.Prosjektart_underordnet = Slot(uri=ADM.underordnet, name="Prosjektart_underordnet", curie=ADM.curie('underordnet'),
                   model_uri=ADM.Prosjektart_underordnet, domain=Prosjektart, range=Optional[Union[Union[str, ProsjektartId], list[Union[str, ProsjektartId]]]])

slots.Stillingskode_forelder = Slot(uri=ADM.forelder, name="Stillingskode_forelder", curie=ADM.curie('forelder'),
                   model_uri=ADM.Stillingskode_forelder, domain=Stillingskode, range=Optional[Union[str, StillingskodeId]])

slots.Fastlonn_prosent = Slot(uri=ADM.prosent, name="Fastlonn_prosent", curie=ADM.curie('prosent'),
                   model_uri=ADM.Fastlonn_prosent, domain=Fastlonn, range=int)

slots.Fastlonn_arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="Fastlonn_arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.Fastlonn_arbeidsforhold, domain=Fastlonn, range=Union[str, ArbeidsforholdId])

slots.Fastlonn_lonsart = Slot(uri=ADM.lonsart, name="Fastlonn_lonsart", curie=ADM.curie('lonsart'),
                   model_uri=ADM.Fastlonn_lonsart, domain=Fastlonn, range=Optional[Union[str, LonsartId]])

slots.Fasttillegg_belop = Slot(uri=ADM.belop, name="Fasttillegg_belop", curie=ADM.curie('belop'),
                   model_uri=ADM.Fasttillegg_belop, domain=Fasttillegg, range=int)

slots.Fasttillegg_lonsart = Slot(uri=ADM.lonsart, name="Fasttillegg_lonsart", curie=ADM.curie('lonsart'),
                   model_uri=ADM.Fasttillegg_lonsart, domain=Fasttillegg, range=Union[str, LonsartId])

slots.Fasttillegg_arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="Fasttillegg_arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.Fasttillegg_arbeidsforhold, domain=Fasttillegg, range=Union[str, ArbeidsforholdId])

slots.Variabellonn_antall = Slot(uri=ADM.antall, name="Variabellonn_antall", curie=ADM.curie('antall'),
                   model_uri=ADM.Variabellonn_antall, domain=Variabellonn, range=int)

slots.Variabellonn_lonsart = Slot(uri=ADM.lonsart, name="Variabellonn_lonsart", curie=ADM.curie('lonsart'),
                   model_uri=ADM.Variabellonn_lonsart, domain=Variabellonn, range=Union[str, LonsartId])

slots.Variabellonn_arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="Variabellonn_arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.Variabellonn_arbeidsforhold, domain=Variabellonn, range=Union[str, ArbeidsforholdId])

slots.Variabellonn_belop = Slot(uri=ADM.belop, name="Variabellonn_belop", curie=ADM.curie('belop'),
                   model_uri=ADM.Variabellonn_belop, domain=Variabellonn, range=Optional[int])

slots.Fravaer_periode = Slot(uri=ADM.periode, name="Fravaer_periode", curie=ADM.curie('periode'),
                   model_uri=ADM.Fravaer_periode, domain=Fravaer, range=Union[dict, "Periode"])

slots.Fravaer_prosent = Slot(uri=ADM.prosent, name="Fravaer_prosent", curie=ADM.curie('prosent'),
                   model_uri=ADM.Fravaer_prosent, domain=Fravaer, range=int)

slots.Fravaer_fravaerstype = Slot(uri=ADM.fravaerstype, name="Fravaer_fravaerstype", curie=ADM.curie('fravaerstype'),
                   model_uri=ADM.Fravaer_fravaerstype, domain=Fravaer, range=Union[str, FravaerstypeId])

slots.Fravaer_arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="Fravaer_arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.Fravaer_arbeidsforhold, domain=Fravaer, range=Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]])

slots.Fravaer_godkjent = Slot(uri=ADM.godkjent, name="Fravaer_godkjent", curie=ADM.curie('godkjent'),
                   model_uri=ADM.Fravaer_godkjent, domain=Fravaer, range=Optional[Union[str, XSDDateTime]])

slots.Fravaer_kildesystemId = Slot(uri=ADM.kildesystemId, name="Fravaer_kildesystemId", curie=ADM.curie('kildesystemId'),
                   model_uri=ADM.Fravaer_kildesystemId, domain=Fravaer, range=Optional[Union[dict, "Identifikator"]])

slots.Fravaer_fravaersgrunn = Slot(uri=ADM.fravaersgrunn, name="Fravaer_fravaersgrunn", curie=ADM.curie('fravaersgrunn'),
                   model_uri=ADM.Fravaer_fravaersgrunn, domain=Fravaer, range=Optional[Union[str, FravaersgrunnId]])

slots.Fravaer_fortsettelse = Slot(uri=ADM.fortsettelse, name="Fravaer_fortsettelse", curie=ADM.curie('fortsettelse'),
                   model_uri=ADM.Fravaer_fortsettelse, domain=Fravaer, range=Optional[Union[str, FravaerId]])

slots.Fravaer_fortsetter = Slot(uri=ADM.fortsetter, name="Fravaer_fortsetter", curie=ADM.curie('fortsetter'),
                   model_uri=ADM.Fravaer_fortsetter, domain=Fravaer, range=Optional[Union[str, FravaerId]])

slots.Fravaer_godkjenner = Slot(uri=ADM.godkjenner, name="Fravaer_godkjenner", curie=ADM.curie('godkjenner'),
                   model_uri=ADM.Fravaer_godkjenner, domain=Fravaer, range=Optional[Union[str, PersonalressursId]])

slots.Fullmakt_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Fullmakt_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ADM.Fullmakt_gyldighetsperiode, domain=Fullmakt, range=Union[dict, "Periode"])

slots.Fullmakt_rolle = Slot(uri=ADM.rolle, name="Fullmakt_rolle", curie=ADM.curie('rolle'),
                   model_uri=ADM.Fullmakt_rolle, domain=Fullmakt, range=Union[str, RolleId])

slots.Fullmakt_ramme = Slot(uri=ADM.ramme, name="Fullmakt_ramme", curie=ADM.curie('ramme'),
                   model_uri=ADM.Fullmakt_ramme, domain=Fullmakt, range=Optional[Union[str, RammeId]])

slots.Fullmakt_funksjon = Slot(uri=ADM.funksjon, name="Fullmakt_funksjon", curie=ADM.curie('funksjon'),
                   model_uri=ADM.Fullmakt_funksjon, domain=Fullmakt, range=Optional[Union[str, FunksjonId]])

slots.Fullmakt_objekt = Slot(uri=ADM.objekt, name="Fullmakt_objekt", curie=ADM.curie('objekt'),
                   model_uri=ADM.Fullmakt_objekt, domain=Fullmakt, range=Optional[Union[str, ObjektId]])

slots.Fullmakt_organisasjonselement = Slot(uri=ADM.organisasjonselement, name="Fullmakt_organisasjonselement", curie=ADM.curie('organisasjonselement'),
                   model_uri=ADM.Fullmakt_organisasjonselement, domain=Fullmakt, range=Optional[Union[str, OrganisasjonselementId]])

slots.Fullmakt_art = Slot(uri=ADM.art, name="Fullmakt_art", curie=ADM.curie('art'),
                   model_uri=ADM.Fullmakt_art, domain=Fullmakt, range=Optional[Union[str, ArtId]])

slots.Fullmakt_anlegg = Slot(uri=ADM.anlegg, name="Fullmakt_anlegg", curie=ADM.curie('anlegg'),
                   model_uri=ADM.Fullmakt_anlegg, domain=Fullmakt, range=Optional[Union[str, AnleggId]])

slots.Fullmakt_diverse = Slot(uri=ADM.diverse, name="Fullmakt_diverse", curie=ADM.curie('diverse'),
                   model_uri=ADM.Fullmakt_diverse, domain=Fullmakt, range=Optional[Union[str, DiverseId]])

slots.Fullmakt_aktivitet = Slot(uri=ADM.aktivitet, name="Fullmakt_aktivitet", curie=ADM.curie('aktivitet'),
                   model_uri=ADM.Fullmakt_aktivitet, domain=Fullmakt, range=Optional[Union[str, AktivitetId]])

slots.Fullmakt_ansvar = Slot(uri=ADM.ansvar, name="Fullmakt_ansvar", curie=ADM.curie('ansvar'),
                   model_uri=ADM.Fullmakt_ansvar, domain=Fullmakt, range=Optional[Union[str, AnsvarId]])

slots.Fullmakt_stedfortreder = Slot(uri=ADM.stedfortreder, name="Fullmakt_stedfortreder", curie=ADM.curie('stedfortreder'),
                   model_uri=ADM.Fullmakt_stedfortreder, domain=Fullmakt, range=Optional[Union[str, PersonalressursId]])

slots.Fullmakt_kontrakt = Slot(uri=ADM.kontrakt, name="Fullmakt_kontrakt", curie=ADM.curie('kontrakt'),
                   model_uri=ADM.Fullmakt_kontrakt, domain=Fullmakt, range=Optional[Union[str, KontraktId]])

slots.Fullmakt_fullmektig = Slot(uri=ADM.fullmektig, name="Fullmakt_fullmektig", curie=ADM.curie('fullmektig'),
                   model_uri=ADM.Fullmakt_fullmektig, domain=Fullmakt, range=Optional[Union[str, PersonalressursId]])

slots.Fullmakt_prosjekt = Slot(uri=ADM.prosjekt, name="Fullmakt_prosjekt", curie=ADM.curie('prosjekt'),
                   model_uri=ADM.Fullmakt_prosjekt, domain=Fullmakt, range=Optional[Union[str, ProsjektId]])

slots.Fullmakt_formaal = Slot(uri=ADM.formaal, name="Fullmakt_formaal", curie=ADM.curie('formaal'),
                   model_uri=ADM.Fullmakt_formaal, domain=Fullmakt, range=Optional[Union[str, FormaalId]])

slots.Fullmakt_lopenummer = Slot(uri=ADM.lopenummer, name="Fullmakt_lopenummer", curie=ADM.curie('lopenummer'),
                   model_uri=ADM.Fullmakt_lopenummer, domain=Fullmakt, range=Optional[Union[str, LopenummerId]])

slots.Rolle_rolleNavn = Slot(uri=ADM.rolleNavn, name="Rolle_rolleNavn", curie=ADM.curie('rolleNavn'),
                   model_uri=ADM.Rolle_rolleNavn, domain=Rolle, range=Union[dict, "Identifikator"])

slots.Rolle_beskrivelse = Slot(uri=FINT.beskrivelse, name="Rolle_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=ADM.Rolle_beskrivelse, domain=Rolle, range=str)

slots.Rolle_fullmakt = Slot(uri=ADM.fullmakt, name="Rolle_fullmakt", curie=ADM.curie('fullmakt'),
                   model_uri=ADM.Rolle_fullmakt, domain=Rolle, range=Union[Union[str, FullmaktId], list[Union[str, FullmaktId]]])

slots.Arbeidslokasjon_lokasjonskode = Slot(uri=ADM.lokasjonskode, name="Arbeidslokasjon_lokasjonskode", curie=ADM.curie('lokasjonskode'),
                   model_uri=ADM.Arbeidslokasjon_lokasjonskode, domain=Arbeidslokasjon, range=Union[dict, "Identifikator"])

slots.Arbeidslokasjon_lokasjonsnavn = Slot(uri=ADM.lokasjonsnavn, name="Arbeidslokasjon_lokasjonsnavn", curie=ADM.curie('lokasjonsnavn'),
                   model_uri=ADM.Arbeidslokasjon_lokasjonsnavn, domain=Arbeidslokasjon, range=Optional[str])

slots.Arbeidslokasjon_forretningsadresse = Slot(uri=FINT.forretningsadresse, name="Arbeidslokasjon_forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=ADM.Arbeidslokasjon_forretningsadresse, domain=Arbeidslokasjon, range=Optional[Union[dict, "Adresse"]])

slots.Arbeidslokasjon_organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="Arbeidslokasjon_organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=ADM.Arbeidslokasjon_organisasjonsnavn, domain=Arbeidslokasjon, range=Optional[str])

slots.Arbeidslokasjon_organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="Arbeidslokasjon_organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=ADM.Arbeidslokasjon_organisasjonsnummer, domain=Arbeidslokasjon, range=Optional[Union[dict, "Identifikator"]])

slots.Arbeidslokasjon_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Arbeidslokasjon_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ADM.Arbeidslokasjon_kontaktinformasjon, domain=Arbeidslokasjon, range=Optional[Union[dict, "Kontaktinformasjon"]])

slots.Arbeidslokasjon_postadresse = Slot(uri=FINT.postadresse, name="Arbeidslokasjon_postadresse", curie=FINT.curie('postadresse'),
                   model_uri=ADM.Arbeidslokasjon_postadresse, domain=Arbeidslokasjon, range=Optional[Union[dict, "Adresse"]])

slots.Arbeidslokasjon_arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="Arbeidslokasjon_arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.Arbeidslokasjon_arbeidsforhold, domain=Arbeidslokasjon, range=Optional[Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]]])

slots.Organisasjonselement_organisasjonsId = Slot(uri=ADM.organisasjonsId, name="Organisasjonselement_organisasjonsId", curie=ADM.curie('organisasjonsId'),
                   model_uri=ADM.Organisasjonselement_organisasjonsId, domain=Organisasjonselement, range=Union[dict, "Identifikator"])

slots.Organisasjonselement_organisasjonsKode = Slot(uri=ADM.organisasjonsKode, name="Organisasjonselement_organisasjonsKode", curie=ADM.curie('organisasjonsKode'),
                   model_uri=ADM.Organisasjonselement_organisasjonsKode, domain=Organisasjonselement, range=Union[dict, "Identifikator"])

slots.Organisasjonselement_overordnet = Slot(uri=ADM.overordnet, name="Organisasjonselement_overordnet", curie=ADM.curie('overordnet'),
                   model_uri=ADM.Organisasjonselement_overordnet, domain=Organisasjonselement, range=Union[str, OrganisasjonselementId])

slots.Organisasjonselement_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Organisasjonselement_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ADM.Organisasjonselement_gyldighetsperiode, domain=Organisasjonselement, range=Optional[Union[dict, "Periode"]])

slots.Organisasjonselement_kortnavn = Slot(uri=ADM.kortnavn, name="Organisasjonselement_kortnavn", curie=ADM.curie('kortnavn'),
                   model_uri=ADM.Organisasjonselement_kortnavn, domain=Organisasjonselement, range=Optional[str])

slots.Organisasjonselement_navn = Slot(uri=FINT.navn, name="Organisasjonselement_navn", curie=FINT.curie('navn'),
                   model_uri=ADM.Organisasjonselement_navn, domain=Organisasjonselement, range=Optional[str])

slots.Organisasjonselement_forretningsadresse = Slot(uri=FINT.forretningsadresse, name="Organisasjonselement_forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=ADM.Organisasjonselement_forretningsadresse, domain=Organisasjonselement, range=Optional[Union[dict, "Adresse"]])

slots.Organisasjonselement_organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="Organisasjonselement_organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=ADM.Organisasjonselement_organisasjonsnavn, domain=Organisasjonselement, range=Optional[str])

slots.Organisasjonselement_organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="Organisasjonselement_organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=ADM.Organisasjonselement_organisasjonsnummer, domain=Organisasjonselement, range=Optional[Union[dict, "Identifikator"]])

slots.Organisasjonselement_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Organisasjonselement_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ADM.Organisasjonselement_kontaktinformasjon, domain=Organisasjonselement, range=Optional[Union[dict, "Kontaktinformasjon"]])

slots.Organisasjonselement_postadresse = Slot(uri=FINT.postadresse, name="Organisasjonselement_postadresse", curie=FINT.curie('postadresse'),
                   model_uri=ADM.Organisasjonselement_postadresse, domain=Organisasjonselement, range=Optional[Union[dict, "Adresse"]])

slots.Organisasjonselement_ansvar = Slot(uri=ADM.ansvar, name="Organisasjonselement_ansvar", curie=ADM.curie('ansvar'),
                   model_uri=ADM.Organisasjonselement_ansvar, domain=Organisasjonselement, range=Optional[Union[Union[str, AnsvarId], list[Union[str, AnsvarId]]]])

slots.Organisasjonselement_organisasjonstype = Slot(uri=ADM.organisasjonstype, name="Organisasjonselement_organisasjonstype", curie=ADM.curie('organisasjonstype'),
                   model_uri=ADM.Organisasjonselement_organisasjonstype, domain=Organisasjonselement, range=Optional[Union[str, OrganisasjonstypeId]])

slots.Organisasjonselement_leder = Slot(uri=ADM.leder, name="Organisasjonselement_leder", curie=ADM.curie('leder'),
                   model_uri=ADM.Organisasjonselement_leder, domain=Organisasjonselement, range=Optional[Union[str, PersonalressursId]])

slots.Organisasjonselement_underordnet = Slot(uri=ADM.underordnet, name="Organisasjonselement_underordnet", curie=ADM.curie('underordnet'),
                   model_uri=ADM.Organisasjonselement_underordnet, domain=Organisasjonselement, range=Optional[Union[Union[str, OrganisasjonselementId], list[Union[str, OrganisasjonselementId]]]])

slots.Organisasjonselement_skole = Slot(uri=ADM.skole, name="Organisasjonselement_skole", curie=ADM.curie('skole'),
                   model_uri=ADM.Organisasjonselement_skole, domain=Organisasjonselement, range=Optional[Union[str, URIorCURIE]])

slots.Organisasjonselement_arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="Organisasjonselement_arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.Organisasjonselement_arbeidsforhold, domain=Organisasjonselement, range=Optional[Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]]])

slots.Personalressurs_ansattnummer = Slot(uri=ADM.ansattnummer, name="Personalressurs_ansattnummer", curie=ADM.curie('ansattnummer'),
                   model_uri=ADM.Personalressurs_ansattnummer, domain=Personalressurs, range=Union[dict, "Identifikator"])

slots.Personalressurs_ansettelsesperiode = Slot(uri=ADM.ansettelsesperiode, name="Personalressurs_ansettelsesperiode", curie=ADM.curie('ansettelsesperiode'),
                   model_uri=ADM.Personalressurs_ansettelsesperiode, domain=Personalressurs, range=Union[dict, "Periode"])

slots.Personalressurs_person = Slot(uri=FINT.person, name="Personalressurs_person", curie=FINT.curie('person'),
                   model_uri=ADM.Personalressurs_person, domain=Personalressurs, range=Union[str, PersonId])

slots.Personalressurs_personalressurskategori = Slot(uri=ADM.personalressurskategori, name="Personalressurs_personalressurskategori", curie=ADM.curie('personalressurskategori'),
                   model_uri=ADM.Personalressurs_personalressurskategori, domain=Personalressurs, range=Union[str, PersonalressurskategoriId])

slots.Personalressurs_ansiennitet = Slot(uri=ADM.ansiennitet, name="Personalressurs_ansiennitet", curie=ADM.curie('ansiennitet'),
                   model_uri=ADM.Personalressurs_ansiennitet, domain=Personalressurs, range=Optional[Union[str, XSDDate]])

slots.Personalressurs_brukernavn = Slot(uri=ADM.brukernavn, name="Personalressurs_brukernavn", curie=ADM.curie('brukernavn'),
                   model_uri=ADM.Personalressurs_brukernavn, domain=Personalressurs, range=Optional[Union[dict, "Identifikator"]])

slots.Personalressurs_jobbtittel = Slot(uri=ADM.jobbtittel, name="Personalressurs_jobbtittel", curie=ADM.curie('jobbtittel'),
                   model_uri=ADM.Personalressurs_jobbtittel, domain=Personalressurs, range=Optional[str])

slots.Personalressurs_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Personalressurs_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ADM.Personalressurs_kontaktinformasjon, domain=Personalressurs, range=Optional[Union[dict, "Kontaktinformasjon"]])

slots.Personalressurs_stedfortreder = Slot(uri=ADM.stedfortreder, name="Personalressurs_stedfortreder", curie=ADM.curie('stedfortreder'),
                   model_uri=ADM.Personalressurs_stedfortreder, domain=Personalressurs, range=Optional[Union[Union[str, FullmaktId], list[Union[str, FullmaktId]]]])

slots.Personalressurs_fullmakt = Slot(uri=ADM.fullmakt, name="Personalressurs_fullmakt", curie=ADM.curie('fullmakt'),
                   model_uri=ADM.Personalressurs_fullmakt, domain=Personalressurs, range=Optional[Union[Union[str, FullmaktId], list[Union[str, FullmaktId]]]])

slots.Personalressurs_lederFor = Slot(uri=ADM.lederFor, name="Personalressurs_lederFor", curie=ADM.curie('lederFor'),
                   model_uri=ADM.Personalressurs_lederFor, domain=Personalressurs, range=Optional[Union[Union[str, OrganisasjonselementId], list[Union[str, OrganisasjonselementId]]]])

slots.Personalressurs_arbeidsforhold = Slot(uri=ADM.arbeidsforhold, name="Personalressurs_arbeidsforhold", curie=ADM.curie('arbeidsforhold'),
                   model_uri=ADM.Personalressurs_arbeidsforhold, domain=Personalressurs, range=Optional[Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]]])

slots.Personalressurs_personalansvar = Slot(uri=ADM.personalansvar, name="Personalressurs_personalansvar", curie=ADM.curie('personalansvar'),
                   model_uri=ADM.Personalressurs_personalansvar, domain=Personalressurs, range=Optional[Union[Union[str, ArbeidsforholdId], list[Union[str, ArbeidsforholdId]]]])

slots.Personalressurs_skoleressurs = Slot(uri=ADM.skoleressurs, name="Personalressurs_skoleressurs", curie=ADM.curie('skoleressurs'),
                   model_uri=ADM.Personalressurs_skoleressurs, domain=Personalressurs, range=Optional[Union[str, URIorCURIE]])

slots.Arbeidsforhold_ansettelsesprosent = Slot(uri=ADM.ansettelsesprosent, name="Arbeidsforhold_ansettelsesprosent", curie=ADM.curie('ansettelsesprosent'),
                   model_uri=ADM.Arbeidsforhold_ansettelsesprosent, domain=Arbeidsforhold, range=int)

slots.Arbeidsforhold_aarslonn = Slot(uri=ADM.aarslonn, name="Arbeidsforhold_aarslonn", curie=ADM.curie('aarslonn'),
                   model_uri=ADM.Arbeidsforhold_aarslonn, domain=Arbeidsforhold, range=int)

slots.Arbeidsforhold_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Arbeidsforhold_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ADM.Arbeidsforhold_gyldighetsperiode, domain=Arbeidsforhold, range=Union[dict, "Periode"])

slots.Arbeidsforhold_hovedstilling = Slot(uri=ADM.hovedstilling, name="Arbeidsforhold_hovedstilling", curie=ADM.curie('hovedstilling'),
                   model_uri=ADM.Arbeidsforhold_hovedstilling, domain=Arbeidsforhold, range=Union[bool, Bool])

slots.Arbeidsforhold_lonnsprosent = Slot(uri=ADM.lonnsprosent, name="Arbeidsforhold_lonnsprosent", curie=ADM.curie('lonnsprosent'),
                   model_uri=ADM.Arbeidsforhold_lonnsprosent, domain=Arbeidsforhold, range=int)

slots.Arbeidsforhold_stillingsnummer = Slot(uri=ADM.stillingsnummer, name="Arbeidsforhold_stillingsnummer", curie=ADM.curie('stillingsnummer'),
                   model_uri=ADM.Arbeidsforhold_stillingsnummer, domain=Arbeidsforhold, range=str)

slots.Arbeidsforhold_tilstedeprosent = Slot(uri=ADM.tilstedeprosent, name="Arbeidsforhold_tilstedeprosent", curie=ADM.curie('tilstedeprosent'),
                   model_uri=ADM.Arbeidsforhold_tilstedeprosent, domain=Arbeidsforhold, range=int)

slots.Arbeidsforhold_arbeidssted = Slot(uri=ADM.arbeidssted, name="Arbeidsforhold_arbeidssted", curie=ADM.curie('arbeidssted'),
                   model_uri=ADM.Arbeidsforhold_arbeidssted, domain=Arbeidsforhold, range=Union[str, OrganisasjonselementId])

slots.Arbeidsforhold_personalressurs = Slot(uri=ADM.personalressurs, name="Arbeidsforhold_personalressurs", curie=ADM.curie('personalressurs'),
                   model_uri=ADM.Arbeidsforhold_personalressurs, domain=Arbeidsforhold, range=Union[str, PersonalressursId])

slots.Arbeidsforhold_arbeidsforholdsperiode = Slot(uri=ADM.arbeidsforholdsperiode, name="Arbeidsforhold_arbeidsforholdsperiode", curie=ADM.curie('arbeidsforholdsperiode'),
                   model_uri=ADM.Arbeidsforhold_arbeidsforholdsperiode, domain=Arbeidsforhold, range=Optional[Union[dict, "Periode"]])

slots.Arbeidsforhold_stillingstittel = Slot(uri=ADM.stillingstittel, name="Arbeidsforhold_stillingstittel", curie=ADM.curie('stillingstittel'),
                   model_uri=ADM.Arbeidsforhold_stillingstittel, domain=Arbeidsforhold, range=Optional[str])

slots.Arbeidsforhold_aktivitet = Slot(uri=ADM.aktivitet, name="Arbeidsforhold_aktivitet", curie=ADM.curie('aktivitet'),
                   model_uri=ADM.Arbeidsforhold_aktivitet, domain=Arbeidsforhold, range=Optional[Union[str, AktivitetId]])

slots.Arbeidsforhold_anlegg = Slot(uri=ADM.anlegg, name="Arbeidsforhold_anlegg", curie=ADM.curie('anlegg'),
                   model_uri=ADM.Arbeidsforhold_anlegg, domain=Arbeidsforhold, range=Optional[Union[str, AnleggId]])

slots.Arbeidsforhold_ansvar = Slot(uri=ADM.ansvar, name="Arbeidsforhold_ansvar", curie=ADM.curie('ansvar'),
                   model_uri=ADM.Arbeidsforhold_ansvar, domain=Arbeidsforhold, range=Optional[Union[str, AnsvarId]])

slots.Arbeidsforhold_arbeidsforholdstype = Slot(uri=ADM.arbeidsforholdstype, name="Arbeidsforhold_arbeidsforholdstype", curie=ADM.curie('arbeidsforholdstype'),
                   model_uri=ADM.Arbeidsforhold_arbeidsforholdstype, domain=Arbeidsforhold, range=Optional[Union[str, ArbeidsforholdstypeId]])

slots.Arbeidsforhold_art = Slot(uri=ADM.art, name="Arbeidsforhold_art", curie=ADM.curie('art'),
                   model_uri=ADM.Arbeidsforhold_art, domain=Arbeidsforhold, range=Optional[Union[str, ArtId]])

slots.Arbeidsforhold_diverse = Slot(uri=ADM.diverse, name="Arbeidsforhold_diverse", curie=ADM.curie('diverse'),
                   model_uri=ADM.Arbeidsforhold_diverse, domain=Arbeidsforhold, range=Optional[Union[str, DiverseId]])

slots.Arbeidsforhold_formaal = Slot(uri=ADM.formaal, name="Arbeidsforhold_formaal", curie=ADM.curie('formaal'),
                   model_uri=ADM.Arbeidsforhold_formaal, domain=Arbeidsforhold, range=Optional[Union[str, FormaalId]])

slots.Arbeidsforhold_funksjon = Slot(uri=ADM.funksjon, name="Arbeidsforhold_funksjon", curie=ADM.curie('funksjon'),
                   model_uri=ADM.Arbeidsforhold_funksjon, domain=Arbeidsforhold, range=Optional[Union[str, FunksjonId]])

slots.Arbeidsforhold_kontrakt = Slot(uri=ADM.kontrakt, name="Arbeidsforhold_kontrakt", curie=ADM.curie('kontrakt'),
                   model_uri=ADM.Arbeidsforhold_kontrakt, domain=Arbeidsforhold, range=Optional[Union[str, KontraktId]])

slots.Arbeidsforhold_lopenummer = Slot(uri=ADM.lopenummer, name="Arbeidsforhold_lopenummer", curie=ADM.curie('lopenummer'),
                   model_uri=ADM.Arbeidsforhold_lopenummer, domain=Arbeidsforhold, range=Optional[Union[str, LopenummerId]])

slots.Arbeidsforhold_objekt = Slot(uri=ADM.objekt, name="Arbeidsforhold_objekt", curie=ADM.curie('objekt'),
                   model_uri=ADM.Arbeidsforhold_objekt, domain=Arbeidsforhold, range=Optional[Union[str, ObjektId]])

slots.Arbeidsforhold_prosjekt = Slot(uri=ADM.prosjekt, name="Arbeidsforhold_prosjekt", curie=ADM.curie('prosjekt'),
                   model_uri=ADM.Arbeidsforhold_prosjekt, domain=Arbeidsforhold, range=Optional[Union[str, ProsjektId]])

slots.Arbeidsforhold_ramme = Slot(uri=ADM.ramme, name="Arbeidsforhold_ramme", curie=ADM.curie('ramme'),
                   model_uri=ADM.Arbeidsforhold_ramme, domain=Arbeidsforhold, range=Optional[Union[str, RammeId]])

slots.Arbeidsforhold_stillingskode = Slot(uri=ADM.stillingskode, name="Arbeidsforhold_stillingskode", curie=ADM.curie('stillingskode'),
                   model_uri=ADM.Arbeidsforhold_stillingskode, domain=Arbeidsforhold, range=Optional[Union[str, StillingskodeId]])

slots.Arbeidsforhold_timerPerUke = Slot(uri=ADM.timerPerUke, name="Arbeidsforhold_timerPerUke", curie=ADM.curie('timerPerUke'),
                   model_uri=ADM.Arbeidsforhold_timerPerUke, domain=Arbeidsforhold, range=Optional[Union[str, UketimetallId]])

slots.Arbeidsforhold_arbeidslokasjon = Slot(uri=ADM.arbeidslokasjon, name="Arbeidsforhold_arbeidslokasjon", curie=ADM.curie('arbeidslokasjon'),
                   model_uri=ADM.Arbeidsforhold_arbeidslokasjon, domain=Arbeidsforhold, range=Optional[Union[str, ArbeidslokasjonId]])

slots.Arbeidsforhold_fastlonn = Slot(uri=ADM.fastlonn, name="Arbeidsforhold_fastlonn", curie=ADM.curie('fastlonn'),
                   model_uri=ADM.Arbeidsforhold_fastlonn, domain=Arbeidsforhold, range=Optional[Union[Union[str, FastlonnId], list[Union[str, FastlonnId]]]])

slots.Arbeidsforhold_fasttillegg = Slot(uri=ADM.fasttillegg, name="Arbeidsforhold_fasttillegg", curie=ADM.curie('fasttillegg'),
                   model_uri=ADM.Arbeidsforhold_fasttillegg, domain=Arbeidsforhold, range=Optional[Union[Union[str, FasttilleggId], list[Union[str, FasttilleggId]]]])

slots.Arbeidsforhold_fravaer = Slot(uri=ADM.fravaer, name="Arbeidsforhold_fravaer", curie=ADM.curie('fravaer'),
                   model_uri=ADM.Arbeidsforhold_fravaer, domain=Arbeidsforhold, range=Optional[Union[Union[str, FravaerId], list[Union[str, FravaerId]]]])

slots.Arbeidsforhold_variabellonn = Slot(uri=ADM.variabellonn, name="Arbeidsforhold_variabellonn", curie=ADM.curie('variabellonn'),
                   model_uri=ADM.Arbeidsforhold_variabellonn, domain=Arbeidsforhold, range=Optional[Union[Union[str, VariabellonnId], list[Union[str, VariabellonnId]]]])

slots.Arbeidsforhold_personalleder = Slot(uri=ADM.personalleder, name="Arbeidsforhold_personalleder", curie=ADM.curie('personalleder'),
                   model_uri=ADM.Arbeidsforhold_personalleder, domain=Arbeidsforhold, range=Optional[Union[str, PersonalressursId]])

slots.Arbeidsforhold_undervisningsforhold = Slot(uri=ADM.undervisningsforhold, name="Arbeidsforhold_undervisningsforhold", curie=ADM.curie('undervisningsforhold'),
                   model_uri=ADM.Arbeidsforhold_undervisningsforhold, domain=Arbeidsforhold, range=Optional[Union[str, URIorCURIE]])

slots.Aktoer_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Aktoer_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ADM.Aktoer_kontaktinformasjon, domain=Aktoer, range=Optional[Union[dict, "Kontaktinformasjon"]])

slots.Aktoer_postadresse = Slot(uri=FINT.postadresse, name="Aktoer_postadresse", curie=FINT.curie('postadresse'),
                   model_uri=ADM.Aktoer_postadresse, domain=Aktoer, range=Optional[Union[dict, "Adresse"]])

slots.Begrep_kode = Slot(uri=FINT.kode, name="Begrep_kode", curie=FINT.curie('kode'),
                   model_uri=ADM.Begrep_kode, domain=Begrep, range=str)

slots.Begrep_navn = Slot(uri=FINT.navn, name="Begrep_navn", curie=FINT.curie('navn'),
                   model_uri=ADM.Begrep_navn, domain=Begrep, range=str)

slots.Begrep_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Begrep_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ADM.Begrep_gyldighetsperiode, domain=Begrep, range=Optional[Union[dict, "Periode"]])

slots.Begrep_passiv = Slot(uri=FINT.passiv, name="Begrep_passiv", curie=FINT.curie('passiv'),
                   model_uri=ADM.Begrep_passiv, domain=Begrep, range=Optional[Union[bool, Bool]])

slots.Elev_elevnummer = Slot(uri=FINT.elevnummer, name="Elev_elevnummer", curie=FINT.curie('elevnummer'),
                   model_uri=ADM.Elev_elevnummer, domain=Elev, range=Optional[Union[dict, "Identifikator"]])

slots.Elev_person = Slot(uri=FINT.person, name="Elev_person", curie=FINT.curie('person'),
                   model_uri=ADM.Elev_person, domain=Elev, range=Optional[Union[str, PersonId]])

slots.Enhet_forretningsadresse = Slot(uri=FINT.forretningsadresse, name="Enhet_forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=ADM.Enhet_forretningsadresse, domain=Enhet, range=Optional[Union[dict, "Adresse"]])

slots.Enhet_organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="Enhet_organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=ADM.Enhet_organisasjonsnavn, domain=Enhet, range=Optional[str])

slots.Enhet_organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="Enhet_organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=ADM.Enhet_organisasjonsnummer, domain=Enhet, range=Optional[Union[dict, "Identifikator"]])

slots.Identifikator_identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="Identifikator_identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=ADM.Identifikator_identifikatorverdi, domain=Identifikator, range=str)

slots.Periode_start = Slot(uri=FINT.start, name="Periode_start", curie=FINT.curie('start'),
                   model_uri=ADM.Periode_start, domain=Periode, range=Union[str, XSDDateTime])

slots.Personnavn_fornavn = Slot(uri=FINT.fornavn, name="Personnavn_fornavn", curie=FINT.curie('fornavn'),
                   model_uri=ADM.Personnavn_fornavn, domain=Personnavn, range=str)

slots.Personnavn_etternavn = Slot(uri=FINT.etternavn, name="Personnavn_etternavn", curie=FINT.curie('etternavn'),
                   model_uri=ADM.Personnavn_etternavn, domain=Personnavn, range=str)

slots.Fylke_kommune = Slot(uri=FINT.kommune, name="Fylke_kommune", curie=FINT.curie('kommune'),
                   model_uri=ADM.Fylke_kommune, domain=Fylke, range=Optional[Union[Union[str, KommuneId], list[Union[str, KommuneId]]]])

slots.Kommune_fylke = Slot(uri=FINT.fylke, name="Kommune_fylke", curie=FINT.curie('fylke'),
                   model_uri=ADM.Kommune_fylke, domain=Kommune, range=Union[str, FylkeId])

slots.Valuta_bokstavkode = Slot(uri=FINT.bokstavkode, name="Valuta_bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=ADM.Valuta_bokstavkode, domain=Valuta, range=Union[dict, Identifikator])

slots.Valuta_valuta_navn = Slot(uri=FINT.valutaNavn, name="Valuta_valuta_navn", curie=FINT.curie('valutaNavn'),
                   model_uri=ADM.Valuta_valuta_navn, domain=Valuta, range=str)

slots.Valuta_nummerkode = Slot(uri=FINT.nummerkode, name="Valuta_nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=ADM.Valuta_nummerkode, domain=Valuta, range=Union[dict, Identifikator])

slots.Person_fodselsnummer = Slot(uri=FINT.fodselsnummer, name="Person_fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=ADM.Person_fodselsnummer, domain=Person, range=Union[dict, Identifikator])

slots.Person_person_navn = Slot(uri=FINT.personNavn, name="Person_person_navn", curie=FINT.curie('personNavn'),
                   model_uri=ADM.Person_person_navn, domain=Person, range=Union[dict, Personnavn])

slots.Person_bilde = Slot(uri=FINT.bilde, name="Person_bilde", curie=FINT.curie('bilde'),
                   model_uri=ADM.Person_bilde, domain=Person, range=Optional[str])

slots.Person_bostedsadresse = Slot(uri=FINT.bostedsadresse, name="Person_bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=ADM.Person_bostedsadresse, domain=Person, range=Optional[Union[dict, Adresse]])

slots.Person_fodselsdato = Slot(uri=FINT.fodselsdato, name="Person_fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=ADM.Person_fodselsdato, domain=Person, range=Optional[Union[str, XSDDate]])

slots.Person_parorende = Slot(uri=FINT.parorende, name="Person_parorende", curie=FINT.curie('parorende'),
                   model_uri=ADM.Person_parorende, domain=Person, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.Person_statsborgerskap = Slot(uri=FINT.statsborgerskap, name="Person_statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=ADM.Person_statsborgerskap, domain=Person, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.Person_kommune = Slot(uri=FINT.kommune, name="Person_kommune", curie=FINT.curie('kommune'),
                   model_uri=ADM.Person_kommune, domain=Person, range=Optional[Union[str, KommuneId]])

slots.Person_kjonn = Slot(uri=FINT.kjonn, name="Person_kjonn", curie=FINT.curie('kjonn'),
                   model_uri=ADM.Person_kjonn, domain=Person, range=Optional[Union[str, KjonnId]])

slots.Person_foreldreansvar = Slot(uri=FINT.foreldreansvar, name="Person_foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=ADM.Person_foreldreansvar, domain=Person, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Person_foreldre = Slot(uri=FINT.foreldre, name="Person_foreldre", curie=FINT.curie('foreldre'),
                   model_uri=ADM.Person_foreldre, domain=Person, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Person_maalform = Slot(uri=FINT.maalform, name="Person_maalform", curie=FINT.curie('maalform'),
                   model_uri=ADM.Person_maalform, domain=Person, range=Optional[Union[str, SpraakId]])

slots.Person_morsmaal = Slot(uri=FINT.morsmaal, name="Person_morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=ADM.Person_morsmaal, domain=Person, range=Optional[Union[str, SpraakId]])

slots.Person_laerling = Slot(uri=FINT.laerling, name="Person_laerling", curie=FINT.curie('laerling'),
                   model_uri=ADM.Person_laerling, domain=Person, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Person_elev = Slot(uri=FINT.elev, name="Person_elev", curie=FINT.curie('elev'),
                   model_uri=ADM.Person_elev, domain=Person, range=Optional[Union[str, ElevId]])

slots.Person_otungdom = Slot(uri=FINT.otungdom, name="Person_otungdom", curie=FINT.curie('otungdom'),
                   model_uri=ADM.Person_otungdom, domain=Person, range=Optional[Union[str, URIorCURIE]])

slots.Kontaktperson_type = Slot(uri=FINT.type, name="Kontaktperson_type", curie=FINT.curie('type'),
                   model_uri=ADM.Kontaktperson_type, domain=Kontaktperson, range=str)

slots.Kontaktperson_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Kontaktperson_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ADM.Kontaktperson_kontaktinformasjon, domain=Kontaktperson, range=Optional[Union[dict, Kontaktinformasjon]])

slots.Kontaktperson_kontaktperson_navn = Slot(uri=FINT.kontaktpersonNavn, name="Kontaktperson_kontaktperson_navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=ADM.Kontaktperson_kontaktperson_navn, domain=Kontaktperson, range=Optional[Union[dict, Personnavn]])

slots.Kontaktperson_kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="Kontaktperson_kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=ADM.Kontaktperson_kontaktperson, domain=Kontaktperson, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Virksomhet_virksomhetsId = Slot(uri=FINT.virksomhetsId, name="Virksomhet_virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=ADM.Virksomhet_virksomhetsId, domain=Virksomhet, range=Union[dict, Identifikator])

slots.Virksomhet_laerling = Slot(uri=FINT.laerling, name="Virksomhet_laerling", curie=FINT.curie('laerling'),
                   model_uri=ADM.Virksomhet_laerling, domain=Virksomhet, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

