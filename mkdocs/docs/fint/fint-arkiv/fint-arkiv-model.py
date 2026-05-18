# Auto generated from fint-arkiv-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-18T09:11:07
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
    personalmappe_liste: Optional[Union[dict[Union[str, PersonalmappeId], Union[dict, "Personalmappe"]], list[Union[dict, "Personalmappe"]]]] = empty_dict()
    dispensasjonAutomatiskFredaKulturminne_liste: Optional[Union[dict[Union[str, DispensasjonAutomatiskFredaKulturminneId], Union[dict, "DispensasjonAutomatiskFredaKulturminne"]], list[Union[dict, "DispensasjonAutomatiskFredaKulturminne"]]]] = empty_dict()
    tilskuddFartoy_liste: Optional[Union[dict[Union[str, TilskuddFartoyId], Union[dict, "TilskuddFartoy"]], list[Union[dict, "TilskuddFartoy"]]]] = empty_dict()
    tilskuddFredaBygningPrivatEie_liste: Optional[Union[dict[Union[str, TilskuddFredaBygningPrivatEieId], Union[dict, "TilskuddFredaBygningPrivatEie"]], list[Union[dict, "TilskuddFredaBygningPrivatEie"]]]] = empty_dict()
    soeknadDrosjeloeyve_liste: Optional[Union[dict[Union[str, SoeknadDrosjeloeyveId], Union[dict, "SoeknadDrosjeloeyve"]], list[Union[dict, "SoeknadDrosjeloeyve"]]]] = empty_dict()
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

        self._normalize_inlined_as_list(slot_name="personalmappe_liste", slot_type=Personalmappe, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dispensasjonAutomatiskFredaKulturminne_liste", slot_type=DispensasjonAutomatiskFredaKulturminne, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tilskuddFartoy_liste", slot_type=TilskuddFartoy, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tilskuddFredaBygningPrivatEie_liste", slot_type=TilskuddFredaBygningPrivatEie, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="soeknadDrosjeloeyve_liste", slot_type=SoeknadDrosjeloeyve, key_name="id", keyed=True)

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
    opprettetAvNavn: str = None
    opprettetDato: Union[str, XSDDateTime] = None
    tittel: str = None
    arkivdel: Union[Union[str, ArkivdelId], list[Union[str, ArkivdelId]]] = None
    avsluttetAvNavn: Optional[str] = None
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

        if self._is_empty(self.opprettetAvNavn):
            self.MissingRequiredField("opprettetAvNavn")
        if not isinstance(self.opprettetAvNavn, str):
            self.opprettetAvNavn = str(self.opprettetAvNavn)

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

        if self.avsluttetAvNavn is not None and not isinstance(self.avsluttetAvNavn, str):
            self.avsluttetAvNavn = str(self.avsluttetAvNavn)

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
    personnavn: Union[dict, "Personnavn"] = None
    person: Union[str, PersonId] = None
    leder: Union[str, URIorCURIE] = None
    arbeidssted: Union[str, URIorCURIE] = None
    personalressurs: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonalmappeId):
            self.id = PersonalmappeId(self.id)

        if self._is_empty(self.personnavn):
            self.MissingRequiredField("personnavn")
        if not isinstance(self.personnavn, Personnavn):
            self.personnavn = Personnavn(**as_dict(self.personnavn))

        if self._is_empty(self.person):
            self.MissingRequiredField("person")
        if not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

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
    orgnummer: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoeknadDrosjeloeyveId):
            self.id = SoeknadDrosjeloeyveId(self.id)

        if self._is_empty(self.organisasjonsnavn):
            self.MissingRequiredField("organisasjonsnavn")
        if not isinstance(self.organisasjonsnavn, str):
            self.organisasjonsnavn = str(self.organisasjonsnavn)

        if self._is_empty(self.orgnummer):
            self.MissingRequiredField("orgnummer")
        if not isinstance(self.orgnummer, str):
            self.orgnummer = str(self.orgnummer)

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
    rekkefoelge: Optional[int] = None
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

        if self.rekkefoelge is not None and not isinstance(self.rekkefoelge, int):
            self.rekkefoelge = int(self.rekkefoelge)

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
    kontaktperson_str: Optional[str] = None
    korrespondansepartNavn: Optional[str] = None
    orgnummer: Optional[str] = None
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

        if self.kontaktperson_str is not None and not isinstance(self.kontaktperson_str, str):
            self.kontaktperson_str = str(self.kontaktperson_str)

        if self.korrespondansepartNavn is not None and not isinstance(self.korrespondansepartNavn, str):
            self.korrespondansepartNavn = str(self.korrespondansepartNavn)

        if self.orgnummer is not None and not isinstance(self.orgnummer, str):
            self.orgnummer = str(self.orgnummer)

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
    kontaktperson_str: Optional[str] = None
    orgnummer: Optional[str] = None
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

        if self.kontaktperson_str is not None and not isinstance(self.kontaktperson_str, str):
            self.kontaktperson_str = str(self.kontaktperson_str)

        if self.orgnummer is not None and not isinstance(self.orgnummer, str):
            self.orgnummer = str(self.orgnummer)

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
class Elev(YAMLRoot):
    """
    Ein elev registrert i skulesystemet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FINT["Elev"]
    class_class_curie: ClassVar[str] = "fint:Elev"
    class_name: ClassVar[str] = "Elev"
    class_model_uri: ClassVar[URIRef] = ARK.Elev

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
    class_model_uri: ClassVar[URIRef] = ARK.Person

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
    class_model_uri: ClassVar[URIRef] = ARK.Kontaktperson

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

slots.arkivdelar = Slot(uri=ARK.arkivdelar, name="arkivdelar", curie=ARK.curie('arkivdelar'),
                   model_uri=ARK.arkivdelar, domain=None, range=Optional[Union[dict[Union[str, ArkivdelId], Union[dict, Arkivdel]], list[Union[dict, Arkivdel]]]])

slots.arkivressursar = Slot(uri=ARK.arkivressursar, name="arkivressursar", curie=ARK.curie('arkivressursar'),
                   model_uri=ARK.arkivressursar, domain=None, range=Optional[Union[dict[Union[str, ArkivressursId], Union[dict, Arkivressurs]], list[Union[dict, Arkivressurs]]]])

slots.autorisasjonar = Slot(uri=ARK.autorisasjonar, name="autorisasjonar", curie=ARK.curie('autorisasjonar'),
                   model_uri=ARK.autorisasjonar, domain=None, range=Optional[Union[dict[Union[str, AutorisasjonId], Union[dict, Autorisasjon]], list[Union[dict, Autorisasjon]]]])

slots.administrativeEiningar = Slot(uri=ARK.administrativeEiningar, name="administrativeEiningar", curie=ARK.curie('administrativeEiningar'),
                   model_uri=ARK.administrativeEiningar, domain=None, range=Optional[Union[dict[Union[str, AdministrativEnhetId], Union[dict, AdministrativEnhet]], list[Union[dict, AdministrativEnhet]]]])

slots.dokumentfiler = Slot(uri=ARK.dokumentfiler, name="dokumentfiler", curie=ARK.curie('dokumentfiler'),
                   model_uri=ARK.dokumentfiler, domain=None, range=Optional[Union[dict[Union[str, DokumentfilId], Union[dict, Dokumentfil]], list[Union[dict, Dokumentfil]]]])

slots.dokumentbeskrivelsar = Slot(uri=ARK.dokumentbeskrivelsar, name="dokumentbeskrivelsar", curie=ARK.curie('dokumentbeskrivelsar'),
                   model_uri=ARK.dokumentbeskrivelsar, domain=None, range=Optional[Union[dict[Union[str, DokumentbeskrivelseId], Union[dict, Dokumentbeskrivelse]], list[Union[dict, Dokumentbeskrivelse]]]])

slots.journalpostar = Slot(uri=ARK.journalpostar, name="journalpostar", curie=ARK.curie('journalpostar'),
                   model_uri=ARK.journalpostar, domain=None, range=Optional[Union[dict[Union[str, JournalpostId], Union[dict, Journalpost]], list[Union[dict, Journalpost]]]])

slots.tilgangar = Slot(uri=ARK.tilgangar, name="tilgangar", curie=ARK.curie('tilgangar'),
                   model_uri=ARK.tilgangar, domain=None, range=Optional[Union[dict[Union[str, TilgangId], Union[dict, Tilgang]], list[Union[dict, Tilgang]]]])

slots.sakar = Slot(uri=ARK.sakar, name="sakar", curie=ARK.curie('sakar'),
                   model_uri=ARK.sakar, domain=None, range=Optional[Union[dict[Union[str, SakId], Union[dict, Sak]], list[Union[dict, Sak]]]])

slots.personalmappe_liste = Slot(uri=ARK.personalmappe, name="personalmappe_liste", curie=ARK.curie('personalmappe'),
                   model_uri=ARK.personalmappe_liste, domain=None, range=Optional[Union[dict[Union[str, PersonalmappeId], Union[dict, Personalmappe]], list[Union[dict, Personalmappe]]]])

slots.dispensasjonAutomatiskFredaKulturminne_liste = Slot(uri=ARK.dispensasjonAutomatiskFredaKulturminne, name="dispensasjonAutomatiskFredaKulturminne_liste", curie=ARK.curie('dispensasjonAutomatiskFredaKulturminne'),
                   model_uri=ARK.dispensasjonAutomatiskFredaKulturminne_liste, domain=None, range=Optional[Union[dict[Union[str, DispensasjonAutomatiskFredaKulturminneId], Union[dict, DispensasjonAutomatiskFredaKulturminne]], list[Union[dict, DispensasjonAutomatiskFredaKulturminne]]]])

slots.tilskuddFartoy_liste = Slot(uri=ARK.tilskuddFartoy, name="tilskuddFartoy_liste", curie=ARK.curie('tilskuddFartoy'),
                   model_uri=ARK.tilskuddFartoy_liste, domain=None, range=Optional[Union[dict[Union[str, TilskuddFartoyId], Union[dict, TilskuddFartoy]], list[Union[dict, TilskuddFartoy]]]])

slots.tilskuddFredaBygningPrivatEie_liste = Slot(uri=ARK.tilskuddFredaBygningPrivatEie, name="tilskuddFredaBygningPrivatEie_liste", curie=ARK.curie('tilskuddFredaBygningPrivatEie'),
                   model_uri=ARK.tilskuddFredaBygningPrivatEie_liste, domain=None, range=Optional[Union[dict[Union[str, TilskuddFredaBygningPrivatEieId], Union[dict, TilskuddFredaBygningPrivatEie]], list[Union[dict, TilskuddFredaBygningPrivatEie]]]])

slots.soeknadDrosjeloeyve_liste = Slot(uri=ARK.soeknadDrosjeloeyve, name="soeknadDrosjeloeyve_liste", curie=ARK.curie('soeknadDrosjeloeyve'),
                   model_uri=ARK.soeknadDrosjeloeyve_liste, domain=None, range=Optional[Union[dict[Union[str, SoeknadDrosjeloeyveId], Union[dict, SoeknadDrosjeloeyve]], list[Union[dict, SoeknadDrosjeloeyve]]]])

slots.dokumentstatuskodar = Slot(uri=ARK.dokumentstatuskodar, name="dokumentstatuskodar", curie=ARK.curie('dokumentstatuskodar'),
                   model_uri=ARK.dokumentstatuskodar, domain=None, range=Optional[Union[dict[Union[str, DokumentStatusId], Union[dict, DokumentStatus]], list[Union[dict, DokumentStatus]]]])

slots.dokumenttypar = Slot(uri=ARK.dokumenttypar, name="dokumenttypar", curie=ARK.curie('dokumenttypar'),
                   model_uri=ARK.dokumenttypar, domain=None, range=Optional[Union[dict[Union[str, DokumentTypeId], Union[dict, DokumentType]], list[Union[dict, DokumentType]]]])

slots.formatar = Slot(uri=ARK.formatar, name="formatar", curie=ARK.curie('formatar'),
                   model_uri=ARK.formatar, domain=None, range=Optional[Union[dict[Union[str, FormatId], Union[dict, Format]], list[Union[dict, Format]]]])

slots.journalposttypar = Slot(uri=ARK.journalposttypar, name="journalposttypar", curie=ARK.curie('journalposttypar'),
                   model_uri=ARK.journalposttypar, domain=None, range=Optional[Union[dict[Union[str, JournalpostTypeId], Union[dict, JournalpostType]], list[Union[dict, JournalpostType]]]])

slots.journalstatuskodar = Slot(uri=ARK.journalstatuskodar, name="journalstatuskodar", curie=ARK.curie('journalstatuskodar'),
                   model_uri=ARK.journalstatuskodar, domain=None, range=Optional[Union[dict[Union[str, JournalStatusId], Union[dict, JournalStatus]], list[Union[dict, JournalStatus]]]])

slots.klassifikasjonstypar = Slot(uri=ARK.klassifikasjonstypar, name="klassifikasjonstypar", curie=ARK.curie('klassifikasjonstypar'),
                   model_uri=ARK.klassifikasjonstypar, domain=None, range=Optional[Union[dict[Union[str, KlassifikasjonstypeId], Union[dict, Klassifikasjonstype]], list[Union[dict, Klassifikasjonstype]]]])

slots.korrespondanseparttypar = Slot(uri=ARK.korrespondanseparttypar, name="korrespondanseparttypar", curie=ARK.curie('korrespondanseparttypar'),
                   model_uri=ARK.korrespondanseparttypar, domain=None, range=Optional[Union[dict[Union[str, KorrespondansepartTypeId], Union[dict, KorrespondansepartType]], list[Union[dict, KorrespondansepartType]]]])

slots.merknadstypar = Slot(uri=ARK.merknadstypar, name="merknadstypar", curie=ARK.curie('merknadstypar'),
                   model_uri=ARK.merknadstypar, domain=None, range=Optional[Union[dict[Union[str, MerknadstypeId], Union[dict, Merknadstype]], list[Union[dict, Merknadstype]]]])

slots.partRollar = Slot(uri=ARK.partRollar, name="partRollar", curie=ARK.curie('partRollar'),
                   model_uri=ARK.partRollar, domain=None, range=Optional[Union[dict[Union[str, PartRolleId], Union[dict, PartRolle]], list[Union[dict, PartRolle]]]])

slots.rollar = Slot(uri=ARK.rollar, name="rollar", curie=ARK.curie('rollar'),
                   model_uri=ARK.rollar, domain=None, range=Optional[Union[dict[Union[str, RolleId], Union[dict, Rolle]], list[Union[dict, Rolle]]]])

slots.saksmappetypar = Slot(uri=ARK.saksmappetypar, name="saksmappetypar", curie=ARK.curie('saksmappetypar'),
                   model_uri=ARK.saksmappetypar, domain=None, range=Optional[Union[dict[Union[str, SaksmappetypeId], Union[dict, Saksmappetype]], list[Union[dict, Saksmappetype]]]])

slots.sakstatuskodar = Slot(uri=ARK.sakstatuskodar, name="sakstatuskodar", curie=ARK.curie('sakstatuskodar'),
                   model_uri=ARK.sakstatuskodar, domain=None, range=Optional[Union[dict[Union[str, SaksstatusId], Union[dict, Saksstatus]], list[Union[dict, Saksstatus]]]])

slots.skjermingsheimlar = Slot(uri=ARK.skjermingsheimlar, name="skjermingsheimlar", curie=ARK.curie('skjermingsheimlar'),
                   model_uri=ARK.skjermingsheimlar, domain=None, range=Optional[Union[dict[Union[str, SkjermingshjemmelId], Union[dict, Skjermingshjemmel]], list[Union[dict, Skjermingshjemmel]]]])

slots.tilgangsgrupper = Slot(uri=ARK.tilgangsgrupper, name="tilgangsgrupper", curie=ARK.curie('tilgangsgrupper'),
                   model_uri=ARK.tilgangsgrupper, domain=None, range=Optional[Union[dict[Union[str, TilgangsgruppeId], Union[dict, Tilgangsgruppe]], list[Union[dict, Tilgangsgruppe]]]])

slots.tilgangsrestriksjonar = Slot(uri=ARK.tilgangsrestriksjonar, name="tilgangsrestriksjonar", curie=ARK.curie('tilgangsrestriksjonar'),
                   model_uri=ARK.tilgangsrestriksjonar, domain=None, range=Optional[Union[dict[Union[str, TilgangsrestriksjonId], Union[dict, Tilgangsrestriksjon]], list[Union[dict, Tilgangsrestriksjon]]]])

slots.tilknyttetRegistreringSomKodar = Slot(uri=ARK.tilknyttetRegistreringSomKodar, name="tilknyttetRegistreringSomKodar", curie=ARK.curie('tilknyttetRegistreringSomKodar'),
                   model_uri=ARK.tilknyttetRegistreringSomKodar, domain=None, range=Optional[Union[dict[Union[str, TilknyttetRegistreringSomId], Union[dict, TilknyttetRegistreringSom]], list[Union[dict, TilknyttetRegistreringSom]]]])

slots.variantformatar = Slot(uri=ARK.variantformatar, name="variantformatar", curie=ARK.curie('variantformatar'),
                   model_uri=ARK.variantformatar, domain=None, range=Optional[Union[dict[Union[str, VariantformatId], Union[dict, Variantformat]], list[Union[dict, Variantformat]]]])

slots.tittel = Slot(uri=ARK.tittel, name="tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.tittel, domain=None, range=Optional[str])

slots.avsluttetDato = Slot(uri=ARK.avsluttetDato, name="avsluttetDato", curie=ARK.curie('avsluttetDato'),
                   model_uri=ARK.avsluttetDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.opprettetDato = Slot(uri=ARK.opprettetDato, name="opprettetDato", curie=ARK.curie('opprettetDato'),
                   model_uri=ARK.opprettetDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.offentligTittel = Slot(uri=ARK.offentligTittel, name="offentligTittel", curie=ARK.curie('offentligTittel'),
                   model_uri=ARK.offentligTittel, domain=None, range=Optional[str])

slots.klasse = Slot(uri=ARK.klasse, name="klasse", curie=ARK.curie('klasse'),
                   model_uri=ARK.klasse, domain=None, range=Optional[Union[dict, Klasse]])

slots.part = Slot(uri=ARK.part, name="part", curie=ARK.curie('part'),
                   model_uri=ARK.part, domain=None, range=Optional[Union[Union[dict, Part], list[Union[dict, Part]]]])

slots.merknad = Slot(uri=ARK.merknad, name="merknad", curie=ARK.curie('merknad'),
                   model_uri=ARK.merknad, domain=None, range=Optional[Union[Union[dict, Merknad], list[Union[dict, Merknad]]]])

slots.skjerming = Slot(uri=ARK.skjerming, name="skjerming", curie=ARK.curie('skjerming'),
                   model_uri=ARK.skjerming, domain=None, range=Optional[Union[dict, Skjerming]])

slots.arkivdel = Slot(uri=ARK.arkivdel, name="arkivdel", curie=ARK.curie('arkivdel'),
                   model_uri=ARK.arkivdel, domain=None, range=Optional[Union[str, ArkivdelId]])

slots.opprettetAv = Slot(uri=ARK.opprettetAv, name="opprettetAv", curie=ARK.curie('opprettetAv'),
                   model_uri=ARK.opprettetAv, domain=None, range=Optional[Union[str, ArkivressursId]])

slots.avsluttetAv = Slot(uri=ARK.avsluttetAv, name="avsluttetAv", curie=ARK.curie('avsluttetAv'),
                   model_uri=ARK.avsluttetAv, domain=None, range=Optional[Union[str, ArkivressursId]])

slots.noekkelord = Slot(uri=ARK.noekkelord, name="noekkelord", curie=ARK.curie('noekkelord'),
                   model_uri=ARK.noekkelord, domain=None, range=Optional[Union[str, list[str]]])

slots.mappeId = Slot(uri=ARK.mappeId, name="mappeId", curie=ARK.curie('mappeId'),
                   model_uri=ARK.mappeId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.tilgangsgruppe = Slot(uri=ARK.tilgangsgruppe, name="tilgangsgruppe", curie=ARK.curie('tilgangsgruppe'),
                   model_uri=ARK.tilgangsgruppe, domain=None, range=Optional[Union[str, TilgangsgruppeId]])

slots.administrativEnhet = Slot(uri=ARK.administrativEnhet, name="administrativEnhet", curie=ARK.curie('administrativEnhet'),
                   model_uri=ARK.administrativEnhet, domain=None, range=Optional[Union[str, AdministrativEnhetId]])

slots.journalenhet = Slot(uri=ARK.journalenhet, name="journalenhet", curie=ARK.curie('journalenhet'),
                   model_uri=ARK.journalenhet, domain=None, range=Optional[Union[str, AdministrativEnhetId]])

slots.arkivressurs = Slot(uri=ARK.arkivressurs, name="arkivressurs", curie=ARK.curie('arkivressurs'),
                   model_uri=ARK.arkivressurs, domain=None, range=Optional[Union[Union[str, ArkivressursId], list[Union[str, ArkivressursId]]]])

slots.tilgangsrestriksjon = Slot(uri=ARK.tilgangsrestriksjon, name="tilgangsrestriksjon", curie=ARK.curie('tilgangsrestriksjon'),
                   model_uri=ARK.tilgangsrestriksjon, domain=None, range=Optional[Union[str, TilgangsrestriksjonId]])

slots.forfatter = Slot(uri=ARK.forfatter, name="forfatter", curie=ARK.curie('forfatter'),
                   model_uri=ARK.forfatter, domain=None, range=Optional[Union[str, list[str]]])

slots.journalpost = Slot(uri=ARK.journalpost, name="journalpost", curie=ARK.curie('journalpost'),
                   model_uri=ARK.journalpost, domain=None, range=Optional[Union[Union[str, JournalpostId], list[Union[str, JournalpostId]]]])

slots.saksaar = Slot(uri=ARK.saksaar, name="saksaar", curie=ARK.curie('saksaar'),
                   model_uri=ARK.saksaar, domain=None, range=Optional[str])

slots.saksdato = Slot(uri=ARK.saksdato, name="saksdato", curie=ARK.curie('saksdato'),
                   model_uri=ARK.saksdato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.sakssekvensnummer = Slot(uri=ARK.sakssekvensnummer, name="sakssekvensnummer", curie=ARK.curie('sakssekvensnummer'),
                   model_uri=ARK.sakssekvensnummer, domain=None, range=Optional[str])

slots.utlaantDato = Slot(uri=ARK.utlaantDato, name="utlaantDato", curie=ARK.curie('utlaantDato'),
                   model_uri=ARK.utlaantDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.saksmappetype = Slot(uri=ARK.saksmappetype, name="saksmappetype", curie=ARK.curie('saksmappetype'),
                   model_uri=ARK.saksmappetype, domain=None, range=Optional[Union[str, SaksmappetypeId]])

slots.saksstatus = Slot(uri=ARK.saksstatus, name="saksstatus", curie=ARK.curie('saksstatus'),
                   model_uri=ARK.saksstatus, domain=None, range=Optional[Union[str, SaksstatusId]])

slots.saksansvarlig = Slot(uri=ARK.saksansvarlig, name="saksansvarlig", curie=ARK.curie('saksansvarlig'),
                   model_uri=ARK.saksansvarlig, domain=None, range=Optional[Union[str, ArkivressursId]])

slots.arkivertDato = Slot(uri=ARK.arkivertDato, name="arkivertDato", curie=ARK.curie('arkivertDato'),
                   model_uri=ARK.arkivertDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.dokumentbeskrivelse = Slot(uri=ARK.dokumentbeskrivelse, name="dokumentbeskrivelse", curie=ARK.curie('dokumentbeskrivelse'),
                   model_uri=ARK.dokumentbeskrivelse, domain=None, range=Optional[Union[Union[str, DokumentbeskrivelseId], list[Union[str, DokumentbeskrivelseId]]]])

slots.korrespondansepart = Slot(uri=ARK.korrespondansepart, name="korrespondansepart", curie=ARK.curie('korrespondansepart'),
                   model_uri=ARK.korrespondansepart, domain=None, range=Optional[Union[Union[dict, Korrespondansepart], list[Union[dict, Korrespondansepart]]]])

slots.nokkelord = Slot(uri=ARK.nokkelord, name="nokkelord", curie=ARK.curie('nokkelord'),
                   model_uri=ARK.nokkelord, domain=None, range=Optional[Union[str, list[str]]])

slots.referanseArkivDel = Slot(uri=ARK.referanseArkivDel, name="referanseArkivDel", curie=ARK.curie('referanseArkivDel'),
                   model_uri=ARK.referanseArkivDel, domain=None, range=Optional[Union[str, list[str]]])

slots.registreringsId = Slot(uri=ARK.registreringsId, name="registreringsId", curie=ARK.curie('registreringsId'),
                   model_uri=ARK.registreringsId, domain=None, range=Optional[str])

slots.saksbehandler = Slot(uri=ARK.saksbehandler, name="saksbehandler", curie=ARK.curie('saksbehandler'),
                   model_uri=ARK.saksbehandler, domain=None, range=Optional[Union[str, ArkivressursId]])

slots.arkivertAv = Slot(uri=ARK.arkivertAv, name="arkivertAv", curie=ARK.curie('arkivertAv'),
                   model_uri=ARK.arkivertAv, domain=None, range=Optional[Union[str, ArkivressursId]])

slots.personnavn = Slot(uri=ARK.personnavn, name="personnavn", curie=ARK.curie('personnavn'),
                   model_uri=ARK.personnavn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.organisasjonselement = Slot(uri=ARK.organisasjonselement, name="organisasjonselement", curie=ARK.curie('organisasjonselement'),
                   model_uri=ARK.organisasjonselement, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kildesystemId = Slot(uri=ARK.kildesystemId, name="kildesystemId", curie=ARK.curie('kildesystemId'),
                   model_uri=ARK.kildesystemId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.personalressurs = Slot(uri=ARK.personalressurs, name="personalressurs", curie=ARK.curie('personalressurs'),
                   model_uri=ARK.personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.autorisasjon = Slot(uri=ARK.autorisasjon, name="autorisasjon", curie=ARK.curie('autorisasjon'),
                   model_uri=ARK.autorisasjon, domain=None, range=Optional[Union[Union[str, AutorisasjonId], list[Union[str, AutorisasjonId]]]])

slots.tilgang = Slot(uri=ARK.tilgang, name="tilgang", curie=ARK.curie('tilgang'),
                   model_uri=ARK.tilgang, domain=None, range=Optional[Union[Union[str, TilgangId], list[Union[str, TilgangId]]]])

slots.administrativenhet = Slot(uri=ARK.administrativenhet, name="administrativenhet", curie=ARK.curie('administrativenhet'),
                   model_uri=ARK.administrativenhet, domain=None, range=Optional[Union[Union[str, AdministrativEnhetId], list[Union[str, AdministrativEnhetId]]]])

slots.klassifikasjonssystem = Slot(uri=ARK.klassifikasjonssystem, name="klassifikasjonssystem", curie=ARK.curie('klassifikasjonssystem'),
                   model_uri=ARK.klassifikasjonssystem, domain=None, range=Optional[Union[str, KlassifikasjonssystemId]])

slots.klassifikasjonstype = Slot(uri=ARK.klassifikasjonstype, name="klassifikasjonstype", curie=ARK.curie('klassifikasjonstype'),
                   model_uri=ARK.klassifikasjonstype, domain=None, range=Optional[Union[str, KlassifikasjonstypeId]])

slots.avsluttetAvNavn = Slot(uri=ARK.avsluttetAvNavn, name="avsluttetAvNavn", curie=ARK.curie('avsluttetAvNavn'),
                   model_uri=ARK.avsluttetAvNavn, domain=None, range=Optional[str])

slots.opprettetAvNavn = Slot(uri=ARK.opprettetAvNavn, name="opprettetAvNavn", curie=ARK.curie('opprettetAvNavn'),
                   model_uri=ARK.opprettetAvNavn, domain=None, range=Optional[str])

slots.rolle = Slot(uri=ARK.rolle, name="rolle", curie=ARK.curie('rolle'),
                   model_uri=ARK.rolle, domain=None, range=Optional[Union[str, RolleId]])

slots.data = Slot(uri=ARK.data, name="data", curie=ARK.curie('data'),
                   model_uri=ARK.data, domain=None, range=Optional[str])

slots.filnavn = Slot(uri=ARK.filnavn, name="filnavn", curie=ARK.curie('filnavn'),
                   model_uri=ARK.filnavn, domain=None, range=Optional[str])

slots.format = Slot(uri=ARK.format, name="format", curie=ARK.curie('format'),
                   model_uri=ARK.format, domain=None, range=Optional[str])

slots.antallVedlegg = Slot(uri=ARK.antallVedlegg, name="antallVedlegg", curie=ARK.curie('antallVedlegg'),
                   model_uri=ARK.antallVedlegg, domain=None, range=Optional[int])

slots.avskrivning = Slot(uri=ARK.avskrivning, name="avskrivning", curie=ARK.curie('avskrivning'),
                   model_uri=ARK.avskrivning, domain=None, range=Optional[Union[dict, Avskrivning]])

slots.dokumentetsDato = Slot(uri=ARK.dokumentetsDato, name="dokumentetsDato", curie=ARK.curie('dokumentetsDato'),
                   model_uri=ARK.dokumentetsDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.forfallsDato = Slot(uri=ARK.forfallsDato, name="forfallsDato", curie=ARK.curie('forfallsDato'),
                   model_uri=ARK.forfallsDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.journalAr = Slot(uri=ARK.journalAr, name="journalAr", curie=ARK.curie('journalAr'),
                   model_uri=ARK.journalAr, domain=None, range=Optional[str])

slots.journalDato = Slot(uri=ARK.journalDato, name="journalDato", curie=ARK.curie('journalDato'),
                   model_uri=ARK.journalDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.journalPostnummer = Slot(uri=ARK.journalPostnummer, name="journalPostnummer", curie=ARK.curie('journalPostnummer'),
                   model_uri=ARK.journalPostnummer, domain=None, range=Optional[int])

slots.journalSekvensnummer = Slot(uri=ARK.journalSekvensnummer, name="journalSekvensnummer", curie=ARK.curie('journalSekvensnummer'),
                   model_uri=ARK.journalSekvensnummer, domain=None, range=Optional[int])

slots.mottattDato = Slot(uri=ARK.mottattDato, name="mottattDato", curie=ARK.curie('mottattDato'),
                   model_uri=ARK.mottattDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.offentlighetsvurdertDato = Slot(uri=ARK.offentlighetsvurdertDato, name="offentlighetsvurdertDato", curie=ARK.curie('offentlighetsvurdertDato'),
                   model_uri=ARK.offentlighetsvurdertDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.sendtDato = Slot(uri=ARK.sendtDato, name="sendtDato", curie=ARK.curie('sendtDato'),
                   model_uri=ARK.sendtDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.journalposttype = Slot(uri=ARK.journalposttype, name="journalposttype", curie=ARK.curie('journalposttype'),
                   model_uri=ARK.journalposttype, domain=None, range=Optional[Union[str, JournalpostTypeId]])

slots.journalstatus = Slot(uri=ARK.journalstatus, name="journalstatus", curie=ARK.curie('journalstatus'),
                   model_uri=ARK.journalstatus, domain=None, range=Optional[Union[str, JournalStatusId]])

slots.dokumentnummer = Slot(uri=ARK.dokumentnummer, name="dokumentnummer", curie=ARK.curie('dokumentnummer'),
                   model_uri=ARK.dokumentnummer, domain=None, range=Optional[int])

slots.dokumentobjekt = Slot(uri=ARK.dokumentobjekt, name="dokumentobjekt", curie=ARK.curie('dokumentobjekt'),
                   model_uri=ARK.dokumentobjekt, domain=None, range=Optional[Union[Union[dict, Dokumentobjekt], list[Union[dict, Dokumentobjekt]]]])

slots.referanseArkivdel = Slot(uri=ARK.referanseArkivdel, name="referanseArkivdel", curie=ARK.curie('referanseArkivdel'),
                   model_uri=ARK.referanseArkivdel, domain=None, range=Optional[Union[str, list[str]]])

slots.tilknyttetDato = Slot(uri=ARK.tilknyttetDato, name="tilknyttetDato", curie=ARK.curie('tilknyttetDato'),
                   model_uri=ARK.tilknyttetDato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.dokumentstatus = Slot(uri=ARK.dokumentstatus, name="dokumentstatus", curie=ARK.curie('dokumentstatus'),
                   model_uri=ARK.dokumentstatus, domain=None, range=Optional[Union[str, DokumentStatusId]])

slots.dokumentType = Slot(uri=ARK.dokumentType, name="dokumentType", curie=ARK.curie('dokumentType'),
                   model_uri=ARK.dokumentType, domain=None, range=Optional[Union[str, DokumentTypeId]])

slots.tilknyttetRegistreringSom = Slot(uri=ARK.tilknyttetRegistreringSom, name="tilknyttetRegistreringSom", curie=ARK.curie('tilknyttetRegistreringSom'),
                   model_uri=ARK.tilknyttetRegistreringSom, domain=None, range=Optional[Union[Union[str, TilknyttetRegistreringSomId], list[Union[str, TilknyttetRegistreringSomId]]]])

slots.tilknyttetAv = Slot(uri=ARK.tilknyttetAv, name="tilknyttetAv", curie=ARK.curie('tilknyttetAv'),
                   model_uri=ARK.tilknyttetAv, domain=None, range=Optional[Union[str, ArkivressursId]])

slots.filstorrelse = Slot(uri=ARK.filstorrelse, name="filstorrelse", curie=ARK.curie('filstorrelse'),
                   model_uri=ARK.filstorrelse, domain=None, range=Optional[str])

slots.formatDetaljer = Slot(uri=ARK.formatDetaljer, name="formatDetaljer", curie=ARK.curie('formatDetaljer'),
                   model_uri=ARK.formatDetaljer, domain=None, range=Optional[str])

slots.sjekksum = Slot(uri=ARK.sjekksum, name="sjekksum", curie=ARK.curie('sjekksum'),
                   model_uri=ARK.sjekksum, domain=None, range=Optional[str])

slots.sjekksumAlgoritme = Slot(uri=ARK.sjekksumAlgoritme, name="sjekksumAlgoritme", curie=ARK.curie('sjekksumAlgoritme'),
                   model_uri=ARK.sjekksumAlgoritme, domain=None, range=Optional[str])

slots.versjonsnummer = Slot(uri=ARK.versjonsnummer, name="versjonsnummer", curie=ARK.curie('versjonsnummer'),
                   model_uri=ARK.versjonsnummer, domain=None, range=Optional[int])

slots.filformat = Slot(uri=ARK.filformat, name="filformat", curie=ARK.curie('filformat'),
                   model_uri=ARK.filformat, domain=None, range=Optional[Union[str, FormatId]])

slots.variantFormat = Slot(uri=ARK.variantFormat, name="variantFormat", curie=ARK.curie('variantFormat'),
                   model_uri=ARK.variantFormat, domain=None, range=Optional[Union[str, VariantformatId]])

slots.referanseDokumentfil = Slot(uri=ARK.referanseDokumentfil, name="referanseDokumentfil", curie=ARK.curie('referanseDokumentfil'),
                   model_uri=ARK.referanseDokumentfil, domain=None, range=Optional[Union[str, DokumentfilId]])

slots.klasseId = Slot(uri=ARK.klasseId, name="klasseId", curie=ARK.curie('klasseId'),
                   model_uri=ARK.klasseId, domain=None, range=Optional[str])

slots.rekkefoelge = Slot(uri=ARK.rekkefolge, name="rekkefoelge", curie=ARK.curie('rekkefolge'),
                   model_uri=ARK.rekkefoelge, domain=None, range=Optional[int])

slots.foedselsnummer = Slot(uri=ARK.foedselsnummer, name="foedselsnummer", curie=ARK.curie('foedselsnummer'),
                   model_uri=ARK.foedselsnummer, domain=None, range=Optional[str])

slots.kontaktperson_str = Slot(uri=ARK.kontaktperson, name="kontaktperson_str", curie=ARK.curie('kontaktperson'),
                   model_uri=ARK.kontaktperson_str, domain=None, range=Optional[str])

slots.korrespondansepartNavn = Slot(uri=ARK.korrespondansepartNavn, name="korrespondansepartNavn", curie=ARK.curie('korrespondansepartNavn'),
                   model_uri=ARK.korrespondansepartNavn, domain=None, range=Optional[str])

slots.orgnummer = Slot(uri=ARK.organisasjonsnummer, name="orgnummer", curie=ARK.curie('organisasjonsnummer'),
                   model_uri=ARK.orgnummer, domain=None, range=Optional[str])

slots.korrespondanseparttype = Slot(uri=ARK.korrespondanseparttype, name="korrespondanseparttype", curie=ARK.curie('korrespondanseparttype'),
                   model_uri=ARK.korrespondanseparttype, domain=None, range=Optional[Union[str, KorrespondansepartTypeId]])

slots.partNavn = Slot(uri=ARK.partNavn, name="partNavn", curie=ARK.curie('partNavn'),
                   model_uri=ARK.partNavn, domain=None, range=Optional[str])

slots.partRolle = Slot(uri=ARK.partRolle, name="partRolle", curie=ARK.curie('partRolle'),
                   model_uri=ARK.partRolle, domain=None, range=Optional[Union[str, PartRolleId]])

slots.merknadsdato = Slot(uri=ARK.merknadsdato, name="merknadsdato", curie=ARK.curie('merknadsdato'),
                   model_uri=ARK.merknadsdato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.merknadstekst = Slot(uri=ARK.merknadstekst, name="merknadstekst", curie=ARK.curie('merknadstekst'),
                   model_uri=ARK.merknadstekst, domain=None, range=Optional[str])

slots.merknadstype = Slot(uri=ARK.merknadstype, name="merknadstype", curie=ARK.curie('merknadstype'),
                   model_uri=ARK.merknadstype, domain=None, range=Optional[Union[str, MerknadstypeId]])

slots.merknadRegistrertAv = Slot(uri=ARK.merknadRegistrertAv, name="merknadRegistrertAv", curie=ARK.curie('merknadRegistrertAv'),
                   model_uri=ARK.merknadRegistrertAv, domain=None, range=Optional[Union[str, ArkivressursId]])

slots.skjermingshjemmel = Slot(uri=ARK.skjermingshjemmel, name="skjermingshjemmel", curie=ARK.curie('skjermingshjemmel'),
                   model_uri=ARK.skjermingshjemmel, domain=None, range=Optional[Union[str, SkjermingshjemmelId]])

slots.avskrevetAv = Slot(uri=ARK.avskrevetAv, name="avskrevetAv", curie=ARK.curie('avskrevetAv'),
                   model_uri=ARK.avskrevetAv, domain=None, range=Optional[str])

slots.avskrivningsdato = Slot(uri=ARK.avskrivningsdato, name="avskrivningsdato", curie=ARK.curie('avskrivningsdato'),
                   model_uri=ARK.avskrivningsdato, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.avskrivningsmate = Slot(uri=ARK.avskrivningsmate, name="avskrivningsmate", curie=ARK.curie('avskrivningsmate'),
                   model_uri=ARK.avskrivningsmate, domain=None, range=Optional[str])

slots.leder = Slot(uri=ARK.leder, name="leder", curie=ARK.curie('leder'),
                   model_uri=ARK.leder, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.arbeidssted = Slot(uri=ARK.arbeidssted, name="arbeidssted", curie=ARK.curie('arbeidssted'),
                   model_uri=ARK.arbeidssted, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kulturminneId = Slot(uri=ARK.kulturminneId, name="kulturminneId", curie=ARK.curie('kulturminneId'),
                   model_uri=ARK.kulturminneId, domain=None, range=Optional[str])

slots.matrikkelnummer = Slot(uri=ARK.matrikkelnummer, name="matrikkelnummer", curie=ARK.curie('matrikkelnummer'),
                   model_uri=ARK.matrikkelnummer, domain=None, range=Optional[Union[dict, Matrikkelnummer]])

slots.soeknadsnummer = Slot(uri=ARK.soeknadsnummer, name="soeknadsnummer", curie=ARK.curie('soeknadsnummer'),
                   model_uri=ARK.soeknadsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.tiltak = Slot(uri=ARK.tiltak, name="tiltak", curie=ARK.curie('tiltak'),
                   model_uri=ARK.tiltak, domain=None, range=Optional[str])

slots.fartoyNavn = Slot(uri=ARK.fartoyNavn, name="fartoyNavn", curie=ARK.curie('fartoyNavn'),
                   model_uri=ARK.fartoyNavn, domain=None, range=Optional[str])

slots.kallesignal = Slot(uri=ARK.kallesignal, name="kallesignal", curie=ARK.curie('kallesignal'),
                   model_uri=ARK.kallesignal, domain=None, range=Optional[str])

slots.bygningsnavn = Slot(uri=ARK.bygningsnavn, name="bygningsnavn", curie=ARK.curie('bygningsnavn'),
                   model_uri=ARK.bygningsnavn, domain=None, range=Optional[str])

slots.id = Slot(uri=FINT.id, name="id", curie=FINT.curie('id'),
                   model_uri=ARK.id, domain=None, range=URIRef)

slots.gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.gyldighetsperiode, domain=None, range=Optional[Union[dict, Periode]])

slots.kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ARK.kontaktinformasjon, domain=None, range=Optional[Union[dict, Kontaktinformasjon]])

slots.postadresse = Slot(uri=FINT.postadresse, name="postadresse", curie=FINT.curie('postadresse'),
                   model_uri=ARK.postadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.forretningsadresse = Slot(uri=FINT.forretningsadresse, name="forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=ARK.forretningsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=ARK.organisasjonsnavn, domain=None, range=Optional[str])

slots.organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=ARK.organisasjonsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.kode = Slot(uri=FINT.kode, name="kode", curie=FINT.curie('kode'),
                   model_uri=ARK.kode, domain=None, range=Optional[str])

slots.navn = Slot(uri=FINT.navn, name="navn", curie=FINT.curie('navn'),
                   model_uri=ARK.navn, domain=None, range=Optional[str])

slots.passiv = Slot(uri=FINT.passiv, name="passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.passiv, domain=None, range=Optional[Union[bool, Bool]])

slots.identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=ARK.identifikatorverdi, domain=None, range=Optional[str])

slots.beskrivelse = Slot(uri=FINT.beskrivelse, name="beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=ARK.beskrivelse, domain=None, range=Optional[str])

slots.start = Slot(uri=FINT.start, name="start", curie=FINT.curie('start'),
                   model_uri=ARK.start, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.slutt = Slot(uri=FINT.slutt, name="slutt", curie=FINT.curie('slutt'),
                   model_uri=ARK.slutt, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.fornavn = Slot(uri=FINT.fornavn, name="fornavn", curie=FINT.curie('fornavn'),
                   model_uri=ARK.fornavn, domain=None, range=Optional[str])

slots.mellomnavn = Slot(uri=FINT.mellomnavn, name="mellomnavn", curie=FINT.curie('mellomnavn'),
                   model_uri=ARK.mellomnavn, domain=None, range=Optional[str])

slots.etternavn = Slot(uri=FINT.etternavn, name="etternavn", curie=FINT.curie('etternavn'),
                   model_uri=ARK.etternavn, domain=None, range=Optional[str])

slots.epostadresse = Slot(uri=FINT.epostadresse, name="epostadresse", curie=FINT.curie('epostadresse'),
                   model_uri=ARK.epostadresse, domain=None, range=Optional[str])

slots.mobiltelefonnummer = Slot(uri=FINT.mobiltelefonnummer, name="mobiltelefonnummer", curie=FINT.curie('mobiltelefonnummer'),
                   model_uri=ARK.mobiltelefonnummer, domain=None, range=Optional[str])

slots.nettsted = Slot(uri=FINT.nettsted, name="nettsted", curie=FINT.curie('nettsted'),
                   model_uri=ARK.nettsted, domain=None, range=Optional[str])

slots.sip = Slot(uri=FINT.sip, name="sip", curie=FINT.curie('sip'),
                   model_uri=ARK.sip, domain=None, range=Optional[str])

slots.telefonnummer = Slot(uri=FINT.telefonnummer, name="telefonnummer", curie=FINT.curie('telefonnummer'),
                   model_uri=ARK.telefonnummer, domain=None, range=Optional[str])

slots.adresselinje = Slot(uri=FINT.adresselinje, name="adresselinje", curie=FINT.curie('adresselinje'),
                   model_uri=ARK.adresselinje, domain=None, range=Optional[Union[str, list[str]]])

slots.postnummer = Slot(uri=FINT.postnummer, name="postnummer", curie=FINT.curie('postnummer'),
                   model_uri=ARK.postnummer, domain=None, range=Optional[str])

slots.poststed = Slot(uri=FINT.poststed, name="poststed", curie=FINT.curie('poststed'),
                   model_uri=ARK.poststed, domain=None, range=Optional[str])

slots.land = Slot(uri=FINT.land, name="land", curie=FINT.curie('land'),
                   model_uri=ARK.land, domain=None, range=Optional[Union[str, LandkodeId]])

slots.adresse = Slot(uri=FINT.adresse, name="adresse", curie=FINT.curie('adresse'),
                   model_uri=ARK.adresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.bruksnummer = Slot(uri=FINT.bruksnummer, name="bruksnummer", curie=FINT.curie('bruksnummer'),
                   model_uri=ARK.bruksnummer, domain=None, range=Optional[str])

slots.festenummer = Slot(uri=FINT.festenummer, name="festenummer", curie=FINT.curie('festenummer'),
                   model_uri=ARK.festenummer, domain=None, range=Optional[str])

slots.gaardsnummer = Slot(uri=FINT.gaardsnummer, name="gaardsnummer", curie=FINT.curie('gaardsnummer'),
                   model_uri=ARK.gaardsnummer, domain=None, range=Optional[str])

slots.seksjonsnummer = Slot(uri=FINT.seksjonsnummer, name="seksjonsnummer", curie=FINT.curie('seksjonsnummer'),
                   model_uri=ARK.seksjonsnummer, domain=None, range=Optional[str])

slots.kommunenummer = Slot(uri=FINT.kommunenummer, name="kommunenummer", curie=FINT.curie('kommunenummer'),
                   model_uri=ARK.kommunenummer, domain=None, range=Optional[Union[str, KommuneId]])

slots.fylke = Slot(uri=FINT.fylke, name="fylke", curie=FINT.curie('fylke'),
                   model_uri=ARK.fylke, domain=None, range=Optional[Union[str, FylkeId]])

slots.kommune = Slot(uri=FINT.kommune, name="kommune", curie=FINT.curie('kommune'),
                   model_uri=ARK.kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.kjonn = Slot(uri=FINT.kjonn, name="kjonn", curie=FINT.curie('kjonn'),
                   model_uri=ARK.kjonn, domain=None, range=Optional[Union[str, KjonnId]])

slots.bokstavkode = Slot(uri=FINT.bokstavkode, name="bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=ARK.bokstavkode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.valuta_navn = Slot(uri=FINT.valutaNavn, name="valuta_navn", curie=FINT.curie('valutaNavn'),
                   model_uri=ARK.valuta_navn, domain=None, range=Optional[str])

slots.nummerkode = Slot(uri=FINT.nummerkode, name="nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=ARK.nummerkode, domain=None, range=Optional[Union[dict, Identifikator]])

slots.bilde = Slot(uri=FINT.bilde, name="bilde", curie=FINT.curie('bilde'),
                   model_uri=ARK.bilde, domain=None, range=Optional[str])

slots.bostedsadresse = Slot(uri=FINT.bostedsadresse, name="bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=ARK.bostedsadresse, domain=None, range=Optional[Union[dict, Adresse]])

slots.fodselsdato = Slot(uri=FINT.fodselsdato, name="fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=ARK.fodselsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.fodselsnummer = Slot(uri=FINT.fodselsnummer, name="fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=ARK.fodselsnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person_navn = Slot(uri=FINT.personNavn, name="person_navn", curie=FINT.curie('personNavn'),
                   model_uri=ARK.person_navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.parorende = Slot(uri=FINT.parorende, name="parorende", curie=FINT.curie('parorende'),
                   model_uri=ARK.parorende, domain=None, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.statsborgerskap = Slot(uri=FINT.statsborgerskap, name="statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=ARK.statsborgerskap, domain=None, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.foreldreansvar = Slot(uri=FINT.foreldreansvar, name="foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=ARK.foreldreansvar, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.foreldre = Slot(uri=FINT.foreldre, name="foreldre", curie=FINT.curie('foreldre'),
                   model_uri=ARK.foreldre, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.maalform = Slot(uri=FINT.maalform, name="maalform", curie=FINT.curie('maalform'),
                   model_uri=ARK.maalform, domain=None, range=Optional[Union[str, SpraakId]])

slots.morsmaal = Slot(uri=FINT.morsmaal, name="morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=ARK.morsmaal, domain=None, range=Optional[Union[str, SpraakId]])

slots.laerling = Slot(uri=FINT.laerling, name="laerling", curie=FINT.curie('laerling'),
                   model_uri=ARK.laerling, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.elev = Slot(uri=FINT.elev, name="elev", curie=FINT.curie('elev'),
                   model_uri=ARK.elev, domain=None, range=Optional[Union[str, ElevId]])

slots.elevnummer = Slot(uri=FINT.elevnummer, name="elevnummer", curie=FINT.curie('elevnummer'),
                   model_uri=ARK.elevnummer, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person = Slot(uri=FINT.person, name="person", curie=FINT.curie('person'),
                   model_uri=ARK.person, domain=None, range=Optional[Union[str, PersonId]])

slots.otungdom = Slot(uri=FINT.otungdom, name="otungdom", curie=FINT.curie('otungdom'),
                   model_uri=ARK.otungdom, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.kontaktperson_navn = Slot(uri=FINT.kontaktpersonNavn, name="kontaktperson_navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=ARK.kontaktperson_navn, domain=None, range=Optional[Union[dict, Personnavn]])

slots.type = Slot(uri=FINT.type, name="type", curie=FINT.curie('type'),
                   model_uri=ARK.type, domain=None, range=Optional[str])

slots.kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=ARK.kontaktperson, domain=None, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.virksomhetsId = Slot(uri=FINT.virksomhetsId, name="virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=ARK.virksomhetsId, domain=None, range=Optional[Union[dict, Identifikator]])

slots.person__personalressurs = Slot(uri=FINT.personalressurs, name="person__personalressurs", curie=FINT.curie('personalressurs'),
                   model_uri=ARK.person__personalressurs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.ArkivContainer_klassifikasjonssystem = Slot(uri=ARK.klassifikasjonssystem, name="ArkivContainer_klassifikasjonssystem", curie=ARK.curie('klassifikasjonssystem'),
                   model_uri=ARK.ArkivContainer_klassifikasjonssystem, domain=ArkivContainer, range=Optional[Union[dict[Union[str, KlassifikasjonssystemId], Union[dict, "Klassifikasjonssystem"]], list[Union[dict, "Klassifikasjonssystem"]]]])

slots.Mappe_avsluttetDato = Slot(uri=ARK.avsluttetDato, name="Mappe_avsluttetDato", curie=ARK.curie('avsluttetDato'),
                   model_uri=ARK.Mappe_avsluttetDato, domain=Mappe, range=Optional[Union[str, XSDDateTime]])

slots.Mappe_beskrivelse = Slot(uri=FINT.beskrivelse, name="Mappe_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=ARK.Mappe_beskrivelse, domain=Mappe, range=Optional[str])

slots.Mappe_klasse = Slot(uri=ARK.klasse, name="Mappe_klasse", curie=ARK.curie('klasse'),
                   model_uri=ARK.Mappe_klasse, domain=Mappe, range=Optional[Union[Union[dict, "Klasse"], list[Union[dict, "Klasse"]]]])

slots.Mappe_mappeId = Slot(uri=ARK.mappeId, name="Mappe_mappeId", curie=ARK.curie('mappeId'),
                   model_uri=ARK.Mappe_mappeId, domain=Mappe, range=Optional[Union[dict, "Identifikator"]])

slots.Mappe_merknad = Slot(uri=ARK.merknad, name="Mappe_merknad", curie=ARK.curie('merknad'),
                   model_uri=ARK.Mappe_merknad, domain=Mappe, range=Optional[Union[Union[dict, "Merknad"], list[Union[dict, "Merknad"]]]])

slots.Mappe_noekkelord = Slot(uri=ARK.noekkelord, name="Mappe_noekkelord", curie=ARK.curie('noekkelord'),
                   model_uri=ARK.Mappe_noekkelord, domain=Mappe, range=Optional[Union[str, list[str]]])

slots.Mappe_offentligTittel = Slot(uri=ARK.offentligTittel, name="Mappe_offentligTittel", curie=ARK.curie('offentligTittel'),
                   model_uri=ARK.Mappe_offentligTittel, domain=Mappe, range=Optional[str])

slots.Mappe_opprettetDato = Slot(uri=ARK.opprettetDato, name="Mappe_opprettetDato", curie=ARK.curie('opprettetDato'),
                   model_uri=ARK.Mappe_opprettetDato, domain=Mappe, range=Optional[Union[str, XSDDateTime]])

slots.Mappe_part = Slot(uri=ARK.part, name="Mappe_part", curie=ARK.curie('part'),
                   model_uri=ARK.Mappe_part, domain=Mappe, range=Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]])

slots.Mappe_skjerming = Slot(uri=ARK.skjerming, name="Mappe_skjerming", curie=ARK.curie('skjerming'),
                   model_uri=ARK.Mappe_skjerming, domain=Mappe, range=Optional[Union[dict, "Skjerming"]])

slots.Mappe_tittel = Slot(uri=ARK.tittel, name="Mappe_tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.Mappe_tittel, domain=Mappe, range=Optional[str])

slots.Mappe_arkivdel = Slot(uri=ARK.arkivdel, name="Mappe_arkivdel", curie=ARK.curie('arkivdel'),
                   model_uri=ARK.Mappe_arkivdel, domain=Mappe, range=Optional[Union[str, ArkivdelId]])

slots.Mappe_avsluttetAv = Slot(uri=ARK.avsluttetAv, name="Mappe_avsluttetAv", curie=ARK.curie('avsluttetAv'),
                   model_uri=ARK.Mappe_avsluttetAv, domain=Mappe, range=Optional[Union[str, ArkivressursId]])

slots.Mappe_opprettetAv = Slot(uri=ARK.opprettetAv, name="Mappe_opprettetAv", curie=ARK.curie('opprettetAv'),
                   model_uri=ARK.Mappe_opprettetAv, domain=Mappe, range=Union[str, ArkivressursId])

slots.Saksmappe_journalpost = Slot(uri=ARK.journalpost, name="Saksmappe_journalpost", curie=ARK.curie('journalpost'),
                   model_uri=ARK.Saksmappe_journalpost, domain=Saksmappe, range=Optional[Union[Union[str, JournalpostId], list[Union[str, JournalpostId]]]])

slots.Saksmappe_saksaar = Slot(uri=ARK.saksaar, name="Saksmappe_saksaar", curie=ARK.curie('saksaar'),
                   model_uri=ARK.Saksmappe_saksaar, domain=Saksmappe, range=Optional[str])

slots.Saksmappe_saksdato = Slot(uri=ARK.saksdato, name="Saksmappe_saksdato", curie=ARK.curie('saksdato'),
                   model_uri=ARK.Saksmappe_saksdato, domain=Saksmappe, range=Optional[Union[str, XSDDateTime]])

slots.Saksmappe_sakssekvensnummer = Slot(uri=ARK.sakssekvensnummer, name="Saksmappe_sakssekvensnummer", curie=ARK.curie('sakssekvensnummer'),
                   model_uri=ARK.Saksmappe_sakssekvensnummer, domain=Saksmappe, range=Optional[str])

slots.Saksmappe_utlaantDato = Slot(uri=ARK.utlaantDato, name="Saksmappe_utlaantDato", curie=ARK.curie('utlaantDato'),
                   model_uri=ARK.Saksmappe_utlaantDato, domain=Saksmappe, range=Optional[Union[str, XSDDateTime]])

slots.Saksmappe_saksmappetype = Slot(uri=ARK.saksmappetype, name="Saksmappe_saksmappetype", curie=ARK.curie('saksmappetype'),
                   model_uri=ARK.Saksmappe_saksmappetype, domain=Saksmappe, range=Optional[Union[str, SaksmappetypeId]])

slots.Saksmappe_saksstatus = Slot(uri=ARK.saksstatus, name="Saksmappe_saksstatus", curie=ARK.curie('saksstatus'),
                   model_uri=ARK.Saksmappe_saksstatus, domain=Saksmappe, range=Union[str, SaksstatusId])

slots.Saksmappe_tilgangsgruppe = Slot(uri=ARK.tilgangsgruppe, name="Saksmappe_tilgangsgruppe", curie=ARK.curie('tilgangsgruppe'),
                   model_uri=ARK.Saksmappe_tilgangsgruppe, domain=Saksmappe, range=Optional[Union[str, TilgangsgruppeId]])

slots.Saksmappe_journalenhet = Slot(uri=ARK.journalenhet, name="Saksmappe_journalenhet", curie=ARK.curie('journalenhet'),
                   model_uri=ARK.Saksmappe_journalenhet, domain=Saksmappe, range=Optional[Union[str, AdministrativEnhetId]])

slots.Saksmappe_administrativEnhet = Slot(uri=ARK.administrativEnhet, name="Saksmappe_administrativEnhet", curie=ARK.curie('administrativEnhet'),
                   model_uri=ARK.Saksmappe_administrativEnhet, domain=Saksmappe, range=Union[str, AdministrativEnhetId])

slots.Saksmappe_saksansvarlig = Slot(uri=ARK.saksansvarlig, name="Saksmappe_saksansvarlig", curie=ARK.curie('saksansvarlig'),
                   model_uri=ARK.Saksmappe_saksansvarlig, domain=Saksmappe, range=Union[str, ArkivressursId])

slots.Registrering_arkivertDato = Slot(uri=ARK.arkivertDato, name="Registrering_arkivertDato", curie=ARK.curie('arkivertDato'),
                   model_uri=ARK.Registrering_arkivertDato, domain=Registrering, range=Optional[Union[str, XSDDateTime]])

slots.Registrering_beskrivelse = Slot(uri=FINT.beskrivelse, name="Registrering_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=ARK.Registrering_beskrivelse, domain=Registrering, range=Optional[str])

slots.Registrering_dokumentbeskrivelse = Slot(uri=ARK.dokumentbeskrivelse, name="Registrering_dokumentbeskrivelse", curie=ARK.curie('dokumentbeskrivelse'),
                   model_uri=ARK.Registrering_dokumentbeskrivelse, domain=Registrering, range=Optional[Union[Union[str, DokumentbeskrivelseId], list[Union[str, DokumentbeskrivelseId]]]])

slots.Registrering_forfatter = Slot(uri=ARK.forfatter, name="Registrering_forfatter", curie=ARK.curie('forfatter'),
                   model_uri=ARK.Registrering_forfatter, domain=Registrering, range=Optional[Union[str, list[str]]])

slots.Registrering_klasse = Slot(uri=ARK.klasse, name="Registrering_klasse", curie=ARK.curie('klasse'),
                   model_uri=ARK.Registrering_klasse, domain=Registrering, range=Optional[Union[dict, "Klasse"]])

slots.Registrering_korrespondansepart = Slot(uri=ARK.korrespondansepart, name="Registrering_korrespondansepart", curie=ARK.curie('korrespondansepart'),
                   model_uri=ARK.Registrering_korrespondansepart, domain=Registrering, range=Optional[Union[Union[dict, "Korrespondansepart"], list[Union[dict, "Korrespondansepart"]]]])

slots.Registrering_merknad = Slot(uri=ARK.merknad, name="Registrering_merknad", curie=ARK.curie('merknad'),
                   model_uri=ARK.Registrering_merknad, domain=Registrering, range=Optional[Union[Union[dict, "Merknad"], list[Union[dict, "Merknad"]]]])

slots.Registrering_nokkelord = Slot(uri=ARK.nokkelord, name="Registrering_nokkelord", curie=ARK.curie('nokkelord'),
                   model_uri=ARK.Registrering_nokkelord, domain=Registrering, range=Optional[Union[str, list[str]]])

slots.Registrering_offentligTittel = Slot(uri=ARK.offentligTittel, name="Registrering_offentligTittel", curie=ARK.curie('offentligTittel'),
                   model_uri=ARK.Registrering_offentligTittel, domain=Registrering, range=Optional[str])

slots.Registrering_opprettetDato = Slot(uri=ARK.opprettetDato, name="Registrering_opprettetDato", curie=ARK.curie('opprettetDato'),
                   model_uri=ARK.Registrering_opprettetDato, domain=Registrering, range=Optional[Union[str, XSDDateTime]])

slots.Registrering_part = Slot(uri=ARK.part, name="Registrering_part", curie=ARK.curie('part'),
                   model_uri=ARK.Registrering_part, domain=Registrering, range=Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]])

slots.Registrering_referanseArkivDel = Slot(uri=ARK.referanseArkivDel, name="Registrering_referanseArkivDel", curie=ARK.curie('referanseArkivDel'),
                   model_uri=ARK.Registrering_referanseArkivDel, domain=Registrering, range=Optional[Union[str, list[str]]])

slots.Registrering_registreringsId = Slot(uri=ARK.registreringsId, name="Registrering_registreringsId", curie=ARK.curie('registreringsId'),
                   model_uri=ARK.Registrering_registreringsId, domain=Registrering, range=Optional[str])

slots.Registrering_skjerming = Slot(uri=ARK.skjerming, name="Registrering_skjerming", curie=ARK.curie('skjerming'),
                   model_uri=ARK.Registrering_skjerming, domain=Registrering, range=Optional[Union[dict, "Skjerming"]])

slots.Registrering_tittel = Slot(uri=ARK.tittel, name="Registrering_tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.Registrering_tittel, domain=Registrering, range=str)

slots.Registrering_tilgangsgruppe = Slot(uri=ARK.tilgangsgruppe, name="Registrering_tilgangsgruppe", curie=ARK.curie('tilgangsgruppe'),
                   model_uri=ARK.Registrering_tilgangsgruppe, domain=Registrering, range=Optional[Union[str, TilgangsgruppeId]])

slots.Registrering_administrativEnhet = Slot(uri=ARK.administrativEnhet, name="Registrering_administrativEnhet", curie=ARK.curie('administrativEnhet'),
                   model_uri=ARK.Registrering_administrativEnhet, domain=Registrering, range=Optional[Union[str, AdministrativEnhetId]])

slots.Registrering_arkivdel = Slot(uri=ARK.arkivdel, name="Registrering_arkivdel", curie=ARK.curie('arkivdel'),
                   model_uri=ARK.Registrering_arkivdel, domain=Registrering, range=Optional[Union[str, ArkivdelId]])

slots.Registrering_saksbehandler = Slot(uri=ARK.saksbehandler, name="Registrering_saksbehandler", curie=ARK.curie('saksbehandler'),
                   model_uri=ARK.Registrering_saksbehandler, domain=Registrering, range=Optional[Union[str, ArkivressursId]])

slots.Registrering_arkivertAv = Slot(uri=ARK.arkivertAv, name="Registrering_arkivertAv", curie=ARK.curie('arkivertAv'),
                   model_uri=ARK.Registrering_arkivertAv, domain=Registrering, range=Union[str, ArkivressursId])

slots.Registrering_opprettetAv = Slot(uri=ARK.opprettetAv, name="Registrering_opprettetAv", curie=ARK.curie('opprettetAv'),
                   model_uri=ARK.Registrering_opprettetAv, domain=Registrering, range=Union[str, ArkivressursId])

slots.AdministrativEnhet_navn = Slot(uri=FINT.navn, name="AdministrativEnhet_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.AdministrativEnhet_navn, domain=AdministrativEnhet, range=str)

slots.AdministrativEnhet_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="AdministrativEnhet_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.AdministrativEnhet_gyldighetsperiode, domain=AdministrativEnhet, range=Optional[Union[dict, "Periode"]])

slots.AdministrativEnhet_organisasjonselement = Slot(uri=ARK.organisasjonselement, name="AdministrativEnhet_organisasjonselement", curie=ARK.curie('organisasjonselement'),
                   model_uri=ARK.AdministrativEnhet_organisasjonselement, domain=AdministrativEnhet, range=Optional[Union[str, URIorCURIE]])

slots.Arkivdel_tittel = Slot(uri=ARK.tittel, name="Arkivdel_tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.Arkivdel_tittel, domain=Arkivdel, range=str)

slots.Arkivdel_klassifikasjonssystem = Slot(uri=ARK.klassifikasjonssystem, name="Arkivdel_klassifikasjonssystem", curie=ARK.curie('klassifikasjonssystem'),
                   model_uri=ARK.Arkivdel_klassifikasjonssystem, domain=Arkivdel, range=Optional[Union[Union[str, KlassifikasjonssystemId], list[Union[str, KlassifikasjonssystemId]]]])

slots.Arkivressurs_kildesystemId = Slot(uri=ARK.kildesystemId, name="Arkivressurs_kildesystemId", curie=ARK.curie('kildesystemId'),
                   model_uri=ARK.Arkivressurs_kildesystemId, domain=Arkivressurs, range=Optional[Union[dict, "Identifikator"]])

slots.Arkivressurs_personalressurs = Slot(uri=ARK.personalressurs, name="Arkivressurs_personalressurs", curie=ARK.curie('personalressurs'),
                   model_uri=ARK.Arkivressurs_personalressurs, domain=Arkivressurs, range=Union[str, URIorCURIE])

slots.Arkivressurs_autorisasjon = Slot(uri=ARK.autorisasjon, name="Arkivressurs_autorisasjon", curie=ARK.curie('autorisasjon'),
                   model_uri=ARK.Arkivressurs_autorisasjon, domain=Arkivressurs, range=Optional[Union[Union[str, AutorisasjonId], list[Union[str, AutorisasjonId]]]])

slots.Arkivressurs_tilgang = Slot(uri=ARK.tilgang, name="Arkivressurs_tilgang", curie=ARK.curie('tilgang'),
                   model_uri=ARK.Arkivressurs_tilgang, domain=Arkivressurs, range=Optional[Union[Union[str, TilgangId], list[Union[str, TilgangId]]]])

slots.Autorisasjon_tilgangsrestriksjon = Slot(uri=ARK.tilgangsrestriksjon, name="Autorisasjon_tilgangsrestriksjon", curie=ARK.curie('tilgangsrestriksjon'),
                   model_uri=ARK.Autorisasjon_tilgangsrestriksjon, domain=Autorisasjon, range=Union[Union[str, TilgangsrestriksjonId], list[Union[str, TilgangsrestriksjonId]]])

slots.Autorisasjon_administrativenhet = Slot(uri=ARK.administrativenhet, name="Autorisasjon_administrativenhet", curie=ARK.curie('administrativenhet'),
                   model_uri=ARK.Autorisasjon_administrativenhet, domain=Autorisasjon, range=Optional[Union[Union[str, AdministrativEnhetId], list[Union[str, AdministrativEnhetId]]]])

slots.Autorisasjon_arkivressurs = Slot(uri=ARK.arkivressurs, name="Autorisasjon_arkivressurs", curie=ARK.curie('arkivressurs'),
                   model_uri=ARK.Autorisasjon_arkivressurs, domain=Autorisasjon, range=Optional[Union[Union[str, ArkivressursId], list[Union[str, ArkivressursId]]]])

slots.Dokumentfil_data = Slot(uri=ARK.data, name="Dokumentfil_data", curie=ARK.curie('data'),
                   model_uri=ARK.Dokumentfil_data, domain=Dokumentfil, range=str)

slots.Dokumentfil_filnavn = Slot(uri=ARK.filnavn, name="Dokumentfil_filnavn", curie=ARK.curie('filnavn'),
                   model_uri=ARK.Dokumentfil_filnavn, domain=Dokumentfil, range=Optional[str])

slots.Dokumentfil_format = Slot(uri=ARK.format, name="Dokumentfil_format", curie=ARK.curie('format'),
                   model_uri=ARK.Dokumentfil_format, domain=Dokumentfil, range=str)

slots.Journalpost_antallVedlegg = Slot(uri=ARK.antallVedlegg, name="Journalpost_antallVedlegg", curie=ARK.curie('antallVedlegg'),
                   model_uri=ARK.Journalpost_antallVedlegg, domain=Journalpost, range=Optional[int])

slots.Journalpost_avskrivning = Slot(uri=ARK.avskrivning, name="Journalpost_avskrivning", curie=ARK.curie('avskrivning'),
                   model_uri=ARK.Journalpost_avskrivning, domain=Journalpost, range=Optional[Union[dict, "Avskrivning"]])

slots.Journalpost_dokumentetsDato = Slot(uri=ARK.dokumentetsDato, name="Journalpost_dokumentetsDato", curie=ARK.curie('dokumentetsDato'),
                   model_uri=ARK.Journalpost_dokumentetsDato, domain=Journalpost, range=Optional[Union[str, XSDDateTime]])

slots.Journalpost_forfallsDato = Slot(uri=ARK.forfallsDato, name="Journalpost_forfallsDato", curie=ARK.curie('forfallsDato'),
                   model_uri=ARK.Journalpost_forfallsDato, domain=Journalpost, range=Optional[Union[str, XSDDateTime]])

slots.Journalpost_journalAr = Slot(uri=ARK.journalAr, name="Journalpost_journalAr", curie=ARK.curie('journalAr'),
                   model_uri=ARK.Journalpost_journalAr, domain=Journalpost, range=Optional[str])

slots.Journalpost_journalDato = Slot(uri=ARK.journalDato, name="Journalpost_journalDato", curie=ARK.curie('journalDato'),
                   model_uri=ARK.Journalpost_journalDato, domain=Journalpost, range=Optional[Union[str, XSDDateTime]])

slots.Journalpost_journalPostnummer = Slot(uri=ARK.journalPostnummer, name="Journalpost_journalPostnummer", curie=ARK.curie('journalPostnummer'),
                   model_uri=ARK.Journalpost_journalPostnummer, domain=Journalpost, range=Optional[int])

slots.Journalpost_journalSekvensnummer = Slot(uri=ARK.journalSekvensnummer, name="Journalpost_journalSekvensnummer", curie=ARK.curie('journalSekvensnummer'),
                   model_uri=ARK.Journalpost_journalSekvensnummer, domain=Journalpost, range=Optional[int])

slots.Journalpost_mottattDato = Slot(uri=ARK.mottattDato, name="Journalpost_mottattDato", curie=ARK.curie('mottattDato'),
                   model_uri=ARK.Journalpost_mottattDato, domain=Journalpost, range=Optional[Union[str, XSDDateTime]])

slots.Journalpost_offentlighetsvurdertDato = Slot(uri=ARK.offentlighetsvurdertDato, name="Journalpost_offentlighetsvurdertDato", curie=ARK.curie('offentlighetsvurdertDato'),
                   model_uri=ARK.Journalpost_offentlighetsvurdertDato, domain=Journalpost, range=Optional[Union[str, XSDDateTime]])

slots.Journalpost_sendtDato = Slot(uri=ARK.sendtDato, name="Journalpost_sendtDato", curie=ARK.curie('sendtDato'),
                   model_uri=ARK.Journalpost_sendtDato, domain=Journalpost, range=Optional[Union[str, XSDDateTime]])

slots.Journalpost_journalposttype = Slot(uri=ARK.journalposttype, name="Journalpost_journalposttype", curie=ARK.curie('journalposttype'),
                   model_uri=ARK.Journalpost_journalposttype, domain=Journalpost, range=Union[str, JournalpostTypeId])

slots.Journalpost_journalstatus = Slot(uri=ARK.journalstatus, name="Journalpost_journalstatus", curie=ARK.curie('journalstatus'),
                   model_uri=ARK.Journalpost_journalstatus, domain=Journalpost, range=Union[str, JournalStatusId])

slots.Journalpost_journalenhet = Slot(uri=ARK.journalenhet, name="Journalpost_journalenhet", curie=ARK.curie('journalenhet'),
                   model_uri=ARK.Journalpost_journalenhet, domain=Journalpost, range=Optional[Union[str, AdministrativEnhetId]])

slots.Klassifikasjonssystem_avsluttetAvNavn = Slot(uri=ARK.avsluttetAvNavn, name="Klassifikasjonssystem_avsluttetAvNavn", curie=ARK.curie('avsluttetAvNavn'),
                   model_uri=ARK.Klassifikasjonssystem_avsluttetAvNavn, domain=Klassifikasjonssystem, range=Optional[str])

slots.Klassifikasjonssystem_avsluttetDato = Slot(uri=ARK.avsluttetDato, name="Klassifikasjonssystem_avsluttetDato", curie=ARK.curie('avsluttetDato'),
                   model_uri=ARK.Klassifikasjonssystem_avsluttetDato, domain=Klassifikasjonssystem, range=Optional[Union[str, XSDDateTime]])

slots.Klassifikasjonssystem_beskrivelse = Slot(uri=FINT.beskrivelse, name="Klassifikasjonssystem_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=ARK.Klassifikasjonssystem_beskrivelse, domain=Klassifikasjonssystem, range=Optional[str])

slots.Klassifikasjonssystem_klasse = Slot(uri=ARK.klasse, name="Klassifikasjonssystem_klasse", curie=ARK.curie('klasse'),
                   model_uri=ARK.Klassifikasjonssystem_klasse, domain=Klassifikasjonssystem, range=Union[Union[dict, "Klasse"], list[Union[dict, "Klasse"]]])

slots.Klassifikasjonssystem_opprettetAvNavn = Slot(uri=ARK.opprettetAvNavn, name="Klassifikasjonssystem_opprettetAvNavn", curie=ARK.curie('opprettetAvNavn'),
                   model_uri=ARK.Klassifikasjonssystem_opprettetAvNavn, domain=Klassifikasjonssystem, range=str)

slots.Klassifikasjonssystem_opprettetDato = Slot(uri=ARK.opprettetDato, name="Klassifikasjonssystem_opprettetDato", curie=ARK.curie('opprettetDato'),
                   model_uri=ARK.Klassifikasjonssystem_opprettetDato, domain=Klassifikasjonssystem, range=Union[str, XSDDateTime])

slots.Klassifikasjonssystem_tittel = Slot(uri=ARK.tittel, name="Klassifikasjonssystem_tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.Klassifikasjonssystem_tittel, domain=Klassifikasjonssystem, range=str)

slots.Klassifikasjonssystem_klassifikasjonstype = Slot(uri=ARK.klassifikasjonstype, name="Klassifikasjonssystem_klassifikasjonstype", curie=ARK.curie('klassifikasjonstype'),
                   model_uri=ARK.Klassifikasjonssystem_klassifikasjonstype, domain=Klassifikasjonssystem, range=Optional[Union[str, KlassifikasjonstypeId]])

slots.Klassifikasjonssystem_arkivdel = Slot(uri=ARK.arkivdel, name="Klassifikasjonssystem_arkivdel", curie=ARK.curie('arkivdel'),
                   model_uri=ARK.Klassifikasjonssystem_arkivdel, domain=Klassifikasjonssystem, range=Union[Union[str, ArkivdelId], list[Union[str, ArkivdelId]]])

slots.Tilgang_tittel = Slot(uri=ARK.tittel, name="Tilgang_tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.Tilgang_tittel, domain=Tilgang, range=str)

slots.Tilgang_rolle = Slot(uri=ARK.rolle, name="Tilgang_rolle", curie=ARK.curie('rolle'),
                   model_uri=ARK.Tilgang_rolle, domain=Tilgang, range=Union[str, RolleId])

slots.Tilgang_administrativEnhet = Slot(uri=ARK.administrativEnhet, name="Tilgang_administrativEnhet", curie=ARK.curie('administrativEnhet'),
                   model_uri=ARK.Tilgang_administrativEnhet, domain=Tilgang, range=Optional[Union[str, AdministrativEnhetId]])

slots.Tilgang_arkivdel = Slot(uri=ARK.arkivdel, name="Tilgang_arkivdel", curie=ARK.curie('arkivdel'),
                   model_uri=ARK.Tilgang_arkivdel, domain=Tilgang, range=Optional[Union[str, ArkivdelId]])

slots.Tilgang_arkivressurs = Slot(uri=ARK.arkivressurs, name="Tilgang_arkivressurs", curie=ARK.curie('arkivressurs'),
                   model_uri=ARK.Tilgang_arkivressurs, domain=Tilgang, range=Optional[Union[Union[str, ArkivressursId], list[Union[str, ArkivressursId]]]])

slots.Personalmappe_personnavn = Slot(uri=ARK.personnavn, name="Personalmappe_personnavn", curie=ARK.curie('personnavn'),
                   model_uri=ARK.Personalmappe_personnavn, domain=Personalmappe, range=Union[dict, "Personnavn"])

slots.Personalmappe_person = Slot(uri=FINT.person, name="Personalmappe_person", curie=FINT.curie('person'),
                   model_uri=ARK.Personalmappe_person, domain=Personalmappe, range=Union[str, PersonId])

slots.Personalmappe_leder = Slot(uri=ARK.leder, name="Personalmappe_leder", curie=ARK.curie('leder'),
                   model_uri=ARK.Personalmappe_leder, domain=Personalmappe, range=Union[str, URIorCURIE])

slots.Personalmappe_arbeidssted = Slot(uri=ARK.arbeidssted, name="Personalmappe_arbeidssted", curie=ARK.curie('arbeidssted'),
                   model_uri=ARK.Personalmappe_arbeidssted, domain=Personalmappe, range=Union[str, URIorCURIE])

slots.Personalmappe_personalressurs = Slot(uri=ARK.personalressurs, name="Personalmappe_personalressurs", curie=ARK.curie('personalressurs'),
                   model_uri=ARK.Personalmappe_personalressurs, domain=Personalmappe, range=Union[str, URIorCURIE])

slots.DispensasjonAutomatiskFredaKulturminne_kulturminneId = Slot(uri=ARK.kulturminneId, name="DispensasjonAutomatiskFredaKulturminne_kulturminneId", curie=ARK.curie('kulturminneId'),
                   model_uri=ARK.DispensasjonAutomatiskFredaKulturminne_kulturminneId, domain=DispensasjonAutomatiskFredaKulturminne, range=str)

slots.DispensasjonAutomatiskFredaKulturminne_matrikkelnummer = Slot(uri=ARK.matrikkelnummer, name="DispensasjonAutomatiskFredaKulturminne_matrikkelnummer", curie=ARK.curie('matrikkelnummer'),
                   model_uri=ARK.DispensasjonAutomatiskFredaKulturminne_matrikkelnummer, domain=DispensasjonAutomatiskFredaKulturminne, range=Union[dict, "Matrikkelnummer"])

slots.DispensasjonAutomatiskFredaKulturminne_soeknadsnummer = Slot(uri=ARK.soeknadsnummer, name="DispensasjonAutomatiskFredaKulturminne_soeknadsnummer", curie=ARK.curie('soeknadsnummer'),
                   model_uri=ARK.DispensasjonAutomatiskFredaKulturminne_soeknadsnummer, domain=DispensasjonAutomatiskFredaKulturminne, range=Union[dict, "Identifikator"])

slots.DispensasjonAutomatiskFredaKulturminne_tiltak = Slot(uri=ARK.tiltak, name="DispensasjonAutomatiskFredaKulturminne_tiltak", curie=ARK.curie('tiltak'),
                   model_uri=ARK.DispensasjonAutomatiskFredaKulturminne_tiltak, domain=DispensasjonAutomatiskFredaKulturminne, range=Optional[str])

slots.TilskuddFartoy_fartoyNavn = Slot(uri=ARK.fartoyNavn, name="TilskuddFartoy_fartoyNavn", curie=ARK.curie('fartoyNavn'),
                   model_uri=ARK.TilskuddFartoy_fartoyNavn, domain=TilskuddFartoy, range=str)

slots.TilskuddFartoy_kallesignal = Slot(uri=ARK.kallesignal, name="TilskuddFartoy_kallesignal", curie=ARK.curie('kallesignal'),
                   model_uri=ARK.TilskuddFartoy_kallesignal, domain=TilskuddFartoy, range=str)

slots.TilskuddFartoy_kulturminneId = Slot(uri=ARK.kulturminneId, name="TilskuddFartoy_kulturminneId", curie=ARK.curie('kulturminneId'),
                   model_uri=ARK.TilskuddFartoy_kulturminneId, domain=TilskuddFartoy, range=str)

slots.TilskuddFartoy_soeknadsnummer = Slot(uri=ARK.soeknadsnummer, name="TilskuddFartoy_soeknadsnummer", curie=ARK.curie('soeknadsnummer'),
                   model_uri=ARK.TilskuddFartoy_soeknadsnummer, domain=TilskuddFartoy, range=Union[dict, "Identifikator"])

slots.TilskuddFredaBygningPrivatEie_bygningsnavn = Slot(uri=ARK.bygningsnavn, name="TilskuddFredaBygningPrivatEie_bygningsnavn", curie=ARK.curie('bygningsnavn'),
                   model_uri=ARK.TilskuddFredaBygningPrivatEie_bygningsnavn, domain=TilskuddFredaBygningPrivatEie, range=Optional[str])

slots.TilskuddFredaBygningPrivatEie_kulturminneId = Slot(uri=ARK.kulturminneId, name="TilskuddFredaBygningPrivatEie_kulturminneId", curie=ARK.curie('kulturminneId'),
                   model_uri=ARK.TilskuddFredaBygningPrivatEie_kulturminneId, domain=TilskuddFredaBygningPrivatEie, range=str)

slots.TilskuddFredaBygningPrivatEie_matrikkelnummer = Slot(uri=ARK.matrikkelnummer, name="TilskuddFredaBygningPrivatEie_matrikkelnummer", curie=ARK.curie('matrikkelnummer'),
                   model_uri=ARK.TilskuddFredaBygningPrivatEie_matrikkelnummer, domain=TilskuddFredaBygningPrivatEie, range=Optional[Union[dict, "Matrikkelnummer"]])

slots.TilskuddFredaBygningPrivatEie_soeknadsnummer = Slot(uri=ARK.soeknadsnummer, name="TilskuddFredaBygningPrivatEie_soeknadsnummer", curie=ARK.curie('soeknadsnummer'),
                   model_uri=ARK.TilskuddFredaBygningPrivatEie_soeknadsnummer, domain=TilskuddFredaBygningPrivatEie, range=Optional[Union[dict, "Identifikator"]])

slots.SoeknadDrosjeloeyve_organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="SoeknadDrosjeloeyve_organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=ARK.SoeknadDrosjeloeyve_organisasjonsnavn, domain=SoeknadDrosjeloeyve, range=str)

slots.SoeknadDrosjeloeyve_orgnummer = Slot(uri=ARK.organisasjonsnummer, name="SoeknadDrosjeloeyve_orgnummer", curie=ARK.curie('organisasjonsnummer'),
                   model_uri=ARK.SoeknadDrosjeloeyve_orgnummer, domain=SoeknadDrosjeloeyve, range=str)

slots.Avskrivning_avskrevetAv = Slot(uri=ARK.avskrevetAv, name="Avskrivning_avskrevetAv", curie=ARK.curie('avskrevetAv'),
                   model_uri=ARK.Avskrivning_avskrevetAv, domain=Avskrivning, range=str)

slots.Avskrivning_avskrivningsdato = Slot(uri=ARK.avskrivningsdato, name="Avskrivning_avskrivningsdato", curie=ARK.curie('avskrivningsdato'),
                   model_uri=ARK.Avskrivning_avskrivningsdato, domain=Avskrivning, range=Union[str, XSDDateTime])

slots.Avskrivning_avskrivningsmate = Slot(uri=ARK.avskrivningsmate, name="Avskrivning_avskrivningsmate", curie=ARK.curie('avskrivningsmate'),
                   model_uri=ARK.Avskrivning_avskrivningsmate, domain=Avskrivning, range=str)

slots.Dokumentbeskrivelse_beskrivelse = Slot(uri=FINT.beskrivelse, name="Dokumentbeskrivelse_beskrivelse", curie=FINT.curie('beskrivelse'),
                   model_uri=ARK.Dokumentbeskrivelse_beskrivelse, domain=Dokumentbeskrivelse, range=Optional[str])

slots.Dokumentbeskrivelse_dokumentnummer = Slot(uri=ARK.dokumentnummer, name="Dokumentbeskrivelse_dokumentnummer", curie=ARK.curie('dokumentnummer'),
                   model_uri=ARK.Dokumentbeskrivelse_dokumentnummer, domain=Dokumentbeskrivelse, range=Optional[int])

slots.Dokumentbeskrivelse_dokumentobjekt = Slot(uri=ARK.dokumentobjekt, name="Dokumentbeskrivelse_dokumentobjekt", curie=ARK.curie('dokumentobjekt'),
                   model_uri=ARK.Dokumentbeskrivelse_dokumentobjekt, domain=Dokumentbeskrivelse, range=Optional[Union[Union[dict, "Dokumentobjekt"], list[Union[dict, "Dokumentobjekt"]]]])

slots.Dokumentbeskrivelse_forfatter = Slot(uri=ARK.forfatter, name="Dokumentbeskrivelse_forfatter", curie=ARK.curie('forfatter'),
                   model_uri=ARK.Dokumentbeskrivelse_forfatter, domain=Dokumentbeskrivelse, range=Optional[Union[str, list[str]]])

slots.Dokumentbeskrivelse_opprettetDato = Slot(uri=ARK.opprettetDato, name="Dokumentbeskrivelse_opprettetDato", curie=ARK.curie('opprettetDato'),
                   model_uri=ARK.Dokumentbeskrivelse_opprettetDato, domain=Dokumentbeskrivelse, range=Optional[Union[str, XSDDateTime]])

slots.Dokumentbeskrivelse_part = Slot(uri=ARK.part, name="Dokumentbeskrivelse_part", curie=ARK.curie('part'),
                   model_uri=ARK.Dokumentbeskrivelse_part, domain=Dokumentbeskrivelse, range=Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]])

slots.Dokumentbeskrivelse_referanseArkivdel = Slot(uri=ARK.referanseArkivdel, name="Dokumentbeskrivelse_referanseArkivdel", curie=ARK.curie('referanseArkivdel'),
                   model_uri=ARK.Dokumentbeskrivelse_referanseArkivdel, domain=Dokumentbeskrivelse, range=Optional[Union[str, list[str]]])

slots.Dokumentbeskrivelse_skjerming = Slot(uri=ARK.skjerming, name="Dokumentbeskrivelse_skjerming", curie=ARK.curie('skjerming'),
                   model_uri=ARK.Dokumentbeskrivelse_skjerming, domain=Dokumentbeskrivelse, range=Optional[Union[dict, "Skjerming"]])

slots.Dokumentbeskrivelse_tilknyttetDato = Slot(uri=ARK.tilknyttetDato, name="Dokumentbeskrivelse_tilknyttetDato", curie=ARK.curie('tilknyttetDato'),
                   model_uri=ARK.Dokumentbeskrivelse_tilknyttetDato, domain=Dokumentbeskrivelse, range=Optional[Union[str, XSDDateTime]])

slots.Dokumentbeskrivelse_tittel = Slot(uri=ARK.tittel, name="Dokumentbeskrivelse_tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.Dokumentbeskrivelse_tittel, domain=Dokumentbeskrivelse, range=str)

slots.Dokumentbeskrivelse_dokumentstatus = Slot(uri=ARK.dokumentstatus, name="Dokumentbeskrivelse_dokumentstatus", curie=ARK.curie('dokumentstatus'),
                   model_uri=ARK.Dokumentbeskrivelse_dokumentstatus, domain=Dokumentbeskrivelse, range=Union[str, DokumentStatusId])

slots.Dokumentbeskrivelse_dokumentType = Slot(uri=ARK.dokumentType, name="Dokumentbeskrivelse_dokumentType", curie=ARK.curie('dokumentType'),
                   model_uri=ARK.Dokumentbeskrivelse_dokumentType, domain=Dokumentbeskrivelse, range=Union[str, DokumentTypeId])

slots.Dokumentbeskrivelse_tilknyttetRegistreringSom = Slot(uri=ARK.tilknyttetRegistreringSom, name="Dokumentbeskrivelse_tilknyttetRegistreringSom", curie=ARK.curie('tilknyttetRegistreringSom'),
                   model_uri=ARK.Dokumentbeskrivelse_tilknyttetRegistreringSom, domain=Dokumentbeskrivelse, range=Union[Union[str, TilknyttetRegistreringSomId], list[Union[str, TilknyttetRegistreringSomId]]])

slots.Dokumentbeskrivelse_tilknyttetAv = Slot(uri=ARK.tilknyttetAv, name="Dokumentbeskrivelse_tilknyttetAv", curie=ARK.curie('tilknyttetAv'),
                   model_uri=ARK.Dokumentbeskrivelse_tilknyttetAv, domain=Dokumentbeskrivelse, range=Union[str, ArkivressursId])

slots.Dokumentbeskrivelse_opprettetAv = Slot(uri=ARK.opprettetAv, name="Dokumentbeskrivelse_opprettetAv", curie=ARK.curie('opprettetAv'),
                   model_uri=ARK.Dokumentbeskrivelse_opprettetAv, domain=Dokumentbeskrivelse, range=Union[str, ArkivressursId])

slots.Dokumentobjekt_filstorrelse = Slot(uri=ARK.filstorrelse, name="Dokumentobjekt_filstorrelse", curie=ARK.curie('filstorrelse'),
                   model_uri=ARK.Dokumentobjekt_filstorrelse, domain=Dokumentobjekt, range=Optional[str])

slots.Dokumentobjekt_formatDetaljer = Slot(uri=ARK.formatDetaljer, name="Dokumentobjekt_formatDetaljer", curie=ARK.curie('formatDetaljer'),
                   model_uri=ARK.Dokumentobjekt_formatDetaljer, domain=Dokumentobjekt, range=Optional[str])

slots.Dokumentobjekt_sjekksum = Slot(uri=ARK.sjekksum, name="Dokumentobjekt_sjekksum", curie=ARK.curie('sjekksum'),
                   model_uri=ARK.Dokumentobjekt_sjekksum, domain=Dokumentobjekt, range=Optional[str])

slots.Dokumentobjekt_sjekksumAlgoritme = Slot(uri=ARK.sjekksumAlgoritme, name="Dokumentobjekt_sjekksumAlgoritme", curie=ARK.curie('sjekksumAlgoritme'),
                   model_uri=ARK.Dokumentobjekt_sjekksumAlgoritme, domain=Dokumentobjekt, range=Optional[str])

slots.Dokumentobjekt_versjonsnummer = Slot(uri=ARK.versjonsnummer, name="Dokumentobjekt_versjonsnummer", curie=ARK.curie('versjonsnummer'),
                   model_uri=ARK.Dokumentobjekt_versjonsnummer, domain=Dokumentobjekt, range=Optional[int])

slots.Dokumentobjekt_filformat = Slot(uri=ARK.filformat, name="Dokumentobjekt_filformat", curie=ARK.curie('filformat'),
                   model_uri=ARK.Dokumentobjekt_filformat, domain=Dokumentobjekt, range=Optional[Union[str, FormatId]])

slots.Dokumentobjekt_variantFormat = Slot(uri=ARK.variantFormat, name="Dokumentobjekt_variantFormat", curie=ARK.curie('variantFormat'),
                   model_uri=ARK.Dokumentobjekt_variantFormat, domain=Dokumentobjekt, range=Union[str, VariantformatId])

slots.Dokumentobjekt_opprettetAv = Slot(uri=ARK.opprettetAv, name="Dokumentobjekt_opprettetAv", curie=ARK.curie('opprettetAv'),
                   model_uri=ARK.Dokumentobjekt_opprettetAv, domain=Dokumentobjekt, range=Union[str, ArkivressursId])

slots.Dokumentobjekt_referanseDokumentfil = Slot(uri=ARK.referanseDokumentfil, name="Dokumentobjekt_referanseDokumentfil", curie=ARK.curie('referanseDokumentfil'),
                   model_uri=ARK.Dokumentobjekt_referanseDokumentfil, domain=Dokumentobjekt, range=Optional[Union[str, DokumentfilId]])

slots.Klasse_klasseId = Slot(uri=ARK.klasseId, name="Klasse_klasseId", curie=ARK.curie('klasseId'),
                   model_uri=ARK.Klasse_klasseId, domain=Klasse, range=str)

slots.Klasse_rekkefoelge = Slot(uri=ARK.rekkefolge, name="Klasse_rekkefoelge", curie=ARK.curie('rekkefolge'),
                   model_uri=ARK.Klasse_rekkefoelge, domain=Klasse, range=Optional[int])

slots.Klasse_skjerming = Slot(uri=ARK.skjerming, name="Klasse_skjerming", curie=ARK.curie('skjerming'),
                   model_uri=ARK.Klasse_skjerming, domain=Klasse, range=Optional[Union[dict, "Skjerming"]])

slots.Klasse_tittel = Slot(uri=ARK.tittel, name="Klasse_tittel", curie=ARK.curie('tittel'),
                   model_uri=ARK.Klasse_tittel, domain=Klasse, range=str)

slots.Klasse_klassifikasjonssystem = Slot(uri=ARK.klassifikasjonssystem, name="Klasse_klassifikasjonssystem", curie=ARK.curie('klassifikasjonssystem'),
                   model_uri=ARK.Klasse_klassifikasjonssystem, domain=Klasse, range=Union[str, KlassifikasjonssystemId])

slots.Korrespondansepart_adresse = Slot(uri=FINT.adresse, name="Korrespondansepart_adresse", curie=FINT.curie('adresse'),
                   model_uri=ARK.Korrespondansepart_adresse, domain=Korrespondansepart, range=Optional[Union[dict, "Adresse"]])

slots.Korrespondansepart_foedselsnummer = Slot(uri=ARK.foedselsnummer, name="Korrespondansepart_foedselsnummer", curie=ARK.curie('foedselsnummer'),
                   model_uri=ARK.Korrespondansepart_foedselsnummer, domain=Korrespondansepart, range=Optional[str])

slots.Korrespondansepart_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Korrespondansepart_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ARK.Korrespondansepart_kontaktinformasjon, domain=Korrespondansepart, range=Optional[Union[dict, "Kontaktinformasjon"]])

slots.Korrespondansepart_kontaktperson_str = Slot(uri=ARK.kontaktperson, name="Korrespondansepart_kontaktperson_str", curie=ARK.curie('kontaktperson'),
                   model_uri=ARK.Korrespondansepart_kontaktperson_str, domain=Korrespondansepart, range=Optional[str])

slots.Korrespondansepart_korrespondansepartNavn = Slot(uri=ARK.korrespondansepartNavn, name="Korrespondansepart_korrespondansepartNavn", curie=ARK.curie('korrespondansepartNavn'),
                   model_uri=ARK.Korrespondansepart_korrespondansepartNavn, domain=Korrespondansepart, range=Optional[str])

slots.Korrespondansepart_orgnummer = Slot(uri=ARK.organisasjonsnummer, name="Korrespondansepart_orgnummer", curie=ARK.curie('organisasjonsnummer'),
                   model_uri=ARK.Korrespondansepart_orgnummer, domain=Korrespondansepart, range=Optional[str])

slots.Korrespondansepart_skjerming = Slot(uri=ARK.skjerming, name="Korrespondansepart_skjerming", curie=ARK.curie('skjerming'),
                   model_uri=ARK.Korrespondansepart_skjerming, domain=Korrespondansepart, range=Optional[Union[dict, "Skjerming"]])

slots.Korrespondansepart_korrespondanseparttype = Slot(uri=ARK.korrespondanseparttype, name="Korrespondansepart_korrespondanseparttype", curie=ARK.curie('korrespondanseparttype'),
                   model_uri=ARK.Korrespondansepart_korrespondanseparttype, domain=Korrespondansepart, range=Union[str, KorrespondansepartTypeId])

slots.Merknad_merknadsdato = Slot(uri=ARK.merknadsdato, name="Merknad_merknadsdato", curie=ARK.curie('merknadsdato'),
                   model_uri=ARK.Merknad_merknadsdato, domain=Merknad, range=Union[str, XSDDateTime])

slots.Merknad_merknadstekst = Slot(uri=ARK.merknadstekst, name="Merknad_merknadstekst", curie=ARK.curie('merknadstekst'),
                   model_uri=ARK.Merknad_merknadstekst, domain=Merknad, range=str)

slots.Merknad_merknadstype = Slot(uri=ARK.merknadstype, name="Merknad_merknadstype", curie=ARK.curie('merknadstype'),
                   model_uri=ARK.Merknad_merknadstype, domain=Merknad, range=Union[str, MerknadstypeId])

slots.Merknad_merknadRegistrertAv = Slot(uri=ARK.merknadRegistrertAv, name="Merknad_merknadRegistrertAv", curie=ARK.curie('merknadRegistrertAv'),
                   model_uri=ARK.Merknad_merknadRegistrertAv, domain=Merknad, range=Union[str, ArkivressursId])

slots.Part_adresse = Slot(uri=FINT.adresse, name="Part_adresse", curie=FINT.curie('adresse'),
                   model_uri=ARK.Part_adresse, domain=Part, range=Optional[Union[dict, "Adresse"]])

slots.Part_foedselsnummer = Slot(uri=ARK.foedselsnummer, name="Part_foedselsnummer", curie=ARK.curie('foedselsnummer'),
                   model_uri=ARK.Part_foedselsnummer, domain=Part, range=Optional[str])

slots.Part_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Part_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ARK.Part_kontaktinformasjon, domain=Part, range=Optional[Union[dict, "Kontaktinformasjon"]])

slots.Part_kontaktperson_str = Slot(uri=ARK.kontaktperson, name="Part_kontaktperson_str", curie=ARK.curie('kontaktperson'),
                   model_uri=ARK.Part_kontaktperson_str, domain=Part, range=Optional[str])

slots.Part_orgnummer = Slot(uri=ARK.organisasjonsnummer, name="Part_orgnummer", curie=ARK.curie('organisasjonsnummer'),
                   model_uri=ARK.Part_orgnummer, domain=Part, range=Optional[str])

slots.Part_partNavn = Slot(uri=ARK.partNavn, name="Part_partNavn", curie=ARK.curie('partNavn'),
                   model_uri=ARK.Part_partNavn, domain=Part, range=str)

slots.Part_partRolle = Slot(uri=ARK.partRolle, name="Part_partRolle", curie=ARK.curie('partRolle'),
                   model_uri=ARK.Part_partRolle, domain=Part, range=Optional[Union[str, PartRolleId]])

slots.Skjerming_skjermingshjemmel = Slot(uri=ARK.skjermingshjemmel, name="Skjerming_skjermingshjemmel", curie=ARK.curie('skjermingshjemmel'),
                   model_uri=ARK.Skjerming_skjermingshjemmel, domain=Skjerming, range=Union[str, SkjermingshjemmelId])

slots.Skjerming_tilgangsrestriksjon = Slot(uri=ARK.tilgangsrestriksjon, name="Skjerming_tilgangsrestriksjon", curie=ARK.curie('tilgangsrestriksjon'),
                   model_uri=ARK.Skjerming_tilgangsrestriksjon, domain=Skjerming, range=Union[str, TilgangsrestriksjonId])

slots.DokumentStatus_kode = Slot(uri=FINT.kode, name="DokumentStatus_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.DokumentStatus_kode, domain=DokumentStatus, range=str)

slots.DokumentStatus_navn = Slot(uri=FINT.navn, name="DokumentStatus_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.DokumentStatus_navn, domain=DokumentStatus, range=str)

slots.DokumentStatus_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="DokumentStatus_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.DokumentStatus_gyldighetsperiode, domain=DokumentStatus, range=Optional[Union[dict, "Periode"]])

slots.DokumentStatus_passiv = Slot(uri=FINT.passiv, name="DokumentStatus_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.DokumentStatus_passiv, domain=DokumentStatus, range=Optional[Union[bool, Bool]])

slots.DokumentType_kode = Slot(uri=FINT.kode, name="DokumentType_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.DokumentType_kode, domain=DokumentType, range=str)

slots.DokumentType_navn = Slot(uri=FINT.navn, name="DokumentType_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.DokumentType_navn, domain=DokumentType, range=str)

slots.DokumentType_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="DokumentType_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.DokumentType_gyldighetsperiode, domain=DokumentType, range=Optional[Union[dict, "Periode"]])

slots.DokumentType_passiv = Slot(uri=FINT.passiv, name="DokumentType_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.DokumentType_passiv, domain=DokumentType, range=Optional[Union[bool, Bool]])

slots.Format_kode = Slot(uri=FINT.kode, name="Format_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.Format_kode, domain=Format, range=str)

slots.Format_navn = Slot(uri=FINT.navn, name="Format_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.Format_navn, domain=Format, range=str)

slots.Format_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Format_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.Format_gyldighetsperiode, domain=Format, range=Optional[Union[dict, "Periode"]])

slots.Format_passiv = Slot(uri=FINT.passiv, name="Format_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.Format_passiv, domain=Format, range=Optional[Union[bool, Bool]])

slots.JournalpostType_kode = Slot(uri=FINT.kode, name="JournalpostType_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.JournalpostType_kode, domain=JournalpostType, range=str)

slots.JournalpostType_navn = Slot(uri=FINT.navn, name="JournalpostType_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.JournalpostType_navn, domain=JournalpostType, range=str)

slots.JournalpostType_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="JournalpostType_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.JournalpostType_gyldighetsperiode, domain=JournalpostType, range=Optional[Union[dict, "Periode"]])

slots.JournalpostType_passiv = Slot(uri=FINT.passiv, name="JournalpostType_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.JournalpostType_passiv, domain=JournalpostType, range=Optional[Union[bool, Bool]])

slots.JournalStatus_kode = Slot(uri=FINT.kode, name="JournalStatus_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.JournalStatus_kode, domain=JournalStatus, range=str)

slots.JournalStatus_navn = Slot(uri=FINT.navn, name="JournalStatus_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.JournalStatus_navn, domain=JournalStatus, range=str)

slots.JournalStatus_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="JournalStatus_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.JournalStatus_gyldighetsperiode, domain=JournalStatus, range=Optional[Union[dict, "Periode"]])

slots.JournalStatus_passiv = Slot(uri=FINT.passiv, name="JournalStatus_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.JournalStatus_passiv, domain=JournalStatus, range=Optional[Union[bool, Bool]])

slots.Klassifikasjonstype_kode = Slot(uri=FINT.kode, name="Klassifikasjonstype_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.Klassifikasjonstype_kode, domain=Klassifikasjonstype, range=str)

slots.Klassifikasjonstype_navn = Slot(uri=FINT.navn, name="Klassifikasjonstype_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.Klassifikasjonstype_navn, domain=Klassifikasjonstype, range=str)

slots.Klassifikasjonstype_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Klassifikasjonstype_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.Klassifikasjonstype_gyldighetsperiode, domain=Klassifikasjonstype, range=Optional[Union[dict, "Periode"]])

slots.Klassifikasjonstype_passiv = Slot(uri=FINT.passiv, name="Klassifikasjonstype_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.Klassifikasjonstype_passiv, domain=Klassifikasjonstype, range=Optional[Union[bool, Bool]])

slots.KorrespondansepartType_kode = Slot(uri=FINT.kode, name="KorrespondansepartType_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.KorrespondansepartType_kode, domain=KorrespondansepartType, range=str)

slots.KorrespondansepartType_navn = Slot(uri=FINT.navn, name="KorrespondansepartType_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.KorrespondansepartType_navn, domain=KorrespondansepartType, range=str)

slots.KorrespondansepartType_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="KorrespondansepartType_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.KorrespondansepartType_gyldighetsperiode, domain=KorrespondansepartType, range=Optional[Union[dict, "Periode"]])

slots.KorrespondansepartType_passiv = Slot(uri=FINT.passiv, name="KorrespondansepartType_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.KorrespondansepartType_passiv, domain=KorrespondansepartType, range=Optional[Union[bool, Bool]])

slots.Merknadstype_kode = Slot(uri=FINT.kode, name="Merknadstype_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.Merknadstype_kode, domain=Merknadstype, range=str)

slots.Merknadstype_navn = Slot(uri=FINT.navn, name="Merknadstype_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.Merknadstype_navn, domain=Merknadstype, range=str)

slots.Merknadstype_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Merknadstype_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.Merknadstype_gyldighetsperiode, domain=Merknadstype, range=Optional[Union[dict, "Periode"]])

slots.Merknadstype_passiv = Slot(uri=FINT.passiv, name="Merknadstype_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.Merknadstype_passiv, domain=Merknadstype, range=Optional[Union[bool, Bool]])

slots.PartRolle_kode = Slot(uri=FINT.kode, name="PartRolle_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.PartRolle_kode, domain=PartRolle, range=str)

slots.PartRolle_navn = Slot(uri=FINT.navn, name="PartRolle_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.PartRolle_navn, domain=PartRolle, range=str)

slots.PartRolle_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="PartRolle_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.PartRolle_gyldighetsperiode, domain=PartRolle, range=Optional[Union[dict, "Periode"]])

slots.PartRolle_passiv = Slot(uri=FINT.passiv, name="PartRolle_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.PartRolle_passiv, domain=PartRolle, range=Optional[Union[bool, Bool]])

slots.Rolle_kode = Slot(uri=FINT.kode, name="Rolle_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.Rolle_kode, domain=Rolle, range=str)

slots.Rolle_navn = Slot(uri=FINT.navn, name="Rolle_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.Rolle_navn, domain=Rolle, range=str)

slots.Rolle_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Rolle_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.Rolle_gyldighetsperiode, domain=Rolle, range=Optional[Union[dict, "Periode"]])

slots.Rolle_passiv = Slot(uri=FINT.passiv, name="Rolle_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.Rolle_passiv, domain=Rolle, range=Optional[Union[bool, Bool]])

slots.Saksmappetype_kode = Slot(uri=FINT.kode, name="Saksmappetype_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.Saksmappetype_kode, domain=Saksmappetype, range=str)

slots.Saksmappetype_navn = Slot(uri=FINT.navn, name="Saksmappetype_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.Saksmappetype_navn, domain=Saksmappetype, range=str)

slots.Saksmappetype_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Saksmappetype_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.Saksmappetype_gyldighetsperiode, domain=Saksmappetype, range=Optional[Union[dict, "Periode"]])

slots.Saksmappetype_passiv = Slot(uri=FINT.passiv, name="Saksmappetype_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.Saksmappetype_passiv, domain=Saksmappetype, range=Optional[Union[bool, Bool]])

slots.Saksstatus_kode = Slot(uri=FINT.kode, name="Saksstatus_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.Saksstatus_kode, domain=Saksstatus, range=str)

slots.Saksstatus_navn = Slot(uri=FINT.navn, name="Saksstatus_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.Saksstatus_navn, domain=Saksstatus, range=str)

slots.Saksstatus_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Saksstatus_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.Saksstatus_gyldighetsperiode, domain=Saksstatus, range=Optional[Union[dict, "Periode"]])

slots.Saksstatus_passiv = Slot(uri=FINT.passiv, name="Saksstatus_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.Saksstatus_passiv, domain=Saksstatus, range=Optional[Union[bool, Bool]])

slots.Skjermingshjemmel_kode = Slot(uri=FINT.kode, name="Skjermingshjemmel_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.Skjermingshjemmel_kode, domain=Skjermingshjemmel, range=str)

slots.Skjermingshjemmel_navn = Slot(uri=FINT.navn, name="Skjermingshjemmel_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.Skjermingshjemmel_navn, domain=Skjermingshjemmel, range=str)

slots.Skjermingshjemmel_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Skjermingshjemmel_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.Skjermingshjemmel_gyldighetsperiode, domain=Skjermingshjemmel, range=Optional[Union[dict, "Periode"]])

slots.Skjermingshjemmel_passiv = Slot(uri=FINT.passiv, name="Skjermingshjemmel_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.Skjermingshjemmel_passiv, domain=Skjermingshjemmel, range=Optional[Union[bool, Bool]])

slots.Tilgangsgruppe_kode = Slot(uri=FINT.kode, name="Tilgangsgruppe_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.Tilgangsgruppe_kode, domain=Tilgangsgruppe, range=str)

slots.Tilgangsgruppe_navn = Slot(uri=FINT.navn, name="Tilgangsgruppe_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.Tilgangsgruppe_navn, domain=Tilgangsgruppe, range=str)

slots.Tilgangsgruppe_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Tilgangsgruppe_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.Tilgangsgruppe_gyldighetsperiode, domain=Tilgangsgruppe, range=Optional[Union[dict, "Periode"]])

slots.Tilgangsgruppe_passiv = Slot(uri=FINT.passiv, name="Tilgangsgruppe_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.Tilgangsgruppe_passiv, domain=Tilgangsgruppe, range=Optional[Union[bool, Bool]])

slots.Tilgangsrestriksjon_kode = Slot(uri=FINT.kode, name="Tilgangsrestriksjon_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.Tilgangsrestriksjon_kode, domain=Tilgangsrestriksjon, range=str)

slots.Tilgangsrestriksjon_navn = Slot(uri=FINT.navn, name="Tilgangsrestriksjon_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.Tilgangsrestriksjon_navn, domain=Tilgangsrestriksjon, range=str)

slots.Tilgangsrestriksjon_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Tilgangsrestriksjon_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.Tilgangsrestriksjon_gyldighetsperiode, domain=Tilgangsrestriksjon, range=Optional[Union[dict, "Periode"]])

slots.Tilgangsrestriksjon_passiv = Slot(uri=FINT.passiv, name="Tilgangsrestriksjon_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.Tilgangsrestriksjon_passiv, domain=Tilgangsrestriksjon, range=Optional[Union[bool, Bool]])

slots.TilknyttetRegistreringSom_kode = Slot(uri=FINT.kode, name="TilknyttetRegistreringSom_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.TilknyttetRegistreringSom_kode, domain=TilknyttetRegistreringSom, range=str)

slots.TilknyttetRegistreringSom_navn = Slot(uri=FINT.navn, name="TilknyttetRegistreringSom_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.TilknyttetRegistreringSom_navn, domain=TilknyttetRegistreringSom, range=str)

slots.TilknyttetRegistreringSom_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="TilknyttetRegistreringSom_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.TilknyttetRegistreringSom_gyldighetsperiode, domain=TilknyttetRegistreringSom, range=Optional[Union[dict, "Periode"]])

slots.TilknyttetRegistreringSom_passiv = Slot(uri=FINT.passiv, name="TilknyttetRegistreringSom_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.TilknyttetRegistreringSom_passiv, domain=TilknyttetRegistreringSom, range=Optional[Union[bool, Bool]])

slots.Variantformat_kode = Slot(uri=FINT.kode, name="Variantformat_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.Variantformat_kode, domain=Variantformat, range=str)

slots.Variantformat_navn = Slot(uri=FINT.navn, name="Variantformat_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.Variantformat_navn, domain=Variantformat, range=str)

slots.Variantformat_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Variantformat_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.Variantformat_gyldighetsperiode, domain=Variantformat, range=Optional[Union[dict, "Periode"]])

slots.Variantformat_passiv = Slot(uri=FINT.passiv, name="Variantformat_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.Variantformat_passiv, domain=Variantformat, range=Optional[Union[bool, Bool]])

slots.Aktoer_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Aktoer_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ARK.Aktoer_kontaktinformasjon, domain=Aktoer, range=Optional[Union[dict, "Kontaktinformasjon"]])

slots.Aktoer_postadresse = Slot(uri=FINT.postadresse, name="Aktoer_postadresse", curie=FINT.curie('postadresse'),
                   model_uri=ARK.Aktoer_postadresse, domain=Aktoer, range=Optional[Union[dict, "Adresse"]])

slots.Begrep_kode = Slot(uri=FINT.kode, name="Begrep_kode", curie=FINT.curie('kode'),
                   model_uri=ARK.Begrep_kode, domain=Begrep, range=str)

slots.Begrep_navn = Slot(uri=FINT.navn, name="Begrep_navn", curie=FINT.curie('navn'),
                   model_uri=ARK.Begrep_navn, domain=Begrep, range=str)

slots.Begrep_gyldighetsperiode = Slot(uri=FINT.gyldighetsperiode, name="Begrep_gyldighetsperiode", curie=FINT.curie('gyldighetsperiode'),
                   model_uri=ARK.Begrep_gyldighetsperiode, domain=Begrep, range=Optional[Union[dict, "Periode"]])

slots.Begrep_passiv = Slot(uri=FINT.passiv, name="Begrep_passiv", curie=FINT.curie('passiv'),
                   model_uri=ARK.Begrep_passiv, domain=Begrep, range=Optional[Union[bool, Bool]])

slots.Elev_elevnummer = Slot(uri=FINT.elevnummer, name="Elev_elevnummer", curie=FINT.curie('elevnummer'),
                   model_uri=ARK.Elev_elevnummer, domain=Elev, range=Optional[Union[dict, "Identifikator"]])

slots.Elev_person = Slot(uri=FINT.person, name="Elev_person", curie=FINT.curie('person'),
                   model_uri=ARK.Elev_person, domain=Elev, range=Optional[Union[str, PersonId]])

slots.Enhet_forretningsadresse = Slot(uri=FINT.forretningsadresse, name="Enhet_forretningsadresse", curie=FINT.curie('forretningsadresse'),
                   model_uri=ARK.Enhet_forretningsadresse, domain=Enhet, range=Optional[Union[dict, "Adresse"]])

slots.Enhet_organisasjonsnavn = Slot(uri=FINT.organisasjonsnavn, name="Enhet_organisasjonsnavn", curie=FINT.curie('organisasjonsnavn'),
                   model_uri=ARK.Enhet_organisasjonsnavn, domain=Enhet, range=Optional[str])

slots.Enhet_organisasjonsnummer = Slot(uri=FINT.organisasjonsnummer, name="Enhet_organisasjonsnummer", curie=FINT.curie('organisasjonsnummer'),
                   model_uri=ARK.Enhet_organisasjonsnummer, domain=Enhet, range=Optional[Union[dict, "Identifikator"]])

slots.Identifikator_identifikatorverdi = Slot(uri=FINT.identifikatorverdi, name="Identifikator_identifikatorverdi", curie=FINT.curie('identifikatorverdi'),
                   model_uri=ARK.Identifikator_identifikatorverdi, domain=Identifikator, range=str)

slots.Periode_start = Slot(uri=FINT.start, name="Periode_start", curie=FINT.curie('start'),
                   model_uri=ARK.Periode_start, domain=Periode, range=Union[str, XSDDateTime])

slots.Personnavn_fornavn = Slot(uri=FINT.fornavn, name="Personnavn_fornavn", curie=FINT.curie('fornavn'),
                   model_uri=ARK.Personnavn_fornavn, domain=Personnavn, range=str)

slots.Personnavn_etternavn = Slot(uri=FINT.etternavn, name="Personnavn_etternavn", curie=FINT.curie('etternavn'),
                   model_uri=ARK.Personnavn_etternavn, domain=Personnavn, range=str)

slots.Fylke_kommune = Slot(uri=FINT.kommune, name="Fylke_kommune", curie=FINT.curie('kommune'),
                   model_uri=ARK.Fylke_kommune, domain=Fylke, range=Optional[Union[Union[str, KommuneId], list[Union[str, KommuneId]]]])

slots.Kommune_fylke = Slot(uri=FINT.fylke, name="Kommune_fylke", curie=FINT.curie('fylke'),
                   model_uri=ARK.Kommune_fylke, domain=Kommune, range=Union[str, FylkeId])

slots.Valuta_bokstavkode = Slot(uri=FINT.bokstavkode, name="Valuta_bokstavkode", curie=FINT.curie('bokstavkode'),
                   model_uri=ARK.Valuta_bokstavkode, domain=Valuta, range=Union[dict, Identifikator])

slots.Valuta_valuta_navn = Slot(uri=FINT.valutaNavn, name="Valuta_valuta_navn", curie=FINT.curie('valutaNavn'),
                   model_uri=ARK.Valuta_valuta_navn, domain=Valuta, range=str)

slots.Valuta_nummerkode = Slot(uri=FINT.nummerkode, name="Valuta_nummerkode", curie=FINT.curie('nummerkode'),
                   model_uri=ARK.Valuta_nummerkode, domain=Valuta, range=Union[dict, Identifikator])

slots.Person_fodselsnummer = Slot(uri=FINT.fodselsnummer, name="Person_fodselsnummer", curie=FINT.curie('fodselsnummer'),
                   model_uri=ARK.Person_fodselsnummer, domain=Person, range=Union[dict, Identifikator])

slots.Person_person_navn = Slot(uri=FINT.personNavn, name="Person_person_navn", curie=FINT.curie('personNavn'),
                   model_uri=ARK.Person_person_navn, domain=Person, range=Union[dict, Personnavn])

slots.Person_bilde = Slot(uri=FINT.bilde, name="Person_bilde", curie=FINT.curie('bilde'),
                   model_uri=ARK.Person_bilde, domain=Person, range=Optional[str])

slots.Person_bostedsadresse = Slot(uri=FINT.bostedsadresse, name="Person_bostedsadresse", curie=FINT.curie('bostedsadresse'),
                   model_uri=ARK.Person_bostedsadresse, domain=Person, range=Optional[Union[dict, Adresse]])

slots.Person_fodselsdato = Slot(uri=FINT.fodselsdato, name="Person_fodselsdato", curie=FINT.curie('fodselsdato'),
                   model_uri=ARK.Person_fodselsdato, domain=Person, range=Optional[Union[str, XSDDate]])

slots.Person_parorende = Slot(uri=FINT.parorende, name="Person_parorende", curie=FINT.curie('parorende'),
                   model_uri=ARK.Person_parorende, domain=Person, range=Optional[Union[Union[str, KontaktpersonId], list[Union[str, KontaktpersonId]]]])

slots.Person_statsborgerskap = Slot(uri=FINT.statsborgerskap, name="Person_statsborgerskap", curie=FINT.curie('statsborgerskap'),
                   model_uri=ARK.Person_statsborgerskap, domain=Person, range=Optional[Union[Union[str, LandkodeId], list[Union[str, LandkodeId]]]])

slots.Person_kommune = Slot(uri=FINT.kommune, name="Person_kommune", curie=FINT.curie('kommune'),
                   model_uri=ARK.Person_kommune, domain=Person, range=Optional[Union[str, KommuneId]])

slots.Person_kjonn = Slot(uri=FINT.kjonn, name="Person_kjonn", curie=FINT.curie('kjonn'),
                   model_uri=ARK.Person_kjonn, domain=Person, range=Optional[Union[str, KjonnId]])

slots.Person_foreldreansvar = Slot(uri=FINT.foreldreansvar, name="Person_foreldreansvar", curie=FINT.curie('foreldreansvar'),
                   model_uri=ARK.Person_foreldreansvar, domain=Person, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Person_foreldre = Slot(uri=FINT.foreldre, name="Person_foreldre", curie=FINT.curie('foreldre'),
                   model_uri=ARK.Person_foreldre, domain=Person, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Person_maalform = Slot(uri=FINT.maalform, name="Person_maalform", curie=FINT.curie('maalform'),
                   model_uri=ARK.Person_maalform, domain=Person, range=Optional[Union[str, SpraakId]])

slots.Person_morsmaal = Slot(uri=FINT.morsmaal, name="Person_morsmaal", curie=FINT.curie('morsmaal'),
                   model_uri=ARK.Person_morsmaal, domain=Person, range=Optional[Union[str, SpraakId]])

slots.Person_laerling = Slot(uri=FINT.laerling, name="Person_laerling", curie=FINT.curie('laerling'),
                   model_uri=ARK.Person_laerling, domain=Person, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Person_elev = Slot(uri=FINT.elev, name="Person_elev", curie=FINT.curie('elev'),
                   model_uri=ARK.Person_elev, domain=Person, range=Optional[Union[str, ElevId]])

slots.Person_otungdom = Slot(uri=FINT.otungdom, name="Person_otungdom", curie=FINT.curie('otungdom'),
                   model_uri=ARK.Person_otungdom, domain=Person, range=Optional[Union[str, URIorCURIE]])

slots.Kontaktperson_type = Slot(uri=FINT.type, name="Kontaktperson_type", curie=FINT.curie('type'),
                   model_uri=ARK.Kontaktperson_type, domain=Kontaktperson, range=str)

slots.Kontaktperson_kontaktinformasjon = Slot(uri=FINT.kontaktinformasjon, name="Kontaktperson_kontaktinformasjon", curie=FINT.curie('kontaktinformasjon'),
                   model_uri=ARK.Kontaktperson_kontaktinformasjon, domain=Kontaktperson, range=Optional[Union[dict, Kontaktinformasjon]])

slots.Kontaktperson_kontaktperson_navn = Slot(uri=FINT.kontaktpersonNavn, name="Kontaktperson_kontaktperson_navn", curie=FINT.curie('kontaktpersonNavn'),
                   model_uri=ARK.Kontaktperson_kontaktperson_navn, domain=Kontaktperson, range=Optional[Union[dict, Personnavn]])

slots.Kontaktperson_kontaktperson = Slot(uri=FINT.kontaktpersonFor, name="Kontaktperson_kontaktperson", curie=FINT.curie('kontaktpersonFor'),
                   model_uri=ARK.Kontaktperson_kontaktperson, domain=Kontaktperson, range=Optional[Union[Union[str, PersonId], list[Union[str, PersonId]]]])

slots.Virksomhet_virksomhetsId = Slot(uri=FINT.virksomhetsId, name="Virksomhet_virksomhetsId", curie=FINT.curie('virksomhetsId'),
                   model_uri=ARK.Virksomhet_virksomhetsId, domain=Virksomhet, range=Union[dict, Identifikator])

slots.Virksomhet_laerling = Slot(uri=FINT.laerling, name="Virksomhet_laerling", curie=FINT.curie('laerling'),
                   model_uri=ARK.Virksomhet_laerling, domain=Virksomhet, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

