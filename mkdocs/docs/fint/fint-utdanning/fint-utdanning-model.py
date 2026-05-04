# Auto generated from fint-utdanning-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-04T20:07:44
# Schema: fint-utdanning
#
# id: https://data.norge.no/linkml/fint-utdanning
# description: FINT-domenemodell for utdanning. Dekkjer elevar, skular, skoleressursar, elevforhold, undervisningsforhold, klasser, undervisningsgrupper, faggrupper, kontaktlærergrupper, utdanningsprogram, programområde, vurdering, lærling og OT.
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
UTD = CurieNamespace('utd', 'https://schema.fintlabs.no/utdanning/')
DEFAULT_ = UTD


# Types

# Class references
class GruppeId(URIorCURIE):
    pass


class GruppemedlemskapId(URIorCURIE):
    pass


class UtdanningsforholdId(URIorCURIE):
    pass


class ElevId(URIorCURIE):
    pass


class ElevforholdId(URIorCURIE):
    pass


class ElevtilretteleggingId(URIorCURIE):
    pass


class KlasseId(GruppeId):
    pass


class KlassemedlemskapId(GruppemedlemskapId):
    pass


class KontaktlaerergruppeId(GruppeId):
    pass


class KontaktlaerergruppemedlemskapId(GruppemedlemskapId):
    pass


class PersongruppeId(GruppeId):
    pass


class PersongruppemedlemskapId(GruppemedlemskapId):
    pass


class SkoleId(URIorCURIE):
    pass


class SkoleressursId(URIorCURIE):
    pass


class VarselId(URIorCURIE):
    pass


class ArstrinnId(GruppeId):
    pass


class ProgramomradeId(GruppeId):
    pass


class ProgramomrademedlemskapId(GruppemedlemskapId):
    pass


class UtdanningsprogramId(GruppeId):
    pass


class EksamenId(URIorCURIE):
    pass


class FagId(GruppeId):
    pass


class FaggruppeId(GruppeId):
    pass


class FaggruppemedlemskapId(GruppemedlemskapId):
    pass


class RomId(URIorCURIE):
    pass


class TimeId(URIorCURIE):
    pass


class UndervisningsforholdId(UtdanningsforholdId):
    pass


class UndervisningsgruppeId(GruppeId):
    pass


class UndervisningsgruppemedlemskapId(GruppemedlemskapId):
    pass


class FagvurderingAbstraktId(URIorCURIE):
    pass


class OrdensvurderingAbstraktId(URIorCURIE):
    pass


class AnmerkningerId(URIorCURIE):
    pass


class EksamensgruppeId(GruppeId):
    pass


class EksamensgruppemedlemskapId(GruppemedlemskapId):
    pass


class EksamensvurderingId(FagvurderingAbstraktId):
    pass


class ElevfravarId(URIorCURIE):
    pass


class ElevvurderingId(URIorCURIE):
    pass


class FravarsoversiktId(URIorCURIE):
    pass


class FraversregistreringId(URIorCURIE):
    pass


class HalvaarsfagvurderingId(FagvurderingAbstraktId):
    pass


class HalvaarsordensvurderingId(OrdensvurderingAbstraktId):
    pass


class KarakterhistorieId(URIorCURIE):
    pass


class SensorId(URIorCURIE):
    pass


class SluttfagvurderingId(FagvurderingAbstraktId):
    pass


class SluttordensvurderingId(OrdensvurderingAbstraktId):
    pass


class UnderveisfagvurderingId(FagvurderingAbstraktId):
    pass


class UnderveisordensvurderingId(OrdensvurderingAbstraktId):
    pass


class AvlagtProveId(URIorCURIE):
    pass


class LaerlingId(URIorCURIE):
    pass


class OtUngdomId(URIorCURIE):
    pass


class AvbruddsaarsakId(URIorCURIE):
    pass


class BetalingsstatusId(URIorCURIE):
    pass


class BevistypeId(URIorCURIE):
    pass


class BrevtypeId(URIorCURIE):
    pass


class EksamensformId(URIorCURIE):
    pass


class ElevkategoriId(URIorCURIE):
    pass


class FagmerknadId(URIorCURIE):
    pass


class FagstatusId(URIorCURIE):
    pass


class FravartypeId(URIorCURIE):
    pass


class FullfortkodeId(URIorCURIE):
    pass


class KarakterskalaId(URIorCURIE):
    pass


class KarakterstatusId(URIorCURIE):
    pass


class KarakterverdiId(URIorCURIE):
    pass


class OtEnhetId(URIorCURIE):
    pass


class OtStatusId(URIorCURIE):
    pass


class ProvestatusId(URIorCURIE):
    pass


class SkoleaarId(URIorCURIE):
    pass


class SkoleeiertypeId(URIorCURIE):
    pass


class TerminId(URIorCURIE):
    pass


class TilretteleggingId(URIorCURIE):
    pass


class VarseltypeId(URIorCURIE):
    pass


class VitnemalsmerknadId(URIorCURIE):
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
class UtdanningContainer(YAMLRoot):
    """
    Rotcontainer for FINT Utdanning-instansar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["UtdanningContainer"]
    class_class_curie: ClassVar[str] = "utd:UtdanningContainer"
    class_name: ClassVar[str] = "UtdanningContainer"
    class_model_uri: ClassVar[URIRef] = UTD.UtdanningContainer

    elevar: Optional[Union[dict[Union[str, ElevId], Union[dict, "Elev"]], list[Union[dict, "Elev"]]]] = empty_dict()
    skolar: Optional[Union[dict[Union[str, SkoleId], Union[dict, "Skole"]], list[Union[dict, "Skole"]]]] = empty_dict()
    skoleressursar: Optional[Union[dict[Union[str, SkoleressursId], Union[dict, "Skoleressurs"]], list[Union[dict, "Skoleressurs"]]]] = empty_dict()
    elevforhold: Optional[Union[dict[Union[str, ElevforholdId], Union[dict, "Elevforhold"]], list[Union[dict, "Elevforhold"]]]] = empty_dict()
    elevtilrettelegging: Optional[Union[dict[Union[str, ElevtilretteleggingId], Union[dict, "Elevtilrettelegging"]], list[Union[dict, "Elevtilrettelegging"]]]] = empty_dict()
    klasser: Optional[Union[dict[Union[str, KlasseId], Union[dict, "Klasse"]], list[Union[dict, "Klasse"]]]] = empty_dict()
    klassemedlemskap: Optional[Union[dict[Union[str, KlassemedlemskapId], Union[dict, "Klassemedlemskap"]], list[Union[dict, "Klassemedlemskap"]]]] = empty_dict()
    kontaktlaerergrupper: Optional[Union[dict[Union[str, KontaktlaerergruppeId], Union[dict, "Kontaktlaerergruppe"]], list[Union[dict, "Kontaktlaerergruppe"]]]] = empty_dict()
    kontaktlaerergruppemedlemskap: Optional[Union[dict[Union[str, KontaktlaerergruppemedlemskapId], Union[dict, "Kontaktlaerergruppemedlemskap"]], list[Union[dict, "Kontaktlaerergruppemedlemskap"]]]] = empty_dict()
    persongrupper: Optional[Union[dict[Union[str, PersongruppeId], Union[dict, "Persongruppe"]], list[Union[dict, "Persongruppe"]]]] = empty_dict()
    persongruppemedlemskap: Optional[Union[dict[Union[str, PersongruppemedlemskapId], Union[dict, "Persongruppemedlemskap"]], list[Union[dict, "Persongruppemedlemskap"]]]] = empty_dict()
    varsel: Optional[Union[dict[Union[str, VarselId], Union[dict, "Varsel"]], list[Union[dict, "Varsel"]]]] = empty_dict()
    arstrinn: Optional[Union[dict[Union[str, ArstrinnId], Union[dict, "Arstrinn"]], list[Union[dict, "Arstrinn"]]]] = empty_dict()
    programomrader: Optional[Union[dict[Union[str, ProgramomradeId], Union[dict, "Programomrade"]], list[Union[dict, "Programomrade"]]]] = empty_dict()
    programomrademedlemskap: Optional[Union[dict[Union[str, ProgramomrademedlemskapId], Union[dict, "Programomrademedlemskap"]], list[Union[dict, "Programomrademedlemskap"]]]] = empty_dict()
    utdanningsprogram: Optional[Union[dict[Union[str, UtdanningsprogramId], Union[dict, "Utdanningsprogram"]], list[Union[dict, "Utdanningsprogram"]]]] = empty_dict()
    eksamen: Optional[Union[dict[Union[str, EksamenId], Union[dict, "Eksamen"]], list[Union[dict, "Eksamen"]]]] = empty_dict()
    fag: Optional[Union[dict[Union[str, FagId], Union[dict, "Fag"]], list[Union[dict, "Fag"]]]] = empty_dict()
    faggrupper: Optional[Union[dict[Union[str, FaggruppeId], Union[dict, "Faggruppe"]], list[Union[dict, "Faggruppe"]]]] = empty_dict()
    faggruppemedlemskap: Optional[Union[dict[Union[str, FaggruppemedlemskapId], Union[dict, "Faggruppemedlemskap"]], list[Union[dict, "Faggruppemedlemskap"]]]] = empty_dict()
    rom: Optional[Union[dict[Union[str, RomId], Union[dict, "Rom"]], list[Union[dict, "Rom"]]]] = empty_dict()
    timar: Optional[Union[dict[Union[str, TimeId], Union[dict, "Time"]], list[Union[dict, "Time"]]]] = empty_dict()
    undervisningsforhold: Optional[Union[dict[Union[str, UndervisningsforholdId], Union[dict, "Undervisningsforhold"]], list[Union[dict, "Undervisningsforhold"]]]] = empty_dict()
    undervisningsgrupper: Optional[Union[dict[Union[str, UndervisningsgruppeId], Union[dict, "Undervisningsgruppe"]], list[Union[dict, "Undervisningsgruppe"]]]] = empty_dict()
    undervisningsgruppemedlemskap: Optional[Union[dict[Union[str, UndervisningsgruppemedlemskapId], Union[dict, "Undervisningsgruppemedlemskap"]], list[Union[dict, "Undervisningsgruppemedlemskap"]]]] = empty_dict()
    anmerkningar: Optional[Union[dict[Union[str, AnmerkningerId], Union[dict, "Anmerkninger"]], list[Union[dict, "Anmerkninger"]]]] = empty_dict()
    eksamensgrupper: Optional[Union[dict[Union[str, EksamensgruppeId], Union[dict, "Eksamensgruppe"]], list[Union[dict, "Eksamensgruppe"]]]] = empty_dict()
    eksamensgruppemedlemskap: Optional[Union[dict[Union[str, EksamensgruppemedlemskapId], Union[dict, "Eksamensgruppemedlemskap"]], list[Union[dict, "Eksamensgruppemedlemskap"]]]] = empty_dict()
    eksamensvurdering: Optional[Union[dict[Union[str, EksamensvurderingId], Union[dict, "Eksamensvurdering"]], list[Union[dict, "Eksamensvurdering"]]]] = empty_dict()
    elevfravar: Optional[Union[dict[Union[str, ElevfravarId], Union[dict, "Elevfravar"]], list[Union[dict, "Elevfravar"]]]] = empty_dict()
    elevvurdering: Optional[Union[dict[Union[str, ElevvurderingId], Union[dict, "Elevvurdering"]], list[Union[dict, "Elevvurdering"]]]] = empty_dict()
    fravarsoversikt: Optional[Union[dict[Union[str, FravarsoversiktId], Union[dict, "Fravarsoversikt"]], list[Union[dict, "Fravarsoversikt"]]]] = empty_dict()
    fraversregistrering: Optional[Union[dict[Union[str, FraversregistreringId], Union[dict, "Fraversregistrering"]], list[Union[dict, "Fraversregistrering"]]]] = empty_dict()
    halvaarsfagvurdering: Optional[Union[dict[Union[str, HalvaarsfagvurderingId], Union[dict, "Halvaarsfagvurdering"]], list[Union[dict, "Halvaarsfagvurdering"]]]] = empty_dict()
    halvaarsordensvurdering: Optional[Union[dict[Union[str, HalvaarsordensvurderingId], Union[dict, "Halvaarsordensvurdering"]], list[Union[dict, "Halvaarsordensvurdering"]]]] = empty_dict()
    karakterhistorie: Optional[Union[dict[Union[str, KarakterhistorieId], Union[dict, "Karakterhistorie"]], list[Union[dict, "Karakterhistorie"]]]] = empty_dict()
    sensor: Optional[Union[dict[Union[str, SensorId], Union[dict, "Sensor"]], list[Union[dict, "Sensor"]]]] = empty_dict()
    sluttfagvurdering: Optional[Union[dict[Union[str, SluttfagvurderingId], Union[dict, "Sluttfagvurdering"]], list[Union[dict, "Sluttfagvurdering"]]]] = empty_dict()
    sluttordensvurdering: Optional[Union[dict[Union[str, SluttordensvurderingId], Union[dict, "Sluttordensvurdering"]], list[Union[dict, "Sluttordensvurdering"]]]] = empty_dict()
    underveisfagvurdering: Optional[Union[dict[Union[str, UnderveisfagvurderingId], Union[dict, "Underveisfagvurdering"]], list[Union[dict, "Underveisfagvurdering"]]]] = empty_dict()
    underveisordensvurdering: Optional[Union[dict[Union[str, UnderveisordensvurderingId], Union[dict, "Underveisordensvurdering"]], list[Union[dict, "Underveisordensvurdering"]]]] = empty_dict()
    avlagteprover: Optional[Union[dict[Union[str, AvlagtProveId], Union[dict, "AvlagtProve"]], list[Union[dict, "AvlagtProve"]]]] = empty_dict()
    laerlingar: Optional[Union[dict[Union[str, LaerlingId], Union[dict, "Laerling"]], list[Union[dict, "Laerling"]]]] = empty_dict()
    otUngdom: Optional[Union[dict[Union[str, OtUngdomId], Union[dict, "OtUngdom"]], list[Union[dict, "OtUngdom"]]]] = empty_dict()
    avbruddsaarsaker: Optional[Union[dict[Union[str, AvbruddsaarsakId], Union[dict, "Avbruddsaarsak"]], list[Union[dict, "Avbruddsaarsak"]]]] = empty_dict()
    betalingsstatus: Optional[Union[dict[Union[str, BetalingsstatusId], Union[dict, "Betalingsstatus"]], list[Union[dict, "Betalingsstatus"]]]] = empty_dict()
    bevistypar: Optional[Union[dict[Union[str, BevistypeId], Union[dict, "Bevistype"]], list[Union[dict, "Bevistype"]]]] = empty_dict()
    brevtypar: Optional[Union[dict[Union[str, BrevtypeId], Union[dict, "Brevtype"]], list[Union[dict, "Brevtype"]]]] = empty_dict()
    eksamensformer: Optional[Union[dict[Union[str, EksamensformId], Union[dict, "Eksamensform"]], list[Union[dict, "Eksamensform"]]]] = empty_dict()
    elevkategoriar: Optional[Union[dict[Union[str, ElevkategoriId], Union[dict, "Elevkategori"]], list[Union[dict, "Elevkategori"]]]] = empty_dict()
    fagmerknader: Optional[Union[dict[Union[str, FagmerknadId], Union[dict, "Fagmerknad"]], list[Union[dict, "Fagmerknad"]]]] = empty_dict()
    fagstatus: Optional[Union[dict[Union[str, FagstatusId], Union[dict, "Fagstatus"]], list[Union[dict, "Fagstatus"]]]] = empty_dict()
    fravartypar: Optional[Union[dict[Union[str, FravartypeId], Union[dict, "Fravartype"]], list[Union[dict, "Fravartype"]]]] = empty_dict()
    fullfortkoder: Optional[Union[dict[Union[str, FullfortkodeId], Union[dict, "Fullfortkode"]], list[Union[dict, "Fullfortkode"]]]] = empty_dict()
    karakterskalaer: Optional[Union[dict[Union[str, KarakterskalaId], Union[dict, "Karakterskala"]], list[Union[dict, "Karakterskala"]]]] = empty_dict()
    karakterstatus: Optional[Union[dict[Union[str, KarakterstatusId], Union[dict, "Karakterstatus"]], list[Union[dict, "Karakterstatus"]]]] = empty_dict()
    karakterverdiar: Optional[Union[dict[Union[str, KarakterverdiId], Union[dict, "Karakterverdi"]], list[Union[dict, "Karakterverdi"]]]] = empty_dict()
    otEnheter: Optional[Union[dict[Union[str, OtEnhetId], Union[dict, "OtEnhet"]], list[Union[dict, "OtEnhet"]]]] = empty_dict()
    otStatus: Optional[Union[dict[Union[str, OtStatusId], Union[dict, "OtStatus"]], list[Union[dict, "OtStatus"]]]] = empty_dict()
    provestatuser: Optional[Union[dict[Union[str, ProvestatusId], Union[dict, "Provestatus"]], list[Union[dict, "Provestatus"]]]] = empty_dict()
    skoleaar: Optional[Union[dict[Union[str, SkoleaarId], Union[dict, "Skoleaar"]], list[Union[dict, "Skoleaar"]]]] = empty_dict()
    skoleeijartypar: Optional[Union[dict[Union[str, SkoleeiertypeId], Union[dict, "Skoleeiertype"]], list[Union[dict, "Skoleeiertype"]]]] = empty_dict()
    terminar: Optional[Union[dict[Union[str, TerminId], Union[dict, "Termin"]], list[Union[dict, "Termin"]]]] = empty_dict()
    tilrettelegging: Optional[Union[dict[Union[str, TilretteleggingId], Union[dict, "Tilrettelegging"]], list[Union[dict, "Tilrettelegging"]]]] = empty_dict()
    varseltypar: Optional[Union[dict[Union[str, VarseltypeId], Union[dict, "Varseltype"]], list[Union[dict, "Varseltype"]]]] = empty_dict()
    vitnemalsmerknad: Optional[Union[dict[Union[str, VitnemalsmerknadId], Union[dict, "Vitnemalsmerknad"]], list[Union[dict, "Vitnemalsmerknad"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="elevar", slot_type=Elev, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="skolar", slot_type=Skole, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="skoleressursar", slot_type=Skoleressurs, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="elevforhold", slot_type=Elevforhold, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="elevtilrettelegging", slot_type=Elevtilrettelegging, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="klasser", slot_type=Klasse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="klassemedlemskap", slot_type=Klassemedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kontaktlaerergrupper", slot_type=Kontaktlaerergruppe, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kontaktlaerergruppemedlemskap", slot_type=Kontaktlaerergruppemedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="persongrupper", slot_type=Persongruppe, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="persongruppemedlemskap", slot_type=Persongruppemedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="varsel", slot_type=Varsel, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="arstrinn", slot_type=Arstrinn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="programomrader", slot_type=Programomrade, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="programomrademedlemskap", slot_type=Programomrademedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="utdanningsprogram", slot_type=Utdanningsprogram, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="eksamen", slot_type=Eksamen, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fag", slot_type=Fag, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="faggrupper", slot_type=Faggruppe, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="faggruppemedlemskap", slot_type=Faggruppemedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rom", slot_type=Rom, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="timar", slot_type=Time, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="undervisningsforhold", slot_type=Undervisningsforhold, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="undervisningsgrupper", slot_type=Undervisningsgruppe, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="undervisningsgruppemedlemskap", slot_type=Undervisningsgruppemedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="anmerkningar", slot_type=Anmerkninger, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="eksamensgrupper", slot_type=Eksamensgruppe, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="eksamensgruppemedlemskap", slot_type=Eksamensgruppemedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="eksamensvurdering", slot_type=Eksamensvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="elevfravar", slot_type=Elevfravar, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="elevvurdering", slot_type=Elevvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fravarsoversikt", slot_type=Fravarsoversikt, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fraversregistrering", slot_type=Fraversregistrering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="halvaarsfagvurdering", slot_type=Halvaarsfagvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="halvaarsordensvurdering", slot_type=Halvaarsordensvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="karakterhistorie", slot_type=Karakterhistorie, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sensor", slot_type=Sensor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sluttfagvurdering", slot_type=Sluttfagvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sluttordensvurdering", slot_type=Sluttordensvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="underveisfagvurdering", slot_type=Underveisfagvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="underveisordensvurdering", slot_type=Underveisordensvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="avlagteprover", slot_type=AvlagtProve, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="laerlingar", slot_type=Laerling, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="otUngdom", slot_type=OtUngdom, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="avbruddsaarsaker", slot_type=Avbruddsaarsak, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="betalingsstatus", slot_type=Betalingsstatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="bevistypar", slot_type=Bevistype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="brevtypar", slot_type=Brevtype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="eksamensformer", slot_type=Eksamensform, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="elevkategoriar", slot_type=Elevkategori, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fagmerknader", slot_type=Fagmerknad, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fagstatus", slot_type=Fagstatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fravartypar", slot_type=Fravartype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fullfortkoder", slot_type=Fullfortkode, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="karakterskalaer", slot_type=Karakterskala, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="karakterstatus", slot_type=Karakterstatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="karakterverdiar", slot_type=Karakterverdi, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="otEnheter", slot_type=OtEnhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="otStatus", slot_type=OtStatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="provestatuser", slot_type=Provestatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="skoleaar", slot_type=Skoleaar, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="skoleeijartypar", slot_type=Skoleeiertype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="terminar", slot_type=Termin, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tilrettelegging", slot_type=Tilrettelegging, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="varseltypar", slot_type=Varseltype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="vitnemalsmerknad", slot_type=Vitnemalsmerknad, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Gruppe(YAMLRoot):
    """
    Abstrakt basisklasse for alle gruppetypar i utdanning.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Gruppe"]
    class_class_curie: ClassVar[str] = "utd:Gruppe"
    class_name: ClassVar[str] = "Gruppe"
    class_model_uri: ClassVar[URIRef] = UTD.Gruppe

    id: Union[str, GruppeId] = None
    navn: str = None
    beskrivelse: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GruppeId):
            self.id = GruppeId(self.id)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Gruppemedlemskap(YAMLRoot):
    """
    Abstrakt basisklasse for gruppemedlemskapar i utdanning.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Gruppemedlemskap"]
    class_class_curie: ClassVar[str] = "utd:Gruppemedlemskap"
    class_name: ClassVar[str] = "Gruppemedlemskap"
    class_model_uri: ClassVar[URIRef] = UTD.Gruppemedlemskap

    id: Union[str, GruppemedlemskapId] = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GruppemedlemskapId):
            self.id = GruppemedlemskapId(self.id)

        if self.gyldighetsperiode is not None and not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Utdanningsforhold(YAMLRoot):
    """
    Abstrakt basisklasse for undervisningsforhold i utdanning.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Utdanningsforhold"]
    class_class_curie: ClassVar[str] = "utd:Utdanningsforhold"
    class_name: ClassVar[str] = "Utdanningsforhold"
    class_model_uri: ClassVar[URIRef] = UTD.Utdanningsforhold

    id: Union[str, UtdanningsforholdId] = None
    beskrivelse: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UtdanningsforholdId):
            self.id = UtdanningsforholdId(self.id)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Elev(YAMLRoot):
    """
    Ein elev registrert i skulesystemet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Elev"]
    class_class_curie: ClassVar[str] = "utd:Elev"
    class_name: ClassVar[str] = "Elev"
    class_model_uri: ClassVar[URIRef] = UTD.Elev

    id: Union[str, ElevId] = None
    elevnummer: Optional[Union[dict, "Identifikator"]] = None
    person: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElevId):
            self.id = ElevId(self.id)

        if self.elevnummer is not None and not isinstance(self.elevnummer, Identifikator):
            self.elevnummer = Identifikator(**as_dict(self.elevnummer))

        if self.person is not None and not isinstance(self.person, URIorCURIE):
            self.person = URIorCURIE(self.person)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Elevforhold(YAMLRoot):
    """
    Eit elevs tilknyting til ein skule og eit skoleår.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Elevforhold"]
    class_class_curie: ClassVar[str] = "utd:Elevforhold"
    class_name: ClassVar[str] = "Elevforhold"
    class_model_uri: ClassVar[URIRef] = UTD.Elevforhold

    id: Union[str, ElevforholdId] = None
    beskrivelse: str = None
    elev: Union[str, ElevId] = None
    skole: Union[str, SkoleId] = None
    avbruddsdato: Optional[Union[str, XSDDate]] = None
    tosprakligFagopplaering: Optional[Union[bool, Bool]] = None
    kategori: Optional[Union[str, ElevkategoriId]] = None
    avbruddsarsak: Optional[Union[str, AvbruddsaarsakId]] = None
    skoleaar: Optional[Union[str, SkoleaarId]] = None
    programomrademedlemskap: Optional[Union[Union[str, ProgramomrademedlemskapId], list[Union[str, ProgramomrademedlemskapId]]]] = empty_list()
    klassemedlemskap: Optional[Union[Union[str, KlassemedlemskapId], list[Union[str, KlassemedlemskapId]]]] = empty_list()
    faggruppemedlemskap: Optional[Union[Union[str, FaggruppemedlemskapId], list[Union[str, FaggruppemedlemskapId]]]] = empty_list()
    undervisningsgruppemedlemskap: Optional[Union[Union[str, UndervisningsgruppemedlemskapId], list[Union[str, UndervisningsgruppemedlemskapId]]]] = empty_list()
    kontaktlaerergruppemedlemskap: Optional[Union[Union[str, KontaktlaerergruppemedlemskapId], list[Union[str, KontaktlaerergruppemedlemskapId]]]] = empty_list()
    persongruppemedlemskap: Optional[Union[Union[str, PersongruppemedlemskapId], list[Union[str, PersongruppemedlemskapId]]]] = empty_list()
    eksamensgruppemedlemskap: Optional[Union[Union[str, EksamensgruppemedlemskapId], list[Union[str, EksamensgruppemedlemskapId]]]] = empty_list()
    fraversregistreringer: Optional[Union[Union[str, ElevfravarId], list[Union[str, ElevfravarId]]]] = empty_list()
    elevfravar: Optional[Union[str, FravarsoversiktId]] = None
    tilrettelegging: Optional[Union[Union[str, ElevtilretteleggingId], list[Union[str, ElevtilretteleggingId]]]] = empty_list()
    elevvurdering: Optional[Union[str, ElevvurderingId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElevforholdId):
            self.id = ElevforholdId(self.id)

        if self._is_empty(self.beskrivelse):
            self.MissingRequiredField("beskrivelse")
        if not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, ElevId):
            self.elev = ElevId(self.elev)

        if self._is_empty(self.skole):
            self.MissingRequiredField("skole")
        if not isinstance(self.skole, SkoleId):
            self.skole = SkoleId(self.skole)

        if self.avbruddsdato is not None and not isinstance(self.avbruddsdato, XSDDate):
            self.avbruddsdato = XSDDate(self.avbruddsdato)

        if self.tosprakligFagopplaering is not None and not isinstance(self.tosprakligFagopplaering, Bool):
            self.tosprakligFagopplaering = Bool(self.tosprakligFagopplaering)

        if self.kategori is not None and not isinstance(self.kategori, ElevkategoriId):
            self.kategori = ElevkategoriId(self.kategori)

        if self.avbruddsarsak is not None and not isinstance(self.avbruddsarsak, AvbruddsaarsakId):
            self.avbruddsarsak = AvbruddsaarsakId(self.avbruddsarsak)

        if self.skoleaar is not None and not isinstance(self.skoleaar, SkoleaarId):
            self.skoleaar = SkoleaarId(self.skoleaar)

        if not isinstance(self.programomrademedlemskap, list):
            self.programomrademedlemskap = [self.programomrademedlemskap] if self.programomrademedlemskap is not None else []
        self.programomrademedlemskap = [v if isinstance(v, ProgramomrademedlemskapId) else ProgramomrademedlemskapId(v) for v in self.programomrademedlemskap]

        if not isinstance(self.klassemedlemskap, list):
            self.klassemedlemskap = [self.klassemedlemskap] if self.klassemedlemskap is not None else []
        self.klassemedlemskap = [v if isinstance(v, KlassemedlemskapId) else KlassemedlemskapId(v) for v in self.klassemedlemskap]

        if not isinstance(self.faggruppemedlemskap, list):
            self.faggruppemedlemskap = [self.faggruppemedlemskap] if self.faggruppemedlemskap is not None else []
        self.faggruppemedlemskap = [v if isinstance(v, FaggruppemedlemskapId) else FaggruppemedlemskapId(v) for v in self.faggruppemedlemskap]

        if not isinstance(self.undervisningsgruppemedlemskap, list):
            self.undervisningsgruppemedlemskap = [self.undervisningsgruppemedlemskap] if self.undervisningsgruppemedlemskap is not None else []
        self.undervisningsgruppemedlemskap = [v if isinstance(v, UndervisningsgruppemedlemskapId) else UndervisningsgruppemedlemskapId(v) for v in self.undervisningsgruppemedlemskap]

        if not isinstance(self.kontaktlaerergruppemedlemskap, list):
            self.kontaktlaerergruppemedlemskap = [self.kontaktlaerergruppemedlemskap] if self.kontaktlaerergruppemedlemskap is not None else []
        self.kontaktlaerergruppemedlemskap = [v if isinstance(v, KontaktlaerergruppemedlemskapId) else KontaktlaerergruppemedlemskapId(v) for v in self.kontaktlaerergruppemedlemskap]

        if not isinstance(self.persongruppemedlemskap, list):
            self.persongruppemedlemskap = [self.persongruppemedlemskap] if self.persongruppemedlemskap is not None else []
        self.persongruppemedlemskap = [v if isinstance(v, PersongruppemedlemskapId) else PersongruppemedlemskapId(v) for v in self.persongruppemedlemskap]

        if not isinstance(self.eksamensgruppemedlemskap, list):
            self.eksamensgruppemedlemskap = [self.eksamensgruppemedlemskap] if self.eksamensgruppemedlemskap is not None else []
        self.eksamensgruppemedlemskap = [v if isinstance(v, EksamensgruppemedlemskapId) else EksamensgruppemedlemskapId(v) for v in self.eksamensgruppemedlemskap]

        if not isinstance(self.fraversregistreringer, list):
            self.fraversregistreringer = [self.fraversregistreringer] if self.fraversregistreringer is not None else []
        self.fraversregistreringer = [v if isinstance(v, ElevfravarId) else ElevfravarId(v) for v in self.fraversregistreringer]

        if self.elevfravar is not None and not isinstance(self.elevfravar, FravarsoversiktId):
            self.elevfravar = FravarsoversiktId(self.elevfravar)

        if not isinstance(self.tilrettelegging, list):
            self.tilrettelegging = [self.tilrettelegging] if self.tilrettelegging is not None else []
        self.tilrettelegging = [v if isinstance(v, ElevtilretteleggingId) else ElevtilretteleggingId(v) for v in self.tilrettelegging]

        if self.elevvurdering is not None and not isinstance(self.elevvurdering, ElevvurderingId):
            self.elevvurdering = ElevvurderingId(self.elevvurdering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Elevtilrettelegging(YAMLRoot):
    """
    Tilrettelegging for ein elev i eit elevforhold.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Elevtilrettelegging"]
    class_class_curie: ClassVar[str] = "utd:Elevtilrettelegging"
    class_name: ClassVar[str] = "Elevtilrettelegging"
    class_model_uri: ClassVar[URIRef] = UTD.Elevtilrettelegging

    id: Union[str, ElevtilretteleggingId] = None
    elev: Optional[Union[str, ElevforholdId]] = None
    tilrettelegging: Optional[Union[str, TilretteleggingId]] = None
    eksamensform: Optional[Union[str, EksamensformId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElevtilretteleggingId):
            self.id = ElevtilretteleggingId(self.id)

        if self.elev is not None and not isinstance(self.elev, ElevforholdId):
            self.elev = ElevforholdId(self.elev)

        if self.tilrettelegging is not None and not isinstance(self.tilrettelegging, TilretteleggingId):
            self.tilrettelegging = TilretteleggingId(self.tilrettelegging)

        if self.eksamensform is not None and not isinstance(self.eksamensform, EksamensformId):
            self.eksamensform = EksamensformId(self.eksamensform)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Klasse(Gruppe):
    """
    Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Klasse"]
    class_class_curie: ClassVar[str] = "utd:Klasse"
    class_name: ClassVar[str] = "Klasse"
    class_model_uri: ClassVar[URIRef] = UTD.Klasse

    id: Union[str, KlasseId] = None
    navn: str = None
    skoleaar: Optional[Union[str, SkoleaarId]] = None
    termin: Optional[Union[Union[str, TerminId], list[Union[str, TerminId]]]] = empty_list()
    trinn: Optional[Union[Union[str, ArstrinnId], list[Union[str, ArstrinnId]]]] = empty_list()
    skole: Optional[Union[str, SkoleId]] = None
    undervisningsforhold: Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]] = empty_list()
    klassemedlemskap: Optional[Union[Union[str, KlassemedlemskapId], list[Union[str, KlassemedlemskapId]]]] = empty_list()
    kontaktlaerergruppe: Optional[Union[Union[str, KontaktlaerergruppeId], list[Union[str, KontaktlaerergruppeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KlasseId):
            self.id = KlasseId(self.id)

        if self.skoleaar is not None and not isinstance(self.skoleaar, SkoleaarId):
            self.skoleaar = SkoleaarId(self.skoleaar)

        if not isinstance(self.termin, list):
            self.termin = [self.termin] if self.termin is not None else []
        self.termin = [v if isinstance(v, TerminId) else TerminId(v) for v in self.termin]

        if not isinstance(self.trinn, list):
            self.trinn = [self.trinn] if self.trinn is not None else []
        self.trinn = [v if isinstance(v, ArstrinnId) else ArstrinnId(v) for v in self.trinn]

        if self.skole is not None and not isinstance(self.skole, SkoleId):
            self.skole = SkoleId(self.skole)

        if not isinstance(self.undervisningsforhold, list):
            self.undervisningsforhold = [self.undervisningsforhold] if self.undervisningsforhold is not None else []
        self.undervisningsforhold = [v if isinstance(v, UndervisningsforholdId) else UndervisningsforholdId(v) for v in self.undervisningsforhold]

        if not isinstance(self.klassemedlemskap, list):
            self.klassemedlemskap = [self.klassemedlemskap] if self.klassemedlemskap is not None else []
        self.klassemedlemskap = [v if isinstance(v, KlassemedlemskapId) else KlassemedlemskapId(v) for v in self.klassemedlemskap]

        if not isinstance(self.kontaktlaerergruppe, list):
            self.kontaktlaerergruppe = [self.kontaktlaerergruppe] if self.kontaktlaerergruppe is not None else []
        self.kontaktlaerergruppe = [v if isinstance(v, KontaktlaerergruppeId) else KontaktlaerergruppeId(v) for v in self.kontaktlaerergruppe]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Klassemedlemskap(Gruppemedlemskap):
    """
    Eit elevs medlemskap i ei klasse.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Klassemedlemskap"]
    class_class_curie: ClassVar[str] = "utd:Klassemedlemskap"
    class_name: ClassVar[str] = "Klassemedlemskap"
    class_model_uri: ClassVar[URIRef] = UTD.Klassemedlemskap

    id: Union[str, KlassemedlemskapId] = None
    elevforhold: Optional[Union[str, ElevforholdId]] = None
    klasse: Optional[Union[str, KlasseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KlassemedlemskapId):
            self.id = KlassemedlemskapId(self.id)

        if self.elevforhold is not None and not isinstance(self.elevforhold, ElevforholdId):
            self.elevforhold = ElevforholdId(self.elevforhold)

        if self.klasse is not None and not isinstance(self.klasse, KlasseId):
            self.klasse = KlasseId(self.klasse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontaktlaerergruppe(Gruppe):
    """
    Gruppe av elevar med felles kontaktlærar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Kontaktlaerergruppe"]
    class_class_curie: ClassVar[str] = "utd:Kontaktlaerergruppe"
    class_name: ClassVar[str] = "Kontaktlaerergruppe"
    class_model_uri: ClassVar[URIRef] = UTD.Kontaktlaerergruppe

    id: Union[str, KontaktlaerergruppeId] = None
    navn: str = None
    klasse: Union[Union[str, KlasseId], list[Union[str, KlasseId]]] = None
    termin: Optional[Union[Union[str, TerminId], list[Union[str, TerminId]]]] = empty_list()
    skole: Optional[Union[str, SkoleId]] = None
    skoleaar: Optional[Union[str, SkoleaarId]] = None
    undervisningsforhold: Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]] = empty_list()
    gruppemedlemskap: Optional[Union[Union[str, KontaktlaerergruppemedlemskapId], list[Union[str, KontaktlaerergruppemedlemskapId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KontaktlaerergruppeId):
            self.id = KontaktlaerergruppeId(self.id)

        if self._is_empty(self.klasse):
            self.MissingRequiredField("klasse")
        if not isinstance(self.klasse, list):
            self.klasse = [self.klasse] if self.klasse is not None else []
        self.klasse = [v if isinstance(v, KlasseId) else KlasseId(v) for v in self.klasse]

        if not isinstance(self.termin, list):
            self.termin = [self.termin] if self.termin is not None else []
        self.termin = [v if isinstance(v, TerminId) else TerminId(v) for v in self.termin]

        if self.skole is not None and not isinstance(self.skole, SkoleId):
            self.skole = SkoleId(self.skole)

        if self.skoleaar is not None and not isinstance(self.skoleaar, SkoleaarId):
            self.skoleaar = SkoleaarId(self.skoleaar)

        if not isinstance(self.undervisningsforhold, list):
            self.undervisningsforhold = [self.undervisningsforhold] if self.undervisningsforhold is not None else []
        self.undervisningsforhold = [v if isinstance(v, UndervisningsforholdId) else UndervisningsforholdId(v) for v in self.undervisningsforhold]

        if not isinstance(self.gruppemedlemskap, list):
            self.gruppemedlemskap = [self.gruppemedlemskap] if self.gruppemedlemskap is not None else []
        self.gruppemedlemskap = [v if isinstance(v, KontaktlaerergruppemedlemskapId) else KontaktlaerergruppemedlemskapId(v) for v in self.gruppemedlemskap]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontaktlaerergruppemedlemskap(Gruppemedlemskap):
    """
    Eit elevs medlemskap i ei kontaktlærargruppe.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Kontaktlaerergruppemedlemskap"]
    class_class_curie: ClassVar[str] = "utd:Kontaktlaerergruppemedlemskap"
    class_name: ClassVar[str] = "Kontaktlaerergruppemedlemskap"
    class_model_uri: ClassVar[URIRef] = UTD.Kontaktlaerergruppemedlemskap

    id: Union[str, KontaktlaerergruppemedlemskapId] = None
    elevforhold: Optional[Union[str, ElevforholdId]] = None
    kontaktlaerergruppe: Optional[Union[str, KontaktlaerergruppeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KontaktlaerergruppemedlemskapId):
            self.id = KontaktlaerergruppemedlemskapId(self.id)

        if self.elevforhold is not None and not isinstance(self.elevforhold, ElevforholdId):
            self.elevforhold = ElevforholdId(self.elevforhold)

        if self.kontaktlaerergruppe is not None and not isinstance(self.kontaktlaerergruppe, KontaktlaerergruppeId):
            self.kontaktlaerergruppe = KontaktlaerergruppeId(self.kontaktlaerergruppe)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Persongruppe(Gruppe):
    """
    Ei gruppe elevar definert for personlege føremål.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Persongruppe"]
    class_class_curie: ClassVar[str] = "utd:Persongruppe"
    class_name: ClassVar[str] = "Persongruppe"
    class_model_uri: ClassVar[URIRef] = UTD.Persongruppe

    id: Union[str, PersongruppeId] = None
    navn: str = None
    elev: Optional[Union[Union[str, ElevforholdId], list[Union[str, ElevforholdId]]]] = empty_list()
    persongruppemedlemskap: Optional[Union[Union[str, PersongruppemedlemskapId], list[Union[str, PersongruppemedlemskapId]]]] = empty_list()
    termin: Optional[Union[Union[str, TerminId], list[Union[str, TerminId]]]] = empty_list()
    undervisningsforhold: Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]] = empty_list()
    skole: Optional[Union[str, SkoleId]] = None
    skoleressurs: Optional[Union[Union[str, SkoleressursId], list[Union[str, SkoleressursId]]]] = empty_list()
    skoleaar: Optional[Union[str, SkoleaarId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersongruppeId):
            self.id = PersongruppeId(self.id)

        if not isinstance(self.elev, list):
            self.elev = [self.elev] if self.elev is not None else []
        self.elev = [v if isinstance(v, ElevforholdId) else ElevforholdId(v) for v in self.elev]

        if not isinstance(self.persongruppemedlemskap, list):
            self.persongruppemedlemskap = [self.persongruppemedlemskap] if self.persongruppemedlemskap is not None else []
        self.persongruppemedlemskap = [v if isinstance(v, PersongruppemedlemskapId) else PersongruppemedlemskapId(v) for v in self.persongruppemedlemskap]

        if not isinstance(self.termin, list):
            self.termin = [self.termin] if self.termin is not None else []
        self.termin = [v if isinstance(v, TerminId) else TerminId(v) for v in self.termin]

        if not isinstance(self.undervisningsforhold, list):
            self.undervisningsforhold = [self.undervisningsforhold] if self.undervisningsforhold is not None else []
        self.undervisningsforhold = [v if isinstance(v, UndervisningsforholdId) else UndervisningsforholdId(v) for v in self.undervisningsforhold]

        if self.skole is not None and not isinstance(self.skole, SkoleId):
            self.skole = SkoleId(self.skole)

        if not isinstance(self.skoleressurs, list):
            self.skoleressurs = [self.skoleressurs] if self.skoleressurs is not None else []
        self.skoleressurs = [v if isinstance(v, SkoleressursId) else SkoleressursId(v) for v in self.skoleressurs]

        if self.skoleaar is not None and not isinstance(self.skoleaar, SkoleaarId):
            self.skoleaar = SkoleaarId(self.skoleaar)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Persongruppemedlemskap(Gruppemedlemskap):
    """
    Eit elevs medlemskap i ei persongruppe.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Persongruppemedlemskap"]
    class_class_curie: ClassVar[str] = "utd:Persongruppemedlemskap"
    class_name: ClassVar[str] = "Persongruppemedlemskap"
    class_model_uri: ClassVar[URIRef] = UTD.Persongruppemedlemskap

    id: Union[str, PersongruppemedlemskapId] = None
    elevforhold: Optional[Union[str, ElevforholdId]] = None
    persongruppe: Optional[Union[str, PersongruppeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersongruppemedlemskapId):
            self.id = PersongruppemedlemskapId(self.id)

        if self.elevforhold is not None and not isinstance(self.elevforhold, ElevforholdId):
            self.elevforhold = ElevforholdId(self.elevforhold)

        if self.persongruppe is not None and not isinstance(self.persongruppe, PersongruppeId):
            self.persongruppe = PersongruppeId(self.persongruppe)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Skole(YAMLRoot):
    """
    Ein skule eller opplæringsinstitusjon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Skole"]
    class_class_curie: ClassVar[str] = "utd:Skole"
    class_name: ClassVar[str] = "Skole"
    class_model_uri: ClassVar[URIRef] = UTD.Skole

    id: Union[str, SkoleId] = None
    navn: str = None
    domenenavn: Optional[str] = None
    juridiskNavn: Optional[str] = None
    organisasjonsnavn: Optional[str] = None
    skolenummer: Optional[Union[dict, "Identifikator"]] = None
    organisasjonsnummer: Optional[Union[dict, "Identifikator"]] = None
    forretningsadresse: Optional[Union[dict, "Adresse"]] = None
    postadresse: Optional[Union[dict, "Adresse"]] = None
    organisasjon: Optional[Union[str, URIorCURIE]] = None
    klasse: Optional[Union[Union[str, KlasseId], list[Union[str, KlasseId]]]] = empty_list()
    kontaktlaerergruppe: Optional[Union[Union[str, KontaktlaerergruppeId], list[Union[str, KontaktlaerergruppeId]]]] = empty_list()
    skoleressurs: Optional[Union[Union[str, SkoleressursId], list[Union[str, SkoleressursId]]]] = empty_list()
    fag: Optional[Union[Union[str, FagId], list[Union[str, FagId]]]] = empty_list()
    faggruppe: Optional[Union[Union[str, FaggruppeId], list[Union[str, FaggruppeId]]]] = empty_list()
    skoleeierType: Optional[Union[str, SkoleeiertypeId]] = None
    vigoreferanse: Optional[Union[str, URIorCURIE]] = None
    eksamensgruppe: Optional[Union[Union[str, EksamensgruppeId], list[Union[str, EksamensgruppeId]]]] = empty_list()
    utdanningsprogram: Optional[Union[Union[str, UtdanningsprogramId], list[Union[str, UtdanningsprogramId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SkoleId):
            self.id = SkoleId(self.id)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.domenenavn is not None and not isinstance(self.domenenavn, str):
            self.domenenavn = str(self.domenenavn)

        if self.juridiskNavn is not None and not isinstance(self.juridiskNavn, str):
            self.juridiskNavn = str(self.juridiskNavn)

        if self.organisasjonsnavn is not None and not isinstance(self.organisasjonsnavn, str):
            self.organisasjonsnavn = str(self.organisasjonsnavn)

        if self.skolenummer is not None and not isinstance(self.skolenummer, Identifikator):
            self.skolenummer = Identifikator(**as_dict(self.skolenummer))

        if self.organisasjonsnummer is not None and not isinstance(self.organisasjonsnummer, Identifikator):
            self.organisasjonsnummer = Identifikator(**as_dict(self.organisasjonsnummer))

        if self.forretningsadresse is not None and not isinstance(self.forretningsadresse, Adresse):
            self.forretningsadresse = Adresse(**as_dict(self.forretningsadresse))

        if self.postadresse is not None and not isinstance(self.postadresse, Adresse):
            self.postadresse = Adresse(**as_dict(self.postadresse))

        if self.organisasjon is not None and not isinstance(self.organisasjon, URIorCURIE):
            self.organisasjon = URIorCURIE(self.organisasjon)

        if not isinstance(self.klasse, list):
            self.klasse = [self.klasse] if self.klasse is not None else []
        self.klasse = [v if isinstance(v, KlasseId) else KlasseId(v) for v in self.klasse]

        if not isinstance(self.kontaktlaerergruppe, list):
            self.kontaktlaerergruppe = [self.kontaktlaerergruppe] if self.kontaktlaerergruppe is not None else []
        self.kontaktlaerergruppe = [v if isinstance(v, KontaktlaerergruppeId) else KontaktlaerergruppeId(v) for v in self.kontaktlaerergruppe]

        if not isinstance(self.skoleressurs, list):
            self.skoleressurs = [self.skoleressurs] if self.skoleressurs is not None else []
        self.skoleressurs = [v if isinstance(v, SkoleressursId) else SkoleressursId(v) for v in self.skoleressurs]

        if not isinstance(self.fag, list):
            self.fag = [self.fag] if self.fag is not None else []
        self.fag = [v if isinstance(v, FagId) else FagId(v) for v in self.fag]

        if not isinstance(self.faggruppe, list):
            self.faggruppe = [self.faggruppe] if self.faggruppe is not None else []
        self.faggruppe = [v if isinstance(v, FaggruppeId) else FaggruppeId(v) for v in self.faggruppe]

        if self.skoleeierType is not None and not isinstance(self.skoleeierType, SkoleeiertypeId):
            self.skoleeierType = SkoleeiertypeId(self.skoleeierType)

        if self.vigoreferanse is not None and not isinstance(self.vigoreferanse, URIorCURIE):
            self.vigoreferanse = URIorCURIE(self.vigoreferanse)

        if not isinstance(self.eksamensgruppe, list):
            self.eksamensgruppe = [self.eksamensgruppe] if self.eksamensgruppe is not None else []
        self.eksamensgruppe = [v if isinstance(v, EksamensgruppeId) else EksamensgruppeId(v) for v in self.eksamensgruppe]

        if not isinstance(self.utdanningsprogram, list):
            self.utdanningsprogram = [self.utdanningsprogram] if self.utdanningsprogram is not None else []
        self.utdanningsprogram = [v if isinstance(v, UtdanningsprogramId) else UtdanningsprogramId(v) for v in self.utdanningsprogram]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Skoleressurs(YAMLRoot):
    """
    Ein lærar eller anna tilsett ved ein skule.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Skoleressurs"]
    class_class_curie: ClassVar[str] = "utd:Skoleressurs"
    class_name: ClassVar[str] = "Skoleressurs"
    class_model_uri: ClassVar[URIRef] = UTD.Skoleressurs

    id: Union[str, SkoleressursId] = None
    feidenavn: Optional[Union[dict, "Identifikator"]] = None
    personalressurs: Optional[Union[str, URIorCURIE]] = None
    person: Optional[Union[str, URIorCURIE]] = None
    skole: Optional[Union[Union[str, SkoleId], list[Union[str, SkoleId]]]] = empty_list()
    sensor: Optional[Union[Union[str, SensorId], list[Union[str, SensorId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SkoleressursId):
            self.id = SkoleressursId(self.id)

        if self.feidenavn is not None and not isinstance(self.feidenavn, Identifikator):
            self.feidenavn = Identifikator(**as_dict(self.feidenavn))

        if self.personalressurs is not None and not isinstance(self.personalressurs, URIorCURIE):
            self.personalressurs = URIorCURIE(self.personalressurs)

        if self.person is not None and not isinstance(self.person, URIorCURIE):
            self.person = URIorCURIE(self.person)

        if not isinstance(self.skole, list):
            self.skole = [self.skole] if self.skole is not None else []
        self.skole = [v if isinstance(v, SkoleId) else SkoleId(v) for v in self.skole]

        if not isinstance(self.sensor, list):
            self.sensor = [self.sensor] if self.sensor is not None else []
        self.sensor = [v if isinstance(v, SensorId) else SensorId(v) for v in self.sensor]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Varsel(YAMLRoot):
    """
    Eit varsel knytt til ein elev i ei faggruppe.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Varsel"]
    class_class_curie: ClassVar[str] = "utd:Varsel"
    class_name: ClassVar[str] = "Varsel"
    class_model_uri: ClassVar[URIRef] = UTD.Varsel

    id: Union[str, VarselId] = None
    fravarsprosent: Optional[int] = None
    sendt: Optional[Union[str, XSDDate]] = None
    tekst: Optional[str] = None
    utsteder: Optional[Union[str, SkoleressursId]] = None
    karakteransvarlig: Optional[Union[str, SkoleressursId]] = None
    type: Optional[Union[str, VarseltypeId]] = None
    faggruppemedlemskap: Optional[Union[str, FaggruppemedlemskapId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VarselId):
            self.id = VarselId(self.id)

        if self.fravarsprosent is not None and not isinstance(self.fravarsprosent, int):
            self.fravarsprosent = int(self.fravarsprosent)

        if self.sendt is not None and not isinstance(self.sendt, XSDDate):
            self.sendt = XSDDate(self.sendt)

        if self.tekst is not None and not isinstance(self.tekst, str):
            self.tekst = str(self.tekst)

        if self.utsteder is not None and not isinstance(self.utsteder, SkoleressursId):
            self.utsteder = SkoleressursId(self.utsteder)

        if self.karakteransvarlig is not None and not isinstance(self.karakteransvarlig, SkoleressursId):
            self.karakteransvarlig = SkoleressursId(self.karakteransvarlig)

        if self.type is not None and not isinstance(self.type, VarseltypeId):
            self.type = VarseltypeId(self.type)

        if self.faggruppemedlemskap is not None and not isinstance(self.faggruppemedlemskap, FaggruppemedlemskapId):
            self.faggruppemedlemskap = FaggruppemedlemskapId(self.faggruppemedlemskap)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Arstrinn(Gruppe):
    """
    Eit årstrinn i skulen (t.d. Vg1, Vg2, Vg3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Arstrinn"]
    class_class_curie: ClassVar[str] = "utd:Arstrinn"
    class_name: ClassVar[str] = "Arstrinn"
    class_model_uri: ClassVar[URIRef] = UTD.Arstrinn

    id: Union[str, ArstrinnId] = None
    navn: str = None
    klasse: Optional[Union[Union[str, KlasseId], list[Union[str, KlasseId]]]] = empty_list()
    vigoreferanse: Optional[Union[str, URIorCURIE]] = None
    grepreferanse: Optional[Union[str, URIorCURIE]] = None
    programomrade: Optional[Union[Union[str, ProgramomradeId], list[Union[str, ProgramomradeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArstrinnId):
            self.id = ArstrinnId(self.id)

        if not isinstance(self.klasse, list):
            self.klasse = [self.klasse] if self.klasse is not None else []
        self.klasse = [v if isinstance(v, KlasseId) else KlasseId(v) for v in self.klasse]

        if self.vigoreferanse is not None and not isinstance(self.vigoreferanse, URIorCURIE):
            self.vigoreferanse = URIorCURIE(self.vigoreferanse)

        if self.grepreferanse is not None and not isinstance(self.grepreferanse, URIorCURIE):
            self.grepreferanse = URIorCURIE(self.grepreferanse)

        if not isinstance(self.programomrade, list):
            self.programomrade = [self.programomrade] if self.programomrade is not None else []
        self.programomrade = [v if isinstance(v, ProgramomradeId) else ProgramomradeId(v) for v in self.programomrade]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Programomrade(Gruppe):
    """
    Eit programområde innanfor eit utdanningsprogram (t.d. Vg2 Elektrofaget).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Programomrade"]
    class_class_curie: ClassVar[str] = "utd:Programomrade"
    class_name: ClassVar[str] = "Programomrade"
    class_model_uri: ClassVar[URIRef] = UTD.Programomrade

    id: Union[str, ProgramomradeId] = None
    navn: str = None
    trinn: Optional[Union[Union[str, ArstrinnId], list[Union[str, ArstrinnId]]]] = empty_list()
    grepreferanse: Optional[Union[str, URIorCURIE]] = None
    vigoreferanse: Optional[Union[str, URIorCURIE]] = None
    gruppemedlemskap: Optional[Union[Union[str, ProgramomrademedlemskapId], list[Union[str, ProgramomrademedlemskapId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProgramomradeId):
            self.id = ProgramomradeId(self.id)

        if not isinstance(self.trinn, list):
            self.trinn = [self.trinn] if self.trinn is not None else []
        self.trinn = [v if isinstance(v, ArstrinnId) else ArstrinnId(v) for v in self.trinn]

        if self.grepreferanse is not None and not isinstance(self.grepreferanse, URIorCURIE):
            self.grepreferanse = URIorCURIE(self.grepreferanse)

        if self.vigoreferanse is not None and not isinstance(self.vigoreferanse, URIorCURIE):
            self.vigoreferanse = URIorCURIE(self.vigoreferanse)

        if not isinstance(self.gruppemedlemskap, list):
            self.gruppemedlemskap = [self.gruppemedlemskap] if self.gruppemedlemskap is not None else []
        self.gruppemedlemskap = [v if isinstance(v, ProgramomrademedlemskapId) else ProgramomrademedlemskapId(v) for v in self.gruppemedlemskap]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Programomrademedlemskap(Gruppemedlemskap):
    """
    Eit elevs tilknyting til eit programområde.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Programomrademedlemskap"]
    class_class_curie: ClassVar[str] = "utd:Programomrademedlemskap"
    class_name: ClassVar[str] = "Programomrademedlemskap"
    class_model_uri: ClassVar[URIRef] = UTD.Programomrademedlemskap

    id: Union[str, ProgramomrademedlemskapId] = None
    elevforhold: Optional[Union[str, ElevforholdId]] = None
    programomrade: Optional[Union[str, ProgramomradeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProgramomrademedlemskapId):
            self.id = ProgramomrademedlemskapId(self.id)

        if self.elevforhold is not None and not isinstance(self.elevforhold, ElevforholdId):
            self.elevforhold = ElevforholdId(self.elevforhold)

        if self.programomrade is not None and not isinstance(self.programomrade, ProgramomradeId):
            self.programomrade = ProgramomradeId(self.programomrade)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Utdanningsprogram(Gruppe):
    """
    Eit utdanningsprogram (t.d. Elektrofag, Studiespesialisering).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Utdanningsprogram"]
    class_class_curie: ClassVar[str] = "utd:Utdanningsprogram"
    class_name: ClassVar[str] = "Utdanningsprogram"
    class_model_uri: ClassVar[URIRef] = UTD.Utdanningsprogram

    id: Union[str, UtdanningsprogramId] = None
    navn: str = None
    programomrade: Optional[Union[Union[str, ProgramomradeId], list[Union[str, ProgramomradeId]]]] = empty_list()
    skole: Optional[Union[Union[str, SkoleId], list[Union[str, SkoleId]]]] = empty_list()
    grepreferanse: Optional[Union[str, URIorCURIE]] = None
    vigoreferanse: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UtdanningsprogramId):
            self.id = UtdanningsprogramId(self.id)

        if not isinstance(self.programomrade, list):
            self.programomrade = [self.programomrade] if self.programomrade is not None else []
        self.programomrade = [v if isinstance(v, ProgramomradeId) else ProgramomradeId(v) for v in self.programomrade]

        if not isinstance(self.skole, list):
            self.skole = [self.skole] if self.skole is not None else []
        self.skole = [v if isinstance(v, SkoleId) else SkoleId(v) for v in self.skole]

        if self.grepreferanse is not None and not isinstance(self.grepreferanse, URIorCURIE):
            self.grepreferanse = URIorCURIE(self.grepreferanse)

        if self.vigoreferanse is not None and not isinstance(self.vigoreferanse, URIorCURIE):
            self.vigoreferanse = URIorCURIE(self.vigoreferanse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Eksamen(YAMLRoot):
    """
    Ein eksamen knytt til ei eksamensgruppe.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Eksamen"]
    class_class_curie: ClassVar[str] = "utd:Eksamen"
    class_name: ClassVar[str] = "Eksamen"
    class_model_uri: ClassVar[URIRef] = UTD.Eksamen

    id: Union[str, EksamenId] = None
    navn: str = None
    beskrivelse: Optional[str] = None
    oppmoetetidspunkt: Optional[Union[str, XSDDateTime]] = None
    tidsrom: Optional[Union[dict, "Periode"]] = None
    rom: Optional[Union[Union[str, RomId], list[Union[str, RomId]]]] = empty_list()
    eksamensgruppe: Optional[Union[str, EksamensgruppeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EksamenId):
            self.id = EksamenId(self.id)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if self.oppmoetetidspunkt is not None and not isinstance(self.oppmoetetidspunkt, XSDDateTime):
            self.oppmoetetidspunkt = XSDDateTime(self.oppmoetetidspunkt)

        if self.tidsrom is not None and not isinstance(self.tidsrom, Periode):
            self.tidsrom = Periode(**as_dict(self.tidsrom))

        if not isinstance(self.rom, list):
            self.rom = [self.rom] if self.rom is not None else []
        self.rom = [v if isinstance(v, RomId) else RomId(v) for v in self.rom]

        if self.eksamensgruppe is not None and not isinstance(self.eksamensgruppe, EksamensgruppeId):
            self.eksamensgruppe = EksamensgruppeId(self.eksamensgruppe)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fag(Gruppe):
    """
    Eit skulefag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Fag"]
    class_class_curie: ClassVar[str] = "utd:Fag"
    class_name: ClassVar[str] = "Fag"
    class_model_uri: ClassVar[URIRef] = UTD.Fag

    id: Union[str, FagId] = None
    navn: str = None
    tilrettelegging: Optional[Union[Union[str, TilretteleggingId], list[Union[str, TilretteleggingId]]]] = empty_list()
    grepreferanse: Optional[Union[str, URIorCURIE]] = None
    skole: Optional[Union[Union[str, SkoleId], list[Union[str, SkoleId]]]] = empty_list()
    vigoreferanse: Optional[Union[str, URIorCURIE]] = None
    programomrade: Optional[Union[Union[str, ProgramomradeId], list[Union[str, ProgramomradeId]]]] = empty_list()
    faggruppe: Optional[Union[Union[str, FaggruppeId], list[Union[str, FaggruppeId]]]] = empty_list()
    undervisningsgruppe: Optional[Union[Union[str, UndervisningsgruppeId], list[Union[str, UndervisningsgruppeId]]]] = empty_list()
    eksamensgruppe: Optional[Union[Union[str, EksamensgruppeId], list[Union[str, EksamensgruppeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FagId):
            self.id = FagId(self.id)

        if not isinstance(self.tilrettelegging, list):
            self.tilrettelegging = [self.tilrettelegging] if self.tilrettelegging is not None else []
        self.tilrettelegging = [v if isinstance(v, TilretteleggingId) else TilretteleggingId(v) for v in self.tilrettelegging]

        if self.grepreferanse is not None and not isinstance(self.grepreferanse, URIorCURIE):
            self.grepreferanse = URIorCURIE(self.grepreferanse)

        if not isinstance(self.skole, list):
            self.skole = [self.skole] if self.skole is not None else []
        self.skole = [v if isinstance(v, SkoleId) else SkoleId(v) for v in self.skole]

        if self.vigoreferanse is not None and not isinstance(self.vigoreferanse, URIorCURIE):
            self.vigoreferanse = URIorCURIE(self.vigoreferanse)

        if not isinstance(self.programomrade, list):
            self.programomrade = [self.programomrade] if self.programomrade is not None else []
        self.programomrade = [v if isinstance(v, ProgramomradeId) else ProgramomradeId(v) for v in self.programomrade]

        if not isinstance(self.faggruppe, list):
            self.faggruppe = [self.faggruppe] if self.faggruppe is not None else []
        self.faggruppe = [v if isinstance(v, FaggruppeId) else FaggruppeId(v) for v in self.faggruppe]

        if not isinstance(self.undervisningsgruppe, list):
            self.undervisningsgruppe = [self.undervisningsgruppe] if self.undervisningsgruppe is not None else []
        self.undervisningsgruppe = [v if isinstance(v, UndervisningsgruppeId) else UndervisningsgruppeId(v) for v in self.undervisningsgruppe]

        if not isinstance(self.eksamensgruppe, list):
            self.eksamensgruppe = [self.eksamensgruppe] if self.eksamensgruppe is not None else []
        self.eksamensgruppe = [v if isinstance(v, EksamensgruppeId) else EksamensgruppeId(v) for v in self.eksamensgruppe]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Faggruppe(Gruppe):
    """
    Ei gruppe elevar knytt til eit fag på ein skule.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Faggruppe"]
    class_class_curie: ClassVar[str] = "utd:Faggruppe"
    class_name: ClassVar[str] = "Faggruppe"
    class_model_uri: ClassVar[URIRef] = UTD.Faggruppe

    id: Union[str, FaggruppeId] = None
    navn: str = None
    fag: Union[str, FagId] = None
    skole: Optional[Union[str, SkoleId]] = None
    skoleaar: Optional[Union[str, SkoleaarId]] = None
    faggruppemedlemskap: Optional[Union[Union[str, FaggruppemedlemskapId], list[Union[str, FaggruppemedlemskapId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaggruppeId):
            self.id = FaggruppeId(self.id)

        if self._is_empty(self.fag):
            self.MissingRequiredField("fag")
        if not isinstance(self.fag, FagId):
            self.fag = FagId(self.fag)

        if self.skole is not None and not isinstance(self.skole, SkoleId):
            self.skole = SkoleId(self.skole)

        if self.skoleaar is not None and not isinstance(self.skoleaar, SkoleaarId):
            self.skoleaar = SkoleaarId(self.skoleaar)

        if not isinstance(self.faggruppemedlemskap, list):
            self.faggruppemedlemskap = [self.faggruppemedlemskap] if self.faggruppemedlemskap is not None else []
        self.faggruppemedlemskap = [v if isinstance(v, FaggruppemedlemskapId) else FaggruppemedlemskapId(v) for v in self.faggruppemedlemskap]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Faggruppemedlemskap(Gruppemedlemskap):
    """
    Eit elevs medlemskap i ei faggruppe.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Faggruppemedlemskap"]
    class_class_curie: ClassVar[str] = "utd:Faggruppemedlemskap"
    class_name: ClassVar[str] = "Faggruppemedlemskap"
    class_model_uri: ClassVar[URIRef] = UTD.Faggruppemedlemskap

    id: Union[str, FaggruppemedlemskapId] = None
    elevforhold: Optional[Union[str, ElevforholdId]] = None
    varsel: Optional[Union[Union[str, VarselId], list[Union[str, VarselId]]]] = empty_list()
    faggruppe: Optional[Union[str, FaggruppeId]] = None
    fagmerknad: Optional[Union[str, FagmerknadId]] = None
    fagstatus: Optional[Union[str, FagstatusId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaggruppemedlemskapId):
            self.id = FaggruppemedlemskapId(self.id)

        if self.elevforhold is not None and not isinstance(self.elevforhold, ElevforholdId):
            self.elevforhold = ElevforholdId(self.elevforhold)

        if not isinstance(self.varsel, list):
            self.varsel = [self.varsel] if self.varsel is not None else []
        self.varsel = [v if isinstance(v, VarselId) else VarselId(v) for v in self.varsel]

        if self.faggruppe is not None and not isinstance(self.faggruppe, FaggruppeId):
            self.faggruppe = FaggruppeId(self.faggruppe)

        if self.fagmerknad is not None and not isinstance(self.fagmerknad, FagmerknadId):
            self.fagmerknad = FagmerknadId(self.fagmerknad)

        if self.fagstatus is not None and not isinstance(self.fagstatus, FagstatusId):
            self.fagstatus = FagstatusId(self.fagstatus)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rom(YAMLRoot):
    """
    Eit rom eller lokale ved ein skule.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Rom"]
    class_class_curie: ClassVar[str] = "utd:Rom"
    class_name: ClassVar[str] = "Rom"
    class_model_uri: ClassVar[URIRef] = UTD.Rom

    id: Union[str, RomId] = None
    navn: Optional[str] = None
    eksamen: Optional[Union[Union[str, EksamenId], list[Union[str, EksamenId]]]] = empty_list()
    time: Optional[Union[Union[str, TimeId], list[Union[str, TimeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RomId):
            self.id = RomId(self.id)

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if not isinstance(self.eksamen, list):
            self.eksamen = [self.eksamen] if self.eksamen is not None else []
        self.eksamen = [v if isinstance(v, EksamenId) else EksamenId(v) for v in self.eksamen]

        if not isinstance(self.time, list):
            self.time = [self.time] if self.time is not None else []
        self.time = [v if isinstance(v, TimeId) else TimeId(v) for v in self.time]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Time(YAMLRoot):
    """
    Ein time i timeplanen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Time"]
    class_class_curie: ClassVar[str] = "utd:Time"
    class_name: ClassVar[str] = "Time"
    class_model_uri: ClassVar[URIRef] = UTD.Time

    id: Union[str, TimeId] = None
    undervisningsforhold: Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]] = None
    undervisningsgruppe: Union[Union[str, UndervisningsgruppeId], list[Union[str, UndervisningsgruppeId]]] = None
    navn: Optional[str] = None
    beskrivelse: Optional[str] = None
    tidsrom: Optional[Union[dict, "Periode"]] = None
    rom: Optional[Union[Union[str, RomId], list[Union[str, RomId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TimeId):
            self.id = TimeId(self.id)

        if self._is_empty(self.undervisningsforhold):
            self.MissingRequiredField("undervisningsforhold")
        if not isinstance(self.undervisningsforhold, list):
            self.undervisningsforhold = [self.undervisningsforhold] if self.undervisningsforhold is not None else []
        self.undervisningsforhold = [v if isinstance(v, UndervisningsforholdId) else UndervisningsforholdId(v) for v in self.undervisningsforhold]

        if self._is_empty(self.undervisningsgruppe):
            self.MissingRequiredField("undervisningsgruppe")
        if not isinstance(self.undervisningsgruppe, list):
            self.undervisningsgruppe = [self.undervisningsgruppe] if self.undervisningsgruppe is not None else []
        self.undervisningsgruppe = [v if isinstance(v, UndervisningsgruppeId) else UndervisningsgruppeId(v) for v in self.undervisningsgruppe]

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if self.tidsrom is not None and not isinstance(self.tidsrom, Periode):
            self.tidsrom = Periode(**as_dict(self.tidsrom))

        if not isinstance(self.rom, list):
            self.rom = [self.rom] if self.rom is not None else []
        self.rom = [v if isinstance(v, RomId) else RomId(v) for v in self.rom]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Undervisningsforhold(Utdanningsforhold):
    """
    Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Undervisningsforhold"]
    class_class_curie: ClassVar[str] = "utd:Undervisningsforhold"
    class_name: ClassVar[str] = "Undervisningsforhold"
    class_model_uri: ClassVar[URIRef] = UTD.Undervisningsforhold

    id: Union[str, UndervisningsforholdId] = None
    arbeidsforhold: Union[str, URIorCURIE] = None
    skoleressurs: Optional[Union[str, SkoleressursId]] = None
    klasse: Optional[Union[Union[str, KlasseId], list[Union[str, KlasseId]]]] = empty_list()
    kontaktlaerergruppe: Optional[Union[Union[str, KontaktlaerergruppeId], list[Union[str, KontaktlaerergruppeId]]]] = empty_list()
    time: Optional[Union[Union[str, TimeId], list[Union[str, TimeId]]]] = empty_list()
    eksamensgruppe: Optional[Union[Union[str, EksamensgruppeId], list[Union[str, EksamensgruppeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UndervisningsforholdId):
            self.id = UndervisningsforholdId(self.id)

        if self._is_empty(self.arbeidsforhold):
            self.MissingRequiredField("arbeidsforhold")
        if not isinstance(self.arbeidsforhold, URIorCURIE):
            self.arbeidsforhold = URIorCURIE(self.arbeidsforhold)

        if self.skoleressurs is not None and not isinstance(self.skoleressurs, SkoleressursId):
            self.skoleressurs = SkoleressursId(self.skoleressurs)

        if not isinstance(self.klasse, list):
            self.klasse = [self.klasse] if self.klasse is not None else []
        self.klasse = [v if isinstance(v, KlasseId) else KlasseId(v) for v in self.klasse]

        if not isinstance(self.kontaktlaerergruppe, list):
            self.kontaktlaerergruppe = [self.kontaktlaerergruppe] if self.kontaktlaerergruppe is not None else []
        self.kontaktlaerergruppe = [v if isinstance(v, KontaktlaerergruppeId) else KontaktlaerergruppeId(v) for v in self.kontaktlaerergruppe]

        if not isinstance(self.time, list):
            self.time = [self.time] if self.time is not None else []
        self.time = [v if isinstance(v, TimeId) else TimeId(v) for v in self.time]

        if not isinstance(self.eksamensgruppe, list):
            self.eksamensgruppe = [self.eksamensgruppe] if self.eksamensgruppe is not None else []
        self.eksamensgruppe = [v if isinstance(v, EksamensgruppeId) else EksamensgruppeId(v) for v in self.eksamensgruppe]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Undervisningsgruppe(Gruppe):
    """
    Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Undervisningsgruppe"]
    class_class_curie: ClassVar[str] = "utd:Undervisningsgruppe"
    class_name: ClassVar[str] = "Undervisningsgruppe"
    class_model_uri: ClassVar[URIRef] = UTD.Undervisningsgruppe

    id: Union[str, UndervisningsgruppeId] = None
    navn: str = None
    fag: Union[Union[str, FagId], list[Union[str, FagId]]] = None
    undervisningsforhold: Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]] = empty_list()
    time: Optional[Union[Union[str, TimeId], list[Union[str, TimeId]]]] = empty_list()
    termin: Optional[Union[Union[str, TerminId], list[Union[str, TerminId]]]] = empty_list()
    skole: Optional[Union[str, SkoleId]] = None
    skoleaar: Optional[Union[str, SkoleaarId]] = None
    gruppemedlemskap: Optional[Union[Union[str, UndervisningsgruppemedlemskapId], list[Union[str, UndervisningsgruppemedlemskapId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UndervisningsgruppeId):
            self.id = UndervisningsgruppeId(self.id)

        if self._is_empty(self.fag):
            self.MissingRequiredField("fag")
        if not isinstance(self.fag, list):
            self.fag = [self.fag] if self.fag is not None else []
        self.fag = [v if isinstance(v, FagId) else FagId(v) for v in self.fag]

        if not isinstance(self.undervisningsforhold, list):
            self.undervisningsforhold = [self.undervisningsforhold] if self.undervisningsforhold is not None else []
        self.undervisningsforhold = [v if isinstance(v, UndervisningsforholdId) else UndervisningsforholdId(v) for v in self.undervisningsforhold]

        if not isinstance(self.time, list):
            self.time = [self.time] if self.time is not None else []
        self.time = [v if isinstance(v, TimeId) else TimeId(v) for v in self.time]

        if not isinstance(self.termin, list):
            self.termin = [self.termin] if self.termin is not None else []
        self.termin = [v if isinstance(v, TerminId) else TerminId(v) for v in self.termin]

        if self.skole is not None and not isinstance(self.skole, SkoleId):
            self.skole = SkoleId(self.skole)

        if self.skoleaar is not None and not isinstance(self.skoleaar, SkoleaarId):
            self.skoleaar = SkoleaarId(self.skoleaar)

        if not isinstance(self.gruppemedlemskap, list):
            self.gruppemedlemskap = [self.gruppemedlemskap] if self.gruppemedlemskap is not None else []
        self.gruppemedlemskap = [v if isinstance(v, UndervisningsgruppemedlemskapId) else UndervisningsgruppemedlemskapId(v) for v in self.gruppemedlemskap]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Undervisningsgruppemedlemskap(Gruppemedlemskap):
    """
    Eit elevs medlemskap i ei undervisningsgruppe.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Undervisningsgruppemedlemskap"]
    class_class_curie: ClassVar[str] = "utd:Undervisningsgruppemedlemskap"
    class_name: ClassVar[str] = "Undervisningsgruppemedlemskap"
    class_model_uri: ClassVar[URIRef] = UTD.Undervisningsgruppemedlemskap

    id: Union[str, UndervisningsgruppemedlemskapId] = None
    elevforhold: Optional[Union[str, ElevforholdId]] = None
    undervisningsgruppe: Optional[Union[str, UndervisningsgruppeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UndervisningsgruppemedlemskapId):
            self.id = UndervisningsgruppemedlemskapId(self.id)

        if self.elevforhold is not None and not isinstance(self.elevforhold, ElevforholdId):
            self.elevforhold = ElevforholdId(self.elevforhold)

        if self.undervisningsgruppe is not None and not isinstance(self.undervisningsgruppe, UndervisningsgruppeId):
            self.undervisningsgruppe = UndervisningsgruppeId(self.undervisningsgruppe)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FagvurderingAbstrakt(YAMLRoot):
    """
    Abstrakt basisklasse for fagvurderingar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["FagvurderingAbstrakt"]
    class_class_curie: ClassVar[str] = "utd:FagvurderingAbstrakt"
    class_name: ClassVar[str] = "FagvurderingAbstrakt"
    class_model_uri: ClassVar[URIRef] = UTD.FagvurderingAbstrakt

    id: Union[str, FagvurderingAbstraktId] = None
    kommentar: str = None
    vurderingsdato: Union[str, XSDDateTime] = None
    fag: Optional[Union[str, FagId]] = None
    skoleaar: Optional[Union[str, SkoleaarId]] = None
    karakter: Optional[Union[str, KarakterverdiId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FagvurderingAbstraktId):
            self.id = FagvurderingAbstraktId(self.id)

        if self._is_empty(self.kommentar):
            self.MissingRequiredField("kommentar")
        if not isinstance(self.kommentar, str):
            self.kommentar = str(self.kommentar)

        if self._is_empty(self.vurderingsdato):
            self.MissingRequiredField("vurderingsdato")
        if not isinstance(self.vurderingsdato, XSDDateTime):
            self.vurderingsdato = XSDDateTime(self.vurderingsdato)

        if self.fag is not None and not isinstance(self.fag, FagId):
            self.fag = FagId(self.fag)

        if self.skoleaar is not None and not isinstance(self.skoleaar, SkoleaarId):
            self.skoleaar = SkoleaarId(self.skoleaar)

        if self.karakter is not None and not isinstance(self.karakter, KarakterverdiId):
            self.karakter = KarakterverdiId(self.karakter)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrdensvurderingAbstrakt(YAMLRoot):
    """
    Abstrakt basisklasse for ordensvurderingar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["OrdensvurderingAbstrakt"]
    class_class_curie: ClassVar[str] = "utd:OrdensvurderingAbstrakt"
    class_name: ClassVar[str] = "OrdensvurderingAbstrakt"
    class_model_uri: ClassVar[URIRef] = UTD.OrdensvurderingAbstrakt

    id: Union[str, OrdensvurderingAbstraktId] = None
    kommentar: str = None
    vurderingsdato: Union[str, XSDDateTime] = None
    atferd: Optional[Union[str, KarakterverdiId]] = None
    orden: Optional[Union[str, KarakterverdiId]] = None
    skoleaar: Optional[Union[str, SkoleaarId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrdensvurderingAbstraktId):
            self.id = OrdensvurderingAbstraktId(self.id)

        if self._is_empty(self.kommentar):
            self.MissingRequiredField("kommentar")
        if not isinstance(self.kommentar, str):
            self.kommentar = str(self.kommentar)

        if self._is_empty(self.vurderingsdato):
            self.MissingRequiredField("vurderingsdato")
        if not isinstance(self.vurderingsdato, XSDDateTime):
            self.vurderingsdato = XSDDateTime(self.vurderingsdato)

        if self.atferd is not None and not isinstance(self.atferd, KarakterverdiId):
            self.atferd = KarakterverdiId(self.atferd)

        if self.orden is not None and not isinstance(self.orden, KarakterverdiId):
            self.orden = KarakterverdiId(self.orden)

        if self.skoleaar is not None and not isinstance(self.skoleaar, SkoleaarId):
            self.skoleaar = SkoleaarId(self.skoleaar)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Anmerkninger(YAMLRoot):
    """
    Åtferds- og ordensanmerkningar for ein elev i eit skoleår.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Anmerkninger"]
    class_class_curie: ClassVar[str] = "utd:Anmerkninger"
    class_name: ClassVar[str] = "Anmerkninger"
    class_model_uri: ClassVar[URIRef] = UTD.Anmerkninger

    id: Union[str, AnmerkningerId] = None
    atferd: int = None
    orden: int = None
    skoleaar: Optional[Union[str, SkoleaarId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnmerkningerId):
            self.id = AnmerkningerId(self.id)

        if self._is_empty(self.atferd):
            self.MissingRequiredField("atferd")
        if not isinstance(self.atferd, int):
            self.atferd = int(self.atferd)

        if self._is_empty(self.orden):
            self.MissingRequiredField("orden")
        if not isinstance(self.orden, int):
            self.orden = int(self.orden)

        if self.skoleaar is not None and not isinstance(self.skoleaar, SkoleaarId):
            self.skoleaar = SkoleaarId(self.skoleaar)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Eksamensgruppe(Gruppe):
    """
    Ei gruppe elevar som avlegg same eksamen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Eksamensgruppe"]
    class_class_curie: ClassVar[str] = "utd:Eksamensgruppe"
    class_name: ClassVar[str] = "Eksamensgruppe"
    class_model_uri: ClassVar[URIRef] = UTD.Eksamensgruppe

    id: Union[str, EksamensgruppeId] = None
    navn: str = None
    fag: Union[str, FagId] = None
    skole: Union[str, SkoleId] = None
    termin: Union[str, TerminId] = None
    eksamensdato: Optional[Union[str, XSDDateTime]] = None
    undervisningsforhold: Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]] = empty_list()
    eksamen: Optional[Union[str, EksamenId]] = None
    eksamensform: Optional[Union[str, EksamensformId]] = None
    skoleaar: Optional[Union[str, SkoleaarId]] = None
    gruppemedlemskap: Optional[Union[Union[str, EksamensgruppemedlemskapId], list[Union[str, EksamensgruppemedlemskapId]]]] = empty_list()
    sensor: Optional[Union[Union[str, SensorId], list[Union[str, SensorId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EksamensgruppeId):
            self.id = EksamensgruppeId(self.id)

        if self._is_empty(self.fag):
            self.MissingRequiredField("fag")
        if not isinstance(self.fag, FagId):
            self.fag = FagId(self.fag)

        if self._is_empty(self.skole):
            self.MissingRequiredField("skole")
        if not isinstance(self.skole, SkoleId):
            self.skole = SkoleId(self.skole)

        if self._is_empty(self.termin):
            self.MissingRequiredField("termin")
        if not isinstance(self.termin, TerminId):
            self.termin = TerminId(self.termin)

        if self.eksamensdato is not None and not isinstance(self.eksamensdato, XSDDateTime):
            self.eksamensdato = XSDDateTime(self.eksamensdato)

        if not isinstance(self.undervisningsforhold, list):
            self.undervisningsforhold = [self.undervisningsforhold] if self.undervisningsforhold is not None else []
        self.undervisningsforhold = [v if isinstance(v, UndervisningsforholdId) else UndervisningsforholdId(v) for v in self.undervisningsforhold]

        if self.eksamen is not None and not isinstance(self.eksamen, EksamenId):
            self.eksamen = EksamenId(self.eksamen)

        if self.eksamensform is not None and not isinstance(self.eksamensform, EksamensformId):
            self.eksamensform = EksamensformId(self.eksamensform)

        if self.skoleaar is not None and not isinstance(self.skoleaar, SkoleaarId):
            self.skoleaar = SkoleaarId(self.skoleaar)

        if not isinstance(self.gruppemedlemskap, list):
            self.gruppemedlemskap = [self.gruppemedlemskap] if self.gruppemedlemskap is not None else []
        self.gruppemedlemskap = [v if isinstance(v, EksamensgruppemedlemskapId) else EksamensgruppemedlemskapId(v) for v in self.gruppemedlemskap]

        if not isinstance(self.sensor, list):
            self.sensor = [self.sensor] if self.sensor is not None else []
        self.sensor = [v if isinstance(v, SensorId) else SensorId(v) for v in self.sensor]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Eksamensgruppemedlemskap(Gruppemedlemskap):
    """
    Eit elevs deltaking i ei eksamensgruppe.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Eksamensgruppemedlemskap"]
    class_class_curie: ClassVar[str] = "utd:Eksamensgruppemedlemskap"
    class_name: ClassVar[str] = "Eksamensgruppemedlemskap"
    class_model_uri: ClassVar[URIRef] = UTD.Eksamensgruppemedlemskap

    id: Union[str, EksamensgruppemedlemskapId] = None
    elevforhold: Union[str, ElevforholdId] = None
    eksamensgruppe: Union[str, EksamensgruppeId] = None
    delegert: Optional[Union[bool, Bool]] = None
    kandidatnummer: Optional[str] = None
    delegertTil: Optional[Union[str, URIorCURIE]] = None
    foretrukketSkole: Optional[Union[bool, Bool]] = None
    foretrukketSensor: Optional[Union[bool, Bool]] = None
    betalingsstatus: Optional[Union[str, BetalingsstatusId]] = None
    nus: Optional[Union[str, KarakterstatusId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EksamensgruppemedlemskapId):
            self.id = EksamensgruppemedlemskapId(self.id)

        if self._is_empty(self.elevforhold):
            self.MissingRequiredField("elevforhold")
        if not isinstance(self.elevforhold, ElevforholdId):
            self.elevforhold = ElevforholdId(self.elevforhold)

        if self._is_empty(self.eksamensgruppe):
            self.MissingRequiredField("eksamensgruppe")
        if not isinstance(self.eksamensgruppe, EksamensgruppeId):
            self.eksamensgruppe = EksamensgruppeId(self.eksamensgruppe)

        if self.delegert is not None and not isinstance(self.delegert, Bool):
            self.delegert = Bool(self.delegert)

        if self.kandidatnummer is not None and not isinstance(self.kandidatnummer, str):
            self.kandidatnummer = str(self.kandidatnummer)

        if self.delegertTil is not None and not isinstance(self.delegertTil, URIorCURIE):
            self.delegertTil = URIorCURIE(self.delegertTil)

        if self.foretrukketSkole is not None and not isinstance(self.foretrukketSkole, Bool):
            self.foretrukketSkole = Bool(self.foretrukketSkole)

        if self.foretrukketSensor is not None and not isinstance(self.foretrukketSensor, Bool):
            self.foretrukketSensor = Bool(self.foretrukketSensor)

        if self.betalingsstatus is not None and not isinstance(self.betalingsstatus, BetalingsstatusId):
            self.betalingsstatus = BetalingsstatusId(self.betalingsstatus)

        if self.nus is not None and not isinstance(self.nus, KarakterstatusId):
            self.nus = KarakterstatusId(self.nus)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Eksamensvurdering(FagvurderingAbstrakt):
    """
    Vurdering gjeven i samband med ein eksamen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Eksamensvurdering"]
    class_class_curie: ClassVar[str] = "utd:Eksamensvurdering"
    class_name: ClassVar[str] = "Eksamensvurdering"
    class_model_uri: ClassVar[URIRef] = UTD.Eksamensvurdering

    id: Union[str, EksamensvurderingId] = None
    kommentar: str = None
    vurderingsdato: Union[str, XSDDateTime] = None
    eksamensgruppe: Union[str, EksamensgruppeId] = None
    elevvurdering: Union[str, ElevvurderingId] = None
    karakterhistorie: Optional[Union[Union[str, KarakterhistorieId], list[Union[str, KarakterhistorieId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EksamensvurderingId):
            self.id = EksamensvurderingId(self.id)

        if self._is_empty(self.eksamensgruppe):
            self.MissingRequiredField("eksamensgruppe")
        if not isinstance(self.eksamensgruppe, EksamensgruppeId):
            self.eksamensgruppe = EksamensgruppeId(self.eksamensgruppe)

        if self._is_empty(self.elevvurdering):
            self.MissingRequiredField("elevvurdering")
        if not isinstance(self.elevvurdering, ElevvurderingId):
            self.elevvurdering = ElevvurderingId(self.elevvurdering)

        if not isinstance(self.karakterhistorie, list):
            self.karakterhistorie = [self.karakterhistorie] if self.karakterhistorie is not None else []
        self.karakterhistorie = [v if isinstance(v, KarakterhistorieId) else KarakterhistorieId(v) for v in self.karakterhistorie]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Elevfravar(YAMLRoot):
    """
    Fråværsregistreringar for ein elev knytt til eit elevforhold.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Elevfravar"]
    class_class_curie: ClassVar[str] = "utd:Elevfravar"
    class_name: ClassVar[str] = "Elevfravar"
    class_model_uri: ClassVar[URIRef] = UTD.Elevfravar

    id: Union[str, ElevfravarId] = None
    elevforhold: Union[str, ElevforholdId] = None
    fraversregistrering: Optional[Union[Union[str, FraversregistreringId], list[Union[str, FraversregistreringId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElevfravarId):
            self.id = ElevfravarId(self.id)

        if self._is_empty(self.elevforhold):
            self.MissingRequiredField("elevforhold")
        if not isinstance(self.elevforhold, ElevforholdId):
            self.elevforhold = ElevforholdId(self.elevforhold)

        if not isinstance(self.fraversregistrering, list):
            self.fraversregistrering = [self.fraversregistrering] if self.fraversregistrering is not None else []
        self.fraversregistrering = [v if isinstance(v, FraversregistreringId) else FraversregistreringId(v) for v in self.fraversregistrering]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Elevvurdering(YAMLRoot):
    """
    Samling av alle vurderingar for ein elev i eit elevforhold.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Elevvurdering"]
    class_class_curie: ClassVar[str] = "utd:Elevvurdering"
    class_name: ClassVar[str] = "Elevvurdering"
    class_model_uri: ClassVar[URIRef] = UTD.Elevvurdering

    id: Union[str, ElevvurderingId] = None
    elevforhold: Union[str, ElevforholdId] = None
    eksamensvurdering: Optional[Union[Union[str, EksamensvurderingId], list[Union[str, EksamensvurderingId]]]] = empty_list()
    sluttfagvurdering: Optional[Union[Union[str, SluttfagvurderingId], list[Union[str, SluttfagvurderingId]]]] = empty_list()
    halvaarsfagvurdering: Optional[Union[Union[str, HalvaarsfagvurderingId], list[Union[str, HalvaarsfagvurderingId]]]] = empty_list()
    underveisfagvurdering: Optional[Union[Union[str, UnderveisfagvurderingId], list[Union[str, UnderveisfagvurderingId]]]] = empty_list()
    halvaarsordensvurdering: Optional[Union[Union[str, HalvaarsordensvurderingId], list[Union[str, HalvaarsordensvurderingId]]]] = empty_list()
    underveisordensvurdering: Optional[Union[Union[str, UnderveisordensvurderingId], list[Union[str, UnderveisordensvurderingId]]]] = empty_list()
    sluttordensvurdering: Optional[Union[Union[str, SluttordensvurderingId], list[Union[str, SluttordensvurderingId]]]] = empty_list()
    vitnemalsmerknad: Optional[Union[str, VitnemalsmerknadId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElevvurderingId):
            self.id = ElevvurderingId(self.id)

        if self._is_empty(self.elevforhold):
            self.MissingRequiredField("elevforhold")
        if not isinstance(self.elevforhold, ElevforholdId):
            self.elevforhold = ElevforholdId(self.elevforhold)

        if not isinstance(self.eksamensvurdering, list):
            self.eksamensvurdering = [self.eksamensvurdering] if self.eksamensvurdering is not None else []
        self.eksamensvurdering = [v if isinstance(v, EksamensvurderingId) else EksamensvurderingId(v) for v in self.eksamensvurdering]

        if not isinstance(self.sluttfagvurdering, list):
            self.sluttfagvurdering = [self.sluttfagvurdering] if self.sluttfagvurdering is not None else []
        self.sluttfagvurdering = [v if isinstance(v, SluttfagvurderingId) else SluttfagvurderingId(v) for v in self.sluttfagvurdering]

        if not isinstance(self.halvaarsfagvurdering, list):
            self.halvaarsfagvurdering = [self.halvaarsfagvurdering] if self.halvaarsfagvurdering is not None else []
        self.halvaarsfagvurdering = [v if isinstance(v, HalvaarsfagvurderingId) else HalvaarsfagvurderingId(v) for v in self.halvaarsfagvurdering]

        if not isinstance(self.underveisfagvurdering, list):
            self.underveisfagvurdering = [self.underveisfagvurdering] if self.underveisfagvurdering is not None else []
        self.underveisfagvurdering = [v if isinstance(v, UnderveisfagvurderingId) else UnderveisfagvurderingId(v) for v in self.underveisfagvurdering]

        if not isinstance(self.halvaarsordensvurdering, list):
            self.halvaarsordensvurdering = [self.halvaarsordensvurdering] if self.halvaarsordensvurdering is not None else []
        self.halvaarsordensvurdering = [v if isinstance(v, HalvaarsordensvurderingId) else HalvaarsordensvurderingId(v) for v in self.halvaarsordensvurdering]

        if not isinstance(self.underveisordensvurdering, list):
            self.underveisordensvurdering = [self.underveisordensvurdering] if self.underveisordensvurdering is not None else []
        self.underveisordensvurdering = [v if isinstance(v, UnderveisordensvurderingId) else UnderveisordensvurderingId(v) for v in self.underveisordensvurdering]

        if not isinstance(self.sluttordensvurdering, list):
            self.sluttordensvurdering = [self.sluttordensvurdering] if self.sluttordensvurdering is not None else []
        self.sluttordensvurdering = [v if isinstance(v, SluttordensvurderingId) else SluttordensvurderingId(v) for v in self.sluttordensvurdering]

        if self.vitnemalsmerknad is not None and not isinstance(self.vitnemalsmerknad, VitnemalsmerknadId):
            self.vitnemalsmerknad = VitnemalsmerknadId(self.vitnemalsmerknad)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fravarsoversikt(YAMLRoot):
    """
    Oversikt over fråvær for ein elev i eit fag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Fravarsoversikt"]
    class_class_curie: ClassVar[str] = "utd:Fravarsoversikt"
    class_name: ClassVar[str] = "Fravarsoversikt"
    class_model_uri: ClassVar[URIRef] = UTD.Fravarsoversikt

    id: Union[str, FravarsoversiktId] = None
    halvaar: Union[dict, "Fravarsprosent"] = None
    skoleaarFravar: Union[dict, "Fravarsprosent"] = None
    elevforhold: Union[str, ElevforholdId] = None
    fag: Union[str, FagId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FravarsoversiktId):
            self.id = FravarsoversiktId(self.id)

        if self._is_empty(self.halvaar):
            self.MissingRequiredField("halvaar")
        if not isinstance(self.halvaar, Fravarsprosent):
            self.halvaar = Fravarsprosent(**as_dict(self.halvaar))

        if self._is_empty(self.skoleaarFravar):
            self.MissingRequiredField("skoleaarFravar")
        if not isinstance(self.skoleaarFravar, Fravarsprosent):
            self.skoleaarFravar = Fravarsprosent(**as_dict(self.skoleaarFravar))

        if self._is_empty(self.elevforhold):
            self.MissingRequiredField("elevforhold")
        if not isinstance(self.elevforhold, ElevforholdId):
            self.elevforhold = ElevforholdId(self.elevforhold)

        if self._is_empty(self.fag):
            self.MissingRequiredField("fag")
        if not isinstance(self.fag, FagId):
            self.fag = FagId(self.fag)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fravarsprosent(YAMLRoot):
    """
    Kompleks type som representerer fråværsprosent for ein periode.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Fravarsprosent"]
    class_class_curie: ClassVar[str] = "utd:Fravarsprosent"
    class_name: ClassVar[str] = "Fravarsprosent"
    class_model_uri: ClassVar[URIRef] = UTD.Fravarsprosent

    fravaerstimer: int = None
    prosent: int = None
    undervisningstimer: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fravaerstimer):
            self.MissingRequiredField("fravaerstimer")
        if not isinstance(self.fravaerstimer, int):
            self.fravaerstimer = int(self.fravaerstimer)

        if self._is_empty(self.prosent):
            self.MissingRequiredField("prosent")
        if not isinstance(self.prosent, int):
            self.prosent = int(self.prosent)

        if self._is_empty(self.undervisningstimer):
            self.MissingRequiredField("undervisningstimer")
        if not isinstance(self.undervisningstimer, int):
            self.undervisningstimer = int(self.undervisningstimer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fraversregistrering(YAMLRoot):
    """
    Ei enkelt fråversregistrering for ein elev.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Fraversregistrering"]
    class_class_curie: ClassVar[str] = "utd:Fraversregistrering"
    class_name: ClassVar[str] = "Fraversregistrering"
    class_model_uri: ClassVar[URIRef] = UTD.Fraversregistrering

    id: Union[str, FraversregistreringId] = None
    forersPaaVitnemaal: Union[bool, Bool] = None
    periode: Union[dict, "Periode"] = None
    undervisningsgruppe: Union[str, UndervisningsgruppeId] = None
    elevfravar: Union[str, ElevfravarId] = None
    fravartype: Union[str, FravartypeId] = None
    kommentar: Optional[str] = None
    registrertAv: Optional[Union[str, SkoleressursId]] = None
    faggruppe: Optional[Union[str, FaggruppeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FraversregistreringId):
            self.id = FraversregistreringId(self.id)

        if self._is_empty(self.forersPaaVitnemaal):
            self.MissingRequiredField("forersPaaVitnemaal")
        if not isinstance(self.forersPaaVitnemaal, Bool):
            self.forersPaaVitnemaal = Bool(self.forersPaaVitnemaal)

        if self._is_empty(self.periode):
            self.MissingRequiredField("periode")
        if not isinstance(self.periode, Periode):
            self.periode = Periode(**as_dict(self.periode))

        if self._is_empty(self.undervisningsgruppe):
            self.MissingRequiredField("undervisningsgruppe")
        if not isinstance(self.undervisningsgruppe, UndervisningsgruppeId):
            self.undervisningsgruppe = UndervisningsgruppeId(self.undervisningsgruppe)

        if self._is_empty(self.elevfravar):
            self.MissingRequiredField("elevfravar")
        if not isinstance(self.elevfravar, ElevfravarId):
            self.elevfravar = ElevfravarId(self.elevfravar)

        if self._is_empty(self.fravartype):
            self.MissingRequiredField("fravartype")
        if not isinstance(self.fravartype, FravartypeId):
            self.fravartype = FravartypeId(self.fravartype)

        if self.kommentar is not None and not isinstance(self.kommentar, str):
            self.kommentar = str(self.kommentar)

        if self.registrertAv is not None and not isinstance(self.registrertAv, SkoleressursId):
            self.registrertAv = SkoleressursId(self.registrertAv)

        if self.faggruppe is not None and not isinstance(self.faggruppe, FaggruppeId):
            self.faggruppe = FaggruppeId(self.faggruppe)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Halvaarsfagvurdering(FagvurderingAbstrakt):
    """
    Halvårsvurdering i eit fag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Halvaarsfagvurdering"]
    class_class_curie: ClassVar[str] = "utd:Halvaarsfagvurdering"
    class_name: ClassVar[str] = "Halvaarsfagvurdering"
    class_model_uri: ClassVar[URIRef] = UTD.Halvaarsfagvurdering

    id: Union[str, HalvaarsfagvurderingId] = None
    kommentar: str = None
    vurderingsdato: Union[str, XSDDateTime] = None
    elevvurdering: Union[str, ElevvurderingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HalvaarsfagvurderingId):
            self.id = HalvaarsfagvurderingId(self.id)

        if self._is_empty(self.elevvurdering):
            self.MissingRequiredField("elevvurdering")
        if not isinstance(self.elevvurdering, ElevvurderingId):
            self.elevvurdering = ElevvurderingId(self.elevvurdering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Halvaarsordensvurdering(OrdensvurderingAbstrakt):
    """
    Halvårsordensvurdering for ein elev.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Halvaarsordensvurdering"]
    class_class_curie: ClassVar[str] = "utd:Halvaarsordensvurdering"
    class_name: ClassVar[str] = "Halvaarsordensvurdering"
    class_model_uri: ClassVar[URIRef] = UTD.Halvaarsordensvurdering

    id: Union[str, HalvaarsordensvurderingId] = None
    kommentar: str = None
    vurderingsdato: Union[str, XSDDateTime] = None
    elevvurdering: Union[str, ElevvurderingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HalvaarsordensvurderingId):
            self.id = HalvaarsordensvurderingId(self.id)

        if self._is_empty(self.elevvurdering):
            self.MissingRequiredField("elevvurdering")
        if not isinstance(self.elevvurdering, ElevvurderingId):
            self.elevvurdering = ElevvurderingId(self.elevvurdering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Karakterhistorie(YAMLRoot):
    """
    Historikk over endringar i ein karakter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Karakterhistorie"]
    class_class_curie: ClassVar[str] = "utd:Karakterhistorie"
    class_name: ClassVar[str] = "Karakterhistorie"
    class_model_uri: ClassVar[URIRef] = UTD.Karakterhistorie

    id: Union[str, KarakterhistorieId] = None
    endretDato: Union[str, XSDDateTime] = None
    oppdatertAv: Optional[Union[str, SkoleressursId]] = None
    opprinneligKarakterverdi: Optional[Union[str, KarakterverdiId]] = None
    opprinneligKarakterstatus: Optional[Union[str, KarakterstatusId]] = None
    karakterverdi: Optional[Union[str, KarakterverdiId]] = None
    karakterstatus: Optional[Union[str, KarakterstatusId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KarakterhistorieId):
            self.id = KarakterhistorieId(self.id)

        if self._is_empty(self.endretDato):
            self.MissingRequiredField("endretDato")
        if not isinstance(self.endretDato, XSDDateTime):
            self.endretDato = XSDDateTime(self.endretDato)

        if self.oppdatertAv is not None and not isinstance(self.oppdatertAv, SkoleressursId):
            self.oppdatertAv = SkoleressursId(self.oppdatertAv)

        if self.opprinneligKarakterverdi is not None and not isinstance(self.opprinneligKarakterverdi, KarakterverdiId):
            self.opprinneligKarakterverdi = KarakterverdiId(self.opprinneligKarakterverdi)

        if self.opprinneligKarakterstatus is not None and not isinstance(self.opprinneligKarakterstatus, KarakterstatusId):
            self.opprinneligKarakterstatus = KarakterstatusId(self.opprinneligKarakterstatus)

        if self.karakterverdi is not None and not isinstance(self.karakterverdi, KarakterverdiId):
            self.karakterverdi = KarakterverdiId(self.karakterverdi)

        if self.karakterstatus is not None and not isinstance(self.karakterstatus, KarakterstatusId):
            self.karakterstatus = KarakterstatusId(self.karakterstatus)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sensor(YAMLRoot):
    """
    Ein sensor for ein eksamen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Sensor"]
    class_class_curie: ClassVar[str] = "utd:Sensor"
    class_name: ClassVar[str] = "Sensor"
    class_model_uri: ClassVar[URIRef] = UTD.Sensor

    id: Union[str, SensorId] = None
    aktiv: Union[bool, Bool] = None
    skoleressurs: Union[str, SkoleressursId] = None
    eksamensgruppe: Union[str, EksamensgruppeId] = None
    sensornummer: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SensorId):
            self.id = SensorId(self.id)

        if self._is_empty(self.aktiv):
            self.MissingRequiredField("aktiv")
        if not isinstance(self.aktiv, Bool):
            self.aktiv = Bool(self.aktiv)

        if self._is_empty(self.skoleressurs):
            self.MissingRequiredField("skoleressurs")
        if not isinstance(self.skoleressurs, SkoleressursId):
            self.skoleressurs = SkoleressursId(self.skoleressurs)

        if self._is_empty(self.eksamensgruppe):
            self.MissingRequiredField("eksamensgruppe")
        if not isinstance(self.eksamensgruppe, EksamensgruppeId):
            self.eksamensgruppe = EksamensgruppeId(self.eksamensgruppe)

        if self.sensornummer is not None and not isinstance(self.sensornummer, int):
            self.sensornummer = int(self.sensornummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sluttfagvurdering(FagvurderingAbstrakt):
    """
    Sluttkarakter i eit fag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Sluttfagvurdering"]
    class_class_curie: ClassVar[str] = "utd:Sluttfagvurdering"
    class_name: ClassVar[str] = "Sluttfagvurdering"
    class_model_uri: ClassVar[URIRef] = UTD.Sluttfagvurdering

    id: Union[str, SluttfagvurderingId] = None
    kommentar: str = None
    vurderingsdato: Union[str, XSDDateTime] = None
    elevvurdering: Union[str, ElevvurderingId] = None
    eksamensgruppe: Optional[Union[str, EksamensgruppeId]] = None
    karakterhistorie: Optional[Union[Union[str, KarakterhistorieId], list[Union[str, KarakterhistorieId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SluttfagvurderingId):
            self.id = SluttfagvurderingId(self.id)

        if self._is_empty(self.elevvurdering):
            self.MissingRequiredField("elevvurdering")
        if not isinstance(self.elevvurdering, ElevvurderingId):
            self.elevvurdering = ElevvurderingId(self.elevvurdering)

        if self.eksamensgruppe is not None and not isinstance(self.eksamensgruppe, EksamensgruppeId):
            self.eksamensgruppe = EksamensgruppeId(self.eksamensgruppe)

        if not isinstance(self.karakterhistorie, list):
            self.karakterhistorie = [self.karakterhistorie] if self.karakterhistorie is not None else []
        self.karakterhistorie = [v if isinstance(v, KarakterhistorieId) else KarakterhistorieId(v) for v in self.karakterhistorie]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sluttordensvurdering(OrdensvurderingAbstrakt):
    """
    Sluttordensvurdering for ein elev.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Sluttordensvurdering"]
    class_class_curie: ClassVar[str] = "utd:Sluttordensvurdering"
    class_name: ClassVar[str] = "Sluttordensvurdering"
    class_model_uri: ClassVar[URIRef] = UTD.Sluttordensvurdering

    id: Union[str, SluttordensvurderingId] = None
    kommentar: str = None
    vurderingsdato: Union[str, XSDDateTime] = None
    elevvurdering: Union[str, ElevvurderingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SluttordensvurderingId):
            self.id = SluttordensvurderingId(self.id)

        if self._is_empty(self.elevvurdering):
            self.MissingRequiredField("elevvurdering")
        if not isinstance(self.elevvurdering, ElevvurderingId):
            self.elevvurdering = ElevvurderingId(self.elevvurdering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Underveisfagvurdering(FagvurderingAbstrakt):
    """
    Underveisfagvurdering for ein elev.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Underveisfagvurdering"]
    class_class_curie: ClassVar[str] = "utd:Underveisfagvurdering"
    class_name: ClassVar[str] = "Underveisfagvurdering"
    class_model_uri: ClassVar[URIRef] = UTD.Underveisfagvurdering

    id: Union[str, UnderveisfagvurderingId] = None
    kommentar: str = None
    vurderingsdato: Union[str, XSDDateTime] = None
    elevvurdering: Union[str, ElevvurderingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnderveisfagvurderingId):
            self.id = UnderveisfagvurderingId(self.id)

        if self._is_empty(self.elevvurdering):
            self.MissingRequiredField("elevvurdering")
        if not isinstance(self.elevvurdering, ElevvurderingId):
            self.elevvurdering = ElevvurderingId(self.elevvurdering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Underveisordensvurdering(OrdensvurderingAbstrakt):
    """
    Underveisordensvurdering for ein elev.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Underveisordensvurdering"]
    class_class_curie: ClassVar[str] = "utd:Underveisordensvurdering"
    class_name: ClassVar[str] = "Underveisordensvurdering"
    class_model_uri: ClassVar[URIRef] = UTD.Underveisordensvurdering

    id: Union[str, UnderveisordensvurderingId] = None
    kommentar: str = None
    vurderingsdato: Union[str, XSDDateTime] = None
    elevvurdering: Union[str, ElevvurderingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnderveisordensvurderingId):
            self.id = UnderveisordensvurderingId(self.id)

        if self._is_empty(self.elevvurdering):
            self.MissingRequiredField("elevvurdering")
        if not isinstance(self.elevvurdering, ElevvurderingId):
            self.elevvurdering = ElevvurderingId(self.elevvurdering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AvlagtProve(YAMLRoot):
    """
    Ei avlagt prøve for ein lærling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["AvlagtProve"]
    class_class_curie: ClassVar[str] = "utd:AvlagtProve"
    class_name: ClassVar[str] = "AvlagtProve"
    class_model_uri: ClassVar[URIRef] = UTD.AvlagtProve

    id: Union[str, AvlagtProveId] = None
    laerling: Union[str, LaerlingId] = None
    provedato: Optional[Union[str, XSDDate]] = None
    provestatus: Optional[Union[str, ProvestatusId]] = None
    fullfortkode: Optional[Union[str, FullfortkodeId]] = None
    brevtype: Optional[Union[str, BrevtypeId]] = None
    bevistype: Optional[Union[str, BevistypeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AvlagtProveId):
            self.id = AvlagtProveId(self.id)

        if self._is_empty(self.laerling):
            self.MissingRequiredField("laerling")
        if not isinstance(self.laerling, LaerlingId):
            self.laerling = LaerlingId(self.laerling)

        if self.provedato is not None and not isinstance(self.provedato, XSDDate):
            self.provedato = XSDDate(self.provedato)

        if self.provestatus is not None and not isinstance(self.provestatus, ProvestatusId):
            self.provestatus = ProvestatusId(self.provestatus)

        if self.fullfortkode is not None and not isinstance(self.fullfortkode, FullfortkodeId):
            self.fullfortkode = FullfortkodeId(self.fullfortkode)

        if self.brevtype is not None and not isinstance(self.brevtype, BrevtypeId):
            self.brevtype = BrevtypeId(self.brevtype)

        if self.bevistype is not None and not isinstance(self.bevistype, BevistypeId):
            self.bevistype = BevistypeId(self.bevistype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Laerling(YAMLRoot):
    """
    Ein lærling i yrkesopplæring.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Laerling"]
    class_class_curie: ClassVar[str] = "utd:Laerling"
    class_name: ClassVar[str] = "Laerling"
    class_model_uri: ClassVar[URIRef] = UTD.Laerling

    id: Union[str, LaerlingId] = None
    person: Union[str, URIorCURIE] = None
    kontraktstype: Optional[str] = None
    laretid: Optional[Union[dict, "Periode"]] = None
    bedrift: Optional[Union[str, URIorCURIE]] = None
    avlagtprove: Optional[Union[Union[str, AvlagtProveId], list[Union[str, AvlagtProveId]]]] = empty_list()
    programomrade: Optional[Union[str, ProgramomradeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LaerlingId):
            self.id = LaerlingId(self.id)

        if self._is_empty(self.person):
            self.MissingRequiredField("person")
        if not isinstance(self.person, URIorCURIE):
            self.person = URIorCURIE(self.person)

        if self.kontraktstype is not None and not isinstance(self.kontraktstype, str):
            self.kontraktstype = str(self.kontraktstype)

        if self.laretid is not None and not isinstance(self.laretid, Periode):
            self.laretid = Periode(**as_dict(self.laretid))

        if self.bedrift is not None and not isinstance(self.bedrift, URIorCURIE):
            self.bedrift = URIorCURIE(self.bedrift)

        if not isinstance(self.avlagtprove, list):
            self.avlagtprove = [self.avlagtprove] if self.avlagtprove is not None else []
        self.avlagtprove = [v if isinstance(v, AvlagtProveId) else AvlagtProveId(v) for v in self.avlagtprove]

        if self.programomrade is not None and not isinstance(self.programomrade, ProgramomradeId):
            self.programomrade = ProgramomradeId(self.programomrade)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OtUngdom(YAMLRoot):
    """
    Eit ungdomsobjekt i oppfølgingstenesta (OT).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["OtUngdom"]
    class_class_curie: ClassVar[str] = "utd:OtUngdom"
    class_name: ClassVar[str] = "OtUngdom"
    class_model_uri: ClassVar[URIRef] = UTD.OtUngdom

    id: Union[str, OtUngdomId] = None
    person: Union[str, URIorCURIE] = None
    status: Optional[Union[str, OtStatusId]] = None
    enhet: Optional[Union[str, OtEnhetId]] = None
    programomrade: Optional[Union[str, ProgramomradeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OtUngdomId):
            self.id = OtUngdomId(self.id)

        if self._is_empty(self.person):
            self.MissingRequiredField("person")
        if not isinstance(self.person, URIorCURIE):
            self.person = URIorCURIE(self.person)

        if self.status is not None and not isinstance(self.status, OtStatusId):
            self.status = OtStatusId(self.status)

        if self.enhet is not None and not isinstance(self.enhet, OtEnhetId):
            self.enhet = OtEnhetId(self.enhet)

        if self.programomrade is not None and not isinstance(self.programomrade, ProgramomradeId):
            self.programomrade = ProgramomradeId(self.programomrade)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Avbruddsaarsak(YAMLRoot):
    """
    Årsak til avbrot frå opplæring.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Avbruddsaarsak"]
    class_class_curie: ClassVar[str] = "utd:Avbruddsaarsak"
    class_name: ClassVar[str] = "Avbruddsaarsak"
    class_model_uri: ClassVar[URIRef] = UTD.Avbruddsaarsak

    id: Union[str, AvbruddsaarsakId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AvbruddsaarsakId):
            self.id = AvbruddsaarsakId(self.id)

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
class Betalingsstatus(YAMLRoot):
    """
    Betalingsstatus for eksamensavgift.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Betalingsstatus"]
    class_class_curie: ClassVar[str] = "utd:Betalingsstatus"
    class_name: ClassVar[str] = "Betalingsstatus"
    class_model_uri: ClassVar[URIRef] = UTD.Betalingsstatus

    id: Union[str, BetalingsstatusId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BetalingsstatusId):
            self.id = BetalingsstatusId(self.id)

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
class Bevistype(YAMLRoot):
    """
    Type kompetansebevis for lærling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Bevistype"]
    class_class_curie: ClassVar[str] = "utd:Bevistype"
    class_name: ClassVar[str] = "Bevistype"
    class_model_uri: ClassVar[URIRef] = UTD.Bevistype

    id: Union[str, BevistypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BevistypeId):
            self.id = BevistypeId(self.id)

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
class Brevtype(YAMLRoot):
    """
    Type brev knytt til lærlingprøve.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Brevtype"]
    class_class_curie: ClassVar[str] = "utd:Brevtype"
    class_name: ClassVar[str] = "Brevtype"
    class_model_uri: ClassVar[URIRef] = UTD.Brevtype

    id: Union[str, BrevtypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BrevtypeId):
            self.id = BrevtypeId(self.id)

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
class Eksamensform(YAMLRoot):
    """
    Form for gjennomføring av eksamen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Eksamensform"]
    class_class_curie: ClassVar[str] = "utd:Eksamensform"
    class_name: ClassVar[str] = "Eksamensform"
    class_model_uri: ClassVar[URIRef] = UTD.Eksamensform

    id: Union[str, EksamensformId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EksamensformId):
            self.id = EksamensformId(self.id)

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
class Elevkategori(YAMLRoot):
    """
    Kategori for eit elevforhold (t.d. Ordinær, Privatist, Voksen).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Elevkategori"]
    class_class_curie: ClassVar[str] = "utd:Elevkategori"
    class_name: ClassVar[str] = "Elevkategori"
    class_model_uri: ClassVar[URIRef] = UTD.Elevkategori

    id: Union[str, ElevkategoriId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElevkategoriId):
            self.id = ElevkategoriId(self.id)

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
class Fagmerknad(YAMLRoot):
    """
    Merknad knytt til eit fag i ei faggruppe.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Fagmerknad"]
    class_class_curie: ClassVar[str] = "utd:Fagmerknad"
    class_name: ClassVar[str] = "Fagmerknad"
    class_model_uri: ClassVar[URIRef] = UTD.Fagmerknad

    id: Union[str, FagmerknadId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FagmerknadId):
            self.id = FagmerknadId(self.id)

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
class Fagstatus(YAMLRoot):
    """
    Status for eit fag i eit faggruppemedlemskap.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Fagstatus"]
    class_class_curie: ClassVar[str] = "utd:Fagstatus"
    class_name: ClassVar[str] = "Fagstatus"
    class_model_uri: ClassVar[URIRef] = UTD.Fagstatus

    id: Union[str, FagstatusId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FagstatusId):
            self.id = FagstatusId(self.id)

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
class Fravartype(YAMLRoot):
    """
    Type fråvær (t.d. Udokumentert, Dokumentert).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Fravartype"]
    class_class_curie: ClassVar[str] = "utd:Fravartype"
    class_name: ClassVar[str] = "Fravartype"
    class_model_uri: ClassVar[URIRef] = UTD.Fravartype

    id: Union[str, FravartypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FravartypeId):
            self.id = FravartypeId(self.id)

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
class Fullfortkode(YAMLRoot):
    """
    Kode for fullførtresultat av lærling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Fullfortkode"]
    class_class_curie: ClassVar[str] = "utd:Fullfortkode"
    class_name: ClassVar[str] = "Fullfortkode"
    class_model_uri: ClassVar[URIRef] = UTD.Fullfortkode

    id: Union[str, FullfortkodeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FullfortkodeId):
            self.id = FullfortkodeId(self.id)

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
class Karakterskala(YAMLRoot):
    """
    Skala for karaktersetjing (t.d. 1-6, Bestått/Ikkje bestått).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Karakterskala"]
    class_class_curie: ClassVar[str] = "utd:Karakterskala"
    class_name: ClassVar[str] = "Karakterskala"
    class_model_uri: ClassVar[URIRef] = UTD.Karakterskala

    id: Union[str, KarakterskalaId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None
    verdi: Optional[Union[Union[str, KarakterverdiId], list[Union[str, KarakterverdiId]]]] = empty_list()
    vigoreferanse: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KarakterskalaId):
            self.id = KarakterskalaId(self.id)

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

        if not isinstance(self.verdi, list):
            self.verdi = [self.verdi] if self.verdi is not None else []
        self.verdi = [v if isinstance(v, KarakterverdiId) else KarakterverdiId(v) for v in self.verdi]

        if self.vigoreferanse is not None and not isinstance(self.vigoreferanse, URIorCURIE):
            self.vigoreferanse = URIorCURIE(self.vigoreferanse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Karakterstatus(YAMLRoot):
    """
    Status for ein karakter (t.d. Fråvær, Friteke).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Karakterstatus"]
    class_class_curie: ClassVar[str] = "utd:Karakterstatus"
    class_name: ClassVar[str] = "Karakterstatus"
    class_model_uri: ClassVar[URIRef] = UTD.Karakterstatus

    id: Union[str, KarakterstatusId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KarakterstatusId):
            self.id = KarakterstatusId(self.id)

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
class Karakterverdi(YAMLRoot):
    """
    Ein konkret karakterverdi i ei karakterskala.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Karakterverdi"]
    class_class_curie: ClassVar[str] = "utd:Karakterverdi"
    class_name: ClassVar[str] = "Karakterverdi"
    class_model_uri: ClassVar[URIRef] = UTD.Karakterverdi

    id: Union[str, KarakterverdiId] = None
    kode: str = None
    navn: str = None
    skala: Union[str, KarakterskalaId] = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KarakterverdiId):
            self.id = KarakterverdiId(self.id)

        if self._is_empty(self.kode):
            self.MissingRequiredField("kode")
        if not isinstance(self.kode, str):
            self.kode = str(self.kode)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self._is_empty(self.skala):
            self.MissingRequiredField("skala")
        if not isinstance(self.skala, KarakterskalaId):
            self.skala = KarakterskalaId(self.skala)

        if self.gyldighetsperiode is not None and not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self.passiv is not None and not isinstance(self.passiv, Bool):
            self.passiv = Bool(self.passiv)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OtEnhet(YAMLRoot):
    """
    Eining i oppfølgingstenesta (OT).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["OtEnhet"]
    class_class_curie: ClassVar[str] = "utd:OtEnhet"
    class_name: ClassVar[str] = "OtEnhet"
    class_model_uri: ClassVar[URIRef] = UTD.OtEnhet

    id: Union[str, OtEnhetId] = None
    kode: str = None
    navn: str = None
    kommune: Union[str, URIorCURIE] = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OtEnhetId):
            self.id = OtEnhetId(self.id)

        if self._is_empty(self.kode):
            self.MissingRequiredField("kode")
        if not isinstance(self.kode, str):
            self.kode = str(self.kode)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self._is_empty(self.kommune):
            self.MissingRequiredField("kommune")
        if not isinstance(self.kommune, URIorCURIE):
            self.kommune = URIorCURIE(self.kommune)

        if self.gyldighetsperiode is not None and not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self.passiv is not None and not isinstance(self.passiv, Bool):
            self.passiv = Bool(self.passiv)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OtStatus(YAMLRoot):
    """
    Status for ein ungdom i oppfølgingstenesta.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["OtStatus"]
    class_class_curie: ClassVar[str] = "utd:OtStatus"
    class_name: ClassVar[str] = "OtStatus"
    class_model_uri: ClassVar[URIRef] = UTD.OtStatus

    id: Union[str, OtStatusId] = None
    kode: str = None
    navn: str = None
    type: str = None
    beskrivelse: Optional[str] = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OtStatusId):
            self.id = OtStatusId(self.id)

        if self._is_empty(self.kode):
            self.MissingRequiredField("kode")
        if not isinstance(self.kode, str):
            self.kode = str(self.kode)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if self.gyldighetsperiode is not None and not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self.passiv is not None and not isinstance(self.passiv, Bool):
            self.passiv = Bool(self.passiv)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Provestatus(YAMLRoot):
    """
    Status for ei lærlingprøve.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Provestatus"]
    class_class_curie: ClassVar[str] = "utd:Provestatus"
    class_name: ClassVar[str] = "Provestatus"
    class_model_uri: ClassVar[URIRef] = UTD.Provestatus

    id: Union[str, ProvestatusId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProvestatusId):
            self.id = ProvestatusId(self.id)

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
class Skoleaar(YAMLRoot):
    """
    Eit skoleår (t.d. 2024/2025).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Skoleaar"]
    class_class_curie: ClassVar[str] = "utd:Skoleaar"
    class_name: ClassVar[str] = "Skoleaar"
    class_model_uri: ClassVar[URIRef] = UTD.Skoleaar

    id: Union[str, SkoleaarId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SkoleaarId):
            self.id = SkoleaarId(self.id)

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
class Skoleeiertype(YAMLRoot):
    """
    Type skuleeigartilknyting.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Skoleeiertype"]
    class_class_curie: ClassVar[str] = "utd:Skoleeiertype"
    class_name: ClassVar[str] = "Skoleeiertype"
    class_model_uri: ClassVar[URIRef] = UTD.Skoleeiertype

    id: Union[str, SkoleeiertypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SkoleeiertypeId):
            self.id = SkoleeiertypeId(self.id)

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
class Termin(YAMLRoot):
    """
    Ein skuleterm (t.d. Haust, Vår) — kodeverk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Termin"]
    class_class_curie: ClassVar[str] = "utd:Termin"
    class_name: ClassVar[str] = "Termin"
    class_model_uri: ClassVar[URIRef] = UTD.Termin

    id: Union[str, TerminId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TerminId):
            self.id = TerminId(self.id)

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
class Tilrettelegging(YAMLRoot):
    """
    Type tilrettelegging for elevar (t.d. Utvida tid).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Tilrettelegging"]
    class_class_curie: ClassVar[str] = "utd:Tilrettelegging"
    class_name: ClassVar[str] = "Tilrettelegging"
    class_model_uri: ClassVar[URIRef] = UTD.Tilrettelegging

    id: Union[str, TilretteleggingId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TilretteleggingId):
            self.id = TilretteleggingId(self.id)

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
class Varseltype(YAMLRoot):
    """
    Type varsel knytt til ein elev.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Varseltype"]
    class_class_curie: ClassVar[str] = "utd:Varseltype"
    class_name: ClassVar[str] = "Varseltype"
    class_model_uri: ClassVar[URIRef] = UTD.Varseltype

    id: Union[str, VarseltypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VarseltypeId):
            self.id = VarseltypeId(self.id)

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
class Vitnemalsmerknad(YAMLRoot):
    """
    Merknad på vitnemål.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UTD["Vitnemalsmerknad"]
    class_class_curie: ClassVar[str] = "utd:Vitnemalsmerknad"
    class_name: ClassVar[str] = "Vitnemalsmerknad"
    class_model_uri: ClassVar[URIRef] = UTD.Vitnemalsmerknad

    id: Union[str, VitnemalsmerknadId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VitnemalsmerknadId):
            self.id = VitnemalsmerknadId(self.id)

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
    class_model_uri: ClassVar[URIRef] = UTD.Aktoer

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
    class_model_uri: ClassVar[URIRef] = UTD.Begrep

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
    class_model_uri: ClassVar[URIRef] = UTD.Enhet

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
    class_model_uri: ClassVar[URIRef] = UTD.Identifikator

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
    class_model_uri: ClassVar[URIRef] = UTD.Periode

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
    class_model_uri: ClassVar[URIRef] = UTD.Personnavn

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
    class_model_uri: ClassVar[URIRef] = UTD.Kontaktinformasjon

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
    class_model_uri: ClassVar[URIRef] = UTD.Adresse

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
    class_model_uri: ClassVar[URIRef] = UTD.Matrikkelnummer

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
    class_model_uri: ClassVar[URIRef] = UTD.Landkode

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
    class_model_uri: ClassVar[URIRef] = UTD.Kjonn

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
    class_model_uri: ClassVar[URIRef] = UTD.Fylke

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
    class_model_uri: ClassVar[URIRef] = UTD.Kommune

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
    class_model_uri: ClassVar[URIRef] = UTD.Spraak

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
    class_model_uri: ClassVar[URIRef] = UTD.Valuta

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
    class_model_uri: ClassVar[URIRef] = UTD.Person

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
    class_model_uri: ClassVar[URIRef] = UTD.Kontaktperson

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
    class_model_uri: ClassVar[URIRef] = UTD.Virksomhet

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
                   model_uri=UTD.id, domain=None, range=URIRef)

slots.utdanningContainer__elevar = Slot(uri=UTD.elevar, name="utdanningContainer__elevar", curie=UTD.curie('elevar'),
                   model_uri=UTD.utdanningContainer__elevar, domain=None, range=Optional[Union[dict[Union[str, ElevId], Union[dict, Elev]], list[Union[dict, Elev]]]])

slots.utdanningContainer__skolar = Slot(uri=UTD.skolar, name="utdanningContainer__skolar", curie=UTD.curie('skolar'),
                   model_uri=UTD.utdanningContainer__skolar, domain=None, range=Optional[Union[dict[Union[str, SkoleId], Union[dict, Skole]], list[Union[dict, Skole]]]])

slots.utdanningContainer__skoleressursar = Slot(uri=UTD.skoleressursar, name="utdanningContainer__skoleressursar", curie=UTD.curie('skoleressursar'),
                   model_uri=UTD.utdanningContainer__skoleressursar, domain=None, range=Optional[Union[dict[Union[str, SkoleressursId], Union[dict, Skoleressurs]], list[Union[dict, Skoleressurs]]]])

slots.utdanningContainer__elevforhold = Slot(uri=UTD.elevforhold, name="utdanningContainer__elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.utdanningContainer__elevforhold, domain=None, range=Optional[Union[dict[Union[str, ElevforholdId], Union[dict, Elevforhold]], list[Union[dict, Elevforhold]]]])

slots.utdanningContainer__elevtilrettelegging = Slot(uri=UTD.elevtilrettelegging, name="utdanningContainer__elevtilrettelegging", curie=UTD.curie('elevtilrettelegging'),
                   model_uri=UTD.utdanningContainer__elevtilrettelegging, domain=None, range=Optional[Union[dict[Union[str, ElevtilretteleggingId], Union[dict, Elevtilrettelegging]], list[Union[dict, Elevtilrettelegging]]]])

slots.utdanningContainer__klasser = Slot(uri=UTD.klasser, name="utdanningContainer__klasser", curie=UTD.curie('klasser'),
                   model_uri=UTD.utdanningContainer__klasser, domain=None, range=Optional[Union[dict[Union[str, KlasseId], Union[dict, Klasse]], list[Union[dict, Klasse]]]])

slots.utdanningContainer__klassemedlemskap = Slot(uri=UTD.klassemedlemskap, name="utdanningContainer__klassemedlemskap", curie=UTD.curie('klassemedlemskap'),
                   model_uri=UTD.utdanningContainer__klassemedlemskap, domain=None, range=Optional[Union[dict[Union[str, KlassemedlemskapId], Union[dict, Klassemedlemskap]], list[Union[dict, Klassemedlemskap]]]])

slots.utdanningContainer__kontaktlaerergrupper = Slot(uri=UTD.kontaktlaerergrupper, name="utdanningContainer__kontaktlaerergrupper", curie=UTD.curie('kontaktlaerergrupper'),
                   model_uri=UTD.utdanningContainer__kontaktlaerergrupper, domain=None, range=Optional[Union[dict[Union[str, KontaktlaerergruppeId], Union[dict, Kontaktlaerergruppe]], list[Union[dict, Kontaktlaerergruppe]]]])

slots.utdanningContainer__kontaktlaerergruppemedlemskap = Slot(uri=UTD.kontaktlaerergruppemedlemskap, name="utdanningContainer__kontaktlaerergruppemedlemskap", curie=UTD.curie('kontaktlaerergruppemedlemskap'),
                   model_uri=UTD.utdanningContainer__kontaktlaerergruppemedlemskap, domain=None, range=Optional[Union[dict[Union[str, KontaktlaerergruppemedlemskapId], Union[dict, Kontaktlaerergruppemedlemskap]], list[Union[dict, Kontaktlaerergruppemedlemskap]]]])

slots.utdanningContainer__persongrupper = Slot(uri=UTD.persongrupper, name="utdanningContainer__persongrupper", curie=UTD.curie('persongrupper'),
                   model_uri=UTD.utdanningContainer__persongrupper, domain=None, range=Optional[Union[dict[Union[str, PersongruppeId], Union[dict, Persongruppe]], list[Union[dict, Persongruppe]]]])

slots.utdanningContainer__persongruppemedlemskap = Slot(uri=UTD.persongruppemedlemskap, name="utdanningContainer__persongruppemedlemskap", curie=UTD.curie('persongruppemedlemskap'),
                   model_uri=UTD.utdanningContainer__persongruppemedlemskap, domain=None, range=Optional[Union[dict[Union[str, PersongruppemedlemskapId], Union[dict, Persongruppemedlemskap]], list[Union[dict, Persongruppemedlemskap]]]])

slots.utdanningContainer__varsel = Slot(uri=UTD.varsel, name="utdanningContainer__varsel", curie=UTD.curie('varsel'),
                   model_uri=UTD.utdanningContainer__varsel, domain=None, range=Optional[Union[dict[Union[str, VarselId], Union[dict, Varsel]], list[Union[dict, Varsel]]]])

slots.utdanningContainer__arstrinn = Slot(uri=UTD.arstrinn, name="utdanningContainer__arstrinn", curie=UTD.curie('arstrinn'),
                   model_uri=UTD.utdanningContainer__arstrinn, domain=None, range=Optional[Union[dict[Union[str, ArstrinnId], Union[dict, Arstrinn]], list[Union[dict, Arstrinn]]]])

slots.utdanningContainer__programomrader = Slot(uri=UTD.programomrader, name="utdanningContainer__programomrader", curie=UTD.curie('programomrader'),
                   model_uri=UTD.utdanningContainer__programomrader, domain=None, range=Optional[Union[dict[Union[str, ProgramomradeId], Union[dict, Programomrade]], list[Union[dict, Programomrade]]]])

slots.utdanningContainer__programomrademedlemskap = Slot(uri=UTD.programomrademedlemskap, name="utdanningContainer__programomrademedlemskap", curie=UTD.curie('programomrademedlemskap'),
                   model_uri=UTD.utdanningContainer__programomrademedlemskap, domain=None, range=Optional[Union[dict[Union[str, ProgramomrademedlemskapId], Union[dict, Programomrademedlemskap]], list[Union[dict, Programomrademedlemskap]]]])

slots.utdanningContainer__utdanningsprogram = Slot(uri=UTD.utdanningsprogram, name="utdanningContainer__utdanningsprogram", curie=UTD.curie('utdanningsprogram'),
                   model_uri=UTD.utdanningContainer__utdanningsprogram, domain=None, range=Optional[Union[dict[Union[str, UtdanningsprogramId], Union[dict, Utdanningsprogram]], list[Union[dict, Utdanningsprogram]]]])

slots.utdanningContainer__eksamen = Slot(uri=UTD.eksamen, name="utdanningContainer__eksamen", curie=UTD.curie('eksamen'),
                   model_uri=UTD.utdanningContainer__eksamen, domain=None, range=Optional[Union[dict[Union[str, EksamenId], Union[dict, Eksamen]], list[Union[dict, Eksamen]]]])

slots.utdanningContainer__fag = Slot(uri=UTD.fag, name="utdanningContainer__fag", curie=UTD.curie('fag'),
                   model_uri=UTD.utdanningContainer__fag, domain=None, range=Optional[Union[dict[Union[str, FagId], Union[dict, Fag]], list[Union[dict, Fag]]]])

slots.utdanningContainer__faggrupper = Slot(uri=UTD.faggrupper, name="utdanningContainer__faggrupper", curie=UTD.curie('faggrupper'),
                   model_uri=UTD.utdanningContainer__faggrupper, domain=None, range=Optional[Union[dict[Union[str, FaggruppeId], Union[dict, Faggruppe]], list[Union[dict, Faggruppe]]]])

slots.utdanningContainer__faggruppemedlemskap = Slot(uri=UTD.faggruppemedlemskap, name="utdanningContainer__faggruppemedlemskap", curie=UTD.curie('faggruppemedlemskap'),
                   model_uri=UTD.utdanningContainer__faggruppemedlemskap, domain=None, range=Optional[Union[dict[Union[str, FaggruppemedlemskapId], Union[dict, Faggruppemedlemskap]], list[Union[dict, Faggruppemedlemskap]]]])

slots.utdanningContainer__rom = Slot(uri=UTD.rom, name="utdanningContainer__rom", curie=UTD.curie('rom'),
                   model_uri=UTD.utdanningContainer__rom, domain=None, range=Optional[Union[dict[Union[str, RomId], Union[dict, Rom]], list[Union[dict, Rom]]]])

slots.utdanningContainer__timar = Slot(uri=UTD.timar, name="utdanningContainer__timar", curie=UTD.curie('timar'),
                   model_uri=UTD.utdanningContainer__timar, domain=None, range=Optional[Union[dict[Union[str, TimeId], Union[dict, Time]], list[Union[dict, Time]]]])

slots.utdanningContainer__undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="utdanningContainer__undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.utdanningContainer__undervisningsforhold, domain=None, range=Optional[Union[dict[Union[str, UndervisningsforholdId], Union[dict, Undervisningsforhold]], list[Union[dict, Undervisningsforhold]]]])

slots.utdanningContainer__undervisningsgrupper = Slot(uri=UTD.undervisningsgrupper, name="utdanningContainer__undervisningsgrupper", curie=UTD.curie('undervisningsgrupper'),
                   model_uri=UTD.utdanningContainer__undervisningsgrupper, domain=None, range=Optional[Union[dict[Union[str, UndervisningsgruppeId], Union[dict, Undervisningsgruppe]], list[Union[dict, Undervisningsgruppe]]]])

slots.utdanningContainer__undervisningsgruppemedlemskap = Slot(uri=UTD.undervisningsgruppemedlemskap, name="utdanningContainer__undervisningsgruppemedlemskap", curie=UTD.curie('undervisningsgruppemedlemskap'),
                   model_uri=UTD.utdanningContainer__undervisningsgruppemedlemskap, domain=None, range=Optional[Union[dict[Union[str, UndervisningsgruppemedlemskapId], Union[dict, Undervisningsgruppemedlemskap]], list[Union[dict, Undervisningsgruppemedlemskap]]]])

slots.utdanningContainer__anmerkningar = Slot(uri=UTD.anmerkningar, name="utdanningContainer__anmerkningar", curie=UTD.curie('anmerkningar'),
                   model_uri=UTD.utdanningContainer__anmerkningar, domain=None, range=Optional[Union[dict[Union[str, AnmerkningerId], Union[dict, Anmerkninger]], list[Union[dict, Anmerkninger]]]])

slots.utdanningContainer__eksamensgrupper = Slot(uri=UTD.eksamensgrupper, name="utdanningContainer__eksamensgrupper", curie=UTD.curie('eksamensgrupper'),
                   model_uri=UTD.utdanningContainer__eksamensgrupper, domain=None, range=Optional[Union[dict[Union[str, EksamensgruppeId], Union[dict, Eksamensgruppe]], list[Union[dict, Eksamensgruppe]]]])

slots.utdanningContainer__eksamensgruppemedlemskap = Slot(uri=UTD.eksamensgruppemedlemskap, name="utdanningContainer__eksamensgruppemedlemskap", curie=UTD.curie('eksamensgruppemedlemskap'),
                   model_uri=UTD.utdanningContainer__eksamensgruppemedlemskap, domain=None, range=Optional[Union[dict[Union[str, EksamensgruppemedlemskapId], Union[dict, Eksamensgruppemedlemskap]], list[Union[dict, Eksamensgruppemedlemskap]]]])

slots.utdanningContainer__eksamensvurdering = Slot(uri=UTD.eksamensvurdering, name="utdanningContainer__eksamensvurdering", curie=UTD.curie('eksamensvurdering'),
                   model_uri=UTD.utdanningContainer__eksamensvurdering, domain=None, range=Optional[Union[dict[Union[str, EksamensvurderingId], Union[dict, Eksamensvurdering]], list[Union[dict, Eksamensvurdering]]]])

slots.utdanningContainer__elevfravar = Slot(uri=UTD.elevfravar, name="utdanningContainer__elevfravar", curie=UTD.curie('elevfravar'),
                   model_uri=UTD.utdanningContainer__elevfravar, domain=None, range=Optional[Union[dict[Union[str, ElevfravarId], Union[dict, Elevfravar]], list[Union[dict, Elevfravar]]]])

slots.utdanningContainer__elevvurdering = Slot(uri=UTD.elevvurdering, name="utdanningContainer__elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.utdanningContainer__elevvurdering, domain=None, range=Optional[Union[dict[Union[str, ElevvurderingId], Union[dict, Elevvurdering]], list[Union[dict, Elevvurdering]]]])

slots.utdanningContainer__fravarsoversikt = Slot(uri=UTD.fravarsoversikt, name="utdanningContainer__fravarsoversikt", curie=UTD.curie('fravarsoversikt'),
                   model_uri=UTD.utdanningContainer__fravarsoversikt, domain=None, range=Optional[Union[dict[Union[str, FravarsoversiktId], Union[dict, Fravarsoversikt]], list[Union[dict, Fravarsoversikt]]]])

slots.utdanningContainer__fraversregistrering = Slot(uri=UTD.fraversregistrering, name="utdanningContainer__fraversregistrering", curie=UTD.curie('fraversregistrering'),
                   model_uri=UTD.utdanningContainer__fraversregistrering, domain=None, range=Optional[Union[dict[Union[str, FraversregistreringId], Union[dict, Fraversregistrering]], list[Union[dict, Fraversregistrering]]]])

slots.utdanningContainer__halvaarsfagvurdering = Slot(uri=UTD.halvaarsfagvurdering, name="utdanningContainer__halvaarsfagvurdering", curie=UTD.curie('halvaarsfagvurdering'),
                   model_uri=UTD.utdanningContainer__halvaarsfagvurdering, domain=None, range=Optional[Union[dict[Union[str, HalvaarsfagvurderingId], Union[dict, Halvaarsfagvurdering]], list[Union[dict, Halvaarsfagvurdering]]]])

slots.utdanningContainer__halvaarsordensvurdering = Slot(uri=UTD.halvaarsordensvurdering, name="utdanningContainer__halvaarsordensvurdering", curie=UTD.curie('halvaarsordensvurdering'),
                   model_uri=UTD.utdanningContainer__halvaarsordensvurdering, domain=None, range=Optional[Union[dict[Union[str, HalvaarsordensvurderingId], Union[dict, Halvaarsordensvurdering]], list[Union[dict, Halvaarsordensvurdering]]]])

slots.utdanningContainer__karakterhistorie = Slot(uri=UTD.karakterhistorie, name="utdanningContainer__karakterhistorie", curie=UTD.curie('karakterhistorie'),
                   model_uri=UTD.utdanningContainer__karakterhistorie, domain=None, range=Optional[Union[dict[Union[str, KarakterhistorieId], Union[dict, Karakterhistorie]], list[Union[dict, Karakterhistorie]]]])

slots.utdanningContainer__sensor = Slot(uri=UTD.sensor, name="utdanningContainer__sensor", curie=UTD.curie('sensor'),
                   model_uri=UTD.utdanningContainer__sensor, domain=None, range=Optional[Union[dict[Union[str, SensorId], Union[dict, Sensor]], list[Union[dict, Sensor]]]])

slots.utdanningContainer__sluttfagvurdering = Slot(uri=UTD.sluttfagvurdering, name="utdanningContainer__sluttfagvurdering", curie=UTD.curie('sluttfagvurdering'),
                   model_uri=UTD.utdanningContainer__sluttfagvurdering, domain=None, range=Optional[Union[dict[Union[str, SluttfagvurderingId], Union[dict, Sluttfagvurdering]], list[Union[dict, Sluttfagvurdering]]]])

slots.utdanningContainer__sluttordensvurdering = Slot(uri=UTD.sluttordensvurdering, name="utdanningContainer__sluttordensvurdering", curie=UTD.curie('sluttordensvurdering'),
                   model_uri=UTD.utdanningContainer__sluttordensvurdering, domain=None, range=Optional[Union[dict[Union[str, SluttordensvurderingId], Union[dict, Sluttordensvurdering]], list[Union[dict, Sluttordensvurdering]]]])

slots.utdanningContainer__underveisfagvurdering = Slot(uri=UTD.underveisfagvurdering, name="utdanningContainer__underveisfagvurdering", curie=UTD.curie('underveisfagvurdering'),
                   model_uri=UTD.utdanningContainer__underveisfagvurdering, domain=None, range=Optional[Union[dict[Union[str, UnderveisfagvurderingId], Union[dict, Underveisfagvurdering]], list[Union[dict, Underveisfagvurdering]]]])

slots.utdanningContainer__underveisordensvurdering = Slot(uri=UTD.underveisordensvurdering, name="utdanningContainer__underveisordensvurdering", curie=UTD.curie('underveisordensvurdering'),
                   model_uri=UTD.utdanningContainer__underveisordensvurdering, domain=None, range=Optional[Union[dict[Union[str, UnderveisordensvurderingId], Union[dict, Underveisordensvurdering]], list[Union[dict, Underveisordensvurdering]]]])

slots.utdanningContainer__avlagteprover = Slot(uri=UTD.avlagteprover, name="utdanningContainer__avlagteprover", curie=UTD.curie('avlagteprover'),
                   model_uri=UTD.utdanningContainer__avlagteprover, domain=None, range=Optional[Union[dict[Union[str, AvlagtProveId], Union[dict, AvlagtProve]], list[Union[dict, AvlagtProve]]]])

slots.utdanningContainer__laerlingar = Slot(uri=UTD.laerlingar, name="utdanningContainer__laerlingar", curie=UTD.curie('laerlingar'),
                   model_uri=UTD.utdanningContainer__laerlingar, domain=None, range=Optional[Union[dict[Union[str, LaerlingId], Union[dict, Laerling]], list[Union[dict, Laerling]]]])

slots.utdanningContainer__otUngdom = Slot(uri=UTD.otUngdom, name="utdanningContainer__otUngdom", curie=UTD.curie('otUngdom'),
                   model_uri=UTD.utdanningContainer__otUngdom, domain=None, range=Optional[Union[dict[Union[str, OtUngdomId], Union[dict, OtUngdom]], list[Union[dict, OtUngdom]]]])

slots.utdanningContainer__avbruddsaarsaker = Slot(uri=UTD.avbruddsaarsaker, name="utdanningContainer__avbruddsaarsaker", curie=UTD.curie('avbruddsaarsaker'),
                   model_uri=UTD.utdanningContainer__avbruddsaarsaker, domain=None, range=Optional[Union[dict[Union[str, AvbruddsaarsakId], Union[dict, Avbruddsaarsak]], list[Union[dict, Avbruddsaarsak]]]])

slots.utdanningContainer__betalingsstatus = Slot(uri=UTD.betalingsstatus, name="utdanningContainer__betalingsstatus", curie=UTD.curie('betalingsstatus'),
                   model_uri=UTD.utdanningContainer__betalingsstatus, domain=None, range=Optional[Union[dict[Union[str, BetalingsstatusId], Union[dict, Betalingsstatus]], list[Union[dict, Betalingsstatus]]]])

slots.utdanningContainer__bevistypar = Slot(uri=UTD.bevistypar, name="utdanningContainer__bevistypar", curie=UTD.curie('bevistypar'),
                   model_uri=UTD.utdanningContainer__bevistypar, domain=None, range=Optional[Union[dict[Union[str, BevistypeId], Union[dict, Bevistype]], list[Union[dict, Bevistype]]]])

slots.utdanningContainer__brevtypar = Slot(uri=UTD.brevtypar, name="utdanningContainer__brevtypar", curie=UTD.curie('brevtypar'),
                   model_uri=UTD.utdanningContainer__brevtypar, domain=None, range=Optional[Union[dict[Union[str, BrevtypeId], Union[dict, Brevtype]], list[Union[dict, Brevtype]]]])

slots.utdanningContainer__eksamensformer = Slot(uri=UTD.eksamensformer, name="utdanningContainer__eksamensformer", curie=UTD.curie('eksamensformer'),
                   model_uri=UTD.utdanningContainer__eksamensformer, domain=None, range=Optional[Union[dict[Union[str, EksamensformId], Union[dict, Eksamensform]], list[Union[dict, Eksamensform]]]])

slots.utdanningContainer__elevkategoriar = Slot(uri=UTD.elevkategoriar, name="utdanningContainer__elevkategoriar", curie=UTD.curie('elevkategoriar'),
                   model_uri=UTD.utdanningContainer__elevkategoriar, domain=None, range=Optional[Union[dict[Union[str, ElevkategoriId], Union[dict, Elevkategori]], list[Union[dict, Elevkategori]]]])

slots.utdanningContainer__fagmerknader = Slot(uri=UTD.fagmerknader, name="utdanningContainer__fagmerknader", curie=UTD.curie('fagmerknader'),
                   model_uri=UTD.utdanningContainer__fagmerknader, domain=None, range=Optional[Union[dict[Union[str, FagmerknadId], Union[dict, Fagmerknad]], list[Union[dict, Fagmerknad]]]])

slots.utdanningContainer__fagstatus = Slot(uri=UTD.fagstatus, name="utdanningContainer__fagstatus", curie=UTD.curie('fagstatus'),
                   model_uri=UTD.utdanningContainer__fagstatus, domain=None, range=Optional[Union[dict[Union[str, FagstatusId], Union[dict, Fagstatus]], list[Union[dict, Fagstatus]]]])

slots.utdanningContainer__fravartypar = Slot(uri=UTD.fravartypar, name="utdanningContainer__fravartypar", curie=UTD.curie('fravartypar'),
                   model_uri=UTD.utdanningContainer__fravartypar, domain=None, range=Optional[Union[dict[Union[str, FravartypeId], Union[dict, Fravartype]], list[Union[dict, Fravartype]]]])

slots.utdanningContainer__fullfortkoder = Slot(uri=UTD.fullfortkoder, name="utdanningContainer__fullfortkoder", curie=UTD.curie('fullfortkoder'),
                   model_uri=UTD.utdanningContainer__fullfortkoder, domain=None, range=Optional[Union[dict[Union[str, FullfortkodeId], Union[dict, Fullfortkode]], list[Union[dict, Fullfortkode]]]])

slots.utdanningContainer__karakterskalaer = Slot(uri=UTD.karakterskalaer, name="utdanningContainer__karakterskalaer", curie=UTD.curie('karakterskalaer'),
                   model_uri=UTD.utdanningContainer__karakterskalaer, domain=None, range=Optional[Union[dict[Union[str, KarakterskalaId], Union[dict, Karakterskala]], list[Union[dict, Karakterskala]]]])

slots.utdanningContainer__karakterstatus = Slot(uri=UTD.karakterstatus, name="utdanningContainer__karakterstatus", curie=UTD.curie('karakterstatus'),
                   model_uri=UTD.utdanningContainer__karakterstatus, domain=None, range=Optional[Union[dict[Union[str, KarakterstatusId], Union[dict, Karakterstatus]], list[Union[dict, Karakterstatus]]]])

slots.utdanningContainer__karakterverdiar = Slot(uri=UTD.karakterverdiar, name="utdanningContainer__karakterverdiar", curie=UTD.curie('karakterverdiar'),
                   model_uri=UTD.utdanningContainer__karakterverdiar, domain=None, range=Optional[Union[dict[Union[str, KarakterverdiId], Union[dict, Karakterverdi]], list[Union[dict, Karakterverdi]]]])

slots.utdanningContainer__otEnheter = Slot(uri=UTD.otEnheter, name="utdanningContainer__otEnheter", curie=UTD.curie('otEnheter'),
                   model_uri=UTD.utdanningContainer__otEnheter, domain=None, range=Optional[Union[dict[Union[str, OtEnhetId], Union[dict, OtEnhet]], list[Union[dict, OtEnhet]]]])

slots.utdanningContainer__otStatus = Slot(uri=UTD.otStatus, name="utdanningContainer__otStatus", curie=UTD.curie('otStatus'),
                   model_uri=UTD.utdanningContainer__otStatus, domain=None, range=Optional[Union[dict[Union[str, OtStatusId], Union[dict, OtStatus]], list[Union[dict, OtStatus]]]])

slots.utdanningContainer__provestatuser = Slot(uri=UTD.provestatuser, name="utdanningContainer__provestatuser", curie=UTD.curie('provestatuser'),
                   model_uri=UTD.utdanningContainer__provestatuser, domain=None, range=Optional[Union[dict[Union[str, ProvestatusId], Union[dict, Provestatus]], list[Union[dict, Provestatus]]]])

slots.utdanningContainer__skoleaar = Slot(uri=UTD.skoleaar, name="utdanningContainer__skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.utdanningContainer__skoleaar, domain=None, range=Optional[Union[dict[Union[str, SkoleaarId], Union[dict, Skoleaar]], list[Union[dict, Skoleaar]]]])

slots.utdanningContainer__skoleeijartypar = Slot(uri=UTD.skoleeijartypar, name="utdanningContainer__skoleeijartypar", curie=UTD.curie('skoleeijartypar'),
                   model_uri=UTD.utdanningContainer__skoleeijartypar, domain=None, range=Optional[Union[dict[Union[str, SkoleeiertypeId], Union[dict, Skoleeiertype]], list[Union[dict, Skoleeiertype]]]])

slots.utdanningContainer__terminar = Slot(uri=UTD.terminar, name="utdanningContainer__terminar", curie=UTD.curie('terminar'),
                   model_uri=UTD.utdanningContainer__terminar, domain=None, range=Optional[Union[dict[Union[str, TerminId], Union[dict, Termin]], list[Union[dict, Termin]]]])

slots.utdanningContainer__tilrettelegging = Slot(uri=UTD.tilrettelegging, name="utdanningContainer__tilrettelegging", curie=UTD.curie('tilrettelegging'),
                   model_uri=UTD.utdanningContainer__tilrettelegging, domain=None, range=Optional[Union[dict[Union[str, TilretteleggingId], Union[dict, Tilrettelegging]], list[Union[dict, Tilrettelegging]]]])

slots.utdanningContainer__varseltypar = Slot(uri=UTD.varseltypar, name="utdanningContainer__varseltypar", curie=UTD.curie('varseltypar'),
                   model_uri=UTD.utdanningContainer__varseltypar, domain=None, range=Optional[Union[dict[Union[str, VarseltypeId], Union[dict, Varseltype]], list[Union[dict, Varseltype]]]])

slots.utdanningContainer__vitnemalsmerknad = Slot(uri=UTD.vitnemalsmerknad, name="utdanningContainer__vitnemalsmerknad", curie=UTD.curie('vitnemalsmerknad'),
                   model_uri=UTD.utdanningContainer__vitnemalsmerknad, domain=None, range=Optional[Union[dict[Union[str, VitnemalsmerknadId], Union[dict, Vitnemalsmerknad]], list[Union[dict, Vitnemalsmerknad]]]])

slots.gruppe__navn = Slot(uri=UTD.navn, name="gruppe__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.gruppe__navn, domain=None, range=str)

slots.gruppe__beskrivelse = Slot(uri=UTD.beskrivelse, name="gruppe__beskrivelse", curie=UTD.curie('beskrivelse'),
                   model_uri=UTD.gruppe__beskrivelse, domain=None, range=Optional[str])

slots.gruppemedlemskap__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="gruppemedlemskap__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.gruppemedlemskap__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.utdanningsforhold__beskrivelse = Slot(uri=UTD.beskrivelse, name="utdanningsforhold__beskrivelse", curie=UTD.curie('beskrivelse'),
                   model_uri=UTD.utdanningsforhold__beskrivelse, domain=None, range=Optional[str])

slots.elev__elevnummer = Slot(uri=UTD.elevnummer, name="elev__elevnummer", curie=UTD.curie('elevnummer'),
                   model_uri=UTD.elev__elevnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.elev__person = Slot(uri=UTD.person, name="elev__person", curie=UTD.curie('person'),
                   model_uri=UTD.elev__person, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.elevforhold__beskrivelse = Slot(uri=UTD.beskrivelse, name="elevforhold__beskrivelse", curie=UTD.curie('beskrivelse'),
                   model_uri=UTD.elevforhold__beskrivelse, domain=None, range=str)

slots.elevforhold__avbruddsdato = Slot(uri=UTD.avbruddsdato, name="elevforhold__avbruddsdato", curie=UTD.curie('avbruddsdato'),
                   model_uri=UTD.elevforhold__avbruddsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.elevforhold__tosprakligFagopplaering = Slot(uri=UTD.tosprakligFagopplaering, name="elevforhold__tosprakligFagopplaering", curie=UTD.curie('tosprakligFagopplaering'),
                   model_uri=UTD.elevforhold__tosprakligFagopplaering, domain=None, range=Optional[Union[bool, Bool]])

slots.elevforhold__elev = Slot(uri=UTD.elev, name="elevforhold__elev", curie=UTD.curie('elev'),
                   model_uri=UTD.elevforhold__elev, domain=None, range=Union[str, ElevId])

slots.elevforhold__skole = Slot(uri=UTD.skole, name="elevforhold__skole", curie=UTD.curie('skole'),
                   model_uri=UTD.elevforhold__skole, domain=None, range=Union[str, SkoleId])

slots.elevforhold__kategori = Slot(uri=UTD.kategori, name="elevforhold__kategori", curie=UTD.curie('kategori'),
                   model_uri=UTD.elevforhold__kategori, domain=None, range=Optional[Union[str, ElevkategoriId]])

slots.elevforhold__avbruddsarsak = Slot(uri=UTD.avbruddsarsak, name="elevforhold__avbruddsarsak", curie=UTD.curie('avbruddsarsak'),
                   model_uri=UTD.elevforhold__avbruddsarsak, domain=None, range=Optional[Union[str, AvbruddsaarsakId]])

slots.elevforhold__skoleaar = Slot(uri=UTD.skoleaar, name="elevforhold__skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.elevforhold__skoleaar, domain=None, range=Optional[Union[str, SkoleaarId]])

slots.elevforhold__programomrademedlemskap = Slot(uri=UTD.programomrademedlemskap, name="elevforhold__programomrademedlemskap", curie=UTD.curie('programomrademedlemskap'),
                   model_uri=UTD.elevforhold__programomrademedlemskap, domain=None, range=Optional[Union[Union[str, ProgramomrademedlemskapId], list[Union[str, ProgramomrademedlemskapId]]]])

slots.elevforhold__klassemedlemskap = Slot(uri=UTD.klassemedlemskap, name="elevforhold__klassemedlemskap", curie=UTD.curie('klassemedlemskap'),
                   model_uri=UTD.elevforhold__klassemedlemskap, domain=None, range=Optional[Union[Union[str, KlassemedlemskapId], list[Union[str, KlassemedlemskapId]]]])

slots.elevforhold__faggruppemedlemskap = Slot(uri=UTD.faggruppemedlemskap, name="elevforhold__faggruppemedlemskap", curie=UTD.curie('faggruppemedlemskap'),
                   model_uri=UTD.elevforhold__faggruppemedlemskap, domain=None, range=Optional[Union[Union[str, FaggruppemedlemskapId], list[Union[str, FaggruppemedlemskapId]]]])

slots.elevforhold__undervisningsgruppemedlemskap = Slot(uri=UTD.undervisningsgruppemedlemskap, name="elevforhold__undervisningsgruppemedlemskap", curie=UTD.curie('undervisningsgruppemedlemskap'),
                   model_uri=UTD.elevforhold__undervisningsgruppemedlemskap, domain=None, range=Optional[Union[Union[str, UndervisningsgruppemedlemskapId], list[Union[str, UndervisningsgruppemedlemskapId]]]])

slots.elevforhold__kontaktlaerergruppemedlemskap = Slot(uri=UTD.kontaktlaerergruppemedlemskap, name="elevforhold__kontaktlaerergruppemedlemskap", curie=UTD.curie('kontaktlaerergruppemedlemskap'),
                   model_uri=UTD.elevforhold__kontaktlaerergruppemedlemskap, domain=None, range=Optional[Union[Union[str, KontaktlaerergruppemedlemskapId], list[Union[str, KontaktlaerergruppemedlemskapId]]]])

slots.elevforhold__persongruppemedlemskap = Slot(uri=UTD.persongruppemedlemskap, name="elevforhold__persongruppemedlemskap", curie=UTD.curie('persongruppemedlemskap'),
                   model_uri=UTD.elevforhold__persongruppemedlemskap, domain=None, range=Optional[Union[Union[str, PersongruppemedlemskapId], list[Union[str, PersongruppemedlemskapId]]]])

slots.elevforhold__eksamensgruppemedlemskap = Slot(uri=UTD.eksamensgruppemedlemskap, name="elevforhold__eksamensgruppemedlemskap", curie=UTD.curie('eksamensgruppemedlemskap'),
                   model_uri=UTD.elevforhold__eksamensgruppemedlemskap, domain=None, range=Optional[Union[Union[str, EksamensgruppemedlemskapId], list[Union[str, EksamensgruppemedlemskapId]]]])

slots.elevforhold__fraversregistreringer = Slot(uri=UTD.fraversregistreringer, name="elevforhold__fraversregistreringer", curie=UTD.curie('fraversregistreringer'),
                   model_uri=UTD.elevforhold__fraversregistreringer, domain=None, range=Optional[Union[Union[str, ElevfravarId], list[Union[str, ElevfravarId]]]])

slots.elevforhold__elevfravar = Slot(uri=UTD.elevfravar, name="elevforhold__elevfravar", curie=UTD.curie('elevfravar'),
                   model_uri=UTD.elevforhold__elevfravar, domain=None, range=Optional[Union[str, FravarsoversiktId]])

slots.elevforhold__tilrettelegging = Slot(uri=UTD.tilrettelegging, name="elevforhold__tilrettelegging", curie=UTD.curie('tilrettelegging'),
                   model_uri=UTD.elevforhold__tilrettelegging, domain=None, range=Optional[Union[Union[str, ElevtilretteleggingId], list[Union[str, ElevtilretteleggingId]]]])

slots.elevforhold__elevvurdering = Slot(uri=UTD.elevvurdering, name="elevforhold__elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.elevforhold__elevvurdering, domain=None, range=Optional[Union[str, ElevvurderingId]])

slots.elevtilrettelegging__elev = Slot(uri=UTD.elev, name="elevtilrettelegging__elev", curie=UTD.curie('elev'),
                   model_uri=UTD.elevtilrettelegging__elev, domain=None, range=Optional[Union[str, ElevforholdId]])

slots.elevtilrettelegging__tilrettelegging = Slot(uri=UTD.tilrettelegging, name="elevtilrettelegging__tilrettelegging", curie=UTD.curie('tilrettelegging'),
                   model_uri=UTD.elevtilrettelegging__tilrettelegging, domain=None, range=Optional[Union[str, TilretteleggingId]])

slots.elevtilrettelegging__eksamensform = Slot(uri=UTD.eksamensform, name="elevtilrettelegging__eksamensform", curie=UTD.curie('eksamensform'),
                   model_uri=UTD.elevtilrettelegging__eksamensform, domain=None, range=Optional[Union[str, EksamensformId]])

slots.klasse__skoleaar = Slot(uri=UTD.skoleaar, name="klasse__skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.klasse__skoleaar, domain=None, range=Optional[Union[str, SkoleaarId]])

slots.klasse__termin = Slot(uri=UTD.termin, name="klasse__termin", curie=UTD.curie('termin'),
                   model_uri=UTD.klasse__termin, domain=None, range=Optional[Union[Union[str, TerminId], list[Union[str, TerminId]]]])

slots.klasse__trinn = Slot(uri=UTD.trinn, name="klasse__trinn", curie=UTD.curie('trinn'),
                   model_uri=UTD.klasse__trinn, domain=None, range=Optional[Union[Union[str, ArstrinnId], list[Union[str, ArstrinnId]]]])

slots.klasse__skole = Slot(uri=UTD.skole, name="klasse__skole", curie=UTD.curie('skole'),
                   model_uri=UTD.klasse__skole, domain=None, range=Optional[Union[str, SkoleId]])

slots.klasse__undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="klasse__undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.klasse__undervisningsforhold, domain=None, range=Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]])

slots.klasse__klassemedlemskap = Slot(uri=UTD.klassemedlemskap, name="klasse__klassemedlemskap", curie=UTD.curie('klassemedlemskap'),
                   model_uri=UTD.klasse__klassemedlemskap, domain=None, range=Optional[Union[Union[str, KlassemedlemskapId], list[Union[str, KlassemedlemskapId]]]])

slots.klasse__kontaktlaerergruppe = Slot(uri=UTD.kontaktlaerergruppe, name="klasse__kontaktlaerergruppe", curie=UTD.curie('kontaktlaerergruppe'),
                   model_uri=UTD.klasse__kontaktlaerergruppe, domain=None, range=Optional[Union[Union[str, KontaktlaerergruppeId], list[Union[str, KontaktlaerergruppeId]]]])

slots.klassemedlemskap__elevforhold = Slot(uri=UTD.elevforhold, name="klassemedlemskap__elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.klassemedlemskap__elevforhold, domain=None, range=Optional[Union[str, ElevforholdId]])

slots.klassemedlemskap__klasse = Slot(uri=UTD.klasse, name="klassemedlemskap__klasse", curie=UTD.curie('klasse'),
                   model_uri=UTD.klassemedlemskap__klasse, domain=None, range=Optional[Union[str, KlasseId]])

slots.kontaktlaerergruppe__klasse = Slot(uri=UTD.klasse, name="kontaktlaerergruppe__klasse", curie=UTD.curie('klasse'),
                   model_uri=UTD.kontaktlaerergruppe__klasse, domain=None, range=Union[Union[str, KlasseId], list[Union[str, KlasseId]]])

slots.kontaktlaerergruppe__termin = Slot(uri=UTD.termin, name="kontaktlaerergruppe__termin", curie=UTD.curie('termin'),
                   model_uri=UTD.kontaktlaerergruppe__termin, domain=None, range=Optional[Union[Union[str, TerminId], list[Union[str, TerminId]]]])

slots.kontaktlaerergruppe__skole = Slot(uri=UTD.skole, name="kontaktlaerergruppe__skole", curie=UTD.curie('skole'),
                   model_uri=UTD.kontaktlaerergruppe__skole, domain=None, range=Optional[Union[str, SkoleId]])

slots.kontaktlaerergruppe__skoleaar = Slot(uri=UTD.skoleaar, name="kontaktlaerergruppe__skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.kontaktlaerergruppe__skoleaar, domain=None, range=Optional[Union[str, SkoleaarId]])

slots.kontaktlaerergruppe__undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="kontaktlaerergruppe__undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.kontaktlaerergruppe__undervisningsforhold, domain=None, range=Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]])

slots.kontaktlaerergruppe__gruppemedlemskap = Slot(uri=UTD.gruppemedlemskap, name="kontaktlaerergruppe__gruppemedlemskap", curie=UTD.curie('gruppemedlemskap'),
                   model_uri=UTD.kontaktlaerergruppe__gruppemedlemskap, domain=None, range=Optional[Union[Union[str, KontaktlaerergruppemedlemskapId], list[Union[str, KontaktlaerergruppemedlemskapId]]]])

slots.kontaktlaerergruppemedlemskap__elevforhold = Slot(uri=UTD.elevforhold, name="kontaktlaerergruppemedlemskap__elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.kontaktlaerergruppemedlemskap__elevforhold, domain=None, range=Optional[Union[str, ElevforholdId]])

slots.kontaktlaerergruppemedlemskap__kontaktlaerergruppe = Slot(uri=UTD.kontaktlaerergruppe, name="kontaktlaerergruppemedlemskap__kontaktlaerergruppe", curie=UTD.curie('kontaktlaerergruppe'),
                   model_uri=UTD.kontaktlaerergruppemedlemskap__kontaktlaerergruppe, domain=None, range=Optional[Union[str, KontaktlaerergruppeId]])

slots.persongruppe__elev = Slot(uri=UTD.elev, name="persongruppe__elev", curie=UTD.curie('elev'),
                   model_uri=UTD.persongruppe__elev, domain=None, range=Optional[Union[Union[str, ElevforholdId], list[Union[str, ElevforholdId]]]])

slots.persongruppe__persongruppemedlemskap = Slot(uri=UTD.persongruppemedlemskap, name="persongruppe__persongruppemedlemskap", curie=UTD.curie('persongruppemedlemskap'),
                   model_uri=UTD.persongruppe__persongruppemedlemskap, domain=None, range=Optional[Union[Union[str, PersongruppemedlemskapId], list[Union[str, PersongruppemedlemskapId]]]])

slots.persongruppe__termin = Slot(uri=UTD.termin, name="persongruppe__termin", curie=UTD.curie('termin'),
                   model_uri=UTD.persongruppe__termin, domain=None, range=Optional[Union[Union[str, TerminId], list[Union[str, TerminId]]]])

slots.persongruppe__undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="persongruppe__undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.persongruppe__undervisningsforhold, domain=None, range=Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]])

slots.persongruppe__skole = Slot(uri=UTD.skole, name="persongruppe__skole", curie=UTD.curie('skole'),
                   model_uri=UTD.persongruppe__skole, domain=None, range=Optional[Union[str, SkoleId]])

slots.persongruppe__skoleressurs = Slot(uri=UTD.skoleressurs, name="persongruppe__skoleressurs", curie=UTD.curie('skoleressurs'),
                   model_uri=UTD.persongruppe__skoleressurs, domain=None, range=Optional[Union[Union[str, SkoleressursId], list[Union[str, SkoleressursId]]]])

slots.persongruppe__skoleaar = Slot(uri=UTD.skoleaar, name="persongruppe__skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.persongruppe__skoleaar, domain=None, range=Optional[Union[str, SkoleaarId]])

slots.persongruppemedlemskap__elevforhold = Slot(uri=UTD.elevforhold, name="persongruppemedlemskap__elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.persongruppemedlemskap__elevforhold, domain=None, range=Optional[Union[str, ElevforholdId]])

slots.persongruppemedlemskap__persongruppe = Slot(uri=UTD.persongruppe, name="persongruppemedlemskap__persongruppe", curie=UTD.curie('persongruppe'),
                   model_uri=UTD.persongruppemedlemskap__persongruppe, domain=None, range=Optional[Union[str, PersongruppeId]])

slots.skole__navn = Slot(uri=UTD.navn, name="skole__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.skole__navn, domain=None, range=str)

slots.skole__domenenavn = Slot(uri=UTD.domenenavn, name="skole__domenenavn", curie=UTD.curie('domenenavn'),
                   model_uri=UTD.skole__domenenavn, domain=None, range=Optional[str])

slots.skole__juridiskNavn = Slot(uri=UTD.juridiskNavn, name="skole__juridiskNavn", curie=UTD.curie('juridiskNavn'),
                   model_uri=UTD.skole__juridiskNavn, domain=None, range=Optional[str])

slots.skole__organisasjonsnavn = Slot(uri=UTD.organisasjonsnavn, name="skole__organisasjonsnavn", curie=UTD.curie('organisasjonsnavn'),
                   model_uri=UTD.skole__organisasjonsnavn, domain=None, range=Optional[str])

slots.skole__skolenummer = Slot(uri=UTD.skolenummer, name="skole__skolenummer", curie=UTD.curie('skolenummer'),
                   model_uri=UTD.skole__skolenummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.skole__organisasjonsnummer = Slot(uri=UTD.organisasjonsnummer, name="skole__organisasjonsnummer", curie=UTD.curie('organisasjonsnummer'),
                   model_uri=UTD.skole__organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.skole__forretningsadresse = Slot(uri=UTD.forretningsadresse, name="skole__forretningsadresse", curie=UTD.curie('forretningsadresse'),
                   model_uri=UTD.skole__forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.skole__postadresse = Slot(uri=UTD.postadresse, name="skole__postadresse", curie=UTD.curie('postadresse'),
                   model_uri=UTD.skole__postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.skole__organisasjon = Slot(uri=UTD.organisasjon, name="skole__organisasjon", curie=UTD.curie('organisasjon'),
                   model_uri=UTD.skole__organisasjon, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.skole__klasse = Slot(uri=UTD.klasse, name="skole__klasse", curie=UTD.curie('klasse'),
                   model_uri=UTD.skole__klasse, domain=None, range=Optional[Union[Union[str, KlasseId], list[Union[str, KlasseId]]]])

slots.skole__kontaktlaerergruppe = Slot(uri=UTD.kontaktlaerergruppe, name="skole__kontaktlaerergruppe", curie=UTD.curie('kontaktlaerergruppe'),
                   model_uri=UTD.skole__kontaktlaerergruppe, domain=None, range=Optional[Union[Union[str, KontaktlaerergruppeId], list[Union[str, KontaktlaerergruppeId]]]])

slots.skole__skoleressurs = Slot(uri=UTD.skoleressurs, name="skole__skoleressurs", curie=UTD.curie('skoleressurs'),
                   model_uri=UTD.skole__skoleressurs, domain=None, range=Optional[Union[Union[str, SkoleressursId], list[Union[str, SkoleressursId]]]])

slots.skole__fag = Slot(uri=UTD.fag, name="skole__fag", curie=UTD.curie('fag'),
                   model_uri=UTD.skole__fag, domain=None, range=Optional[Union[Union[str, FagId], list[Union[str, FagId]]]])

slots.skole__faggruppe = Slot(uri=UTD.faggruppe, name="skole__faggruppe", curie=UTD.curie('faggruppe'),
                   model_uri=UTD.skole__faggruppe, domain=None, range=Optional[Union[Union[str, FaggruppeId], list[Union[str, FaggruppeId]]]])

slots.skole__skoleeierType = Slot(uri=UTD.skoleeierType, name="skole__skoleeierType", curie=UTD.curie('skoleeierType'),
                   model_uri=UTD.skole__skoleeierType, domain=None, range=Optional[Union[str, SkoleeiertypeId]])

slots.skole__vigoreferanse = Slot(uri=UTD.vigoreferanse, name="skole__vigoreferanse", curie=UTD.curie('vigoreferanse'),
                   model_uri=UTD.skole__vigoreferanse, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.skole__eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="skole__eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.skole__eksamensgruppe, domain=None, range=Optional[Union[Union[str, EksamensgruppeId], list[Union[str, EksamensgruppeId]]]])

slots.skole__utdanningsprogram = Slot(uri=UTD.utdanningsprogram, name="skole__utdanningsprogram", curie=UTD.curie('utdanningsprogram'),
                   model_uri=UTD.skole__utdanningsprogram, domain=None, range=Optional[Union[Union[str, UtdanningsprogramId], list[Union[str, UtdanningsprogramId]]]])

slots.skoleressurs__feidenavn = Slot(uri=UTD.feidenavn, name="skoleressurs__feidenavn", curie=UTD.curie('feidenavn'),
                   model_uri=UTD.skoleressurs__feidenavn, domain=None, range=Optional[Union[dict, Identifikator]])

slots.skoleressurs__personalressurs = Slot(uri=UTD.personalressurs, name="skoleressurs__personalressurs", curie=UTD.curie('personalressurs'),
                   model_uri=UTD.skoleressurs__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.skoleressurs__person = Slot(uri=UTD.person, name="skoleressurs__person", curie=UTD.curie('person'),
                   model_uri=UTD.skoleressurs__person, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.skoleressurs__skole = Slot(uri=UTD.skole, name="skoleressurs__skole", curie=UTD.curie('skole'),
                   model_uri=UTD.skoleressurs__skole, domain=None, range=Optional[Union[Union[str, SkoleId], list[Union[str, SkoleId]]]])

slots.skoleressurs__sensor = Slot(uri=UTD.sensor, name="skoleressurs__sensor", curie=UTD.curie('sensor'),
                   model_uri=UTD.skoleressurs__sensor, domain=None, range=Optional[Union[Union[str, SensorId], list[Union[str, SensorId]]]])

slots.varsel__fravarsprosent = Slot(uri=UTD.fravarsprosent, name="varsel__fravarsprosent", curie=UTD.curie('fravarsprosent'),
                   model_uri=UTD.varsel__fravarsprosent, domain=None, range=Optional[int])

slots.varsel__sendt = Slot(uri=UTD.sendt, name="varsel__sendt", curie=UTD.curie('sendt'),
                   model_uri=UTD.varsel__sendt, domain=None, range=Optional[Union[str, XSDDate]])

slots.varsel__tekst = Slot(uri=UTD.tekst, name="varsel__tekst", curie=UTD.curie('tekst'),
                   model_uri=UTD.varsel__tekst, domain=None, range=Optional[str])

slots.varsel__utsteder = Slot(uri=UTD.utsteder, name="varsel__utsteder", curie=UTD.curie('utsteder'),
                   model_uri=UTD.varsel__utsteder, domain=None, range=Optional[Union[str, SkoleressursId]])

slots.varsel__karakteransvarlig = Slot(uri=UTD.karakteransvarlig, name="varsel__karakteransvarlig", curie=UTD.curie('karakteransvarlig'),
                   model_uri=UTD.varsel__karakteransvarlig, domain=None, range=Optional[Union[str, SkoleressursId]])

slots.varsel__type = Slot(uri=UTD.type, name="varsel__type", curie=UTD.curie('type'),
                   model_uri=UTD.varsel__type, domain=None, range=Optional[Union[str, VarseltypeId]])

slots.varsel__faggruppemedlemskap = Slot(uri=UTD.faggruppemedlemskap, name="varsel__faggruppemedlemskap", curie=UTD.curie('faggruppemedlemskap'),
                   model_uri=UTD.varsel__faggruppemedlemskap, domain=None, range=Optional[Union[str, FaggruppemedlemskapId]])

slots.arstrinn__klasse = Slot(uri=UTD.klasse, name="arstrinn__klasse", curie=UTD.curie('klasse'),
                   model_uri=UTD.arstrinn__klasse, domain=None, range=Optional[Union[Union[str, KlasseId], list[Union[str, KlasseId]]]])

slots.arstrinn__vigoreferanse = Slot(uri=UTD.vigoreferanse, name="arstrinn__vigoreferanse", curie=UTD.curie('vigoreferanse'),
                   model_uri=UTD.arstrinn__vigoreferanse, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.arstrinn__grepreferanse = Slot(uri=UTD.grepreferanse, name="arstrinn__grepreferanse", curie=UTD.curie('grepreferanse'),
                   model_uri=UTD.arstrinn__grepreferanse, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.arstrinn__programomrade = Slot(uri=UTD.programomrade, name="arstrinn__programomrade", curie=UTD.curie('programomrade'),
                   model_uri=UTD.arstrinn__programomrade, domain=None, range=Optional[Union[Union[str, ProgramomradeId], list[Union[str, ProgramomradeId]]]])

slots.programomrade__trinn = Slot(uri=UTD.trinn, name="programomrade__trinn", curie=UTD.curie('trinn'),
                   model_uri=UTD.programomrade__trinn, domain=None, range=Optional[Union[Union[str, ArstrinnId], list[Union[str, ArstrinnId]]]])

slots.programomrade__grepreferanse = Slot(uri=UTD.grepreferanse, name="programomrade__grepreferanse", curie=UTD.curie('grepreferanse'),
                   model_uri=UTD.programomrade__grepreferanse, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.programomrade__vigoreferanse = Slot(uri=UTD.vigoreferanse, name="programomrade__vigoreferanse", curie=UTD.curie('vigoreferanse'),
                   model_uri=UTD.programomrade__vigoreferanse, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.programomrade__gruppemedlemskap = Slot(uri=UTD.gruppemedlemskap, name="programomrade__gruppemedlemskap", curie=UTD.curie('gruppemedlemskap'),
                   model_uri=UTD.programomrade__gruppemedlemskap, domain=None, range=Optional[Union[Union[str, ProgramomrademedlemskapId], list[Union[str, ProgramomrademedlemskapId]]]])

slots.programomrademedlemskap__elevforhold = Slot(uri=UTD.elevforhold, name="programomrademedlemskap__elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.programomrademedlemskap__elevforhold, domain=None, range=Optional[Union[str, ElevforholdId]])

slots.programomrademedlemskap__programomrade = Slot(uri=UTD.programomrade, name="programomrademedlemskap__programomrade", curie=UTD.curie('programomrade'),
                   model_uri=UTD.programomrademedlemskap__programomrade, domain=None, range=Optional[Union[str, ProgramomradeId]])

slots.utdanningsprogram__programomrade = Slot(uri=UTD.programomrade, name="utdanningsprogram__programomrade", curie=UTD.curie('programomrade'),
                   model_uri=UTD.utdanningsprogram__programomrade, domain=None, range=Optional[Union[Union[str, ProgramomradeId], list[Union[str, ProgramomradeId]]]])

slots.utdanningsprogram__skole = Slot(uri=UTD.skole, name="utdanningsprogram__skole", curie=UTD.curie('skole'),
                   model_uri=UTD.utdanningsprogram__skole, domain=None, range=Optional[Union[Union[str, SkoleId], list[Union[str, SkoleId]]]])

slots.utdanningsprogram__grepreferanse = Slot(uri=UTD.grepreferanse, name="utdanningsprogram__grepreferanse", curie=UTD.curie('grepreferanse'),
                   model_uri=UTD.utdanningsprogram__grepreferanse, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.utdanningsprogram__vigoreferanse = Slot(uri=UTD.vigoreferanse, name="utdanningsprogram__vigoreferanse", curie=UTD.curie('vigoreferanse'),
                   model_uri=UTD.utdanningsprogram__vigoreferanse, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.eksamen__navn = Slot(uri=UTD.navn, name="eksamen__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.eksamen__navn, domain=None, range=str)

slots.eksamen__beskrivelse = Slot(uri=UTD.beskrivelse, name="eksamen__beskrivelse", curie=UTD.curie('beskrivelse'),
                   model_uri=UTD.eksamen__beskrivelse, domain=None, range=Optional[str])

slots.eksamen__oppmoetetidspunkt = Slot(uri=UTD.oppmoetetidspunkt, name="eksamen__oppmoetetidspunkt", curie=UTD.curie('oppmoetetidspunkt'),
                   model_uri=UTD.eksamen__oppmoetetidspunkt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.eksamen__tidsrom = Slot(uri=UTD.tidsrom, name="eksamen__tidsrom", curie=UTD.curie('tidsrom'),
                   model_uri=UTD.eksamen__tidsrom, domain=None, range=Optional[Union[dict, Periode]])

slots.eksamen__rom = Slot(uri=UTD.rom, name="eksamen__rom", curie=UTD.curie('rom'),
                   model_uri=UTD.eksamen__rom, domain=None, range=Optional[Union[Union[str, RomId], list[Union[str, RomId]]]])

slots.eksamen__eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="eksamen__eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.eksamen__eksamensgruppe, domain=None, range=Optional[Union[str, EksamensgruppeId]])

slots.fag__tilrettelegging = Slot(uri=UTD.tilrettelegging, name="fag__tilrettelegging", curie=UTD.curie('tilrettelegging'),
                   model_uri=UTD.fag__tilrettelegging, domain=None, range=Optional[Union[Union[str, TilretteleggingId], list[Union[str, TilretteleggingId]]]])

slots.fag__grepreferanse = Slot(uri=UTD.grepreferanse, name="fag__grepreferanse", curie=UTD.curie('grepreferanse'),
                   model_uri=UTD.fag__grepreferanse, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.fag__skole = Slot(uri=UTD.skole, name="fag__skole", curie=UTD.curie('skole'),
                   model_uri=UTD.fag__skole, domain=None, range=Optional[Union[Union[str, SkoleId], list[Union[str, SkoleId]]]])

slots.fag__vigoreferanse = Slot(uri=UTD.vigoreferanse, name="fag__vigoreferanse", curie=UTD.curie('vigoreferanse'),
                   model_uri=UTD.fag__vigoreferanse, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.fag__programomrade = Slot(uri=UTD.programomrade, name="fag__programomrade", curie=UTD.curie('programomrade'),
                   model_uri=UTD.fag__programomrade, domain=None, range=Optional[Union[Union[str, ProgramomradeId], list[Union[str, ProgramomradeId]]]])

slots.fag__faggruppe = Slot(uri=UTD.faggruppe, name="fag__faggruppe", curie=UTD.curie('faggruppe'),
                   model_uri=UTD.fag__faggruppe, domain=None, range=Optional[Union[Union[str, FaggruppeId], list[Union[str, FaggruppeId]]]])

slots.fag__undervisningsgruppe = Slot(uri=UTD.undervisningsgruppe, name="fag__undervisningsgruppe", curie=UTD.curie('undervisningsgruppe'),
                   model_uri=UTD.fag__undervisningsgruppe, domain=None, range=Optional[Union[Union[str, UndervisningsgruppeId], list[Union[str, UndervisningsgruppeId]]]])

slots.fag__eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="fag__eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.fag__eksamensgruppe, domain=None, range=Optional[Union[Union[str, EksamensgruppeId], list[Union[str, EksamensgruppeId]]]])

slots.faggruppe__fag = Slot(uri=UTD.fag, name="faggruppe__fag", curie=UTD.curie('fag'),
                   model_uri=UTD.faggruppe__fag, domain=None, range=Union[str, FagId])

slots.faggruppe__skole = Slot(uri=UTD.skole, name="faggruppe__skole", curie=UTD.curie('skole'),
                   model_uri=UTD.faggruppe__skole, domain=None, range=Optional[Union[str, SkoleId]])

slots.faggruppe__skoleaar = Slot(uri=UTD.skoleaar, name="faggruppe__skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.faggruppe__skoleaar, domain=None, range=Optional[Union[str, SkoleaarId]])

slots.faggruppe__faggruppemedlemskap = Slot(uri=UTD.faggruppemedlemskap, name="faggruppe__faggruppemedlemskap", curie=UTD.curie('faggruppemedlemskap'),
                   model_uri=UTD.faggruppe__faggruppemedlemskap, domain=None, range=Optional[Union[Union[str, FaggruppemedlemskapId], list[Union[str, FaggruppemedlemskapId]]]])

slots.faggruppemedlemskap__elevforhold = Slot(uri=UTD.elevforhold, name="faggruppemedlemskap__elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.faggruppemedlemskap__elevforhold, domain=None, range=Optional[Union[str, ElevforholdId]])

slots.faggruppemedlemskap__varsel = Slot(uri=UTD.varsel, name="faggruppemedlemskap__varsel", curie=UTD.curie('varsel'),
                   model_uri=UTD.faggruppemedlemskap__varsel, domain=None, range=Optional[Union[Union[str, VarselId], list[Union[str, VarselId]]]])

slots.faggruppemedlemskap__faggruppe = Slot(uri=UTD.faggruppe, name="faggruppemedlemskap__faggruppe", curie=UTD.curie('faggruppe'),
                   model_uri=UTD.faggruppemedlemskap__faggruppe, domain=None, range=Optional[Union[str, FaggruppeId]])

slots.faggruppemedlemskap__fagmerknad = Slot(uri=UTD.fagmerknad, name="faggruppemedlemskap__fagmerknad", curie=UTD.curie('fagmerknad'),
                   model_uri=UTD.faggruppemedlemskap__fagmerknad, domain=None, range=Optional[Union[str, FagmerknadId]])

slots.faggruppemedlemskap__fagstatus = Slot(uri=UTD.fagstatus, name="faggruppemedlemskap__fagstatus", curie=UTD.curie('fagstatus'),
                   model_uri=UTD.faggruppemedlemskap__fagstatus, domain=None, range=Optional[Union[str, FagstatusId]])

slots.rom__navn = Slot(uri=UTD.navn, name="rom__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.rom__navn, domain=None, range=Optional[str])

slots.rom__eksamen = Slot(uri=UTD.eksamen, name="rom__eksamen", curie=UTD.curie('eksamen'),
                   model_uri=UTD.rom__eksamen, domain=None, range=Optional[Union[Union[str, EksamenId], list[Union[str, EksamenId]]]])

slots.rom__time = Slot(uri=UTD.time, name="rom__time", curie=UTD.curie('time'),
                   model_uri=UTD.rom__time, domain=None, range=Optional[Union[Union[str, TimeId], list[Union[str, TimeId]]]])

slots.time__navn = Slot(uri=UTD.navn, name="time__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.time__navn, domain=None, range=Optional[str])

slots.time__beskrivelse = Slot(uri=UTD.beskrivelse, name="time__beskrivelse", curie=UTD.curie('beskrivelse'),
                   model_uri=UTD.time__beskrivelse, domain=None, range=Optional[str])

slots.time__tidsrom = Slot(uri=UTD.tidsrom, name="time__tidsrom", curie=UTD.curie('tidsrom'),
                   model_uri=UTD.time__tidsrom, domain=None, range=Optional[Union[dict, Periode]])

slots.time__undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="time__undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.time__undervisningsforhold, domain=None, range=Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]])

slots.time__rom = Slot(uri=UTD.rom, name="time__rom", curie=UTD.curie('rom'),
                   model_uri=UTD.time__rom, domain=None, range=Optional[Union[Union[str, RomId], list[Union[str, RomId]]]])

slots.time__undervisningsgruppe = Slot(uri=UTD.undervisningsgruppe, name="time__undervisningsgruppe", curie=UTD.curie('undervisningsgruppe'),
                   model_uri=UTD.time__undervisningsgruppe, domain=None, range=Union[Union[str, UndervisningsgruppeId], list[Union[str, UndervisningsgruppeId]]])

slots.undervisningsforhold__arbeidsforhold = Slot(uri=UTD.arbeidsforhold, name="undervisningsforhold__arbeidsforhold", curie=UTD.curie('arbeidsforhold'),
                   model_uri=UTD.undervisningsforhold__arbeidsforhold, domain=None, range=Union[str, URIorCURIE])

slots.undervisningsforhold__skoleressurs = Slot(uri=UTD.skoleressurs, name="undervisningsforhold__skoleressurs", curie=UTD.curie('skoleressurs'),
                   model_uri=UTD.undervisningsforhold__skoleressurs, domain=None, range=Optional[Union[str, SkoleressursId]])

slots.undervisningsforhold__klasse = Slot(uri=UTD.klasse, name="undervisningsforhold__klasse", curie=UTD.curie('klasse'),
                   model_uri=UTD.undervisningsforhold__klasse, domain=None, range=Optional[Union[Union[str, KlasseId], list[Union[str, KlasseId]]]])

slots.undervisningsforhold__kontaktlaerergruppe = Slot(uri=UTD.kontaktlaerergruppe, name="undervisningsforhold__kontaktlaerergruppe", curie=UTD.curie('kontaktlaerergruppe'),
                   model_uri=UTD.undervisningsforhold__kontaktlaerergruppe, domain=None, range=Optional[Union[Union[str, KontaktlaerergruppeId], list[Union[str, KontaktlaerergruppeId]]]])

slots.undervisningsforhold__time = Slot(uri=UTD.time, name="undervisningsforhold__time", curie=UTD.curie('time'),
                   model_uri=UTD.undervisningsforhold__time, domain=None, range=Optional[Union[Union[str, TimeId], list[Union[str, TimeId]]]])

slots.undervisningsforhold__eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="undervisningsforhold__eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.undervisningsforhold__eksamensgruppe, domain=None, range=Optional[Union[Union[str, EksamensgruppeId], list[Union[str, EksamensgruppeId]]]])

slots.undervisningsgruppe__undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="undervisningsgruppe__undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.undervisningsgruppe__undervisningsforhold, domain=None, range=Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]])

slots.undervisningsgruppe__fag = Slot(uri=UTD.fag, name="undervisningsgruppe__fag", curie=UTD.curie('fag'),
                   model_uri=UTD.undervisningsgruppe__fag, domain=None, range=Union[Union[str, FagId], list[Union[str, FagId]]])

slots.undervisningsgruppe__time = Slot(uri=UTD.time, name="undervisningsgruppe__time", curie=UTD.curie('time'),
                   model_uri=UTD.undervisningsgruppe__time, domain=None, range=Optional[Union[Union[str, TimeId], list[Union[str, TimeId]]]])

slots.undervisningsgruppe__termin = Slot(uri=UTD.termin, name="undervisningsgruppe__termin", curie=UTD.curie('termin'),
                   model_uri=UTD.undervisningsgruppe__termin, domain=None, range=Optional[Union[Union[str, TerminId], list[Union[str, TerminId]]]])

slots.undervisningsgruppe__skole = Slot(uri=UTD.skole, name="undervisningsgruppe__skole", curie=UTD.curie('skole'),
                   model_uri=UTD.undervisningsgruppe__skole, domain=None, range=Optional[Union[str, SkoleId]])

slots.undervisningsgruppe__skoleaar = Slot(uri=UTD.skoleaar, name="undervisningsgruppe__skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.undervisningsgruppe__skoleaar, domain=None, range=Optional[Union[str, SkoleaarId]])

slots.undervisningsgruppe__gruppemedlemskap = Slot(uri=UTD.gruppemedlemskap, name="undervisningsgruppe__gruppemedlemskap", curie=UTD.curie('gruppemedlemskap'),
                   model_uri=UTD.undervisningsgruppe__gruppemedlemskap, domain=None, range=Optional[Union[Union[str, UndervisningsgruppemedlemskapId], list[Union[str, UndervisningsgruppemedlemskapId]]]])

slots.undervisningsgruppemedlemskap__elevforhold = Slot(uri=UTD.elevforhold, name="undervisningsgruppemedlemskap__elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.undervisningsgruppemedlemskap__elevforhold, domain=None, range=Optional[Union[str, ElevforholdId]])

slots.undervisningsgruppemedlemskap__undervisningsgruppe = Slot(uri=UTD.undervisningsgruppe, name="undervisningsgruppemedlemskap__undervisningsgruppe", curie=UTD.curie('undervisningsgruppe'),
                   model_uri=UTD.undervisningsgruppemedlemskap__undervisningsgruppe, domain=None, range=Optional[Union[str, UndervisningsgruppeId]])

slots.fagvurderingAbstrakt__kommentar = Slot(uri=UTD.kommentar, name="fagvurderingAbstrakt__kommentar", curie=UTD.curie('kommentar'),
                   model_uri=UTD.fagvurderingAbstrakt__kommentar, domain=None, range=str)

slots.fagvurderingAbstrakt__vurderingsdato = Slot(uri=UTD.vurderingsdato, name="fagvurderingAbstrakt__vurderingsdato", curie=UTD.curie('vurderingsdato'),
                   model_uri=UTD.fagvurderingAbstrakt__vurderingsdato, domain=None, range=Union[str, XSDDateTime])

slots.fagvurderingAbstrakt__fag = Slot(uri=UTD.fag, name="fagvurderingAbstrakt__fag", curie=UTD.curie('fag'),
                   model_uri=UTD.fagvurderingAbstrakt__fag, domain=None, range=Optional[Union[str, FagId]])

slots.fagvurderingAbstrakt__skoleaar = Slot(uri=UTD.skoleaar, name="fagvurderingAbstrakt__skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.fagvurderingAbstrakt__skoleaar, domain=None, range=Optional[Union[str, SkoleaarId]])

slots.fagvurderingAbstrakt__karakter = Slot(uri=UTD.karakter, name="fagvurderingAbstrakt__karakter", curie=UTD.curie('karakter'),
                   model_uri=UTD.fagvurderingAbstrakt__karakter, domain=None, range=Optional[Union[str, KarakterverdiId]])

slots.ordensvurderingAbstrakt__kommentar = Slot(uri=UTD.kommentar, name="ordensvurderingAbstrakt__kommentar", curie=UTD.curie('kommentar'),
                   model_uri=UTD.ordensvurderingAbstrakt__kommentar, domain=None, range=str)

slots.ordensvurderingAbstrakt__vurderingsdato = Slot(uri=UTD.vurderingsdato, name="ordensvurderingAbstrakt__vurderingsdato", curie=UTD.curie('vurderingsdato'),
                   model_uri=UTD.ordensvurderingAbstrakt__vurderingsdato, domain=None, range=Union[str, XSDDateTime])

slots.ordensvurderingAbstrakt__atferd = Slot(uri=UTD.atferd, name="ordensvurderingAbstrakt__atferd", curie=UTD.curie('atferd'),
                   model_uri=UTD.ordensvurderingAbstrakt__atferd, domain=None, range=Optional[Union[str, KarakterverdiId]])

slots.ordensvurderingAbstrakt__orden = Slot(uri=UTD.orden, name="ordensvurderingAbstrakt__orden", curie=UTD.curie('orden'),
                   model_uri=UTD.ordensvurderingAbstrakt__orden, domain=None, range=Optional[Union[str, KarakterverdiId]])

slots.ordensvurderingAbstrakt__skoleaar = Slot(uri=UTD.skoleaar, name="ordensvurderingAbstrakt__skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.ordensvurderingAbstrakt__skoleaar, domain=None, range=Optional[Union[str, SkoleaarId]])

slots.anmerkninger__atferd = Slot(uri=UTD.atferd, name="anmerkninger__atferd", curie=UTD.curie('atferd'),
                   model_uri=UTD.anmerkninger__atferd, domain=None, range=int)

slots.anmerkninger__orden = Slot(uri=UTD.orden, name="anmerkninger__orden", curie=UTD.curie('orden'),
                   model_uri=UTD.anmerkninger__orden, domain=None, range=int)

slots.anmerkninger__skoleaar = Slot(uri=UTD.skoleaar, name="anmerkninger__skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.anmerkninger__skoleaar, domain=None, range=Optional[Union[str, SkoleaarId]])

slots.eksamensgruppe__eksamensdato = Slot(uri=UTD.eksamensdato, name="eksamensgruppe__eksamensdato", curie=UTD.curie('eksamensdato'),
                   model_uri=UTD.eksamensgruppe__eksamensdato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.eksamensgruppe__fag = Slot(uri=UTD.fag, name="eksamensgruppe__fag", curie=UTD.curie('fag'),
                   model_uri=UTD.eksamensgruppe__fag, domain=None, range=Union[str, FagId])

slots.eksamensgruppe__skole = Slot(uri=UTD.skole, name="eksamensgruppe__skole", curie=UTD.curie('skole'),
                   model_uri=UTD.eksamensgruppe__skole, domain=None, range=Union[str, SkoleId])

slots.eksamensgruppe__termin = Slot(uri=UTD.termin, name="eksamensgruppe__termin", curie=UTD.curie('termin'),
                   model_uri=UTD.eksamensgruppe__termin, domain=None, range=Union[str, TerminId])

slots.eksamensgruppe__undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="eksamensgruppe__undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.eksamensgruppe__undervisningsforhold, domain=None, range=Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]])

slots.eksamensgruppe__eksamen = Slot(uri=UTD.eksamen, name="eksamensgruppe__eksamen", curie=UTD.curie('eksamen'),
                   model_uri=UTD.eksamensgruppe__eksamen, domain=None, range=Optional[Union[str, EksamenId]])

slots.eksamensgruppe__eksamensform = Slot(uri=UTD.eksamensform, name="eksamensgruppe__eksamensform", curie=UTD.curie('eksamensform'),
                   model_uri=UTD.eksamensgruppe__eksamensform, domain=None, range=Optional[Union[str, EksamensformId]])

slots.eksamensgruppe__skoleaar = Slot(uri=UTD.skoleaar, name="eksamensgruppe__skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.eksamensgruppe__skoleaar, domain=None, range=Optional[Union[str, SkoleaarId]])

slots.eksamensgruppe__gruppemedlemskap = Slot(uri=UTD.gruppemedlemskap, name="eksamensgruppe__gruppemedlemskap", curie=UTD.curie('gruppemedlemskap'),
                   model_uri=UTD.eksamensgruppe__gruppemedlemskap, domain=None, range=Optional[Union[Union[str, EksamensgruppemedlemskapId], list[Union[str, EksamensgruppemedlemskapId]]]])

slots.eksamensgruppe__sensor = Slot(uri=UTD.sensor, name="eksamensgruppe__sensor", curie=UTD.curie('sensor'),
                   model_uri=UTD.eksamensgruppe__sensor, domain=None, range=Optional[Union[Union[str, SensorId], list[Union[str, SensorId]]]])

slots.eksamensgruppemedlemskap__delegert = Slot(uri=UTD.delegert, name="eksamensgruppemedlemskap__delegert", curie=UTD.curie('delegert'),
                   model_uri=UTD.eksamensgruppemedlemskap__delegert, domain=None, range=Optional[Union[bool, Bool]])

slots.eksamensgruppemedlemskap__kandidatnummer = Slot(uri=UTD.kandidatnummer, name="eksamensgruppemedlemskap__kandidatnummer", curie=UTD.curie('kandidatnummer'),
                   model_uri=UTD.eksamensgruppemedlemskap__kandidatnummer, domain=None, range=Optional[str])

slots.eksamensgruppemedlemskap__delegertTil = Slot(uri=UTD.delegertTil, name="eksamensgruppemedlemskap__delegertTil", curie=UTD.curie('delegertTil'),
                   model_uri=UTD.eksamensgruppemedlemskap__delegertTil, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.eksamensgruppemedlemskap__foretrukketSkole = Slot(uri=UTD.foretrukketSkole, name="eksamensgruppemedlemskap__foretrukketSkole", curie=UTD.curie('foretrukketSkole'),
                   model_uri=UTD.eksamensgruppemedlemskap__foretrukketSkole, domain=None, range=Optional[Union[bool, Bool]])

slots.eksamensgruppemedlemskap__foretrukketSensor = Slot(uri=UTD.foretrukketSensor, name="eksamensgruppemedlemskap__foretrukketSensor", curie=UTD.curie('foretrukketSensor'),
                   model_uri=UTD.eksamensgruppemedlemskap__foretrukketSensor, domain=None, range=Optional[Union[bool, Bool]])

slots.eksamensgruppemedlemskap__betalingsstatus = Slot(uri=UTD.betalingsstatus, name="eksamensgruppemedlemskap__betalingsstatus", curie=UTD.curie('betalingsstatus'),
                   model_uri=UTD.eksamensgruppemedlemskap__betalingsstatus, domain=None, range=Optional[Union[str, BetalingsstatusId]])

slots.eksamensgruppemedlemskap__elevforhold = Slot(uri=UTD.elevforhold, name="eksamensgruppemedlemskap__elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.eksamensgruppemedlemskap__elevforhold, domain=None, range=Union[str, ElevforholdId])

slots.eksamensgruppemedlemskap__eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="eksamensgruppemedlemskap__eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.eksamensgruppemedlemskap__eksamensgruppe, domain=None, range=Union[str, EksamensgruppeId])

slots.eksamensgruppemedlemskap__nus = Slot(uri=UTD.nus, name="eksamensgruppemedlemskap__nus", curie=UTD.curie('nus'),
                   model_uri=UTD.eksamensgruppemedlemskap__nus, domain=None, range=Optional[Union[str, KarakterstatusId]])

slots.eksamensvurdering__eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="eksamensvurdering__eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.eksamensvurdering__eksamensgruppe, domain=None, range=Union[str, EksamensgruppeId])

slots.eksamensvurdering__karakterhistorie = Slot(uri=UTD.karakterhistorie, name="eksamensvurdering__karakterhistorie", curie=UTD.curie('karakterhistorie'),
                   model_uri=UTD.eksamensvurdering__karakterhistorie, domain=None, range=Optional[Union[Union[str, KarakterhistorieId], list[Union[str, KarakterhistorieId]]]])

slots.eksamensvurdering__elevvurdering = Slot(uri=UTD.elevvurdering, name="eksamensvurdering__elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.eksamensvurdering__elevvurdering, domain=None, range=Union[str, ElevvurderingId])

slots.elevfravar__elevforhold = Slot(uri=UTD.elevforhold, name="elevfravar__elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.elevfravar__elevforhold, domain=None, range=Union[str, ElevforholdId])

slots.elevfravar__fraversregistrering = Slot(uri=UTD.fraversregistrering, name="elevfravar__fraversregistrering", curie=UTD.curie('fraversregistrering'),
                   model_uri=UTD.elevfravar__fraversregistrering, domain=None, range=Optional[Union[Union[str, FraversregistreringId], list[Union[str, FraversregistreringId]]]])

slots.elevvurdering__elevforhold = Slot(uri=UTD.elevforhold, name="elevvurdering__elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.elevvurdering__elevforhold, domain=None, range=Union[str, ElevforholdId])

slots.elevvurdering__eksamensvurdering = Slot(uri=UTD.eksamensvurdering, name="elevvurdering__eksamensvurdering", curie=UTD.curie('eksamensvurdering'),
                   model_uri=UTD.elevvurdering__eksamensvurdering, domain=None, range=Optional[Union[Union[str, EksamensvurderingId], list[Union[str, EksamensvurderingId]]]])

slots.elevvurdering__sluttfagvurdering = Slot(uri=UTD.sluttfagvurdering, name="elevvurdering__sluttfagvurdering", curie=UTD.curie('sluttfagvurdering'),
                   model_uri=UTD.elevvurdering__sluttfagvurdering, domain=None, range=Optional[Union[Union[str, SluttfagvurderingId], list[Union[str, SluttfagvurderingId]]]])

slots.elevvurdering__halvaarsfagvurdering = Slot(uri=UTD.halvaarsfagvurdering, name="elevvurdering__halvaarsfagvurdering", curie=UTD.curie('halvaarsfagvurdering'),
                   model_uri=UTD.elevvurdering__halvaarsfagvurdering, domain=None, range=Optional[Union[Union[str, HalvaarsfagvurderingId], list[Union[str, HalvaarsfagvurderingId]]]])

slots.elevvurdering__underveisfagvurdering = Slot(uri=UTD.underveisfagvurdering, name="elevvurdering__underveisfagvurdering", curie=UTD.curie('underveisfagvurdering'),
                   model_uri=UTD.elevvurdering__underveisfagvurdering, domain=None, range=Optional[Union[Union[str, UnderveisfagvurderingId], list[Union[str, UnderveisfagvurderingId]]]])

slots.elevvurdering__halvaarsordensvurdering = Slot(uri=UTD.halvaarsordensvurdering, name="elevvurdering__halvaarsordensvurdering", curie=UTD.curie('halvaarsordensvurdering'),
                   model_uri=UTD.elevvurdering__halvaarsordensvurdering, domain=None, range=Optional[Union[Union[str, HalvaarsordensvurderingId], list[Union[str, HalvaarsordensvurderingId]]]])

slots.elevvurdering__underveisordensvurdering = Slot(uri=UTD.underveisordensvurdering, name="elevvurdering__underveisordensvurdering", curie=UTD.curie('underveisordensvurdering'),
                   model_uri=UTD.elevvurdering__underveisordensvurdering, domain=None, range=Optional[Union[Union[str, UnderveisordensvurderingId], list[Union[str, UnderveisordensvurderingId]]]])

slots.elevvurdering__sluttordensvurdering = Slot(uri=UTD.sluttordensvurdering, name="elevvurdering__sluttordensvurdering", curie=UTD.curie('sluttordensvurdering'),
                   model_uri=UTD.elevvurdering__sluttordensvurdering, domain=None, range=Optional[Union[Union[str, SluttordensvurderingId], list[Union[str, SluttordensvurderingId]]]])

slots.elevvurdering__vitnemalsmerknad = Slot(uri=UTD.vitnemalsmerknad, name="elevvurdering__vitnemalsmerknad", curie=UTD.curie('vitnemalsmerknad'),
                   model_uri=UTD.elevvurdering__vitnemalsmerknad, domain=None, range=Optional[Union[str, VitnemalsmerknadId]])

slots.fravarsoversikt__halvaar = Slot(uri=UTD.halvaar, name="fravarsoversikt__halvaar", curie=UTD.curie('halvaar'),
                   model_uri=UTD.fravarsoversikt__halvaar, domain=None, range=Union[dict, Fravarsprosent])

slots.fravarsoversikt__skoleaarFravar = Slot(uri=UTD.skoleaarFravar, name="fravarsoversikt__skoleaarFravar", curie=UTD.curie('skoleaarFravar'),
                   model_uri=UTD.fravarsoversikt__skoleaarFravar, domain=None, range=Union[dict, Fravarsprosent])

slots.fravarsoversikt__elevforhold = Slot(uri=UTD.elevforhold, name="fravarsoversikt__elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.fravarsoversikt__elevforhold, domain=None, range=Union[str, ElevforholdId])

slots.fravarsoversikt__fag = Slot(uri=UTD.fag, name="fravarsoversikt__fag", curie=UTD.curie('fag'),
                   model_uri=UTD.fravarsoversikt__fag, domain=None, range=Union[str, FagId])

slots.fravarsprosent__fravaerstimer = Slot(uri=UTD.fravaerstimer, name="fravarsprosent__fravaerstimer", curie=UTD.curie('fravaerstimer'),
                   model_uri=UTD.fravarsprosent__fravaerstimer, domain=None, range=int)

slots.fravarsprosent__prosent = Slot(uri=UTD.prosent, name="fravarsprosent__prosent", curie=UTD.curie('prosent'),
                   model_uri=UTD.fravarsprosent__prosent, domain=None, range=int)

slots.fravarsprosent__undervisningstimer = Slot(uri=UTD.undervisningstimer, name="fravarsprosent__undervisningstimer", curie=UTD.curie('undervisningstimer'),
                   model_uri=UTD.fravarsprosent__undervisningstimer, domain=None, range=int)

slots.fraversregistrering__forersPaaVitnemaal = Slot(uri=UTD.forersPaaVitnemaal, name="fraversregistrering__forersPaaVitnemaal", curie=UTD.curie('forersPaaVitnemaal'),
                   model_uri=UTD.fraversregistrering__forersPaaVitnemaal, domain=None, range=Union[bool, Bool])

slots.fraversregistrering__kommentar = Slot(uri=UTD.kommentar, name="fraversregistrering__kommentar", curie=UTD.curie('kommentar'),
                   model_uri=UTD.fraversregistrering__kommentar, domain=None, range=Optional[str])

slots.fraversregistrering__periode = Slot(uri=UTD.periode, name="fraversregistrering__periode", curie=UTD.curie('periode'),
                   model_uri=UTD.fraversregistrering__periode, domain=None, range=Union[dict, Periode])

slots.fraversregistrering__registrertAv = Slot(uri=UTD.registrertAv, name="fraversregistrering__registrertAv", curie=UTD.curie('registrertAv'),
                   model_uri=UTD.fraversregistrering__registrertAv, domain=None, range=Optional[Union[str, SkoleressursId]])

slots.fraversregistrering__faggruppe = Slot(uri=UTD.faggruppe, name="fraversregistrering__faggruppe", curie=UTD.curie('faggruppe'),
                   model_uri=UTD.fraversregistrering__faggruppe, domain=None, range=Optional[Union[str, FaggruppeId]])

slots.fraversregistrering__undervisningsgruppe = Slot(uri=UTD.undervisningsgruppe, name="fraversregistrering__undervisningsgruppe", curie=UTD.curie('undervisningsgruppe'),
                   model_uri=UTD.fraversregistrering__undervisningsgruppe, domain=None, range=Union[str, UndervisningsgruppeId])

slots.fraversregistrering__elevfravar = Slot(uri=UTD.elevfravar, name="fraversregistrering__elevfravar", curie=UTD.curie('elevfravar'),
                   model_uri=UTD.fraversregistrering__elevfravar, domain=None, range=Union[str, ElevfravarId])

slots.fraversregistrering__fravartype = Slot(uri=UTD.fravartype, name="fraversregistrering__fravartype", curie=UTD.curie('fravartype'),
                   model_uri=UTD.fraversregistrering__fravartype, domain=None, range=Union[str, FravartypeId])

slots.halvaarsfagvurdering__elevvurdering = Slot(uri=UTD.elevvurdering, name="halvaarsfagvurdering__elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.halvaarsfagvurdering__elevvurdering, domain=None, range=Union[str, ElevvurderingId])

slots.halvaarsordensvurdering__elevvurdering = Slot(uri=UTD.elevvurdering, name="halvaarsordensvurdering__elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.halvaarsordensvurdering__elevvurdering, domain=None, range=Union[str, ElevvurderingId])

slots.karakterhistorie__endretDato = Slot(uri=UTD.endretDato, name="karakterhistorie__endretDato", curie=UTD.curie('endretDato'),
                   model_uri=UTD.karakterhistorie__endretDato, domain=None, range=Union[str, XSDDateTime])

slots.karakterhistorie__oppdatertAv = Slot(uri=UTD.oppdatertAv, name="karakterhistorie__oppdatertAv", curie=UTD.curie('oppdatertAv'),
                   model_uri=UTD.karakterhistorie__oppdatertAv, domain=None, range=Optional[Union[str, SkoleressursId]])

slots.karakterhistorie__opprinneligKarakterverdi = Slot(uri=UTD.opprinneligKarakterverdi, name="karakterhistorie__opprinneligKarakterverdi", curie=UTD.curie('opprinneligKarakterverdi'),
                   model_uri=UTD.karakterhistorie__opprinneligKarakterverdi, domain=None, range=Optional[Union[str, KarakterverdiId]])

slots.karakterhistorie__opprinneligKarakterstatus = Slot(uri=UTD.opprinneligKarakterstatus, name="karakterhistorie__opprinneligKarakterstatus", curie=UTD.curie('opprinneligKarakterstatus'),
                   model_uri=UTD.karakterhistorie__opprinneligKarakterstatus, domain=None, range=Optional[Union[str, KarakterstatusId]])

slots.karakterhistorie__karakterverdi = Slot(uri=UTD.karakterverdi, name="karakterhistorie__karakterverdi", curie=UTD.curie('karakterverdi'),
                   model_uri=UTD.karakterhistorie__karakterverdi, domain=None, range=Optional[Union[str, KarakterverdiId]])

slots.karakterhistorie__karakterstatus = Slot(uri=UTD.karakterstatus, name="karakterhistorie__karakterstatus", curie=UTD.curie('karakterstatus'),
                   model_uri=UTD.karakterhistorie__karakterstatus, domain=None, range=Optional[Union[str, KarakterstatusId]])

slots.sensor__aktiv = Slot(uri=UTD.aktiv, name="sensor__aktiv", curie=UTD.curie('aktiv'),
                   model_uri=UTD.sensor__aktiv, domain=None, range=Union[bool, Bool])

slots.sensor__sensornummer = Slot(uri=UTD.sensornummer, name="sensor__sensornummer", curie=UTD.curie('sensornummer'),
                   model_uri=UTD.sensor__sensornummer, domain=None, range=Optional[int])

slots.sensor__skoleressurs = Slot(uri=UTD.skoleressurs, name="sensor__skoleressurs", curie=UTD.curie('skoleressurs'),
                   model_uri=UTD.sensor__skoleressurs, domain=None, range=Union[str, SkoleressursId])

slots.sensor__eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="sensor__eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.sensor__eksamensgruppe, domain=None, range=Union[str, EksamensgruppeId])

slots.sluttfagvurdering__eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="sluttfagvurdering__eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.sluttfagvurdering__eksamensgruppe, domain=None, range=Optional[Union[str, EksamensgruppeId]])

slots.sluttfagvurdering__elevvurdering = Slot(uri=UTD.elevvurdering, name="sluttfagvurdering__elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.sluttfagvurdering__elevvurdering, domain=None, range=Union[str, ElevvurderingId])

slots.sluttfagvurdering__karakterhistorie = Slot(uri=UTD.karakterhistorie, name="sluttfagvurdering__karakterhistorie", curie=UTD.curie('karakterhistorie'),
                   model_uri=UTD.sluttfagvurdering__karakterhistorie, domain=None, range=Optional[Union[Union[str, KarakterhistorieId], list[Union[str, KarakterhistorieId]]]])

slots.sluttordensvurdering__elevvurdering = Slot(uri=UTD.elevvurdering, name="sluttordensvurdering__elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.sluttordensvurdering__elevvurdering, domain=None, range=Union[str, ElevvurderingId])

slots.underveisfagvurdering__elevvurdering = Slot(uri=UTD.elevvurdering, name="underveisfagvurdering__elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.underveisfagvurdering__elevvurdering, domain=None, range=Union[str, ElevvurderingId])

slots.underveisordensvurdering__elevvurdering = Slot(uri=UTD.elevvurdering, name="underveisordensvurdering__elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.underveisordensvurdering__elevvurdering, domain=None, range=Union[str, ElevvurderingId])

slots.avlagtProve__provedato = Slot(uri=UTD.provedato, name="avlagtProve__provedato", curie=UTD.curie('provedato'),
                   model_uri=UTD.avlagtProve__provedato, domain=None, range=Optional[Union[str, XSDDate]])

slots.avlagtProve__laerling = Slot(uri=UTD.laerling, name="avlagtProve__laerling", curie=UTD.curie('laerling'),
                   model_uri=UTD.avlagtProve__laerling, domain=None, range=Union[str, LaerlingId])

slots.avlagtProve__provestatus = Slot(uri=UTD.provestatus, name="avlagtProve__provestatus", curie=UTD.curie('provestatus'),
                   model_uri=UTD.avlagtProve__provestatus, domain=None, range=Optional[Union[str, ProvestatusId]])

slots.avlagtProve__fullfortkode = Slot(uri=UTD.fullfortkode, name="avlagtProve__fullfortkode", curie=UTD.curie('fullfortkode'),
                   model_uri=UTD.avlagtProve__fullfortkode, domain=None, range=Optional[Union[str, FullfortkodeId]])

slots.avlagtProve__brevtype = Slot(uri=UTD.brevtype, name="avlagtProve__brevtype", curie=UTD.curie('brevtype'),
                   model_uri=UTD.avlagtProve__brevtype, domain=None, range=Optional[Union[str, BrevtypeId]])

slots.avlagtProve__bevistype = Slot(uri=UTD.bevistype, name="avlagtProve__bevistype", curie=UTD.curie('bevistype'),
                   model_uri=UTD.avlagtProve__bevistype, domain=None, range=Optional[Union[str, BevistypeId]])

slots.laerling__kontraktstype = Slot(uri=UTD.kontraktstype, name="laerling__kontraktstype", curie=UTD.curie('kontraktstype'),
                   model_uri=UTD.laerling__kontraktstype, domain=None, range=Optional[str])

slots.laerling__laretid = Slot(uri=UTD.laretid, name="laerling__laretid", curie=UTD.curie('laretid'),
                   model_uri=UTD.laerling__laretid, domain=None, range=Optional[Union[dict, Periode]])

slots.laerling__person = Slot(uri=UTD.person, name="laerling__person", curie=UTD.curie('person'),
                   model_uri=UTD.laerling__person, domain=None, range=Union[str, URIorCURIE])

slots.laerling__bedrift = Slot(uri=UTD.bedrift, name="laerling__bedrift", curie=UTD.curie('bedrift'),
                   model_uri=UTD.laerling__bedrift, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.laerling__avlagtprove = Slot(uri=UTD.avlagtprove, name="laerling__avlagtprove", curie=UTD.curie('avlagtprove'),
                   model_uri=UTD.laerling__avlagtprove, domain=None, range=Optional[Union[Union[str, AvlagtProveId], list[Union[str, AvlagtProveId]]]])

slots.laerling__programomrade = Slot(uri=UTD.programomrade, name="laerling__programomrade", curie=UTD.curie('programomrade'),
                   model_uri=UTD.laerling__programomrade, domain=None, range=Optional[Union[str, ProgramomradeId]])

slots.otUngdom__person = Slot(uri=UTD.person, name="otUngdom__person", curie=UTD.curie('person'),
                   model_uri=UTD.otUngdom__person, domain=None, range=Union[str, URIorCURIE])

slots.otUngdom__status = Slot(uri=UTD.status, name="otUngdom__status", curie=UTD.curie('status'),
                   model_uri=UTD.otUngdom__status, domain=None, range=Optional[Union[str, OtStatusId]])

slots.otUngdom__enhet = Slot(uri=UTD.enhet, name="otUngdom__enhet", curie=UTD.curie('enhet'),
                   model_uri=UTD.otUngdom__enhet, domain=None, range=Optional[Union[str, OtEnhetId]])

slots.otUngdom__programomrade = Slot(uri=UTD.programomrade, name="otUngdom__programomrade", curie=UTD.curie('programomrade'),
                   model_uri=UTD.otUngdom__programomrade, domain=None, range=Optional[Union[str, ProgramomradeId]])

slots.avbruddsaarsak__kode = Slot(uri=UTD.kode, name="avbruddsaarsak__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.avbruddsaarsak__kode, domain=None, range=str)

slots.avbruddsaarsak__navn = Slot(uri=UTD.navn, name="avbruddsaarsak__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.avbruddsaarsak__navn, domain=None, range=str)

slots.avbruddsaarsak__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="avbruddsaarsak__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.avbruddsaarsak__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.avbruddsaarsak__passiv = Slot(uri=UTD.passiv, name="avbruddsaarsak__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.avbruddsaarsak__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.betalingsstatus__kode = Slot(uri=UTD.kode, name="betalingsstatus__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.betalingsstatus__kode, domain=None, range=str)

slots.betalingsstatus__navn = Slot(uri=UTD.navn, name="betalingsstatus__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.betalingsstatus__navn, domain=None, range=str)

slots.betalingsstatus__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="betalingsstatus__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.betalingsstatus__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.betalingsstatus__passiv = Slot(uri=UTD.passiv, name="betalingsstatus__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.betalingsstatus__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.bevistype__kode = Slot(uri=UTD.kode, name="bevistype__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.bevistype__kode, domain=None, range=str)

slots.bevistype__navn = Slot(uri=UTD.navn, name="bevistype__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.bevistype__navn, domain=None, range=str)

slots.bevistype__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="bevistype__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.bevistype__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.bevistype__passiv = Slot(uri=UTD.passiv, name="bevistype__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.bevistype__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.brevtype__kode = Slot(uri=UTD.kode, name="brevtype__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.brevtype__kode, domain=None, range=str)

slots.brevtype__navn = Slot(uri=UTD.navn, name="brevtype__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.brevtype__navn, domain=None, range=str)

slots.brevtype__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="brevtype__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.brevtype__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.brevtype__passiv = Slot(uri=UTD.passiv, name="brevtype__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.brevtype__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.eksamensform__kode = Slot(uri=UTD.kode, name="eksamensform__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.eksamensform__kode, domain=None, range=str)

slots.eksamensform__navn = Slot(uri=UTD.navn, name="eksamensform__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.eksamensform__navn, domain=None, range=str)

slots.eksamensform__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="eksamensform__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.eksamensform__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.eksamensform__passiv = Slot(uri=UTD.passiv, name="eksamensform__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.eksamensform__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.elevkategori__kode = Slot(uri=UTD.kode, name="elevkategori__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.elevkategori__kode, domain=None, range=str)

slots.elevkategori__navn = Slot(uri=UTD.navn, name="elevkategori__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.elevkategori__navn, domain=None, range=str)

slots.elevkategori__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="elevkategori__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.elevkategori__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.elevkategori__passiv = Slot(uri=UTD.passiv, name="elevkategori__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.elevkategori__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.fagmerknad__kode = Slot(uri=UTD.kode, name="fagmerknad__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.fagmerknad__kode, domain=None, range=str)

slots.fagmerknad__navn = Slot(uri=UTD.navn, name="fagmerknad__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.fagmerknad__navn, domain=None, range=str)

slots.fagmerknad__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="fagmerknad__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.fagmerknad__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.fagmerknad__passiv = Slot(uri=UTD.passiv, name="fagmerknad__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.fagmerknad__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.fagstatus__kode = Slot(uri=UTD.kode, name="fagstatus__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.fagstatus__kode, domain=None, range=str)

slots.fagstatus__navn = Slot(uri=UTD.navn, name="fagstatus__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.fagstatus__navn, domain=None, range=str)

slots.fagstatus__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="fagstatus__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.fagstatus__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.fagstatus__passiv = Slot(uri=UTD.passiv, name="fagstatus__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.fagstatus__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.fravartype__kode = Slot(uri=UTD.kode, name="fravartype__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.fravartype__kode, domain=None, range=str)

slots.fravartype__navn = Slot(uri=UTD.navn, name="fravartype__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.fravartype__navn, domain=None, range=str)

slots.fravartype__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="fravartype__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.fravartype__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.fravartype__passiv = Slot(uri=UTD.passiv, name="fravartype__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.fravartype__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.fullfortkode__kode = Slot(uri=UTD.kode, name="fullfortkode__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.fullfortkode__kode, domain=None, range=str)

slots.fullfortkode__navn = Slot(uri=UTD.navn, name="fullfortkode__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.fullfortkode__navn, domain=None, range=str)

slots.fullfortkode__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="fullfortkode__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.fullfortkode__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.fullfortkode__passiv = Slot(uri=UTD.passiv, name="fullfortkode__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.fullfortkode__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.karakterskala__kode = Slot(uri=UTD.kode, name="karakterskala__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.karakterskala__kode, domain=None, range=str)

slots.karakterskala__navn = Slot(uri=UTD.navn, name="karakterskala__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.karakterskala__navn, domain=None, range=str)

slots.karakterskala__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="karakterskala__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.karakterskala__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.karakterskala__passiv = Slot(uri=UTD.passiv, name="karakterskala__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.karakterskala__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.karakterskala__verdi = Slot(uri=UTD.verdi, name="karakterskala__verdi", curie=UTD.curie('verdi'),
                   model_uri=UTD.karakterskala__verdi, domain=None, range=Optional[Union[Union[str, KarakterverdiId], list[Union[str, KarakterverdiId]]]])

slots.karakterskala__vigoreferanse = Slot(uri=UTD.vigoreferanse, name="karakterskala__vigoreferanse", curie=UTD.curie('vigoreferanse'),
                   model_uri=UTD.karakterskala__vigoreferanse, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.karakterstatus__kode = Slot(uri=UTD.kode, name="karakterstatus__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.karakterstatus__kode, domain=None, range=str)

slots.karakterstatus__navn = Slot(uri=UTD.navn, name="karakterstatus__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.karakterstatus__navn, domain=None, range=str)

slots.karakterstatus__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="karakterstatus__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.karakterstatus__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.karakterstatus__passiv = Slot(uri=UTD.passiv, name="karakterstatus__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.karakterstatus__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.karakterverdi__kode = Slot(uri=UTD.kode, name="karakterverdi__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.karakterverdi__kode, domain=None, range=str)

slots.karakterverdi__navn = Slot(uri=UTD.navn, name="karakterverdi__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.karakterverdi__navn, domain=None, range=str)

slots.karakterverdi__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="karakterverdi__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.karakterverdi__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.karakterverdi__passiv = Slot(uri=UTD.passiv, name="karakterverdi__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.karakterverdi__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.karakterverdi__skala = Slot(uri=UTD.skala, name="karakterverdi__skala", curie=UTD.curie('skala'),
                   model_uri=UTD.karakterverdi__skala, domain=None, range=Union[str, KarakterskalaId])

slots.otEnhet__kode = Slot(uri=UTD.kode, name="otEnhet__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.otEnhet__kode, domain=None, range=str)

slots.otEnhet__navn = Slot(uri=UTD.navn, name="otEnhet__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.otEnhet__navn, domain=None, range=str)

slots.otEnhet__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="otEnhet__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.otEnhet__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.otEnhet__passiv = Slot(uri=UTD.passiv, name="otEnhet__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.otEnhet__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.otEnhet__kommune = Slot(uri=UTD.kommune, name="otEnhet__kommune", curie=UTD.curie('kommune'),
                   model_uri=UTD.otEnhet__kommune, domain=None, range=Union[str, URIorCURIE])

slots.otStatus__kode = Slot(uri=UTD.kode, name="otStatus__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.otStatus__kode, domain=None, range=str)

slots.otStatus__navn = Slot(uri=UTD.navn, name="otStatus__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.otStatus__navn, domain=None, range=str)

slots.otStatus__beskrivelse = Slot(uri=UTD.beskrivelse, name="otStatus__beskrivelse", curie=UTD.curie('beskrivelse'),
                   model_uri=UTD.otStatus__beskrivelse, domain=None, range=Optional[str])

slots.otStatus__type = Slot(uri=UTD.type, name="otStatus__type", curie=UTD.curie('type'),
                   model_uri=UTD.otStatus__type, domain=None, range=str)

slots.otStatus__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="otStatus__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.otStatus__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.otStatus__passiv = Slot(uri=UTD.passiv, name="otStatus__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.otStatus__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.provestatus__kode = Slot(uri=UTD.kode, name="provestatus__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.provestatus__kode, domain=None, range=str)

slots.provestatus__navn = Slot(uri=UTD.navn, name="provestatus__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.provestatus__navn, domain=None, range=str)

slots.provestatus__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="provestatus__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.provestatus__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.provestatus__passiv = Slot(uri=UTD.passiv, name="provestatus__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.provestatus__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.skoleaar__kode = Slot(uri=UTD.kode, name="skoleaar__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.skoleaar__kode, domain=None, range=str)

slots.skoleaar__navn = Slot(uri=UTD.navn, name="skoleaar__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.skoleaar__navn, domain=None, range=str)

slots.skoleaar__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="skoleaar__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.skoleaar__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.skoleaar__passiv = Slot(uri=UTD.passiv, name="skoleaar__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.skoleaar__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.skoleeiertype__kode = Slot(uri=UTD.kode, name="skoleeiertype__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.skoleeiertype__kode, domain=None, range=str)

slots.skoleeiertype__navn = Slot(uri=UTD.navn, name="skoleeiertype__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.skoleeiertype__navn, domain=None, range=str)

slots.skoleeiertype__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="skoleeiertype__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.skoleeiertype__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.skoleeiertype__passiv = Slot(uri=UTD.passiv, name="skoleeiertype__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.skoleeiertype__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.termin__kode = Slot(uri=UTD.kode, name="termin__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.termin__kode, domain=None, range=str)

slots.termin__navn = Slot(uri=UTD.navn, name="termin__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.termin__navn, domain=None, range=str)

slots.termin__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="termin__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.termin__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.termin__passiv = Slot(uri=UTD.passiv, name="termin__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.termin__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.tilrettelegging__kode = Slot(uri=UTD.kode, name="tilrettelegging__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.tilrettelegging__kode, domain=None, range=str)

slots.tilrettelegging__navn = Slot(uri=UTD.navn, name="tilrettelegging__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.tilrettelegging__navn, domain=None, range=str)

slots.tilrettelegging__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="tilrettelegging__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.tilrettelegging__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.tilrettelegging__passiv = Slot(uri=UTD.passiv, name="tilrettelegging__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.tilrettelegging__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.varseltype__kode = Slot(uri=UTD.kode, name="varseltype__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.varseltype__kode, domain=None, range=str)

slots.varseltype__navn = Slot(uri=UTD.navn, name="varseltype__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.varseltype__navn, domain=None, range=str)

slots.varseltype__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="varseltype__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.varseltype__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.varseltype__passiv = Slot(uri=UTD.passiv, name="varseltype__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.varseltype__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.vitnemalsmerknad__kode = Slot(uri=UTD.kode, name="vitnemalsmerknad__kode", curie=UTD.curie('kode'),
                   model_uri=UTD.vitnemalsmerknad__kode, domain=None, range=str)

slots.vitnemalsmerknad__navn = Slot(uri=UTD.navn, name="vitnemalsmerknad__navn", curie=UTD.curie('navn'),
                   model_uri=UTD.vitnemalsmerknad__navn, domain=None, range=str)

slots.vitnemalsmerknad__gyldighetsperiode = Slot(uri=UTD.gyldighetsperiode, name="vitnemalsmerknad__gyldighetsperiode", curie=UTD.curie('gyldighetsperiode'),
                   model_uri=UTD.vitnemalsmerknad__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.vitnemalsmerknad__passiv = Slot(uri=UTD.passiv, name="vitnemalsmerknad__passiv", curie=UTD.curie('passiv'),
                   model_uri=UTD.vitnemalsmerknad__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.aktoer__kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="aktoer__kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=UTD.aktoer__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.aktoer__postadresse = Slot(uri=FINT.postadresse, name="aktoer__postadresse", curie=FINT.curie('postadresse'),
                   model_uri=UTD.aktoer__postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.begrep__kode = Slot(uri=FINT.kode, name="begrep__kode", curie=FINT.curie('kode'),
                   model_uri=UTD.begrep__kode, domain=None, range=str)

slots.begrep__navn = Slot(uri=FINT.navn, name="begrep__navn", curie=FINT.curie('navn'),
                   model_uri=UTD.begrep__navn, domain=None, range=str)

slots.begrep__gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="begrep__gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.begrep__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.begrep__passiv = Slot(uri=FINT.passiv, name="begrep__passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.begrep__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.enhet__forretningsadresse = Slot(uri=FINT.forretningsadresse, name="enhet__forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=UTD.enhet__forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.enhet__organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="enhet__organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=UTD.enhet__organisasjonsnavn, domain=None, range=Optional[str])

slots.enhet__organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="enhet__organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=UTD.enhet__organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.identifikator__identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="identifikator__identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=UTD.identifikator__identifikatorverdi, domain=None, range=str)

slots.identifikator__gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="identifikator__gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.identifikator__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.periode__beskrivelse = Slot(uri=FINT.beskrivelse, name="periode__beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=UTD.periode__beskrivelse, domain=None, range=Optional[str])

slots.periode__start = Slot(uri=FINT.start, name="periode__start", curie=FINT.curie('start'),
                   model_uri=UTD.periode__start, domain=None, range=Union[str, XSDDateTime])

slots.periode__slutt = Slot(uri=FINT.slutt, name="periode__slutt", curie=FINT.curie('slutt'),
                   model_uri=UTD.periode__slutt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.personnavn__fornavn = Slot(uri=FINT.fornavn, name="personnavn__fornavn", curie=FINT.curie('fornavn'),
                   model_uri=UTD.personnavn__fornavn, domain=None, range=str)

slots.personnavn__mellomnavn = Slot(uri=FINT.mellomnavn, name="personnavn__mellomnavn", curie=FINT.curie('mellomnavn'),
                   model_uri=UTD.personnavn__mellomnavn, domain=None, range=Optional[str])

slots.personnavn__etternavn = Slot(uri=FINT.etternavn, name="personnavn__etternavn", curie=FINT.curie('etternavn'),
                   model_uri=UTD.personnavn__etternavn, domain=None, range=str)

slots.kontaktinformasjon__epostadresse = Slot(uri=FINT.epostadresse, name="kontaktinformasjon__epostadresse", curie=FINT.curie('epostadresse'),
                   model_uri=UTD.kontaktinformasjon__epostadresse, domain=None, range=Optional[str])

slots.kontaktinformasjon__mobiltelefonnummer = Slot(uri=FINT.mobiltelefonnummer, name="kontaktinformasjon__mobiltelefonnummer", curie=FINT.curie('mobiltelefonnummer'),
                   model_uri=UTD.kontaktinformasjon__mobiltelefonnummer, domain=None, range=Optional[str])

slots.kontaktinformasjon__nettsted = Slot(uri=FINT.nettsted, name="kontaktinformasjon__nettsted", curie=FINT.curie('nettsted'),
                   model_uri=UTD.kontaktinformasjon__nettsted, domain=None, range=Optional[str])

slots.kontaktinformasjon__sip = Slot(uri=FINT.sip, name="kontaktinformasjon__sip", curie=FINT.curie('sip'),
                   model_uri=UTD.kontaktinformasjon__sip, domain=None, range=Optional[str])

slots.kontaktinformasjon__telefonnummer = Slot(uri=FINT.telefonnummer, name="kontaktinformasjon__telefonnummer", curie=FINT.curie('telefonnummer'),
                   model_uri=UTD.kontaktinformasjon__telefonnummer, domain=None, range=Optional[str])

slots.adresse__adresselinje = Slot(uri=FINT.adresselinje, name="adresse__adresselinje", curie=FINT.curie('adresselinje'),
                   model_uri=UTD.adresse__adresselinje, domain=None, range=Optional[Union[str, list[str]]])

slots.adresse__postnummer = Slot(uri=FINT.postnummer, name="adresse__postnummer", curie=FINT.curie('postnummer'),
                   model_uri=UTD.adresse__postnummer, domain=None, range=Optional[str])

slots.adresse__poststed = Slot(uri=FINT.poststed, name="adresse__poststed", curie=FINT.curie('poststed'),
                   model_uri=UTD.adresse__poststed, domain=None, range=Optional[str])

slots.adresse__land = Slot(uri=FINT.land, name="adresse__land", curie=FINT.curie('land'),
                   model_uri=UTD.adresse__land, domain=None, range=Optional[Union[str, LandkodeId]])

slots.matrikkelnummer__adresse = Slot(uri=FINT.adresse, name="matrikkelnummer__adresse", curie=FINT.curie('adresse'),
                   model_uri=UTD.matrikkelnummer__adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.matrikkelnummer__bruksnummer = Slot(uri=FINT.bruksnummer, name="matrikkelnummer__bruksnummer", curie=FINT.curie('bruksnummer'),
                   model_uri=UTD.matrikkelnummer__bruksnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__festenummer = Slot(uri=FINT.festenummer, name="matrikkelnummer__festenummer", curie=FINT.curie('festenummer'),
                   model_uri=UTD.matrikkelnummer__festenummer, domain=None, range=Optional[str])

slots.matrikkelnummer__gaardsnummer = Slot(uri=FINT.gaardsnummer, name="matrikkelnummer__gaardsnummer", curie=FINT.curie('gaardsnummer'),
                   model_uri=UTD.matrikkelnummer__gaardsnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__seksjonsnummer = Slot(uri=FINT.seksjonsnummer, name="matrikkelnummer__seksjonsnummer", curie=FINT.curie('seksjonsnummer'),
                   model_uri=UTD.matrikkelnummer__seksjonsnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__kommunenummer = Slot(uri=FINT.kommunenummer, name="matrikkelnummer__kommunenummer", curie=FINT.curie('kommunenummer'),
                   model_uri=UTD.matrikkelnummer__kommunenummer, domain=None, range=Optional[Union[str, KommuneId]])

slots.fylke__kommune = Slot(uri=FINT.kommune, name="fylke__kommune", curie=FINT.curie('kommune'),
                   model_uri=UTD.fylke__kommune, domain=None, range=Optional[Union[Union[str, KommuneId], list[Union[str, KommuneId]]]])

slots.kommune__fylke = Slot(uri=FINT.fylke, name="kommune__fylke", curie=FINT.curie('fylke'),
                   model_uri=UTD.kommune__fylke, domain=None, range=Union[str, FylkeId])

slots.valuta__bokstavkode = Slot(uri=FINT.bokstavkode, name="valuta__bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=UTD.valuta__bokstavkode, domain=None, range=Union[dict, Identifikator])

slots.valuta__navn = Slot(uri=FINT.valutaNavn, name="valuta__navn", curie=FINT.curie('valutaNavn'),
                   model_uri=UTD.valuta__navn, domain=None, range=str)

slots.valuta__nummerkode = Slot(uri=FINT.nummerkode, name="valuta__nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=UTD.valuta__nummerkode, domain=None, range=Union[dict, Identifikator])

slots.person__bilde = Slot(uri=FINT.bilde, name="person__bilde", curie=FINT.curie('bilde'),
                   model_uri=UTD.person__bilde, domain=None, range=Optional[str])

slots.person__bostedsadresse = Slot(uri=FINT.bostedsadresse, name="person__bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=UTD.person__bostedsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.person__fodselsdato = Slot(uri=FINT.fodselsdato, name="person__fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=UTD.person__fodselsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.person__fodselsnummer = Slot(uri=FINT.fodselsnummer, name="person__fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=UTD.person__fodselsnummer, domain=None, range=Union[dict, Identifikator])

slots.person__navn = Slot(uri=FINT.personNavn, name="person__navn", curie=FINT.curie('personNavn'),
                   model_uri=UTD.person__navn, domain=None, range=Union[dict, Personnavn])

slots.person__parorende = Slot(uri=FINT.parorende, name="person__parorende", curie=FINT.curie('parorende'),
                   model_uri=UTD.person__parorende, domain=None, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.person__statsborgerskap = Slot(uri=FINT.statsborgerskap, name="person__statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=UTD.person__statsborgerskap, domain=None, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.person__kommune = Slot(uri=FINT.kommune, name="person__kommune", curie=FINT.curie('kommune'),
                   model_uri=UTD.person__kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.person__kjonn = Slot(uri=FINT.kjonn, name="person__kjonn", curie=FINT.curie('kjonn'),
                   model_uri=UTD.person__kjonn, domain=None, range=Optional[Union[str, KjonnId]])

slots.person__foreldreansvar = Slot(uri=FINT.foreldreansvar, name="person__foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=UTD.person__foreldreansvar, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.person__foreldre = Slot(uri=FINT.foreldre, name="person__foreldre", curie=FINT.curie('foreldre'),
                   model_uri=UTD.person__foreldre, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.person__maalform = Slot(uri=FINT.maalform, name="person__maalform", curie=FINT.curie('maalform'),
                   model_uri=UTD.person__maalform, domain=None, range=Optional[Union[str, SpraakId]])

slots.person__personalressurs = Slot(uri=FINT.personalressurs, name="person__personalressurs", curie=FINT.curie('personalressurs'),
                   model_uri=UTD.person__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.person__morsmaal = Slot(uri=FINT.morsmaal, name="person__morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=UTD.person__morsmaal, domain=None, range=Optional[Union[str, SpraakId]])

slots.person__laerling = Slot(uri=FINT.laerling, name="person__laerling", curie=FINT.curie('laerling'),
                   model_uri=UTD.person__laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.person__elev = Slot(uri=FINT.elev, name="person__elev", curie=FINT.curie('elev'),
                   model_uri=UTD.person__elev, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.person__otungdom = Slot(uri=FINT.otungdom, name="person__otungdom", curie=FINT.curie('otungdom'),
                   model_uri=UTD.person__otungdom, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kontaktperson__kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="kontaktperson__kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=UTD.kontaktperson__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.kontaktperson__navn = Slot(uri=FINT.kontaktpersonNavn, name="kontaktperson__navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=UTD.kontaktperson__navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.kontaktperson__type = Slot(uri=FINT.type, name="kontaktperson__type", curie=FINT.curie('type'),
                   model_uri=UTD.kontaktperson__type, domain=None, range=str)

slots.kontaktperson__kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="kontaktperson__kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=UTD.kontaktperson__kontaktperson, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.virksomhet__virksomhetsId = Slot(uri=FINT.virksomhetsId, name="virksomhet__virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=UTD.virksomhet__virksomhetsId, domain=None, range=Union[dict, Identifikator])

slots.virksomhet__laerling = Slot(uri=FINT.laerling, name="virksomhet__laerling", curie=FINT.curie('laerling'),
                   model_uri=UTD.virksomhet__laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

