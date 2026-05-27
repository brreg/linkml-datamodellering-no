# Auto generated from fint-utdanning-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-27T14:51:45
# Schema: fint-utdanning
#
# id: https://data.norge.no/fint/fint-utdanning
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

metamodel_version = "1.11.0"
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
    elevforhold: Optional[Union[str, ElevforholdId]] = None
    elevtilrettelegging: Optional[Union[dict[Union[str, ElevtilretteleggingId], Union[dict, "Elevtilrettelegging"]], list[Union[dict, "Elevtilrettelegging"]]]] = empty_dict()
    klasser: Optional[Union[dict[Union[str, KlasseId], Union[dict, "Klasse"]], list[Union[dict, "Klasse"]]]] = empty_dict()
    klassemedlemskap: Optional[Union[Union[str, KlassemedlemskapId], list[Union[str, KlassemedlemskapId]]]] = empty_list()
    kontaktlaerergrupper: Optional[Union[dict[Union[str, KontaktlaerergruppeId], Union[dict, "Kontaktlaerergruppe"]], list[Union[dict, "Kontaktlaerergruppe"]]]] = empty_dict()
    kontaktlaerergruppemedlemskap: Optional[Union[Union[str, KontaktlaerergruppemedlemskapId], list[Union[str, KontaktlaerergruppemedlemskapId]]]] = empty_list()
    persongrupper: Optional[Union[dict[Union[str, PersongruppeId], Union[dict, "Persongruppe"]], list[Union[dict, "Persongruppe"]]]] = empty_dict()
    persongruppemedlemskap: Optional[Union[Union[str, PersongruppemedlemskapId], list[Union[str, PersongruppemedlemskapId]]]] = empty_list()
    varsel: Optional[Union[Union[str, VarselId], list[Union[str, VarselId]]]] = empty_list()
    arstrinn: Optional[Union[dict[Union[str, ArstrinnId], Union[dict, "Arstrinn"]], list[Union[dict, "Arstrinn"]]]] = empty_dict()
    programomrader: Optional[Union[dict[Union[str, ProgramomradeId], Union[dict, "Programomrade"]], list[Union[dict, "Programomrade"]]]] = empty_dict()
    programomrademedlemskap: Optional[Union[Union[str, ProgramomrademedlemskapId], list[Union[str, ProgramomrademedlemskapId]]]] = empty_list()
    utdanningsprogram: Optional[Union[Union[str, UtdanningsprogramId], list[Union[str, UtdanningsprogramId]]]] = empty_list()
    eksamen: Optional[Union[str, EksamenId]] = None
    fag: Optional[Union[str, FagId]] = None
    faggrupper: Optional[Union[dict[Union[str, FaggruppeId], Union[dict, "Faggruppe"]], list[Union[dict, "Faggruppe"]]]] = empty_dict()
    faggruppemedlemskap: Optional[Union[Union[str, FaggruppemedlemskapId], list[Union[str, FaggruppemedlemskapId]]]] = empty_list()
    rom: Optional[Union[str, RomId]] = None
    timar: Optional[Union[dict[Union[str, TimeId], Union[dict, "Time"]], list[Union[dict, "Time"]]]] = empty_dict()
    undervisningsforhold: Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]] = empty_list()
    undervisningsgrupper: Optional[Union[dict[Union[str, UndervisningsgruppeId], Union[dict, "Undervisningsgruppe"]], list[Union[dict, "Undervisningsgruppe"]]]] = empty_dict()
    undervisningsgruppemedlemskap: Optional[Union[Union[str, UndervisningsgruppemedlemskapId], list[Union[str, UndervisningsgruppemedlemskapId]]]] = empty_list()
    anmerkningar: Optional[Union[dict[Union[str, AnmerkningerId], Union[dict, "Anmerkninger"]], list[Union[dict, "Anmerkninger"]]]] = empty_dict()
    eksamensgrupper: Optional[Union[dict[Union[str, EksamensgruppeId], Union[dict, "Eksamensgruppe"]], list[Union[dict, "Eksamensgruppe"]]]] = empty_dict()
    eksamensgruppemedlemskap: Optional[Union[Union[str, EksamensgruppemedlemskapId], list[Union[str, EksamensgruppemedlemskapId]]]] = empty_list()
    eksamensvurdering: Optional[Union[Union[str, EksamensvurderingId], list[Union[str, EksamensvurderingId]]]] = empty_list()
    elevfravar: Optional[Union[str, ElevfravarId]] = None
    elevvurdering: Optional[Union[str, ElevvurderingId]] = None
    fravarsoversikt: Optional[Union[dict[Union[str, FravarsoversiktId], Union[dict, "Fravarsoversikt"]], list[Union[dict, "Fravarsoversikt"]]]] = empty_dict()
    fraversregistrering: Optional[Union[Union[str, FraversregistreringId], list[Union[str, FraversregistreringId]]]] = empty_list()
    halvaarsfagvurdering: Optional[Union[Union[str, HalvaarsfagvurderingId], list[Union[str, HalvaarsfagvurderingId]]]] = empty_list()
    halvaarsordensvurdering: Optional[Union[Union[str, HalvaarsordensvurderingId], list[Union[str, HalvaarsordensvurderingId]]]] = empty_list()
    karakterhistorie: Optional[Union[Union[str, KarakterhistorieId], list[Union[str, KarakterhistorieId]]]] = empty_list()
    sensor: Optional[Union[Union[str, SensorId], list[Union[str, SensorId]]]] = empty_list()
    sluttfagvurdering: Optional[Union[Union[str, SluttfagvurderingId], list[Union[str, SluttfagvurderingId]]]] = empty_list()
    sluttordensvurdering: Optional[Union[Union[str, SluttordensvurderingId], list[Union[str, SluttordensvurderingId]]]] = empty_list()
    underveisfagvurdering: Optional[Union[Union[str, UnderveisfagvurderingId], list[Union[str, UnderveisfagvurderingId]]]] = empty_list()
    underveisordensvurdering: Optional[Union[Union[str, UnderveisordensvurderingId], list[Union[str, UnderveisordensvurderingId]]]] = empty_list()
    vitnemalsmerknad: Optional[Union[str, VitnemalsmerknadId]] = None
    betalingsstatus: Optional[Union[str, BetalingsstatusId]] = None
    fagstatus: Optional[Union[str, FagstatusId]] = None
    karakterstatus: Optional[Union[str, KarakterstatusId]] = None
    skoleaar: Optional[Union[str, SkoleaarId]] = None
    tilrettelegging: Optional[Union[str, TilretteleggingId]] = None
    avlagteprover: Optional[Union[dict[Union[str, AvlagtProveId], Union[dict, "AvlagtProve"]], list[Union[dict, "AvlagtProve"]]]] = empty_dict()
    laerlingar: Optional[Union[dict[Union[str, LaerlingId], Union[dict, "Laerling"]], list[Union[dict, "Laerling"]]]] = empty_dict()
    otUngdom: Optional[Union[dict[Union[str, OtUngdomId], Union[dict, "OtUngdom"]], list[Union[dict, "OtUngdom"]]]] = empty_dict()
    avbruddsaarsaker: Optional[Union[dict[Union[str, AvbruddsaarsakId], Union[dict, "Avbruddsaarsak"]], list[Union[dict, "Avbruddsaarsak"]]]] = empty_dict()
    bevistypar: Optional[Union[dict[Union[str, BevistypeId], Union[dict, "Bevistype"]], list[Union[dict, "Bevistype"]]]] = empty_dict()
    brevtypar: Optional[Union[dict[Union[str, BrevtypeId], Union[dict, "Brevtype"]], list[Union[dict, "Brevtype"]]]] = empty_dict()
    eksamensformer: Optional[Union[dict[Union[str, EksamensformId], Union[dict, "Eksamensform"]], list[Union[dict, "Eksamensform"]]]] = empty_dict()
    elevkategoriar: Optional[Union[dict[Union[str, ElevkategoriId], Union[dict, "Elevkategori"]], list[Union[dict, "Elevkategori"]]]] = empty_dict()
    fagmerknader: Optional[Union[dict[Union[str, FagmerknadId], Union[dict, "Fagmerknad"]], list[Union[dict, "Fagmerknad"]]]] = empty_dict()
    fravartypar: Optional[Union[dict[Union[str, FravartypeId], Union[dict, "Fravartype"]], list[Union[dict, "Fravartype"]]]] = empty_dict()
    fullfortkoder: Optional[Union[dict[Union[str, FullfortkodeId], Union[dict, "Fullfortkode"]], list[Union[dict, "Fullfortkode"]]]] = empty_dict()
    karakterskalaer: Optional[Union[dict[Union[str, KarakterskalaId], Union[dict, "Karakterskala"]], list[Union[dict, "Karakterskala"]]]] = empty_dict()
    karakterverdiar: Optional[Union[dict[Union[str, KarakterverdiId], Union[dict, "Karakterverdi"]], list[Union[dict, "Karakterverdi"]]]] = empty_dict()
    otEnheter: Optional[Union[dict[Union[str, OtEnhetId], Union[dict, "OtEnhet"]], list[Union[dict, "OtEnhet"]]]] = empty_dict()
    otStatus: Optional[Union[dict[Union[str, OtStatusId], Union[dict, "OtStatus"]], list[Union[dict, "OtStatus"]]]] = empty_dict()
    provestatuser: Optional[Union[dict[Union[str, ProvestatusId], Union[dict, "Provestatus"]], list[Union[dict, "Provestatus"]]]] = empty_dict()
    skoleeijartypar: Optional[Union[dict[Union[str, SkoleeiertypeId], Union[dict, "Skoleeiertype"]], list[Union[dict, "Skoleeiertype"]]]] = empty_dict()
    terminar: Optional[Union[dict[Union[str, TerminId], Union[dict, "Termin"]], list[Union[dict, "Termin"]]]] = empty_dict()
    varseltypar: Optional[Union[dict[Union[str, VarseltypeId], Union[dict, "Varseltype"]], list[Union[dict, "Varseltype"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="elevar", slot_type=Elev, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="skolar", slot_type=Skole, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="skoleressursar", slot_type=Skoleressurs, key_name="id", keyed=True)

        if self.elevforhold is not None and not isinstance(self.elevforhold, ElevforholdId):
            self.elevforhold = ElevforholdId(self.elevforhold)

        self._normalize_inlined_as_list(slot_name="elevtilrettelegging", slot_type=Elevtilrettelegging, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="klasser", slot_type=Klasse, key_name="id", keyed=True)

        if not isinstance(self.klassemedlemskap, list):
            self.klassemedlemskap = [self.klassemedlemskap] if self.klassemedlemskap is not None else []
        self.klassemedlemskap = [v if isinstance(v, KlassemedlemskapId) else KlassemedlemskapId(v) for v in self.klassemedlemskap]

        self._normalize_inlined_as_list(slot_name="kontaktlaerergrupper", slot_type=Kontaktlaerergruppe, key_name="id", keyed=True)

        if not isinstance(self.kontaktlaerergruppemedlemskap, list):
            self.kontaktlaerergruppemedlemskap = [self.kontaktlaerergruppemedlemskap] if self.kontaktlaerergruppemedlemskap is not None else []
        self.kontaktlaerergruppemedlemskap = [v if isinstance(v, KontaktlaerergruppemedlemskapId) else KontaktlaerergruppemedlemskapId(v) for v in self.kontaktlaerergruppemedlemskap]

        self._normalize_inlined_as_list(slot_name="persongrupper", slot_type=Persongruppe, key_name="id", keyed=True)

        if not isinstance(self.persongruppemedlemskap, list):
            self.persongruppemedlemskap = [self.persongruppemedlemskap] if self.persongruppemedlemskap is not None else []
        self.persongruppemedlemskap = [v if isinstance(v, PersongruppemedlemskapId) else PersongruppemedlemskapId(v) for v in self.persongruppemedlemskap]

        if not isinstance(self.varsel, list):
            self.varsel = [self.varsel] if self.varsel is not None else []
        self.varsel = [v if isinstance(v, VarselId) else VarselId(v) for v in self.varsel]

        self._normalize_inlined_as_list(slot_name="arstrinn", slot_type=Arstrinn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="programomrader", slot_type=Programomrade, key_name="id", keyed=True)

        if not isinstance(self.programomrademedlemskap, list):
            self.programomrademedlemskap = [self.programomrademedlemskap] if self.programomrademedlemskap is not None else []
        self.programomrademedlemskap = [v if isinstance(v, ProgramomrademedlemskapId) else ProgramomrademedlemskapId(v) for v in self.programomrademedlemskap]

        if not isinstance(self.utdanningsprogram, list):
            self.utdanningsprogram = [self.utdanningsprogram] if self.utdanningsprogram is not None else []
        self.utdanningsprogram = [v if isinstance(v, UtdanningsprogramId) else UtdanningsprogramId(v) for v in self.utdanningsprogram]

        if self.eksamen is not None and not isinstance(self.eksamen, EksamenId):
            self.eksamen = EksamenId(self.eksamen)

        if self.fag is not None and not isinstance(self.fag, FagId):
            self.fag = FagId(self.fag)

        self._normalize_inlined_as_list(slot_name="faggrupper", slot_type=Faggruppe, key_name="id", keyed=True)

        if not isinstance(self.faggruppemedlemskap, list):
            self.faggruppemedlemskap = [self.faggruppemedlemskap] if self.faggruppemedlemskap is not None else []
        self.faggruppemedlemskap = [v if isinstance(v, FaggruppemedlemskapId) else FaggruppemedlemskapId(v) for v in self.faggruppemedlemskap]

        if self.rom is not None and not isinstance(self.rom, RomId):
            self.rom = RomId(self.rom)

        self._normalize_inlined_as_list(slot_name="timar", slot_type=Time, key_name="id", keyed=True)

        if not isinstance(self.undervisningsforhold, list):
            self.undervisningsforhold = [self.undervisningsforhold] if self.undervisningsforhold is not None else []
        self.undervisningsforhold = [v if isinstance(v, UndervisningsforholdId) else UndervisningsforholdId(v) for v in self.undervisningsforhold]

        self._normalize_inlined_as_list(slot_name="undervisningsgrupper", slot_type=Undervisningsgruppe, key_name="id", keyed=True)

        if not isinstance(self.undervisningsgruppemedlemskap, list):
            self.undervisningsgruppemedlemskap = [self.undervisningsgruppemedlemskap] if self.undervisningsgruppemedlemskap is not None else []
        self.undervisningsgruppemedlemskap = [v if isinstance(v, UndervisningsgruppemedlemskapId) else UndervisningsgruppemedlemskapId(v) for v in self.undervisningsgruppemedlemskap]

        self._normalize_inlined_as_list(slot_name="anmerkningar", slot_type=Anmerkninger, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="eksamensgrupper", slot_type=Eksamensgruppe, key_name="id", keyed=True)

        if not isinstance(self.eksamensgruppemedlemskap, list):
            self.eksamensgruppemedlemskap = [self.eksamensgruppemedlemskap] if self.eksamensgruppemedlemskap is not None else []
        self.eksamensgruppemedlemskap = [v if isinstance(v, EksamensgruppemedlemskapId) else EksamensgruppemedlemskapId(v) for v in self.eksamensgruppemedlemskap]

        if not isinstance(self.eksamensvurdering, list):
            self.eksamensvurdering = [self.eksamensvurdering] if self.eksamensvurdering is not None else []
        self.eksamensvurdering = [v if isinstance(v, EksamensvurderingId) else EksamensvurderingId(v) for v in self.eksamensvurdering]

        if self.elevfravar is not None and not isinstance(self.elevfravar, ElevfravarId):
            self.elevfravar = ElevfravarId(self.elevfravar)

        if self.elevvurdering is not None and not isinstance(self.elevvurdering, ElevvurderingId):
            self.elevvurdering = ElevvurderingId(self.elevvurdering)

        self._normalize_inlined_as_list(slot_name="fravarsoversikt", slot_type=Fravarsoversikt, key_name="id", keyed=True)

        if not isinstance(self.fraversregistrering, list):
            self.fraversregistrering = [self.fraversregistrering] if self.fraversregistrering is not None else []
        self.fraversregistrering = [v if isinstance(v, FraversregistreringId) else FraversregistreringId(v) for v in self.fraversregistrering]

        if not isinstance(self.halvaarsfagvurdering, list):
            self.halvaarsfagvurdering = [self.halvaarsfagvurdering] if self.halvaarsfagvurdering is not None else []
        self.halvaarsfagvurdering = [v if isinstance(v, HalvaarsfagvurderingId) else HalvaarsfagvurderingId(v) for v in self.halvaarsfagvurdering]

        if not isinstance(self.halvaarsordensvurdering, list):
            self.halvaarsordensvurdering = [self.halvaarsordensvurdering] if self.halvaarsordensvurdering is not None else []
        self.halvaarsordensvurdering = [v if isinstance(v, HalvaarsordensvurderingId) else HalvaarsordensvurderingId(v) for v in self.halvaarsordensvurdering]

        if not isinstance(self.karakterhistorie, list):
            self.karakterhistorie = [self.karakterhistorie] if self.karakterhistorie is not None else []
        self.karakterhistorie = [v if isinstance(v, KarakterhistorieId) else KarakterhistorieId(v) for v in self.karakterhistorie]

        if not isinstance(self.sensor, list):
            self.sensor = [self.sensor] if self.sensor is not None else []
        self.sensor = [v if isinstance(v, SensorId) else SensorId(v) for v in self.sensor]

        if not isinstance(self.sluttfagvurdering, list):
            self.sluttfagvurdering = [self.sluttfagvurdering] if self.sluttfagvurdering is not None else []
        self.sluttfagvurdering = [v if isinstance(v, SluttfagvurderingId) else SluttfagvurderingId(v) for v in self.sluttfagvurdering]

        if not isinstance(self.sluttordensvurdering, list):
            self.sluttordensvurdering = [self.sluttordensvurdering] if self.sluttordensvurdering is not None else []
        self.sluttordensvurdering = [v if isinstance(v, SluttordensvurderingId) else SluttordensvurderingId(v) for v in self.sluttordensvurdering]

        if not isinstance(self.underveisfagvurdering, list):
            self.underveisfagvurdering = [self.underveisfagvurdering] if self.underveisfagvurdering is not None else []
        self.underveisfagvurdering = [v if isinstance(v, UnderveisfagvurderingId) else UnderveisfagvurderingId(v) for v in self.underveisfagvurdering]

        if not isinstance(self.underveisordensvurdering, list):
            self.underveisordensvurdering = [self.underveisordensvurdering] if self.underveisordensvurdering is not None else []
        self.underveisordensvurdering = [v if isinstance(v, UnderveisordensvurderingId) else UnderveisordensvurderingId(v) for v in self.underveisordensvurdering]

        if self.vitnemalsmerknad is not None and not isinstance(self.vitnemalsmerknad, VitnemalsmerknadId):
            self.vitnemalsmerknad = VitnemalsmerknadId(self.vitnemalsmerknad)

        if self.betalingsstatus is not None and not isinstance(self.betalingsstatus, BetalingsstatusId):
            self.betalingsstatus = BetalingsstatusId(self.betalingsstatus)

        if self.fagstatus is not None and not isinstance(self.fagstatus, FagstatusId):
            self.fagstatus = FagstatusId(self.fagstatus)

        if self.karakterstatus is not None and not isinstance(self.karakterstatus, KarakterstatusId):
            self.karakterstatus = KarakterstatusId(self.karakterstatus)

        if self.skoleaar is not None and not isinstance(self.skoleaar, SkoleaarId):
            self.skoleaar = SkoleaarId(self.skoleaar)

        if self.tilrettelegging is not None and not isinstance(self.tilrettelegging, TilretteleggingId):
            self.tilrettelegging = TilretteleggingId(self.tilrettelegging)

        self._normalize_inlined_as_list(slot_name="avlagteprover", slot_type=AvlagtProve, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="laerlingar", slot_type=Laerling, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="otUngdom", slot_type=OtUngdom, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="avbruddsaarsaker", slot_type=Avbruddsaarsak, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="bevistypar", slot_type=Bevistype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="brevtypar", slot_type=Brevtype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="eksamensformer", slot_type=Eksamensform, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="elevkategoriar", slot_type=Elevkategori, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fagmerknader", slot_type=Fagmerknad, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fravartypar", slot_type=Fravartype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fullfortkoder", slot_type=Fullfortkode, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="karakterskalaer", slot_type=Karakterskala, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="karakterverdiar", slot_type=Karakterverdi, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="otEnheter", slot_type=OtEnhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="otStatus", slot_type=OtStatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="provestatuser", slot_type=Provestatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="skoleeijartypar", slot_type=Skoleeiertype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="terminar", slot_type=Termin, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="varseltypar", slot_type=Varseltype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="elevforhold", slot_type=Elevforhold, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="eksamen", slot_type=Eksamen, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fag", slot_type=Fag, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rom", slot_type=Rom, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="elevfravar", slot_type=Elevfravar, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="elevvurdering", slot_type=Elevvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="vitnemalsmerknad", slot_type=Vitnemalsmerknad, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="betalingsstatus", slot_type=Betalingsstatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fagstatus", slot_type=Fagstatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="karakterstatus", slot_type=Karakterstatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="skoleaar", slot_type=Skoleaar, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tilrettelegging", slot_type=Tilrettelegging, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="klassemedlemskap", slot_type=Klassemedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kontaktlaerergruppemedlemskap", slot_type=Kontaktlaerergruppemedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="persongruppemedlemskap", slot_type=Persongruppemedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="programomrademedlemskap", slot_type=Programomrademedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="undervisningsgruppemedlemskap", slot_type=Undervisningsgruppemedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="eksamensgruppemedlemskap", slot_type=Eksamensgruppemedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="faggruppemedlemskap", slot_type=Faggruppemedlemskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="utdanningsprogram", slot_type=Utdanningsprogram, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="undervisningsforhold", slot_type=Undervisningsforhold, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="varsel", slot_type=Varsel, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="karakterhistorie", slot_type=Karakterhistorie, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sensor", slot_type=Sensor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fraversregistrering", slot_type=Fraversregistrering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="halvaarsfagvurdering", slot_type=Halvaarsfagvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="halvaarsordensvurdering", slot_type=Halvaarsordensvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sluttfagvurdering", slot_type=Sluttfagvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sluttordensvurdering", slot_type=Sluttordensvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="underveisfagvurdering", slot_type=Underveisfagvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="underveisordensvurdering", slot_type=Underveisordensvurdering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="eksamensvurdering", slot_type=Eksamensvurdering, key_name="id", keyed=True)

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
    person: Optional[Union[str, PersonId]] = None
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

        if self.person is not None and not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

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
    faggruppemedlemskap: Optional[Union[Union[str, FaggruppemedlemskapId], list[Union[str, FaggruppemedlemskapId]]]] = empty_list()

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

        if not isinstance(self.faggruppemedlemskap, list):
            self.faggruppemedlemskap = [self.faggruppemedlemskap] if self.faggruppemedlemskap is not None else []
        self.faggruppemedlemskap = [v if isinstance(v, FaggruppemedlemskapId) else FaggruppemedlemskapId(v) for v in self.faggruppemedlemskap]

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
    skuletime: Optional[Union[Union[str, TimeId], list[Union[str, TimeId]]]] = empty_list()

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

        if not isinstance(self.skuletime, list):
            self.skuletime = [self.skuletime] if self.skuletime is not None else []
        self.skuletime = [v if isinstance(v, TimeId) else TimeId(v) for v in self.skuletime]

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
    skuletime: Optional[Union[Union[str, TimeId], list[Union[str, TimeId]]]] = empty_list()
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

        if not isinstance(self.skuletime, list):
            self.skuletime = [self.skuletime] if self.skuletime is not None else []
        self.skuletime = [v if isinstance(v, TimeId) else TimeId(v) for v in self.skuletime]

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
    skuletime: Optional[Union[Union[str, TimeId], list[Union[str, TimeId]]]] = empty_list()
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

        if not isinstance(self.skuletime, list):
            self.skuletime = [self.skuletime] if self.skuletime is not None else []
        self.skuletime = [v if isinstance(v, TimeId) else TimeId(v) for v in self.skuletime]

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
    fravartype: Union[str, FravartypeId] = None
    kommentar: Optional[str] = None
    registrertAv: Optional[Union[str, SkoleressursId]] = None
    faggruppe: Optional[Union[str, FaggruppeId]] = None
    elevfravar: Optional[Union[str, ElevfravarId]] = None

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

        if self.elevfravar is not None and not isinstance(self.elevfravar, ElevfravarId):
            self.elevfravar = ElevfravarId(self.elevfravar)

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
    laerling: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
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
        if not isinstance(self.laerling, list):
            self.laerling = [self.laerling] if self.laerling is not None else []
        self.laerling = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.laerling]

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
    person: Union[str, PersonId] = None
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
        if not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

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
    person: Union[str, PersonId] = None
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
        if not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

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
    kommune: Union[str, KommuneId] = None
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
        if not isinstance(self.kommune, KommuneId):
            self.kommune = KommuneId(self.kommune)

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
class Elev(YAMLRoot):
    """
    Ein elev registrert i skulesystemet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Elev"]
    class_class_curie: ClassVar[str] = "fint:Elev"
    class_name: ClassVar[str] = "Elev"
    class_model_uri: ClassVar[URIRef] = UTD.Elev

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
    class_model_uri: ClassVar[URIRef] = UTD.Person

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
    class_model_uri: ClassVar[URIRef] = UTD.Kontaktperson

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

slots.elevforhold = Slot(uri=UTD.elevforhold, name="elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.elevforhold, domain=None, range=Optional[Union[str, ElevforholdId]])

slots.klassemedlemskap = Slot(uri=UTD.klassemedlemskap, name="klassemedlemskap", curie=UTD.curie('klassemedlemskap'),
                   model_uri=UTD.klassemedlemskap, domain=None, range=Optional[Union[Union[str, KlassemedlemskapId], list[Union[str, KlassemedlemskapId]]]])

slots.kontaktlaerergruppemedlemskap = Slot(uri=UTD.kontaktlaerergruppemedlemskap, name="kontaktlaerergruppemedlemskap", curie=UTD.curie('kontaktlaerergruppemedlemskap'),
                   model_uri=UTD.kontaktlaerergruppemedlemskap, domain=None, range=Optional[Union[Union[str, KontaktlaerergruppemedlemskapId], list[Union[str, KontaktlaerergruppemedlemskapId]]]])

slots.persongruppemedlemskap = Slot(uri=UTD.persongruppemedlemskap, name="persongruppemedlemskap", curie=UTD.curie('persongruppemedlemskap'),
                   model_uri=UTD.persongruppemedlemskap, domain=None, range=Optional[Union[Union[str, PersongruppemedlemskapId], list[Union[str, PersongruppemedlemskapId]]]])

slots.programomrademedlemskap = Slot(uri=UTD.programomrademedlemskap, name="programomrademedlemskap", curie=UTD.curie('programomrademedlemskap'),
                   model_uri=UTD.programomrademedlemskap, domain=None, range=Optional[Union[Union[str, ProgramomrademedlemskapId], list[Union[str, ProgramomrademedlemskapId]]]])

slots.undervisningsgruppemedlemskap = Slot(uri=UTD.undervisningsgruppemedlemskap, name="undervisningsgruppemedlemskap", curie=UTD.curie('undervisningsgruppemedlemskap'),
                   model_uri=UTD.undervisningsgruppemedlemskap, domain=None, range=Optional[Union[Union[str, UndervisningsgruppemedlemskapId], list[Union[str, UndervisningsgruppemedlemskapId]]]])

slots.eksamensgruppemedlemskap = Slot(uri=UTD.eksamensgruppemedlemskap, name="eksamensgruppemedlemskap", curie=UTD.curie('eksamensgruppemedlemskap'),
                   model_uri=UTD.eksamensgruppemedlemskap, domain=None, range=Optional[Union[Union[str, EksamensgruppemedlemskapId], list[Union[str, EksamensgruppemedlemskapId]]]])

slots.faggruppemedlemskap = Slot(uri=UTD.faggruppemedlemskap, name="faggruppemedlemskap", curie=UTD.curie('faggruppemedlemskap'),
                   model_uri=UTD.faggruppemedlemskap, domain=None, range=Optional[Union[Union[str, FaggruppemedlemskapId], list[Union[str, FaggruppemedlemskapId]]]])

slots.utdanningsprogram = Slot(uri=UTD.utdanningsprogram, name="utdanningsprogram", curie=UTD.curie('utdanningsprogram'),
                   model_uri=UTD.utdanningsprogram, domain=None, range=Optional[Union[Union[str, UtdanningsprogramId], list[Union[str, UtdanningsprogramId]]]])

slots.eksamen = Slot(uri=UTD.eksamen, name="eksamen", curie=UTD.curie('eksamen'),
                   model_uri=UTD.eksamen, domain=None, range=Optional[Union[str, EksamenId]])

slots.fag = Slot(uri=UTD.fag, name="fag", curie=UTD.curie('fag'),
                   model_uri=UTD.fag, domain=None, range=Optional[Union[str, FagId]])

slots.rom = Slot(uri=UTD.rom, name="rom", curie=UTD.curie('rom'),
                   model_uri=UTD.rom, domain=None, range=Optional[Union[str, RomId]])

slots.undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.undervisningsforhold, domain=None, range=Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]])

slots.varsel = Slot(uri=UTD.varsel, name="varsel", curie=UTD.curie('varsel'),
                   model_uri=UTD.varsel, domain=None, range=Optional[Union[Union[str, VarselId], list[Union[str, VarselId]]]])

slots.karakterhistorie = Slot(uri=UTD.karakterhistorie, name="karakterhistorie", curie=UTD.curie('karakterhistorie'),
                   model_uri=UTD.karakterhistorie, domain=None, range=Optional[Union[Union[str, KarakterhistorieId], list[Union[str, KarakterhistorieId]]]])

slots.sensor = Slot(uri=UTD.sensor, name="sensor", curie=UTD.curie('sensor'),
                   model_uri=UTD.sensor, domain=None, range=Optional[Union[Union[str, SensorId], list[Union[str, SensorId]]]])

slots.elevfravar = Slot(uri=UTD.elevfravar, name="elevfravar", curie=UTD.curie('elevfravar'),
                   model_uri=UTD.elevfravar, domain=None, range=Optional[Union[str, ElevfravarId]])

slots.elevvurdering = Slot(uri=UTD.elevvurdering, name="elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.elevvurdering, domain=None, range=Optional[Union[str, ElevvurderingId]])

slots.fraversregistrering = Slot(uri=UTD.fraversregistrering, name="fraversregistrering", curie=UTD.curie('fraversregistrering'),
                   model_uri=UTD.fraversregistrering, domain=None, range=Optional[Union[Union[str, FraversregistreringId], list[Union[str, FraversregistreringId]]]])

slots.halvaarsfagvurdering = Slot(uri=UTD.halvaarsfagvurdering, name="halvaarsfagvurdering", curie=UTD.curie('halvaarsfagvurdering'),
                   model_uri=UTD.halvaarsfagvurdering, domain=None, range=Optional[Union[Union[str, HalvaarsfagvurderingId], list[Union[str, HalvaarsfagvurderingId]]]])

slots.halvaarsordensvurdering = Slot(uri=UTD.halvaarsordensvurdering, name="halvaarsordensvurdering", curie=UTD.curie('halvaarsordensvurdering'),
                   model_uri=UTD.halvaarsordensvurdering, domain=None, range=Optional[Union[Union[str, HalvaarsordensvurderingId], list[Union[str, HalvaarsordensvurderingId]]]])

slots.sluttfagvurdering = Slot(uri=UTD.sluttfagvurdering, name="sluttfagvurdering", curie=UTD.curie('sluttfagvurdering'),
                   model_uri=UTD.sluttfagvurdering, domain=None, range=Optional[Union[Union[str, SluttfagvurderingId], list[Union[str, SluttfagvurderingId]]]])

slots.sluttordensvurdering = Slot(uri=UTD.sluttordensvurdering, name="sluttordensvurdering", curie=UTD.curie('sluttordensvurdering'),
                   model_uri=UTD.sluttordensvurdering, domain=None, range=Optional[Union[Union[str, SluttordensvurderingId], list[Union[str, SluttordensvurderingId]]]])

slots.underveisfagvurdering = Slot(uri=UTD.underveisfagvurdering, name="underveisfagvurdering", curie=UTD.curie('underveisfagvurdering'),
                   model_uri=UTD.underveisfagvurdering, domain=None, range=Optional[Union[Union[str, UnderveisfagvurderingId], list[Union[str, UnderveisfagvurderingId]]]])

slots.underveisordensvurdering = Slot(uri=UTD.underveisordensvurdering, name="underveisordensvurdering", curie=UTD.curie('underveisordensvurdering'),
                   model_uri=UTD.underveisordensvurdering, domain=None, range=Optional[Union[Union[str, UnderveisordensvurderingId], list[Union[str, UnderveisordensvurderingId]]]])

slots.eksamensvurdering = Slot(uri=UTD.eksamensvurdering, name="eksamensvurdering", curie=UTD.curie('eksamensvurdering'),
                   model_uri=UTD.eksamensvurdering, domain=None, range=Optional[Union[Union[str, EksamensvurderingId], list[Union[str, EksamensvurderingId]]]])

slots.vitnemalsmerknad = Slot(uri=UTD.vitnemalsmerknad, name="vitnemalsmerknad", curie=UTD.curie('vitnemalsmerknad'),
                   model_uri=UTD.vitnemalsmerknad, domain=None, range=Optional[Union[str, VitnemalsmerknadId]])

slots.betalingsstatus = Slot(uri=UTD.betalingsstatus, name="betalingsstatus", curie=UTD.curie('betalingsstatus'),
                   model_uri=UTD.betalingsstatus, domain=None, range=Optional[Union[str, BetalingsstatusId]])

slots.fagstatus = Slot(uri=UTD.fagstatus, name="fagstatus", curie=UTD.curie('fagstatus'),
                   model_uri=UTD.fagstatus, domain=None, range=Optional[Union[str, FagstatusId]])

slots.karakterstatus = Slot(uri=UTD.karakterstatus, name="karakterstatus", curie=UTD.curie('karakterstatus'),
                   model_uri=UTD.karakterstatus, domain=None, range=Optional[Union[str, KarakterstatusId]])

slots.skoleaar = Slot(uri=UTD.skoleaar, name="skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.skoleaar, domain=None, range=Optional[Union[str, SkoleaarId]])

slots.tilrettelegging = Slot(uri=UTD.tilrettelegging, name="tilrettelegging", curie=UTD.curie('tilrettelegging'),
                   model_uri=UTD.tilrettelegging, domain=None, range=Optional[Union[str, TilretteleggingId]])

slots.avbruddsdato = Slot(uri=UTD.avbruddsdato, name="avbruddsdato", curie=UTD.curie('avbruddsdato'),
                   model_uri=UTD.avbruddsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.tosprakligFagopplaering = Slot(uri=UTD.tosprakligFagopplaering, name="tosprakligFagopplaering", curie=UTD.curie('tosprakligFagopplaering'),
                   model_uri=UTD.tosprakligFagopplaering, domain=None, range=Optional[Union[bool, Bool]])

slots.kategori = Slot(uri=UTD.kategori, name="kategori", curie=UTD.curie('kategori'),
                   model_uri=UTD.kategori, domain=None, range=Optional[Union[str, ElevkategoriId]])

slots.avbruddsarsak = Slot(uri=UTD.avbruddsarsak, name="avbruddsarsak", curie=UTD.curie('avbruddsarsak'),
                   model_uri=UTD.avbruddsarsak, domain=None, range=Optional[Union[str, AvbruddsaarsakId]])

slots.fraversregistreringer = Slot(uri=UTD.fraversregistreringer, name="fraversregistreringer", curie=UTD.curie('fraversregistreringer'),
                   model_uri=UTD.fraversregistreringer, domain=None, range=Optional[Union[Union[str, ElevfravarId], list[Union[str, ElevfravarId]]]])

slots.domenenavn = Slot(uri=UTD.domenenavn, name="domenenavn", curie=UTD.curie('domenenavn'),
                   model_uri=UTD.domenenavn, domain=None, range=Optional[str])

slots.juridiskNavn = Slot(uri=UTD.juridiskNavn, name="juridiskNavn", curie=UTD.curie('juridiskNavn'),
                   model_uri=UTD.juridiskNavn, domain=None, range=Optional[str])

slots.skolenummer = Slot(uri=UTD.skolenummer, name="skolenummer", curie=UTD.curie('skolenummer'),
                   model_uri=UTD.skolenummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.organisasjon = Slot(uri=UTD.organisasjon, name="organisasjon", curie=UTD.curie('organisasjon'),
                   model_uri=UTD.organisasjon, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.skole = Slot(uri=UTD.skole, name="skole", curie=UTD.curie('skole'),
                   model_uri=UTD.skole, domain=None, range=Optional[Union[str, SkoleId]])

slots.kontaktlaerergruppe = Slot(uri=UTD.kontaktlaerergruppe, name="kontaktlaerergruppe", curie=UTD.curie('kontaktlaerergruppe'),
                   model_uri=UTD.kontaktlaerergruppe, domain=None, range=Optional[Union[str, KontaktlaerergruppeId]])

slots.faggruppe = Slot(uri=UTD.faggruppe, name="faggruppe", curie=UTD.curie('faggruppe'),
                   model_uri=UTD.faggruppe, domain=None, range=Optional[Union[str, FaggruppeId]])

slots.skoleeierType = Slot(uri=UTD.skoleeierType, name="skoleeierType", curie=UTD.curie('skoleeierType'),
                   model_uri=UTD.skoleeierType, domain=None, range=Optional[Union[str, SkoleeiertypeId]])

slots.vigoreferanse = Slot(uri=UTD.vigoreferanse, name="vigoreferanse", curie=UTD.curie('vigoreferanse'),
                   model_uri=UTD.vigoreferanse, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.eksamensgruppe, domain=None, range=Optional[Union[str, EksamensgruppeId]])

slots.feidenavn = Slot(uri=UTD.feidenavn, name="feidenavn", curie=UTD.curie('feidenavn'),
                   model_uri=UTD.feidenavn, domain=None, range=Optional[Union[dict, Identifikator]])

slots.personalressurs = Slot(uri=UTD.personalressurs, name="personalressurs", curie=UTD.curie('personalressurs'),
                   model_uri=UTD.personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.skoleressurs = Slot(uri=UTD.skoleressurs, name="skoleressurs", curie=UTD.curie('skoleressurs'),
                   model_uri=UTD.skoleressurs, domain=None, range=Optional[Union[str, SkoleressursId]])

slots.fravarsprosent = Slot(uri=UTD.fravarsprosent, name="fravarsprosent", curie=UTD.curie('fravarsprosent'),
                   model_uri=UTD.fravarsprosent, domain=None, range=Optional[int])

slots.sendt = Slot(uri=UTD.sendt, name="sendt", curie=UTD.curie('sendt'),
                   model_uri=UTD.sendt, domain=None, range=Optional[Union[str, XSDDate]])

slots.tekst = Slot(uri=UTD.tekst, name="tekst", curie=UTD.curie('tekst'),
                   model_uri=UTD.tekst, domain=None, range=Optional[str])

slots.utsteder = Slot(uri=UTD.utsteder, name="utsteder", curie=UTD.curie('utsteder'),
                   model_uri=UTD.utsteder, domain=None, range=Optional[Union[str, SkoleressursId]])

slots.karakteransvarlig = Slot(uri=UTD.karakteransvarlig, name="karakteransvarlig", curie=UTD.curie('karakteransvarlig'),
                   model_uri=UTD.karakteransvarlig, domain=None, range=Optional[Union[str, SkoleressursId]])

slots.klasse = Slot(uri=UTD.klasse, name="klasse", curie=UTD.curie('klasse'),
                   model_uri=UTD.klasse, domain=None, range=Optional[Union[str, KlasseId]])

slots.termin = Slot(uri=UTD.termin, name="termin", curie=UTD.curie('termin'),
                   model_uri=UTD.termin, domain=None, range=Optional[Union[str, TerminId]])

slots.trinn = Slot(uri=UTD.trinn, name="trinn", curie=UTD.curie('trinn'),
                   model_uri=UTD.trinn, domain=None, range=Optional[Union[Union[str, ArstrinnId], list[Union[str, ArstrinnId]]]])

slots.gruppemedlemskap = Slot(uri=UTD.gruppemedlemskap, name="gruppemedlemskap", curie=UTD.curie('gruppemedlemskap'),
                   model_uri=UTD.gruppemedlemskap, domain=None, range=Optional[Union[Union[str, GruppemedlemskapId], list[Union[str, GruppemedlemskapId]]]])

slots.persongruppe = Slot(uri=UTD.persongruppe, name="persongruppe", curie=UTD.curie('persongruppe'),
                   model_uri=UTD.persongruppe, domain=None, range=Optional[Union[str, PersongruppeId]])

slots.programomrade = Slot(uri=UTD.programomrade, name="programomrade", curie=UTD.curie('programomrade'),
                   model_uri=UTD.programomrade, domain=None, range=Optional[Union[str, ProgramomradeId]])

slots.grepreferanse = Slot(uri=UTD.grepreferanse, name="grepreferanse", curie=UTD.curie('grepreferanse'),
                   model_uri=UTD.grepreferanse, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.oppmoetetidspunkt = Slot(uri=UTD.oppmoetetidspunkt, name="oppmoetetidspunkt", curie=UTD.curie('oppmoetetidspunkt'),
                   model_uri=UTD.oppmoetetidspunkt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.tidsrom = Slot(uri=UTD.tidsrom, name="tidsrom", curie=UTD.curie('tidsrom'),
                   model_uri=UTD.tidsrom, domain=None, range=Optional[Union[dict, Periode]])

slots.arbeidsforhold = Slot(uri=UTD.arbeidsforhold, name="arbeidsforhold", curie=UTD.curie('arbeidsforhold'),
                   model_uri=UTD.arbeidsforhold, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.skuletime = Slot(uri=UTD.skuletime, name="skuletime", curie=UTD.curie('skuletime'),
                   model_uri=UTD.skuletime, domain=None, range=Optional[Union[Union[str, TimeId], list[Union[str, TimeId]]]])

slots.undervisningsgruppe = Slot(uri=UTD.undervisningsgruppe, name="undervisningsgruppe", curie=UTD.curie('undervisningsgruppe'),
                   model_uri=UTD.undervisningsgruppe, domain=None, range=Optional[Union[str, UndervisningsgruppeId]])

slots.kommentar = Slot(uri=UTD.kommentar, name="kommentar", curie=UTD.curie('kommentar'),
                   model_uri=UTD.kommentar, domain=None, range=Optional[str])

slots.vurderingsdato = Slot(uri=UTD.vurderingsdato, name="vurderingsdato", curie=UTD.curie('vurderingsdato'),
                   model_uri=UTD.vurderingsdato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.karakter = Slot(uri=UTD.karakter, name="karakter", curie=UTD.curie('karakter'),
                   model_uri=UTD.karakter, domain=None, range=Optional[Union[str, KarakterverdiId]])

slots.atferd = Slot(uri=UTD.atferd, name="atferd", curie=UTD.curie('atferd'),
                   model_uri=UTD.atferd, domain=None, range=Optional[Union[str, KarakterverdiId]])

slots.orden = Slot(uri=UTD.orden, name="orden", curie=UTD.curie('orden'),
                   model_uri=UTD.orden, domain=None, range=Optional[Union[str, KarakterverdiId]])

slots.delegert = Slot(uri=UTD.delegert, name="delegert", curie=UTD.curie('delegert'),
                   model_uri=UTD.delegert, domain=None, range=Optional[Union[bool, Bool]])

slots.kandidatnummer = Slot(uri=UTD.kandidatnummer, name="kandidatnummer", curie=UTD.curie('kandidatnummer'),
                   model_uri=UTD.kandidatnummer, domain=None, range=Optional[str])

slots.delegertTil = Slot(uri=UTD.delegertTil, name="delegertTil", curie=UTD.curie('delegertTil'),
                   model_uri=UTD.delegertTil, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.foretrukketSkole = Slot(uri=UTD.foretrukketSkole, name="foretrukketSkole", curie=UTD.curie('foretrukketSkole'),
                   model_uri=UTD.foretrukketSkole, domain=None, range=Optional[Union[bool, Bool]])

slots.foretrukketSensor = Slot(uri=UTD.foretrukketSensor, name="foretrukketSensor", curie=UTD.curie('foretrukketSensor'),
                   model_uri=UTD.foretrukketSensor, domain=None, range=Optional[Union[bool, Bool]])

slots.nus = Slot(uri=UTD.nus, name="nus", curie=UTD.curie('nus'),
                   model_uri=UTD.nus, domain=None, range=Optional[Union[str, KarakterstatusId]])

slots.halvaar = Slot(uri=UTD.halvaar, name="halvaar", curie=UTD.curie('halvaar'),
                   model_uri=UTD.halvaar, domain=None, range=Optional[Union[dict, Fravarsprosent]])

slots.skoleaarFravar = Slot(uri=UTD.skoleaarFravar, name="skoleaarFravar", curie=UTD.curie('skoleaarFravar'),
                   model_uri=UTD.skoleaarFravar, domain=None, range=Optional[Union[dict, Fravarsprosent]])

slots.fravaerstimer = Slot(uri=UTD.fravaerstimer, name="fravaerstimer", curie=UTD.curie('fravaerstimer'),
                   model_uri=UTD.fravaerstimer, domain=None, range=Optional[int])

slots.prosent = Slot(uri=UTD.prosent, name="prosent", curie=UTD.curie('prosent'),
                   model_uri=UTD.prosent, domain=None, range=Optional[int])

slots.undervisningstimer = Slot(uri=UTD.undervisningstimer, name="undervisningstimer", curie=UTD.curie('undervisningstimer'),
                   model_uri=UTD.undervisningstimer, domain=None, range=Optional[int])

slots.forersPaaVitnemaal = Slot(uri=UTD.forersPaaVitnemaal, name="forersPaaVitnemaal", curie=UTD.curie('forersPaaVitnemaal'),
                   model_uri=UTD.forersPaaVitnemaal, domain=None, range=Optional[Union[bool, Bool]])

slots.periode = Slot(uri=UTD.periode, name="periode", curie=UTD.curie('periode'),
                   model_uri=UTD.periode, domain=None, range=Optional[Union[dict, Periode]])

slots.registrertAv = Slot(uri=UTD.registrertAv, name="registrertAv", curie=UTD.curie('registrertAv'),
                   model_uri=UTD.registrertAv, domain=None, range=Optional[Union[str, SkoleressursId]])

slots.fravartype = Slot(uri=UTD.fravartype, name="fravartype", curie=UTD.curie('fravartype'),
                   model_uri=UTD.fravartype, domain=None, range=Optional[Union[str, FravartypeId]])

slots.endretDato = Slot(uri=UTD.endretDato, name="endretDato", curie=UTD.curie('endretDato'),
                   model_uri=UTD.endretDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.oppdatertAv = Slot(uri=UTD.oppdatertAv, name="oppdatertAv", curie=UTD.curie('oppdatertAv'),
                   model_uri=UTD.oppdatertAv, domain=None, range=Optional[Union[str, SkoleressursId]])

slots.opprinneligKarakterverdi = Slot(uri=UTD.opprinneligKarakterverdi, name="opprinneligKarakterverdi", curie=UTD.curie('opprinneligKarakterverdi'),
                   model_uri=UTD.opprinneligKarakterverdi, domain=None, range=Optional[Union[str, KarakterverdiId]])

slots.opprinneligKarakterstatus = Slot(uri=UTD.opprinneligKarakterstatus, name="opprinneligKarakterstatus", curie=UTD.curie('opprinneligKarakterstatus'),
                   model_uri=UTD.opprinneligKarakterstatus, domain=None, range=Optional[Union[str, KarakterstatusId]])

slots.karakterverdi = Slot(uri=UTD.karakterverdi, name="karakterverdi", curie=UTD.curie('karakterverdi'),
                   model_uri=UTD.karakterverdi, domain=None, range=Optional[Union[str, KarakterverdiId]])

slots.aktiv = Slot(uri=UTD.aktiv, name="aktiv", curie=UTD.curie('aktiv'),
                   model_uri=UTD.aktiv, domain=None, range=Optional[Union[bool, Bool]])

slots.sensornummer = Slot(uri=UTD.sensornummer, name="sensornummer", curie=UTD.curie('sensornummer'),
                   model_uri=UTD.sensornummer, domain=None, range=Optional[int])

slots.eksamensdato = Slot(uri=UTD.eksamensdato, name="eksamensdato", curie=UTD.curie('eksamensdato'),
                   model_uri=UTD.eksamensdato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.eksamensform = Slot(uri=UTD.eksamensform, name="eksamensform", curie=UTD.curie('eksamensform'),
                   model_uri=UTD.eksamensform, domain=None, range=Optional[Union[str, EksamensformId]])

slots.provedato = Slot(uri=UTD.provedato, name="provedato", curie=UTD.curie('provedato'),
                   model_uri=UTD.provedato, domain=None, range=Optional[Union[str, XSDDate]])

slots.provestatus = Slot(uri=UTD.provestatus, name="provestatus", curie=UTD.curie('provestatus'),
                   model_uri=UTD.provestatus, domain=None, range=Optional[Union[str, ProvestatusId]])

slots.fullfortkode = Slot(uri=UTD.fullfortkode, name="fullfortkode", curie=UTD.curie('fullfortkode'),
                   model_uri=UTD.fullfortkode, domain=None, range=Optional[Union[str, FullfortkodeId]])

slots.brevtype = Slot(uri=UTD.brevtype, name="brevtype", curie=UTD.curie('brevtype'),
                   model_uri=UTD.brevtype, domain=None, range=Optional[Union[str, BrevtypeId]])

slots.bevistype = Slot(uri=UTD.bevistype, name="bevistype", curie=UTD.curie('bevistype'),
                   model_uri=UTD.bevistype, domain=None, range=Optional[Union[str, BevistypeId]])

slots.kontraktstype = Slot(uri=UTD.kontraktstype, name="kontraktstype", curie=UTD.curie('kontraktstype'),
                   model_uri=UTD.kontraktstype, domain=None, range=Optional[str])

slots.laretid = Slot(uri=UTD.laretid, name="laretid", curie=UTD.curie('laretid'),
                   model_uri=UTD.laretid, domain=None, range=Optional[Union[dict, Periode]])

slots.bedrift = Slot(uri=UTD.bedrift, name="bedrift", curie=UTD.curie('bedrift'),
                   model_uri=UTD.bedrift, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.avlagtprove = Slot(uri=UTD.avlagtprove, name="avlagtprove", curie=UTD.curie('avlagtprove'),
                   model_uri=UTD.avlagtprove, domain=None, range=Optional[Union[Union[str, AvlagtProveId], list[Union[str, AvlagtProveId]]]])

slots.status = Slot(uri=UTD.status, name="status", curie=UTD.curie('status'),
                   model_uri=UTD.status, domain=None, range=Optional[Union[str, OtStatusId]])

slots.enhet = Slot(uri=UTD.enhet, name="enhet", curie=UTD.curie('enhet'),
                   model_uri=UTD.enhet, domain=None, range=Optional[Union[str, OtEnhetId]])

slots.verdi = Slot(uri=UTD.verdi, name="verdi", curie=UTD.curie('verdi'),
                   model_uri=UTD.verdi, domain=None, range=Optional[Union[Union[str, KarakterverdiId], list[Union[str, KarakterverdiId]]]])

slots.skala = Slot(uri=UTD.skala, name="skala", curie=UTD.curie('skala'),
                   model_uri=UTD.skala, domain=None, range=Optional[Union[str, KarakterskalaId]])

slots.fagmerknad = Slot(uri=UTD.fagmerknad, name="fagmerknad", curie=UTD.curie('fagmerknad'),
                   model_uri=UTD.fagmerknad, domain=None, range=Optional[Union[str, FagmerknadId]])

slots.id = Slot(uri=FINT.id, name="id", curie=FINT.curie('id'),
                   model_uri=UTD.id, domain=None, range=URIRef)

slots.gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=UTD.kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.postadresse = Slot(uri=FINT.postadresse, name="postadresse", curie=FINT.curie('postadresse'),
                   model_uri=UTD.postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.forretningsadresse = Slot(uri=FINT.forretningsadresse, name="forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=UTD.forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=UTD.organisasjonsnavn, domain=None, range=Optional[str])

slots.organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=UTD.organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.kode = Slot(uri=FINT.kode, name="kode", curie=FINT.curie('kode'),
                   model_uri=UTD.kode, domain=None, range=Optional[str])

slots.navn = Slot(uri=FINT.navn, name="navn", curie=FINT.curie('navn'),
                   model_uri=UTD.navn, domain=None, range=Optional[str])

slots.passiv = Slot(uri=FINT.passiv, name="passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=UTD.identifikatorverdi, domain=None, range=Optional[str])

slots.beskrivelse = Slot(uri=FINT.beskrivelse, name="beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=UTD.beskrivelse, domain=None, range=Optional[str])

slots.start = Slot(uri=FINT.start, name="start", curie=FINT.curie('start'),
                   model_uri=UTD.start, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.slutt = Slot(uri=FINT.slutt, name="slutt", curie=FINT.curie('slutt'),
                   model_uri=UTD.slutt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.fornavn = Slot(uri=FINT.fornavn, name="fornavn", curie=FINT.curie('fornavn'),
                   model_uri=UTD.fornavn, domain=None, range=Optional[str])

slots.mellomnavn = Slot(uri=FINT.mellomnavn, name="mellomnavn", curie=FINT.curie('mellomnavn'),
                   model_uri=UTD.mellomnavn, domain=None, range=Optional[str])

slots.etternavn = Slot(uri=FINT.etternavn, name="etternavn", curie=FINT.curie('etternavn'),
                   model_uri=UTD.etternavn, domain=None, range=Optional[str])

slots.epostadresse = Slot(uri=FINT.epostadresse, name="epostadresse", curie=FINT.curie('epostadresse'),
                   model_uri=UTD.epostadresse, domain=None, range=Optional[str])

slots.mobiltelefonnummer = Slot(uri=FINT.mobiltelefonnummer, name="mobiltelefonnummer", curie=FINT.curie('mobiltelefonnummer'),
                   model_uri=UTD.mobiltelefonnummer, domain=None, range=Optional[str])

slots.nettsted = Slot(uri=FINT.nettsted, name="nettsted", curie=FINT.curie('nettsted'),
                   model_uri=UTD.nettsted, domain=None, range=Optional[str])

slots.sip = Slot(uri=FINT.sip, name="sip", curie=FINT.curie('sip'),
                   model_uri=UTD.sip, domain=None, range=Optional[str])

slots.telefonnummer = Slot(uri=FINT.telefonnummer, name="telefonnummer", curie=FINT.curie('telefonnummer'),
                   model_uri=UTD.telefonnummer, domain=None, range=Optional[str])

slots.adresselinje = Slot(uri=FINT.adresselinje, name="adresselinje", curie=FINT.curie('adresselinje'),
                   model_uri=UTD.adresselinje, domain=None, range=Optional[Union[str, list[str]]])

slots.postnummer = Slot(uri=FINT.postnummer, name="postnummer", curie=FINT.curie('postnummer'),
                   model_uri=UTD.postnummer, domain=None, range=Optional[str])

slots.poststed = Slot(uri=FINT.poststed, name="poststed", curie=FINT.curie('poststed'),
                   model_uri=UTD.poststed, domain=None, range=Optional[str])

slots.land = Slot(uri=FINT.land, name="land", curie=FINT.curie('land'),
                   model_uri=UTD.land, domain=None, range=Optional[Union[str, LandkodeId]])

slots.adresse = Slot(uri=FINT.adresse, name="adresse", curie=FINT.curie('adresse'),
                   model_uri=UTD.adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.bruksnummer = Slot(uri=FINT.bruksnummer, name="bruksnummer", curie=FINT.curie('bruksnummer'),
                   model_uri=UTD.bruksnummer, domain=None, range=Optional[str])

slots.festenummer = Slot(uri=FINT.festenummer, name="festenummer", curie=FINT.curie('festenummer'),
                   model_uri=UTD.festenummer, domain=None, range=Optional[str])

slots.gaardsnummer = Slot(uri=FINT.gaardsnummer, name="gaardsnummer", curie=FINT.curie('gaardsnummer'),
                   model_uri=UTD.gaardsnummer, domain=None, range=Optional[str])

slots.seksjonsnummer = Slot(uri=FINT.seksjonsnummer, name="seksjonsnummer", curie=FINT.curie('seksjonsnummer'),
                   model_uri=UTD.seksjonsnummer, domain=None, range=Optional[str])

slots.kommunenummer = Slot(uri=FINT.kommunenummer, name="kommunenummer", curie=FINT.curie('kommunenummer'),
                   model_uri=UTD.kommunenummer, domain=None, range=Optional[Union[str, KommuneId]])

slots.fylke = Slot(uri=FINT.fylke, name="fylke", curie=FINT.curie('fylke'),
                   model_uri=UTD.fylke, domain=None, range=Optional[Union[str, FylkeId]])

slots.kommune = Slot(uri=FINT.kommune, name="kommune", curie=FINT.curie('kommune'),
                   model_uri=UTD.kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.kjonn = Slot(uri=FINT.kjonn, name="kjonn", curie=FINT.curie('kjonn'),
                   model_uri=UTD.kjonn, domain=None, range=Optional[Union[str, KjonnId]])

slots.bokstavkode = Slot(uri=FINT.bokstavkode, name="bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=UTD.bokstavkode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.valuta_navn = Slot(uri=FINT.valutaNavn, name="valuta_navn", curie=FINT.curie('valutaNavn'),
                   model_uri=UTD.valuta_navn, domain=None, range=Optional[str])

slots.nummerkode = Slot(uri=FINT.nummerkode, name="nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=UTD.nummerkode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.bilde = Slot(uri=FINT.bilde, name="bilde", curie=FINT.curie('bilde'),
                   model_uri=UTD.bilde, domain=None, range=Optional[str])

slots.bostedsadresse = Slot(uri=FINT.bostedsadresse, name="bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=UTD.bostedsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.fodselsdato = Slot(uri=FINT.fodselsdato, name="fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=UTD.fodselsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.fodselsnummer = Slot(uri=FINT.fodselsnummer, name="fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=UTD.fodselsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person_navn = Slot(uri=FINT.personNavn, name="person_navn", curie=FINT.curie('personNavn'),
                   model_uri=UTD.person_navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.parorende = Slot(uri=FINT.parorende, name="parorende", curie=FINT.curie('parorende'),
                   model_uri=UTD.parorende, domain=None, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.statsborgerskap = Slot(uri=FINT.statsborgerskap, name="statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=UTD.statsborgerskap, domain=None, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.foreldreansvar = Slot(uri=FINT.foreldreansvar, name="foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=UTD.foreldreansvar, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.foreldre = Slot(uri=FINT.foreldre, name="foreldre", curie=FINT.curie('foreldre'),
                   model_uri=UTD.foreldre, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.maalform = Slot(uri=FINT.maalform, name="maalform", curie=FINT.curie('maalform'),
                   model_uri=UTD.maalform, domain=None, range=Optional[Union[str, SpraakId]])

slots.morsmaal = Slot(uri=FINT.morsmaal, name="morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=UTD.morsmaal, domain=None, range=Optional[Union[str, SpraakId]])

slots.laerling = Slot(uri=FINT.laerling, name="laerling", curie=FINT.curie('laerling'),
                   model_uri=UTD.laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.elev = Slot(uri=FINT.elev, name="elev", curie=FINT.curie('elev'),
                   model_uri=UTD.elev, domain=None, range=Optional[Union[str, ElevId]])

slots.elevnummer = Slot(uri=FINT.elevnummer, name="elevnummer", curie=FINT.curie('elevnummer'),
                   model_uri=UTD.elevnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person = Slot(uri=FINT.person, name="person", curie=FINT.curie('person'),
                   model_uri=UTD.person, domain=None, range=Optional[Union[str, PersonId]])

slots.otungdom = Slot(uri=FINT.otungdom, name="otungdom", curie=FINT.curie('otungdom'),
                   model_uri=UTD.otungdom, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kontaktperson_navn = Slot(uri=FINT.kontaktpersonNavn, name="kontaktperson_navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=UTD.kontaktperson_navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.type = Slot(uri=FINT.type, name="type", curie=FINT.curie('type'),
                   model_uri=UTD.type, domain=None, range=Optional[str])

slots.kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=UTD.kontaktperson, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.virksomhetsId = Slot(uri=FINT.virksomhetsId, name="virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=UTD.virksomhetsId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.utdanningContainer__elevar = Slot(uri=UTD.elevar, name="utdanningContainer__elevar", curie=UTD.curie('elevar'),
                   model_uri=UTD.utdanningContainer__elevar, domain=None, range=Optional[Union[dict[Union[str, ElevId], Union[dict, Elev]], list[Union[dict, Elev]]]])

slots.utdanningContainer__skolar = Slot(uri=UTD.skolar, name="utdanningContainer__skolar", curie=UTD.curie('skolar'),
                   model_uri=UTD.utdanningContainer__skolar, domain=None, range=Optional[Union[dict[Union[str, SkoleId], Union[dict, Skole]], list[Union[dict, Skole]]]])

slots.utdanningContainer__skoleressursar = Slot(uri=UTD.skoleressursar, name="utdanningContainer__skoleressursar", curie=UTD.curie('skoleressursar'),
                   model_uri=UTD.utdanningContainer__skoleressursar, domain=None, range=Optional[Union[dict[Union[str, SkoleressursId], Union[dict, Skoleressurs]], list[Union[dict, Skoleressurs]]]])

slots.utdanningContainer__elevforhold = Slot(uri=UTD.elevforhold, name="utdanningContainer__elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.utdanningContainer__elevforhold, domain=None, range=Optional[Union[str, ElevforholdId]])

slots.utdanningContainer__elevtilrettelegging = Slot(uri=UTD.elevtilrettelegging, name="utdanningContainer__elevtilrettelegging", curie=UTD.curie('elevtilrettelegging'),
                   model_uri=UTD.utdanningContainer__elevtilrettelegging, domain=None, range=Optional[Union[dict[Union[str, ElevtilretteleggingId], Union[dict, Elevtilrettelegging]], list[Union[dict, Elevtilrettelegging]]]])

slots.utdanningContainer__klasser = Slot(uri=UTD.klasser, name="utdanningContainer__klasser", curie=UTD.curie('klasser'),
                   model_uri=UTD.utdanningContainer__klasser, domain=None, range=Optional[Union[dict[Union[str, KlasseId], Union[dict, Klasse]], list[Union[dict, Klasse]]]])

slots.utdanningContainer__klassemedlemskap = Slot(uri=UTD.klassemedlemskap, name="utdanningContainer__klassemedlemskap", curie=UTD.curie('klassemedlemskap'),
                   model_uri=UTD.utdanningContainer__klassemedlemskap, domain=None, range=Optional[Union[Union[str, KlassemedlemskapId], list[Union[str, KlassemedlemskapId]]]])

slots.utdanningContainer__kontaktlaerergrupper = Slot(uri=UTD.kontaktlaerergrupper, name="utdanningContainer__kontaktlaerergrupper", curie=UTD.curie('kontaktlaerergrupper'),
                   model_uri=UTD.utdanningContainer__kontaktlaerergrupper, domain=None, range=Optional[Union[dict[Union[str, KontaktlaerergruppeId], Union[dict, Kontaktlaerergruppe]], list[Union[dict, Kontaktlaerergruppe]]]])

slots.utdanningContainer__kontaktlaerergruppemedlemskap = Slot(uri=UTD.kontaktlaerergruppemedlemskap, name="utdanningContainer__kontaktlaerergruppemedlemskap", curie=UTD.curie('kontaktlaerergruppemedlemskap'),
                   model_uri=UTD.utdanningContainer__kontaktlaerergruppemedlemskap, domain=None, range=Optional[Union[Union[str, KontaktlaerergruppemedlemskapId], list[Union[str, KontaktlaerergruppemedlemskapId]]]])

slots.utdanningContainer__persongrupper = Slot(uri=UTD.persongrupper, name="utdanningContainer__persongrupper", curie=UTD.curie('persongrupper'),
                   model_uri=UTD.utdanningContainer__persongrupper, domain=None, range=Optional[Union[dict[Union[str, PersongruppeId], Union[dict, Persongruppe]], list[Union[dict, Persongruppe]]]])

slots.utdanningContainer__persongruppemedlemskap = Slot(uri=UTD.persongruppemedlemskap, name="utdanningContainer__persongruppemedlemskap", curie=UTD.curie('persongruppemedlemskap'),
                   model_uri=UTD.utdanningContainer__persongruppemedlemskap, domain=None, range=Optional[Union[Union[str, PersongruppemedlemskapId], list[Union[str, PersongruppemedlemskapId]]]])

slots.utdanningContainer__varsel = Slot(uri=UTD.varsel, name="utdanningContainer__varsel", curie=UTD.curie('varsel'),
                   model_uri=UTD.utdanningContainer__varsel, domain=None, range=Optional[Union[Union[str, VarselId], list[Union[str, VarselId]]]])

slots.utdanningContainer__arstrinn = Slot(uri=UTD.arstrinn, name="utdanningContainer__arstrinn", curie=UTD.curie('arstrinn'),
                   model_uri=UTD.utdanningContainer__arstrinn, domain=None, range=Optional[Union[dict[Union[str, ArstrinnId], Union[dict, Arstrinn]], list[Union[dict, Arstrinn]]]])

slots.utdanningContainer__programomrader = Slot(uri=UTD.programomrader, name="utdanningContainer__programomrader", curie=UTD.curie('programomrader'),
                   model_uri=UTD.utdanningContainer__programomrader, domain=None, range=Optional[Union[dict[Union[str, ProgramomradeId], Union[dict, Programomrade]], list[Union[dict, Programomrade]]]])

slots.utdanningContainer__programomrademedlemskap = Slot(uri=UTD.programomrademedlemskap, name="utdanningContainer__programomrademedlemskap", curie=UTD.curie('programomrademedlemskap'),
                   model_uri=UTD.utdanningContainer__programomrademedlemskap, domain=None, range=Optional[Union[Union[str, ProgramomrademedlemskapId], list[Union[str, ProgramomrademedlemskapId]]]])

slots.utdanningContainer__utdanningsprogram = Slot(uri=UTD.utdanningsprogram, name="utdanningContainer__utdanningsprogram", curie=UTD.curie('utdanningsprogram'),
                   model_uri=UTD.utdanningContainer__utdanningsprogram, domain=None, range=Optional[Union[Union[str, UtdanningsprogramId], list[Union[str, UtdanningsprogramId]]]])

slots.utdanningContainer__eksamen = Slot(uri=UTD.eksamen, name="utdanningContainer__eksamen", curie=UTD.curie('eksamen'),
                   model_uri=UTD.utdanningContainer__eksamen, domain=None, range=Optional[Union[str, EksamenId]])

slots.utdanningContainer__fag = Slot(uri=UTD.fag, name="utdanningContainer__fag", curie=UTD.curie('fag'),
                   model_uri=UTD.utdanningContainer__fag, domain=None, range=Optional[Union[str, FagId]])

slots.utdanningContainer__faggrupper = Slot(uri=UTD.faggrupper, name="utdanningContainer__faggrupper", curie=UTD.curie('faggrupper'),
                   model_uri=UTD.utdanningContainer__faggrupper, domain=None, range=Optional[Union[dict[Union[str, FaggruppeId], Union[dict, Faggruppe]], list[Union[dict, Faggruppe]]]])

slots.utdanningContainer__faggruppemedlemskap = Slot(uri=UTD.faggruppemedlemskap, name="utdanningContainer__faggruppemedlemskap", curie=UTD.curie('faggruppemedlemskap'),
                   model_uri=UTD.utdanningContainer__faggruppemedlemskap, domain=None, range=Optional[Union[Union[str, FaggruppemedlemskapId], list[Union[str, FaggruppemedlemskapId]]]])

slots.utdanningContainer__rom = Slot(uri=UTD.rom, name="utdanningContainer__rom", curie=UTD.curie('rom'),
                   model_uri=UTD.utdanningContainer__rom, domain=None, range=Optional[Union[str, RomId]])

slots.utdanningContainer__timar = Slot(uri=UTD.timar, name="utdanningContainer__timar", curie=UTD.curie('timar'),
                   model_uri=UTD.utdanningContainer__timar, domain=None, range=Optional[Union[dict[Union[str, TimeId], Union[dict, Time]], list[Union[dict, Time]]]])

slots.utdanningContainer__undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="utdanningContainer__undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.utdanningContainer__undervisningsforhold, domain=None, range=Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]])

slots.utdanningContainer__undervisningsgrupper = Slot(uri=UTD.undervisningsgrupper, name="utdanningContainer__undervisningsgrupper", curie=UTD.curie('undervisningsgrupper'),
                   model_uri=UTD.utdanningContainer__undervisningsgrupper, domain=None, range=Optional[Union[dict[Union[str, UndervisningsgruppeId], Union[dict, Undervisningsgruppe]], list[Union[dict, Undervisningsgruppe]]]])

slots.utdanningContainer__undervisningsgruppemedlemskap = Slot(uri=UTD.undervisningsgruppemedlemskap, name="utdanningContainer__undervisningsgruppemedlemskap", curie=UTD.curie('undervisningsgruppemedlemskap'),
                   model_uri=UTD.utdanningContainer__undervisningsgruppemedlemskap, domain=None, range=Optional[Union[Union[str, UndervisningsgruppemedlemskapId], list[Union[str, UndervisningsgruppemedlemskapId]]]])

slots.utdanningContainer__anmerkningar = Slot(uri=UTD.anmerkningar, name="utdanningContainer__anmerkningar", curie=UTD.curie('anmerkningar'),
                   model_uri=UTD.utdanningContainer__anmerkningar, domain=None, range=Optional[Union[dict[Union[str, AnmerkningerId], Union[dict, Anmerkninger]], list[Union[dict, Anmerkninger]]]])

slots.utdanningContainer__eksamensgrupper = Slot(uri=UTD.eksamensgrupper, name="utdanningContainer__eksamensgrupper", curie=UTD.curie('eksamensgrupper'),
                   model_uri=UTD.utdanningContainer__eksamensgrupper, domain=None, range=Optional[Union[dict[Union[str, EksamensgruppeId], Union[dict, Eksamensgruppe]], list[Union[dict, Eksamensgruppe]]]])

slots.utdanningContainer__eksamensgruppemedlemskap = Slot(uri=UTD.eksamensgruppemedlemskap, name="utdanningContainer__eksamensgruppemedlemskap", curie=UTD.curie('eksamensgruppemedlemskap'),
                   model_uri=UTD.utdanningContainer__eksamensgruppemedlemskap, domain=None, range=Optional[Union[Union[str, EksamensgruppemedlemskapId], list[Union[str, EksamensgruppemedlemskapId]]]])

slots.utdanningContainer__eksamensvurdering = Slot(uri=UTD.eksamensvurdering, name="utdanningContainer__eksamensvurdering", curie=UTD.curie('eksamensvurdering'),
                   model_uri=UTD.utdanningContainer__eksamensvurdering, domain=None, range=Optional[Union[Union[str, EksamensvurderingId], list[Union[str, EksamensvurderingId]]]])

slots.utdanningContainer__elevfravar = Slot(uri=UTD.elevfravar, name="utdanningContainer__elevfravar", curie=UTD.curie('elevfravar'),
                   model_uri=UTD.utdanningContainer__elevfravar, domain=None, range=Optional[Union[str, ElevfravarId]])

slots.utdanningContainer__elevvurdering = Slot(uri=UTD.elevvurdering, name="utdanningContainer__elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.utdanningContainer__elevvurdering, domain=None, range=Optional[Union[str, ElevvurderingId]])

slots.utdanningContainer__fravarsoversikt = Slot(uri=UTD.fravarsoversikt, name="utdanningContainer__fravarsoversikt", curie=UTD.curie('fravarsoversikt'),
                   model_uri=UTD.utdanningContainer__fravarsoversikt, domain=None, range=Optional[Union[dict[Union[str, FravarsoversiktId], Union[dict, Fravarsoversikt]], list[Union[dict, Fravarsoversikt]]]])

slots.utdanningContainer__fraversregistrering = Slot(uri=UTD.fraversregistrering, name="utdanningContainer__fraversregistrering", curie=UTD.curie('fraversregistrering'),
                   model_uri=UTD.utdanningContainer__fraversregistrering, domain=None, range=Optional[Union[Union[str, FraversregistreringId], list[Union[str, FraversregistreringId]]]])

slots.utdanningContainer__halvaarsfagvurdering = Slot(uri=UTD.halvaarsfagvurdering, name="utdanningContainer__halvaarsfagvurdering", curie=UTD.curie('halvaarsfagvurdering'),
                   model_uri=UTD.utdanningContainer__halvaarsfagvurdering, domain=None, range=Optional[Union[Union[str, HalvaarsfagvurderingId], list[Union[str, HalvaarsfagvurderingId]]]])

slots.utdanningContainer__halvaarsordensvurdering = Slot(uri=UTD.halvaarsordensvurdering, name="utdanningContainer__halvaarsordensvurdering", curie=UTD.curie('halvaarsordensvurdering'),
                   model_uri=UTD.utdanningContainer__halvaarsordensvurdering, domain=None, range=Optional[Union[Union[str, HalvaarsordensvurderingId], list[Union[str, HalvaarsordensvurderingId]]]])

slots.utdanningContainer__karakterhistorie = Slot(uri=UTD.karakterhistorie, name="utdanningContainer__karakterhistorie", curie=UTD.curie('karakterhistorie'),
                   model_uri=UTD.utdanningContainer__karakterhistorie, domain=None, range=Optional[Union[Union[str, KarakterhistorieId], list[Union[str, KarakterhistorieId]]]])

slots.utdanningContainer__sensor = Slot(uri=UTD.sensor, name="utdanningContainer__sensor", curie=UTD.curie('sensor'),
                   model_uri=UTD.utdanningContainer__sensor, domain=None, range=Optional[Union[Union[str, SensorId], list[Union[str, SensorId]]]])

slots.utdanningContainer__sluttfagvurdering = Slot(uri=UTD.sluttfagvurdering, name="utdanningContainer__sluttfagvurdering", curie=UTD.curie('sluttfagvurdering'),
                   model_uri=UTD.utdanningContainer__sluttfagvurdering, domain=None, range=Optional[Union[Union[str, SluttfagvurderingId], list[Union[str, SluttfagvurderingId]]]])

slots.utdanningContainer__sluttordensvurdering = Slot(uri=UTD.sluttordensvurdering, name="utdanningContainer__sluttordensvurdering", curie=UTD.curie('sluttordensvurdering'),
                   model_uri=UTD.utdanningContainer__sluttordensvurdering, domain=None, range=Optional[Union[Union[str, SluttordensvurderingId], list[Union[str, SluttordensvurderingId]]]])

slots.utdanningContainer__underveisfagvurdering = Slot(uri=UTD.underveisfagvurdering, name="utdanningContainer__underveisfagvurdering", curie=UTD.curie('underveisfagvurdering'),
                   model_uri=UTD.utdanningContainer__underveisfagvurdering, domain=None, range=Optional[Union[Union[str, UnderveisfagvurderingId], list[Union[str, UnderveisfagvurderingId]]]])

slots.utdanningContainer__underveisordensvurdering = Slot(uri=UTD.underveisordensvurdering, name="utdanningContainer__underveisordensvurdering", curie=UTD.curie('underveisordensvurdering'),
                   model_uri=UTD.utdanningContainer__underveisordensvurdering, domain=None, range=Optional[Union[Union[str, UnderveisordensvurderingId], list[Union[str, UnderveisordensvurderingId]]]])

slots.utdanningContainer__vitnemalsmerknad = Slot(uri=UTD.vitnemalsmerknad, name="utdanningContainer__vitnemalsmerknad", curie=UTD.curie('vitnemalsmerknad'),
                   model_uri=UTD.utdanningContainer__vitnemalsmerknad, domain=None, range=Optional[Union[str, VitnemalsmerknadId]])

slots.utdanningContainer__betalingsstatus = Slot(uri=UTD.betalingsstatus, name="utdanningContainer__betalingsstatus", curie=UTD.curie('betalingsstatus'),
                   model_uri=UTD.utdanningContainer__betalingsstatus, domain=None, range=Optional[Union[str, BetalingsstatusId]])

slots.utdanningContainer__fagstatus = Slot(uri=UTD.fagstatus, name="utdanningContainer__fagstatus", curie=UTD.curie('fagstatus'),
                   model_uri=UTD.utdanningContainer__fagstatus, domain=None, range=Optional[Union[str, FagstatusId]])

slots.utdanningContainer__karakterstatus = Slot(uri=UTD.karakterstatus, name="utdanningContainer__karakterstatus", curie=UTD.curie('karakterstatus'),
                   model_uri=UTD.utdanningContainer__karakterstatus, domain=None, range=Optional[Union[str, KarakterstatusId]])

slots.utdanningContainer__skoleaar = Slot(uri=UTD.skoleaar, name="utdanningContainer__skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.utdanningContainer__skoleaar, domain=None, range=Optional[Union[str, SkoleaarId]])

slots.utdanningContainer__tilrettelegging = Slot(uri=UTD.tilrettelegging, name="utdanningContainer__tilrettelegging", curie=UTD.curie('tilrettelegging'),
                   model_uri=UTD.utdanningContainer__tilrettelegging, domain=None, range=Optional[Union[str, TilretteleggingId]])

slots.utdanningContainer__avlagteprover = Slot(uri=UTD.avlagteprover, name="utdanningContainer__avlagteprover", curie=UTD.curie('avlagteprover'),
                   model_uri=UTD.utdanningContainer__avlagteprover, domain=None, range=Optional[Union[dict[Union[str, AvlagtProveId], Union[dict, AvlagtProve]], list[Union[dict, AvlagtProve]]]])

slots.utdanningContainer__laerlingar = Slot(uri=UTD.laerlingar, name="utdanningContainer__laerlingar", curie=UTD.curie('laerlingar'),
                   model_uri=UTD.utdanningContainer__laerlingar, domain=None, range=Optional[Union[dict[Union[str, LaerlingId], Union[dict, Laerling]], list[Union[dict, Laerling]]]])

slots.utdanningContainer__otUngdom = Slot(uri=UTD.otUngdom, name="utdanningContainer__otUngdom", curie=UTD.curie('otUngdom'),
                   model_uri=UTD.utdanningContainer__otUngdom, domain=None, range=Optional[Union[dict[Union[str, OtUngdomId], Union[dict, OtUngdom]], list[Union[dict, OtUngdom]]]])

slots.utdanningContainer__avbruddsaarsaker = Slot(uri=UTD.avbruddsaarsaker, name="utdanningContainer__avbruddsaarsaker", curie=UTD.curie('avbruddsaarsaker'),
                   model_uri=UTD.utdanningContainer__avbruddsaarsaker, domain=None, range=Optional[Union[dict[Union[str, AvbruddsaarsakId], Union[dict, Avbruddsaarsak]], list[Union[dict, Avbruddsaarsak]]]])

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

slots.utdanningContainer__fravartypar = Slot(uri=UTD.fravartypar, name="utdanningContainer__fravartypar", curie=UTD.curie('fravartypar'),
                   model_uri=UTD.utdanningContainer__fravartypar, domain=None, range=Optional[Union[dict[Union[str, FravartypeId], Union[dict, Fravartype]], list[Union[dict, Fravartype]]]])

slots.utdanningContainer__fullfortkoder = Slot(uri=UTD.fullfortkoder, name="utdanningContainer__fullfortkoder", curie=UTD.curie('fullfortkoder'),
                   model_uri=UTD.utdanningContainer__fullfortkoder, domain=None, range=Optional[Union[dict[Union[str, FullfortkodeId], Union[dict, Fullfortkode]], list[Union[dict, Fullfortkode]]]])

slots.utdanningContainer__karakterskalaer = Slot(uri=UTD.karakterskalaer, name="utdanningContainer__karakterskalaer", curie=UTD.curie('karakterskalaer'),
                   model_uri=UTD.utdanningContainer__karakterskalaer, domain=None, range=Optional[Union[dict[Union[str, KarakterskalaId], Union[dict, Karakterskala]], list[Union[dict, Karakterskala]]]])

slots.utdanningContainer__karakterverdiar = Slot(uri=UTD.karakterverdiar, name="utdanningContainer__karakterverdiar", curie=UTD.curie('karakterverdiar'),
                   model_uri=UTD.utdanningContainer__karakterverdiar, domain=None, range=Optional[Union[dict[Union[str, KarakterverdiId], Union[dict, Karakterverdi]], list[Union[dict, Karakterverdi]]]])

slots.utdanningContainer__otEnheter = Slot(uri=UTD.otEnheter, name="utdanningContainer__otEnheter", curie=UTD.curie('otEnheter'),
                   model_uri=UTD.utdanningContainer__otEnheter, domain=None, range=Optional[Union[dict[Union[str, OtEnhetId], Union[dict, OtEnhet]], list[Union[dict, OtEnhet]]]])

slots.utdanningContainer__otStatus = Slot(uri=UTD.otStatus, name="utdanningContainer__otStatus", curie=UTD.curie('otStatus'),
                   model_uri=UTD.utdanningContainer__otStatus, domain=None, range=Optional[Union[dict[Union[str, OtStatusId], Union[dict, OtStatus]], list[Union[dict, OtStatus]]]])

slots.utdanningContainer__provestatuser = Slot(uri=UTD.provestatuser, name="utdanningContainer__provestatuser", curie=UTD.curie('provestatuser'),
                   model_uri=UTD.utdanningContainer__provestatuser, domain=None, range=Optional[Union[dict[Union[str, ProvestatusId], Union[dict, Provestatus]], list[Union[dict, Provestatus]]]])

slots.utdanningContainer__skoleeijartypar = Slot(uri=UTD.skoleeijartypar, name="utdanningContainer__skoleeijartypar", curie=UTD.curie('skoleeijartypar'),
                   model_uri=UTD.utdanningContainer__skoleeijartypar, domain=None, range=Optional[Union[dict[Union[str, SkoleeiertypeId], Union[dict, Skoleeiertype]], list[Union[dict, Skoleeiertype]]]])

slots.utdanningContainer__terminar = Slot(uri=UTD.terminar, name="utdanningContainer__terminar", curie=UTD.curie('terminar'),
                   model_uri=UTD.utdanningContainer__terminar, domain=None, range=Optional[Union[dict[Union[str, TerminId], Union[dict, Termin]], list[Union[dict, Termin]]]])

slots.utdanningContainer__varseltypar = Slot(uri=UTD.varseltypar, name="utdanningContainer__varseltypar", curie=UTD.curie('varseltypar'),
                   model_uri=UTD.utdanningContainer__varseltypar, domain=None, range=Optional[Union[dict[Union[str, VarseltypeId], Union[dict, Varseltype]], list[Union[dict, Varseltype]]]])

slots.person__personalressurs = Slot(uri=FINT.personalressurs, name="person__personalressurs", curie=FINT.curie('personalressurs'),
                   model_uri=UTD.person__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.UtdanningContainer_elevforhold = Slot(uri=UTD.elevforhold, name="UtdanningContainer_elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.UtdanningContainer_elevforhold, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, ElevforholdId], Union[dict, "Elevforhold"]], list[Union[dict, "Elevforhold"]]]])

slots.UtdanningContainer_eksamen = Slot(uri=UTD.eksamen, name="UtdanningContainer_eksamen", curie=UTD.curie('eksamen'),
                   model_uri=UTD.UtdanningContainer_eksamen, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, EksamenId], Union[dict, "Eksamen"]], list[Union[dict, "Eksamen"]]]])

slots.UtdanningContainer_fag = Slot(uri=UTD.fag, name="UtdanningContainer_fag", curie=UTD.curie('fag'),
                   model_uri=UTD.UtdanningContainer_fag, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, FagId], Union[dict, "Fag"]], list[Union[dict, "Fag"]]]])

slots.UtdanningContainer_rom = Slot(uri=UTD.rom, name="UtdanningContainer_rom", curie=UTD.curie('rom'),
                   model_uri=UTD.UtdanningContainer_rom, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, RomId], Union[dict, "Rom"]], list[Union[dict, "Rom"]]]])

slots.UtdanningContainer_elevfravar = Slot(uri=UTD.elevfravar, name="UtdanningContainer_elevfravar", curie=UTD.curie('elevfravar'),
                   model_uri=UTD.UtdanningContainer_elevfravar, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, ElevfravarId], Union[dict, "Elevfravar"]], list[Union[dict, "Elevfravar"]]]])

slots.UtdanningContainer_elevvurdering = Slot(uri=UTD.elevvurdering, name="UtdanningContainer_elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.UtdanningContainer_elevvurdering, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, ElevvurderingId], Union[dict, "Elevvurdering"]], list[Union[dict, "Elevvurdering"]]]])

slots.UtdanningContainer_vitnemalsmerknad = Slot(uri=UTD.vitnemalsmerknad, name="UtdanningContainer_vitnemalsmerknad", curie=UTD.curie('vitnemalsmerknad'),
                   model_uri=UTD.UtdanningContainer_vitnemalsmerknad, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, VitnemalsmerknadId], Union[dict, "Vitnemalsmerknad"]], list[Union[dict, "Vitnemalsmerknad"]]]])

slots.UtdanningContainer_betalingsstatus = Slot(uri=UTD.betalingsstatus, name="UtdanningContainer_betalingsstatus", curie=UTD.curie('betalingsstatus'),
                   model_uri=UTD.UtdanningContainer_betalingsstatus, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, BetalingsstatusId], Union[dict, "Betalingsstatus"]], list[Union[dict, "Betalingsstatus"]]]])

slots.UtdanningContainer_fagstatus = Slot(uri=UTD.fagstatus, name="UtdanningContainer_fagstatus", curie=UTD.curie('fagstatus'),
                   model_uri=UTD.UtdanningContainer_fagstatus, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, FagstatusId], Union[dict, "Fagstatus"]], list[Union[dict, "Fagstatus"]]]])

slots.UtdanningContainer_karakterstatus = Slot(uri=UTD.karakterstatus, name="UtdanningContainer_karakterstatus", curie=UTD.curie('karakterstatus'),
                   model_uri=UTD.UtdanningContainer_karakterstatus, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, KarakterstatusId], Union[dict, "Karakterstatus"]], list[Union[dict, "Karakterstatus"]]]])

slots.UtdanningContainer_skoleaar = Slot(uri=UTD.skoleaar, name="UtdanningContainer_skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.UtdanningContainer_skoleaar, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, SkoleaarId], Union[dict, "Skoleaar"]], list[Union[dict, "Skoleaar"]]]])

slots.UtdanningContainer_tilrettelegging = Slot(uri=UTD.tilrettelegging, name="UtdanningContainer_tilrettelegging", curie=UTD.curie('tilrettelegging'),
                   model_uri=UTD.UtdanningContainer_tilrettelegging, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, TilretteleggingId], Union[dict, "Tilrettelegging"]], list[Union[dict, "Tilrettelegging"]]]])

slots.UtdanningContainer_klassemedlemskap = Slot(uri=UTD.klassemedlemskap, name="UtdanningContainer_klassemedlemskap", curie=UTD.curie('klassemedlemskap'),
                   model_uri=UTD.UtdanningContainer_klassemedlemskap, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, KlassemedlemskapId], Union[dict, "Klassemedlemskap"]], list[Union[dict, "Klassemedlemskap"]]]])

slots.UtdanningContainer_kontaktlaerergruppemedlemskap = Slot(uri=UTD.kontaktlaerergruppemedlemskap, name="UtdanningContainer_kontaktlaerergruppemedlemskap", curie=UTD.curie('kontaktlaerergruppemedlemskap'),
                   model_uri=UTD.UtdanningContainer_kontaktlaerergruppemedlemskap, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, KontaktlaerergruppemedlemskapId], Union[dict, "Kontaktlaerergruppemedlemskap"]], list[Union[dict, "Kontaktlaerergruppemedlemskap"]]]])

slots.UtdanningContainer_persongruppemedlemskap = Slot(uri=UTD.persongruppemedlemskap, name="UtdanningContainer_persongruppemedlemskap", curie=UTD.curie('persongruppemedlemskap'),
                   model_uri=UTD.UtdanningContainer_persongruppemedlemskap, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, PersongruppemedlemskapId], Union[dict, "Persongruppemedlemskap"]], list[Union[dict, "Persongruppemedlemskap"]]]])

slots.UtdanningContainer_programomrademedlemskap = Slot(uri=UTD.programomrademedlemskap, name="UtdanningContainer_programomrademedlemskap", curie=UTD.curie('programomrademedlemskap'),
                   model_uri=UTD.UtdanningContainer_programomrademedlemskap, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, ProgramomrademedlemskapId], Union[dict, "Programomrademedlemskap"]], list[Union[dict, "Programomrademedlemskap"]]]])

slots.UtdanningContainer_undervisningsgruppemedlemskap = Slot(uri=UTD.undervisningsgruppemedlemskap, name="UtdanningContainer_undervisningsgruppemedlemskap", curie=UTD.curie('undervisningsgruppemedlemskap'),
                   model_uri=UTD.UtdanningContainer_undervisningsgruppemedlemskap, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, UndervisningsgruppemedlemskapId], Union[dict, "Undervisningsgruppemedlemskap"]], list[Union[dict, "Undervisningsgruppemedlemskap"]]]])

slots.UtdanningContainer_eksamensgruppemedlemskap = Slot(uri=UTD.eksamensgruppemedlemskap, name="UtdanningContainer_eksamensgruppemedlemskap", curie=UTD.curie('eksamensgruppemedlemskap'),
                   model_uri=UTD.UtdanningContainer_eksamensgruppemedlemskap, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, EksamensgruppemedlemskapId], Union[dict, "Eksamensgruppemedlemskap"]], list[Union[dict, "Eksamensgruppemedlemskap"]]]])

slots.UtdanningContainer_faggruppemedlemskap = Slot(uri=UTD.faggruppemedlemskap, name="UtdanningContainer_faggruppemedlemskap", curie=UTD.curie('faggruppemedlemskap'),
                   model_uri=UTD.UtdanningContainer_faggruppemedlemskap, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, FaggruppemedlemskapId], Union[dict, "Faggruppemedlemskap"]], list[Union[dict, "Faggruppemedlemskap"]]]])

slots.UtdanningContainer_utdanningsprogram = Slot(uri=UTD.utdanningsprogram, name="UtdanningContainer_utdanningsprogram", curie=UTD.curie('utdanningsprogram'),
                   model_uri=UTD.UtdanningContainer_utdanningsprogram, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, UtdanningsprogramId], Union[dict, "Utdanningsprogram"]], list[Union[dict, "Utdanningsprogram"]]]])

slots.UtdanningContainer_undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="UtdanningContainer_undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.UtdanningContainer_undervisningsforhold, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, UndervisningsforholdId], Union[dict, "Undervisningsforhold"]], list[Union[dict, "Undervisningsforhold"]]]])

slots.UtdanningContainer_varsel = Slot(uri=UTD.varsel, name="UtdanningContainer_varsel", curie=UTD.curie('varsel'),
                   model_uri=UTD.UtdanningContainer_varsel, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, VarselId], Union[dict, "Varsel"]], list[Union[dict, "Varsel"]]]])

slots.UtdanningContainer_karakterhistorie = Slot(uri=UTD.karakterhistorie, name="UtdanningContainer_karakterhistorie", curie=UTD.curie('karakterhistorie'),
                   model_uri=UTD.UtdanningContainer_karakterhistorie, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, KarakterhistorieId], Union[dict, "Karakterhistorie"]], list[Union[dict, "Karakterhistorie"]]]])

slots.UtdanningContainer_sensor = Slot(uri=UTD.sensor, name="UtdanningContainer_sensor", curie=UTD.curie('sensor'),
                   model_uri=UTD.UtdanningContainer_sensor, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, SensorId], Union[dict, "Sensor"]], list[Union[dict, "Sensor"]]]])

slots.UtdanningContainer_fraversregistrering = Slot(uri=UTD.fraversregistrering, name="UtdanningContainer_fraversregistrering", curie=UTD.curie('fraversregistrering'),
                   model_uri=UTD.UtdanningContainer_fraversregistrering, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, FraversregistreringId], Union[dict, "Fraversregistrering"]], list[Union[dict, "Fraversregistrering"]]]])

slots.UtdanningContainer_halvaarsfagvurdering = Slot(uri=UTD.halvaarsfagvurdering, name="UtdanningContainer_halvaarsfagvurdering", curie=UTD.curie('halvaarsfagvurdering'),
                   model_uri=UTD.UtdanningContainer_halvaarsfagvurdering, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, HalvaarsfagvurderingId], Union[dict, "Halvaarsfagvurdering"]], list[Union[dict, "Halvaarsfagvurdering"]]]])

slots.UtdanningContainer_halvaarsordensvurdering = Slot(uri=UTD.halvaarsordensvurdering, name="UtdanningContainer_halvaarsordensvurdering", curie=UTD.curie('halvaarsordensvurdering'),
                   model_uri=UTD.UtdanningContainer_halvaarsordensvurdering, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, HalvaarsordensvurderingId], Union[dict, "Halvaarsordensvurdering"]], list[Union[dict, "Halvaarsordensvurdering"]]]])

slots.UtdanningContainer_sluttfagvurdering = Slot(uri=UTD.sluttfagvurdering, name="UtdanningContainer_sluttfagvurdering", curie=UTD.curie('sluttfagvurdering'),
                   model_uri=UTD.UtdanningContainer_sluttfagvurdering, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, SluttfagvurderingId], Union[dict, "Sluttfagvurdering"]], list[Union[dict, "Sluttfagvurdering"]]]])

slots.UtdanningContainer_sluttordensvurdering = Slot(uri=UTD.sluttordensvurdering, name="UtdanningContainer_sluttordensvurdering", curie=UTD.curie('sluttordensvurdering'),
                   model_uri=UTD.UtdanningContainer_sluttordensvurdering, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, SluttordensvurderingId], Union[dict, "Sluttordensvurdering"]], list[Union[dict, "Sluttordensvurdering"]]]])

slots.UtdanningContainer_underveisfagvurdering = Slot(uri=UTD.underveisfagvurdering, name="UtdanningContainer_underveisfagvurdering", curie=UTD.curie('underveisfagvurdering'),
                   model_uri=UTD.UtdanningContainer_underveisfagvurdering, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, UnderveisfagvurderingId], Union[dict, "Underveisfagvurdering"]], list[Union[dict, "Underveisfagvurdering"]]]])

slots.UtdanningContainer_underveisordensvurdering = Slot(uri=UTD.underveisordensvurdering, name="UtdanningContainer_underveisordensvurdering", curie=UTD.curie('underveisordensvurdering'),
                   model_uri=UTD.UtdanningContainer_underveisordensvurdering, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, UnderveisordensvurderingId], Union[dict, "Underveisordensvurdering"]], list[Union[dict, "Underveisordensvurdering"]]]])

slots.UtdanningContainer_eksamensvurdering = Slot(uri=UTD.eksamensvurdering, name="UtdanningContainer_eksamensvurdering", curie=UTD.curie('eksamensvurdering'),
                   model_uri=UTD.UtdanningContainer_eksamensvurdering, domain=UtdanningContainer, range=Optional[Union[dict[Union[str, EksamensvurderingId], Union[dict, "Eksamensvurdering"]], list[Union[dict, "Eksamensvurdering"]]]])

slots.Gruppe_navn = Slot(uri=FINT.navn, name="Gruppe_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Gruppe_navn, domain=Gruppe, range=str)

slots.Gruppe_beskrivelse = Slot(uri=FINT.beskrivelse, name="Gruppe_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=UTD.Gruppe_beskrivelse, domain=Gruppe, range=Optional[str])

slots.Gruppemedlemskap_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Gruppemedlemskap_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Gruppemedlemskap_gyldighetsperiode, domain=Gruppemedlemskap, range=Optional[Union[dict, "Periode"]])

slots.Utdanningsforhold_beskrivelse = Slot(uri=FINT.beskrivelse, name="Utdanningsforhold_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=UTD.Utdanningsforhold_beskrivelse, domain=Utdanningsforhold, range=Optional[str])

slots.Elevforhold_beskrivelse = Slot(uri=FINT.beskrivelse, name="Elevforhold_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=UTD.Elevforhold_beskrivelse, domain=Elevforhold, range=str)

slots.Elevforhold_avbruddsdato = Slot(uri=UTD.avbruddsdato, name="Elevforhold_avbruddsdato", curie=UTD.curie('avbruddsdato'),
                   model_uri=UTD.Elevforhold_avbruddsdato, domain=Elevforhold, range=Optional[Union[str, XSDDate]])

slots.Elevforhold_tosprakligFagopplaering = Slot(uri=UTD.tosprakligFagopplaering, name="Elevforhold_tosprakligFagopplaering", curie=UTD.curie('tosprakligFagopplaering'),
                   model_uri=UTD.Elevforhold_tosprakligFagopplaering, domain=Elevforhold, range=Optional[Union[bool, Bool]])

slots.Elevforhold_elev = Slot(uri=FINT.elev, name="Elevforhold_elev", curie=FINT.curie('elev'),
                   model_uri=UTD.Elevforhold_elev, domain=Elevforhold, range=Union[str, ElevId])

slots.Elevforhold_skole = Slot(uri=UTD.skole, name="Elevforhold_skole", curie=UTD.curie('skole'),
                   model_uri=UTD.Elevforhold_skole, domain=Elevforhold, range=Union[str, SkoleId])

slots.Elevforhold_kategori = Slot(uri=UTD.kategori, name="Elevforhold_kategori", curie=UTD.curie('kategori'),
                   model_uri=UTD.Elevforhold_kategori, domain=Elevforhold, range=Optional[Union[str, ElevkategoriId]])

slots.Elevforhold_avbruddsarsak = Slot(uri=UTD.avbruddsarsak, name="Elevforhold_avbruddsarsak", curie=UTD.curie('avbruddsarsak'),
                   model_uri=UTD.Elevforhold_avbruddsarsak, domain=Elevforhold, range=Optional[Union[str, AvbruddsaarsakId]])

slots.Elevforhold_skoleaar = Slot(uri=UTD.skoleaar, name="Elevforhold_skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.Elevforhold_skoleaar, domain=Elevforhold, range=Optional[Union[str, SkoleaarId]])

slots.Elevforhold_programomrademedlemskap = Slot(uri=UTD.programomrademedlemskap, name="Elevforhold_programomrademedlemskap", curie=UTD.curie('programomrademedlemskap'),
                   model_uri=UTD.Elevforhold_programomrademedlemskap, domain=Elevforhold, range=Optional[Union[Union[str, ProgramomrademedlemskapId], list[Union[str, ProgramomrademedlemskapId]]]])

slots.Elevforhold_klassemedlemskap = Slot(uri=UTD.klassemedlemskap, name="Elevforhold_klassemedlemskap", curie=UTD.curie('klassemedlemskap'),
                   model_uri=UTD.Elevforhold_klassemedlemskap, domain=Elevforhold, range=Optional[Union[Union[str, KlassemedlemskapId], list[Union[str, KlassemedlemskapId]]]])

slots.Elevforhold_faggruppemedlemskap = Slot(uri=UTD.faggruppemedlemskap, name="Elevforhold_faggruppemedlemskap", curie=UTD.curie('faggruppemedlemskap'),
                   model_uri=UTD.Elevforhold_faggruppemedlemskap, domain=Elevforhold, range=Optional[Union[Union[str, FaggruppemedlemskapId], list[Union[str, FaggruppemedlemskapId]]]])

slots.Elevforhold_undervisningsgruppemedlemskap = Slot(uri=UTD.undervisningsgruppemedlemskap, name="Elevforhold_undervisningsgruppemedlemskap", curie=UTD.curie('undervisningsgruppemedlemskap'),
                   model_uri=UTD.Elevforhold_undervisningsgruppemedlemskap, domain=Elevforhold, range=Optional[Union[Union[str, UndervisningsgruppemedlemskapId], list[Union[str, UndervisningsgruppemedlemskapId]]]])

slots.Elevforhold_kontaktlaerergruppemedlemskap = Slot(uri=UTD.kontaktlaerergruppemedlemskap, name="Elevforhold_kontaktlaerergruppemedlemskap", curie=UTD.curie('kontaktlaerergruppemedlemskap'),
                   model_uri=UTD.Elevforhold_kontaktlaerergruppemedlemskap, domain=Elevforhold, range=Optional[Union[Union[str, KontaktlaerergruppemedlemskapId], list[Union[str, KontaktlaerergruppemedlemskapId]]]])

slots.Elevforhold_persongruppemedlemskap = Slot(uri=UTD.persongruppemedlemskap, name="Elevforhold_persongruppemedlemskap", curie=UTD.curie('persongruppemedlemskap'),
                   model_uri=UTD.Elevforhold_persongruppemedlemskap, domain=Elevforhold, range=Optional[Union[Union[str, PersongruppemedlemskapId], list[Union[str, PersongruppemedlemskapId]]]])

slots.Elevforhold_eksamensgruppemedlemskap = Slot(uri=UTD.eksamensgruppemedlemskap, name="Elevforhold_eksamensgruppemedlemskap", curie=UTD.curie('eksamensgruppemedlemskap'),
                   model_uri=UTD.Elevforhold_eksamensgruppemedlemskap, domain=Elevforhold, range=Optional[Union[Union[str, EksamensgruppemedlemskapId], list[Union[str, EksamensgruppemedlemskapId]]]])

slots.Elevforhold_fraversregistreringer = Slot(uri=UTD.fraversregistreringer, name="Elevforhold_fraversregistreringer", curie=UTD.curie('fraversregistreringer'),
                   model_uri=UTD.Elevforhold_fraversregistreringer, domain=Elevforhold, range=Optional[Union[Union[str, ElevfravarId], list[Union[str, ElevfravarId]]]])

slots.Elevforhold_elevfravar = Slot(uri=UTD.elevfravar, name="Elevforhold_elevfravar", curie=UTD.curie('elevfravar'),
                   model_uri=UTD.Elevforhold_elevfravar, domain=Elevforhold, range=Optional[Union[str, FravarsoversiktId]])

slots.Elevforhold_tilrettelegging = Slot(uri=UTD.tilrettelegging, name="Elevforhold_tilrettelegging", curie=UTD.curie('tilrettelegging'),
                   model_uri=UTD.Elevforhold_tilrettelegging, domain=Elevforhold, range=Optional[Union[Union[str, ElevtilretteleggingId], list[Union[str, ElevtilretteleggingId]]]])

slots.Elevforhold_elevvurdering = Slot(uri=UTD.elevvurdering, name="Elevforhold_elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.Elevforhold_elevvurdering, domain=Elevforhold, range=Optional[Union[str, ElevvurderingId]])

slots.Elevtilrettelegging_elev = Slot(uri=FINT.elev, name="Elevtilrettelegging_elev", curie=FINT.curie('elev'),
                   model_uri=UTD.Elevtilrettelegging_elev, domain=Elevtilrettelegging, range=Optional[Union[str, ElevforholdId]])

slots.Elevtilrettelegging_tilrettelegging = Slot(uri=UTD.tilrettelegging, name="Elevtilrettelegging_tilrettelegging", curie=UTD.curie('tilrettelegging'),
                   model_uri=UTD.Elevtilrettelegging_tilrettelegging, domain=Elevtilrettelegging, range=Optional[Union[str, TilretteleggingId]])

slots.Elevtilrettelegging_eksamensform = Slot(uri=UTD.eksamensform, name="Elevtilrettelegging_eksamensform", curie=UTD.curie('eksamensform'),
                   model_uri=UTD.Elevtilrettelegging_eksamensform, domain=Elevtilrettelegging, range=Optional[Union[str, EksamensformId]])

slots.Klasse_skoleaar = Slot(uri=UTD.skoleaar, name="Klasse_skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.Klasse_skoleaar, domain=Klasse, range=Optional[Union[str, SkoleaarId]])

slots.Klasse_termin = Slot(uri=UTD.termin, name="Klasse_termin", curie=UTD.curie('termin'),
                   model_uri=UTD.Klasse_termin, domain=Klasse, range=Optional[Union[Union[str, TerminId], list[Union[str, TerminId]]]])

slots.Klasse_trinn = Slot(uri=UTD.trinn, name="Klasse_trinn", curie=UTD.curie('trinn'),
                   model_uri=UTD.Klasse_trinn, domain=Klasse, range=Optional[Union[Union[str, ArstrinnId], list[Union[str, ArstrinnId]]]])

slots.Klasse_skole = Slot(uri=UTD.skole, name="Klasse_skole", curie=UTD.curie('skole'),
                   model_uri=UTD.Klasse_skole, domain=Klasse, range=Optional[Union[str, SkoleId]])

slots.Klasse_undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="Klasse_undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.Klasse_undervisningsforhold, domain=Klasse, range=Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]])

slots.Klasse_klassemedlemskap = Slot(uri=UTD.klassemedlemskap, name="Klasse_klassemedlemskap", curie=UTD.curie('klassemedlemskap'),
                   model_uri=UTD.Klasse_klassemedlemskap, domain=Klasse, range=Optional[Union[Union[str, KlassemedlemskapId], list[Union[str, KlassemedlemskapId]]]])

slots.Klasse_kontaktlaerergruppe = Slot(uri=UTD.kontaktlaerergruppe, name="Klasse_kontaktlaerergruppe", curie=UTD.curie('kontaktlaerergruppe'),
                   model_uri=UTD.Klasse_kontaktlaerergruppe, domain=Klasse, range=Optional[Union[Union[str, KontaktlaerergruppeId], list[Union[str, KontaktlaerergruppeId]]]])

slots.Klassemedlemskap_elevforhold = Slot(uri=UTD.elevforhold, name="Klassemedlemskap_elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.Klassemedlemskap_elevforhold, domain=Klassemedlemskap, range=Optional[Union[str, ElevforholdId]])

slots.Klassemedlemskap_klasse = Slot(uri=UTD.klasse, name="Klassemedlemskap_klasse", curie=UTD.curie('klasse'),
                   model_uri=UTD.Klassemedlemskap_klasse, domain=Klassemedlemskap, range=Optional[Union[str, KlasseId]])

slots.Kontaktlaerergruppe_klasse = Slot(uri=UTD.klasse, name="Kontaktlaerergruppe_klasse", curie=UTD.curie('klasse'),
                   model_uri=UTD.Kontaktlaerergruppe_klasse, domain=Kontaktlaerergruppe, range=Union[Union[str, KlasseId], list[Union[str, KlasseId]]])

slots.Kontaktlaerergruppe_termin = Slot(uri=UTD.termin, name="Kontaktlaerergruppe_termin", curie=UTD.curie('termin'),
                   model_uri=UTD.Kontaktlaerergruppe_termin, domain=Kontaktlaerergruppe, range=Optional[Union[Union[str, TerminId], list[Union[str, TerminId]]]])

slots.Kontaktlaerergruppe_skole = Slot(uri=UTD.skole, name="Kontaktlaerergruppe_skole", curie=UTD.curie('skole'),
                   model_uri=UTD.Kontaktlaerergruppe_skole, domain=Kontaktlaerergruppe, range=Optional[Union[str, SkoleId]])

slots.Kontaktlaerergruppe_skoleaar = Slot(uri=UTD.skoleaar, name="Kontaktlaerergruppe_skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.Kontaktlaerergruppe_skoleaar, domain=Kontaktlaerergruppe, range=Optional[Union[str, SkoleaarId]])

slots.Kontaktlaerergruppe_undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="Kontaktlaerergruppe_undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.Kontaktlaerergruppe_undervisningsforhold, domain=Kontaktlaerergruppe, range=Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]])

slots.Kontaktlaerergruppe_gruppemedlemskap = Slot(uri=UTD.gruppemedlemskap, name="Kontaktlaerergruppe_gruppemedlemskap", curie=UTD.curie('gruppemedlemskap'),
                   model_uri=UTD.Kontaktlaerergruppe_gruppemedlemskap, domain=Kontaktlaerergruppe, range=Optional[Union[Union[str, KontaktlaerergruppemedlemskapId], list[Union[str, KontaktlaerergruppemedlemskapId]]]])

slots.Kontaktlaerergruppemedlemskap_elevforhold = Slot(uri=UTD.elevforhold, name="Kontaktlaerergruppemedlemskap_elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.Kontaktlaerergruppemedlemskap_elevforhold, domain=Kontaktlaerergruppemedlemskap, range=Optional[Union[str, ElevforholdId]])

slots.Kontaktlaerergruppemedlemskap_kontaktlaerergruppe = Slot(uri=UTD.kontaktlaerergruppe, name="Kontaktlaerergruppemedlemskap_kontaktlaerergruppe", curie=UTD.curie('kontaktlaerergruppe'),
                   model_uri=UTD.Kontaktlaerergruppemedlemskap_kontaktlaerergruppe, domain=Kontaktlaerergruppemedlemskap, range=Optional[Union[str, KontaktlaerergruppeId]])

slots.Persongruppe_elev = Slot(uri=FINT.elev, name="Persongruppe_elev", curie=FINT.curie('elev'),
                   model_uri=UTD.Persongruppe_elev, domain=Persongruppe, range=Optional[Union[Union[str, ElevforholdId], list[Union[str, ElevforholdId]]]])

slots.Persongruppe_persongruppemedlemskap = Slot(uri=UTD.persongruppemedlemskap, name="Persongruppe_persongruppemedlemskap", curie=UTD.curie('persongruppemedlemskap'),
                   model_uri=UTD.Persongruppe_persongruppemedlemskap, domain=Persongruppe, range=Optional[Union[Union[str, PersongruppemedlemskapId], list[Union[str, PersongruppemedlemskapId]]]])

slots.Persongruppe_termin = Slot(uri=UTD.termin, name="Persongruppe_termin", curie=UTD.curie('termin'),
                   model_uri=UTD.Persongruppe_termin, domain=Persongruppe, range=Optional[Union[Union[str, TerminId], list[Union[str, TerminId]]]])

slots.Persongruppe_undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="Persongruppe_undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.Persongruppe_undervisningsforhold, domain=Persongruppe, range=Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]])

slots.Persongruppe_skole = Slot(uri=UTD.skole, name="Persongruppe_skole", curie=UTD.curie('skole'),
                   model_uri=UTD.Persongruppe_skole, domain=Persongruppe, range=Optional[Union[str, SkoleId]])

slots.Persongruppe_skoleressurs = Slot(uri=UTD.skoleressurs, name="Persongruppe_skoleressurs", curie=UTD.curie('skoleressurs'),
                   model_uri=UTD.Persongruppe_skoleressurs, domain=Persongruppe, range=Optional[Union[Union[str, SkoleressursId], list[Union[str, SkoleressursId]]]])

slots.Persongruppe_skoleaar = Slot(uri=UTD.skoleaar, name="Persongruppe_skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.Persongruppe_skoleaar, domain=Persongruppe, range=Optional[Union[str, SkoleaarId]])

slots.Persongruppemedlemskap_elevforhold = Slot(uri=UTD.elevforhold, name="Persongruppemedlemskap_elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.Persongruppemedlemskap_elevforhold, domain=Persongruppemedlemskap, range=Optional[Union[str, ElevforholdId]])

slots.Persongruppemedlemskap_persongruppe = Slot(uri=UTD.persongruppe, name="Persongruppemedlemskap_persongruppe", curie=UTD.curie('persongruppe'),
                   model_uri=UTD.Persongruppemedlemskap_persongruppe, domain=Persongruppemedlemskap, range=Optional[Union[str, PersongruppeId]])

slots.Skole_navn = Slot(uri=FINT.navn, name="Skole_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Skole_navn, domain=Skole, range=str)

slots.Skole_domenenavn = Slot(uri=UTD.domenenavn, name="Skole_domenenavn", curie=UTD.curie('domenenavn'),
                   model_uri=UTD.Skole_domenenavn, domain=Skole, range=Optional[str])

slots.Skole_juridiskNavn = Slot(uri=UTD.juridiskNavn, name="Skole_juridiskNavn", curie=UTD.curie('juridiskNavn'),
                   model_uri=UTD.Skole_juridiskNavn, domain=Skole, range=Optional[str])

slots.Skole_organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="Skole_organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=UTD.Skole_organisasjonsnavn, domain=Skole, range=Optional[str])

slots.Skole_skolenummer = Slot(uri=UTD.skolenummer, name="Skole_skolenummer", curie=UTD.curie('skolenummer'),
                   model_uri=UTD.Skole_skolenummer, domain=Skole, range=Optional[Union[dict, "Identifikator"]])

slots.Skole_organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="Skole_organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=UTD.Skole_organisasjonsnummer, domain=Skole, range=Optional[Union[dict, "Identifikator"]])

slots.Skole_forretningsadresse = Slot(uri=FINT.forretningsadresse, name="Skole_forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=UTD.Skole_forretningsadresse, domain=Skole, range=Optional[Union[dict, "Adresse"]])

slots.Skole_postadresse = Slot(uri=FINT.postadresse, name="Skole_postadresse", curie=FINT.curie('postadresse'),
                   model_uri=UTD.Skole_postadresse, domain=Skole, range=Optional[Union[dict, "Adresse"]])

slots.Skole_organisasjon = Slot(uri=UTD.organisasjon, name="Skole_organisasjon", curie=UTD.curie('organisasjon'),
                   model_uri=UTD.Skole_organisasjon, domain=Skole, range=Optional[Union[str, URIorCURIE]])

slots.Skole_klasse = Slot(uri=UTD.klasse, name="Skole_klasse", curie=UTD.curie('klasse'),
                   model_uri=UTD.Skole_klasse, domain=Skole, range=Optional[Union[Union[str, KlasseId], list[Union[str, KlasseId]]]])

slots.Skole_kontaktlaerergruppe = Slot(uri=UTD.kontaktlaerergruppe, name="Skole_kontaktlaerergruppe", curie=UTD.curie('kontaktlaerergruppe'),
                   model_uri=UTD.Skole_kontaktlaerergruppe, domain=Skole, range=Optional[Union[Union[str, KontaktlaerergruppeId], list[Union[str, KontaktlaerergruppeId]]]])

slots.Skole_skoleressurs = Slot(uri=UTD.skoleressurs, name="Skole_skoleressurs", curie=UTD.curie('skoleressurs'),
                   model_uri=UTD.Skole_skoleressurs, domain=Skole, range=Optional[Union[Union[str, SkoleressursId], list[Union[str, SkoleressursId]]]])

slots.Skole_fag = Slot(uri=UTD.fag, name="Skole_fag", curie=UTD.curie('fag'),
                   model_uri=UTD.Skole_fag, domain=Skole, range=Optional[Union[Union[str, FagId], list[Union[str, FagId]]]])

slots.Skole_faggruppe = Slot(uri=UTD.faggruppe, name="Skole_faggruppe", curie=UTD.curie('faggruppe'),
                   model_uri=UTD.Skole_faggruppe, domain=Skole, range=Optional[Union[Union[str, FaggruppeId], list[Union[str, FaggruppeId]]]])

slots.Skole_skoleeierType = Slot(uri=UTD.skoleeierType, name="Skole_skoleeierType", curie=UTD.curie('skoleeierType'),
                   model_uri=UTD.Skole_skoleeierType, domain=Skole, range=Optional[Union[str, SkoleeiertypeId]])

slots.Skole_vigoreferanse = Slot(uri=UTD.vigoreferanse, name="Skole_vigoreferanse", curie=UTD.curie('vigoreferanse'),
                   model_uri=UTD.Skole_vigoreferanse, domain=Skole, range=Optional[Union[str, URIorCURIE]])

slots.Skole_eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="Skole_eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.Skole_eksamensgruppe, domain=Skole, range=Optional[Union[Union[str, EksamensgruppeId], list[Union[str, EksamensgruppeId]]]])

slots.Skole_utdanningsprogram = Slot(uri=UTD.utdanningsprogram, name="Skole_utdanningsprogram", curie=UTD.curie('utdanningsprogram'),
                   model_uri=UTD.Skole_utdanningsprogram, domain=Skole, range=Optional[Union[Union[str, UtdanningsprogramId], list[Union[str, UtdanningsprogramId]]]])

slots.Skoleressurs_feidenavn = Slot(uri=UTD.feidenavn, name="Skoleressurs_feidenavn", curie=UTD.curie('feidenavn'),
                   model_uri=UTD.Skoleressurs_feidenavn, domain=Skoleressurs, range=Optional[Union[dict, "Identifikator"]])

slots.Skoleressurs_personalressurs = Slot(uri=UTD.personalressurs, name="Skoleressurs_personalressurs", curie=UTD.curie('personalressurs'),
                   model_uri=UTD.Skoleressurs_personalressurs, domain=Skoleressurs, range=Optional[Union[str, URIorCURIE]])

slots.Skoleressurs_person = Slot(uri=FINT.person, name="Skoleressurs_person", curie=FINT.curie('person'),
                   model_uri=UTD.Skoleressurs_person, domain=Skoleressurs, range=Optional[Union[str, PersonId]])

slots.Skoleressurs_skole = Slot(uri=UTD.skole, name="Skoleressurs_skole", curie=UTD.curie('skole'),
                   model_uri=UTD.Skoleressurs_skole, domain=Skoleressurs, range=Optional[Union[Union[str, SkoleId], list[Union[str, SkoleId]]]])

slots.Skoleressurs_sensor = Slot(uri=UTD.sensor, name="Skoleressurs_sensor", curie=UTD.curie('sensor'),
                   model_uri=UTD.Skoleressurs_sensor, domain=Skoleressurs, range=Optional[Union[Union[str, SensorId], list[Union[str, SensorId]]]])

slots.Varsel_fravarsprosent = Slot(uri=UTD.fravarsprosent, name="Varsel_fravarsprosent", curie=UTD.curie('fravarsprosent'),
                   model_uri=UTD.Varsel_fravarsprosent, domain=Varsel, range=Optional[int])

slots.Varsel_sendt = Slot(uri=UTD.sendt, name="Varsel_sendt", curie=UTD.curie('sendt'),
                   model_uri=UTD.Varsel_sendt, domain=Varsel, range=Optional[Union[str, XSDDate]])

slots.Varsel_tekst = Slot(uri=UTD.tekst, name="Varsel_tekst", curie=UTD.curie('tekst'),
                   model_uri=UTD.Varsel_tekst, domain=Varsel, range=Optional[str])

slots.Varsel_utsteder = Slot(uri=UTD.utsteder, name="Varsel_utsteder", curie=UTD.curie('utsteder'),
                   model_uri=UTD.Varsel_utsteder, domain=Varsel, range=Optional[Union[str, SkoleressursId]])

slots.Varsel_karakteransvarlig = Slot(uri=UTD.karakteransvarlig, name="Varsel_karakteransvarlig", curie=UTD.curie('karakteransvarlig'),
                   model_uri=UTD.Varsel_karakteransvarlig, domain=Varsel, range=Optional[Union[str, SkoleressursId]])

slots.Varsel_type = Slot(uri=FINT.type, name="Varsel_type", curie=FINT.curie('type'),
                   model_uri=UTD.Varsel_type, domain=Varsel, range=Optional[Union[str, VarseltypeId]])

slots.Varsel_faggruppemedlemskap = Slot(uri=UTD.faggruppemedlemskap, name="Varsel_faggruppemedlemskap", curie=UTD.curie('faggruppemedlemskap'),
                   model_uri=UTD.Varsel_faggruppemedlemskap, domain=Varsel, range=Optional[Union[Union[str, FaggruppemedlemskapId], list[Union[str, FaggruppemedlemskapId]]]])

slots.Arstrinn_klasse = Slot(uri=UTD.klasse, name="Arstrinn_klasse", curie=UTD.curie('klasse'),
                   model_uri=UTD.Arstrinn_klasse, domain=Arstrinn, range=Optional[Union[Union[str, KlasseId], list[Union[str, KlasseId]]]])

slots.Arstrinn_vigoreferanse = Slot(uri=UTD.vigoreferanse, name="Arstrinn_vigoreferanse", curie=UTD.curie('vigoreferanse'),
                   model_uri=UTD.Arstrinn_vigoreferanse, domain=Arstrinn, range=Optional[Union[str, URIorCURIE]])

slots.Arstrinn_grepreferanse = Slot(uri=UTD.grepreferanse, name="Arstrinn_grepreferanse", curie=UTD.curie('grepreferanse'),
                   model_uri=UTD.Arstrinn_grepreferanse, domain=Arstrinn, range=Optional[Union[str, URIorCURIE]])

slots.Arstrinn_programomrade = Slot(uri=UTD.programomrade, name="Arstrinn_programomrade", curie=UTD.curie('programomrade'),
                   model_uri=UTD.Arstrinn_programomrade, domain=Arstrinn, range=Optional[Union[Union[str, ProgramomradeId], list[Union[str, ProgramomradeId]]]])

slots.Programomrade_trinn = Slot(uri=UTD.trinn, name="Programomrade_trinn", curie=UTD.curie('trinn'),
                   model_uri=UTD.Programomrade_trinn, domain=Programomrade, range=Optional[Union[Union[str, ArstrinnId], list[Union[str, ArstrinnId]]]])

slots.Programomrade_grepreferanse = Slot(uri=UTD.grepreferanse, name="Programomrade_grepreferanse", curie=UTD.curie('grepreferanse'),
                   model_uri=UTD.Programomrade_grepreferanse, domain=Programomrade, range=Optional[Union[str, URIorCURIE]])

slots.Programomrade_vigoreferanse = Slot(uri=UTD.vigoreferanse, name="Programomrade_vigoreferanse", curie=UTD.curie('vigoreferanse'),
                   model_uri=UTD.Programomrade_vigoreferanse, domain=Programomrade, range=Optional[Union[str, URIorCURIE]])

slots.Programomrade_gruppemedlemskap = Slot(uri=UTD.gruppemedlemskap, name="Programomrade_gruppemedlemskap", curie=UTD.curie('gruppemedlemskap'),
                   model_uri=UTD.Programomrade_gruppemedlemskap, domain=Programomrade, range=Optional[Union[Union[str, ProgramomrademedlemskapId], list[Union[str, ProgramomrademedlemskapId]]]])

slots.Programomrademedlemskap_elevforhold = Slot(uri=UTD.elevforhold, name="Programomrademedlemskap_elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.Programomrademedlemskap_elevforhold, domain=Programomrademedlemskap, range=Optional[Union[str, ElevforholdId]])

slots.Programomrademedlemskap_programomrade = Slot(uri=UTD.programomrade, name="Programomrademedlemskap_programomrade", curie=UTD.curie('programomrade'),
                   model_uri=UTD.Programomrademedlemskap_programomrade, domain=Programomrademedlemskap, range=Optional[Union[str, ProgramomradeId]])

slots.Utdanningsprogram_programomrade = Slot(uri=UTD.programomrade, name="Utdanningsprogram_programomrade", curie=UTD.curie('programomrade'),
                   model_uri=UTD.Utdanningsprogram_programomrade, domain=Utdanningsprogram, range=Optional[Union[Union[str, ProgramomradeId], list[Union[str, ProgramomradeId]]]])

slots.Utdanningsprogram_skole = Slot(uri=UTD.skole, name="Utdanningsprogram_skole", curie=UTD.curie('skole'),
                   model_uri=UTD.Utdanningsprogram_skole, domain=Utdanningsprogram, range=Optional[Union[Union[str, SkoleId], list[Union[str, SkoleId]]]])

slots.Utdanningsprogram_grepreferanse = Slot(uri=UTD.grepreferanse, name="Utdanningsprogram_grepreferanse", curie=UTD.curie('grepreferanse'),
                   model_uri=UTD.Utdanningsprogram_grepreferanse, domain=Utdanningsprogram, range=Optional[Union[str, URIorCURIE]])

slots.Utdanningsprogram_vigoreferanse = Slot(uri=UTD.vigoreferanse, name="Utdanningsprogram_vigoreferanse", curie=UTD.curie('vigoreferanse'),
                   model_uri=UTD.Utdanningsprogram_vigoreferanse, domain=Utdanningsprogram, range=Optional[Union[str, URIorCURIE]])

slots.Eksamen_navn = Slot(uri=FINT.navn, name="Eksamen_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Eksamen_navn, domain=Eksamen, range=str)

slots.Eksamen_beskrivelse = Slot(uri=FINT.beskrivelse, name="Eksamen_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=UTD.Eksamen_beskrivelse, domain=Eksamen, range=Optional[str])

slots.Eksamen_oppmoetetidspunkt = Slot(uri=UTD.oppmoetetidspunkt, name="Eksamen_oppmoetetidspunkt", curie=UTD.curie('oppmoetetidspunkt'),
                   model_uri=UTD.Eksamen_oppmoetetidspunkt, domain=Eksamen, range=Optional[Union[str, XSDDateTime]])

slots.Eksamen_tidsrom = Slot(uri=UTD.tidsrom, name="Eksamen_tidsrom", curie=UTD.curie('tidsrom'),
                   model_uri=UTD.Eksamen_tidsrom, domain=Eksamen, range=Optional[Union[dict, "Periode"]])

slots.Eksamen_rom = Slot(uri=UTD.rom, name="Eksamen_rom", curie=UTD.curie('rom'),
                   model_uri=UTD.Eksamen_rom, domain=Eksamen, range=Optional[Union[Union[str, RomId], list[Union[str, RomId]]]])

slots.Eksamen_eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="Eksamen_eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.Eksamen_eksamensgruppe, domain=Eksamen, range=Optional[Union[str, EksamensgruppeId]])

slots.Fag_tilrettelegging = Slot(uri=UTD.tilrettelegging, name="Fag_tilrettelegging", curie=UTD.curie('tilrettelegging'),
                   model_uri=UTD.Fag_tilrettelegging, domain=Fag, range=Optional[Union[Union[str, TilretteleggingId], list[Union[str, TilretteleggingId]]]])

slots.Fag_grepreferanse = Slot(uri=UTD.grepreferanse, name="Fag_grepreferanse", curie=UTD.curie('grepreferanse'),
                   model_uri=UTD.Fag_grepreferanse, domain=Fag, range=Optional[Union[str, URIorCURIE]])

slots.Fag_skole = Slot(uri=UTD.skole, name="Fag_skole", curie=UTD.curie('skole'),
                   model_uri=UTD.Fag_skole, domain=Fag, range=Optional[Union[Union[str, SkoleId], list[Union[str, SkoleId]]]])

slots.Fag_vigoreferanse = Slot(uri=UTD.vigoreferanse, name="Fag_vigoreferanse", curie=UTD.curie('vigoreferanse'),
                   model_uri=UTD.Fag_vigoreferanse, domain=Fag, range=Optional[Union[str, URIorCURIE]])

slots.Fag_programomrade = Slot(uri=UTD.programomrade, name="Fag_programomrade", curie=UTD.curie('programomrade'),
                   model_uri=UTD.Fag_programomrade, domain=Fag, range=Optional[Union[Union[str, ProgramomradeId], list[Union[str, ProgramomradeId]]]])

slots.Fag_faggruppe = Slot(uri=UTD.faggruppe, name="Fag_faggruppe", curie=UTD.curie('faggruppe'),
                   model_uri=UTD.Fag_faggruppe, domain=Fag, range=Optional[Union[Union[str, FaggruppeId], list[Union[str, FaggruppeId]]]])

slots.Fag_undervisningsgruppe = Slot(uri=UTD.undervisningsgruppe, name="Fag_undervisningsgruppe", curie=UTD.curie('undervisningsgruppe'),
                   model_uri=UTD.Fag_undervisningsgruppe, domain=Fag, range=Optional[Union[Union[str, UndervisningsgruppeId], list[Union[str, UndervisningsgruppeId]]]])

slots.Fag_eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="Fag_eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.Fag_eksamensgruppe, domain=Fag, range=Optional[Union[Union[str, EksamensgruppeId], list[Union[str, EksamensgruppeId]]]])

slots.Faggruppe_fag = Slot(uri=UTD.fag, name="Faggruppe_fag", curie=UTD.curie('fag'),
                   model_uri=UTD.Faggruppe_fag, domain=Faggruppe, range=Union[str, FagId])

slots.Faggruppe_skole = Slot(uri=UTD.skole, name="Faggruppe_skole", curie=UTD.curie('skole'),
                   model_uri=UTD.Faggruppe_skole, domain=Faggruppe, range=Optional[Union[str, SkoleId]])

slots.Faggruppe_skoleaar = Slot(uri=UTD.skoleaar, name="Faggruppe_skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.Faggruppe_skoleaar, domain=Faggruppe, range=Optional[Union[str, SkoleaarId]])

slots.Faggruppe_faggruppemedlemskap = Slot(uri=UTD.faggruppemedlemskap, name="Faggruppe_faggruppemedlemskap", curie=UTD.curie('faggruppemedlemskap'),
                   model_uri=UTD.Faggruppe_faggruppemedlemskap, domain=Faggruppe, range=Optional[Union[Union[str, FaggruppemedlemskapId], list[Union[str, FaggruppemedlemskapId]]]])

slots.Faggruppemedlemskap_elevforhold = Slot(uri=UTD.elevforhold, name="Faggruppemedlemskap_elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.Faggruppemedlemskap_elevforhold, domain=Faggruppemedlemskap, range=Optional[Union[str, ElevforholdId]])

slots.Faggruppemedlemskap_varsel = Slot(uri=UTD.varsel, name="Faggruppemedlemskap_varsel", curie=UTD.curie('varsel'),
                   model_uri=UTD.Faggruppemedlemskap_varsel, domain=Faggruppemedlemskap, range=Optional[Union[Union[str, VarselId], list[Union[str, VarselId]]]])

slots.Faggruppemedlemskap_faggruppe = Slot(uri=UTD.faggruppe, name="Faggruppemedlemskap_faggruppe", curie=UTD.curie('faggruppe'),
                   model_uri=UTD.Faggruppemedlemskap_faggruppe, domain=Faggruppemedlemskap, range=Optional[Union[str, FaggruppeId]])

slots.Faggruppemedlemskap_fagmerknad = Slot(uri=UTD.fagmerknad, name="Faggruppemedlemskap_fagmerknad", curie=UTD.curie('fagmerknad'),
                   model_uri=UTD.Faggruppemedlemskap_fagmerknad, domain=Faggruppemedlemskap, range=Optional[Union[str, FagmerknadId]])

slots.Faggruppemedlemskap_fagstatus = Slot(uri=UTD.fagstatus, name="Faggruppemedlemskap_fagstatus", curie=UTD.curie('fagstatus'),
                   model_uri=UTD.Faggruppemedlemskap_fagstatus, domain=Faggruppemedlemskap, range=Optional[Union[str, FagstatusId]])

slots.Rom_navn = Slot(uri=FINT.navn, name="Rom_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Rom_navn, domain=Rom, range=Optional[str])

slots.Rom_eksamen = Slot(uri=UTD.eksamen, name="Rom_eksamen", curie=UTD.curie('eksamen'),
                   model_uri=UTD.Rom_eksamen, domain=Rom, range=Optional[Union[Union[str, EksamenId], list[Union[str, EksamenId]]]])

slots.Rom_skuletime = Slot(uri=UTD.skuletime, name="Rom_skuletime", curie=UTD.curie('skuletime'),
                   model_uri=UTD.Rom_skuletime, domain=Rom, range=Optional[Union[Union[str, TimeId], list[Union[str, TimeId]]]])

slots.Time_navn = Slot(uri=FINT.navn, name="Time_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Time_navn, domain=Time, range=Optional[str])

slots.Time_beskrivelse = Slot(uri=FINT.beskrivelse, name="Time_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=UTD.Time_beskrivelse, domain=Time, range=Optional[str])

slots.Time_tidsrom = Slot(uri=UTD.tidsrom, name="Time_tidsrom", curie=UTD.curie('tidsrom'),
                   model_uri=UTD.Time_tidsrom, domain=Time, range=Optional[Union[dict, "Periode"]])

slots.Time_undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="Time_undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.Time_undervisningsforhold, domain=Time, range=Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]])

slots.Time_rom = Slot(uri=UTD.rom, name="Time_rom", curie=UTD.curie('rom'),
                   model_uri=UTD.Time_rom, domain=Time, range=Optional[Union[Union[str, RomId], list[Union[str, RomId]]]])

slots.Time_undervisningsgruppe = Slot(uri=UTD.undervisningsgruppe, name="Time_undervisningsgruppe", curie=UTD.curie('undervisningsgruppe'),
                   model_uri=UTD.Time_undervisningsgruppe, domain=Time, range=Union[Union[str, UndervisningsgruppeId], list[Union[str, UndervisningsgruppeId]]])

slots.Undervisningsforhold_arbeidsforhold = Slot(uri=UTD.arbeidsforhold, name="Undervisningsforhold_arbeidsforhold", curie=UTD.curie('arbeidsforhold'),
                   model_uri=UTD.Undervisningsforhold_arbeidsforhold, domain=Undervisningsforhold, range=Union[str, URIorCURIE])

slots.Undervisningsforhold_skoleressurs = Slot(uri=UTD.skoleressurs, name="Undervisningsforhold_skoleressurs", curie=UTD.curie('skoleressurs'),
                   model_uri=UTD.Undervisningsforhold_skoleressurs, domain=Undervisningsforhold, range=Optional[Union[str, SkoleressursId]])

slots.Undervisningsforhold_klasse = Slot(uri=UTD.klasse, name="Undervisningsforhold_klasse", curie=UTD.curie('klasse'),
                   model_uri=UTD.Undervisningsforhold_klasse, domain=Undervisningsforhold, range=Optional[Union[Union[str, KlasseId], list[Union[str, KlasseId]]]])

slots.Undervisningsforhold_kontaktlaerergruppe = Slot(uri=UTD.kontaktlaerergruppe, name="Undervisningsforhold_kontaktlaerergruppe", curie=UTD.curie('kontaktlaerergruppe'),
                   model_uri=UTD.Undervisningsforhold_kontaktlaerergruppe, domain=Undervisningsforhold, range=Optional[Union[Union[str, KontaktlaerergruppeId], list[Union[str, KontaktlaerergruppeId]]]])

slots.Undervisningsforhold_skuletime = Slot(uri=UTD.skuletime, name="Undervisningsforhold_skuletime", curie=UTD.curie('skuletime'),
                   model_uri=UTD.Undervisningsforhold_skuletime, domain=Undervisningsforhold, range=Optional[Union[Union[str, TimeId], list[Union[str, TimeId]]]])

slots.Undervisningsforhold_eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="Undervisningsforhold_eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.Undervisningsforhold_eksamensgruppe, domain=Undervisningsforhold, range=Optional[Union[Union[str, EksamensgruppeId], list[Union[str, EksamensgruppeId]]]])

slots.Undervisningsgruppe_undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="Undervisningsgruppe_undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.Undervisningsgruppe_undervisningsforhold, domain=Undervisningsgruppe, range=Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]])

slots.Undervisningsgruppe_fag = Slot(uri=UTD.fag, name="Undervisningsgruppe_fag", curie=UTD.curie('fag'),
                   model_uri=UTD.Undervisningsgruppe_fag, domain=Undervisningsgruppe, range=Union[Union[str, FagId], list[Union[str, FagId]]])

slots.Undervisningsgruppe_skuletime = Slot(uri=UTD.skuletime, name="Undervisningsgruppe_skuletime", curie=UTD.curie('skuletime'),
                   model_uri=UTD.Undervisningsgruppe_skuletime, domain=Undervisningsgruppe, range=Optional[Union[Union[str, TimeId], list[Union[str, TimeId]]]])

slots.Undervisningsgruppe_termin = Slot(uri=UTD.termin, name="Undervisningsgruppe_termin", curie=UTD.curie('termin'),
                   model_uri=UTD.Undervisningsgruppe_termin, domain=Undervisningsgruppe, range=Optional[Union[Union[str, TerminId], list[Union[str, TerminId]]]])

slots.Undervisningsgruppe_skole = Slot(uri=UTD.skole, name="Undervisningsgruppe_skole", curie=UTD.curie('skole'),
                   model_uri=UTD.Undervisningsgruppe_skole, domain=Undervisningsgruppe, range=Optional[Union[str, SkoleId]])

slots.Undervisningsgruppe_skoleaar = Slot(uri=UTD.skoleaar, name="Undervisningsgruppe_skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.Undervisningsgruppe_skoleaar, domain=Undervisningsgruppe, range=Optional[Union[str, SkoleaarId]])

slots.Undervisningsgruppe_gruppemedlemskap = Slot(uri=UTD.gruppemedlemskap, name="Undervisningsgruppe_gruppemedlemskap", curie=UTD.curie('gruppemedlemskap'),
                   model_uri=UTD.Undervisningsgruppe_gruppemedlemskap, domain=Undervisningsgruppe, range=Optional[Union[Union[str, UndervisningsgruppemedlemskapId], list[Union[str, UndervisningsgruppemedlemskapId]]]])

slots.Undervisningsgruppemedlemskap_elevforhold = Slot(uri=UTD.elevforhold, name="Undervisningsgruppemedlemskap_elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.Undervisningsgruppemedlemskap_elevforhold, domain=Undervisningsgruppemedlemskap, range=Optional[Union[str, ElevforholdId]])

slots.Undervisningsgruppemedlemskap_undervisningsgruppe = Slot(uri=UTD.undervisningsgruppe, name="Undervisningsgruppemedlemskap_undervisningsgruppe", curie=UTD.curie('undervisningsgruppe'),
                   model_uri=UTD.Undervisningsgruppemedlemskap_undervisningsgruppe, domain=Undervisningsgruppemedlemskap, range=Optional[Union[str, UndervisningsgruppeId]])

slots.FagvurderingAbstrakt_kommentar = Slot(uri=UTD.kommentar, name="FagvurderingAbstrakt_kommentar", curie=UTD.curie('kommentar'),
                   model_uri=UTD.FagvurderingAbstrakt_kommentar, domain=FagvurderingAbstrakt, range=str)

slots.FagvurderingAbstrakt_vurderingsdato = Slot(uri=UTD.vurderingsdato, name="FagvurderingAbstrakt_vurderingsdato", curie=UTD.curie('vurderingsdato'),
                   model_uri=UTD.FagvurderingAbstrakt_vurderingsdato, domain=FagvurderingAbstrakt, range=Union[str, XSDDateTime])

slots.FagvurderingAbstrakt_fag = Slot(uri=UTD.fag, name="FagvurderingAbstrakt_fag", curie=UTD.curie('fag'),
                   model_uri=UTD.FagvurderingAbstrakt_fag, domain=FagvurderingAbstrakt, range=Optional[Union[str, FagId]])

slots.FagvurderingAbstrakt_skoleaar = Slot(uri=UTD.skoleaar, name="FagvurderingAbstrakt_skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.FagvurderingAbstrakt_skoleaar, domain=FagvurderingAbstrakt, range=Optional[Union[str, SkoleaarId]])

slots.FagvurderingAbstrakt_karakter = Slot(uri=UTD.karakter, name="FagvurderingAbstrakt_karakter", curie=UTD.curie('karakter'),
                   model_uri=UTD.FagvurderingAbstrakt_karakter, domain=FagvurderingAbstrakt, range=Optional[Union[str, KarakterverdiId]])

slots.OrdensvurderingAbstrakt_kommentar = Slot(uri=UTD.kommentar, name="OrdensvurderingAbstrakt_kommentar", curie=UTD.curie('kommentar'),
                   model_uri=UTD.OrdensvurderingAbstrakt_kommentar, domain=OrdensvurderingAbstrakt, range=str)

slots.OrdensvurderingAbstrakt_vurderingsdato = Slot(uri=UTD.vurderingsdato, name="OrdensvurderingAbstrakt_vurderingsdato", curie=UTD.curie('vurderingsdato'),
                   model_uri=UTD.OrdensvurderingAbstrakt_vurderingsdato, domain=OrdensvurderingAbstrakt, range=Union[str, XSDDateTime])

slots.OrdensvurderingAbstrakt_atferd = Slot(uri=UTD.atferd, name="OrdensvurderingAbstrakt_atferd", curie=UTD.curie('atferd'),
                   model_uri=UTD.OrdensvurderingAbstrakt_atferd, domain=OrdensvurderingAbstrakt, range=Optional[Union[str, KarakterverdiId]])

slots.OrdensvurderingAbstrakt_orden = Slot(uri=UTD.orden, name="OrdensvurderingAbstrakt_orden", curie=UTD.curie('orden'),
                   model_uri=UTD.OrdensvurderingAbstrakt_orden, domain=OrdensvurderingAbstrakt, range=Optional[Union[str, KarakterverdiId]])

slots.OrdensvurderingAbstrakt_skoleaar = Slot(uri=UTD.skoleaar, name="OrdensvurderingAbstrakt_skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.OrdensvurderingAbstrakt_skoleaar, domain=OrdensvurderingAbstrakt, range=Optional[Union[str, SkoleaarId]])

slots.Anmerkninger_atferd = Slot(uri=UTD.atferd, name="Anmerkninger_atferd", curie=UTD.curie('atferd'),
                   model_uri=UTD.Anmerkninger_atferd, domain=Anmerkninger, range=int)

slots.Anmerkninger_orden = Slot(uri=UTD.orden, name="Anmerkninger_orden", curie=UTD.curie('orden'),
                   model_uri=UTD.Anmerkninger_orden, domain=Anmerkninger, range=int)

slots.Anmerkninger_skoleaar = Slot(uri=UTD.skoleaar, name="Anmerkninger_skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.Anmerkninger_skoleaar, domain=Anmerkninger, range=Optional[Union[str, SkoleaarId]])

slots.Eksamensgruppe_eksamensdato = Slot(uri=UTD.eksamensdato, name="Eksamensgruppe_eksamensdato", curie=UTD.curie('eksamensdato'),
                   model_uri=UTD.Eksamensgruppe_eksamensdato, domain=Eksamensgruppe, range=Optional[Union[str, XSDDateTime]])

slots.Eksamensgruppe_fag = Slot(uri=UTD.fag, name="Eksamensgruppe_fag", curie=UTD.curie('fag'),
                   model_uri=UTD.Eksamensgruppe_fag, domain=Eksamensgruppe, range=Union[str, FagId])

slots.Eksamensgruppe_skole = Slot(uri=UTD.skole, name="Eksamensgruppe_skole", curie=UTD.curie('skole'),
                   model_uri=UTD.Eksamensgruppe_skole, domain=Eksamensgruppe, range=Union[str, SkoleId])

slots.Eksamensgruppe_termin = Slot(uri=UTD.termin, name="Eksamensgruppe_termin", curie=UTD.curie('termin'),
                   model_uri=UTD.Eksamensgruppe_termin, domain=Eksamensgruppe, range=Union[str, TerminId])

slots.Eksamensgruppe_undervisningsforhold = Slot(uri=UTD.undervisningsforhold, name="Eksamensgruppe_undervisningsforhold", curie=UTD.curie('undervisningsforhold'),
                   model_uri=UTD.Eksamensgruppe_undervisningsforhold, domain=Eksamensgruppe, range=Optional[Union[Union[str, UndervisningsforholdId], list[Union[str, UndervisningsforholdId]]]])

slots.Eksamensgruppe_eksamen = Slot(uri=UTD.eksamen, name="Eksamensgruppe_eksamen", curie=UTD.curie('eksamen'),
                   model_uri=UTD.Eksamensgruppe_eksamen, domain=Eksamensgruppe, range=Optional[Union[str, EksamenId]])

slots.Eksamensgruppe_eksamensform = Slot(uri=UTD.eksamensform, name="Eksamensgruppe_eksamensform", curie=UTD.curie('eksamensform'),
                   model_uri=UTD.Eksamensgruppe_eksamensform, domain=Eksamensgruppe, range=Optional[Union[str, EksamensformId]])

slots.Eksamensgruppe_skoleaar = Slot(uri=UTD.skoleaar, name="Eksamensgruppe_skoleaar", curie=UTD.curie('skoleaar'),
                   model_uri=UTD.Eksamensgruppe_skoleaar, domain=Eksamensgruppe, range=Optional[Union[str, SkoleaarId]])

slots.Eksamensgruppe_gruppemedlemskap = Slot(uri=UTD.gruppemedlemskap, name="Eksamensgruppe_gruppemedlemskap", curie=UTD.curie('gruppemedlemskap'),
                   model_uri=UTD.Eksamensgruppe_gruppemedlemskap, domain=Eksamensgruppe, range=Optional[Union[Union[str, EksamensgruppemedlemskapId], list[Union[str, EksamensgruppemedlemskapId]]]])

slots.Eksamensgruppe_sensor = Slot(uri=UTD.sensor, name="Eksamensgruppe_sensor", curie=UTD.curie('sensor'),
                   model_uri=UTD.Eksamensgruppe_sensor, domain=Eksamensgruppe, range=Optional[Union[Union[str, SensorId], list[Union[str, SensorId]]]])

slots.Eksamensgruppemedlemskap_delegert = Slot(uri=UTD.delegert, name="Eksamensgruppemedlemskap_delegert", curie=UTD.curie('delegert'),
                   model_uri=UTD.Eksamensgruppemedlemskap_delegert, domain=Eksamensgruppemedlemskap, range=Optional[Union[bool, Bool]])

slots.Eksamensgruppemedlemskap_kandidatnummer = Slot(uri=UTD.kandidatnummer, name="Eksamensgruppemedlemskap_kandidatnummer", curie=UTD.curie('kandidatnummer'),
                   model_uri=UTD.Eksamensgruppemedlemskap_kandidatnummer, domain=Eksamensgruppemedlemskap, range=Optional[str])

slots.Eksamensgruppemedlemskap_delegertTil = Slot(uri=UTD.delegertTil, name="Eksamensgruppemedlemskap_delegertTil", curie=UTD.curie('delegertTil'),
                   model_uri=UTD.Eksamensgruppemedlemskap_delegertTil, domain=Eksamensgruppemedlemskap, range=Optional[Union[str, URIorCURIE]])

slots.Eksamensgruppemedlemskap_foretrukketSkole = Slot(uri=UTD.foretrukketSkole, name="Eksamensgruppemedlemskap_foretrukketSkole", curie=UTD.curie('foretrukketSkole'),
                   model_uri=UTD.Eksamensgruppemedlemskap_foretrukketSkole, domain=Eksamensgruppemedlemskap, range=Optional[Union[bool, Bool]])

slots.Eksamensgruppemedlemskap_foretrukketSensor = Slot(uri=UTD.foretrukketSensor, name="Eksamensgruppemedlemskap_foretrukketSensor", curie=UTD.curie('foretrukketSensor'),
                   model_uri=UTD.Eksamensgruppemedlemskap_foretrukketSensor, domain=Eksamensgruppemedlemskap, range=Optional[Union[bool, Bool]])

slots.Eksamensgruppemedlemskap_betalingsstatus = Slot(uri=UTD.betalingsstatus, name="Eksamensgruppemedlemskap_betalingsstatus", curie=UTD.curie('betalingsstatus'),
                   model_uri=UTD.Eksamensgruppemedlemskap_betalingsstatus, domain=Eksamensgruppemedlemskap, range=Optional[Union[str, BetalingsstatusId]])

slots.Eksamensgruppemedlemskap_elevforhold = Slot(uri=UTD.elevforhold, name="Eksamensgruppemedlemskap_elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.Eksamensgruppemedlemskap_elevforhold, domain=Eksamensgruppemedlemskap, range=Union[str, ElevforholdId])

slots.Eksamensgruppemedlemskap_eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="Eksamensgruppemedlemskap_eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.Eksamensgruppemedlemskap_eksamensgruppe, domain=Eksamensgruppemedlemskap, range=Union[str, EksamensgruppeId])

slots.Eksamensgruppemedlemskap_nus = Slot(uri=UTD.nus, name="Eksamensgruppemedlemskap_nus", curie=UTD.curie('nus'),
                   model_uri=UTD.Eksamensgruppemedlemskap_nus, domain=Eksamensgruppemedlemskap, range=Optional[Union[str, KarakterstatusId]])

slots.Eksamensvurdering_eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="Eksamensvurdering_eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.Eksamensvurdering_eksamensgruppe, domain=Eksamensvurdering, range=Union[str, EksamensgruppeId])

slots.Eksamensvurdering_karakterhistorie = Slot(uri=UTD.karakterhistorie, name="Eksamensvurdering_karakterhistorie", curie=UTD.curie('karakterhistorie'),
                   model_uri=UTD.Eksamensvurdering_karakterhistorie, domain=Eksamensvurdering, range=Optional[Union[Union[str, KarakterhistorieId], list[Union[str, KarakterhistorieId]]]])

slots.Eksamensvurdering_elevvurdering = Slot(uri=UTD.elevvurdering, name="Eksamensvurdering_elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.Eksamensvurdering_elevvurdering, domain=Eksamensvurdering, range=Union[str, ElevvurderingId])

slots.Elevfravar_elevforhold = Slot(uri=UTD.elevforhold, name="Elevfravar_elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.Elevfravar_elevforhold, domain=Elevfravar, range=Union[str, ElevforholdId])

slots.Elevfravar_fraversregistrering = Slot(uri=UTD.fraversregistrering, name="Elevfravar_fraversregistrering", curie=UTD.curie('fraversregistrering'),
                   model_uri=UTD.Elevfravar_fraversregistrering, domain=Elevfravar, range=Optional[Union[Union[str, FraversregistreringId], list[Union[str, FraversregistreringId]]]])

slots.Elevvurdering_elevforhold = Slot(uri=UTD.elevforhold, name="Elevvurdering_elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.Elevvurdering_elevforhold, domain=Elevvurdering, range=Union[str, ElevforholdId])

slots.Elevvurdering_eksamensvurdering = Slot(uri=UTD.eksamensvurdering, name="Elevvurdering_eksamensvurdering", curie=UTD.curie('eksamensvurdering'),
                   model_uri=UTD.Elevvurdering_eksamensvurdering, domain=Elevvurdering, range=Optional[Union[Union[str, EksamensvurderingId], list[Union[str, EksamensvurderingId]]]])

slots.Elevvurdering_sluttfagvurdering = Slot(uri=UTD.sluttfagvurdering, name="Elevvurdering_sluttfagvurdering", curie=UTD.curie('sluttfagvurdering'),
                   model_uri=UTD.Elevvurdering_sluttfagvurdering, domain=Elevvurdering, range=Optional[Union[Union[str, SluttfagvurderingId], list[Union[str, SluttfagvurderingId]]]])

slots.Elevvurdering_halvaarsfagvurdering = Slot(uri=UTD.halvaarsfagvurdering, name="Elevvurdering_halvaarsfagvurdering", curie=UTD.curie('halvaarsfagvurdering'),
                   model_uri=UTD.Elevvurdering_halvaarsfagvurdering, domain=Elevvurdering, range=Optional[Union[Union[str, HalvaarsfagvurderingId], list[Union[str, HalvaarsfagvurderingId]]]])

slots.Elevvurdering_underveisfagvurdering = Slot(uri=UTD.underveisfagvurdering, name="Elevvurdering_underveisfagvurdering", curie=UTD.curie('underveisfagvurdering'),
                   model_uri=UTD.Elevvurdering_underveisfagvurdering, domain=Elevvurdering, range=Optional[Union[Union[str, UnderveisfagvurderingId], list[Union[str, UnderveisfagvurderingId]]]])

slots.Elevvurdering_halvaarsordensvurdering = Slot(uri=UTD.halvaarsordensvurdering, name="Elevvurdering_halvaarsordensvurdering", curie=UTD.curie('halvaarsordensvurdering'),
                   model_uri=UTD.Elevvurdering_halvaarsordensvurdering, domain=Elevvurdering, range=Optional[Union[Union[str, HalvaarsordensvurderingId], list[Union[str, HalvaarsordensvurderingId]]]])

slots.Elevvurdering_underveisordensvurdering = Slot(uri=UTD.underveisordensvurdering, name="Elevvurdering_underveisordensvurdering", curie=UTD.curie('underveisordensvurdering'),
                   model_uri=UTD.Elevvurdering_underveisordensvurdering, domain=Elevvurdering, range=Optional[Union[Union[str, UnderveisordensvurderingId], list[Union[str, UnderveisordensvurderingId]]]])

slots.Elevvurdering_sluttordensvurdering = Slot(uri=UTD.sluttordensvurdering, name="Elevvurdering_sluttordensvurdering", curie=UTD.curie('sluttordensvurdering'),
                   model_uri=UTD.Elevvurdering_sluttordensvurdering, domain=Elevvurdering, range=Optional[Union[Union[str, SluttordensvurderingId], list[Union[str, SluttordensvurderingId]]]])

slots.Elevvurdering_vitnemalsmerknad = Slot(uri=UTD.vitnemalsmerknad, name="Elevvurdering_vitnemalsmerknad", curie=UTD.curie('vitnemalsmerknad'),
                   model_uri=UTD.Elevvurdering_vitnemalsmerknad, domain=Elevvurdering, range=Optional[Union[str, VitnemalsmerknadId]])

slots.Fravarsoversikt_halvaar = Slot(uri=UTD.halvaar, name="Fravarsoversikt_halvaar", curie=UTD.curie('halvaar'),
                   model_uri=UTD.Fravarsoversikt_halvaar, domain=Fravarsoversikt, range=Union[dict, "Fravarsprosent"])

slots.Fravarsoversikt_skoleaarFravar = Slot(uri=UTD.skoleaarFravar, name="Fravarsoversikt_skoleaarFravar", curie=UTD.curie('skoleaarFravar'),
                   model_uri=UTD.Fravarsoversikt_skoleaarFravar, domain=Fravarsoversikt, range=Union[dict, "Fravarsprosent"])

slots.Fravarsoversikt_elevforhold = Slot(uri=UTD.elevforhold, name="Fravarsoversikt_elevforhold", curie=UTD.curie('elevforhold'),
                   model_uri=UTD.Fravarsoversikt_elevforhold, domain=Fravarsoversikt, range=Union[str, ElevforholdId])

slots.Fravarsoversikt_fag = Slot(uri=UTD.fag, name="Fravarsoversikt_fag", curie=UTD.curie('fag'),
                   model_uri=UTD.Fravarsoversikt_fag, domain=Fravarsoversikt, range=Union[str, FagId])

slots.Fravarsprosent_fravaerstimer = Slot(uri=UTD.fravaerstimer, name="Fravarsprosent_fravaerstimer", curie=UTD.curie('fravaerstimer'),
                   model_uri=UTD.Fravarsprosent_fravaerstimer, domain=Fravarsprosent, range=int)

slots.Fravarsprosent_prosent = Slot(uri=UTD.prosent, name="Fravarsprosent_prosent", curie=UTD.curie('prosent'),
                   model_uri=UTD.Fravarsprosent_prosent, domain=Fravarsprosent, range=int)

slots.Fravarsprosent_undervisningstimer = Slot(uri=UTD.undervisningstimer, name="Fravarsprosent_undervisningstimer", curie=UTD.curie('undervisningstimer'),
                   model_uri=UTD.Fravarsprosent_undervisningstimer, domain=Fravarsprosent, range=int)

slots.Fraversregistrering_forersPaaVitnemaal = Slot(uri=UTD.forersPaaVitnemaal, name="Fraversregistrering_forersPaaVitnemaal", curie=UTD.curie('forersPaaVitnemaal'),
                   model_uri=UTD.Fraversregistrering_forersPaaVitnemaal, domain=Fraversregistrering, range=Union[bool, Bool])

slots.Fraversregistrering_kommentar = Slot(uri=UTD.kommentar, name="Fraversregistrering_kommentar", curie=UTD.curie('kommentar'),
                   model_uri=UTD.Fraversregistrering_kommentar, domain=Fraversregistrering, range=Optional[str])

slots.Fraversregistrering_periode = Slot(uri=UTD.periode, name="Fraversregistrering_periode", curie=UTD.curie('periode'),
                   model_uri=UTD.Fraversregistrering_periode, domain=Fraversregistrering, range=Union[dict, "Periode"])

slots.Fraversregistrering_registrertAv = Slot(uri=UTD.registrertAv, name="Fraversregistrering_registrertAv", curie=UTD.curie('registrertAv'),
                   model_uri=UTD.Fraversregistrering_registrertAv, domain=Fraversregistrering, range=Optional[Union[str, SkoleressursId]])

slots.Fraversregistrering_faggruppe = Slot(uri=UTD.faggruppe, name="Fraversregistrering_faggruppe", curie=UTD.curie('faggruppe'),
                   model_uri=UTD.Fraversregistrering_faggruppe, domain=Fraversregistrering, range=Optional[Union[str, FaggruppeId]])

slots.Fraversregistrering_undervisningsgruppe = Slot(uri=UTD.undervisningsgruppe, name="Fraversregistrering_undervisningsgruppe", curie=UTD.curie('undervisningsgruppe'),
                   model_uri=UTD.Fraversregistrering_undervisningsgruppe, domain=Fraversregistrering, range=Union[str, UndervisningsgruppeId])

slots.Fraversregistrering_elevfravar = Slot(uri=UTD.elevfravar, name="Fraversregistrering_elevfravar", curie=UTD.curie('elevfravar'),
                   model_uri=UTD.Fraversregistrering_elevfravar, domain=Fraversregistrering, range=Optional[Union[str, ElevfravarId]])

slots.Fraversregistrering_fravartype = Slot(uri=UTD.fravartype, name="Fraversregistrering_fravartype", curie=UTD.curie('fravartype'),
                   model_uri=UTD.Fraversregistrering_fravartype, domain=Fraversregistrering, range=Union[str, FravartypeId])

slots.Halvaarsfagvurdering_elevvurdering = Slot(uri=UTD.elevvurdering, name="Halvaarsfagvurdering_elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.Halvaarsfagvurdering_elevvurdering, domain=Halvaarsfagvurdering, range=Union[str, ElevvurderingId])

slots.Halvaarsordensvurdering_elevvurdering = Slot(uri=UTD.elevvurdering, name="Halvaarsordensvurdering_elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.Halvaarsordensvurdering_elevvurdering, domain=Halvaarsordensvurdering, range=Union[str, ElevvurderingId])

slots.Karakterhistorie_endretDato = Slot(uri=UTD.endretDato, name="Karakterhistorie_endretDato", curie=UTD.curie('endretDato'),
                   model_uri=UTD.Karakterhistorie_endretDato, domain=Karakterhistorie, range=Union[str, XSDDateTime])

slots.Karakterhistorie_oppdatertAv = Slot(uri=UTD.oppdatertAv, name="Karakterhistorie_oppdatertAv", curie=UTD.curie('oppdatertAv'),
                   model_uri=UTD.Karakterhistorie_oppdatertAv, domain=Karakterhistorie, range=Optional[Union[str, SkoleressursId]])

slots.Karakterhistorie_opprinneligKarakterverdi = Slot(uri=UTD.opprinneligKarakterverdi, name="Karakterhistorie_opprinneligKarakterverdi", curie=UTD.curie('opprinneligKarakterverdi'),
                   model_uri=UTD.Karakterhistorie_opprinneligKarakterverdi, domain=Karakterhistorie, range=Optional[Union[str, KarakterverdiId]])

slots.Karakterhistorie_opprinneligKarakterstatus = Slot(uri=UTD.opprinneligKarakterstatus, name="Karakterhistorie_opprinneligKarakterstatus", curie=UTD.curie('opprinneligKarakterstatus'),
                   model_uri=UTD.Karakterhistorie_opprinneligKarakterstatus, domain=Karakterhistorie, range=Optional[Union[str, KarakterstatusId]])

slots.Karakterhistorie_karakterverdi = Slot(uri=UTD.karakterverdi, name="Karakterhistorie_karakterverdi", curie=UTD.curie('karakterverdi'),
                   model_uri=UTD.Karakterhistorie_karakterverdi, domain=Karakterhistorie, range=Optional[Union[str, KarakterverdiId]])

slots.Karakterhistorie_karakterstatus = Slot(uri=UTD.karakterstatus, name="Karakterhistorie_karakterstatus", curie=UTD.curie('karakterstatus'),
                   model_uri=UTD.Karakterhistorie_karakterstatus, domain=Karakterhistorie, range=Optional[Union[str, KarakterstatusId]])

slots.Sensor_aktiv = Slot(uri=UTD.aktiv, name="Sensor_aktiv", curie=UTD.curie('aktiv'),
                   model_uri=UTD.Sensor_aktiv, domain=Sensor, range=Union[bool, Bool])

slots.Sensor_sensornummer = Slot(uri=UTD.sensornummer, name="Sensor_sensornummer", curie=UTD.curie('sensornummer'),
                   model_uri=UTD.Sensor_sensornummer, domain=Sensor, range=Optional[int])

slots.Sensor_skoleressurs = Slot(uri=UTD.skoleressurs, name="Sensor_skoleressurs", curie=UTD.curie('skoleressurs'),
                   model_uri=UTD.Sensor_skoleressurs, domain=Sensor, range=Union[str, SkoleressursId])

slots.Sensor_eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="Sensor_eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.Sensor_eksamensgruppe, domain=Sensor, range=Union[str, EksamensgruppeId])

slots.Sluttfagvurdering_eksamensgruppe = Slot(uri=UTD.eksamensgruppe, name="Sluttfagvurdering_eksamensgruppe", curie=UTD.curie('eksamensgruppe'),
                   model_uri=UTD.Sluttfagvurdering_eksamensgruppe, domain=Sluttfagvurdering, range=Optional[Union[str, EksamensgruppeId]])

slots.Sluttfagvurdering_elevvurdering = Slot(uri=UTD.elevvurdering, name="Sluttfagvurdering_elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.Sluttfagvurdering_elevvurdering, domain=Sluttfagvurdering, range=Union[str, ElevvurderingId])

slots.Sluttfagvurdering_karakterhistorie = Slot(uri=UTD.karakterhistorie, name="Sluttfagvurdering_karakterhistorie", curie=UTD.curie('karakterhistorie'),
                   model_uri=UTD.Sluttfagvurdering_karakterhistorie, domain=Sluttfagvurdering, range=Optional[Union[Union[str, KarakterhistorieId], list[Union[str, KarakterhistorieId]]]])

slots.Sluttordensvurdering_elevvurdering = Slot(uri=UTD.elevvurdering, name="Sluttordensvurdering_elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.Sluttordensvurdering_elevvurdering, domain=Sluttordensvurdering, range=Union[str, ElevvurderingId])

slots.Underveisfagvurdering_elevvurdering = Slot(uri=UTD.elevvurdering, name="Underveisfagvurdering_elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.Underveisfagvurdering_elevvurdering, domain=Underveisfagvurdering, range=Union[str, ElevvurderingId])

slots.Underveisordensvurdering_elevvurdering = Slot(uri=UTD.elevvurdering, name="Underveisordensvurdering_elevvurdering", curie=UTD.curie('elevvurdering'),
                   model_uri=UTD.Underveisordensvurdering_elevvurdering, domain=Underveisordensvurdering, range=Union[str, ElevvurderingId])

slots.AvlagtProve_provedato = Slot(uri=UTD.provedato, name="AvlagtProve_provedato", curie=UTD.curie('provedato'),
                   model_uri=UTD.AvlagtProve_provedato, domain=AvlagtProve, range=Optional[Union[str, XSDDate]])

slots.AvlagtProve_laerling = Slot(uri=FINT.laerling, name="AvlagtProve_laerling", curie=FINT.curie('laerling'),
                   model_uri=UTD.AvlagtProve_laerling, domain=AvlagtProve, range=Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]])

slots.AvlagtProve_provestatus = Slot(uri=UTD.provestatus, name="AvlagtProve_provestatus", curie=UTD.curie('provestatus'),
                   model_uri=UTD.AvlagtProve_provestatus, domain=AvlagtProve, range=Optional[Union[str, ProvestatusId]])

slots.AvlagtProve_fullfortkode = Slot(uri=UTD.fullfortkode, name="AvlagtProve_fullfortkode", curie=UTD.curie('fullfortkode'),
                   model_uri=UTD.AvlagtProve_fullfortkode, domain=AvlagtProve, range=Optional[Union[str, FullfortkodeId]])

slots.AvlagtProve_brevtype = Slot(uri=UTD.brevtype, name="AvlagtProve_brevtype", curie=UTD.curie('brevtype'),
                   model_uri=UTD.AvlagtProve_brevtype, domain=AvlagtProve, range=Optional[Union[str, BrevtypeId]])

slots.AvlagtProve_bevistype = Slot(uri=UTD.bevistype, name="AvlagtProve_bevistype", curie=UTD.curie('bevistype'),
                   model_uri=UTD.AvlagtProve_bevistype, domain=AvlagtProve, range=Optional[Union[str, BevistypeId]])

slots.Laerling_kontraktstype = Slot(uri=UTD.kontraktstype, name="Laerling_kontraktstype", curie=UTD.curie('kontraktstype'),
                   model_uri=UTD.Laerling_kontraktstype, domain=Laerling, range=Optional[str])

slots.Laerling_laretid = Slot(uri=UTD.laretid, name="Laerling_laretid", curie=UTD.curie('laretid'),
                   model_uri=UTD.Laerling_laretid, domain=Laerling, range=Optional[Union[dict, "Periode"]])

slots.Laerling_person = Slot(uri=FINT.person, name="Laerling_person", curie=FINT.curie('person'),
                   model_uri=UTD.Laerling_person, domain=Laerling, range=Union[str, PersonId])

slots.Laerling_bedrift = Slot(uri=UTD.bedrift, name="Laerling_bedrift", curie=UTD.curie('bedrift'),
                   model_uri=UTD.Laerling_bedrift, domain=Laerling, range=Optional[Union[str, URIorCURIE]])

slots.Laerling_avlagtprove = Slot(uri=UTD.avlagtprove, name="Laerling_avlagtprove", curie=UTD.curie('avlagtprove'),
                   model_uri=UTD.Laerling_avlagtprove, domain=Laerling, range=Optional[Union[Union[str, AvlagtProveId], list[Union[str, AvlagtProveId]]]])

slots.Laerling_programomrade = Slot(uri=UTD.programomrade, name="Laerling_programomrade", curie=UTD.curie('programomrade'),
                   model_uri=UTD.Laerling_programomrade, domain=Laerling, range=Optional[Union[str, ProgramomradeId]])

slots.OtUngdom_person = Slot(uri=FINT.person, name="OtUngdom_person", curie=FINT.curie('person'),
                   model_uri=UTD.OtUngdom_person, domain=OtUngdom, range=Union[str, PersonId])

slots.OtUngdom_status = Slot(uri=UTD.status, name="OtUngdom_status", curie=UTD.curie('status'),
                   model_uri=UTD.OtUngdom_status, domain=OtUngdom, range=Optional[Union[str, OtStatusId]])

slots.OtUngdom_enhet = Slot(uri=UTD.enhet, name="OtUngdom_enhet", curie=UTD.curie('enhet'),
                   model_uri=UTD.OtUngdom_enhet, domain=OtUngdom, range=Optional[Union[str, OtEnhetId]])

slots.OtUngdom_programomrade = Slot(uri=UTD.programomrade, name="OtUngdom_programomrade", curie=UTD.curie('programomrade'),
                   model_uri=UTD.OtUngdom_programomrade, domain=OtUngdom, range=Optional[Union[str, ProgramomradeId]])

slots.Avbruddsaarsak_kode = Slot(uri=FINT.kode, name="Avbruddsaarsak_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Avbruddsaarsak_kode, domain=Avbruddsaarsak, range=str)

slots.Avbruddsaarsak_navn = Slot(uri=FINT.navn, name="Avbruddsaarsak_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Avbruddsaarsak_navn, domain=Avbruddsaarsak, range=str)

slots.Avbruddsaarsak_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Avbruddsaarsak_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Avbruddsaarsak_gyldighetsperiode, domain=Avbruddsaarsak, range=Optional[Union[dict, "Periode"]])

slots.Avbruddsaarsak_passiv = Slot(uri=FINT.passiv, name="Avbruddsaarsak_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Avbruddsaarsak_passiv, domain=Avbruddsaarsak, range=Optional[Union[bool, Bool]])

slots.Betalingsstatus_kode = Slot(uri=FINT.kode, name="Betalingsstatus_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Betalingsstatus_kode, domain=Betalingsstatus, range=str)

slots.Betalingsstatus_navn = Slot(uri=FINT.navn, name="Betalingsstatus_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Betalingsstatus_navn, domain=Betalingsstatus, range=str)

slots.Betalingsstatus_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Betalingsstatus_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Betalingsstatus_gyldighetsperiode, domain=Betalingsstatus, range=Optional[Union[dict, "Periode"]])

slots.Betalingsstatus_passiv = Slot(uri=FINT.passiv, name="Betalingsstatus_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Betalingsstatus_passiv, domain=Betalingsstatus, range=Optional[Union[bool, Bool]])

slots.Bevistype_kode = Slot(uri=FINT.kode, name="Bevistype_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Bevistype_kode, domain=Bevistype, range=str)

slots.Bevistype_navn = Slot(uri=FINT.navn, name="Bevistype_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Bevistype_navn, domain=Bevistype, range=str)

slots.Bevistype_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Bevistype_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Bevistype_gyldighetsperiode, domain=Bevistype, range=Optional[Union[dict, "Periode"]])

slots.Bevistype_passiv = Slot(uri=FINT.passiv, name="Bevistype_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Bevistype_passiv, domain=Bevistype, range=Optional[Union[bool, Bool]])

slots.Brevtype_kode = Slot(uri=FINT.kode, name="Brevtype_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Brevtype_kode, domain=Brevtype, range=str)

slots.Brevtype_navn = Slot(uri=FINT.navn, name="Brevtype_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Brevtype_navn, domain=Brevtype, range=str)

slots.Brevtype_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Brevtype_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Brevtype_gyldighetsperiode, domain=Brevtype, range=Optional[Union[dict, "Periode"]])

slots.Brevtype_passiv = Slot(uri=FINT.passiv, name="Brevtype_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Brevtype_passiv, domain=Brevtype, range=Optional[Union[bool, Bool]])

slots.Eksamensform_kode = Slot(uri=FINT.kode, name="Eksamensform_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Eksamensform_kode, domain=Eksamensform, range=str)

slots.Eksamensform_navn = Slot(uri=FINT.navn, name="Eksamensform_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Eksamensform_navn, domain=Eksamensform, range=str)

slots.Eksamensform_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Eksamensform_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Eksamensform_gyldighetsperiode, domain=Eksamensform, range=Optional[Union[dict, "Periode"]])

slots.Eksamensform_passiv = Slot(uri=FINT.passiv, name="Eksamensform_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Eksamensform_passiv, domain=Eksamensform, range=Optional[Union[bool, Bool]])

slots.Elevkategori_kode = Slot(uri=FINT.kode, name="Elevkategori_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Elevkategori_kode, domain=Elevkategori, range=str)

slots.Elevkategori_navn = Slot(uri=FINT.navn, name="Elevkategori_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Elevkategori_navn, domain=Elevkategori, range=str)

slots.Elevkategori_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Elevkategori_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Elevkategori_gyldighetsperiode, domain=Elevkategori, range=Optional[Union[dict, "Periode"]])

slots.Elevkategori_passiv = Slot(uri=FINT.passiv, name="Elevkategori_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Elevkategori_passiv, domain=Elevkategori, range=Optional[Union[bool, Bool]])

slots.Fagmerknad_kode = Slot(uri=FINT.kode, name="Fagmerknad_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Fagmerknad_kode, domain=Fagmerknad, range=str)

slots.Fagmerknad_navn = Slot(uri=FINT.navn, name="Fagmerknad_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Fagmerknad_navn, domain=Fagmerknad, range=str)

slots.Fagmerknad_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Fagmerknad_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Fagmerknad_gyldighetsperiode, domain=Fagmerknad, range=Optional[Union[dict, "Periode"]])

slots.Fagmerknad_passiv = Slot(uri=FINT.passiv, name="Fagmerknad_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Fagmerknad_passiv, domain=Fagmerknad, range=Optional[Union[bool, Bool]])

slots.Fagstatus_kode = Slot(uri=FINT.kode, name="Fagstatus_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Fagstatus_kode, domain=Fagstatus, range=str)

slots.Fagstatus_navn = Slot(uri=FINT.navn, name="Fagstatus_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Fagstatus_navn, domain=Fagstatus, range=str)

slots.Fagstatus_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Fagstatus_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Fagstatus_gyldighetsperiode, domain=Fagstatus, range=Optional[Union[dict, "Periode"]])

slots.Fagstatus_passiv = Slot(uri=FINT.passiv, name="Fagstatus_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Fagstatus_passiv, domain=Fagstatus, range=Optional[Union[bool, Bool]])

slots.Fravartype_kode = Slot(uri=FINT.kode, name="Fravartype_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Fravartype_kode, domain=Fravartype, range=str)

slots.Fravartype_navn = Slot(uri=FINT.navn, name="Fravartype_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Fravartype_navn, domain=Fravartype, range=str)

slots.Fravartype_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Fravartype_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Fravartype_gyldighetsperiode, domain=Fravartype, range=Optional[Union[dict, "Periode"]])

slots.Fravartype_passiv = Slot(uri=FINT.passiv, name="Fravartype_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Fravartype_passiv, domain=Fravartype, range=Optional[Union[bool, Bool]])

slots.Fullfortkode_kode = Slot(uri=FINT.kode, name="Fullfortkode_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Fullfortkode_kode, domain=Fullfortkode, range=str)

slots.Fullfortkode_navn = Slot(uri=FINT.navn, name="Fullfortkode_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Fullfortkode_navn, domain=Fullfortkode, range=str)

slots.Fullfortkode_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Fullfortkode_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Fullfortkode_gyldighetsperiode, domain=Fullfortkode, range=Optional[Union[dict, "Periode"]])

slots.Fullfortkode_passiv = Slot(uri=FINT.passiv, name="Fullfortkode_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Fullfortkode_passiv, domain=Fullfortkode, range=Optional[Union[bool, Bool]])

slots.Karakterskala_kode = Slot(uri=FINT.kode, name="Karakterskala_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Karakterskala_kode, domain=Karakterskala, range=str)

slots.Karakterskala_navn = Slot(uri=FINT.navn, name="Karakterskala_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Karakterskala_navn, domain=Karakterskala, range=str)

slots.Karakterskala_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Karakterskala_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Karakterskala_gyldighetsperiode, domain=Karakterskala, range=Optional[Union[dict, "Periode"]])

slots.Karakterskala_passiv = Slot(uri=FINT.passiv, name="Karakterskala_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Karakterskala_passiv, domain=Karakterskala, range=Optional[Union[bool, Bool]])

slots.Karakterskala_verdi = Slot(uri=UTD.verdi, name="Karakterskala_verdi", curie=UTD.curie('verdi'),
                   model_uri=UTD.Karakterskala_verdi, domain=Karakterskala, range=Optional[Union[Union[str, KarakterverdiId], list[Union[str, KarakterverdiId]]]])

slots.Karakterskala_vigoreferanse = Slot(uri=UTD.vigoreferanse, name="Karakterskala_vigoreferanse", curie=UTD.curie('vigoreferanse'),
                   model_uri=UTD.Karakterskala_vigoreferanse, domain=Karakterskala, range=Optional[Union[str, URIorCURIE]])

slots.Karakterstatus_kode = Slot(uri=FINT.kode, name="Karakterstatus_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Karakterstatus_kode, domain=Karakterstatus, range=str)

slots.Karakterstatus_navn = Slot(uri=FINT.navn, name="Karakterstatus_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Karakterstatus_navn, domain=Karakterstatus, range=str)

slots.Karakterstatus_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Karakterstatus_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Karakterstatus_gyldighetsperiode, domain=Karakterstatus, range=Optional[Union[dict, "Periode"]])

slots.Karakterstatus_passiv = Slot(uri=FINT.passiv, name="Karakterstatus_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Karakterstatus_passiv, domain=Karakterstatus, range=Optional[Union[bool, Bool]])

slots.Karakterverdi_kode = Slot(uri=FINT.kode, name="Karakterverdi_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Karakterverdi_kode, domain=Karakterverdi, range=str)

slots.Karakterverdi_navn = Slot(uri=FINT.navn, name="Karakterverdi_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Karakterverdi_navn, domain=Karakterverdi, range=str)

slots.Karakterverdi_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Karakterverdi_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Karakterverdi_gyldighetsperiode, domain=Karakterverdi, range=Optional[Union[dict, "Periode"]])

slots.Karakterverdi_passiv = Slot(uri=FINT.passiv, name="Karakterverdi_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Karakterverdi_passiv, domain=Karakterverdi, range=Optional[Union[bool, Bool]])

slots.Karakterverdi_skala = Slot(uri=UTD.skala, name="Karakterverdi_skala", curie=UTD.curie('skala'),
                   model_uri=UTD.Karakterverdi_skala, domain=Karakterverdi, range=Union[str, KarakterskalaId])

slots.OtEnhet_kode = Slot(uri=FINT.kode, name="OtEnhet_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.OtEnhet_kode, domain=OtEnhet, range=str)

slots.OtEnhet_navn = Slot(uri=FINT.navn, name="OtEnhet_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.OtEnhet_navn, domain=OtEnhet, range=str)

slots.OtEnhet_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="OtEnhet_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.OtEnhet_gyldighetsperiode, domain=OtEnhet, range=Optional[Union[dict, "Periode"]])

slots.OtEnhet_passiv = Slot(uri=FINT.passiv, name="OtEnhet_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.OtEnhet_passiv, domain=OtEnhet, range=Optional[Union[bool, Bool]])

slots.OtEnhet_kommune = Slot(uri=FINT.kommune, name="OtEnhet_kommune", curie=FINT.curie('kommune'),
                   model_uri=UTD.OtEnhet_kommune, domain=OtEnhet, range=Union[str, KommuneId])

slots.OtStatus_kode = Slot(uri=FINT.kode, name="OtStatus_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.OtStatus_kode, domain=OtStatus, range=str)

slots.OtStatus_navn = Slot(uri=FINT.navn, name="OtStatus_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.OtStatus_navn, domain=OtStatus, range=str)

slots.OtStatus_beskrivelse = Slot(uri=FINT.beskrivelse, name="OtStatus_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=UTD.OtStatus_beskrivelse, domain=OtStatus, range=Optional[str])

slots.OtStatus_type = Slot(uri=FINT.type, name="OtStatus_type", curie=FINT.curie('type'),
                   model_uri=UTD.OtStatus_type, domain=OtStatus, range=str)

slots.OtStatus_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="OtStatus_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.OtStatus_gyldighetsperiode, domain=OtStatus, range=Optional[Union[dict, "Periode"]])

slots.OtStatus_passiv = Slot(uri=FINT.passiv, name="OtStatus_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.OtStatus_passiv, domain=OtStatus, range=Optional[Union[bool, Bool]])

slots.Provestatus_kode = Slot(uri=FINT.kode, name="Provestatus_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Provestatus_kode, domain=Provestatus, range=str)

slots.Provestatus_navn = Slot(uri=FINT.navn, name="Provestatus_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Provestatus_navn, domain=Provestatus, range=str)

slots.Provestatus_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Provestatus_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Provestatus_gyldighetsperiode, domain=Provestatus, range=Optional[Union[dict, "Periode"]])

slots.Provestatus_passiv = Slot(uri=FINT.passiv, name="Provestatus_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Provestatus_passiv, domain=Provestatus, range=Optional[Union[bool, Bool]])

slots.Skoleaar_kode = Slot(uri=FINT.kode, name="Skoleaar_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Skoleaar_kode, domain=Skoleaar, range=str)

slots.Skoleaar_navn = Slot(uri=FINT.navn, name="Skoleaar_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Skoleaar_navn, domain=Skoleaar, range=str)

slots.Skoleaar_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Skoleaar_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Skoleaar_gyldighetsperiode, domain=Skoleaar, range=Optional[Union[dict, "Periode"]])

slots.Skoleaar_passiv = Slot(uri=FINT.passiv, name="Skoleaar_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Skoleaar_passiv, domain=Skoleaar, range=Optional[Union[bool, Bool]])

slots.Skoleeiertype_kode = Slot(uri=FINT.kode, name="Skoleeiertype_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Skoleeiertype_kode, domain=Skoleeiertype, range=str)

slots.Skoleeiertype_navn = Slot(uri=FINT.navn, name="Skoleeiertype_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Skoleeiertype_navn, domain=Skoleeiertype, range=str)

slots.Skoleeiertype_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Skoleeiertype_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Skoleeiertype_gyldighetsperiode, domain=Skoleeiertype, range=Optional[Union[dict, "Periode"]])

slots.Skoleeiertype_passiv = Slot(uri=FINT.passiv, name="Skoleeiertype_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Skoleeiertype_passiv, domain=Skoleeiertype, range=Optional[Union[bool, Bool]])

slots.Termin_kode = Slot(uri=FINT.kode, name="Termin_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Termin_kode, domain=Termin, range=str)

slots.Termin_navn = Slot(uri=FINT.navn, name="Termin_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Termin_navn, domain=Termin, range=str)

slots.Termin_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Termin_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Termin_gyldighetsperiode, domain=Termin, range=Optional[Union[dict, "Periode"]])

slots.Termin_passiv = Slot(uri=FINT.passiv, name="Termin_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Termin_passiv, domain=Termin, range=Optional[Union[bool, Bool]])

slots.Tilrettelegging_kode = Slot(uri=FINT.kode, name="Tilrettelegging_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Tilrettelegging_kode, domain=Tilrettelegging, range=str)

slots.Tilrettelegging_navn = Slot(uri=FINT.navn, name="Tilrettelegging_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Tilrettelegging_navn, domain=Tilrettelegging, range=str)

slots.Tilrettelegging_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Tilrettelegging_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Tilrettelegging_gyldighetsperiode, domain=Tilrettelegging, range=Optional[Union[dict, "Periode"]])

slots.Tilrettelegging_passiv = Slot(uri=FINT.passiv, name="Tilrettelegging_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Tilrettelegging_passiv, domain=Tilrettelegging, range=Optional[Union[bool, Bool]])

slots.Varseltype_kode = Slot(uri=FINT.kode, name="Varseltype_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Varseltype_kode, domain=Varseltype, range=str)

slots.Varseltype_navn = Slot(uri=FINT.navn, name="Varseltype_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Varseltype_navn, domain=Varseltype, range=str)

slots.Varseltype_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Varseltype_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Varseltype_gyldighetsperiode, domain=Varseltype, range=Optional[Union[dict, "Periode"]])

slots.Varseltype_passiv = Slot(uri=FINT.passiv, name="Varseltype_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Varseltype_passiv, domain=Varseltype, range=Optional[Union[bool, Bool]])

slots.Vitnemalsmerknad_kode = Slot(uri=FINT.kode, name="Vitnemalsmerknad_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Vitnemalsmerknad_kode, domain=Vitnemalsmerknad, range=str)

slots.Vitnemalsmerknad_navn = Slot(uri=FINT.navn, name="Vitnemalsmerknad_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Vitnemalsmerknad_navn, domain=Vitnemalsmerknad, range=str)

slots.Vitnemalsmerknad_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Vitnemalsmerknad_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Vitnemalsmerknad_gyldighetsperiode, domain=Vitnemalsmerknad, range=Optional[Union[dict, "Periode"]])

slots.Vitnemalsmerknad_passiv = Slot(uri=FINT.passiv, name="Vitnemalsmerknad_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Vitnemalsmerknad_passiv, domain=Vitnemalsmerknad, range=Optional[Union[bool, Bool]])

slots.Aktoer_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Aktoer_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=UTD.Aktoer_kontaktinformasjon, domain=Aktoer, range=Optional[Union[dict, "Kontaktinformasjon"]])

slots.Aktoer_postadresse = Slot(uri=FINT.postadresse, name="Aktoer_postadresse", curie=FINT.curie('postadresse'),
                   model_uri=UTD.Aktoer_postadresse, domain=Aktoer, range=Optional[Union[dict, "Adresse"]])

slots.Begrep_kode = Slot(uri=FINT.kode, name="Begrep_kode", curie=FINT.curie('kode'),
                   model_uri=UTD.Begrep_kode, domain=Begrep, range=str)

slots.Begrep_navn = Slot(uri=FINT.navn, name="Begrep_navn", curie=FINT.curie('navn'),
                   model_uri=UTD.Begrep_navn, domain=Begrep, range=str)

slots.Begrep_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Begrep_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=UTD.Begrep_gyldighetsperiode, domain=Begrep, range=Optional[Union[dict, "Periode"]])

slots.Begrep_passiv = Slot(uri=FINT.passiv, name="Begrep_passiv", curie=FINT.curie('passiv'),
                   model_uri=UTD.Begrep_passiv, domain=Begrep, range=Optional[Union[bool, Bool]])

slots.Elev_elevnummer = Slot(uri=FINT.elevnummer, name="Elev_elevnummer", curie=FINT.curie('elevnummer'),
                   model_uri=UTD.Elev_elevnummer, domain=Elev, range=Optional[Union[dict, "Identifikator"]])

slots.Elev_person = Slot(uri=FINT.person, name="Elev_person", curie=FINT.curie('person'),
                   model_uri=UTD.Elev_person, domain=Elev, range=Optional[Union[str, PersonId]])

slots.Enhet_forretningsadresse = Slot(uri=FINT.forretningsadresse, name="Enhet_forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=UTD.Enhet_forretningsadresse, domain=Enhet, range=Optional[Union[dict, "Adresse"]])

slots.Enhet_organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="Enhet_organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=UTD.Enhet_organisasjonsnavn, domain=Enhet, range=Optional[str])

slots.Enhet_organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="Enhet_organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=UTD.Enhet_organisasjonsnummer, domain=Enhet, range=Optional[Union[dict, "Identifikator"]])

slots.Identifikator_identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="Identifikator_identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=UTD.Identifikator_identifikatorverdi, domain=Identifikator, range=str)

slots.Periode_start = Slot(uri=FINT.start, name="Periode_start", curie=FINT.curie('start'),
                   model_uri=UTD.Periode_start, domain=Periode, range=Union[str, XSDDateTime])

slots.Personnavn_fornavn = Slot(uri=FINT.fornavn, name="Personnavn_fornavn", curie=FINT.curie('fornavn'),
                   model_uri=UTD.Personnavn_fornavn, domain=Personnavn, range=str)

slots.Personnavn_etternavn = Slot(uri=FINT.etternavn, name="Personnavn_etternavn", curie=FINT.curie('etternavn'),
                   model_uri=UTD.Personnavn_etternavn, domain=Personnavn, range=str)

slots.Fylke_kommune = Slot(uri=FINT.kommune, name="Fylke_kommune", curie=FINT.curie('kommune'),
                   model_uri=UTD.Fylke_kommune, domain=Fylke, range=Optional[Union[Union[str, KommuneId], list[Union[str, KommuneId]]]])

slots.Kommune_fylke = Slot(uri=FINT.fylke, name="Kommune_fylke", curie=FINT.curie('fylke'),
                   model_uri=UTD.Kommune_fylke, domain=Kommune, range=Union[str, FylkeId])

slots.Valuta_bokstavkode = Slot(uri=FINT.bokstavkode, name="Valuta_bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=UTD.Valuta_bokstavkode, domain=Valuta, range=Union[dict, Identifikator])

slots.Valuta_valuta_navn = Slot(uri=FINT.valutaNavn, name="Valuta_valuta_navn", curie=FINT.curie('valutaNavn'),
                   model_uri=UTD.Valuta_valuta_navn, domain=Valuta, range=str)

slots.Valuta_nummerkode = Slot(uri=FINT.nummerkode, name="Valuta_nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=UTD.Valuta_nummerkode, domain=Valuta, range=Union[dict, Identifikator])

slots.Person_fodselsnummer = Slot(uri=FINT.fodselsnummer, name="Person_fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=UTD.Person_fodselsnummer, domain=Person, range=Union[dict, Identifikator])

slots.Person_person_navn = Slot(uri=FINT.personNavn, name="Person_person_navn", curie=FINT.curie('personNavn'),
                   model_uri=UTD.Person_person_navn, domain=Person, range=Union[dict, Personnavn])

slots.Person_bilde = Slot(uri=FINT.bilde, name="Person_bilde", curie=FINT.curie('bilde'),
                   model_uri=UTD.Person_bilde, domain=Person, range=Optional[str])

slots.Person_bostedsadresse = Slot(uri=FINT.bostedsadresse, name="Person_bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=UTD.Person_bostedsadresse, domain=Person, range=Optional[Union[dict, Adresse]])

slots.Person_fodselsdato = Slot(uri=FINT.fodselsdato, name="Person_fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=UTD.Person_fodselsdato, domain=Person, range=Optional[Union[str, XSDDate]])

slots.Person_parorende = Slot(uri=FINT.parorende, name="Person_parorende", curie=FINT.curie('parorende'),
                   model_uri=UTD.Person_parorende, domain=Person, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.Person_statsborgerskap = Slot(uri=FINT.statsborgerskap, name="Person_statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=UTD.Person_statsborgerskap, domain=Person, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.Person_kommune = Slot(uri=FINT.kommune, name="Person_kommune", curie=FINT.curie('kommune'),
                   model_uri=UTD.Person_kommune, domain=Person, range=Optional[Union[str, KommuneId]])

slots.Person_kjonn = Slot(uri=FINT.kjonn, name="Person_kjonn", curie=FINT.curie('kjonn'),
                   model_uri=UTD.Person_kjonn, domain=Person, range=Optional[Union[str, KjonnId]])

slots.Person_foreldreansvar = Slot(uri=FINT.foreldreansvar, name="Person_foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=UTD.Person_foreldreansvar, domain=Person, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Person_foreldre = Slot(uri=FINT.foreldre, name="Person_foreldre", curie=FINT.curie('foreldre'),
                   model_uri=UTD.Person_foreldre, domain=Person, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Person_maalform = Slot(uri=FINT.maalform, name="Person_maalform", curie=FINT.curie('maalform'),
                   model_uri=UTD.Person_maalform, domain=Person, range=Optional[Union[str, SpraakId]])

slots.Person_morsmaal = Slot(uri=FINT.morsmaal, name="Person_morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=UTD.Person_morsmaal, domain=Person, range=Optional[Union[str, SpraakId]])

slots.Person_laerling = Slot(uri=FINT.laerling, name="Person_laerling", curie=FINT.curie('laerling'),
                   model_uri=UTD.Person_laerling, domain=Person, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Person_elev = Slot(uri=FINT.elev, name="Person_elev", curie=FINT.curie('elev'),
                   model_uri=UTD.Person_elev, domain=Person, range=Optional[Union[str, ElevId]])

slots.Person_otungdom = Slot(uri=FINT.otungdom, name="Person_otungdom", curie=FINT.curie('otungdom'),
                   model_uri=UTD.Person_otungdom, domain=Person, range=Optional[Union[str, URIorCURIE]])

slots.Kontaktperson_type = Slot(uri=FINT.type, name="Kontaktperson_type", curie=FINT.curie('type'),
                   model_uri=UTD.Kontaktperson_type, domain=Kontaktperson, range=str)

slots.Kontaktperson_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Kontaktperson_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=UTD.Kontaktperson_kontaktinformasjon, domain=Kontaktperson, range=Optional[Union[dict, Kontaktinformasjon]])

slots.Kontaktperson_kontaktperson_navn = Slot(uri=FINT.kontaktpersonNavn, name="Kontaktperson_kontaktperson_navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=UTD.Kontaktperson_kontaktperson_navn, domain=Kontaktperson, range=Optional[Union[dict, Personnavn]])

slots.Kontaktperson_kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="Kontaktperson_kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=UTD.Kontaktperson_kontaktperson, domain=Kontaktperson, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Virksomhet_virksomhetsId = Slot(uri=FINT.virksomhetsId, name="Virksomhet_virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=UTD.Virksomhet_virksomhetsId, domain=Virksomhet, range=Union[dict, Identifikator])

slots.Virksomhet_laerling = Slot(uri=FINT.laerling, name="Virksomhet_laerling", curie=FINT.curie('laerling'),
                   model_uri=UTD.Virksomhet_laerling, domain=Virksomhet, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

