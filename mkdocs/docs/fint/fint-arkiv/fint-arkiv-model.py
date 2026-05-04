# Auto generated from fint-arkiv-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-04T20:07:31
# Schema: fint-arkiv
#
# id: https://data.norge.no/linkml/fint-arkiv
# description: FINT-domenemodell for arkiv basert på Noark 5-standarden. Dekkjer sakshandtering, journalpostar, dokumenthandsaming, tilgangsstyring og spesialiserte saksmappe-typar.
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
ARK = CurieNamespace('ark', 'https://schema.fintlabs.no/arkiv/')
FINT = CurieNamespace('fint', 'https://schema.fintlabs.no/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = ARK


# Types

# Class references
class MappeId(URIorCURIE):
    pass


class SaksmappeId(MappeId):
    pass


class RegistreringId(URIorCURIE):
    pass


class AdministrativEnhetId(URIorCURIE):
    pass


class ArkivdelId(URIorCURIE):
    pass


class ArkivressursId(URIorCURIE):
    pass


class AutorisasjonId(URIorCURIE):
    pass


class DokumentfilId(URIorCURIE):
    pass


class JournalpostId(RegistreringId):
    pass


class KlassifikasjonssystemId(URIorCURIE):
    pass


class TilgangId(URIorCURIE):
    pass


class SakId(SaksmappeId):
    pass


class PersonalmappeId(SaksmappeId):
    pass


class DispensasjonAutomatiskFredaKulturminneId(SaksmappeId):
    pass


class TilskuddFartoyId(SaksmappeId):
    pass


class TilskuddFredaBygningPrivatEieId(SaksmappeId):
    pass


class SoeknadDrosjeloeyveId(SaksmappeId):
    pass


class DokumentbeskrivelseId(URIorCURIE):
    pass


class DokumentStatusId(URIorCURIE):
    pass


class DokumentTypeId(URIorCURIE):
    pass


class FormatId(URIorCURIE):
    pass


class JournalpostTypeId(URIorCURIE):
    pass


class JournalStatusId(URIorCURIE):
    pass


class KlassifikasjonstypeId(URIorCURIE):
    pass


class KorrespondansepartTypeId(URIorCURIE):
    pass


class MerknadstypeId(URIorCURIE):
    pass


class PartRolleId(URIorCURIE):
    pass


class RolleId(URIorCURIE):
    pass


class SaksmappetypeId(URIorCURIE):
    pass


class SaksstatusId(URIorCURIE):
    pass


class SkjermingshjemmelId(URIorCURIE):
    pass


class TilgangsgruppeId(URIorCURIE):
    pass


class TilgangsrestriksjonId(URIorCURIE):
    pass


class TilknyttetRegistreringSomId(URIorCURIE):
    pass


class VariantformatId(URIorCURIE):
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
class ArkivContainer(YAMLRoot):
    """
    Rotcontainer for FINT Arkiv-instansar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["ArkivContainer"]
    class_class_curie: ClassVar[str] = "ark:ArkivContainer"
    class_name: ClassVar[str] = "ArkivContainer"
    class_model_uri: ClassVar[URIRef] = ARK.ArkivContainer

    arkivdelar: Optional[Union[dict[Union[str, ArkivdelId], Union[dict, "Arkivdel"]], list[Union[dict, "Arkivdel"]]]] = empty_dict()
    arkivressursar: Optional[Union[dict[Union[str, ArkivressursId], Union[dict, "Arkivressurs"]], list[Union[dict, "Arkivressurs"]]]] = empty_dict()
    autorisasjonar: Optional[Union[dict[Union[str, AutorisasjonId], Union[dict, "Autorisasjon"]], list[Union[dict, "Autorisasjon"]]]] = empty_dict()
    administrativeEiningar: Optional[Union[dict[Union[str, AdministrativEnhetId], Union[dict, "AdministrativEnhet"]], list[Union[dict, "AdministrativEnhet"]]]] = empty_dict()
    dokumentfiler: Optional[Union[dict[Union[str, DokumentfilId], Union[dict, "Dokumentfil"]], list[Union[dict, "Dokumentfil"]]]] = empty_dict()
    dokumentbeskrivelsar: Optional[Union[dict[Union[str, DokumentbeskrivelseId], Union[dict, "Dokumentbeskrivelse"]], list[Union[dict, "Dokumentbeskrivelse"]]]] = empty_dict()
    journalpostar: Optional[Union[dict[Union[str, JournalpostId], Union[dict, "Journalpost"]], list[Union[dict, "Journalpost"]]]] = empty_dict()
    klassifikasjonssystem: Optional[Union[dict[Union[str, KlassifikasjonssystemId], Union[dict, "Klassifikasjonssystem"]], list[Union[dict, "Klassifikasjonssystem"]]]] = empty_dict()
    tilgangar: Optional[Union[dict[Union[str, TilgangId], Union[dict, "Tilgang"]], list[Union[dict, "Tilgang"]]]] = empty_dict()
    sakar: Optional[Union[dict[Union[str, SakId], Union[dict, "Sak"]], list[Union[dict, "Sak"]]]] = empty_dict()
    personalmappe: Optional[Union[dict[Union[str, PersonalmappeId], Union[dict, "Personalmappe"]], list[Union[dict, "Personalmappe"]]]] = empty_dict()
    dispensasjonAutomatiskFredaKulturminne: Optional[Union[dict[Union[str, DispensasjonAutomatiskFredaKulturminneId], Union[dict, "DispensasjonAutomatiskFredaKulturminne"]], list[Union[dict, "DispensasjonAutomatiskFredaKulturminne"]]]] = empty_dict()
    tilskuddFartoy: Optional[Union[dict[Union[str, TilskuddFartoyId], Union[dict, "TilskuddFartoy"]], list[Union[dict, "TilskuddFartoy"]]]] = empty_dict()
    tilskuddFredaBygningPrivatEie: Optional[Union[dict[Union[str, TilskuddFredaBygningPrivatEieId], Union[dict, "TilskuddFredaBygningPrivatEie"]], list[Union[dict, "TilskuddFredaBygningPrivatEie"]]]] = empty_dict()
    soeknadDrosjeloeyve: Optional[Union[dict[Union[str, SoeknadDrosjeloeyveId], Union[dict, "SoeknadDrosjeloeyve"]], list[Union[dict, "SoeknadDrosjeloeyve"]]]] = empty_dict()
    dokumentstatuskodar: Optional[Union[dict[Union[str, DokumentStatusId], Union[dict, "DokumentStatus"]], list[Union[dict, "DokumentStatus"]]]] = empty_dict()
    dokumenttypar: Optional[Union[dict[Union[str, DokumentTypeId], Union[dict, "DokumentType"]], list[Union[dict, "DokumentType"]]]] = empty_dict()
    formatar: Optional[Union[dict[Union[str, FormatId], Union[dict, "Format"]], list[Union[dict, "Format"]]]] = empty_dict()
    journalposttypar: Optional[Union[dict[Union[str, JournalpostTypeId], Union[dict, "JournalpostType"]], list[Union[dict, "JournalpostType"]]]] = empty_dict()
    journalstatuskodar: Optional[Union[dict[Union[str, JournalStatusId], Union[dict, "JournalStatus"]], list[Union[dict, "JournalStatus"]]]] = empty_dict()
    klassifikasjonstypar: Optional[Union[dict[Union[str, KlassifikasjonstypeId], Union[dict, "Klassifikasjonstype"]], list[Union[dict, "Klassifikasjonstype"]]]] = empty_dict()
    korrespondanseparttypar: Optional[Union[dict[Union[str, KorrespondansepartTypeId], Union[dict, "KorrespondansepartType"]], list[Union[dict, "KorrespondansepartType"]]]] = empty_dict()
    merknadstypar: Optional[Union[dict[Union[str, MerknadstypeId], Union[dict, "Merknadstype"]], list[Union[dict, "Merknadstype"]]]] = empty_dict()
    partRollar: Optional[Union[dict[Union[str, PartRolleId], Union[dict, "PartRolle"]], list[Union[dict, "PartRolle"]]]] = empty_dict()
    rollar: Optional[Union[dict[Union[str, RolleId], Union[dict, "Rolle"]], list[Union[dict, "Rolle"]]]] = empty_dict()
    saksmappetypar: Optional[Union[dict[Union[str, SaksmappetypeId], Union[dict, "Saksmappetype"]], list[Union[dict, "Saksmappetype"]]]] = empty_dict()
    sakstatuskodar: Optional[Union[dict[Union[str, SaksstatusId], Union[dict, "Saksstatus"]], list[Union[dict, "Saksstatus"]]]] = empty_dict()
    skjermingsheimlar: Optional[Union[dict[Union[str, SkjermingshjemmelId], Union[dict, "Skjermingshjemmel"]], list[Union[dict, "Skjermingshjemmel"]]]] = empty_dict()
    tilgangsgrupper: Optional[Union[dict[Union[str, TilgangsgruppeId], Union[dict, "Tilgangsgruppe"]], list[Union[dict, "Tilgangsgruppe"]]]] = empty_dict()
    tilgangsrestriksjonar: Optional[Union[dict[Union[str, TilgangsrestriksjonId], Union[dict, "Tilgangsrestriksjon"]], list[Union[dict, "Tilgangsrestriksjon"]]]] = empty_dict()
    tilknyttetRegistreringSomKodar: Optional[Union[dict[Union[str, TilknyttetRegistreringSomId], Union[dict, "TilknyttetRegistreringSom"]], list[Union[dict, "TilknyttetRegistreringSom"]]]] = empty_dict()
    variantformatar: Optional[Union[dict[Union[str, VariantformatId], Union[dict, "Variantformat"]], list[Union[dict, "Variantformat"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="arkivdelar", slot_type=Arkivdel, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="arkivressursar", slot_type=Arkivressurs, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="autorisasjonar", slot_type=Autorisasjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="administrativeEiningar", slot_type=AdministrativEnhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dokumentfiler", slot_type=Dokumentfil, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dokumentbeskrivelsar", slot_type=Dokumentbeskrivelse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="journalpostar", slot_type=Journalpost, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="klassifikasjonssystem", slot_type=Klassifikasjonssystem, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tilgangar", slot_type=Tilgang, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sakar", slot_type=Sak, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="personalmappe", slot_type=Personalmappe, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dispensasjonAutomatiskFredaKulturminne", slot_type=DispensasjonAutomatiskFredaKulturminne, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tilskuddFartoy", slot_type=TilskuddFartoy, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tilskuddFredaBygningPrivatEie", slot_type=TilskuddFredaBygningPrivatEie, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="soeknadDrosjeloeyve", slot_type=SoeknadDrosjeloeyve, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dokumentstatuskodar", slot_type=DokumentStatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dokumenttypar", slot_type=DokumentType, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="formatar", slot_type=Format, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="journalposttypar", slot_type=JournalpostType, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="journalstatuskodar", slot_type=JournalStatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="klassifikasjonstypar", slot_type=Klassifikasjonstype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="korrespondanseparttypar", slot_type=KorrespondansepartType, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="merknadstypar", slot_type=Merknadstype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="partRollar", slot_type=PartRolle, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rollar", slot_type=Rolle, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="saksmappetypar", slot_type=Saksmappetype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sakstatuskodar", slot_type=Saksstatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="skjermingsheimlar", slot_type=Skjermingshjemmel, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tilgangsgrupper", slot_type=Tilgangsgruppe, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tilgangsrestriksjonar", slot_type=Tilgangsrestriksjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tilknyttetRegistreringSomKodar", slot_type=TilknyttetRegistreringSom, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="variantformatar", slot_type=Variantformat, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Mappe(YAMLRoot):
    """
    Abstrakt basisklasse for alle mappetypar. Grupperer dokument som høyrer saman.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Mappe"]
    class_class_curie: ClassVar[str] = "ark:Mappe"
    class_name: ClassVar[str] = "Mappe"
    class_model_uri: ClassVar[URIRef] = ARK.Mappe

    id: Union[str, MappeId] = None
    opprettetAv: Union[str, ArkivressursId] = None
    avsluttetDato: Optional[Union[str, XSDDateTime]] = None
    beskrivelse: Optional[str] = None
    klasse: Optional[Union[Union[dict, "Klasse"], list[Union[dict, "Klasse"]]]] = empty_list()
    mappeId: Optional[Union[dict, "Identifikator"]] = None
    merknad: Optional[Union[Union[dict, "Merknad"], list[Union[dict, "Merknad"]]]] = empty_list()
    noekkelord: Optional[Union[str, list[str]]] = empty_list()
    offentligTittel: Optional[str] = None
    opprettetDato: Optional[Union[str, XSDDateTime]] = None
    part: Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]] = empty_list()
    skjerming: Optional[Union[dict, "Skjerming"]] = None
    tittel: Optional[str] = None
    arkivdel: Optional[Union[str, ArkivdelId]] = None
    avsluttetAv: Optional[Union[str, ArkivressursId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MappeId):
            self.id = MappeId(self.id)

        if self._is_empty(self.opprettetAv):
            self.MissingRequiredField("opprettetAv")
        if not isinstance(self.opprettetAv, ArkivressursId):
            self.opprettetAv = ArkivressursId(self.opprettetAv)

        if self.avsluttetDato is not None and not isinstance(self.avsluttetDato, XSDDateTime):
            self.avsluttetDato = XSDDateTime(self.avsluttetDato)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        self._normalize_inlined_as_list(slot_name="klasse", slot_type=Klasse, key_name="klasseId", keyed=False)

        if self.mappeId is not None and not isinstance(self.mappeId, Identifikator):
            self.mappeId = Identifikator(**as_dict(self.mappeId))

        self._normalize_inlined_as_list(slot_name="merknad", slot_type=Merknad, key_name="merknadsdato", keyed=False)

        if not isinstance(self.noekkelord, list):
            self.noekkelord = [self.noekkelord] if self.noekkelord is not None else []
        self.noekkelord = [v if isinstance(v, str) else str(v) for v in self.noekkelord]

        if self.offentligTittel is not None and not isinstance(self.offentligTittel, str):
            self.offentligTittel = str(self.offentligTittel)

        if self.opprettetDato is not None and not isinstance(self.opprettetDato, XSDDateTime):
            self.opprettetDato = XSDDateTime(self.opprettetDato)

        self._normalize_inlined_as_list(slot_name="part", slot_type=Part, key_name="partNavn", keyed=False)

        if self.skjerming is not None and not isinstance(self.skjerming, Skjerming):
            self.skjerming = Skjerming(**as_dict(self.skjerming))

        if self.tittel is not None and not isinstance(self.tittel, str):
            self.tittel = str(self.tittel)

        if self.arkivdel is not None and not isinstance(self.arkivdel, ArkivdelId):
            self.arkivdel = ArkivdelId(self.arkivdel)

        if self.avsluttetAv is not None and not isinstance(self.avsluttetAv, ArkivressursId):
            self.avsluttetAv = ArkivressursId(self.avsluttetAv)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Saksmappe(Mappe):
    """
    Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Saksmappe"]
    class_class_curie: ClassVar[str] = "ark:Saksmappe"
    class_name: ClassVar[str] = "Saksmappe"
    class_model_uri: ClassVar[URIRef] = ARK.Saksmappe

    id: Union[str, SaksmappeId] = None
    opprettetAv: Union[str, ArkivressursId] = None
    saksstatus: Union[str, SaksstatusId] = None
    administrativEnhet: Union[str, AdministrativEnhetId] = None
    saksansvarlig: Union[str, ArkivressursId] = None
    journalpost: Optional[Union[Union[str, JournalpostId], list[Union[str, JournalpostId]]]] = empty_list()
    saksaar: Optional[str] = None
    saksdato: Optional[Union[str, XSDDateTime]] = None
    sakssekvensnummer: Optional[str] = None
    utlaantDato: Optional[Union[str, XSDDateTime]] = None
    saksmappetype: Optional[Union[str, SaksmappetypeId]] = None
    tilgangsgruppe: Optional[Union[str, TilgangsgruppeId]] = None
    journalenhet: Optional[Union[str, AdministrativEnhetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.saksstatus):
            self.MissingRequiredField("saksstatus")
        if not isinstance(self.saksstatus, SaksstatusId):
            self.saksstatus = SaksstatusId(self.saksstatus)

        if self._is_empty(self.administrativEnhet):
            self.MissingRequiredField("administrativEnhet")
        if not isinstance(self.administrativEnhet, AdministrativEnhetId):
            self.administrativEnhet = AdministrativEnhetId(self.administrativEnhet)

        if self._is_empty(self.saksansvarlig):
            self.MissingRequiredField("saksansvarlig")
        if not isinstance(self.saksansvarlig, ArkivressursId):
            self.saksansvarlig = ArkivressursId(self.saksansvarlig)

        if not isinstance(self.journalpost, list):
            self.journalpost = [self.journalpost] if self.journalpost is not None else []
        self.journalpost = [v if isinstance(v, JournalpostId) else JournalpostId(v) for v in self.journalpost]

        if self.saksaar is not None and not isinstance(self.saksaar, str):
            self.saksaar = str(self.saksaar)

        if self.saksdato is not None and not isinstance(self.saksdato, XSDDateTime):
            self.saksdato = XSDDateTime(self.saksdato)

        if self.sakssekvensnummer is not None and not isinstance(self.sakssekvensnummer, str):
            self.sakssekvensnummer = str(self.sakssekvensnummer)

        if self.utlaantDato is not None and not isinstance(self.utlaantDato, XSDDateTime):
            self.utlaantDato = XSDDateTime(self.utlaantDato)

        if self.saksmappetype is not None and not isinstance(self.saksmappetype, SaksmappetypeId):
            self.saksmappetype = SaksmappetypeId(self.saksmappetype)

        if self.tilgangsgruppe is not None and not isinstance(self.tilgangsgruppe, TilgangsgruppeId):
            self.tilgangsgruppe = TilgangsgruppeId(self.tilgangsgruppe)

        if self.journalenhet is not None and not isinstance(self.journalenhet, AdministrativEnhetId):
            self.journalenhet = AdministrativEnhetId(self.journalenhet)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Registrering(YAMLRoot):
    """
    Abstrakt basisklasse — arkivets primære byggeklossar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Registrering"]
    class_class_curie: ClassVar[str] = "ark:Registrering"
    class_name: ClassVar[str] = "Registrering"
    class_model_uri: ClassVar[URIRef] = ARK.Registrering

    id: Union[str, RegistreringId] = None
    tittel: str = None
    arkivertAv: Union[str, ArkivressursId] = None
    opprettetAv: Union[str, ArkivressursId] = None
    arkivertDato: Optional[Union[str, XSDDateTime]] = None
    beskrivelse: Optional[str] = None
    dokumentbeskrivelse: Optional[Union[Union[str, DokumentbeskrivelseId], list[Union[str, DokumentbeskrivelseId]]]] = empty_list()
    forfatter: Optional[Union[str, list[str]]] = empty_list()
    klasse: Optional[Union[dict, "Klasse"]] = None
    korrespondansepart: Optional[Union[Union[dict, "Korrespondansepart"], list[Union[dict, "Korrespondansepart"]]]] = empty_list()
    merknad: Optional[Union[Union[dict, "Merknad"], list[Union[dict, "Merknad"]]]] = empty_list()
    nokkelord: Optional[Union[str, list[str]]] = empty_list()
    offentligTittel: Optional[str] = None
    opprettetDato: Optional[Union[str, XSDDateTime]] = None
    part: Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]] = empty_list()
    referanseArkivDel: Optional[Union[str, list[str]]] = empty_list()
    registreringsId: Optional[str] = None
    skjerming: Optional[Union[dict, "Skjerming"]] = None
    tilgangsgruppe: Optional[Union[str, TilgangsgruppeId]] = None
    administrativEnhet: Optional[Union[str, AdministrativEnhetId]] = None
    arkivdel: Optional[Union[str, ArkivdelId]] = None
    saksbehandler: Optional[Union[str, ArkivressursId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegistreringId):
            self.id = RegistreringId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, str):
            self.tittel = str(self.tittel)

        if self._is_empty(self.arkivertAv):
            self.MissingRequiredField("arkivertAv")
        if not isinstance(self.arkivertAv, ArkivressursId):
            self.arkivertAv = ArkivressursId(self.arkivertAv)

        if self._is_empty(self.opprettetAv):
            self.MissingRequiredField("opprettetAv")
        if not isinstance(self.opprettetAv, ArkivressursId):
            self.opprettetAv = ArkivressursId(self.opprettetAv)

        if self.arkivertDato is not None and not isinstance(self.arkivertDato, XSDDateTime):
            self.arkivertDato = XSDDateTime(self.arkivertDato)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if not isinstance(self.dokumentbeskrivelse, list):
            self.dokumentbeskrivelse = [self.dokumentbeskrivelse] if self.dokumentbeskrivelse is not None else []
        self.dokumentbeskrivelse = [v if isinstance(v, DokumentbeskrivelseId) else DokumentbeskrivelseId(v) for v in self.dokumentbeskrivelse]

        if not isinstance(self.forfatter, list):
            self.forfatter = [self.forfatter] if self.forfatter is not None else []
        self.forfatter = [v if isinstance(v, str) else str(v) for v in self.forfatter]

        if self.klasse is not None and not isinstance(self.klasse, Klasse):
            self.klasse = Klasse(**as_dict(self.klasse))

        if not isinstance(self.korrespondansepart, list):
            self.korrespondansepart = [self.korrespondansepart] if self.korrespondansepart is not None else []
        self.korrespondansepart = [v if isinstance(v, Korrespondansepart) else Korrespondansepart(**as_dict(v)) for v in self.korrespondansepart]

        self._normalize_inlined_as_list(slot_name="merknad", slot_type=Merknad, key_name="merknadsdato", keyed=False)

        if not isinstance(self.nokkelord, list):
            self.nokkelord = [self.nokkelord] if self.nokkelord is not None else []
        self.nokkelord = [v if isinstance(v, str) else str(v) for v in self.nokkelord]

        if self.offentligTittel is not None and not isinstance(self.offentligTittel, str):
            self.offentligTittel = str(self.offentligTittel)

        if self.opprettetDato is not None and not isinstance(self.opprettetDato, XSDDateTime):
            self.opprettetDato = XSDDateTime(self.opprettetDato)

        self._normalize_inlined_as_list(slot_name="part", slot_type=Part, key_name="partNavn", keyed=False)

        if not isinstance(self.referanseArkivDel, list):
            self.referanseArkivDel = [self.referanseArkivDel] if self.referanseArkivDel is not None else []
        self.referanseArkivDel = [v if isinstance(v, str) else str(v) for v in self.referanseArkivDel]

        if self.registreringsId is not None and not isinstance(self.registreringsId, str):
            self.registreringsId = str(self.registreringsId)

        if self.skjerming is not None and not isinstance(self.skjerming, Skjerming):
            self.skjerming = Skjerming(**as_dict(self.skjerming))

        if self.tilgangsgruppe is not None and not isinstance(self.tilgangsgruppe, TilgangsgruppeId):
            self.tilgangsgruppe = TilgangsgruppeId(self.tilgangsgruppe)

        if self.administrativEnhet is not None and not isinstance(self.administrativEnhet, AdministrativEnhetId):
            self.administrativEnhet = AdministrativEnhetId(self.administrativEnhet)

        if self.arkivdel is not None and not isinstance(self.arkivdel, ArkivdelId):
            self.arkivdel = ArkivdelId(self.arkivdel)

        if self.saksbehandler is not None and not isinstance(self.saksbehandler, ArkivressursId):
            self.saksbehandler = ArkivressursId(self.saksbehandler)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdministrativEnhet(YAMLRoot):
    """
    Administrativ eining med ansvar for saksbehandling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["AdministrativEnhet"]
    class_class_curie: ClassVar[str] = "ark:AdministrativEnhet"
    class_name: ClassVar[str] = "AdministrativEnhet"
    class_model_uri: ClassVar[URIRef] = ARK.AdministrativEnhet

    id: Union[str, AdministrativEnhetId] = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    organisasjonselement: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdministrativEnhetId):
            self.id = AdministrativEnhetId(self.id)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.gyldighetsperiode is not None and not isinstance(self.gyldighetsperiode, Periode):
            self.gyldighetsperiode = Periode(**as_dict(self.gyldighetsperiode))

        if self.organisasjonselement is not None and not isinstance(self.organisasjonselement, URIorCURIE):
            self.organisasjonselement = URIorCURIE(self.organisasjonselement)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Arkivdel(YAMLRoot):
    """
    Ein vilkårleg definert del av eit arkiv.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Arkivdel"]
    class_class_curie: ClassVar[str] = "ark:Arkivdel"
    class_name: ClassVar[str] = "Arkivdel"
    class_model_uri: ClassVar[URIRef] = ARK.Arkivdel

    id: Union[str, ArkivdelId] = None
    tittel: str = None
    klassifikasjonssystem: Optional[Union[Union[str, KlassifikasjonssystemId], list[Union[str, KlassifikasjonssystemId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArkivdelId):
            self.id = ArkivdelId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, str):
            self.tittel = str(self.tittel)

        if not isinstance(self.klassifikasjonssystem, list):
            self.klassifikasjonssystem = [self.klassifikasjonssystem] if self.klassifikasjonssystem is not None else []
        self.klassifikasjonssystem = [v if isinstance(v, KlassifikasjonssystemId) else KlassifikasjonssystemId(v) for v in self.klassifikasjonssystem]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Arkivressurs(YAMLRoot):
    """
    Ansatt med rolle og rettar innanfor arkiv.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Arkivressurs"]
    class_class_curie: ClassVar[str] = "ark:Arkivressurs"
    class_name: ClassVar[str] = "Arkivressurs"
    class_model_uri: ClassVar[URIRef] = ARK.Arkivressurs

    id: Union[str, ArkivressursId] = None
    personalressurs: Union[str, URIorCURIE] = None
    kildesystemId: Optional[Union[dict, "Identifikator"]] = None
    autorisasjon: Optional[Union[Union[str, AutorisasjonId], list[Union[str, AutorisasjonId]]]] = empty_list()
    tilgang: Optional[Union[Union[str, TilgangId], list[Union[str, TilgangId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArkivressursId):
            self.id = ArkivressursId(self.id)

        if self._is_empty(self.personalressurs):
            self.MissingRequiredField("personalressurs")
        if not isinstance(self.personalressurs, URIorCURIE):
            self.personalressurs = URIorCURIE(self.personalressurs)

        if self.kildesystemId is not None and not isinstance(self.kildesystemId, Identifikator):
            self.kildesystemId = Identifikator(**as_dict(self.kildesystemId))

        if not isinstance(self.autorisasjon, list):
            self.autorisasjon = [self.autorisasjon] if self.autorisasjon is not None else []
        self.autorisasjon = [v if isinstance(v, AutorisasjonId) else AutorisasjonId(v) for v in self.autorisasjon]

        if not isinstance(self.tilgang, list):
            self.tilgang = [self.tilgang] if self.tilgang is not None else []
        self.tilgang = [v if isinstance(v, TilgangId) else TilgangId(v) for v in self.tilgang]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Autorisasjon(YAMLRoot):
    """
    Siling av kva ein innlogga brukar får lov til å gjere i løysinga.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Autorisasjon"]
    class_class_curie: ClassVar[str] = "ark:Autorisasjon"
    class_name: ClassVar[str] = "Autorisasjon"
    class_model_uri: ClassVar[URIRef] = ARK.Autorisasjon

    id: Union[str, AutorisasjonId] = None
    tilgangsrestriksjon: Union[Union[str, TilgangsrestriksjonId], list[Union[str, TilgangsrestriksjonId]]] = None
    administrativenhet: Optional[Union[Union[str, AdministrativEnhetId], list[Union[str, AdministrativEnhetId]]]] = empty_list()
    arkivressurs: Optional[Union[Union[str, ArkivressursId], list[Union[str, ArkivressursId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AutorisasjonId):
            self.id = AutorisasjonId(self.id)

        if self._is_empty(self.tilgangsrestriksjon):
            self.MissingRequiredField("tilgangsrestriksjon")
        if not isinstance(self.tilgangsrestriksjon, list):
            self.tilgangsrestriksjon = [self.tilgangsrestriksjon] if self.tilgangsrestriksjon is not None else []
        self.tilgangsrestriksjon = [v if isinstance(v, TilgangsrestriksjonId) else TilgangsrestriksjonId(v) for v in self.tilgangsrestriksjon]

        if not isinstance(self.administrativenhet, list):
            self.administrativenhet = [self.administrativenhet] if self.administrativenhet is not None else []
        self.administrativenhet = [v if isinstance(v, AdministrativEnhetId) else AdministrativEnhetId(v) for v in self.administrativenhet]

        if not isinstance(self.arkivressurs, list):
            self.arkivressurs = [self.arkivressurs] if self.arkivressurs is not None else []
        self.arkivressurs = [v if isinstance(v, ArkivressursId) else ArkivressursId(v) for v in self.arkivressurs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dokumentfil(YAMLRoot):
    """
    Sjølve dokumentfila med data og metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Dokumentfil"]
    class_class_curie: ClassVar[str] = "ark:Dokumentfil"
    class_name: ClassVar[str] = "Dokumentfil"
    class_model_uri: ClassVar[URIRef] = ARK.Dokumentfil

    id: Union[str, DokumentfilId] = None
    data: str = None
    format: str = None
    filnavn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DokumentfilId):
            self.id = DokumentfilId(self.id)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, str):
            self.data = str(self.data)

        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self.filnavn is not None and not isinstance(self.filnavn, str):
            self.filnavn = str(self.filnavn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Journalpost(Registrering):
    """
    Ein journalpost (inn- eller utgåande dokument, notat o.l.) i ei saksmappe.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Journalpost"]
    class_class_curie: ClassVar[str] = "ark:Journalpost"
    class_name: ClassVar[str] = "Journalpost"
    class_model_uri: ClassVar[URIRef] = ARK.Journalpost

    id: Union[str, JournalpostId] = None
    tittel: str = None
    arkivertAv: Union[str, ArkivressursId] = None
    opprettetAv: Union[str, ArkivressursId] = None
    journalposttype: Union[str, JournalpostTypeId] = None
    journalstatus: Union[str, JournalStatusId] = None
    antallVedlegg: Optional[int] = None
    avskrivning: Optional[Union[dict, "Avskrivning"]] = None
    dokumentetsDato: Optional[Union[str, XSDDateTime]] = None
    forfallsDato: Optional[Union[str, XSDDateTime]] = None
    journalAr: Optional[str] = None
    journalDato: Optional[Union[str, XSDDateTime]] = None
    journalPostnummer: Optional[int] = None
    journalSekvensnummer: Optional[int] = None
    mottattDato: Optional[Union[str, XSDDateTime]] = None
    offentlighetsvurdertDato: Optional[Union[str, XSDDateTime]] = None
    sendtDato: Optional[Union[str, XSDDateTime]] = None
    journalenhet: Optional[Union[str, AdministrativEnhetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JournalpostId):
            self.id = JournalpostId(self.id)

        if self._is_empty(self.journalposttype):
            self.MissingRequiredField("journalposttype")
        if not isinstance(self.journalposttype, JournalpostTypeId):
            self.journalposttype = JournalpostTypeId(self.journalposttype)

        if self._is_empty(self.journalstatus):
            self.MissingRequiredField("journalstatus")
        if not isinstance(self.journalstatus, JournalStatusId):
            self.journalstatus = JournalStatusId(self.journalstatus)

        if self.antallVedlegg is not None and not isinstance(self.antallVedlegg, int):
            self.antallVedlegg = int(self.antallVedlegg)

        if self.avskrivning is not None and not isinstance(self.avskrivning, Avskrivning):
            self.avskrivning = Avskrivning(**as_dict(self.avskrivning))

        if self.dokumentetsDato is not None and not isinstance(self.dokumentetsDato, XSDDateTime):
            self.dokumentetsDato = XSDDateTime(self.dokumentetsDato)

        if self.forfallsDato is not None and not isinstance(self.forfallsDato, XSDDateTime):
            self.forfallsDato = XSDDateTime(self.forfallsDato)

        if self.journalAr is not None and not isinstance(self.journalAr, str):
            self.journalAr = str(self.journalAr)

        if self.journalDato is not None and not isinstance(self.journalDato, XSDDateTime):
            self.journalDato = XSDDateTime(self.journalDato)

        if self.journalPostnummer is not None and not isinstance(self.journalPostnummer, int):
            self.journalPostnummer = int(self.journalPostnummer)

        if self.journalSekvensnummer is not None and not isinstance(self.journalSekvensnummer, int):
            self.journalSekvensnummer = int(self.journalSekvensnummer)

        if self.mottattDato is not None and not isinstance(self.mottattDato, XSDDateTime):
            self.mottattDato = XSDDateTime(self.mottattDato)

        if self.offentlighetsvurdertDato is not None and not isinstance(self.offentlighetsvurdertDato, XSDDateTime):
            self.offentlighetsvurdertDato = XSDDateTime(self.offentlighetsvurdertDato)

        if self.sendtDato is not None and not isinstance(self.sendtDato, XSDDateTime):
            self.sendtDato = XSDDateTime(self.sendtDato)

        if self.journalenhet is not None and not isinstance(self.journalenhet, AdministrativEnhetId):
            self.journalenhet = AdministrativEnhetId(self.journalenhet)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Klassifikasjonssystem(YAMLRoot):
    """
    Overordna struktur for mappene i ein eller fleire arkivdelar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Klassifikasjonssystem"]
    class_class_curie: ClassVar[str] = "ark:Klassifikasjonssystem"
    class_name: ClassVar[str] = "Klassifikasjonssystem"
    class_model_uri: ClassVar[URIRef] = ARK.Klassifikasjonssystem

    id: Union[str, KlassifikasjonssystemId] = None
    klasse: Union[Union[dict, "Klasse"], list[Union[dict, "Klasse"]]] = None
    opprettetAv: str = None
    opprettetDato: Union[str, XSDDateTime] = None
    tittel: str = None
    arkivdel: Union[Union[str, ArkivdelId], list[Union[str, ArkivdelId]]] = None
    avsluttetAv: Optional[str] = None
    avsluttetDato: Optional[Union[str, XSDDateTime]] = None
    beskrivelse: Optional[str] = None
    klassifikasjonstype: Optional[Union[str, KlassifikasjonstypeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KlassifikasjonssystemId):
            self.id = KlassifikasjonssystemId(self.id)

        if self._is_empty(self.klasse):
            self.MissingRequiredField("klasse")
        self._normalize_inlined_as_list(slot_name="klasse", slot_type=Klasse, key_name="klasseId", keyed=False)

        if self._is_empty(self.opprettetAv):
            self.MissingRequiredField("opprettetAv")
        if not isinstance(self.opprettetAv, str):
            self.opprettetAv = str(self.opprettetAv)

        if self._is_empty(self.opprettetDato):
            self.MissingRequiredField("opprettetDato")
        if not isinstance(self.opprettetDato, XSDDateTime):
            self.opprettetDato = XSDDateTime(self.opprettetDato)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, str):
            self.tittel = str(self.tittel)

        if self._is_empty(self.arkivdel):
            self.MissingRequiredField("arkivdel")
        if not isinstance(self.arkivdel, list):
            self.arkivdel = [self.arkivdel] if self.arkivdel is not None else []
        self.arkivdel = [v if isinstance(v, ArkivdelId) else ArkivdelId(v) for v in self.arkivdel]

        if self.avsluttetAv is not None and not isinstance(self.avsluttetAv, str):
            self.avsluttetAv = str(self.avsluttetAv)

        if self.avsluttetDato is not None and not isinstance(self.avsluttetDato, XSDDateTime):
            self.avsluttetDato = XSDDateTime(self.avsluttetDato)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if self.klassifikasjonstype is not None and not isinstance(self.klassifikasjonstype, KlassifikasjonstypeId):
            self.klassifikasjonstype = KlassifikasjonstypeId(self.klassifikasjonstype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tilgang(YAMLRoot):
    """
    Styring av kven som har tilgang til kva opplysningar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Tilgang"]
    class_class_curie: ClassVar[str] = "ark:Tilgang"
    class_name: ClassVar[str] = "Tilgang"
    class_model_uri: ClassVar[URIRef] = ARK.Tilgang

    id: Union[str, TilgangId] = None
    tittel: str = None
    rolle: Union[str, RolleId] = None
    administrativEnhet: Optional[Union[str, AdministrativEnhetId]] = None
    arkivdel: Optional[Union[str, ArkivdelId]] = None
    arkivressurs: Optional[Union[Union[str, ArkivressursId], list[Union[str, ArkivressursId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TilgangId):
            self.id = TilgangId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, str):
            self.tittel = str(self.tittel)

        if self._is_empty(self.rolle):
            self.MissingRequiredField("rolle")
        if not isinstance(self.rolle, RolleId):
            self.rolle = RolleId(self.rolle)

        if self.administrativEnhet is not None and not isinstance(self.administrativEnhet, AdministrativEnhetId):
            self.administrativEnhet = AdministrativEnhetId(self.administrativEnhet)

        if self.arkivdel is not None and not isinstance(self.arkivdel, ArkivdelId):
            self.arkivdel = ArkivdelId(self.arkivdel)

        if not isinstance(self.arkivressurs, list):
            self.arkivressurs = [self.arkivressurs] if self.arkivressurs is not None else []
        self.arkivressurs = [v if isinstance(v, ArkivressursId) else ArkivressursId(v) for v in self.arkivressurs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sak(Saksmappe):
    """
    Generisk saksmappe (konkret Sak i Noark).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Sak"]
    class_class_curie: ClassVar[str] = "ark:Sak"
    class_name: ClassVar[str] = "Sak"
    class_model_uri: ClassVar[URIRef] = ARK.Sak

    id: Union[str, SakId] = None
    opprettetAv: Union[str, ArkivressursId] = None
    saksstatus: Union[str, SaksstatusId] = None
    administrativEnhet: Union[str, AdministrativEnhetId] = None
    saksansvarlig: Union[str, ArkivressursId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SakId):
            self.id = SakId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Personalmappe(Saksmappe):
    """
    Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Personalmappe"]
    class_class_curie: ClassVar[str] = "ark:Personalmappe"
    class_name: ClassVar[str] = "Personalmappe"
    class_model_uri: ClassVar[URIRef] = ARK.Personalmappe

    id: Union[str, PersonalmappeId] = None
    opprettetAv: Union[str, ArkivressursId] = None
    saksstatus: Union[str, SaksstatusId] = None
    administrativEnhet: Union[str, AdministrativEnhetId] = None
    saksansvarlig: Union[str, ArkivressursId] = None
    navn: Union[dict, "Personnavn"] = None
    person: Union[str, URIorCURIE] = None
    leder: Union[str, URIorCURIE] = None
    arbeidssted: Union[str, URIorCURIE] = None
    personalressurs: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonalmappeId):
            self.id = PersonalmappeId(self.id)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, Personnavn):
            self.navn = Personnavn(**as_dict(self.navn))

        if self._is_empty(self.person):
            self.MissingRequiredField("person")
        if not isinstance(self.person, URIorCURIE):
            self.person = URIorCURIE(self.person)

        if self._is_empty(self.leder):
            self.MissingRequiredField("leder")
        if not isinstance(self.leder, URIorCURIE):
            self.leder = URIorCURIE(self.leder)

        if self._is_empty(self.arbeidssted):
            self.MissingRequiredField("arbeidssted")
        if not isinstance(self.arbeidssted, URIorCURIE):
            self.arbeidssted = URIorCURIE(self.arbeidssted)

        if self._is_empty(self.personalressurs):
            self.MissingRequiredField("personalressurs")
        if not isinstance(self.personalressurs, URIorCURIE):
            self.personalressurs = URIorCURIE(self.personalressurs)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DispensasjonAutomatiskFredaKulturminne(Saksmappe):
    """
    Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["DispensasjonAutomatiskFredaKulturminne"]
    class_class_curie: ClassVar[str] = "ark:DispensasjonAutomatiskFredaKulturminne"
    class_name: ClassVar[str] = "DispensasjonAutomatiskFredaKulturminne"
    class_model_uri: ClassVar[URIRef] = ARK.DispensasjonAutomatiskFredaKulturminne

    id: Union[str, DispensasjonAutomatiskFredaKulturminneId] = None
    opprettetAv: Union[str, ArkivressursId] = None
    saksstatus: Union[str, SaksstatusId] = None
    administrativEnhet: Union[str, AdministrativEnhetId] = None
    saksansvarlig: Union[str, ArkivressursId] = None
    kulturminneId: str = None
    matrikkelnummer: Union[dict, "Matrikkelnummer"] = None
    soeknadsnummer: Union[dict, "Identifikator"] = None
    tiltak: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DispensasjonAutomatiskFredaKulturminneId):
            self.id = DispensasjonAutomatiskFredaKulturminneId(self.id)

        if self._is_empty(self.kulturminneId):
            self.MissingRequiredField("kulturminneId")
        if not isinstance(self.kulturminneId, str):
            self.kulturminneId = str(self.kulturminneId)

        if self._is_empty(self.matrikkelnummer):
            self.MissingRequiredField("matrikkelnummer")
        if not isinstance(self.matrikkelnummer, Matrikkelnummer):
            self.matrikkelnummer = Matrikkelnummer(**as_dict(self.matrikkelnummer))

        if self._is_empty(self.soeknadsnummer):
            self.MissingRequiredField("soeknadsnummer")
        if not isinstance(self.soeknadsnummer, Identifikator):
            self.soeknadsnummer = Identifikator(**as_dict(self.soeknadsnummer))

        if self.tiltak is not None and not isinstance(self.tiltak, str):
            self.tiltak = str(self.tiltak)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TilskuddFartoy(Saksmappe):
    """
    Sak om søknad om tilskudd til freda fartøy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["TilskuddFartoy"]
    class_class_curie: ClassVar[str] = "ark:TilskuddFartoy"
    class_name: ClassVar[str] = "TilskuddFartoy"
    class_model_uri: ClassVar[URIRef] = ARK.TilskuddFartoy

    id: Union[str, TilskuddFartoyId] = None
    opprettetAv: Union[str, ArkivressursId] = None
    saksstatus: Union[str, SaksstatusId] = None
    administrativEnhet: Union[str, AdministrativEnhetId] = None
    saksansvarlig: Union[str, ArkivressursId] = None
    fartoyNavn: str = None
    kallesignal: str = None
    kulturminneId: str = None
    soeknadsnummer: Union[dict, "Identifikator"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TilskuddFartoyId):
            self.id = TilskuddFartoyId(self.id)

        if self._is_empty(self.fartoyNavn):
            self.MissingRequiredField("fartoyNavn")
        if not isinstance(self.fartoyNavn, str):
            self.fartoyNavn = str(self.fartoyNavn)

        if self._is_empty(self.kallesignal):
            self.MissingRequiredField("kallesignal")
        if not isinstance(self.kallesignal, str):
            self.kallesignal = str(self.kallesignal)

        if self._is_empty(self.kulturminneId):
            self.MissingRequiredField("kulturminneId")
        if not isinstance(self.kulturminneId, str):
            self.kulturminneId = str(self.kulturminneId)

        if self._is_empty(self.soeknadsnummer):
            self.MissingRequiredField("soeknadsnummer")
        if not isinstance(self.soeknadsnummer, Identifikator):
            self.soeknadsnummer = Identifikator(**as_dict(self.soeknadsnummer))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TilskuddFredaBygningPrivatEie(Saksmappe):
    """
    Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["TilskuddFredaBygningPrivatEie"]
    class_class_curie: ClassVar[str] = "ark:TilskuddFredaBygningPrivatEie"
    class_name: ClassVar[str] = "TilskuddFredaBygningPrivatEie"
    class_model_uri: ClassVar[URIRef] = ARK.TilskuddFredaBygningPrivatEie

    id: Union[str, TilskuddFredaBygningPrivatEieId] = None
    opprettetAv: Union[str, ArkivressursId] = None
    saksstatus: Union[str, SaksstatusId] = None
    administrativEnhet: Union[str, AdministrativEnhetId] = None
    saksansvarlig: Union[str, ArkivressursId] = None
    kulturminneId: str = None
    bygningsnavn: Optional[str] = None
    matrikkelnummer: Optional[Union[dict, "Matrikkelnummer"]] = None
    soeknadsnummer: Optional[Union[dict, "Identifikator"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TilskuddFredaBygningPrivatEieId):
            self.id = TilskuddFredaBygningPrivatEieId(self.id)

        if self._is_empty(self.kulturminneId):
            self.MissingRequiredField("kulturminneId")
        if not isinstance(self.kulturminneId, str):
            self.kulturminneId = str(self.kulturminneId)

        if self.bygningsnavn is not None and not isinstance(self.bygningsnavn, str):
            self.bygningsnavn = str(self.bygningsnavn)

        if self.matrikkelnummer is not None and not isinstance(self.matrikkelnummer, Matrikkelnummer):
            self.matrikkelnummer = Matrikkelnummer(**as_dict(self.matrikkelnummer))

        if self.soeknadsnummer is not None and not isinstance(self.soeknadsnummer, Identifikator):
            self.soeknadsnummer = Identifikator(**as_dict(self.soeknadsnummer))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SoeknadDrosjeloeyve(Saksmappe):
    """
    Sak om søknad om løyve til å køyre drosje.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["SoeknadDrosjeloeyve"]
    class_class_curie: ClassVar[str] = "ark:SoeknadDrosjeloeyve"
    class_name: ClassVar[str] = "SoeknadDrosjeloeyve"
    class_model_uri: ClassVar[URIRef] = ARK.SoeknadDrosjeloeyve

    id: Union[str, SoeknadDrosjeloeyveId] = None
    opprettetAv: Union[str, ArkivressursId] = None
    saksstatus: Union[str, SaksstatusId] = None
    administrativEnhet: Union[str, AdministrativEnhetId] = None
    saksansvarlig: Union[str, ArkivressursId] = None
    organisasjonsnavn: str = None
    organisasjonsnummer: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoeknadDrosjeloeyveId):
            self.id = SoeknadDrosjeloeyveId(self.id)

        if self._is_empty(self.organisasjonsnavn):
            self.MissingRequiredField("organisasjonsnavn")
        if not isinstance(self.organisasjonsnavn, str):
            self.organisasjonsnavn = str(self.organisasjonsnavn)

        if self._is_empty(self.organisasjonsnummer):
            self.MissingRequiredField("organisasjonsnummer")
        if not isinstance(self.organisasjonsnummer, str):
            self.organisasjonsnummer = str(self.organisasjonsnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Avskrivning(YAMLRoot):
    """
    Avskriving av ein journalpost (markering som ferdigbehandla).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Avskrivning"]
    class_class_curie: ClassVar[str] = "ark:Avskrivning"
    class_name: ClassVar[str] = "Avskrivning"
    class_model_uri: ClassVar[URIRef] = ARK.Avskrivning

    avskrevetAv: str = None
    avskrivningsdato: Union[str, XSDDateTime] = None
    avskrivningsmate: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.avskrevetAv):
            self.MissingRequiredField("avskrevetAv")
        if not isinstance(self.avskrevetAv, str):
            self.avskrevetAv = str(self.avskrevetAv)

        if self._is_empty(self.avskrivningsdato):
            self.MissingRequiredField("avskrivningsdato")
        if not isinstance(self.avskrivningsdato, XSDDateTime):
            self.avskrivningsdato = XSDDateTime(self.avskrivningsdato)

        if self._is_empty(self.avskrivningsmate):
            self.MissingRequiredField("avskrivningsmate")
        if not isinstance(self.avskrivningsmate, str):
            self.avskrivningsmate = str(self.avskrivningsmate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dokumentbeskrivelse(YAMLRoot):
    """
    Skildring av eit dokument tilknytt ein journalpost.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Dokumentbeskrivelse"]
    class_class_curie: ClassVar[str] = "ark:Dokumentbeskrivelse"
    class_name: ClassVar[str] = "Dokumentbeskrivelse"
    class_model_uri: ClassVar[URIRef] = ARK.Dokumentbeskrivelse

    id: Union[str, DokumentbeskrivelseId] = None
    tittel: str = None
    dokumentstatus: Union[str, DokumentStatusId] = None
    dokumentType: Union[str, DokumentTypeId] = None
    tilknyttetRegistreringSom: Union[Union[str, TilknyttetRegistreringSomId], list[Union[str, TilknyttetRegistreringSomId]]] = None
    tilknyttetAv: Union[str, ArkivressursId] = None
    opprettetAv: Union[str, ArkivressursId] = None
    beskrivelse: Optional[str] = None
    dokumentnummer: Optional[int] = None
    dokumentobjekt: Optional[Union[Union[dict, "Dokumentobjekt"], list[Union[dict, "Dokumentobjekt"]]]] = empty_list()
    forfatter: Optional[Union[str, list[str]]] = empty_list()
    opprettetDato: Optional[Union[str, XSDDateTime]] = None
    part: Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]] = empty_list()
    referanseArkivdel: Optional[Union[str, list[str]]] = empty_list()
    skjerming: Optional[Union[dict, "Skjerming"]] = None
    tilknyttetDato: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DokumentbeskrivelseId):
            self.id = DokumentbeskrivelseId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, str):
            self.tittel = str(self.tittel)

        if self._is_empty(self.dokumentstatus):
            self.MissingRequiredField("dokumentstatus")
        if not isinstance(self.dokumentstatus, DokumentStatusId):
            self.dokumentstatus = DokumentStatusId(self.dokumentstatus)

        if self._is_empty(self.dokumentType):
            self.MissingRequiredField("dokumentType")
        if not isinstance(self.dokumentType, DokumentTypeId):
            self.dokumentType = DokumentTypeId(self.dokumentType)

        if self._is_empty(self.tilknyttetRegistreringSom):
            self.MissingRequiredField("tilknyttetRegistreringSom")
        if not isinstance(self.tilknyttetRegistreringSom, list):
            self.tilknyttetRegistreringSom = [self.tilknyttetRegistreringSom] if self.tilknyttetRegistreringSom is not None else []
        self.tilknyttetRegistreringSom = [v if isinstance(v, TilknyttetRegistreringSomId) else TilknyttetRegistreringSomId(v) for v in self.tilknyttetRegistreringSom]

        if self._is_empty(self.tilknyttetAv):
            self.MissingRequiredField("tilknyttetAv")
        if not isinstance(self.tilknyttetAv, ArkivressursId):
            self.tilknyttetAv = ArkivressursId(self.tilknyttetAv)

        if self._is_empty(self.opprettetAv):
            self.MissingRequiredField("opprettetAv")
        if not isinstance(self.opprettetAv, ArkivressursId):
            self.opprettetAv = ArkivressursId(self.opprettetAv)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if self.dokumentnummer is not None and not isinstance(self.dokumentnummer, int):
            self.dokumentnummer = int(self.dokumentnummer)

        if not isinstance(self.dokumentobjekt, list):
            self.dokumentobjekt = [self.dokumentobjekt] if self.dokumentobjekt is not None else []
        self.dokumentobjekt = [v if isinstance(v, Dokumentobjekt) else Dokumentobjekt(**as_dict(v)) for v in self.dokumentobjekt]

        if not isinstance(self.forfatter, list):
            self.forfatter = [self.forfatter] if self.forfatter is not None else []
        self.forfatter = [v if isinstance(v, str) else str(v) for v in self.forfatter]

        if self.opprettetDato is not None and not isinstance(self.opprettetDato, XSDDateTime):
            self.opprettetDato = XSDDateTime(self.opprettetDato)

        self._normalize_inlined_as_list(slot_name="part", slot_type=Part, key_name="partNavn", keyed=False)

        if not isinstance(self.referanseArkivdel, list):
            self.referanseArkivdel = [self.referanseArkivdel] if self.referanseArkivdel is not None else []
        self.referanseArkivdel = [v if isinstance(v, str) else str(v) for v in self.referanseArkivdel]

        if self.skjerming is not None and not isinstance(self.skjerming, Skjerming):
            self.skjerming = Skjerming(**as_dict(self.skjerming))

        if self.tilknyttetDato is not None and not isinstance(self.tilknyttetDato, XSDDateTime):
            self.tilknyttetDato = XSDDateTime(self.tilknyttetDato)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dokumentobjekt(YAMLRoot):
    """
    Referanse til éin og berre éin dokumentfil.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Dokumentobjekt"]
    class_class_curie: ClassVar[str] = "ark:Dokumentobjekt"
    class_name: ClassVar[str] = "Dokumentobjekt"
    class_model_uri: ClassVar[URIRef] = ARK.Dokumentobjekt

    variantFormat: Union[str, VariantformatId] = None
    opprettetAv: Union[str, ArkivressursId] = None
    filstorrelse: Optional[str] = None
    formatDetaljer: Optional[str] = None
    sjekksum: Optional[str] = None
    sjekksumAlgoritme: Optional[str] = None
    versjonsnummer: Optional[int] = None
    filformat: Optional[Union[str, FormatId]] = None
    referanseDokumentfil: Optional[Union[str, DokumentfilId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.variantFormat):
            self.MissingRequiredField("variantFormat")
        if not isinstance(self.variantFormat, VariantformatId):
            self.variantFormat = VariantformatId(self.variantFormat)

        if self._is_empty(self.opprettetAv):
            self.MissingRequiredField("opprettetAv")
        if not isinstance(self.opprettetAv, ArkivressursId):
            self.opprettetAv = ArkivressursId(self.opprettetAv)

        if self.filstorrelse is not None and not isinstance(self.filstorrelse, str):
            self.filstorrelse = str(self.filstorrelse)

        if self.formatDetaljer is not None and not isinstance(self.formatDetaljer, str):
            self.formatDetaljer = str(self.formatDetaljer)

        if self.sjekksum is not None and not isinstance(self.sjekksum, str):
            self.sjekksum = str(self.sjekksum)

        if self.sjekksumAlgoritme is not None and not isinstance(self.sjekksumAlgoritme, str):
            self.sjekksumAlgoritme = str(self.sjekksumAlgoritme)

        if self.versjonsnummer is not None and not isinstance(self.versjonsnummer, int):
            self.versjonsnummer = int(self.versjonsnummer)

        if self.filformat is not None and not isinstance(self.filformat, FormatId):
            self.filformat = FormatId(self.filformat)

        if self.referanseDokumentfil is not None and not isinstance(self.referanseDokumentfil, DokumentfilId):
            self.referanseDokumentfil = DokumentfilId(self.referanseDokumentfil)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Klasse(YAMLRoot):
    """
    Ein klasse i eit klassifikasjonssystem.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Klasse"]
    class_class_curie: ClassVar[str] = "ark:Klasse"
    class_name: ClassVar[str] = "Klasse"
    class_model_uri: ClassVar[URIRef] = ARK.Klasse

    klasseId: str = None
    tittel: str = None
    klassifikasjonssystem: Union[str, KlassifikasjonssystemId] = None
    rekkefølge: Optional[int] = None
    skjerming: Optional[Union[dict, "Skjerming"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.klasseId):
            self.MissingRequiredField("klasseId")
        if not isinstance(self.klasseId, str):
            self.klasseId = str(self.klasseId)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, str):
            self.tittel = str(self.tittel)

        if self._is_empty(self.klassifikasjonssystem):
            self.MissingRequiredField("klassifikasjonssystem")
        if not isinstance(self.klassifikasjonssystem, KlassifikasjonssystemId):
            self.klassifikasjonssystem = KlassifikasjonssystemId(self.klassifikasjonssystem)

        if self.rekkefølge is not None and not isinstance(self.rekkefølge, int):
            self.rekkefølge = int(self.rekkefølge)

        if self.skjerming is not None and not isinstance(self.skjerming, Skjerming):
            self.skjerming = Skjerming(**as_dict(self.skjerming))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Korrespondansepart(YAMLRoot):
    """
    Verksemd eller person som arkivskapar mottek eller sender arkivdokument til.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Korrespondansepart"]
    class_class_curie: ClassVar[str] = "ark:Korrespondansepart"
    class_name: ClassVar[str] = "Korrespondansepart"
    class_model_uri: ClassVar[URIRef] = ARK.Korrespondansepart

    korrespondanseparttype: Union[str, KorrespondansepartTypeId] = None
    adresse: Optional[Union[dict, "Adresse"]] = None
    foedselsnummer: Optional[str] = None
    kontaktinformasjon: Optional[Union[dict, "Kontaktinformasjon"]] = None
    kontaktperson: Optional[str] = None
    korrespondansepartNavn: Optional[str] = None
    organisasjonsnummer: Optional[str] = None
    skjerming: Optional[Union[dict, "Skjerming"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.korrespondanseparttype):
            self.MissingRequiredField("korrespondanseparttype")
        if not isinstance(self.korrespondanseparttype, KorrespondansepartTypeId):
            self.korrespondanseparttype = KorrespondansepartTypeId(self.korrespondanseparttype)

        if self.adresse is not None and not isinstance(self.adresse, Adresse):
            self.adresse = Adresse(**as_dict(self.adresse))

        if self.foedselsnummer is not None and not isinstance(self.foedselsnummer, str):
            self.foedselsnummer = str(self.foedselsnummer)

        if self.kontaktinformasjon is not None and not isinstance(self.kontaktinformasjon, Kontaktinformasjon):
            self.kontaktinformasjon = Kontaktinformasjon(**as_dict(self.kontaktinformasjon))

        if self.kontaktperson is not None and not isinstance(self.kontaktperson, str):
            self.kontaktperson = str(self.kontaktperson)

        if self.korrespondansepartNavn is not None and not isinstance(self.korrespondansepartNavn, str):
            self.korrespondansepartNavn = str(self.korrespondansepartNavn)

        if self.organisasjonsnummer is not None and not isinstance(self.organisasjonsnummer, str):
            self.organisasjonsnummer = str(self.organisasjonsnummer)

        if self.skjerming is not None and not isinstance(self.skjerming, Skjerming):
            self.skjerming = Skjerming(**as_dict(self.skjerming))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Merknad(YAMLRoot):
    """
    Merknad knytt til mappe, registrering eller dokumentbeskrivelse.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Merknad"]
    class_class_curie: ClassVar[str] = "ark:Merknad"
    class_name: ClassVar[str] = "Merknad"
    class_model_uri: ClassVar[URIRef] = ARK.Merknad

    merknadsdato: Union[str, XSDDateTime] = None
    merknadstekst: str = None
    merknadstype: Union[str, MerknadstypeId] = None
    merknadRegistrertAv: Union[str, ArkivressursId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.merknadsdato):
            self.MissingRequiredField("merknadsdato")
        if not isinstance(self.merknadsdato, XSDDateTime):
            self.merknadsdato = XSDDateTime(self.merknadsdato)

        if self._is_empty(self.merknadstekst):
            self.MissingRequiredField("merknadstekst")
        if not isinstance(self.merknadstekst, str):
            self.merknadstekst = str(self.merknadstekst)

        if self._is_empty(self.merknadstype):
            self.MissingRequiredField("merknadstype")
        if not isinstance(self.merknadstype, MerknadstypeId):
            self.merknadstype = MerknadstypeId(self.merknadstype)

        if self._is_empty(self.merknadRegistrertAv):
            self.MissingRequiredField("merknadRegistrertAv")
        if not isinstance(self.merknadRegistrertAv, ArkivressursId):
            self.merknadRegistrertAv = ArkivressursId(self.merknadRegistrertAv)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Part(YAMLRoot):
    """
    Part til Mappe, Registrering eller Dokumentbeskrivelse.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Part"]
    class_class_curie: ClassVar[str] = "ark:Part"
    class_name: ClassVar[str] = "Part"
    class_model_uri: ClassVar[URIRef] = ARK.Part

    partNavn: str = None
    adresse: Optional[Union[dict, "Adresse"]] = None
    foedselsnummer: Optional[str] = None
    kontaktinformasjon: Optional[Union[dict, "Kontaktinformasjon"]] = None
    kontaktperson: Optional[str] = None
    organisasjonsnummer: Optional[str] = None
    partRolle: Optional[Union[str, PartRolleId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.partNavn):
            self.MissingRequiredField("partNavn")
        if not isinstance(self.partNavn, str):
            self.partNavn = str(self.partNavn)

        if self.adresse is not None and not isinstance(self.adresse, Adresse):
            self.adresse = Adresse(**as_dict(self.adresse))

        if self.foedselsnummer is not None and not isinstance(self.foedselsnummer, str):
            self.foedselsnummer = str(self.foedselsnummer)

        if self.kontaktinformasjon is not None and not isinstance(self.kontaktinformasjon, Kontaktinformasjon):
            self.kontaktinformasjon = Kontaktinformasjon(**as_dict(self.kontaktinformasjon))

        if self.kontaktperson is not None and not isinstance(self.kontaktperson, str):
            self.kontaktperson = str(self.kontaktperson)

        if self.organisasjonsnummer is not None and not isinstance(self.organisasjonsnummer, str):
            self.organisasjonsnummer = str(self.organisasjonsnummer)

        if self.partRolle is not None and not isinstance(self.partRolle, PartRolleId):
            self.partRolle = PartRolleId(self.partRolle)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Skjerming(YAMLRoot):
    """
    Skjerming av mappe, registrering eller dokument etter offentleglova.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Skjerming"]
    class_class_curie: ClassVar[str] = "ark:Skjerming"
    class_name: ClassVar[str] = "Skjerming"
    class_model_uri: ClassVar[URIRef] = ARK.Skjerming

    skjermingshjemmel: Union[str, SkjermingshjemmelId] = None
    tilgangsrestriksjon: Union[str, TilgangsrestriksjonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.skjermingshjemmel):
            self.MissingRequiredField("skjermingshjemmel")
        if not isinstance(self.skjermingshjemmel, SkjermingshjemmelId):
            self.skjermingshjemmel = SkjermingshjemmelId(self.skjermingshjemmel)

        if self._is_empty(self.tilgangsrestriksjon):
            self.MissingRequiredField("tilgangsrestriksjon")
        if not isinstance(self.tilgangsrestriksjon, TilgangsrestriksjonId):
            self.tilgangsrestriksjon = TilgangsrestriksjonId(self.tilgangsrestriksjon)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DokumentStatus(YAMLRoot):
    """
    Status til eit dokument.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["DokumentStatus"]
    class_class_curie: ClassVar[str] = "ark:DokumentStatus"
    class_name: ClassVar[str] = "DokumentStatus"
    class_model_uri: ClassVar[URIRef] = ARK.DokumentStatus

    id: Union[str, DokumentStatusId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DokumentStatusId):
            self.id = DokumentStatusId(self.id)

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
class DokumentType(YAMLRoot):
    """
    Type dokument.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["DokumentType"]
    class_class_curie: ClassVar[str] = "ark:DokumentType"
    class_name: ClassVar[str] = "DokumentType"
    class_model_uri: ClassVar[URIRef] = ARK.DokumentType

    id: Union[str, DokumentTypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DokumentTypeId):
            self.id = DokumentTypeId(self.id)

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
class Format(YAMLRoot):
    """
    Dokumentets filformat.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Format"]
    class_class_curie: ClassVar[str] = "ark:Format"
    class_name: ClassVar[str] = "Format"
    class_model_uri: ClassVar[URIRef] = ARK.Format

    id: Union[str, FormatId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FormatId):
            self.id = FormatId(self.id)

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
class JournalpostType(YAMLRoot):
    """
    Namn på type journalpost.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["JournalpostType"]
    class_class_curie: ClassVar[str] = "ark:JournalpostType"
    class_name: ClassVar[str] = "JournalpostType"
    class_model_uri: ClassVar[URIRef] = ARK.JournalpostType

    id: Union[str, JournalpostTypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JournalpostTypeId):
            self.id = JournalpostTypeId(self.id)

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
class JournalStatus(YAMLRoot):
    """
    Status til journalposten.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["JournalStatus"]
    class_class_curie: ClassVar[str] = "ark:JournalStatus"
    class_name: ClassVar[str] = "JournalStatus"
    class_model_uri: ClassVar[URIRef] = ARK.JournalStatus

    id: Union[str, JournalStatusId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JournalStatusId):
            self.id = JournalStatusId(self.id)

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
class Klassifikasjonstype(YAMLRoot):
    """
    Type klassifikasjonssystem.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Klassifikasjonstype"]
    class_class_curie: ClassVar[str] = "ark:Klassifikasjonstype"
    class_name: ClassVar[str] = "Klassifikasjonstype"
    class_model_uri: ClassVar[URIRef] = ARK.Klassifikasjonstype

    id: Union[str, KlassifikasjonstypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KlassifikasjonstypeId):
            self.id = KlassifikasjonstypeId(self.id)

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
class KorrespondansepartType(YAMLRoot):
    """
    Type korrespondansepart.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["KorrespondansepartType"]
    class_class_curie: ClassVar[str] = "ark:KorrespondansepartType"
    class_name: ClassVar[str] = "KorrespondansepartType"
    class_model_uri: ClassVar[URIRef] = ARK.KorrespondansepartType

    id: Union[str, KorrespondansepartTypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KorrespondansepartTypeId):
            self.id = KorrespondansepartTypeId(self.id)

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
class Merknadstype(YAMLRoot):
    """
    Namn på type merknad.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Merknadstype"]
    class_class_curie: ClassVar[str] = "ark:Merknadstype"
    class_name: ClassVar[str] = "Merknadstype"
    class_model_uri: ClassVar[URIRef] = ARK.Merknadstype

    id: Union[str, MerknadstypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MerknadstypeId):
            self.id = MerknadstypeId(self.id)

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
class PartRolle(YAMLRoot):
    """
    Rolla til ein part.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["PartRolle"]
    class_class_curie: ClassVar[str] = "ark:PartRolle"
    class_name: ClassVar[str] = "PartRolle"
    class_model_uri: ClassVar[URIRef] = ARK.PartRolle

    id: Union[str, PartRolleId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PartRolleId):
            self.id = PartRolleId(self.id)

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
class Rolle(YAMLRoot):
    """
    Rolla til ein arkivressurs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Rolle"]
    class_class_curie: ClassVar[str] = "ark:Rolle"
    class_name: ClassVar[str] = "Rolle"
    class_model_uri: ClassVar[URIRef] = ARK.Rolle

    id: Union[str, RolleId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RolleId):
            self.id = RolleId(self.id)

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
class Saksmappetype(YAMLRoot):
    """
    Type saksmappe — differensierer innhald og behandlingsrutine.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Saksmappetype"]
    class_class_curie: ClassVar[str] = "ark:Saksmappetype"
    class_name: ClassVar[str] = "Saksmappetype"
    class_model_uri: ClassVar[URIRef] = ARK.Saksmappetype

    id: Union[str, SaksmappetypeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SaksmappetypeId):
            self.id = SaksmappetypeId(self.id)

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
class Saksstatus(YAMLRoot):
    """
    Status til saksmappa.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Saksstatus"]
    class_class_curie: ClassVar[str] = "ark:Saksstatus"
    class_name: ClassVar[str] = "Saksstatus"
    class_model_uri: ClassVar[URIRef] = ARK.Saksstatus

    id: Union[str, SaksstatusId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SaksstatusId):
            self.id = SaksstatusId(self.id)

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
class Skjermingshjemmel(YAMLRoot):
    """
    Tilvising til heimel i offentleglova, tryggingslova eller tryggingsinstruksen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Skjermingshjemmel"]
    class_class_curie: ClassVar[str] = "ark:Skjermingshjemmel"
    class_name: ClassVar[str] = "Skjermingshjemmel"
    class_model_uri: ClassVar[URIRef] = ARK.Skjermingshjemmel

    id: Union[str, SkjermingshjemmelId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SkjermingshjemmelId):
            self.id = SkjermingshjemmelId(self.id)

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
class Tilgangsgruppe(YAMLRoot):
    """
    Tilgangsgruppe for intern skjerming av innhald.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Tilgangsgruppe"]
    class_class_curie: ClassVar[str] = "ark:Tilgangsgruppe"
    class_name: ClassVar[str] = "Tilgangsgruppe"
    class_model_uri: ClassVar[URIRef] = ARK.Tilgangsgruppe

    id: Union[str, TilgangsgruppeId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TilgangsgruppeId):
            self.id = TilgangsgruppeId(self.id)

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
class Tilgangsrestriksjon(YAMLRoot):
    """
    Angiving av at dokumenta ikkje er offentleg tilgjengelege.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Tilgangsrestriksjon"]
    class_class_curie: ClassVar[str] = "ark:Tilgangsrestriksjon"
    class_name: ClassVar[str] = "Tilgangsrestriksjon"
    class_model_uri: ClassVar[URIRef] = ARK.Tilgangsrestriksjon

    id: Union[str, TilgangsrestriksjonId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TilgangsrestriksjonId):
            self.id = TilgangsrestriksjonId(self.id)

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
class TilknyttetRegistreringSom(YAMLRoot):
    """
    Kva rolle dokumentet har i høve registreringa (t.d. Hoveddokument, Vedlegg).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["TilknyttetRegistreringSom"]
    class_class_curie: ClassVar[str] = "ark:TilknyttetRegistreringSom"
    class_name: ClassVar[str] = "TilknyttetRegistreringSom"
    class_model_uri: ClassVar[URIRef] = ARK.TilknyttetRegistreringSom

    id: Union[str, TilknyttetRegistreringSomId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TilknyttetRegistreringSomId):
            self.id = TilknyttetRegistreringSomId(self.id)

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
class Variantformat(YAMLRoot):
    """
    Angiving av kva variant eit dokument førekjem i.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ARK["Variantformat"]
    class_class_curie: ClassVar[str] = "ark:Variantformat"
    class_name: ClassVar[str] = "Variantformat"
    class_model_uri: ClassVar[URIRef] = ARK.Variantformat

    id: Union[str, VariantformatId] = None
    kode: str = None
    navn: str = None
    gyldighetsperiode: Optional[Union[dict, "Periode"]] = None
    passiv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantformatId):
            self.id = VariantformatId(self.id)

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
    class_model_uri: ClassVar[URIRef] = ARK.Aktoer

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
    class_model_uri: ClassVar[URIRef] = ARK.Begrep

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
    class_model_uri: ClassVar[URIRef] = ARK.Enhet

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
    class_model_uri: ClassVar[URIRef] = ARK.Identifikator

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
    class_model_uri: ClassVar[URIRef] = ARK.Periode

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
    class_model_uri: ClassVar[URIRef] = ARK.Personnavn

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
    class_model_uri: ClassVar[URIRef] = ARK.Kontaktinformasjon

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
    class_model_uri: ClassVar[URIRef] = ARK.Adresse

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
    class_model_uri: ClassVar[URIRef] = ARK.Matrikkelnummer

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
    class_model_uri: ClassVar[URIRef] = ARK.Landkode

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
    class_model_uri: ClassVar[URIRef] = ARK.Kjonn

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
    class_model_uri: ClassVar[URIRef] = ARK.Fylke

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
    class_model_uri: ClassVar[URIRef] = ARK.Kommune

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
    class_model_uri: ClassVar[URIRef] = ARK.Spraak

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
    class_model_uri: ClassVar[URIRef] = ARK.Valuta

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
    class_model_uri: ClassVar[URIRef] = ARK.Person

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
    class_model_uri: ClassVar[URIRef] = ARK.Kontaktperson

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
    class_model_uri: ClassVar[URIRef] = ARK.Virksomhet

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
                   model_uri=ARK.id, domain=None, range=URIRef)

slots.arkivContainer__arkivdelar = Slot(uri=ARK.arkivdelar, name="arkivContainer__arkivdelar", curie=ARK.curie('arkivdelar'),
                   model_uri=ARK.arkivContainer__arkivdelar, domain=None, range=Optional[Union[dict[Union[str, ArkivdelId], Union[dict, Arkivdel]], list[Union[dict, Arkivdel]]]])

slots.arkivContainer__arkivressursar = Slot(uri=ARK.arkivressursar, name="arkivContainer__arkivressursar", curie=ARK.curie('arkivressursar'),
                   model_uri=ARK.arkivContainer__arkivressursar, domain=None, range=Optional[Union[dict[Union[str, ArkivressursId], Union[dict, Arkivressurs]], list[Union[dict, Arkivressurs]]]])

slots.arkivContainer__autorisasjonar = Slot(uri=ARK.autorisasjonar, name="arkivContainer__autorisasjonar", curie=ARK.curie('autorisasjonar'),
                   model_uri=ARK.arkivContainer__autorisasjonar, domain=None, range=Optional[Union[dict[Union[str, AutorisasjonId], Union[dict, Autorisasjon]], list[Union[dict, Autorisasjon]]]])

slots.arkivContainer__administrativeEiningar = Slot(uri=ARK.administrativeEiningar, name="arkivContainer__administrativeEiningar", curie=ARK.curie('administrativeEiningar'),
                   model_uri=ARK.arkivContainer__administrativeEiningar, domain=None, range=Optional[Union[dict[Union[str, AdministrativEnhetId], Union[dict, AdministrativEnhet]], list[Union[dict, AdministrativEnhet]]]])

slots.arkivContainer__dokumentfiler = Slot(uri=ARK.dokumentfiler, name="arkivContainer__dokumentfiler", curie=ARK.curie('dokumentfiler'),
                   model_uri=ARK.arkivContainer__dokumentfiler, domain=None, range=Optional[Union[dict[Union[str, DokumentfilId], Union[dict, Dokumentfil]], list[Union[dict, Dokumentfil]]]])

slots.arkivContainer__dokumentbeskrivelsar = Slot(uri=ARK.dokumentbeskrivelsar, name="arkivContainer__dokumentbeskrivelsar", curie=ARK.curie('dokumentbeskrivelsar'),
                   model_uri=ARK.arkivContainer__dokumentbeskrivelsar, domain=None, range=Optional[Union[dict[Union[str, DokumentbeskrivelseId], Union[dict, Dokumentbeskrivelse]], list[Union[dict, Dokumentbeskrivelse]]]])

slots.arkivContainer__journalpostar = Slot(uri=ARK.journalpostar, name="arkivContainer__journalpostar", curie=ARK.curie('journalpostar'),
                   model_uri=ARK.arkivContainer__journalpostar, domain=None, range=Optional[Union[dict[Union[str, JournalpostId], Union[dict, Journalpost]], list[Union[dict, Journalpost]]]])

slots.arkivContainer__klassifikasjonssystem = Slot(uri=ARK.klassifikasjonssystem, name="arkivContainer__klassifikasjonssystem", curie=ARK.curie('klassifikasjonssystem'),
                   model_uri=ARK.arkivContainer__klassifikasjonssystem, domain=None, range=Optional[Union[dict[Union[str, KlassifikasjonssystemId], Union[dict, Klassifikasjonssystem]], list[Union[dict, Klassifikasjonssystem]]]])

slots.arkivContainer__tilgangar = Slot(uri=ARK.tilgangar, name="arkivContainer__tilgangar", curie=ARK.curie('tilgangar'),
                   model_uri=ARK.arkivContainer__tilgangar, domain=None, range=Optional[Union[dict[Union[str, TilgangId], Union[dict, Tilgang]], list[Union[dict, Tilgang]]]])

slots.arkivContainer__sakar = Slot(uri=ARK.sakar, name="arkivContainer__sakar", curie=ARK.curie('sakar'),
                   model_uri=ARK.arkivContainer__sakar, domain=None, range=Optional[Union[dict[Union[str, SakId], Union[dict, Sak]], list[Union[dict, Sak]]]])

slots.arkivContainer__personalmappe = Slot(uri=ARK.personalmappe, name="arkivContainer__personalmappe", curie=ARK.curie('personalmappe'),
                   model_uri=ARK.arkivContainer__personalmappe, domain=None, range=Optional[Union[dict[Union[str, PersonalmappeId], Union[dict, Personalmappe]], list[Union[dict, Personalmappe]]]])

slots.arkivContainer__dispensasjonAutomatiskFredaKulturminne = Slot(uri=ARK.dispensasjonAutomatiskFredaKulturminne, name="arkivContainer__dispensasjonAutomatiskFredaKulturminne", curie=ARK.curie('dispensasjonAutomatiskFredaKulturminne'),
                   model_uri=ARK.arkivContainer__dispensasjonAutomatiskFredaKulturminne, domain=None, range=Optional[Union[dict[Union[str, DispensasjonAutomatiskFredaKulturminneId], Union[dict, DispensasjonAutomatiskFredaKulturminne]], list[Union[dict, DispensasjonAutomatiskFredaKulturminne]]]])

slots.arkivContainer__tilskuddFartoy = Slot(uri=ARK.tilskuddFartoy, name="arkivContainer__tilskuddFartoy", curie=ARK.curie('tilskuddFartoy'),
                   model_uri=ARK.arkivContainer__tilskuddFartoy, domain=None, range=Optional[Union[dict[Union[str, TilskuddFartoyId], Union[dict, TilskuddFartoy]], list[Union[dict, TilskuddFartoy]]]])

slots.arkivContainer__tilskuddFredaBygningPrivatEie = Slot(uri=ARK.tilskuddFredaBygningPrivatEie, name="arkivContainer__tilskuddFredaBygningPrivatEie", curie=ARK.curie('tilskuddFredaBygningPrivatEie'),
                   model_uri=ARK.arkivContainer__tilskuddFredaBygningPrivatEie, domain=None, range=Optional[Union[dict[Union[str, TilskuddFredaBygningPrivatEieId], Union[dict, TilskuddFredaBygningPrivatEie]], list[Union[dict, TilskuddFredaBygningPrivatEie]]]])

slots.arkivContainer__soeknadDrosjeloeyve = Slot(uri=ARK.soeknadDrosjeloeyve, name="arkivContainer__soeknadDrosjeloeyve", curie=ARK.curie('soeknadDrosjeloeyve'),
                   model_uri=ARK.arkivContainer__soeknadDrosjeloeyve, domain=None, range=Optional[Union[dict[Union[str, SoeknadDrosjeloeyveId], Union[dict, SoeknadDrosjeloeyve]], list[Union[dict, SoeknadDrosjeloeyve]]]])

slots.arkivContainer__dokumentstatuskodar = Slot(uri=ARK.dokumentstatuskodar, name="arkivContainer__dokumentstatuskodar", curie=ARK.curie('dokumentstatuskodar'),
                   model_uri=ARK.arkivContainer__dokumentstatuskodar, domain=None, range=Optional[Union[dict[Union[str, DokumentStatusId], Union[dict, DokumentStatus]], list[Union[dict, DokumentStatus]]]])

slots.arkivContainer__dokumenttypar = Slot(uri=ARK.dokumenttypar, name="arkivContainer__dokumenttypar", curie=ARK.curie('dokumenttypar'),
                   model_uri=ARK.arkivContainer__dokumenttypar, domain=None, range=Optional[Union[dict[Union[str, DokumentTypeId], Union[dict, DokumentType]], list[Union[dict, DokumentType]]]])

slots.arkivContainer__formatar = Slot(uri=ARK.formatar, name="arkivContainer__formatar", curie=ARK.curie('formatar'),
                   model_uri=ARK.arkivContainer__formatar, domain=None, range=Optional[Union[dict[Union[str, FormatId], Union[dict, Format]], list[Union[dict, Format]]]])

slots.arkivContainer__journalposttypar = Slot(uri=ARK.journalposttypar, name="arkivContainer__journalposttypar", curie=ARK.curie('journalposttypar'),
                   model_uri=ARK.arkivContainer__journalposttypar, domain=None, range=Optional[Union[dict[Union[str, JournalpostTypeId], Union[dict, JournalpostType]], list[Union[dict, JournalpostType]]]])

slots.arkivContainer__journalstatuskodar = Slot(uri=ARK.journalstatuskodar, name="arkivContainer__journalstatuskodar", curie=ARK.curie('journalstatuskodar'),
                   model_uri=ARK.arkivContainer__journalstatuskodar, domain=None, range=Optional[Union[dict[Union[str, JournalStatusId], Union[dict, JournalStatus]], list[Union[dict, JournalStatus]]]])

slots.arkivContainer__klassifikasjonstypar = Slot(uri=ARK.klassifikasjonstypar, name="arkivContainer__klassifikasjonstypar", curie=ARK.curie('klassifikasjonstypar'),
                   model_uri=ARK.arkivContainer__klassifikasjonstypar, domain=None, range=Optional[Union[dict[Union[str, KlassifikasjonstypeId], Union[dict, Klassifikasjonstype]], list[Union[dict, Klassifikasjonstype]]]])

slots.arkivContainer__korrespondanseparttypar = Slot(uri=ARK.korrespondanseparttypar, name="arkivContainer__korrespondanseparttypar", curie=ARK.curie('korrespondanseparttypar'),
                   model_uri=ARK.arkivContainer__korrespondanseparttypar, domain=None, range=Optional[Union[dict[Union[str, KorrespondansepartTypeId], Union[dict, KorrespondansepartType]], list[Union[dict, KorrespondansepartType]]]])

slots.arkivContainer__merknadstypar = Slot(uri=ARK.merknadstypar, name="arkivContainer__merknadstypar", curie=ARK.curie('merknadstypar'),
                   model_uri=ARK.arkivContainer__merknadstypar, domain=None, range=Optional[Union[dict[Union[str, MerknadstypeId], Union[dict, Merknadstype]], list[Union[dict, Merknadstype]]]])

slots.arkivContainer__partRollar = Slot(uri=ARK.partRollar, name="arkivContainer__partRollar", curie=ARK.curie('partRollar'),
                   model_uri=ARK.arkivContainer__partRollar, domain=None, range=Optional[Union[dict[Union[str, PartRolleId], Union[dict, PartRolle]], list[Union[dict, PartRolle]]]])

slots.arkivContainer__rollar = Slot(uri=ARK.rollar, name="arkivContainer__rollar", curie=ARK.curie('rollar'),
                   model_uri=ARK.arkivContainer__rollar, domain=None, range=Optional[Union[dict[Union[str, RolleId], Union[dict, Rolle]], list[Union[dict, Rolle]]]])

slots.arkivContainer__saksmappetypar = Slot(uri=ARK.saksmappetypar, name="arkivContainer__saksmappetypar", curie=ARK.curie('saksmappetypar'),
                   model_uri=ARK.arkivContainer__saksmappetypar, domain=None, range=Optional[Union[dict[Union[str, SaksmappetypeId], Union[dict, Saksmappetype]], list[Union[dict, Saksmappetype]]]])

slots.arkivContainer__sakstatuskodar = Slot(uri=ARK.sakstatuskodar, name="arkivContainer__sakstatuskodar", curie=ARK.curie('sakstatuskodar'),
                   model_uri=ARK.arkivContainer__sakstatuskodar, domain=None, range=Optional[Union[dict[Union[str, SaksstatusId], Union[dict, Saksstatus]], list[Union[dict, Saksstatus]]]])

slots.arkivContainer__skjermingsheimlar = Slot(uri=ARK.skjermingsheimlar, name="arkivContainer__skjermingsheimlar", curie=ARK.curie('skjermingsheimlar'),
                   model_uri=ARK.arkivContainer__skjermingsheimlar, domain=None, range=Optional[Union[dict[Union[str, SkjermingshjemmelId], Union[dict, Skjermingshjemmel]], list[Union[dict, Skjermingshjemmel]]]])

slots.arkivContainer__tilgangsgrupper = Slot(uri=ARK.tilgangsgrupper, name="arkivContainer__tilgangsgrupper", curie=ARK.curie('tilgangsgrupper'),
                   model_uri=ARK.arkivContainer__tilgangsgrupper, domain=None, range=Optional[Union[dict[Union[str, TilgangsgruppeId], Union[dict, Tilgangsgruppe]], list[Union[dict, Tilgangsgruppe]]]])

slots.arkivContainer__tilgangsrestriksjonar = Slot(uri=ARK.tilgangsrestriksjonar, name="arkivContainer__tilgangsrestriksjonar", curie=ARK.curie('tilgangsrestriksjonar'),
                   model_uri=ARK.arkivContainer__tilgangsrestriksjonar, domain=None, range=Optional[Union[dict[Union[str, TilgangsrestriksjonId], Union[dict, Tilgangsrestriksjon]], list[Union[dict, Tilgangsrestriksjon]]]])

slots.arkivContainer__tilknyttetRegistreringSomKodar = Slot(uri=ARK.tilknyttetRegistreringSomKodar, name="arkivContainer__tilknyttetRegistreringSomKodar", curie=ARK.curie('tilknyttetRegistreringSomKodar'),
                   model_uri=ARK.arkivContainer__tilknyttetRegistreringSomKodar, domain=None, range=Optional[Union[dict[Union[str, TilknyttetRegistreringSomId], Union[dict, TilknyttetRegistreringSom]], list[Union[dict, TilknyttetRegistreringSom]]]])

slots.arkivContainer__variantformatar = Slot(uri=ARK.variantformatar, name="arkivContainer__variantformatar", curie=ARK.curie('variantformatar'),
                   model_uri=ARK.arkivContainer__variantformatar, domain=None, range=Optional[Union[dict[Union[str, VariantformatId], Union[dict, Variantformat]], list[Union[dict, Variantformat]]]])

slots.mappe__avsluttetDato = Slot(uri=ARK.avsluttetDato, name="mappe__avsluttetDato", curie=ARK.curie('avsluttetDato'),
                   model_uri=ARK.mappe__avsluttetDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mappe__beskrivelse = Slot(uri=ARK.beskrivelse, name="mappe__beskrivelse", curie=ARK.curie('beskrivelse'),
                   model_uri=ARK.mappe__beskrivelse, domain=None, range=Optional[str])

slots.mappe__klasse = Slot(uri=ARK.klasse, name="mappe__klasse", curie=ARK.curie('klasse'),
                   model_uri=ARK.mappe__klasse, domain=None, range=Optional[Union[Union[dict, Klasse], list[Union[dict, Klasse]]]])

slots.mappe__mappeId = Slot(uri=ARK.mappeId, name="mappe__mappeId", curie=ARK.curie('mappeId'),
                   model_uri=ARK.mappe__mappeId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.mappe__merknad = Slot(uri=ARK.merknad, name="mappe__merknad", curie=ARK.curie('merknad'),
                   model_uri=ARK.mappe__merknad, domain=None, range=Optional[Union[Union[dict, Merknad], list[Union[dict, Merknad]]]])

slots.mappe__noekkelord = Slot(uri=ARK.noekkelord, name="mappe__noekkelord", curie=ARK.curie('noekkelord'),
                   model_uri=ARK.mappe__noekkelord, domain=None, range=Optional[Union[str, list[str]]])

slots.mappe__offentligTittel = Slot(uri=ARK.offentligTittel, name="mappe__offentligTittel", curie=ARK.curie('offentligTittel'),
                   model_uri=ARK.mappe__offentligTittel, domain=None, range=Optional[str])

slots.mappe__opprettetDato = Slot(uri=ARK.opprettetDato, name="mappe__opprettetDato", curie=ARK.curie('opprettetDato'),
                   model_uri=ARK.mappe__opprettetDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mappe__part = Slot(uri=ARK.part, name="mappe__part", curie=ARK.curie('part'),
                   model_uri=ARK.mappe__part, domain=None, range=Optional[Union[Union[dict, Part], list[Union[dict, Part]]]])

slots.mappe__skjerming = Slot(uri=ARK.skjerming, name="mappe__skjerming", curie=ARK.curie('skjerming'),
                   model_uri=ARK.mappe__skjerming, domain=None, range=Optional[Union[dict, Skjerming]])

slots.mappe__tittel = Slot(uri=ARK.tittel, name="mappe__tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.mappe__tittel, domain=None, range=Optional[str])

slots.mappe__arkivdel = Slot(uri=ARK.arkivdel, name="mappe__arkivdel", curie=ARK.curie('arkivdel'),
                   model_uri=ARK.mappe__arkivdel, domain=None, range=Optional[Union[str, ArkivdelId]])

slots.mappe__avsluttetAv = Slot(uri=ARK.avsluttetAv, name="mappe__avsluttetAv", curie=ARK.curie('avsluttetAv'),
                   model_uri=ARK.mappe__avsluttetAv, domain=None, range=Optional[Union[str, ArkivressursId]])

slots.mappe__opprettetAv = Slot(uri=ARK.opprettetAv, name="mappe__opprettetAv", curie=ARK.curie('opprettetAv'),
                   model_uri=ARK.mappe__opprettetAv, domain=None, range=Union[str, ArkivressursId])

slots.saksmappe__journalpost = Slot(uri=ARK.journalpost, name="saksmappe__journalpost", curie=ARK.curie('journalpost'),
                   model_uri=ARK.saksmappe__journalpost, domain=None, range=Optional[Union[Union[str, JournalpostId], list[Union[str, JournalpostId]]]])

slots.saksmappe__saksaar = Slot(uri=ARK.saksaar, name="saksmappe__saksaar", curie=ARK.curie('saksaar'),
                   model_uri=ARK.saksmappe__saksaar, domain=None, range=Optional[str])

slots.saksmappe__saksdato = Slot(uri=ARK.saksdato, name="saksmappe__saksdato", curie=ARK.curie('saksdato'),
                   model_uri=ARK.saksmappe__saksdato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.saksmappe__sakssekvensnummer = Slot(uri=ARK.sakssekvensnummer, name="saksmappe__sakssekvensnummer", curie=ARK.curie('sakssekvensnummer'),
                   model_uri=ARK.saksmappe__sakssekvensnummer, domain=None, range=Optional[str])

slots.saksmappe__utlaantDato = Slot(uri=ARK.utlaantDato, name="saksmappe__utlaantDato", curie=ARK.curie('utlaantDato'),
                   model_uri=ARK.saksmappe__utlaantDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.saksmappe__saksmappetype = Slot(uri=ARK.saksmappetype, name="saksmappe__saksmappetype", curie=ARK.curie('saksmappetype'),
                   model_uri=ARK.saksmappe__saksmappetype, domain=None, range=Optional[Union[str, SaksmappetypeId]])

slots.saksmappe__saksstatus = Slot(uri=ARK.saksstatus, name="saksmappe__saksstatus", curie=ARK.curie('saksstatus'),
                   model_uri=ARK.saksmappe__saksstatus, domain=None, range=Union[str, SaksstatusId])

slots.saksmappe__tilgangsgruppe = Slot(uri=ARK.tilgangsgruppe, name="saksmappe__tilgangsgruppe", curie=ARK.curie('tilgangsgruppe'),
                   model_uri=ARK.saksmappe__tilgangsgruppe, domain=None, range=Optional[Union[str, TilgangsgruppeId]])

slots.saksmappe__journalenhet = Slot(uri=ARK.journalenhet, name="saksmappe__journalenhet", curie=ARK.curie('journalenhet'),
                   model_uri=ARK.saksmappe__journalenhet, domain=None, range=Optional[Union[str, AdministrativEnhetId]])

slots.saksmappe__administrativEnhet = Slot(uri=ARK.administrativEnhet, name="saksmappe__administrativEnhet", curie=ARK.curie('administrativEnhet'),
                   model_uri=ARK.saksmappe__administrativEnhet, domain=None, range=Union[str, AdministrativEnhetId])

slots.saksmappe__saksansvarlig = Slot(uri=ARK.saksansvarlig, name="saksmappe__saksansvarlig", curie=ARK.curie('saksansvarlig'),
                   model_uri=ARK.saksmappe__saksansvarlig, domain=None, range=Union[str, ArkivressursId])

slots.registrering__arkivertDato = Slot(uri=ARK.arkivertDato, name="registrering__arkivertDato", curie=ARK.curie('arkivertDato'),
                   model_uri=ARK.registrering__arkivertDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.registrering__beskrivelse = Slot(uri=ARK.beskrivelse, name="registrering__beskrivelse", curie=ARK.curie('beskrivelse'),
                   model_uri=ARK.registrering__beskrivelse, domain=None, range=Optional[str])

slots.registrering__dokumentbeskrivelse = Slot(uri=ARK.dokumentbeskrivelse, name="registrering__dokumentbeskrivelse", curie=ARK.curie('dokumentbeskrivelse'),
                   model_uri=ARK.registrering__dokumentbeskrivelse, domain=None, range=Optional[Union[Union[str, DokumentbeskrivelseId], list[Union[str, DokumentbeskrivelseId]]]])

slots.registrering__forfatter = Slot(uri=ARK.forfatter, name="registrering__forfatter", curie=ARK.curie('forfatter'),
                   model_uri=ARK.registrering__forfatter, domain=None, range=Optional[Union[str, list[str]]])

slots.registrering__klasse = Slot(uri=ARK.klasse, name="registrering__klasse", curie=ARK.curie('klasse'),
                   model_uri=ARK.registrering__klasse, domain=None, range=Optional[Union[dict, Klasse]])

slots.registrering__korrespondansepart = Slot(uri=ARK.korrespondansepart, name="registrering__korrespondansepart", curie=ARK.curie('korrespondansepart'),
                   model_uri=ARK.registrering__korrespondansepart, domain=None, range=Optional[Union[Union[dict, Korrespondansepart], list[Union[dict, Korrespondansepart]]]])

slots.registrering__merknad = Slot(uri=ARK.merknad, name="registrering__merknad", curie=ARK.curie('merknad'),
                   model_uri=ARK.registrering__merknad, domain=None, range=Optional[Union[Union[dict, Merknad], list[Union[dict, Merknad]]]])

slots.registrering__nokkelord = Slot(uri=ARK.nokkelord, name="registrering__nokkelord", curie=ARK.curie('nokkelord'),
                   model_uri=ARK.registrering__nokkelord, domain=None, range=Optional[Union[str, list[str]]])

slots.registrering__offentligTittel = Slot(uri=ARK.offentligTittel, name="registrering__offentligTittel", curie=ARK.curie('offentligTittel'),
                   model_uri=ARK.registrering__offentligTittel, domain=None, range=Optional[str])

slots.registrering__opprettetDato = Slot(uri=ARK.opprettetDato, name="registrering__opprettetDato", curie=ARK.curie('opprettetDato'),
                   model_uri=ARK.registrering__opprettetDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.registrering__part = Slot(uri=ARK.part, name="registrering__part", curie=ARK.curie('part'),
                   model_uri=ARK.registrering__part, domain=None, range=Optional[Union[Union[dict, Part], list[Union[dict, Part]]]])

slots.registrering__referanseArkivDel = Slot(uri=ARK.referanseArkivDel, name="registrering__referanseArkivDel", curie=ARK.curie('referanseArkivDel'),
                   model_uri=ARK.registrering__referanseArkivDel, domain=None, range=Optional[Union[str, list[str]]])

slots.registrering__registreringsId = Slot(uri=ARK.registreringsId, name="registrering__registreringsId", curie=ARK.curie('registreringsId'),
                   model_uri=ARK.registrering__registreringsId, domain=None, range=Optional[str])

slots.registrering__skjerming = Slot(uri=ARK.skjerming, name="registrering__skjerming", curie=ARK.curie('skjerming'),
                   model_uri=ARK.registrering__skjerming, domain=None, range=Optional[Union[dict, Skjerming]])

slots.registrering__tittel = Slot(uri=ARK.tittel, name="registrering__tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.registrering__tittel, domain=None, range=str)

slots.registrering__tilgangsgruppe = Slot(uri=ARK.tilgangsgruppe, name="registrering__tilgangsgruppe", curie=ARK.curie('tilgangsgruppe'),
                   model_uri=ARK.registrering__tilgangsgruppe, domain=None, range=Optional[Union[str, TilgangsgruppeId]])

slots.registrering__administrativEnhet = Slot(uri=ARK.administrativEnhet, name="registrering__administrativEnhet", curie=ARK.curie('administrativEnhet'),
                   model_uri=ARK.registrering__administrativEnhet, domain=None, range=Optional[Union[str, AdministrativEnhetId]])

slots.registrering__arkivdel = Slot(uri=ARK.arkivdel, name="registrering__arkivdel", curie=ARK.curie('arkivdel'),
                   model_uri=ARK.registrering__arkivdel, domain=None, range=Optional[Union[str, ArkivdelId]])

slots.registrering__saksbehandler = Slot(uri=ARK.saksbehandler, name="registrering__saksbehandler", curie=ARK.curie('saksbehandler'),
                   model_uri=ARK.registrering__saksbehandler, domain=None, range=Optional[Union[str, ArkivressursId]])

slots.registrering__arkivertAv = Slot(uri=ARK.arkivertAv, name="registrering__arkivertAv", curie=ARK.curie('arkivertAv'),
                   model_uri=ARK.registrering__arkivertAv, domain=None, range=Union[str, ArkivressursId])

slots.registrering__opprettetAv = Slot(uri=ARK.opprettetAv, name="registrering__opprettetAv", curie=ARK.curie('opprettetAv'),
                   model_uri=ARK.registrering__opprettetAv, domain=None, range=Union[str, ArkivressursId])

slots.administrativEnhet__navn = Slot(uri=ARK.navn, name="administrativEnhet__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.administrativEnhet__navn, domain=None, range=str)

slots.administrativEnhet__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="administrativEnhet__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.administrativEnhet__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.administrativEnhet__organisasjonselement = Slot(uri=ARK.organisasjonselement, name="administrativEnhet__organisasjonselement", curie=ARK.curie('organisasjonselement'),
                   model_uri=ARK.administrativEnhet__organisasjonselement, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.arkivdel__tittel = Slot(uri=ARK.tittel, name="arkivdel__tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.arkivdel__tittel, domain=None, range=str)

slots.arkivdel__klassifikasjonssystem = Slot(uri=ARK.klassifikasjonssystem, name="arkivdel__klassifikasjonssystem", curie=ARK.curie('klassifikasjonssystem'),
                   model_uri=ARK.arkivdel__klassifikasjonssystem, domain=None, range=Optional[Union[Union[str, KlassifikasjonssystemId], list[Union[str, KlassifikasjonssystemId]]]])

slots.arkivressurs__kildesystemId = Slot(uri=ARK.kildesystemId, name="arkivressurs__kildesystemId", curie=ARK.curie('kildesystemId'),
                   model_uri=ARK.arkivressurs__kildesystemId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.arkivressurs__personalressurs = Slot(uri=ARK.personalressurs, name="arkivressurs__personalressurs", curie=ARK.curie('personalressurs'),
                   model_uri=ARK.arkivressurs__personalressurs, domain=None, range=Union[str, URIorCURIE])

slots.arkivressurs__autorisasjon = Slot(uri=ARK.autorisasjon, name="arkivressurs__autorisasjon", curie=ARK.curie('autorisasjon'),
                   model_uri=ARK.arkivressurs__autorisasjon, domain=None, range=Optional[Union[Union[str, AutorisasjonId], list[Union[str, AutorisasjonId]]]])

slots.arkivressurs__tilgang = Slot(uri=ARK.tilgang, name="arkivressurs__tilgang", curie=ARK.curie('tilgang'),
                   model_uri=ARK.arkivressurs__tilgang, domain=None, range=Optional[Union[Union[str, TilgangId], list[Union[str, TilgangId]]]])

slots.autorisasjon__tilgangsrestriksjon = Slot(uri=ARK.tilgangsrestriksjon, name="autorisasjon__tilgangsrestriksjon", curie=ARK.curie('tilgangsrestriksjon'),
                   model_uri=ARK.autorisasjon__tilgangsrestriksjon, domain=None, range=Union[Union[str, TilgangsrestriksjonId], list[Union[str, TilgangsrestriksjonId]]])

slots.autorisasjon__administrativenhet = Slot(uri=ARK.administrativenhet, name="autorisasjon__administrativenhet", curie=ARK.curie('administrativenhet'),
                   model_uri=ARK.autorisasjon__administrativenhet, domain=None, range=Optional[Union[Union[str, AdministrativEnhetId], list[Union[str, AdministrativEnhetId]]]])

slots.autorisasjon__arkivressurs = Slot(uri=ARK.arkivressurs, name="autorisasjon__arkivressurs", curie=ARK.curie('arkivressurs'),
                   model_uri=ARK.autorisasjon__arkivressurs, domain=None, range=Optional[Union[Union[str, ArkivressursId], list[Union[str, ArkivressursId]]]])

slots.dokumentfil__data = Slot(uri=ARK.data, name="dokumentfil__data", curie=ARK.curie('data'),
                   model_uri=ARK.dokumentfil__data, domain=None, range=str)

slots.dokumentfil__filnavn = Slot(uri=ARK.filnavn, name="dokumentfil__filnavn", curie=ARK.curie('filnavn'),
                   model_uri=ARK.dokumentfil__filnavn, domain=None, range=Optional[str])

slots.dokumentfil__format = Slot(uri=ARK.format, name="dokumentfil__format", curie=ARK.curie('format'),
                   model_uri=ARK.dokumentfil__format, domain=None, range=str)

slots.journalpost__antallVedlegg = Slot(uri=ARK.antallVedlegg, name="journalpost__antallVedlegg", curie=ARK.curie('antallVedlegg'),
                   model_uri=ARK.journalpost__antallVedlegg, domain=None, range=Optional[int])

slots.journalpost__avskrivning = Slot(uri=ARK.avskrivning, name="journalpost__avskrivning", curie=ARK.curie('avskrivning'),
                   model_uri=ARK.journalpost__avskrivning, domain=None, range=Optional[Union[dict, Avskrivning]])

slots.journalpost__dokumentetsDato = Slot(uri=ARK.dokumentetsDato, name="journalpost__dokumentetsDato", curie=ARK.curie('dokumentetsDato'),
                   model_uri=ARK.journalpost__dokumentetsDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.journalpost__forfallsDato = Slot(uri=ARK.forfallsDato, name="journalpost__forfallsDato", curie=ARK.curie('forfallsDato'),
                   model_uri=ARK.journalpost__forfallsDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.journalpost__journalAr = Slot(uri=ARK.journalAr, name="journalpost__journalAr", curie=ARK.curie('journalAr'),
                   model_uri=ARK.journalpost__journalAr, domain=None, range=Optional[str])

slots.journalpost__journalDato = Slot(uri=ARK.journalDato, name="journalpost__journalDato", curie=ARK.curie('journalDato'),
                   model_uri=ARK.journalpost__journalDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.journalpost__journalPostnummer = Slot(uri=ARK.journalPostnummer, name="journalpost__journalPostnummer", curie=ARK.curie('journalPostnummer'),
                   model_uri=ARK.journalpost__journalPostnummer, domain=None, range=Optional[int])

slots.journalpost__journalSekvensnummer = Slot(uri=ARK.journalSekvensnummer, name="journalpost__journalSekvensnummer", curie=ARK.curie('journalSekvensnummer'),
                   model_uri=ARK.journalpost__journalSekvensnummer, domain=None, range=Optional[int])

slots.journalpost__mottattDato = Slot(uri=ARK.mottattDato, name="journalpost__mottattDato", curie=ARK.curie('mottattDato'),
                   model_uri=ARK.journalpost__mottattDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.journalpost__offentlighetsvurdertDato = Slot(uri=ARK.offentlighetsvurdertDato, name="journalpost__offentlighetsvurdertDato", curie=ARK.curie('offentlighetsvurdertDato'),
                   model_uri=ARK.journalpost__offentlighetsvurdertDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.journalpost__sendtDato = Slot(uri=ARK.sendtDato, name="journalpost__sendtDato", curie=ARK.curie('sendtDato'),
                   model_uri=ARK.journalpost__sendtDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.journalpost__journalposttype = Slot(uri=ARK.journalposttype, name="journalpost__journalposttype", curie=ARK.curie('journalposttype'),
                   model_uri=ARK.journalpost__journalposttype, domain=None, range=Union[str, JournalpostTypeId])

slots.journalpost__journalstatus = Slot(uri=ARK.journalstatus, name="journalpost__journalstatus", curie=ARK.curie('journalstatus'),
                   model_uri=ARK.journalpost__journalstatus, domain=None, range=Union[str, JournalStatusId])

slots.journalpost__journalenhet = Slot(uri=ARK.journalenhet, name="journalpost__journalenhet", curie=ARK.curie('journalenhet'),
                   model_uri=ARK.journalpost__journalenhet, domain=None, range=Optional[Union[str, AdministrativEnhetId]])

slots.klassifikasjonssystem__avsluttetAv = Slot(uri=ARK.avsluttetAvNavn, name="klassifikasjonssystem__avsluttetAv", curie=ARK.curie('avsluttetAvNavn'),
                   model_uri=ARK.klassifikasjonssystem__avsluttetAv, domain=None, range=Optional[str])

slots.klassifikasjonssystem__avsluttetDato = Slot(uri=ARK.avsluttetDato, name="klassifikasjonssystem__avsluttetDato", curie=ARK.curie('avsluttetDato'),
                   model_uri=ARK.klassifikasjonssystem__avsluttetDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.klassifikasjonssystem__beskrivelse = Slot(uri=ARK.beskrivelse, name="klassifikasjonssystem__beskrivelse", curie=ARK.curie('beskrivelse'),
                   model_uri=ARK.klassifikasjonssystem__beskrivelse, domain=None, range=Optional[str])

slots.klassifikasjonssystem__klasse = Slot(uri=ARK.klasse, name="klassifikasjonssystem__klasse", curie=ARK.curie('klasse'),
                   model_uri=ARK.klassifikasjonssystem__klasse, domain=None, range=Union[Union[dict, Klasse], list[Union[dict, Klasse]]])

slots.klassifikasjonssystem__opprettetAv = Slot(uri=ARK.opprettetAvNavn, name="klassifikasjonssystem__opprettetAv", curie=ARK.curie('opprettetAvNavn'),
                   model_uri=ARK.klassifikasjonssystem__opprettetAv, domain=None, range=str)

slots.klassifikasjonssystem__opprettetDato = Slot(uri=ARK.opprettetDato, name="klassifikasjonssystem__opprettetDato", curie=ARK.curie('opprettetDato'),
                   model_uri=ARK.klassifikasjonssystem__opprettetDato, domain=None, range=Union[str, XSDDateTime])

slots.klassifikasjonssystem__tittel = Slot(uri=ARK.tittel, name="klassifikasjonssystem__tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.klassifikasjonssystem__tittel, domain=None, range=str)

slots.klassifikasjonssystem__klassifikasjonstype = Slot(uri=ARK.klassifikasjonstype, name="klassifikasjonssystem__klassifikasjonstype", curie=ARK.curie('klassifikasjonstype'),
                   model_uri=ARK.klassifikasjonssystem__klassifikasjonstype, domain=None, range=Optional[Union[str, KlassifikasjonstypeId]])

slots.klassifikasjonssystem__arkivdel = Slot(uri=ARK.arkivdel, name="klassifikasjonssystem__arkivdel", curie=ARK.curie('arkivdel'),
                   model_uri=ARK.klassifikasjonssystem__arkivdel, domain=None, range=Union[Union[str, ArkivdelId], list[Union[str, ArkivdelId]]])

slots.tilgang__tittel = Slot(uri=ARK.tittel, name="tilgang__tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.tilgang__tittel, domain=None, range=str)

slots.tilgang__rolle = Slot(uri=ARK.rolle, name="tilgang__rolle", curie=ARK.curie('rolle'),
                   model_uri=ARK.tilgang__rolle, domain=None, range=Union[str, RolleId])

slots.tilgang__administrativEnhet = Slot(uri=ARK.administrativEnhet, name="tilgang__administrativEnhet", curie=ARK.curie('administrativEnhet'),
                   model_uri=ARK.tilgang__administrativEnhet, domain=None, range=Optional[Union[str, AdministrativEnhetId]])

slots.tilgang__arkivdel = Slot(uri=ARK.arkivdel, name="tilgang__arkivdel", curie=ARK.curie('arkivdel'),
                   model_uri=ARK.tilgang__arkivdel, domain=None, range=Optional[Union[str, ArkivdelId]])

slots.tilgang__arkivressurs = Slot(uri=ARK.arkivressurs, name="tilgang__arkivressurs", curie=ARK.curie('arkivressurs'),
                   model_uri=ARK.tilgang__arkivressurs, domain=None, range=Optional[Union[Union[str, ArkivressursId], list[Union[str, ArkivressursId]]]])

slots.personalmappe__navn = Slot(uri=ARK.navn, name="personalmappe__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.personalmappe__navn, domain=None, range=Union[dict, Personnavn])

slots.personalmappe__person = Slot(uri=ARK.person, name="personalmappe__person", curie=ARK.curie('person'),
                   model_uri=ARK.personalmappe__person, domain=None, range=Union[str, URIorCURIE])

slots.personalmappe__leder = Slot(uri=ARK.leder, name="personalmappe__leder", curie=ARK.curie('leder'),
                   model_uri=ARK.personalmappe__leder, domain=None, range=Union[str, URIorCURIE])

slots.personalmappe__arbeidssted = Slot(uri=ARK.arbeidssted, name="personalmappe__arbeidssted", curie=ARK.curie('arbeidssted'),
                   model_uri=ARK.personalmappe__arbeidssted, domain=None, range=Union[str, URIorCURIE])

slots.personalmappe__personalressurs = Slot(uri=ARK.personalressurs, name="personalmappe__personalressurs", curie=ARK.curie('personalressurs'),
                   model_uri=ARK.personalmappe__personalressurs, domain=None, range=Union[str, URIorCURIE])

slots.dispensasjonAutomatiskFredaKulturminne__kulturminneId = Slot(uri=ARK.kulturminneId, name="dispensasjonAutomatiskFredaKulturminne__kulturminneId", curie=ARK.curie('kulturminneId'),
                   model_uri=ARK.dispensasjonAutomatiskFredaKulturminne__kulturminneId, domain=None, range=str)

slots.dispensasjonAutomatiskFredaKulturminne__matrikkelnummer = Slot(uri=ARK.matrikkelnummer, name="dispensasjonAutomatiskFredaKulturminne__matrikkelnummer", curie=ARK.curie('matrikkelnummer'),
                   model_uri=ARK.dispensasjonAutomatiskFredaKulturminne__matrikkelnummer, domain=None, range=Union[dict, Matrikkelnummer])

slots.dispensasjonAutomatiskFredaKulturminne__soeknadsnummer = Slot(uri=ARK.soeknadsnummer, name="dispensasjonAutomatiskFredaKulturminne__soeknadsnummer", curie=ARK.curie('soeknadsnummer'),
                   model_uri=ARK.dispensasjonAutomatiskFredaKulturminne__soeknadsnummer, domain=None, range=Union[dict, Identifikator])

slots.dispensasjonAutomatiskFredaKulturminne__tiltak = Slot(uri=ARK.tiltak, name="dispensasjonAutomatiskFredaKulturminne__tiltak", curie=ARK.curie('tiltak'),
                   model_uri=ARK.dispensasjonAutomatiskFredaKulturminne__tiltak, domain=None, range=Optional[str])

slots.tilskuddFartoy__fartoyNavn = Slot(uri=ARK.fartoyNavn, name="tilskuddFartoy__fartoyNavn", curie=ARK.curie('fartoyNavn'),
                   model_uri=ARK.tilskuddFartoy__fartoyNavn, domain=None, range=str)

slots.tilskuddFartoy__kallesignal = Slot(uri=ARK.kallesignal, name="tilskuddFartoy__kallesignal", curie=ARK.curie('kallesignal'),
                   model_uri=ARK.tilskuddFartoy__kallesignal, domain=None, range=str)

slots.tilskuddFartoy__kulturminneId = Slot(uri=ARK.kulturminneId, name="tilskuddFartoy__kulturminneId", curie=ARK.curie('kulturminneId'),
                   model_uri=ARK.tilskuddFartoy__kulturminneId, domain=None, range=str)

slots.tilskuddFartoy__soeknadsnummer = Slot(uri=ARK.soeknadsnummer, name="tilskuddFartoy__soeknadsnummer", curie=ARK.curie('soeknadsnummer'),
                   model_uri=ARK.tilskuddFartoy__soeknadsnummer, domain=None, range=Union[dict, Identifikator])

slots.tilskuddFredaBygningPrivatEie__bygningsnavn = Slot(uri=ARK.bygningsnavn, name="tilskuddFredaBygningPrivatEie__bygningsnavn", curie=ARK.curie('bygningsnavn'),
                   model_uri=ARK.tilskuddFredaBygningPrivatEie__bygningsnavn, domain=None, range=Optional[str])

slots.tilskuddFredaBygningPrivatEie__kulturminneId = Slot(uri=ARK.kulturminneId, name="tilskuddFredaBygningPrivatEie__kulturminneId", curie=ARK.curie('kulturminneId'),
                   model_uri=ARK.tilskuddFredaBygningPrivatEie__kulturminneId, domain=None, range=str)

slots.tilskuddFredaBygningPrivatEie__matrikkelnummer = Slot(uri=ARK.matrikkelnummer, name="tilskuddFredaBygningPrivatEie__matrikkelnummer", curie=ARK.curie('matrikkelnummer'),
                   model_uri=ARK.tilskuddFredaBygningPrivatEie__matrikkelnummer, domain=None, range=Optional[Union[dict, Matrikkelnummer]])

slots.tilskuddFredaBygningPrivatEie__soeknadsnummer = Slot(uri=ARK.soeknadsnummer, name="tilskuddFredaBygningPrivatEie__soeknadsnummer", curie=ARK.curie('soeknadsnummer'),
                   model_uri=ARK.tilskuddFredaBygningPrivatEie__soeknadsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.soeknadDrosjeloeyve__organisasjonsnavn = Slot(uri=ARK.organisasjonsnavn, name="soeknadDrosjeloeyve__organisasjonsnavn", curie=ARK.curie('organisasjonsnavn'),
                   model_uri=ARK.soeknadDrosjeloeyve__organisasjonsnavn, domain=None, range=str)

slots.soeknadDrosjeloeyve__organisasjonsnummer = Slot(uri=ARK.organisasjonsnummer, name="soeknadDrosjeloeyve__organisasjonsnummer", curie=ARK.curie('organisasjonsnummer'),
                   model_uri=ARK.soeknadDrosjeloeyve__organisasjonsnummer, domain=None, range=str)

slots.avskrivning__avskrevetAv = Slot(uri=ARK.avskrevetAv, name="avskrivning__avskrevetAv", curie=ARK.curie('avskrevetAv'),
                   model_uri=ARK.avskrivning__avskrevetAv, domain=None, range=str)

slots.avskrivning__avskrivningsdato = Slot(uri=ARK.avskrivningsdato, name="avskrivning__avskrivningsdato", curie=ARK.curie('avskrivningsdato'),
                   model_uri=ARK.avskrivning__avskrivningsdato, domain=None, range=Union[str, XSDDateTime])

slots.avskrivning__avskrivningsmate = Slot(uri=ARK.avskrivningsmate, name="avskrivning__avskrivningsmate", curie=ARK.curie('avskrivningsmate'),
                   model_uri=ARK.avskrivning__avskrivningsmate, domain=None, range=str)

slots.dokumentbeskrivelse__beskrivelse = Slot(uri=ARK.beskrivelse, name="dokumentbeskrivelse__beskrivelse", curie=ARK.curie('beskrivelse'),
                   model_uri=ARK.dokumentbeskrivelse__beskrivelse, domain=None, range=Optional[str])

slots.dokumentbeskrivelse__dokumentnummer = Slot(uri=ARK.dokumentnummer, name="dokumentbeskrivelse__dokumentnummer", curie=ARK.curie('dokumentnummer'),
                   model_uri=ARK.dokumentbeskrivelse__dokumentnummer, domain=None, range=Optional[int])

slots.dokumentbeskrivelse__dokumentobjekt = Slot(uri=ARK.dokumentobjekt, name="dokumentbeskrivelse__dokumentobjekt", curie=ARK.curie('dokumentobjekt'),
                   model_uri=ARK.dokumentbeskrivelse__dokumentobjekt, domain=None, range=Optional[Union[Union[dict, Dokumentobjekt], list[Union[dict, Dokumentobjekt]]]])

slots.dokumentbeskrivelse__forfatter = Slot(uri=ARK.forfatter, name="dokumentbeskrivelse__forfatter", curie=ARK.curie('forfatter'),
                   model_uri=ARK.dokumentbeskrivelse__forfatter, domain=None, range=Optional[Union[str, list[str]]])

slots.dokumentbeskrivelse__opprettetDato = Slot(uri=ARK.opprettetDato, name="dokumentbeskrivelse__opprettetDato", curie=ARK.curie('opprettetDato'),
                   model_uri=ARK.dokumentbeskrivelse__opprettetDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.dokumentbeskrivelse__part = Slot(uri=ARK.part, name="dokumentbeskrivelse__part", curie=ARK.curie('part'),
                   model_uri=ARK.dokumentbeskrivelse__part, domain=None, range=Optional[Union[Union[dict, Part], list[Union[dict, Part]]]])

slots.dokumentbeskrivelse__referanseArkivdel = Slot(uri=ARK.referanseArkivdel, name="dokumentbeskrivelse__referanseArkivdel", curie=ARK.curie('referanseArkivdel'),
                   model_uri=ARK.dokumentbeskrivelse__referanseArkivdel, domain=None, range=Optional[Union[str, list[str]]])

slots.dokumentbeskrivelse__skjerming = Slot(uri=ARK.skjerming, name="dokumentbeskrivelse__skjerming", curie=ARK.curie('skjerming'),
                   model_uri=ARK.dokumentbeskrivelse__skjerming, domain=None, range=Optional[Union[dict, Skjerming]])

slots.dokumentbeskrivelse__tilknyttetDato = Slot(uri=ARK.tilknyttetDato, name="dokumentbeskrivelse__tilknyttetDato", curie=ARK.curie('tilknyttetDato'),
                   model_uri=ARK.dokumentbeskrivelse__tilknyttetDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.dokumentbeskrivelse__tittel = Slot(uri=ARK.tittel, name="dokumentbeskrivelse__tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.dokumentbeskrivelse__tittel, domain=None, range=str)

slots.dokumentbeskrivelse__dokumentstatus = Slot(uri=ARK.dokumentstatus, name="dokumentbeskrivelse__dokumentstatus", curie=ARK.curie('dokumentstatus'),
                   model_uri=ARK.dokumentbeskrivelse__dokumentstatus, domain=None, range=Union[str, DokumentStatusId])

slots.dokumentbeskrivelse__dokumentType = Slot(uri=ARK.dokumentType, name="dokumentbeskrivelse__dokumentType", curie=ARK.curie('dokumentType'),
                   model_uri=ARK.dokumentbeskrivelse__dokumentType, domain=None, range=Union[str, DokumentTypeId])

slots.dokumentbeskrivelse__tilknyttetRegistreringSom = Slot(uri=ARK.tilknyttetRegistreringSom, name="dokumentbeskrivelse__tilknyttetRegistreringSom", curie=ARK.curie('tilknyttetRegistreringSom'),
                   model_uri=ARK.dokumentbeskrivelse__tilknyttetRegistreringSom, domain=None, range=Union[Union[str, TilknyttetRegistreringSomId], list[Union[str, TilknyttetRegistreringSomId]]])

slots.dokumentbeskrivelse__tilknyttetAv = Slot(uri=ARK.tilknyttetAv, name="dokumentbeskrivelse__tilknyttetAv", curie=ARK.curie('tilknyttetAv'),
                   model_uri=ARK.dokumentbeskrivelse__tilknyttetAv, domain=None, range=Union[str, ArkivressursId])

slots.dokumentbeskrivelse__opprettetAv = Slot(uri=ARK.opprettetAv, name="dokumentbeskrivelse__opprettetAv", curie=ARK.curie('opprettetAv'),
                   model_uri=ARK.dokumentbeskrivelse__opprettetAv, domain=None, range=Union[str, ArkivressursId])

slots.dokumentobjekt__filstorrelse = Slot(uri=ARK.filstorrelse, name="dokumentobjekt__filstorrelse", curie=ARK.curie('filstorrelse'),
                   model_uri=ARK.dokumentobjekt__filstorrelse, domain=None, range=Optional[str])

slots.dokumentobjekt__formatDetaljer = Slot(uri=ARK.formatDetaljer, name="dokumentobjekt__formatDetaljer", curie=ARK.curie('formatDetaljer'),
                   model_uri=ARK.dokumentobjekt__formatDetaljer, domain=None, range=Optional[str])

slots.dokumentobjekt__sjekksum = Slot(uri=ARK.sjekksum, name="dokumentobjekt__sjekksum", curie=ARK.curie('sjekksum'),
                   model_uri=ARK.dokumentobjekt__sjekksum, domain=None, range=Optional[str])

slots.dokumentobjekt__sjekksumAlgoritme = Slot(uri=ARK.sjekksumAlgoritme, name="dokumentobjekt__sjekksumAlgoritme", curie=ARK.curie('sjekksumAlgoritme'),
                   model_uri=ARK.dokumentobjekt__sjekksumAlgoritme, domain=None, range=Optional[str])

slots.dokumentobjekt__versjonsnummer = Slot(uri=ARK.versjonsnummer, name="dokumentobjekt__versjonsnummer", curie=ARK.curie('versjonsnummer'),
                   model_uri=ARK.dokumentobjekt__versjonsnummer, domain=None, range=Optional[int])

slots.dokumentobjekt__filformat = Slot(uri=ARK.filformat, name="dokumentobjekt__filformat", curie=ARK.curie('filformat'),
                   model_uri=ARK.dokumentobjekt__filformat, domain=None, range=Optional[Union[str, FormatId]])

slots.dokumentobjekt__variantFormat = Slot(uri=ARK.variantFormat, name="dokumentobjekt__variantFormat", curie=ARK.curie('variantFormat'),
                   model_uri=ARK.dokumentobjekt__variantFormat, domain=None, range=Union[str, VariantformatId])

slots.dokumentobjekt__opprettetAv = Slot(uri=ARK.opprettetAv, name="dokumentobjekt__opprettetAv", curie=ARK.curie('opprettetAv'),
                   model_uri=ARK.dokumentobjekt__opprettetAv, domain=None, range=Union[str, ArkivressursId])

slots.dokumentobjekt__referanseDokumentfil = Slot(uri=ARK.referanseDokumentfil, name="dokumentobjekt__referanseDokumentfil", curie=ARK.curie('referanseDokumentfil'),
                   model_uri=ARK.dokumentobjekt__referanseDokumentfil, domain=None, range=Optional[Union[str, DokumentfilId]])

slots.klasse__klasseId = Slot(uri=ARK.klasseId, name="klasse__klasseId", curie=ARK.curie('klasseId'),
                   model_uri=ARK.klasse__klasseId, domain=None, range=str)

slots.klasse__rekkefølge = Slot(uri=ARK.rekkefolge, name="klasse__rekkefølge", curie=ARK.curie('rekkefolge'),
                   model_uri=ARK.klasse__rekkefølge, domain=None, range=Optional[int])

slots.klasse__skjerming = Slot(uri=ARK.skjerming, name="klasse__skjerming", curie=ARK.curie('skjerming'),
                   model_uri=ARK.klasse__skjerming, domain=None, range=Optional[Union[dict, Skjerming]])

slots.klasse__tittel = Slot(uri=ARK.tittel, name="klasse__tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.klasse__tittel, domain=None, range=str)

slots.klasse__klassifikasjonssystem = Slot(uri=ARK.klassifikasjonssystem, name="klasse__klassifikasjonssystem", curie=ARK.curie('klassifikasjonssystem'),
                   model_uri=ARK.klasse__klassifikasjonssystem, domain=None, range=Union[str, KlassifikasjonssystemId])

slots.korrespondansepart__adresse = Slot(uri=ARK.adresse, name="korrespondansepart__adresse", curie=ARK.curie('adresse'),
                   model_uri=ARK.korrespondansepart__adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.korrespondansepart__foedselsnummer = Slot(uri=ARK.foedselsnummer, name="korrespondansepart__foedselsnummer", curie=ARK.curie('foedselsnummer'),
                   model_uri=ARK.korrespondansepart__foedselsnummer, domain=None, range=Optional[str])

slots.korrespondansepart__kontaktinformasjon = Slot(uri=ARK.kontaktinformasjon, name="korrespondansepart__kontaktinformasjon", curie=ARK.curie('kontaktinformasjon'),
                   model_uri=ARK.korrespondansepart__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.korrespondansepart__kontaktperson = Slot(uri=ARK.kontaktperson, name="korrespondansepart__kontaktperson", curie=ARK.curie('kontaktperson'),
                   model_uri=ARK.korrespondansepart__kontaktperson, domain=None, range=Optional[str])

slots.korrespondansepart__korrespondansepartNavn = Slot(uri=ARK.korrespondansepartNavn, name="korrespondansepart__korrespondansepartNavn", curie=ARK.curie('korrespondansepartNavn'),
                   model_uri=ARK.korrespondansepart__korrespondansepartNavn, domain=None, range=Optional[str])

slots.korrespondansepart__organisasjonsnummer = Slot(uri=ARK.organisasjonsnummer, name="korrespondansepart__organisasjonsnummer", curie=ARK.curie('organisasjonsnummer'),
                   model_uri=ARK.korrespondansepart__organisasjonsnummer, domain=None, range=Optional[str])

slots.korrespondansepart__skjerming = Slot(uri=ARK.skjerming, name="korrespondansepart__skjerming", curie=ARK.curie('skjerming'),
                   model_uri=ARK.korrespondansepart__skjerming, domain=None, range=Optional[Union[dict, Skjerming]])

slots.korrespondansepart__korrespondanseparttype = Slot(uri=ARK.korrespondanseparttype, name="korrespondansepart__korrespondanseparttype", curie=ARK.curie('korrespondanseparttype'),
                   model_uri=ARK.korrespondansepart__korrespondanseparttype, domain=None, range=Union[str, KorrespondansepartTypeId])

slots.merknad__merknadsdato = Slot(uri=ARK.merknadsdato, name="merknad__merknadsdato", curie=ARK.curie('merknadsdato'),
                   model_uri=ARK.merknad__merknadsdato, domain=None, range=Union[str, XSDDateTime])

slots.merknad__merknadstekst = Slot(uri=ARK.merknadstekst, name="merknad__merknadstekst", curie=ARK.curie('merknadstekst'),
                   model_uri=ARK.merknad__merknadstekst, domain=None, range=str)

slots.merknad__merknadstype = Slot(uri=ARK.merknadstype, name="merknad__merknadstype", curie=ARK.curie('merknadstype'),
                   model_uri=ARK.merknad__merknadstype, domain=None, range=Union[str, MerknadstypeId])

slots.merknad__merknadRegistrertAv = Slot(uri=ARK.merknadRegistrertAv, name="merknad__merknadRegistrertAv", curie=ARK.curie('merknadRegistrertAv'),
                   model_uri=ARK.merknad__merknadRegistrertAv, domain=None, range=Union[str, ArkivressursId])

slots.part__adresse = Slot(uri=ARK.adresse, name="part__adresse", curie=ARK.curie('adresse'),
                   model_uri=ARK.part__adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.part__foedselsnummer = Slot(uri=ARK.foedselsnummer, name="part__foedselsnummer", curie=ARK.curie('foedselsnummer'),
                   model_uri=ARK.part__foedselsnummer, domain=None, range=Optional[str])

slots.part__kontaktinformasjon = Slot(uri=ARK.kontaktinformasjon, name="part__kontaktinformasjon", curie=ARK.curie('kontaktinformasjon'),
                   model_uri=ARK.part__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.part__kontaktperson = Slot(uri=ARK.kontaktperson, name="part__kontaktperson", curie=ARK.curie('kontaktperson'),
                   model_uri=ARK.part__kontaktperson, domain=None, range=Optional[str])

slots.part__organisasjonsnummer = Slot(uri=ARK.organisasjonsnummer, name="part__organisasjonsnummer", curie=ARK.curie('organisasjonsnummer'),
                   model_uri=ARK.part__organisasjonsnummer, domain=None, range=Optional[str])

slots.part__partNavn = Slot(uri=ARK.partNavn, name="part__partNavn", curie=ARK.curie('partNavn'),
                   model_uri=ARK.part__partNavn, domain=None, range=str)

slots.part__partRolle = Slot(uri=ARK.partRolle, name="part__partRolle", curie=ARK.curie('partRolle'),
                   model_uri=ARK.part__partRolle, domain=None, range=Optional[Union[str, PartRolleId]])

slots.skjerming__skjermingshjemmel = Slot(uri=ARK.skjermingshjemmel, name="skjerming__skjermingshjemmel", curie=ARK.curie('skjermingshjemmel'),
                   model_uri=ARK.skjerming__skjermingshjemmel, domain=None, range=Union[str, SkjermingshjemmelId])

slots.skjerming__tilgangsrestriksjon = Slot(uri=ARK.tilgangsrestriksjon, name="skjerming__tilgangsrestriksjon", curie=ARK.curie('tilgangsrestriksjon'),
                   model_uri=ARK.skjerming__tilgangsrestriksjon, domain=None, range=Union[str, TilgangsrestriksjonId])

slots.dokumentStatus__kode = Slot(uri=ARK.kode, name="dokumentStatus__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.dokumentStatus__kode, domain=None, range=str)

slots.dokumentStatus__navn = Slot(uri=ARK.navn, name="dokumentStatus__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.dokumentStatus__navn, domain=None, range=str)

slots.dokumentStatus__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="dokumentStatus__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.dokumentStatus__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.dokumentStatus__passiv = Slot(uri=ARK.passiv, name="dokumentStatus__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.dokumentStatus__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.dokumentType__kode = Slot(uri=ARK.kode, name="dokumentType__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.dokumentType__kode, domain=None, range=str)

slots.dokumentType__navn = Slot(uri=ARK.navn, name="dokumentType__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.dokumentType__navn, domain=None, range=str)

slots.dokumentType__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="dokumentType__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.dokumentType__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.dokumentType__passiv = Slot(uri=ARK.passiv, name="dokumentType__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.dokumentType__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.format__kode = Slot(uri=ARK.kode, name="format__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.format__kode, domain=None, range=str)

slots.format__navn = Slot(uri=ARK.navn, name="format__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.format__navn, domain=None, range=str)

slots.format__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="format__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.format__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.format__passiv = Slot(uri=ARK.passiv, name="format__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.format__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.journalpostType__kode = Slot(uri=ARK.kode, name="journalpostType__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.journalpostType__kode, domain=None, range=str)

slots.journalpostType__navn = Slot(uri=ARK.navn, name="journalpostType__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.journalpostType__navn, domain=None, range=str)

slots.journalpostType__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="journalpostType__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.journalpostType__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.journalpostType__passiv = Slot(uri=ARK.passiv, name="journalpostType__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.journalpostType__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.journalStatus__kode = Slot(uri=ARK.kode, name="journalStatus__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.journalStatus__kode, domain=None, range=str)

slots.journalStatus__navn = Slot(uri=ARK.navn, name="journalStatus__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.journalStatus__navn, domain=None, range=str)

slots.journalStatus__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="journalStatus__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.journalStatus__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.journalStatus__passiv = Slot(uri=ARK.passiv, name="journalStatus__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.journalStatus__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.klassifikasjonstype__kode = Slot(uri=ARK.kode, name="klassifikasjonstype__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.klassifikasjonstype__kode, domain=None, range=str)

slots.klassifikasjonstype__navn = Slot(uri=ARK.navn, name="klassifikasjonstype__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.klassifikasjonstype__navn, domain=None, range=str)

slots.klassifikasjonstype__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="klassifikasjonstype__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.klassifikasjonstype__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.klassifikasjonstype__passiv = Slot(uri=ARK.passiv, name="klassifikasjonstype__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.klassifikasjonstype__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.korrespondansepartType__kode = Slot(uri=ARK.kode, name="korrespondansepartType__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.korrespondansepartType__kode, domain=None, range=str)

slots.korrespondansepartType__navn = Slot(uri=ARK.navn, name="korrespondansepartType__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.korrespondansepartType__navn, domain=None, range=str)

slots.korrespondansepartType__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="korrespondansepartType__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.korrespondansepartType__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.korrespondansepartType__passiv = Slot(uri=ARK.passiv, name="korrespondansepartType__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.korrespondansepartType__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.merknadstype__kode = Slot(uri=ARK.kode, name="merknadstype__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.merknadstype__kode, domain=None, range=str)

slots.merknadstype__navn = Slot(uri=ARK.navn, name="merknadstype__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.merknadstype__navn, domain=None, range=str)

slots.merknadstype__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="merknadstype__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.merknadstype__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.merknadstype__passiv = Slot(uri=ARK.passiv, name="merknadstype__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.merknadstype__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.partRolle__kode = Slot(uri=ARK.kode, name="partRolle__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.partRolle__kode, domain=None, range=str)

slots.partRolle__navn = Slot(uri=ARK.navn, name="partRolle__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.partRolle__navn, domain=None, range=str)

slots.partRolle__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="partRolle__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.partRolle__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.partRolle__passiv = Slot(uri=ARK.passiv, name="partRolle__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.partRolle__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.rolle__kode = Slot(uri=ARK.kode, name="rolle__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.rolle__kode, domain=None, range=str)

slots.rolle__navn = Slot(uri=ARK.navn, name="rolle__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.rolle__navn, domain=None, range=str)

slots.rolle__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="rolle__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.rolle__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.rolle__passiv = Slot(uri=ARK.passiv, name="rolle__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.rolle__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.saksmappetype__kode = Slot(uri=ARK.kode, name="saksmappetype__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.saksmappetype__kode, domain=None, range=str)

slots.saksmappetype__navn = Slot(uri=ARK.navn, name="saksmappetype__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.saksmappetype__navn, domain=None, range=str)

slots.saksmappetype__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="saksmappetype__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.saksmappetype__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.saksmappetype__passiv = Slot(uri=ARK.passiv, name="saksmappetype__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.saksmappetype__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.saksstatus__kode = Slot(uri=ARK.kode, name="saksstatus__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.saksstatus__kode, domain=None, range=str)

slots.saksstatus__navn = Slot(uri=ARK.navn, name="saksstatus__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.saksstatus__navn, domain=None, range=str)

slots.saksstatus__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="saksstatus__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.saksstatus__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.saksstatus__passiv = Slot(uri=ARK.passiv, name="saksstatus__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.saksstatus__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.skjermingshjemmel__kode = Slot(uri=ARK.kode, name="skjermingshjemmel__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.skjermingshjemmel__kode, domain=None, range=str)

slots.skjermingshjemmel__navn = Slot(uri=ARK.navn, name="skjermingshjemmel__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.skjermingshjemmel__navn, domain=None, range=str)

slots.skjermingshjemmel__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="skjermingshjemmel__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.skjermingshjemmel__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.skjermingshjemmel__passiv = Slot(uri=ARK.passiv, name="skjermingshjemmel__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.skjermingshjemmel__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.tilgangsgruppe__kode = Slot(uri=ARK.kode, name="tilgangsgruppe__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.tilgangsgruppe__kode, domain=None, range=str)

slots.tilgangsgruppe__navn = Slot(uri=ARK.navn, name="tilgangsgruppe__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.tilgangsgruppe__navn, domain=None, range=str)

slots.tilgangsgruppe__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="tilgangsgruppe__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.tilgangsgruppe__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.tilgangsgruppe__passiv = Slot(uri=ARK.passiv, name="tilgangsgruppe__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.tilgangsgruppe__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.tilgangsrestriksjon__kode = Slot(uri=ARK.kode, name="tilgangsrestriksjon__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.tilgangsrestriksjon__kode, domain=None, range=str)

slots.tilgangsrestriksjon__navn = Slot(uri=ARK.navn, name="tilgangsrestriksjon__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.tilgangsrestriksjon__navn, domain=None, range=str)

slots.tilgangsrestriksjon__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="tilgangsrestriksjon__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.tilgangsrestriksjon__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.tilgangsrestriksjon__passiv = Slot(uri=ARK.passiv, name="tilgangsrestriksjon__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.tilgangsrestriksjon__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.tilknyttetRegistreringSom__kode = Slot(uri=ARK.kode, name="tilknyttetRegistreringSom__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.tilknyttetRegistreringSom__kode, domain=None, range=str)

slots.tilknyttetRegistreringSom__navn = Slot(uri=ARK.navn, name="tilknyttetRegistreringSom__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.tilknyttetRegistreringSom__navn, domain=None, range=str)

slots.tilknyttetRegistreringSom__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="tilknyttetRegistreringSom__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.tilknyttetRegistreringSom__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.tilknyttetRegistreringSom__passiv = Slot(uri=ARK.passiv, name="tilknyttetRegistreringSom__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.tilknyttetRegistreringSom__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.variantformat__kode = Slot(uri=ARK.kode, name="variantformat__kode", curie=ARK.curie('kode'),
                   model_uri=ARK.variantformat__kode, domain=None, range=str)

slots.variantformat__navn = Slot(uri=ARK.navn, name="variantformat__navn", curie=ARK.curie('navn'),
                   model_uri=ARK.variantformat__navn, domain=None, range=str)

slots.variantformat__gyldighetsperiode = Slot(uri=ARK.gyldighetsperiode, name="variantformat__gyldighetsperiode", curie=ARK.curie('gyldighetsperiode'),
                   model_uri=ARK.variantformat__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.variantformat__passiv = Slot(uri=ARK.passiv, name="variantformat__passiv", curie=ARK.curie('passiv'),
                   model_uri=ARK.variantformat__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.aktoer__kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="aktoer__kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ARK.aktoer__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.aktoer__postadresse = Slot(uri=FINT.postadresse, name="aktoer__postadresse", curie=FINT.curie('postadresse'),
                   model_uri=ARK.aktoer__postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.begrep__kode = Slot(uri=FINT.kode, name="begrep__kode", curie=FINT.curie('kode'),
                   model_uri=ARK.begrep__kode, domain=None, range=str)

slots.begrep__navn = Slot(uri=FINT.navn, name="begrep__navn", curie=FINT.curie('navn'),
                   model_uri=ARK.begrep__navn, domain=None, range=str)

slots.begrep__gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="begrep__gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.begrep__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.begrep__passiv = Slot(uri=FINT.passiv, name="begrep__passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.begrep__passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.enhet__forretningsadresse = Slot(uri=FINT.forretningsadresse, name="enhet__forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=ARK.enhet__forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.enhet__organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="enhet__organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=ARK.enhet__organisasjonsnavn, domain=None, range=Optional[str])

slots.enhet__organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="enhet__organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=ARK.enhet__organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.identifikator__identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="identifikator__identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=ARK.identifikator__identifikatorverdi, domain=None, range=str)

slots.identifikator__gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="identifikator__gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.identifikator__gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.periode__beskrivelse = Slot(uri=FINT.beskrivelse, name="periode__beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=ARK.periode__beskrivelse, domain=None, range=Optional[str])

slots.periode__start = Slot(uri=FINT.start, name="periode__start", curie=FINT.curie('start'),
                   model_uri=ARK.periode__start, domain=None, range=Union[str, XSDDateTime])

slots.periode__slutt = Slot(uri=FINT.slutt, name="periode__slutt", curie=FINT.curie('slutt'),
                   model_uri=ARK.periode__slutt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.personnavn__fornavn = Slot(uri=FINT.fornavn, name="personnavn__fornavn", curie=FINT.curie('fornavn'),
                   model_uri=ARK.personnavn__fornavn, domain=None, range=str)

slots.personnavn__mellomnavn = Slot(uri=FINT.mellomnavn, name="personnavn__mellomnavn", curie=FINT.curie('mellomnavn'),
                   model_uri=ARK.personnavn__mellomnavn, domain=None, range=Optional[str])

slots.personnavn__etternavn = Slot(uri=FINT.etternavn, name="personnavn__etternavn", curie=FINT.curie('etternavn'),
                   model_uri=ARK.personnavn__etternavn, domain=None, range=str)

slots.kontaktinformasjon__epostadresse = Slot(uri=FINT.epostadresse, name="kontaktinformasjon__epostadresse", curie=FINT.curie('epostadresse'),
                   model_uri=ARK.kontaktinformasjon__epostadresse, domain=None, range=Optional[str])

slots.kontaktinformasjon__mobiltelefonnummer = Slot(uri=FINT.mobiltelefonnummer, name="kontaktinformasjon__mobiltelefonnummer", curie=FINT.curie('mobiltelefonnummer'),
                   model_uri=ARK.kontaktinformasjon__mobiltelefonnummer, domain=None, range=Optional[str])

slots.kontaktinformasjon__nettsted = Slot(uri=FINT.nettsted, name="kontaktinformasjon__nettsted", curie=FINT.curie('nettsted'),
                   model_uri=ARK.kontaktinformasjon__nettsted, domain=None, range=Optional[str])

slots.kontaktinformasjon__sip = Slot(uri=FINT.sip, name="kontaktinformasjon__sip", curie=FINT.curie('sip'),
                   model_uri=ARK.kontaktinformasjon__sip, domain=None, range=Optional[str])

slots.kontaktinformasjon__telefonnummer = Slot(uri=FINT.telefonnummer, name="kontaktinformasjon__telefonnummer", curie=FINT.curie('telefonnummer'),
                   model_uri=ARK.kontaktinformasjon__telefonnummer, domain=None, range=Optional[str])

slots.adresse__adresselinje = Slot(uri=FINT.adresselinje, name="adresse__adresselinje", curie=FINT.curie('adresselinje'),
                   model_uri=ARK.adresse__adresselinje, domain=None, range=Optional[Union[str, list[str]]])

slots.adresse__postnummer = Slot(uri=FINT.postnummer, name="adresse__postnummer", curie=FINT.curie('postnummer'),
                   model_uri=ARK.adresse__postnummer, domain=None, range=Optional[str])

slots.adresse__poststed = Slot(uri=FINT.poststed, name="adresse__poststed", curie=FINT.curie('poststed'),
                   model_uri=ARK.adresse__poststed, domain=None, range=Optional[str])

slots.adresse__land = Slot(uri=FINT.land, name="adresse__land", curie=FINT.curie('land'),
                   model_uri=ARK.adresse__land, domain=None, range=Optional[Union[str, LandkodeId]])

slots.matrikkelnummer__adresse = Slot(uri=FINT.adresse, name="matrikkelnummer__adresse", curie=FINT.curie('adresse'),
                   model_uri=ARK.matrikkelnummer__adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.matrikkelnummer__bruksnummer = Slot(uri=FINT.bruksnummer, name="matrikkelnummer__bruksnummer", curie=FINT.curie('bruksnummer'),
                   model_uri=ARK.matrikkelnummer__bruksnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__festenummer = Slot(uri=FINT.festenummer, name="matrikkelnummer__festenummer", curie=FINT.curie('festenummer'),
                   model_uri=ARK.matrikkelnummer__festenummer, domain=None, range=Optional[str])

slots.matrikkelnummer__gaardsnummer = Slot(uri=FINT.gaardsnummer, name="matrikkelnummer__gaardsnummer", curie=FINT.curie('gaardsnummer'),
                   model_uri=ARK.matrikkelnummer__gaardsnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__seksjonsnummer = Slot(uri=FINT.seksjonsnummer, name="matrikkelnummer__seksjonsnummer", curie=FINT.curie('seksjonsnummer'),
                   model_uri=ARK.matrikkelnummer__seksjonsnummer, domain=None, range=Optional[str])

slots.matrikkelnummer__kommunenummer = Slot(uri=FINT.kommunenummer, name="matrikkelnummer__kommunenummer", curie=FINT.curie('kommunenummer'),
                   model_uri=ARK.matrikkelnummer__kommunenummer, domain=None, range=Optional[Union[str, KommuneId]])

slots.fylke__kommune = Slot(uri=FINT.kommune, name="fylke__kommune", curie=FINT.curie('kommune'),
                   model_uri=ARK.fylke__kommune, domain=None, range=Optional[Union[Union[str, KommuneId], list[Union[str, KommuneId]]]])

slots.kommune__fylke = Slot(uri=FINT.fylke, name="kommune__fylke", curie=FINT.curie('fylke'),
                   model_uri=ARK.kommune__fylke, domain=None, range=Union[str, FylkeId])

slots.valuta__bokstavkode = Slot(uri=FINT.bokstavkode, name="valuta__bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=ARK.valuta__bokstavkode, domain=None, range=Union[dict, Identifikator])

slots.valuta__navn = Slot(uri=FINT.valutaNavn, name="valuta__navn", curie=FINT.curie('valutaNavn'),
                   model_uri=ARK.valuta__navn, domain=None, range=str)

slots.valuta__nummerkode = Slot(uri=FINT.nummerkode, name="valuta__nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=ARK.valuta__nummerkode, domain=None, range=Union[dict, Identifikator])

slots.person__bilde = Slot(uri=FINT.bilde, name="person__bilde", curie=FINT.curie('bilde'),
                   model_uri=ARK.person__bilde, domain=None, range=Optional[str])

slots.person__bostedsadresse = Slot(uri=FINT.bostedsadresse, name="person__bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=ARK.person__bostedsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.person__fodselsdato = Slot(uri=FINT.fodselsdato, name="person__fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=ARK.person__fodselsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.person__fodselsnummer = Slot(uri=FINT.fodselsnummer, name="person__fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=ARK.person__fodselsnummer, domain=None, range=Union[dict, Identifikator])

slots.person__navn = Slot(uri=FINT.personNavn, name="person__navn", curie=FINT.curie('personNavn'),
                   model_uri=ARK.person__navn, domain=None, range=Union[dict, Personnavn])

slots.person__parorende = Slot(uri=FINT.parorende, name="person__parorende", curie=FINT.curie('parorende'),
                   model_uri=ARK.person__parorende, domain=None, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.person__statsborgerskap = Slot(uri=FINT.statsborgerskap, name="person__statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=ARK.person__statsborgerskap, domain=None, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.person__kommune = Slot(uri=FINT.kommune, name="person__kommune", curie=FINT.curie('kommune'),
                   model_uri=ARK.person__kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.person__kjonn = Slot(uri=FINT.kjonn, name="person__kjonn", curie=FINT.curie('kjonn'),
                   model_uri=ARK.person__kjonn, domain=None, range=Optional[Union[str, KjonnId]])

slots.person__foreldreansvar = Slot(uri=FINT.foreldreansvar, name="person__foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=ARK.person__foreldreansvar, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.person__foreldre = Slot(uri=FINT.foreldre, name="person__foreldre", curie=FINT.curie('foreldre'),
                   model_uri=ARK.person__foreldre, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.person__maalform = Slot(uri=FINT.maalform, name="person__maalform", curie=FINT.curie('maalform'),
                   model_uri=ARK.person__maalform, domain=None, range=Optional[Union[str, SpraakId]])

slots.person__personalressurs = Slot(uri=FINT.personalressurs, name="person__personalressurs", curie=FINT.curie('personalressurs'),
                   model_uri=ARK.person__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.person__morsmaal = Slot(uri=FINT.morsmaal, name="person__morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=ARK.person__morsmaal, domain=None, range=Optional[Union[str, SpraakId]])

slots.person__laerling = Slot(uri=FINT.laerling, name="person__laerling", curie=FINT.curie('laerling'),
                   model_uri=ARK.person__laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.person__elev = Slot(uri=FINT.elev, name="person__elev", curie=FINT.curie('elev'),
                   model_uri=ARK.person__elev, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.person__otungdom = Slot(uri=FINT.otungdom, name="person__otungdom", curie=FINT.curie('otungdom'),
                   model_uri=ARK.person__otungdom, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kontaktperson__kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="kontaktperson__kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ARK.kontaktperson__kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.kontaktperson__navn = Slot(uri=FINT.kontaktpersonNavn, name="kontaktperson__navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=ARK.kontaktperson__navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.kontaktperson__type = Slot(uri=FINT.type, name="kontaktperson__type", curie=FINT.curie('type'),
                   model_uri=ARK.kontaktperson__type, domain=None, range=str)

slots.kontaktperson__kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="kontaktperson__kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=ARK.kontaktperson__kontaktperson, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.virksomhet__virksomhetsId = Slot(uri=FINT.virksomhetsId, name="virksomhet__virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=ARK.virksomhet__virksomhetsId, domain=None, range=Union[dict, Identifikator])

slots.virksomhet__laerling = Slot(uri=FINT.laerling, name="virksomhet__laerling", curie=FINT.curie('laerling'),
                   model_uri=ARK.virksomhet__laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

