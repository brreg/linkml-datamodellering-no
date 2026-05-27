# Auto generated from ngr-person-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-27T14:51:36
# Schema: ngr-person
#
# id: https://data.norge.no/ngr/ngr-person
# description: Domenemodell for persondata basert på Nasjonale grunndata (utkast). Modellerer Person med identifikasjon, familierelasjonar, adresser, eigarrettar og kontaktopplysningar frå Folkeregisteret og KRR. Basert på https://informasjonsforvaltning.github.io/nasjonale-grunndata/
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

from linkml_runtime.linkml_model.types import Boolean, Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.11.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NGRP = CurieNamespace('ngrp', 'https://data.norge.no/vocabulary/ngr-person#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://data.norge.no/ngr/ngr-person/')


# Types

# Class references
class PersonId(URIorCURIE):
    pass


class PersonnavnId(URIorCURIE):
    pass


class FolkeregisteridentifikatorId(URIorCURIE):
    pass


class FoedselsnummerId(FolkeregisteridentifikatorId):
    pass


class DNummerId(FolkeregisteridentifikatorId):
    pass


class PersonidentifikasjonId(URIorCURIE):
    pass


class FalskIdentitetId(URIorCURIE):
    pass


class IdentifikasjonsdokumentId(URIorCURIE):
    pass


class IdentitetsgrunnlagId(URIorCURIE):
    pass


class KjoennId(URIorCURIE):
    pass


class SivilstandId(URIorCURIE):
    pass


class PersonstatusId(URIorCURIE):
    pass


class StatsborgerskapId(URIorCURIE):
    pass


class OppholdId(URIorCURIE):
    pass


class FoedselId(URIorCURIE):
    pass


class DodsfallId(URIorCURIE):
    pass


class KontaktinformasjonDoedsboId(URIorCURIE):
    pass


class ForeldreansvarForelderId(URIorCURIE):
    pass


class ForeldreansvarBarnId(URIorCURIE):
    pass


class FamilierelasjonForelderId(URIorCURIE):
    pass


class FamilierelasjonBarnId(URIorCURIE):
    pass


class FamilierelasjonEktefelleId(URIorCURIE):
    pass


class InnflyttingTilNorgeId(URIorCURIE):
    pass


class UtflyttingFraNorgeId(URIorCURIE):
    pass


class GeografiskAdresseId(URIorCURIE):
    pass


class BostedsadresseId(GeografiskAdresseId):
    pass


class PostadresseId(GeografiskAdresseId):
    pass


class OppholdsadresseId(GeografiskAdresseId):
    pass


class AdressebeskyttelseId(URIorCURIE):
    pass


class VergeId(URIorCURIE):
    pass


class RettsligHandleevneId(URIorCURIE):
    pass


class ReservasjonMotKommunikasjonPaaNettId(URIorCURIE):
    pass


class KontaktopplysningerId(URIorCURIE):
    pass


class SpraakForElektroniskKommunikasjonId(URIorCURIE):
    pass


@dataclass(repr=False)
class PersonContainer(YAMLRoot):
    """
    Rotklasse for NGR-person-datafiler. Held flate lister av alle instansierbare klassar; referansar mellom objekt
    brukar URI-lenking.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/PersonContainer")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PersonContainer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/PersonContainer")

    personar: Optional[Union[dict[Union[str, PersonId], Union[dict, "Person"]], list[Union[dict, "Person"]]]] = empty_dict()
    personnavn: Optional[Union[dict[Union[str, PersonnavnId], Union[dict, "Personnavn"]], list[Union[dict, "Personnavn"]]]] = empty_dict()
    foedselsnummer: Optional[Union[dict[Union[str, FoedselsnummerId], Union[dict, "Foedselsnummer"]], list[Union[dict, "Foedselsnummer"]]]] = empty_dict()
    dnummer: Optional[Union[dict[Union[str, DNummerId], Union[dict, "DNummer"]], list[Union[dict, "DNummer"]]]] = empty_dict()
    personidentifikasjonar: Optional[Union[dict[Union[str, PersonidentifikasjonId], Union[dict, "Personidentifikasjon"]], list[Union[dict, "Personidentifikasjon"]]]] = empty_dict()
    falskIdentitetar: Optional[Union[dict[Union[str, FalskIdentitetId], Union[dict, "FalskIdentitet"]], list[Union[dict, "FalskIdentitet"]]]] = empty_dict()
    identifikasjonsdokument: Optional[Union[dict[Union[str, IdentifikasjonsdokumentId], Union[dict, "Identifikasjonsdokument"]], list[Union[dict, "Identifikasjonsdokument"]]]] = empty_dict()
    identitetsgrunnlag: Optional[Union[dict[Union[str, IdentitetsgrunnlagId], Union[dict, "Identitetsgrunnlag"]], list[Union[dict, "Identitetsgrunnlag"]]]] = empty_dict()
    kjoenn: Optional[Union[dict[Union[str, KjoennId], Union[dict, "Kjoenn"]], list[Union[dict, "Kjoenn"]]]] = empty_dict()
    sivilstand: Optional[Union[dict[Union[str, SivilstandId], Union[dict, "Sivilstand"]], list[Union[dict, "Sivilstand"]]]] = empty_dict()
    personstatus: Optional[Union[dict[Union[str, PersonstatusId], Union[dict, "Personstatus"]], list[Union[dict, "Personstatus"]]]] = empty_dict()
    statsborgerskap: Optional[Union[dict[Union[str, StatsborgerskapId], Union[dict, "Statsborgerskap"]], list[Union[dict, "Statsborgerskap"]]]] = empty_dict()
    opphold: Optional[Union[dict[Union[str, OppholdId], Union[dict, "Opphold"]], list[Union[dict, "Opphold"]]]] = empty_dict()
    foedslar: Optional[Union[dict[Union[str, FoedselId], Union[dict, "Foedsel"]], list[Union[dict, "Foedsel"]]]] = empty_dict()
    foreldreansvarForelder: Optional[Union[dict[Union[str, ForeldreansvarForelderId], Union[dict, "ForeldreansvarForelder"]], list[Union[dict, "ForeldreansvarForelder"]]]] = empty_dict()
    foreldreansvarBarn: Optional[Union[dict[Union[str, ForeldreansvarBarnId], Union[dict, "ForeldreansvarBarn"]], list[Union[dict, "ForeldreansvarBarn"]]]] = empty_dict()
    familierelasjonForelder: Optional[Union[dict[Union[str, FamilierelasjonForelderId], Union[dict, "FamilierelasjonForelder"]], list[Union[dict, "FamilierelasjonForelder"]]]] = empty_dict()
    familierelasjonBarn: Optional[Union[dict[Union[str, FamilierelasjonBarnId], Union[dict, "FamilierelasjonBarn"]], list[Union[dict, "FamilierelasjonBarn"]]]] = empty_dict()
    familierelasjonEktefelle: Optional[Union[dict[Union[str, FamilierelasjonEktefelleId], Union[dict, "FamilierelasjonEktefelle"]], list[Union[dict, "FamilierelasjonEktefelle"]]]] = empty_dict()
    dodsfall: Optional[Union[dict[Union[str, DodsfallId], Union[dict, "Dodsfall"]], list[Union[dict, "Dodsfall"]]]] = empty_dict()
    kontaktinformasjonDoedsbo: Optional[Union[dict[Union[str, KontaktinformasjonDoedsboId], Union[dict, "KontaktinformasjonDoedsbo"]], list[Union[dict, "KontaktinformasjonDoedsbo"]]]] = empty_dict()
    innflytting: Optional[Union[dict[Union[str, InnflyttingTilNorgeId], Union[dict, "InnflyttingTilNorge"]], list[Union[dict, "InnflyttingTilNorge"]]]] = empty_dict()
    utflytting: Optional[Union[dict[Union[str, UtflyttingFraNorgeId], Union[dict, "UtflyttingFraNorge"]], list[Union[dict, "UtflyttingFraNorge"]]]] = empty_dict()
    adressebeskyttelse: Optional[Union[dict[Union[str, AdressebeskyttelseId], Union[dict, "Adressebeskyttelse"]], list[Union[dict, "Adressebeskyttelse"]]]] = empty_dict()
    bostedsadresser: Optional[Union[dict[Union[str, BostedsadresseId], Union[dict, "Bostedsadresse"]], list[Union[dict, "Bostedsadresse"]]]] = empty_dict()
    postadresser: Optional[Union[dict[Union[str, PostadresseId], Union[dict, "Postadresse"]], list[Union[dict, "Postadresse"]]]] = empty_dict()
    oppholdsadresser: Optional[Union[dict[Union[str, OppholdsadresseId], Union[dict, "Oppholdsadresse"]], list[Union[dict, "Oppholdsadresse"]]]] = empty_dict()
    verger: Optional[Union[dict[Union[str, VergeId], Union[dict, "Verge"]], list[Union[dict, "Verge"]]]] = empty_dict()
    rettsligHandleevne: Optional[Union[dict[Union[str, RettsligHandleevneId], Union[dict, "RettsligHandleevne"]], list[Union[dict, "RettsligHandleevne"]]]] = empty_dict()
    reservasjonar: Optional[Union[dict[Union[str, ReservasjonMotKommunikasjonPaaNettId], Union[dict, "ReservasjonMotKommunikasjonPaaNett"]], list[Union[dict, "ReservasjonMotKommunikasjonPaaNett"]]]] = empty_dict()
    kontaktopplysningar: Optional[Union[dict[Union[str, KontaktopplysningerId], Union[dict, "Kontaktopplysninger"]], list[Union[dict, "Kontaktopplysninger"]]]] = empty_dict()
    spraak: Optional[Union[dict[Union[str, SpraakForElektroniskKommunikasjonId], Union[dict, "SpraakForElektroniskKommunikasjon"]], list[Union[dict, "SpraakForElektroniskKommunikasjon"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="personar", slot_type=Person, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="personnavn", slot_type=Personnavn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="foedselsnummer", slot_type=Foedselsnummer, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dnummer", slot_type=DNummer, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="personidentifikasjonar", slot_type=Personidentifikasjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="falskIdentitetar", slot_type=FalskIdentitet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="identifikasjonsdokument", slot_type=Identifikasjonsdokument, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="identitetsgrunnlag", slot_type=Identitetsgrunnlag, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kjoenn", slot_type=Kjoenn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sivilstand", slot_type=Sivilstand, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="personstatus", slot_type=Personstatus, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="statsborgerskap", slot_type=Statsborgerskap, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="opphold", slot_type=Opphold, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="foedslar", slot_type=Foedsel, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="foreldreansvarForelder", slot_type=ForeldreansvarForelder, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="foreldreansvarBarn", slot_type=ForeldreansvarBarn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="familierelasjonForelder", slot_type=FamilierelasjonForelder, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="familierelasjonBarn", slot_type=FamilierelasjonBarn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="familierelasjonEktefelle", slot_type=FamilierelasjonEktefelle, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dodsfall", slot_type=Dodsfall, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kontaktinformasjonDoedsbo", slot_type=KontaktinformasjonDoedsbo, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="innflytting", slot_type=InnflyttingTilNorge, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="utflytting", slot_type=UtflyttingFraNorge, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="adressebeskyttelse", slot_type=Adressebeskyttelse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="bostedsadresser", slot_type=Bostedsadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="postadresser", slot_type=Postadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="oppholdsadresser", slot_type=Oppholdsadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="verger", slot_type=Verge, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rettsligHandleevne", slot_type=RettsligHandleevne, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="reservasjonar", slot_type=ReservasjonMotKommunikasjonPaaNett, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kontaktopplysningar", slot_type=Kontaktopplysninger, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="spraak", slot_type=SpraakForElektroniskKommunikasjon, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    """
    Ein fysisk person registrert i Folkeregisteret. Hovudbegrepet i domene person.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Person"]
    class_class_curie: ClassVar[str] = "ngrp:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Person")

    id: Union[str, PersonId] = None
    har_personnavn: Union[str, PersonnavnId] = None
    har_folkeregisteridentifikator: Union[str, FolkeregisteridentifikatorId] = None
    har_kjoenn: Union[str, KjoennId] = None
    har_sivilstand: Union[str, SivilstandId] = None
    har_personstatus: Union[str, PersonstatusId] = None
    har_statsborgerskap: Union[Union[str, StatsborgerskapId], list[Union[str, StatsborgerskapId]]] = None
    har_foedsel: Union[str, FoedselId] = None
    har_valgt_spraak: Union[str, SpraakForElektroniskKommunikasjonId] = None
    har_personidentifikasjon: Optional[Union[Union[str, PersonidentifikasjonId], list[Union[str, PersonidentifikasjonId]]]] = empty_list()
    har_falsk_identitet: Optional[Union[str, FalskIdentitetId]] = None
    har_utenlandsk_identifikasjonsdokument: Optional[Union[Union[str, IdentifikasjonsdokumentId], list[Union[str, IdentifikasjonsdokumentId]]]] = empty_list()
    har_identitetsgrunnlag: Optional[Union[str, IdentitetsgrunnlagId]] = None
    har_lovlig_opphold: Optional[Union[str, OppholdId]] = None
    har_foreldreansvar_forelder: Optional[Union[Union[str, ForeldreansvarForelderId], list[Union[str, ForeldreansvarForelderId]]]] = empty_list()
    har_foreldreansvar_barn: Optional[Union[Union[str, ForeldreansvarBarnId], list[Union[str, ForeldreansvarBarnId]]]] = empty_list()
    har_familierelasjon_forelder: Optional[Union[Union[str, FamilierelasjonForelderId], list[Union[str, FamilierelasjonForelderId]]]] = empty_list()
    har_familierelasjon_barn: Optional[Union[Union[str, FamilierelasjonBarnId], list[Union[str, FamilierelasjonBarnId]]]] = empty_list()
    har_familierelasjon_ektefelle: Optional[Union[str, FamilierelasjonEktefelleId]] = None
    har_dodsfall: Optional[Union[str, DodsfallId]] = None
    har_kontaktinformasjon_doedsbo: Optional[Union[str, KontaktinformasjonDoedsboId]] = None
    har_innflytting_til_norge: Optional[Union[str, InnflyttingTilNorgeId]] = None
    har_utflytting_fra_norge: Optional[Union[str, UtflyttingFraNorgeId]] = None
    har_adressebeskyttelse: Optional[Union[str, AdressebeskyttelseId]] = None
    har_bosted_paa: Optional[Union[str, BostedsadresseId]] = None
    mottar_post_paa: Optional[Union[str, PostadresseId]] = None
    oppholder_seg_paa: Optional[Union[str, OppholdsadresseId]] = None
    har_verge: Optional[Union[Union[str, VergeId], list[Union[str, VergeId]]]] = empty_list()
    har_rettslig_handleevne: Optional[Union[str, RettsligHandleevneId]] = None
    har_reservasjon_mot_kommunikasjon: Optional[Union[str, ReservasjonMotKommunikasjonPaaNettId]] = None
    har_kontaktopplysninger: Optional[Union[str, KontaktopplysningerId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.har_personnavn):
            self.MissingRequiredField("har_personnavn")
        if not isinstance(self.har_personnavn, PersonnavnId):
            self.har_personnavn = PersonnavnId(self.har_personnavn)

        if self._is_empty(self.har_folkeregisteridentifikator):
            self.MissingRequiredField("har_folkeregisteridentifikator")
        if not isinstance(self.har_folkeregisteridentifikator, FolkeregisteridentifikatorId):
            self.har_folkeregisteridentifikator = FolkeregisteridentifikatorId(self.har_folkeregisteridentifikator)

        if self._is_empty(self.har_kjoenn):
            self.MissingRequiredField("har_kjoenn")
        if not isinstance(self.har_kjoenn, KjoennId):
            self.har_kjoenn = KjoennId(self.har_kjoenn)

        if self._is_empty(self.har_sivilstand):
            self.MissingRequiredField("har_sivilstand")
        if not isinstance(self.har_sivilstand, SivilstandId):
            self.har_sivilstand = SivilstandId(self.har_sivilstand)

        if self._is_empty(self.har_personstatus):
            self.MissingRequiredField("har_personstatus")
        if not isinstance(self.har_personstatus, PersonstatusId):
            self.har_personstatus = PersonstatusId(self.har_personstatus)

        if self._is_empty(self.har_statsborgerskap):
            self.MissingRequiredField("har_statsborgerskap")
        if not isinstance(self.har_statsborgerskap, list):
            self.har_statsborgerskap = [self.har_statsborgerskap] if self.har_statsborgerskap is not None else []
        self.har_statsborgerskap = [v if isinstance(v, StatsborgerskapId) else StatsborgerskapId(v) for v in self.har_statsborgerskap]

        if self._is_empty(self.har_foedsel):
            self.MissingRequiredField("har_foedsel")
        if not isinstance(self.har_foedsel, FoedselId):
            self.har_foedsel = FoedselId(self.har_foedsel)

        if self._is_empty(self.har_valgt_spraak):
            self.MissingRequiredField("har_valgt_spraak")
        if not isinstance(self.har_valgt_spraak, SpraakForElektroniskKommunikasjonId):
            self.har_valgt_spraak = SpraakForElektroniskKommunikasjonId(self.har_valgt_spraak)

        if not isinstance(self.har_personidentifikasjon, list):
            self.har_personidentifikasjon = [self.har_personidentifikasjon] if self.har_personidentifikasjon is not None else []
        self.har_personidentifikasjon = [v if isinstance(v, PersonidentifikasjonId) else PersonidentifikasjonId(v) for v in self.har_personidentifikasjon]

        if self.har_falsk_identitet is not None and not isinstance(self.har_falsk_identitet, FalskIdentitetId):
            self.har_falsk_identitet = FalskIdentitetId(self.har_falsk_identitet)

        if not isinstance(self.har_utenlandsk_identifikasjonsdokument, list):
            self.har_utenlandsk_identifikasjonsdokument = [self.har_utenlandsk_identifikasjonsdokument] if self.har_utenlandsk_identifikasjonsdokument is not None else []
        self.har_utenlandsk_identifikasjonsdokument = [v if isinstance(v, IdentifikasjonsdokumentId) else IdentifikasjonsdokumentId(v) for v in self.har_utenlandsk_identifikasjonsdokument]

        if self.har_identitetsgrunnlag is not None and not isinstance(self.har_identitetsgrunnlag, IdentitetsgrunnlagId):
            self.har_identitetsgrunnlag = IdentitetsgrunnlagId(self.har_identitetsgrunnlag)

        if self.har_lovlig_opphold is not None and not isinstance(self.har_lovlig_opphold, OppholdId):
            self.har_lovlig_opphold = OppholdId(self.har_lovlig_opphold)

        if not isinstance(self.har_foreldreansvar_forelder, list):
            self.har_foreldreansvar_forelder = [self.har_foreldreansvar_forelder] if self.har_foreldreansvar_forelder is not None else []
        self.har_foreldreansvar_forelder = [v if isinstance(v, ForeldreansvarForelderId) else ForeldreansvarForelderId(v) for v in self.har_foreldreansvar_forelder]

        if not isinstance(self.har_foreldreansvar_barn, list):
            self.har_foreldreansvar_barn = [self.har_foreldreansvar_barn] if self.har_foreldreansvar_barn is not None else []
        self.har_foreldreansvar_barn = [v if isinstance(v, ForeldreansvarBarnId) else ForeldreansvarBarnId(v) for v in self.har_foreldreansvar_barn]

        if not isinstance(self.har_familierelasjon_forelder, list):
            self.har_familierelasjon_forelder = [self.har_familierelasjon_forelder] if self.har_familierelasjon_forelder is not None else []
        self.har_familierelasjon_forelder = [v if isinstance(v, FamilierelasjonForelderId) else FamilierelasjonForelderId(v) for v in self.har_familierelasjon_forelder]

        if not isinstance(self.har_familierelasjon_barn, list):
            self.har_familierelasjon_barn = [self.har_familierelasjon_barn] if self.har_familierelasjon_barn is not None else []
        self.har_familierelasjon_barn = [v if isinstance(v, FamilierelasjonBarnId) else FamilierelasjonBarnId(v) for v in self.har_familierelasjon_barn]

        if self.har_familierelasjon_ektefelle is not None and not isinstance(self.har_familierelasjon_ektefelle, FamilierelasjonEktefelleId):
            self.har_familierelasjon_ektefelle = FamilierelasjonEktefelleId(self.har_familierelasjon_ektefelle)

        if self.har_dodsfall is not None and not isinstance(self.har_dodsfall, DodsfallId):
            self.har_dodsfall = DodsfallId(self.har_dodsfall)

        if self.har_kontaktinformasjon_doedsbo is not None and not isinstance(self.har_kontaktinformasjon_doedsbo, KontaktinformasjonDoedsboId):
            self.har_kontaktinformasjon_doedsbo = KontaktinformasjonDoedsboId(self.har_kontaktinformasjon_doedsbo)

        if self.har_innflytting_til_norge is not None and not isinstance(self.har_innflytting_til_norge, InnflyttingTilNorgeId):
            self.har_innflytting_til_norge = InnflyttingTilNorgeId(self.har_innflytting_til_norge)

        if self.har_utflytting_fra_norge is not None and not isinstance(self.har_utflytting_fra_norge, UtflyttingFraNorgeId):
            self.har_utflytting_fra_norge = UtflyttingFraNorgeId(self.har_utflytting_fra_norge)

        if self.har_adressebeskyttelse is not None and not isinstance(self.har_adressebeskyttelse, AdressebeskyttelseId):
            self.har_adressebeskyttelse = AdressebeskyttelseId(self.har_adressebeskyttelse)

        if self.har_bosted_paa is not None and not isinstance(self.har_bosted_paa, BostedsadresseId):
            self.har_bosted_paa = BostedsadresseId(self.har_bosted_paa)

        if self.mottar_post_paa is not None and not isinstance(self.mottar_post_paa, PostadresseId):
            self.mottar_post_paa = PostadresseId(self.mottar_post_paa)

        if self.oppholder_seg_paa is not None and not isinstance(self.oppholder_seg_paa, OppholdsadresseId):
            self.oppholder_seg_paa = OppholdsadresseId(self.oppholder_seg_paa)

        if not isinstance(self.har_verge, list):
            self.har_verge = [self.har_verge] if self.har_verge is not None else []
        self.har_verge = [v if isinstance(v, VergeId) else VergeId(v) for v in self.har_verge]

        if self.har_rettslig_handleevne is not None and not isinstance(self.har_rettslig_handleevne, RettsligHandleevneId):
            self.har_rettslig_handleevne = RettsligHandleevneId(self.har_rettslig_handleevne)

        if self.har_reservasjon_mot_kommunikasjon is not None and not isinstance(self.har_reservasjon_mot_kommunikasjon, ReservasjonMotKommunikasjonPaaNettId):
            self.har_reservasjon_mot_kommunikasjon = ReservasjonMotKommunikasjonPaaNettId(self.har_reservasjon_mot_kommunikasjon)

        if self.har_kontaktopplysninger is not None and not isinstance(self.har_kontaktopplysninger, KontaktopplysningerId):
            self.har_kontaktopplysninger = KontaktopplysningerId(self.har_kontaktopplysninger)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Personnavn(YAMLRoot):
    """
    Offisielt registrert namn på ein person i Folkeregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Personnavn"]
    class_class_curie: ClassVar[str] = "ngrp:Personnavn"
    class_name: ClassVar[str] = "Personnavn"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Personnavn")

    id: Union[str, PersonnavnId] = None
    fornavn: str = None
    etternavn: str = None
    mellomnavn: Optional[str] = None
    forkortet_navn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnavnId):
            self.id = PersonnavnId(self.id)

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

        if self.forkortet_navn is not None and not isinstance(self.forkortet_navn, str):
            self.forkortet_navn = str(self.forkortet_navn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Folkeregisteridentifikator(YAMLRoot):
    """
    Abstrakt overklasse for unik identifikator i Folkeregisteret. Konkrete underklassar er Fødselsnummer og D-nummer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Folkeregisteridentifikator"]
    class_class_curie: ClassVar[str] = "ngrp:Folkeregisteridentifikator"
    class_name: ClassVar[str] = "Folkeregisteridentifikator"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Folkeregisteridentifikator")

    id: Union[str, FolkeregisteridentifikatorId] = None
    identifikatornummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FolkeregisteridentifikatorId):
            self.id = FolkeregisteridentifikatorId(self.id)

        if self.identifikatornummer is not None and not isinstance(self.identifikatornummer, str):
            self.identifikatornummer = str(self.identifikatornummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Foedselsnummer(Folkeregisteridentifikator):
    """
    Elleve-sifra fødselsnummer tildelt norske statsborgarar og personar med fast opphald i Noreg.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Foedselsnummer"]
    class_class_curie: ClassVar[str] = "ngrp:Foedselsnummer"
    class_name: ClassVar[str] = "Foedselsnummer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Foedselsnummer")

    id: Union[str, FoedselsnummerId] = None
    identifikatornummer: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoedselsnummerId):
            self.id = FoedselsnummerId(self.id)

        if self._is_empty(self.identifikatornummer):
            self.MissingRequiredField("identifikatornummer")
        if not isinstance(self.identifikatornummer, str):
            self.identifikatornummer = str(self.identifikatornummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DNummer(Folkeregisteridentifikator):
    """
    Elleve-sifra D-nummer tildelt utanlandske personar med mellombels opphald i Noreg (t.d. med d-nummer, om dei har
    midlertidig eller permanent opphald). Brukes om de har midlertidig eller ikkje har permanent opphald.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["DNummer"]
    class_class_curie: ClassVar[str] = "ngrp:DNummer"
    class_name: ClassVar[str] = "DNummer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/DNummer")

    id: Union[str, DNummerId] = None
    identifikatornummer: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DNummerId):
            self.id = DNummerId(self.id)

        if self._is_empty(self.identifikatornummer):
            self.MissingRequiredField("identifikatornummer")
        if not isinstance(self.identifikatornummer, str):
            self.identifikatornummer = str(self.identifikatornummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Personidentifikasjon(YAMLRoot):
    """
    Utanlandsk eller alternativ identifikasjon av ein person, t.d. UDIs DUF-nummer, utanlandsk skatteidentifikasjon
    eller social security number.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Personidentifikasjon"]
    class_class_curie: ClassVar[str] = "ngrp:Personidentifikasjon"
    class_name: ClassVar[str] = "Personidentifikasjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Personidentifikasjon")

    id: Union[str, PersonidentifikasjonId] = None
    identifikasjonstype: str = None
    identifikatornummer: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonidentifikasjonId):
            self.id = PersonidentifikasjonId(self.id)

        if self._is_empty(self.identifikasjonstype):
            self.MissingRequiredField("identifikasjonstype")
        if not isinstance(self.identifikasjonstype, str):
            self.identifikasjonstype = str(self.identifikasjonstype)

        if self._is_empty(self.identifikatornummer):
            self.MissingRequiredField("identifikatornummer")
        if not isinstance(self.identifikatornummer, str):
            self.identifikatornummer = str(self.identifikatornummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FalskIdentitet(YAMLRoot):
    """
    Registrering av at ein person har opptrådt med falsk identitet. Kan peke på den rette identiteten om denne er
    kjent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["FalskIdentitet"]
    class_class_curie: ClassVar[str] = "ngrp:FalskIdentitet"
    class_name: ClassVar[str] = "FalskIdentitet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/FalskIdentitet")

    id: Union[str, FalskIdentitetId] = None
    er_falsk: Union[bool, Bool] = None
    rett_identitet_er_ukjent: Optional[Union[bool, Bool]] = None
    rett_identitet: Optional[Union[str, PersonId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FalskIdentitetId):
            self.id = FalskIdentitetId(self.id)

        if self._is_empty(self.er_falsk):
            self.MissingRequiredField("er_falsk")
        if not isinstance(self.er_falsk, Bool):
            self.er_falsk = Bool(self.er_falsk)

        if self.rett_identitet_er_ukjent is not None and not isinstance(self.rett_identitet_er_ukjent, Bool):
            self.rett_identitet_er_ukjent = Bool(self.rett_identitet_er_ukjent)

        if self.rett_identitet is not None and not isinstance(self.rett_identitet, PersonId):
            self.rett_identitet = PersonId(self.rett_identitet)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Identifikasjonsdokument(YAMLRoot):
    """
    Utanlandsk identifikasjonsdokument som pass, førekort eller nasjonalt ID-kort knytt til ein person.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Identifikasjonsdokument"]
    class_class_curie: ClassVar[str] = "ngrp:Identifikasjonsdokument"
    class_name: ClassVar[str] = "Identifikasjonsdokument"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Identifikasjonsdokument")

    id: Union[str, IdentifikasjonsdokumentId] = None
    dokumenttype: Union[str, "IdentifikasjonsdokumentType"] = None
    dokumentnummer: str = None
    utstederland: Optional[str] = None
    utstedtdato: Optional[Union[str, XSDDate]] = None
    utloepsdato: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentifikasjonsdokumentId):
            self.id = IdentifikasjonsdokumentId(self.id)

        if self._is_empty(self.dokumenttype):
            self.MissingRequiredField("dokumenttype")
        if not isinstance(self.dokumenttype, IdentifikasjonsdokumentType):
            self.dokumenttype = IdentifikasjonsdokumentType(self.dokumenttype)

        if self._is_empty(self.dokumentnummer):
            self.MissingRequiredField("dokumentnummer")
        if not isinstance(self.dokumentnummer, str):
            self.dokumentnummer = str(self.dokumentnummer)

        if self.utstederland is not None and not isinstance(self.utstederland, str):
            self.utstederland = str(self.utstederland)

        if self.utstedtdato is not None and not isinstance(self.utstedtdato, XSDDate):
            self.utstedtdato = XSDDate(self.utstedtdato)

        if self.utloepsdato is not None and not isinstance(self.utloepsdato, XSDDate):
            self.utloepsdato = XSDDate(self.utloepsdato)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Identitetsgrunnlag(YAMLRoot):
    """
    Grunnlaget som er brukt for å fastsetje identiteten til ein person ved registrering i Folkeregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Identitetsgrunnlag"]
    class_class_curie: ClassVar[str] = "ngrp:Identitetsgrunnlag"
    class_name: ClassVar[str] = "Identitetsgrunnlag"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Identitetsgrunnlag")

    id: Union[str, IdentitetsgrunnlagId] = None
    identitetsgrunnlag_status: str = None
    identitetsgrunnlag_kilde: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentitetsgrunnlagId):
            self.id = IdentitetsgrunnlagId(self.id)

        if self._is_empty(self.identitetsgrunnlag_status):
            self.MissingRequiredField("identitetsgrunnlag_status")
        if not isinstance(self.identitetsgrunnlag_status, str):
            self.identitetsgrunnlag_status = str(self.identitetsgrunnlag_status)

        if self.identitetsgrunnlag_kilde is not None and not isinstance(self.identitetsgrunnlag_kilde, str):
            self.identitetsgrunnlag_kilde = str(self.identitetsgrunnlag_kilde)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kjoenn(YAMLRoot):
    """
    Kjønn registrert på ein person i Folkeregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Kjoenn"]
    class_class_curie: ClassVar[str] = "ngrp:Kjoenn"
    class_name: ClassVar[str] = "Kjoenn"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Kjoenn")

    id: Union[str, KjoennId] = None
    kjoenn_kode: Union[str, "KjoennKode"] = None
    gyldig_fra_og_med: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KjoennId):
            self.id = KjoennId(self.id)

        if self._is_empty(self.kjoenn_kode):
            self.MissingRequiredField("kjoenn_kode")
        if not isinstance(self.kjoenn_kode, KjoennKode):
            self.kjoenn_kode = KjoennKode(self.kjoenn_kode)

        if self.gyldig_fra_og_med is not None and not isinstance(self.gyldig_fra_og_med, XSDDate):
            self.gyldig_fra_og_med = XSDDate(self.gyldig_fra_og_med)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sivilstand(YAMLRoot):
    """
    Sivilstand registrert på ein person i Folkeregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Sivilstand"]
    class_class_curie: ClassVar[str] = "ngrp:Sivilstand"
    class_name: ClassVar[str] = "Sivilstand"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Sivilstand")

    id: Union[str, SivilstandId] = None
    sivilstand_type: Union[str, "SivilstandType"] = None
    gyldig_fra_og_med: Optional[Union[str, XSDDate]] = None
    relatert_ved_sivilstand: Optional[Union[str, PersonId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SivilstandId):
            self.id = SivilstandId(self.id)

        if self._is_empty(self.sivilstand_type):
            self.MissingRequiredField("sivilstand_type")
        if not isinstance(self.sivilstand_type, SivilstandType):
            self.sivilstand_type = SivilstandType(self.sivilstand_type)

        if self.gyldig_fra_og_med is not None and not isinstance(self.gyldig_fra_og_med, XSDDate):
            self.gyldig_fra_og_med = XSDDate(self.gyldig_fra_og_med)

        if self.relatert_ved_sivilstand is not None and not isinstance(self.relatert_ved_sivilstand, PersonId):
            self.relatert_ved_sivilstand = PersonId(self.relatert_ved_sivilstand)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Personstatus(YAMLRoot):
    """
    Status for ein person i Folkeregisteret (t.d. bosatt, utflyttet, død).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Personstatus"]
    class_class_curie: ClassVar[str] = "ngrp:Personstatus"
    class_name: ClassVar[str] = "Personstatus"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Personstatus")

    id: Union[str, PersonstatusId] = None
    personstatus_type: Union[str, "PersonstatusType"] = None
    gyldig_fra_og_med: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonstatusId):
            self.id = PersonstatusId(self.id)

        if self._is_empty(self.personstatus_type):
            self.MissingRequiredField("personstatus_type")
        if not isinstance(self.personstatus_type, PersonstatusType):
            self.personstatus_type = PersonstatusType(self.personstatus_type)

        if self.gyldig_fra_og_med is not None and not isinstance(self.gyldig_fra_og_med, XSDDate):
            self.gyldig_fra_og_med = XSDDate(self.gyldig_fra_og_med)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Statsborgerskap(YAMLRoot):
    """
    Statsborgerskap registrert på ein person i Folkeregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Statsborgerskap"]
    class_class_curie: ClassVar[str] = "ngrp:Statsborgerskap"
    class_name: ClassVar[str] = "Statsborgerskap"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Statsborgerskap")

    id: Union[str, StatsborgerskapId] = None
    landkode: str = None
    gyldig_fra_og_med: Optional[Union[str, XSDDate]] = None
    gyldig_til_og_med: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StatsborgerskapId):
            self.id = StatsborgerskapId(self.id)

        if self._is_empty(self.landkode):
            self.MissingRequiredField("landkode")
        if not isinstance(self.landkode, str):
            self.landkode = str(self.landkode)

        if self.gyldig_fra_og_med is not None and not isinstance(self.gyldig_fra_og_med, XSDDate):
            self.gyldig_fra_og_med = XSDDate(self.gyldig_fra_og_med)

        if self.gyldig_til_og_med is not None and not isinstance(self.gyldig_til_og_med, XSDDate):
            self.gyldig_til_og_med = XSDDate(self.gyldig_til_og_med)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Opphold(YAMLRoot):
    """
    Lovleg opphaldsgrunnlag for utanlandske statsborgarar registrert i Folkeregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Opphold"]
    class_class_curie: ClassVar[str] = "ngrp:Opphold"
    class_name: ClassVar[str] = "Opphold"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Opphold")

    id: Union[str, OppholdId] = None
    oppholds_type: Union[str, "OppholdstypeKode"] = None
    gyldig_fra_og_med: Union[str, XSDDate] = None
    gyldig_til_og_med: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OppholdId):
            self.id = OppholdId(self.id)

        if self._is_empty(self.oppholds_type):
            self.MissingRequiredField("oppholds_type")
        if not isinstance(self.oppholds_type, OppholdstypeKode):
            self.oppholds_type = OppholdstypeKode(self.oppholds_type)

        if self._is_empty(self.gyldig_fra_og_med):
            self.MissingRequiredField("gyldig_fra_og_med")
        if not isinstance(self.gyldig_fra_og_med, XSDDate):
            self.gyldig_fra_og_med = XSDDate(self.gyldig_fra_og_med)

        if self.gyldig_til_og_med is not None and not isinstance(self.gyldig_til_og_med, XSDDate):
            self.gyldig_til_og_med = XSDDate(self.gyldig_til_og_med)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Foedsel(YAMLRoot):
    """
    Fødselsinformasjon om ein person registrert i Folkeregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Foedsel"]
    class_class_curie: ClassVar[str] = "ngrp:Foedsel"
    class_name: ClassVar[str] = "Foedsel"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Foedsel")

    id: Union[str, FoedselId] = None
    foedselsaar: int = None
    foedselsdato: Optional[Union[str, XSDDate]] = None
    foedested: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoedselId):
            self.id = FoedselId(self.id)

        if self._is_empty(self.foedselsaar):
            self.MissingRequiredField("foedselsaar")
        if not isinstance(self.foedselsaar, int):
            self.foedselsaar = int(self.foedselsaar)

        if self.foedselsdato is not None and not isinstance(self.foedselsdato, XSDDate):
            self.foedselsdato = XSDDate(self.foedselsdato)

        if self.foedested is not None and not isinstance(self.foedested, str):
            self.foedested = str(self.foedested)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dodsfall(YAMLRoot):
    """
    Dødsfallsinformasjon om ein person registrert i Folkeregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Dodsfall"]
    class_class_curie: ClassVar[str] = "ngrp:Dodsfall"
    class_name: ClassVar[str] = "Dodsfall"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Dodsfall")

    id: Union[str, DodsfallId] = None
    doedsdato: Union[str, XSDDate] = None
    doedssted: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DodsfallId):
            self.id = DodsfallId(self.id)

        if self._is_empty(self.doedsdato):
            self.MissingRequiredField("doedsdato")
        if not isinstance(self.doedsdato, XSDDate):
            self.doedsdato = XSDDate(self.doedsdato)

        if self.doedssted is not None and not isinstance(self.doedssted, str):
            self.doedssted = str(self.doedssted)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KontaktinformasjonDoedsbo(YAMLRoot):
    """
    Kontaktinformasjon for eit dødsbu.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["KontaktinformasjonDoedsbo"]
    class_class_curie: ClassVar[str] = "ngrp:KontaktinformasjonDoedsbo"
    class_name: ClassVar[str] = "KontaktinformasjonDoedsbo"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/KontaktinformasjonDoedsbo")

    id: Union[str, KontaktinformasjonDoedsboId] = None
    navn: str = None
    telefonnummer: Optional[str] = None
    epostadresse_verdi: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KontaktinformasjonDoedsboId):
            self.id = KontaktinformasjonDoedsboId(self.id)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.telefonnummer is not None and not isinstance(self.telefonnummer, str):
            self.telefonnummer = str(self.telefonnummer)

        if self.epostadresse_verdi is not None and not isinstance(self.epostadresse_verdi, str):
            self.epostadresse_verdi = str(self.epostadresse_verdi)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ForeldreansvarForelder(YAMLRoot):
    """
    Relasjonsklasse som registrerer kven som har det juridiske foreldreansvaret for eit barn. Seier kven som er den
    ansvarlege forelderen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["ForeldreansvarForelder"]
    class_class_curie: ClassVar[str] = "ngrp:ForeldreansvarForelder"
    class_name: ClassVar[str] = "ForeldreansvarForelder"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/ForeldreansvarForelder")

    id: Union[str, ForeldreansvarForelderId] = None
    er_av_type_person: Union[str, PersonId] = None
    ansvarsstatus: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ForeldreansvarForelderId):
            self.id = ForeldreansvarForelderId(self.id)

        if self._is_empty(self.er_av_type_person):
            self.MissingRequiredField("er_av_type_person")
        if not isinstance(self.er_av_type_person, PersonId):
            self.er_av_type_person = PersonId(self.er_av_type_person)

        if self.ansvarsstatus is not None and not isinstance(self.ansvarsstatus, str):
            self.ansvarsstatus = str(self.ansvarsstatus)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ForeldreansvarBarn(YAMLRoot):
    """
    Relasjonsklasse som registrerer at eit barn er under foreldreansvaret til ein person.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["ForeldreansvarBarn"]
    class_class_curie: ClassVar[str] = "ngrp:ForeldreansvarBarn"
    class_name: ClassVar[str] = "ForeldreansvarBarn"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/ForeldreansvarBarn")

    id: Union[str, ForeldreansvarBarnId] = None
    er_av_type_person: Union[str, PersonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ForeldreansvarBarnId):
            self.id = ForeldreansvarBarnId(self.id)

        if self._is_empty(self.er_av_type_person):
            self.MissingRequiredField("er_av_type_person")
        if not isinstance(self.er_av_type_person, PersonId):
            self.er_av_type_person = PersonId(self.er_av_type_person)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilierelasjonForelder(YAMLRoot):
    """
    Familierelasjon der den relaterte personen er forelder.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["FamilierelasjonForelder"]
    class_class_curie: ClassVar[str] = "ngrp:FamilierelasjonForelder"
    class_name: ClassVar[str] = "FamilierelasjonForelder"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/FamilierelasjonForelder")

    id: Union[str, FamilierelasjonForelderId] = None
    er_av_type_person: Union[str, PersonId] = None
    foreldrerelasjon_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FamilierelasjonForelderId):
            self.id = FamilierelasjonForelderId(self.id)

        if self._is_empty(self.er_av_type_person):
            self.MissingRequiredField("er_av_type_person")
        if not isinstance(self.er_av_type_person, PersonId):
            self.er_av_type_person = PersonId(self.er_av_type_person)

        if self.foreldrerelasjon_type is not None and not isinstance(self.foreldrerelasjon_type, str):
            self.foreldrerelasjon_type = str(self.foreldrerelasjon_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilierelasjonBarn(YAMLRoot):
    """
    Familierelasjon der den relaterte personen er barn.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["FamilierelasjonBarn"]
    class_class_curie: ClassVar[str] = "ngrp:FamilierelasjonBarn"
    class_name: ClassVar[str] = "FamilierelasjonBarn"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/FamilierelasjonBarn")

    id: Union[str, FamilierelasjonBarnId] = None
    er_av_type_person: Union[str, PersonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FamilierelasjonBarnId):
            self.id = FamilierelasjonBarnId(self.id)

        if self._is_empty(self.er_av_type_person):
            self.MissingRequiredField("er_av_type_person")
        if not isinstance(self.er_av_type_person, PersonId):
            self.er_av_type_person = PersonId(self.er_av_type_person)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilierelasjonEktefelle(YAMLRoot):
    """
    Familierelasjon der den relaterte personen er ektefelle eller registrert partnar. Dette er strengt tatt same
    informasjon som sivilstand GIFT.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["FamilierelasjonEktefelle"]
    class_class_curie: ClassVar[str] = "ngrp:FamilierelasjonEktefelle"
    class_name: ClassVar[str] = "FamilierelasjonEktefelle"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/FamilierelasjonEktefelle")

    id: Union[str, FamilierelasjonEktefelleId] = None
    er_av_type_person: Union[str, PersonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FamilierelasjonEktefelleId):
            self.id = FamilierelasjonEktefelleId(self.id)

        if self._is_empty(self.er_av_type_person):
            self.MissingRequiredField("er_av_type_person")
        if not isinstance(self.er_av_type_person, PersonId):
            self.er_av_type_person = PersonId(self.er_av_type_person)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InnflyttingTilNorge(YAMLRoot):
    """
    Registrering av innflytting til Noreg i Folkeregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["InnflyttingTilNorge"]
    class_class_curie: ClassVar[str] = "ngrp:InnflyttingTilNorge"
    class_name: ClassVar[str] = "InnflyttingTilNorge"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/InnflyttingTilNorge")

    id: Union[str, InnflyttingTilNorgeId] = None
    innflyttingsdato: Union[str, XSDDate] = None
    fraflyttingsland: Optional[str] = None
    fraflyttingssted_i_utlandet: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InnflyttingTilNorgeId):
            self.id = InnflyttingTilNorgeId(self.id)

        if self._is_empty(self.innflyttingsdato):
            self.MissingRequiredField("innflyttingsdato")
        if not isinstance(self.innflyttingsdato, XSDDate):
            self.innflyttingsdato = XSDDate(self.innflyttingsdato)

        if self.fraflyttingsland is not None and not isinstance(self.fraflyttingsland, str):
            self.fraflyttingsland = str(self.fraflyttingsland)

        if self.fraflyttingssted_i_utlandet is not None and not isinstance(self.fraflyttingssted_i_utlandet, str):
            self.fraflyttingssted_i_utlandet = str(self.fraflyttingssted_i_utlandet)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UtflyttingFraNorge(YAMLRoot):
    """
    Registrering av utflytting frå Noreg i Folkeregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["UtflyttingFraNorge"]
    class_class_curie: ClassVar[str] = "ngrp:UtflyttingFraNorge"
    class_name: ClassVar[str] = "UtflyttingFraNorge"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/UtflyttingFraNorge")

    id: Union[str, UtflyttingFraNorgeId] = None
    utflyttingsdato: Union[str, XSDDate] = None
    tilflyttingsland: Optional[str] = None
    tilflyttingssted_i_utlandet: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UtflyttingFraNorgeId):
            self.id = UtflyttingFraNorgeId(self.id)

        if self._is_empty(self.utflyttingsdato):
            self.MissingRequiredField("utflyttingsdato")
        if not isinstance(self.utflyttingsdato, XSDDate):
            self.utflyttingsdato = XSDDate(self.utflyttingsdato)

        if self.tilflyttingsland is not None and not isinstance(self.tilflyttingsland, str):
            self.tilflyttingsland = str(self.tilflyttingsland)

        if self.tilflyttingssted_i_utlandet is not None and not isinstance(self.tilflyttingssted_i_utlandet, str):
            self.tilflyttingssted_i_utlandet = str(self.tilflyttingssted_i_utlandet)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeografiskAdresse(YAMLRoot):
    """
    Abstrakt klasse for geografiske adresser. Tilhøyrer Domene adresse og forvaltast av Matrikkelen. Konkrete typar er
    Bostedsadresse, Postadresse og Oppholdsadresse.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["GeografiskAdresse"]
    class_class_curie: ClassVar[str] = "ngrp:GeografiskAdresse"
    class_name: ClassVar[str] = "GeografiskAdresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/GeografiskAdresse")

    id: Union[str, GeografiskAdresseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeografiskAdresseId):
            self.id = GeografiskAdresseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bostedsadresse(GeografiskAdresse):
    """
    Adressa personen er registrert busett på i Folkeregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Bostedsadresse"]
    class_class_curie: ClassVar[str] = "ngrp:Bostedsadresse"
    class_name: ClassVar[str] = "Bostedsadresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Bostedsadresse")

    id: Union[str, BostedsadresseId] = None
    gyldig_fra_og_med: Optional[Union[str, XSDDate]] = None
    gyldig_til_og_med: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BostedsadresseId):
            self.id = BostedsadresseId(self.id)

        if self.gyldig_fra_og_med is not None and not isinstance(self.gyldig_fra_og_med, XSDDate):
            self.gyldig_fra_og_med = XSDDate(self.gyldig_fra_og_med)

        if self.gyldig_til_og_med is not None and not isinstance(self.gyldig_til_og_med, XSDDate):
            self.gyldig_til_og_med = XSDDate(self.gyldig_til_og_med)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Postadresse(GeografiskAdresse):
    """
    Adressa der personen mottar post.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Postadresse"]
    class_class_curie: ClassVar[str] = "ngrp:Postadresse"
    class_name: ClassVar[str] = "Postadresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Postadresse")

    id: Union[str, PostadresseId] = None
    gyldig_fra_og_med: Optional[Union[str, XSDDate]] = None
    gyldig_til_og_med: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PostadresseId):
            self.id = PostadresseId(self.id)

        if self.gyldig_fra_og_med is not None and not isinstance(self.gyldig_fra_og_med, XSDDate):
            self.gyldig_fra_og_med = XSDDate(self.gyldig_fra_og_med)

        if self.gyldig_til_og_med is not None and not isinstance(self.gyldig_til_og_med, XSDDate):
            self.gyldig_til_og_med = XSDDate(self.gyldig_til_og_med)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Oppholdsadresse(GeografiskAdresse):
    """
    Adressa der personen faktisk oppheld seg (ikkje nødvendigvis bustadsadressa).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Oppholdsadresse"]
    class_class_curie: ClassVar[str] = "ngrp:Oppholdsadresse"
    class_name: ClassVar[str] = "Oppholdsadresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Oppholdsadresse")

    id: Union[str, OppholdsadresseId] = None
    gyldig_fra_og_med: Optional[Union[str, XSDDate]] = None
    gyldig_til_og_med: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OppholdsadresseId):
            self.id = OppholdsadresseId(self.id)

        if self.gyldig_fra_og_med is not None and not isinstance(self.gyldig_fra_og_med, XSDDate):
            self.gyldig_fra_og_med = XSDDate(self.gyldig_fra_og_med)

        if self.gyldig_til_og_med is not None and not isinstance(self.gyldig_til_og_med, XSDDate):
            self.gyldig_til_og_med = XSDDate(self.gyldig_til_og_med)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Adressebeskyttelse(YAMLRoot):
    """
    Gradering av adressebeskyttelse for innflyttede personar til Noreg. Tidlegare kalla kode 6 (strengt fortroleg) og
    kode 7 (fortroleg).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Adressebeskyttelse"]
    class_class_curie: ClassVar[str] = "ngrp:Adressebeskyttelse"
    class_name: ClassVar[str] = "Adressebeskyttelse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Adressebeskyttelse")

    id: Union[str, AdressebeskyttelseId] = None
    adressebeskyttelse_gradering: Union[str, "AdressebeskyttelseGradering"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdressebeskyttelseId):
            self.id = AdressebeskyttelseId(self.id)

        if self._is_empty(self.adressebeskyttelse_gradering):
            self.MissingRequiredField("adressebeskyttelse_gradering")
        if not isinstance(self.adressebeskyttelse_gradering, AdressebeskyttelseGradering):
            self.adressebeskyttelse_gradering = AdressebeskyttelseGradering(self.adressebeskyttelse_gradering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Verge(YAMLRoot):
    """
    Ein verje (anten person eller institusjon) som er oppnemnd for å ivareta interessene til ein person. Er av type
    Person.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Verge"]
    class_class_curie: ClassVar[str] = "ngrp:Verge"
    class_name: ClassVar[str] = "Verge"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Verge")

    id: Union[str, VergeId] = None
    er_av_type_person: Union[str, PersonId] = None
    vergetype: Optional[Union[str, "VergetypeKode"]] = None
    embete: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VergeId):
            self.id = VergeId(self.id)

        if self._is_empty(self.er_av_type_person):
            self.MissingRequiredField("er_av_type_person")
        if not isinstance(self.er_av_type_person, PersonId):
            self.er_av_type_person = PersonId(self.er_av_type_person)

        if self.vergetype is not None and not isinstance(self.vergetype, VergetypeKode):
            self.vergetype = VergetypeKode(self.vergetype)

        if self.embete is not None and not isinstance(self.embete, str):
            self.embete = str(self.embete)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RettsligHandleevne(YAMLRoot):
    """
    Registrering av avgrensing i rettsleg handleevne for ein person, t.d. under vergemål eller fråtatt rettsleg
    handleevne.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["RettsligHandleevne"]
    class_class_curie: ClassVar[str] = "ngrp:RettsligHandleevne"
    class_name: ClassVar[str] = "RettsligHandleevne"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/RettsligHandleevne")

    id: Union[str, RettsligHandleevneId] = None
    rettslig_handleevne_type: Union[str, "RettsligHandleevneType"] = None
    omfang: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RettsligHandleevneId):
            self.id = RettsligHandleevneId(self.id)

        if self._is_empty(self.rettslig_handleevne_type):
            self.MissingRequiredField("rettslig_handleevne_type")
        if not isinstance(self.rettslig_handleevne_type, RettsligHandleevneType):
            self.rettslig_handleevne_type = RettsligHandleevneType(self.rettslig_handleevne_type)

        if self.omfang is not None and not isinstance(self.omfang, str):
            self.omfang = str(self.omfang)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReservasjonMotKommunikasjonPaaNett(YAMLRoot):
    """
    Registrering av at ein person har reservert seg mot digital kommunikasjon frå det offentlege. Forvaltast av
    Kontakt- og reservasjonsregisteret (KRR).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["ReservasjonMotKommunikasjonPaaNett"]
    class_class_curie: ClassVar[str] = "ngrp:ReservasjonMotKommunikasjonPaaNett"
    class_name: ClassVar[str] = "ReservasjonMotKommunikasjonPaaNett"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/ReservasjonMotKommunikasjonPaaNett")

    id: Union[str, ReservasjonMotKommunikasjonPaaNettId] = None
    er_reservert: Union[bool, Bool] = None
    gyldig_fra_og_med: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReservasjonMotKommunikasjonPaaNettId):
            self.id = ReservasjonMotKommunikasjonPaaNettId(self.id)

        if self._is_empty(self.er_reservert):
            self.MissingRequiredField("er_reservert")
        if not isinstance(self.er_reservert, Bool):
            self.er_reservert = Bool(self.er_reservert)

        if self.gyldig_fra_og_med is not None and not isinstance(self.gyldig_fra_og_med, XSDDate):
            self.gyldig_fra_og_med = XSDDate(self.gyldig_fra_og_med)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontaktopplysninger(YAMLRoot):
    """
    Kontaktopplysningar (e-post og mobilnummer) for digital kommunikasjon med det offentlege. Forvaltast av Kontakt-
    og reservasjonsregisteret (KRR).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["Kontaktopplysninger"]
    class_class_curie: ClassVar[str] = "ngrp:Kontaktopplysninger"
    class_name: ClassVar[str] = "Kontaktopplysninger"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/Kontaktopplysninger")

    id: Union[str, KontaktopplysningerId] = None
    epostadresse_verdi: Optional[str] = None
    mobiltelefonnummer: Optional[str] = None
    sist_oppdatert: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KontaktopplysningerId):
            self.id = KontaktopplysningerId(self.id)

        if self.epostadresse_verdi is not None and not isinstance(self.epostadresse_verdi, str):
            self.epostadresse_verdi = str(self.epostadresse_verdi)

        if self.mobiltelefonnummer is not None and not isinstance(self.mobiltelefonnummer, str):
            self.mobiltelefonnummer = str(self.mobiltelefonnummer)

        if self.sist_oppdatert is not None and not isinstance(self.sist_oppdatert, XSDDate):
            self.sist_oppdatert = XSDDate(self.sist_oppdatert)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpraakForElektroniskKommunikasjon(YAMLRoot):
    """
    Føretrekt språk for elektronisk kommunikasjon med offentlege styresmakter, valt av personen sjølv.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRP["SpraakForElektroniskKommunikasjon"]
    class_class_curie: ClassVar[str] = "ngrp:SpraakForElektroniskKommunikasjon"
    class_name: ClassVar[str] = "SpraakForElektroniskKommunikasjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-person/SpraakForElektroniskKommunikasjon")

    id: Union[str, SpraakForElektroniskKommunikasjonId] = None
    spraakkode: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpraakForElektroniskKommunikasjonId):
            self.id = SpraakForElektroniskKommunikasjonId(self.id)

        if self._is_empty(self.spraakkode):
            self.MissingRequiredField("spraakkode")
        if not isinstance(self.spraakkode, str):
            self.spraakkode = str(self.spraakkode)

        super().__post_init__(**kwargs)


# Enumerations
class KjoennKode(EnumDefinitionImpl):
    """
    Kjønn registrert i Folkeregisteret.
    """
    MANN = PermissibleValue(
        text="MANN",
        description="Mann")
    KVINNE = PermissibleValue(
        text="KVINNE",
        description="Kvinne")
    UKJENT = PermissibleValue(
        text="UKJENT",
        description="Ukjent kjønn")

    _defn = EnumDefinition(
        name="KjoennKode",
        description="Kjønn registrert i Folkeregisteret.",
    )

class SivilstandType(EnumDefinitionImpl):
    """
    Sivilstandskode frå Folkeregisteret.
    """
    UOPPGITT = PermissibleValue(
        text="UOPPGITT",
        description="Uoppgitt")
    UGIFT = PermissibleValue(
        text="UGIFT",
        description="Ugift")
    GIFT = PermissibleValue(
        text="GIFT",
        description="Gift")
    ENKE_ELLER_ENKEMANN = PermissibleValue(
        text="ENKE_ELLER_ENKEMANN",
        description="Enke eller enkemann")
    SKILT = PermissibleValue(
        text="SKILT",
        description="Skilt")
    SEPARERT = PermissibleValue(
        text="SEPARERT",
        description="Separert")
    REGISTRERT_PARTNER = PermissibleValue(
        text="REGISTRERT_PARTNER",
        description="Registrert partner")
    SEPARERT_PARTNER = PermissibleValue(
        text="SEPARERT_PARTNER",
        description="Separert partner")
    SKILT_PARTNER = PermissibleValue(
        text="SKILT_PARTNER",
        description="Skilt partner")
    ETTERLATT_PARTNER = PermissibleValue(
        text="ETTERLATT_PARTNER",
        description="Etterlatt partner")

    _defn = EnumDefinition(
        name="SivilstandType",
        description="Sivilstandskode frå Folkeregisteret.",
    )

class PersonstatusType(EnumDefinitionImpl):
    """
    Personens status i Folkeregisteret.
    """
    BOSATT = PermissibleValue(
        text="BOSATT",
        description="Bosatt i Noreg")
    UTFLYTTET = PermissibleValue(
        text="UTFLYTTET",
        description="Utflytta frå Noreg")
    DOED = PermissibleValue(
        text="DOED",
        description="Død")
    OPPHORT = PermissibleValue(
        text="OPPHORT",
        description="Opphørt (fjerna frå registeret)")
    INAKTIV = PermissibleValue(
        text="INAKTIV",
        description="Inaktiv")
    MIDLERTIDIG = PermissibleValue(
        text="MIDLERTIDIG",
        description="Midlertidig registrert")
    FORSVUNNET = PermissibleValue(
        text="FORSVUNNET",
        description="Forsvunnen")

    _defn = EnumDefinition(
        name="PersonstatusType",
        description="Personens status i Folkeregisteret.",
    )

class OppholdstypeKode(EnumDefinitionImpl):
    """
    Type opphaldstillatelse registrert i Folkeregisteret.
    """
    MIDLERTIDIG = PermissibleValue(
        text="MIDLERTIDIG",
        description="Mellombels opphaldsløyve")
    PERMANENT = PermissibleValue(
        text="PERMANENT",
        description="Permanent opphaldsløyve")
    OPPLYSNING_MANGLER = PermissibleValue(
        text="OPPLYSNING_MANGLER",
        description="Opplysning manglar")

    _defn = EnumDefinition(
        name="OppholdstypeKode",
        description="Type opphaldstillatelse registrert i Folkeregisteret.",
    )

class AdressebeskyttelseGradering(EnumDefinitionImpl):
    """
    Gradering av adressebeskyttelse (tidlegare kode 6/7).
    """
    STRENGT_FORTROLIG = PermissibleValue(
        text="STRENGT_FORTROLIG",
        description="Strengt fortroleg adresse (tidlegare kode 6)")
    FORTROLIG = PermissibleValue(
        text="FORTROLIG",
        description="Fortroleg adresse (tidlegare kode 7)")
    STRENGT_FORTROLIG_UTLAND = PermissibleValue(
        text="STRENGT_FORTROLIG_UTLAND",
        description="Strengt fortroleg adresse i utlandet")
    UGRADERT = PermissibleValue(
        text="UGRADERT",
        description="Ikkje adressebeskyttelse")

    _defn = EnumDefinition(
        name="AdressebeskyttelseGradering",
        description="Gradering av adressebeskyttelse (tidlegare kode 6/7).",
    )

class IdentifikasjonsdokumentType(EnumDefinitionImpl):
    """
    Type utanlandsk identifikasjonsdokument.
    """
    PASS = PermissibleValue(
        text="PASS",
        description="Pass")
    FOERERKORT = PermissibleValue(
        text="FOERERKORT",
        description="Førekort")
    NASJONAL_ID_KORT = PermissibleValue(
        text="NASJONAL_ID_KORT",
        description="Nasjonalt ID-kort")
    OPPHOLDSTILLATELSE = PermissibleValue(
        text="OPPHOLDSTILLATELSE",
        description="Opphaldsløyve")
    ANNET = PermissibleValue(
        text="ANNET",
        description="Anna dokument")

    _defn = EnumDefinition(
        name="IdentifikasjonsdokumentType",
        description="Type utanlandsk identifikasjonsdokument.",
    )

class RettsligHandleevneType(EnumDefinitionImpl):
    """
    Type avgrensing av rettsleg handleevne.
    """
    UNDER_VERGEMAAL = PermissibleValue(
        text="UNDER_VERGEMAAL",
        description="Under vergemål")
    FRATATT_RETTSLIG_HANDLEEVNE_PERSONLIG = PermissibleValue(
        text="FRATATT_RETTSLIG_HANDLEEVNE_PERSONLIG",
        description="Fråtatt rettsleg handleevne i personlege tilhøve")
    FRATATT_RETTSLIG_HANDLEEVNE_OKONOMISK = PermissibleValue(
        text="FRATATT_RETTSLIG_HANDLEEVNE_OKONOMISK",
        description="Fråtatt rettsleg handleevne i formueretslige tilhøve")

    _defn = EnumDefinition(
        name="RettsligHandleevneType",
        description="Type avgrensing av rettsleg handleevne.",
    )

class VergetypeKode(EnumDefinitionImpl):
    """
    Type vergemål.
    """
    ENSLIG_MINDREAARIG_ASYLSOEKER = PermissibleValue(
        text="ENSLIG_MINDREAARIG_ASYLSOEKER",
        description="Einsleg mindreårig asylsøkjar")
    MINDREAARIG = PermissibleValue(
        text="MINDREAARIG",
        description="Mindreårig")
    VOKSEN = PermissibleValue(
        text="VOKSEN",
        description="Vaksen")
    MIDLERTIDIG_FOR_VOKSEN = PermissibleValue(
        text="MIDLERTIDIG_FOR_VOKSEN",
        description="Mellombels for vaksen")

    _defn = EnumDefinition(
        name="VergetypeKode",
        description="Type vergemål.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.har_personnavn = Slot(uri=NGRP.harPersonnavn, name="har_personnavn", curie=NGRP.curie('harPersonnavn'),
                   model_uri=DEFAULT_.har_personnavn, domain=None, range=Optional[Union[str, PersonnavnId]])

slots.har_folkeregisteridentifikator = Slot(uri=NGRP.harFolkeregisteridentifikator, name="har_folkeregisteridentifikator", curie=NGRP.curie('harFolkeregisteridentifikator'),
                   model_uri=DEFAULT_.har_folkeregisteridentifikator, domain=None, range=Optional[Union[str, FolkeregisteridentifikatorId]])

slots.har_personidentifikasjon = Slot(uri=NGRP.harPersonidentifikasjon, name="har_personidentifikasjon", curie=NGRP.curie('harPersonidentifikasjon'),
                   model_uri=DEFAULT_.har_personidentifikasjon, domain=None, range=Optional[Union[Union[str, PersonidentifikasjonId], list[Union[str, PersonidentifikasjonId]]]])

slots.har_falsk_identitet = Slot(uri=NGRP.harFalskIdentitet, name="har_falsk_identitet", curie=NGRP.curie('harFalskIdentitet'),
                   model_uri=DEFAULT_.har_falsk_identitet, domain=None, range=Optional[Union[str, FalskIdentitetId]])

slots.har_utenlandsk_identifikasjonsdokument = Slot(uri=NGRP.harUtenlandskIdentifikasjonsdokument, name="har_utenlandsk_identifikasjonsdokument", curie=NGRP.curie('harUtenlandskIdentifikasjonsdokument'),
                   model_uri=DEFAULT_.har_utenlandsk_identifikasjonsdokument, domain=None, range=Optional[Union[Union[str, IdentifikasjonsdokumentId], list[Union[str, IdentifikasjonsdokumentId]]]])

slots.har_identitetsgrunnlag = Slot(uri=NGRP.harIdentitetsgrunnlag, name="har_identitetsgrunnlag", curie=NGRP.curie('harIdentitetsgrunnlag'),
                   model_uri=DEFAULT_.har_identitetsgrunnlag, domain=None, range=Optional[Union[str, IdentitetsgrunnlagId]])

slots.har_kjoenn = Slot(uri=NGRP.harKjoenn, name="har_kjoenn", curie=NGRP.curie('harKjoenn'),
                   model_uri=DEFAULT_.har_kjoenn, domain=None, range=Optional[Union[str, KjoennId]])

slots.har_sivilstand = Slot(uri=NGRP.harSivilstand, name="har_sivilstand", curie=NGRP.curie('harSivilstand'),
                   model_uri=DEFAULT_.har_sivilstand, domain=None, range=Optional[Union[str, SivilstandId]])

slots.har_personstatus = Slot(uri=NGRP.harPersonstatus, name="har_personstatus", curie=NGRP.curie('harPersonstatus'),
                   model_uri=DEFAULT_.har_personstatus, domain=None, range=Optional[Union[str, PersonstatusId]])

slots.har_statsborgerskap = Slot(uri=NGRP.harStatsborgerskap, name="har_statsborgerskap", curie=NGRP.curie('harStatsborgerskap'),
                   model_uri=DEFAULT_.har_statsborgerskap, domain=None, range=Optional[Union[Union[str, StatsborgerskapId], list[Union[str, StatsborgerskapId]]]])

slots.har_lovlig_opphold = Slot(uri=NGRP.harLovligOpphold, name="har_lovlig_opphold", curie=NGRP.curie('harLovligOpphold'),
                   model_uri=DEFAULT_.har_lovlig_opphold, domain=None, range=Optional[Union[str, OppholdId]])

slots.har_foedsel = Slot(uri=NGRP.harFoedsel, name="har_foedsel", curie=NGRP.curie('harFoedsel'),
                   model_uri=DEFAULT_.har_foedsel, domain=None, range=Optional[Union[str, FoedselId]])

slots.har_foreldreansvar_forelder = Slot(uri=NGRP.harForeldreansvarForelder, name="har_foreldreansvar_forelder", curie=NGRP.curie('harForeldreansvarForelder'),
                   model_uri=DEFAULT_.har_foreldreansvar_forelder, domain=None, range=Optional[Union[Union[str, ForeldreansvarForelderId], list[Union[str, ForeldreansvarForelderId]]]])

slots.har_foreldreansvar_barn = Slot(uri=NGRP.harForeldreansvarBarn, name="har_foreldreansvar_barn", curie=NGRP.curie('harForeldreansvarBarn'),
                   model_uri=DEFAULT_.har_foreldreansvar_barn, domain=None, range=Optional[Union[Union[str, ForeldreansvarBarnId], list[Union[str, ForeldreansvarBarnId]]]])

slots.har_familierelasjon_forelder = Slot(uri=NGRP.harFamilierelasjonForelder, name="har_familierelasjon_forelder", curie=NGRP.curie('harFamilierelasjonForelder'),
                   model_uri=DEFAULT_.har_familierelasjon_forelder, domain=None, range=Optional[Union[Union[str, FamilierelasjonForelderId], list[Union[str, FamilierelasjonForelderId]]]])

slots.har_familierelasjon_barn = Slot(uri=NGRP.harFamilierelasjonBarn, name="har_familierelasjon_barn", curie=NGRP.curie('harFamilierelasjonBarn'),
                   model_uri=DEFAULT_.har_familierelasjon_barn, domain=None, range=Optional[Union[Union[str, FamilierelasjonBarnId], list[Union[str, FamilierelasjonBarnId]]]])

slots.har_familierelasjon_ektefelle = Slot(uri=NGRP.harFamilierelasjonEktefelle, name="har_familierelasjon_ektefelle", curie=NGRP.curie('harFamilierelasjonEktefelle'),
                   model_uri=DEFAULT_.har_familierelasjon_ektefelle, domain=None, range=Optional[Union[str, FamilierelasjonEktefelleId]])

slots.har_dodsfall = Slot(uri=NGRP.harDodsfall, name="har_dodsfall", curie=NGRP.curie('harDodsfall'),
                   model_uri=DEFAULT_.har_dodsfall, domain=None, range=Optional[Union[str, DodsfallId]])

slots.har_kontaktinformasjon_doedsbo = Slot(uri=NGRP.harKontaktinformasjonDoedsbo, name="har_kontaktinformasjon_doedsbo", curie=NGRP.curie('harKontaktinformasjonDoedsbo'),
                   model_uri=DEFAULT_.har_kontaktinformasjon_doedsbo, domain=None, range=Optional[Union[str, KontaktinformasjonDoedsboId]])

slots.har_innflytting_til_norge = Slot(uri=NGRP.harInnflyttingTilNorge, name="har_innflytting_til_norge", curie=NGRP.curie('harInnflyttingTilNorge'),
                   model_uri=DEFAULT_.har_innflytting_til_norge, domain=None, range=Optional[Union[str, InnflyttingTilNorgeId]])

slots.har_utflytting_fra_norge = Slot(uri=NGRP.harUtflyttingFraNorge, name="har_utflytting_fra_norge", curie=NGRP.curie('harUtflyttingFraNorge'),
                   model_uri=DEFAULT_.har_utflytting_fra_norge, domain=None, range=Optional[Union[str, UtflyttingFraNorgeId]])

slots.har_adressebeskyttelse = Slot(uri=NGRP.harAdressebeskyttelse, name="har_adressebeskyttelse", curie=NGRP.curie('harAdressebeskyttelse'),
                   model_uri=DEFAULT_.har_adressebeskyttelse, domain=None, range=Optional[Union[str, AdressebeskyttelseId]])

slots.har_bosted_paa = Slot(uri=NGRP.harBostedPaa, name="har_bosted_paa", curie=NGRP.curie('harBostedPaa'),
                   model_uri=DEFAULT_.har_bosted_paa, domain=None, range=Optional[Union[str, BostedsadresseId]])

slots.mottar_post_paa = Slot(uri=NGRP.mottarPostPaa, name="mottar_post_paa", curie=NGRP.curie('mottarPostPaa'),
                   model_uri=DEFAULT_.mottar_post_paa, domain=None, range=Optional[Union[str, PostadresseId]])

slots.oppholder_seg_paa = Slot(uri=NGRP.oppholderSegPaa, name="oppholder_seg_paa", curie=NGRP.curie('oppholderSegPaa'),
                   model_uri=DEFAULT_.oppholder_seg_paa, domain=None, range=Optional[Union[str, OppholdsadresseId]])

slots.har_verge = Slot(uri=NGRP.harVerge, name="har_verge", curie=NGRP.curie('harVerge'),
                   model_uri=DEFAULT_.har_verge, domain=None, range=Optional[Union[Union[str, VergeId], list[Union[str, VergeId]]]])

slots.har_rettslig_handleevne = Slot(uri=NGRP.harRettsligHandleevne, name="har_rettslig_handleevne", curie=NGRP.curie('harRettsligHandleevne'),
                   model_uri=DEFAULT_.har_rettslig_handleevne, domain=None, range=Optional[Union[str, RettsligHandleevneId]])

slots.har_reservasjon_mot_kommunikasjon = Slot(uri=NGRP.harReservasjonMotKommunikasjon, name="har_reservasjon_mot_kommunikasjon", curie=NGRP.curie('harReservasjonMotKommunikasjon'),
                   model_uri=DEFAULT_.har_reservasjon_mot_kommunikasjon, domain=None, range=Optional[Union[str, ReservasjonMotKommunikasjonPaaNettId]])

slots.har_kontaktopplysninger = Slot(uri=NGRP.harKontaktopplysninger, name="har_kontaktopplysninger", curie=NGRP.curie('harKontaktopplysninger'),
                   model_uri=DEFAULT_.har_kontaktopplysninger, domain=None, range=Optional[Union[str, KontaktopplysningerId]])

slots.har_valgt_spraak = Slot(uri=NGRP.harValgtSpraak, name="har_valgt_spraak", curie=NGRP.curie('harValgtSpraak'),
                   model_uri=DEFAULT_.har_valgt_spraak, domain=None, range=Optional[Union[str, SpraakForElektroniskKommunikasjonId]])

slots.er_av_type_person = Slot(uri=NGRP.erAvTypePerson, name="er_av_type_person", curie=NGRP.curie('erAvTypePerson'),
                   model_uri=DEFAULT_.er_av_type_person, domain=None, range=Optional[Union[str, PersonId]])

slots.relatert_ved_sivilstand = Slot(uri=NGRP.relatertVedSivilstand, name="relatert_ved_sivilstand", curie=NGRP.curie('relatertVedSivilstand'),
                   model_uri=DEFAULT_.relatert_ved_sivilstand, domain=None, range=Optional[Union[str, PersonId]])

slots.rett_identitet = Slot(uri=NGRP.rettIdentitet, name="rett_identitet", curie=NGRP.curie('rettIdentitet'),
                   model_uri=DEFAULT_.rett_identitet, domain=None, range=Optional[Union[str, PersonId]])

slots.fornavn = Slot(uri=NGRP.fornavn, name="fornavn", curie=NGRP.curie('fornavn'),
                   model_uri=DEFAULT_.fornavn, domain=None, range=Optional[str])

slots.mellomnavn = Slot(uri=NGRP.mellomnavn, name="mellomnavn", curie=NGRP.curie('mellomnavn'),
                   model_uri=DEFAULT_.mellomnavn, domain=None, range=Optional[str])

slots.etternavn = Slot(uri=NGRP.etternavn, name="etternavn", curie=NGRP.curie('etternavn'),
                   model_uri=DEFAULT_.etternavn, domain=None, range=Optional[str])

slots.forkortet_navn = Slot(uri=NGRP.forkortetNavn, name="forkortet_navn", curie=NGRP.curie('forkortetNavn'),
                   model_uri=DEFAULT_.forkortet_navn, domain=None, range=Optional[str])

slots.identifikatornummer = Slot(uri=NGRP.identifikatornummer, name="identifikatornummer", curie=NGRP.curie('identifikatornummer'),
                   model_uri=DEFAULT_.identifikatornummer, domain=None, range=Optional[str])

slots.identifikasjonstype = Slot(uri=NGRP.identifikasjonstype, name="identifikasjonstype", curie=NGRP.curie('identifikasjonstype'),
                   model_uri=DEFAULT_.identifikasjonstype, domain=None, range=Optional[str])

slots.dokumenttype = Slot(uri=NGRP.dokumenttype, name="dokumenttype", curie=NGRP.curie('dokumenttype'),
                   model_uri=DEFAULT_.dokumenttype, domain=None, range=Optional[Union[str, "IdentifikasjonsdokumentType"]])

slots.dokumentnummer = Slot(uri=NGRP.dokumentnummer, name="dokumentnummer", curie=NGRP.curie('dokumentnummer'),
                   model_uri=DEFAULT_.dokumentnummer, domain=None, range=Optional[str])

slots.utstederland = Slot(uri=NGRP.utstederland, name="utstederland", curie=NGRP.curie('utstederland'),
                   model_uri=DEFAULT_.utstederland, domain=None, range=Optional[str])

slots.utstedtdato = Slot(uri=NGRP.utstedtdato, name="utstedtdato", curie=NGRP.curie('utstedtdato'),
                   model_uri=DEFAULT_.utstedtdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.utloepsdato = Slot(uri=NGRP.utloepsdato, name="utloepsdato", curie=NGRP.curie('utloepsdato'),
                   model_uri=DEFAULT_.utloepsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.identitetsgrunnlag_status = Slot(uri=NGRP.identitetsgrunnlagStatus, name="identitetsgrunnlag_status", curie=NGRP.curie('identitetsgrunnlagStatus'),
                   model_uri=DEFAULT_.identitetsgrunnlag_status, domain=None, range=Optional[str])

slots.identitetsgrunnlag_kilde = Slot(uri=NGRP.identitetsgrunnlagKilde, name="identitetsgrunnlag_kilde", curie=NGRP.curie('identitetsgrunnlagKilde'),
                   model_uri=DEFAULT_.identitetsgrunnlag_kilde, domain=None, range=Optional[str])

slots.kjoenn_kode = Slot(uri=NGRP.kjoennKode, name="kjoenn_kode", curie=NGRP.curie('kjoennKode'),
                   model_uri=DEFAULT_.kjoenn_kode, domain=None, range=Optional[Union[str, "KjoennKode"]])

slots.sivilstand_type = Slot(uri=NGRP.sivilstandType, name="sivilstand_type", curie=NGRP.curie('sivilstandType'),
                   model_uri=DEFAULT_.sivilstand_type, domain=None, range=Optional[Union[str, "SivilstandType"]])

slots.personstatus_type = Slot(uri=NGRP.personstatusType, name="personstatus_type", curie=NGRP.curie('personstatusType'),
                   model_uri=DEFAULT_.personstatus_type, domain=None, range=Optional[Union[str, "PersonstatusType"]])

slots.landkode = Slot(uri=NGRP.landkode, name="landkode", curie=NGRP.curie('landkode'),
                   model_uri=DEFAULT_.landkode, domain=None, range=Optional[str])

slots.oppholds_type = Slot(uri=NGRP.oppholdType, name="oppholds_type", curie=NGRP.curie('oppholdType'),
                   model_uri=DEFAULT_.oppholds_type, domain=None, range=Optional[Union[str, "OppholdstypeKode"]])

slots.foedselsdato = Slot(uri=NGRP.foedselsdato, name="foedselsdato", curie=NGRP.curie('foedselsdato'),
                   model_uri=DEFAULT_.foedselsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.foedselsaar = Slot(uri=NGRP.foedselsaar, name="foedselsaar", curie=NGRP.curie('foedselsaar'),
                   model_uri=DEFAULT_.foedselsaar, domain=None, range=Optional[int])

slots.foedested = Slot(uri=NGRP.foedested, name="foedested", curie=NGRP.curie('foedested'),
                   model_uri=DEFAULT_.foedested, domain=None, range=Optional[str])

slots.doedsdato = Slot(uri=NGRP.doedsdato, name="doedsdato", curie=NGRP.curie('doedsdato'),
                   model_uri=DEFAULT_.doedsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.doedssted = Slot(uri=NGRP.doedssted, name="doedssted", curie=NGRP.curie('doedssted'),
                   model_uri=DEFAULT_.doedssted, domain=None, range=Optional[str])

slots.navn = Slot(uri=NGRP.namn, name="navn", curie=NGRP.curie('namn'),
                   model_uri=DEFAULT_.navn, domain=None, range=Optional[str])

slots.telefonnummer = Slot(uri=NGRP.telefonnummer, name="telefonnummer", curie=NGRP.curie('telefonnummer'),
                   model_uri=DEFAULT_.telefonnummer, domain=None, range=Optional[str])

slots.epostadresse_verdi = Slot(uri=NGRP.epostadresse, name="epostadresse_verdi", curie=NGRP.curie('epostadresse'),
                   model_uri=DEFAULT_.epostadresse_verdi, domain=None, range=Optional[str])

slots.mobiltelefonnummer = Slot(uri=NGRP.mobiltelefonnummer, name="mobiltelefonnummer", curie=NGRP.curie('mobiltelefonnummer'),
                   model_uri=DEFAULT_.mobiltelefonnummer, domain=None, range=Optional[str])

slots.sist_oppdatert = Slot(uri=NGRP.sistOppdatert, name="sist_oppdatert", curie=NGRP.curie('sistOppdatert'),
                   model_uri=DEFAULT_.sist_oppdatert, domain=None, range=Optional[Union[str, XSDDate]])

slots.fraflyttingsland = Slot(uri=NGRP.fraflyttingsland, name="fraflyttingsland", curie=NGRP.curie('fraflyttingsland'),
                   model_uri=DEFAULT_.fraflyttingsland, domain=None, range=Optional[str])

slots.fraflyttingssted_i_utlandet = Slot(uri=NGRP.fraflyttingsstedIUtlandet, name="fraflyttingssted_i_utlandet", curie=NGRP.curie('fraflyttingsstedIUtlandet'),
                   model_uri=DEFAULT_.fraflyttingssted_i_utlandet, domain=None, range=Optional[str])

slots.innflyttingsdato = Slot(uri=NGRP.innflyttingsdato, name="innflyttingsdato", curie=NGRP.curie('innflyttingsdato'),
                   model_uri=DEFAULT_.innflyttingsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.tilflyttingsland = Slot(uri=NGRP.tilflyttingsland, name="tilflyttingsland", curie=NGRP.curie('tilflyttingsland'),
                   model_uri=DEFAULT_.tilflyttingsland, domain=None, range=Optional[str])

slots.tilflyttingssted_i_utlandet = Slot(uri=NGRP.tilflyttingsstedIUtlandet, name="tilflyttingssted_i_utlandet", curie=NGRP.curie('tilflyttingsstedIUtlandet'),
                   model_uri=DEFAULT_.tilflyttingssted_i_utlandet, domain=None, range=Optional[str])

slots.utflyttingsdato = Slot(uri=NGRP.utflyttingsdato, name="utflyttingsdato", curie=NGRP.curie('utflyttingsdato'),
                   model_uri=DEFAULT_.utflyttingsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.adressebeskyttelse_gradering = Slot(uri=NGRP.adressebeskyttelseGradering, name="adressebeskyttelse_gradering", curie=NGRP.curie('adressebeskyttelseGradering'),
                   model_uri=DEFAULT_.adressebeskyttelse_gradering, domain=None, range=Optional[Union[str, "AdressebeskyttelseGradering"]])

slots.vergetype = Slot(uri=NGRP.vergetype, name="vergetype", curie=NGRP.curie('vergetype'),
                   model_uri=DEFAULT_.vergetype, domain=None, range=Optional[Union[str, "VergetypeKode"]])

slots.embete = Slot(uri=NGRP.embete, name="embete", curie=NGRP.curie('embete'),
                   model_uri=DEFAULT_.embete, domain=None, range=Optional[str])

slots.ansvarsstatus = Slot(uri=NGRP.ansvarsstatus, name="ansvarsstatus", curie=NGRP.curie('ansvarsstatus'),
                   model_uri=DEFAULT_.ansvarsstatus, domain=None, range=Optional[str])

slots.foreldrerelasjon_type = Slot(uri=NGRP.foreldrerelasjonType, name="foreldrerelasjon_type", curie=NGRP.curie('foreldrerelasjonType'),
                   model_uri=DEFAULT_.foreldrerelasjon_type, domain=None, range=Optional[str])

slots.rettslig_handleevne_type = Slot(uri=NGRP.rettsligHandleevneType, name="rettslig_handleevne_type", curie=NGRP.curie('rettsligHandleevneType'),
                   model_uri=DEFAULT_.rettslig_handleevne_type, domain=None, range=Optional[Union[str, "RettsligHandleevneType"]])

slots.omfang = Slot(uri=NGRP.omfang, name="omfang", curie=NGRP.curie('omfang'),
                   model_uri=DEFAULT_.omfang, domain=None, range=Optional[str])

slots.er_reservert = Slot(uri=NGRP.erReservert, name="er_reservert", curie=NGRP.curie('erReservert'),
                   model_uri=DEFAULT_.er_reservert, domain=None, range=Optional[Union[bool, Bool]])

slots.er_falsk = Slot(uri=NGRP.erFalsk, name="er_falsk", curie=NGRP.curie('erFalsk'),
                   model_uri=DEFAULT_.er_falsk, domain=None, range=Optional[Union[bool, Bool]])

slots.rett_identitet_er_ukjent = Slot(uri=NGRP.rettIdentitetErUkjent, name="rett_identitet_er_ukjent", curie=NGRP.curie('rettIdentitetErUkjent'),
                   model_uri=DEFAULT_.rett_identitet_er_ukjent, domain=None, range=Optional[Union[bool, Bool]])

slots.spraakkode = Slot(uri=NGRP.spraakkode, name="spraakkode", curie=NGRP.curie('spraakkode'),
                   model_uri=DEFAULT_.spraakkode, domain=None, range=Optional[str])

slots.gyldig_fra_og_med = Slot(uri=NGRP.gyldigFraOgMed, name="gyldig_fra_og_med", curie=NGRP.curie('gyldigFraOgMed'),
                   model_uri=DEFAULT_.gyldig_fra_og_med, domain=None, range=Optional[Union[str, XSDDate]])

slots.gyldig_til_og_med = Slot(uri=NGRP.gyldigTilOgMed, name="gyldig_til_og_med", curie=NGRP.curie('gyldigTilOgMed'),
                   model_uri=DEFAULT_.gyldig_til_og_med, domain=None, range=Optional[Union[str, XSDDate]])

slots.personContainer__personar = Slot(uri=DEFAULT_.personar, name="personContainer__personar", curie=DEFAULT_.curie('personar'),
                   model_uri=DEFAULT_.personContainer__personar, domain=None, range=Optional[Union[dict[Union[str, PersonId], Union[dict, Person]], list[Union[dict, Person]]]])

slots.personContainer__personnavn = Slot(uri=DEFAULT_.personnavn, name="personContainer__personnavn", curie=DEFAULT_.curie('personnavn'),
                   model_uri=DEFAULT_.personContainer__personnavn, domain=None, range=Optional[Union[dict[Union[str, PersonnavnId], Union[dict, Personnavn]], list[Union[dict, Personnavn]]]])

slots.personContainer__foedselsnummer = Slot(uri=DEFAULT_.foedselsnummer, name="personContainer__foedselsnummer", curie=DEFAULT_.curie('foedselsnummer'),
                   model_uri=DEFAULT_.personContainer__foedselsnummer, domain=None, range=Optional[Union[dict[Union[str, FoedselsnummerId], Union[dict, Foedselsnummer]], list[Union[dict, Foedselsnummer]]]])

slots.personContainer__dnummer = Slot(uri=DEFAULT_.dnummer, name="personContainer__dnummer", curie=DEFAULT_.curie('dnummer'),
                   model_uri=DEFAULT_.personContainer__dnummer, domain=None, range=Optional[Union[dict[Union[str, DNummerId], Union[dict, DNummer]], list[Union[dict, DNummer]]]])

slots.personContainer__personidentifikasjonar = Slot(uri=DEFAULT_.personidentifikasjonar, name="personContainer__personidentifikasjonar", curie=DEFAULT_.curie('personidentifikasjonar'),
                   model_uri=DEFAULT_.personContainer__personidentifikasjonar, domain=None, range=Optional[Union[dict[Union[str, PersonidentifikasjonId], Union[dict, Personidentifikasjon]], list[Union[dict, Personidentifikasjon]]]])

slots.personContainer__falskIdentitetar = Slot(uri=DEFAULT_.falskIdentitetar, name="personContainer__falskIdentitetar", curie=DEFAULT_.curie('falskIdentitetar'),
                   model_uri=DEFAULT_.personContainer__falskIdentitetar, domain=None, range=Optional[Union[dict[Union[str, FalskIdentitetId], Union[dict, FalskIdentitet]], list[Union[dict, FalskIdentitet]]]])

slots.personContainer__identifikasjonsdokument = Slot(uri=DEFAULT_.identifikasjonsdokument, name="personContainer__identifikasjonsdokument", curie=DEFAULT_.curie('identifikasjonsdokument'),
                   model_uri=DEFAULT_.personContainer__identifikasjonsdokument, domain=None, range=Optional[Union[dict[Union[str, IdentifikasjonsdokumentId], Union[dict, Identifikasjonsdokument]], list[Union[dict, Identifikasjonsdokument]]]])

slots.personContainer__identitetsgrunnlag = Slot(uri=DEFAULT_.identitetsgrunnlag, name="personContainer__identitetsgrunnlag", curie=DEFAULT_.curie('identitetsgrunnlag'),
                   model_uri=DEFAULT_.personContainer__identitetsgrunnlag, domain=None, range=Optional[Union[dict[Union[str, IdentitetsgrunnlagId], Union[dict, Identitetsgrunnlag]], list[Union[dict, Identitetsgrunnlag]]]])

slots.personContainer__kjoenn = Slot(uri=DEFAULT_.kjoenn, name="personContainer__kjoenn", curie=DEFAULT_.curie('kjoenn'),
                   model_uri=DEFAULT_.personContainer__kjoenn, domain=None, range=Optional[Union[dict[Union[str, KjoennId], Union[dict, Kjoenn]], list[Union[dict, Kjoenn]]]])

slots.personContainer__sivilstand = Slot(uri=DEFAULT_.sivilstand, name="personContainer__sivilstand", curie=DEFAULT_.curie('sivilstand'),
                   model_uri=DEFAULT_.personContainer__sivilstand, domain=None, range=Optional[Union[dict[Union[str, SivilstandId], Union[dict, Sivilstand]], list[Union[dict, Sivilstand]]]])

slots.personContainer__personstatus = Slot(uri=DEFAULT_.personstatus, name="personContainer__personstatus", curie=DEFAULT_.curie('personstatus'),
                   model_uri=DEFAULT_.personContainer__personstatus, domain=None, range=Optional[Union[dict[Union[str, PersonstatusId], Union[dict, Personstatus]], list[Union[dict, Personstatus]]]])

slots.personContainer__statsborgerskap = Slot(uri=DEFAULT_.statsborgerskap, name="personContainer__statsborgerskap", curie=DEFAULT_.curie('statsborgerskap'),
                   model_uri=DEFAULT_.personContainer__statsborgerskap, domain=None, range=Optional[Union[dict[Union[str, StatsborgerskapId], Union[dict, Statsborgerskap]], list[Union[dict, Statsborgerskap]]]])

slots.personContainer__opphold = Slot(uri=DEFAULT_.opphold, name="personContainer__opphold", curie=DEFAULT_.curie('opphold'),
                   model_uri=DEFAULT_.personContainer__opphold, domain=None, range=Optional[Union[dict[Union[str, OppholdId], Union[dict, Opphold]], list[Union[dict, Opphold]]]])

slots.personContainer__foedslar = Slot(uri=DEFAULT_.foedslar, name="personContainer__foedslar", curie=DEFAULT_.curie('foedslar'),
                   model_uri=DEFAULT_.personContainer__foedslar, domain=None, range=Optional[Union[dict[Union[str, FoedselId], Union[dict, Foedsel]], list[Union[dict, Foedsel]]]])

slots.personContainer__foreldreansvarForelder = Slot(uri=DEFAULT_.foreldreansvarForelder, name="personContainer__foreldreansvarForelder", curie=DEFAULT_.curie('foreldreansvarForelder'),
                   model_uri=DEFAULT_.personContainer__foreldreansvarForelder, domain=None, range=Optional[Union[dict[Union[str, ForeldreansvarForelderId], Union[dict, ForeldreansvarForelder]], list[Union[dict, ForeldreansvarForelder]]]])

slots.personContainer__foreldreansvarBarn = Slot(uri=DEFAULT_.foreldreansvarBarn, name="personContainer__foreldreansvarBarn", curie=DEFAULT_.curie('foreldreansvarBarn'),
                   model_uri=DEFAULT_.personContainer__foreldreansvarBarn, domain=None, range=Optional[Union[dict[Union[str, ForeldreansvarBarnId], Union[dict, ForeldreansvarBarn]], list[Union[dict, ForeldreansvarBarn]]]])

slots.personContainer__familierelasjonForelder = Slot(uri=DEFAULT_.familierelasjonForelder, name="personContainer__familierelasjonForelder", curie=DEFAULT_.curie('familierelasjonForelder'),
                   model_uri=DEFAULT_.personContainer__familierelasjonForelder, domain=None, range=Optional[Union[dict[Union[str, FamilierelasjonForelderId], Union[dict, FamilierelasjonForelder]], list[Union[dict, FamilierelasjonForelder]]]])

slots.personContainer__familierelasjonBarn = Slot(uri=DEFAULT_.familierelasjonBarn, name="personContainer__familierelasjonBarn", curie=DEFAULT_.curie('familierelasjonBarn'),
                   model_uri=DEFAULT_.personContainer__familierelasjonBarn, domain=None, range=Optional[Union[dict[Union[str, FamilierelasjonBarnId], Union[dict, FamilierelasjonBarn]], list[Union[dict, FamilierelasjonBarn]]]])

slots.personContainer__familierelasjonEktefelle = Slot(uri=DEFAULT_.familierelasjonEktefelle, name="personContainer__familierelasjonEktefelle", curie=DEFAULT_.curie('familierelasjonEktefelle'),
                   model_uri=DEFAULT_.personContainer__familierelasjonEktefelle, domain=None, range=Optional[Union[dict[Union[str, FamilierelasjonEktefelleId], Union[dict, FamilierelasjonEktefelle]], list[Union[dict, FamilierelasjonEktefelle]]]])

slots.personContainer__dodsfall = Slot(uri=DEFAULT_.dodsfall, name="personContainer__dodsfall", curie=DEFAULT_.curie('dodsfall'),
                   model_uri=DEFAULT_.personContainer__dodsfall, domain=None, range=Optional[Union[dict[Union[str, DodsfallId], Union[dict, Dodsfall]], list[Union[dict, Dodsfall]]]])

slots.personContainer__kontaktinformasjonDoedsbo = Slot(uri=DEFAULT_.kontaktinformasjonDoedsbo, name="personContainer__kontaktinformasjonDoedsbo", curie=DEFAULT_.curie('kontaktinformasjonDoedsbo'),
                   model_uri=DEFAULT_.personContainer__kontaktinformasjonDoedsbo, domain=None, range=Optional[Union[dict[Union[str, KontaktinformasjonDoedsboId], Union[dict, KontaktinformasjonDoedsbo]], list[Union[dict, KontaktinformasjonDoedsbo]]]])

slots.personContainer__innflytting = Slot(uri=DEFAULT_.innflytting, name="personContainer__innflytting", curie=DEFAULT_.curie('innflytting'),
                   model_uri=DEFAULT_.personContainer__innflytting, domain=None, range=Optional[Union[dict[Union[str, InnflyttingTilNorgeId], Union[dict, InnflyttingTilNorge]], list[Union[dict, InnflyttingTilNorge]]]])

slots.personContainer__utflytting = Slot(uri=DEFAULT_.utflytting, name="personContainer__utflytting", curie=DEFAULT_.curie('utflytting'),
                   model_uri=DEFAULT_.personContainer__utflytting, domain=None, range=Optional[Union[dict[Union[str, UtflyttingFraNorgeId], Union[dict, UtflyttingFraNorge]], list[Union[dict, UtflyttingFraNorge]]]])

slots.personContainer__adressebeskyttelse = Slot(uri=DEFAULT_.adressebeskyttelse, name="personContainer__adressebeskyttelse", curie=DEFAULT_.curie('adressebeskyttelse'),
                   model_uri=DEFAULT_.personContainer__adressebeskyttelse, domain=None, range=Optional[Union[dict[Union[str, AdressebeskyttelseId], Union[dict, Adressebeskyttelse]], list[Union[dict, Adressebeskyttelse]]]])

slots.personContainer__bostedsadresser = Slot(uri=DEFAULT_.bostedsadresser, name="personContainer__bostedsadresser", curie=DEFAULT_.curie('bostedsadresser'),
                   model_uri=DEFAULT_.personContainer__bostedsadresser, domain=None, range=Optional[Union[dict[Union[str, BostedsadresseId], Union[dict, Bostedsadresse]], list[Union[dict, Bostedsadresse]]]])

slots.personContainer__postadresser = Slot(uri=DEFAULT_.postadresser, name="personContainer__postadresser", curie=DEFAULT_.curie('postadresser'),
                   model_uri=DEFAULT_.personContainer__postadresser, domain=None, range=Optional[Union[dict[Union[str, PostadresseId], Union[dict, Postadresse]], list[Union[dict, Postadresse]]]])

slots.personContainer__oppholdsadresser = Slot(uri=DEFAULT_.oppholdsadresser, name="personContainer__oppholdsadresser", curie=DEFAULT_.curie('oppholdsadresser'),
                   model_uri=DEFAULT_.personContainer__oppholdsadresser, domain=None, range=Optional[Union[dict[Union[str, OppholdsadresseId], Union[dict, Oppholdsadresse]], list[Union[dict, Oppholdsadresse]]]])

slots.personContainer__verger = Slot(uri=DEFAULT_.verger, name="personContainer__verger", curie=DEFAULT_.curie('verger'),
                   model_uri=DEFAULT_.personContainer__verger, domain=None, range=Optional[Union[dict[Union[str, VergeId], Union[dict, Verge]], list[Union[dict, Verge]]]])

slots.personContainer__rettsligHandleevne = Slot(uri=DEFAULT_.rettsligHandleevne, name="personContainer__rettsligHandleevne", curie=DEFAULT_.curie('rettsligHandleevne'),
                   model_uri=DEFAULT_.personContainer__rettsligHandleevne, domain=None, range=Optional[Union[dict[Union[str, RettsligHandleevneId], Union[dict, RettsligHandleevne]], list[Union[dict, RettsligHandleevne]]]])

slots.personContainer__reservasjonar = Slot(uri=DEFAULT_.reservasjonar, name="personContainer__reservasjonar", curie=DEFAULT_.curie('reservasjonar'),
                   model_uri=DEFAULT_.personContainer__reservasjonar, domain=None, range=Optional[Union[dict[Union[str, ReservasjonMotKommunikasjonPaaNettId], Union[dict, ReservasjonMotKommunikasjonPaaNett]], list[Union[dict, ReservasjonMotKommunikasjonPaaNett]]]])

slots.personContainer__kontaktopplysningar = Slot(uri=DEFAULT_.kontaktopplysningar, name="personContainer__kontaktopplysningar", curie=DEFAULT_.curie('kontaktopplysningar'),
                   model_uri=DEFAULT_.personContainer__kontaktopplysningar, domain=None, range=Optional[Union[dict[Union[str, KontaktopplysningerId], Union[dict, Kontaktopplysninger]], list[Union[dict, Kontaktopplysninger]]]])

slots.personContainer__spraak = Slot(uri=DEFAULT_.spraak, name="personContainer__spraak", curie=DEFAULT_.curie('spraak'),
                   model_uri=DEFAULT_.personContainer__spraak, domain=None, range=Optional[Union[dict[Union[str, SpraakForElektroniskKommunikasjonId], Union[dict, SpraakForElektroniskKommunikasjon]], list[Union[dict, SpraakForElektroniskKommunikasjon]]]])

slots.Person_har_personnavn = Slot(uri=NGRP.harPersonnavn, name="Person_har_personnavn", curie=NGRP.curie('harPersonnavn'),
                   model_uri=DEFAULT_.Person_har_personnavn, domain=Person, range=Union[str, PersonnavnId])

slots.Person_har_folkeregisteridentifikator = Slot(uri=NGRP.harFolkeregisteridentifikator, name="Person_har_folkeregisteridentifikator", curie=NGRP.curie('harFolkeregisteridentifikator'),
                   model_uri=DEFAULT_.Person_har_folkeregisteridentifikator, domain=Person, range=Union[str, FolkeregisteridentifikatorId])

slots.Person_har_kjoenn = Slot(uri=NGRP.harKjoenn, name="Person_har_kjoenn", curie=NGRP.curie('harKjoenn'),
                   model_uri=DEFAULT_.Person_har_kjoenn, domain=Person, range=Union[str, KjoennId])

slots.Person_har_sivilstand = Slot(uri=NGRP.harSivilstand, name="Person_har_sivilstand", curie=NGRP.curie('harSivilstand'),
                   model_uri=DEFAULT_.Person_har_sivilstand, domain=Person, range=Union[str, SivilstandId])

slots.Person_har_personstatus = Slot(uri=NGRP.harPersonstatus, name="Person_har_personstatus", curie=NGRP.curie('harPersonstatus'),
                   model_uri=DEFAULT_.Person_har_personstatus, domain=Person, range=Union[str, PersonstatusId])

slots.Person_har_statsborgerskap = Slot(uri=NGRP.harStatsborgerskap, name="Person_har_statsborgerskap", curie=NGRP.curie('harStatsborgerskap'),
                   model_uri=DEFAULT_.Person_har_statsborgerskap, domain=Person, range=Union[Union[str, StatsborgerskapId], list[Union[str, StatsborgerskapId]]])

slots.Person_har_foedsel = Slot(uri=NGRP.harFoedsel, name="Person_har_foedsel", curie=NGRP.curie('harFoedsel'),
                   model_uri=DEFAULT_.Person_har_foedsel, domain=Person, range=Union[str, FoedselId])

slots.Person_har_valgt_spraak = Slot(uri=NGRP.harValgtSpraak, name="Person_har_valgt_spraak", curie=NGRP.curie('harValgtSpraak'),
                   model_uri=DEFAULT_.Person_har_valgt_spraak, domain=Person, range=Union[str, SpraakForElektroniskKommunikasjonId])

slots.Person_har_personidentifikasjon = Slot(uri=NGRP.harPersonidentifikasjon, name="Person_har_personidentifikasjon", curie=NGRP.curie('harPersonidentifikasjon'),
                   model_uri=DEFAULT_.Person_har_personidentifikasjon, domain=Person, range=Optional[Union[Union[str, PersonidentifikasjonId], list[Union[str, PersonidentifikasjonId]]]])

slots.Person_har_utenlandsk_identifikasjonsdokument = Slot(uri=NGRP.harUtenlandskIdentifikasjonsdokument, name="Person_har_utenlandsk_identifikasjonsdokument", curie=NGRP.curie('harUtenlandskIdentifikasjonsdokument'),
                   model_uri=DEFAULT_.Person_har_utenlandsk_identifikasjonsdokument, domain=Person, range=Optional[Union[Union[str, IdentifikasjonsdokumentId], list[Union[str, IdentifikasjonsdokumentId]]]])

slots.Person_har_falsk_identitet = Slot(uri=NGRP.harFalskIdentitet, name="Person_har_falsk_identitet", curie=NGRP.curie('harFalskIdentitet'),
                   model_uri=DEFAULT_.Person_har_falsk_identitet, domain=Person, range=Optional[Union[str, FalskIdentitetId]])

slots.Person_har_identitetsgrunnlag = Slot(uri=NGRP.harIdentitetsgrunnlag, name="Person_har_identitetsgrunnlag", curie=NGRP.curie('harIdentitetsgrunnlag'),
                   model_uri=DEFAULT_.Person_har_identitetsgrunnlag, domain=Person, range=Optional[Union[str, IdentitetsgrunnlagId]])

slots.Person_har_lovlig_opphold = Slot(uri=NGRP.harLovligOpphold, name="Person_har_lovlig_opphold", curie=NGRP.curie('harLovligOpphold'),
                   model_uri=DEFAULT_.Person_har_lovlig_opphold, domain=Person, range=Optional[Union[str, OppholdId]])

slots.Person_har_foreldreansvar_forelder = Slot(uri=NGRP.harForeldreansvarForelder, name="Person_har_foreldreansvar_forelder", curie=NGRP.curie('harForeldreansvarForelder'),
                   model_uri=DEFAULT_.Person_har_foreldreansvar_forelder, domain=Person, range=Optional[Union[Union[str, ForeldreansvarForelderId], list[Union[str, ForeldreansvarForelderId]]]])

slots.Person_har_foreldreansvar_barn = Slot(uri=NGRP.harForeldreansvarBarn, name="Person_har_foreldreansvar_barn", curie=NGRP.curie('harForeldreansvarBarn'),
                   model_uri=DEFAULT_.Person_har_foreldreansvar_barn, domain=Person, range=Optional[Union[Union[str, ForeldreansvarBarnId], list[Union[str, ForeldreansvarBarnId]]]])

slots.Person_har_familierelasjon_forelder = Slot(uri=NGRP.harFamilierelasjonForelder, name="Person_har_familierelasjon_forelder", curie=NGRP.curie('harFamilierelasjonForelder'),
                   model_uri=DEFAULT_.Person_har_familierelasjon_forelder, domain=Person, range=Optional[Union[Union[str, FamilierelasjonForelderId], list[Union[str, FamilierelasjonForelderId]]]])

slots.Person_har_familierelasjon_barn = Slot(uri=NGRP.harFamilierelasjonBarn, name="Person_har_familierelasjon_barn", curie=NGRP.curie('harFamilierelasjonBarn'),
                   model_uri=DEFAULT_.Person_har_familierelasjon_barn, domain=Person, range=Optional[Union[Union[str, FamilierelasjonBarnId], list[Union[str, FamilierelasjonBarnId]]]])

slots.Person_har_familierelasjon_ektefelle = Slot(uri=NGRP.harFamilierelasjonEktefelle, name="Person_har_familierelasjon_ektefelle", curie=NGRP.curie('harFamilierelasjonEktefelle'),
                   model_uri=DEFAULT_.Person_har_familierelasjon_ektefelle, domain=Person, range=Optional[Union[str, FamilierelasjonEktefelleId]])

slots.Person_har_dodsfall = Slot(uri=NGRP.harDodsfall, name="Person_har_dodsfall", curie=NGRP.curie('harDodsfall'),
                   model_uri=DEFAULT_.Person_har_dodsfall, domain=Person, range=Optional[Union[str, DodsfallId]])

slots.Person_har_kontaktinformasjon_doedsbo = Slot(uri=NGRP.harKontaktinformasjonDoedsbo, name="Person_har_kontaktinformasjon_doedsbo", curie=NGRP.curie('harKontaktinformasjonDoedsbo'),
                   model_uri=DEFAULT_.Person_har_kontaktinformasjon_doedsbo, domain=Person, range=Optional[Union[str, KontaktinformasjonDoedsboId]])

slots.Person_har_innflytting_til_norge = Slot(uri=NGRP.harInnflyttingTilNorge, name="Person_har_innflytting_til_norge", curie=NGRP.curie('harInnflyttingTilNorge'),
                   model_uri=DEFAULT_.Person_har_innflytting_til_norge, domain=Person, range=Optional[Union[str, InnflyttingTilNorgeId]])

slots.Person_har_utflytting_fra_norge = Slot(uri=NGRP.harUtflyttingFraNorge, name="Person_har_utflytting_fra_norge", curie=NGRP.curie('harUtflyttingFraNorge'),
                   model_uri=DEFAULT_.Person_har_utflytting_fra_norge, domain=Person, range=Optional[Union[str, UtflyttingFraNorgeId]])

slots.Person_har_adressebeskyttelse = Slot(uri=NGRP.harAdressebeskyttelse, name="Person_har_adressebeskyttelse", curie=NGRP.curie('harAdressebeskyttelse'),
                   model_uri=DEFAULT_.Person_har_adressebeskyttelse, domain=Person, range=Optional[Union[str, AdressebeskyttelseId]])

slots.Person_har_bosted_paa = Slot(uri=NGRP.harBostedPaa, name="Person_har_bosted_paa", curie=NGRP.curie('harBostedPaa'),
                   model_uri=DEFAULT_.Person_har_bosted_paa, domain=Person, range=Optional[Union[str, BostedsadresseId]])

slots.Person_mottar_post_paa = Slot(uri=NGRP.mottarPostPaa, name="Person_mottar_post_paa", curie=NGRP.curie('mottarPostPaa'),
                   model_uri=DEFAULT_.Person_mottar_post_paa, domain=Person, range=Optional[Union[str, PostadresseId]])

slots.Person_oppholder_seg_paa = Slot(uri=NGRP.oppholderSegPaa, name="Person_oppholder_seg_paa", curie=NGRP.curie('oppholderSegPaa'),
                   model_uri=DEFAULT_.Person_oppholder_seg_paa, domain=Person, range=Optional[Union[str, OppholdsadresseId]])

slots.Person_har_verge = Slot(uri=NGRP.harVerge, name="Person_har_verge", curie=NGRP.curie('harVerge'),
                   model_uri=DEFAULT_.Person_har_verge, domain=Person, range=Optional[Union[Union[str, VergeId], list[Union[str, VergeId]]]])

slots.Person_har_rettslig_handleevne = Slot(uri=NGRP.harRettsligHandleevne, name="Person_har_rettslig_handleevne", curie=NGRP.curie('harRettsligHandleevne'),
                   model_uri=DEFAULT_.Person_har_rettslig_handleevne, domain=Person, range=Optional[Union[str, RettsligHandleevneId]])

slots.Person_har_reservasjon_mot_kommunikasjon = Slot(uri=NGRP.harReservasjonMotKommunikasjon, name="Person_har_reservasjon_mot_kommunikasjon", curie=NGRP.curie('harReservasjonMotKommunikasjon'),
                   model_uri=DEFAULT_.Person_har_reservasjon_mot_kommunikasjon, domain=Person, range=Optional[Union[str, ReservasjonMotKommunikasjonPaaNettId]])

slots.Person_har_kontaktopplysninger = Slot(uri=NGRP.harKontaktopplysninger, name="Person_har_kontaktopplysninger", curie=NGRP.curie('harKontaktopplysninger'),
                   model_uri=DEFAULT_.Person_har_kontaktopplysninger, domain=Person, range=Optional[Union[str, KontaktopplysningerId]])

slots.Personnavn_fornavn = Slot(uri=NGRP.fornavn, name="Personnavn_fornavn", curie=NGRP.curie('fornavn'),
                   model_uri=DEFAULT_.Personnavn_fornavn, domain=Personnavn, range=str)

slots.Personnavn_etternavn = Slot(uri=NGRP.etternavn, name="Personnavn_etternavn", curie=NGRP.curie('etternavn'),
                   model_uri=DEFAULT_.Personnavn_etternavn, domain=Personnavn, range=str)

slots.Personnavn_mellomnavn = Slot(uri=NGRP.mellomnavn, name="Personnavn_mellomnavn", curie=NGRP.curie('mellomnavn'),
                   model_uri=DEFAULT_.Personnavn_mellomnavn, domain=Personnavn, range=Optional[str])

slots.Personnavn_forkortet_navn = Slot(uri=NGRP.forkortetNavn, name="Personnavn_forkortet_navn", curie=NGRP.curie('forkortetNavn'),
                   model_uri=DEFAULT_.Personnavn_forkortet_navn, domain=Personnavn, range=Optional[str])

slots.Foedselsnummer_identifikatornummer = Slot(uri=NGRP.identifikatornummer, name="Foedselsnummer_identifikatornummer", curie=NGRP.curie('identifikatornummer'),
                   model_uri=DEFAULT_.Foedselsnummer_identifikatornummer, domain=Foedselsnummer, range=str)

slots.DNummer_identifikatornummer = Slot(uri=NGRP.identifikatornummer, name="DNummer_identifikatornummer", curie=NGRP.curie('identifikatornummer'),
                   model_uri=DEFAULT_.DNummer_identifikatornummer, domain=DNummer, range=str)

slots.Personidentifikasjon_identifikasjonstype = Slot(uri=NGRP.identifikasjonstype, name="Personidentifikasjon_identifikasjonstype", curie=NGRP.curie('identifikasjonstype'),
                   model_uri=DEFAULT_.Personidentifikasjon_identifikasjonstype, domain=Personidentifikasjon, range=str)

slots.Personidentifikasjon_identifikatornummer = Slot(uri=NGRP.identifikatornummer, name="Personidentifikasjon_identifikatornummer", curie=NGRP.curie('identifikatornummer'),
                   model_uri=DEFAULT_.Personidentifikasjon_identifikatornummer, domain=Personidentifikasjon, range=str)

slots.FalskIdentitet_er_falsk = Slot(uri=NGRP.erFalsk, name="FalskIdentitet_er_falsk", curie=NGRP.curie('erFalsk'),
                   model_uri=DEFAULT_.FalskIdentitet_er_falsk, domain=FalskIdentitet, range=Union[bool, Bool])

slots.FalskIdentitet_rett_identitet_er_ukjent = Slot(uri=NGRP.rettIdentitetErUkjent, name="FalskIdentitet_rett_identitet_er_ukjent", curie=NGRP.curie('rettIdentitetErUkjent'),
                   model_uri=DEFAULT_.FalskIdentitet_rett_identitet_er_ukjent, domain=FalskIdentitet, range=Optional[Union[bool, Bool]])

slots.FalskIdentitet_rett_identitet = Slot(uri=NGRP.rettIdentitet, name="FalskIdentitet_rett_identitet", curie=NGRP.curie('rettIdentitet'),
                   model_uri=DEFAULT_.FalskIdentitet_rett_identitet, domain=FalskIdentitet, range=Optional[Union[str, PersonId]])

slots.Identifikasjonsdokument_dokumenttype = Slot(uri=NGRP.dokumenttype, name="Identifikasjonsdokument_dokumenttype", curie=NGRP.curie('dokumenttype'),
                   model_uri=DEFAULT_.Identifikasjonsdokument_dokumenttype, domain=Identifikasjonsdokument, range=Union[str, "IdentifikasjonsdokumentType"])

slots.Identifikasjonsdokument_dokumentnummer = Slot(uri=NGRP.dokumentnummer, name="Identifikasjonsdokument_dokumentnummer", curie=NGRP.curie('dokumentnummer'),
                   model_uri=DEFAULT_.Identifikasjonsdokument_dokumentnummer, domain=Identifikasjonsdokument, range=str)

slots.Identifikasjonsdokument_utstederland = Slot(uri=NGRP.utstederland, name="Identifikasjonsdokument_utstederland", curie=NGRP.curie('utstederland'),
                   model_uri=DEFAULT_.Identifikasjonsdokument_utstederland, domain=Identifikasjonsdokument, range=Optional[str])

slots.Identifikasjonsdokument_utstedtdato = Slot(uri=NGRP.utstedtdato, name="Identifikasjonsdokument_utstedtdato", curie=NGRP.curie('utstedtdato'),
                   model_uri=DEFAULT_.Identifikasjonsdokument_utstedtdato, domain=Identifikasjonsdokument, range=Optional[Union[str, XSDDate]])

slots.Identifikasjonsdokument_utloepsdato = Slot(uri=NGRP.utloepsdato, name="Identifikasjonsdokument_utloepsdato", curie=NGRP.curie('utloepsdato'),
                   model_uri=DEFAULT_.Identifikasjonsdokument_utloepsdato, domain=Identifikasjonsdokument, range=Optional[Union[str, XSDDate]])

slots.Identitetsgrunnlag_identitetsgrunnlag_status = Slot(uri=NGRP.identitetsgrunnlagStatus, name="Identitetsgrunnlag_identitetsgrunnlag_status", curie=NGRP.curie('identitetsgrunnlagStatus'),
                   model_uri=DEFAULT_.Identitetsgrunnlag_identitetsgrunnlag_status, domain=Identitetsgrunnlag, range=str)

slots.Identitetsgrunnlag_identitetsgrunnlag_kilde = Slot(uri=NGRP.identitetsgrunnlagKilde, name="Identitetsgrunnlag_identitetsgrunnlag_kilde", curie=NGRP.curie('identitetsgrunnlagKilde'),
                   model_uri=DEFAULT_.Identitetsgrunnlag_identitetsgrunnlag_kilde, domain=Identitetsgrunnlag, range=Optional[str])

slots.Kjoenn_kjoenn_kode = Slot(uri=NGRP.kjoennKode, name="Kjoenn_kjoenn_kode", curie=NGRP.curie('kjoennKode'),
                   model_uri=DEFAULT_.Kjoenn_kjoenn_kode, domain=Kjoenn, range=Union[str, "KjoennKode"])

slots.Kjoenn_gyldig_fra_og_med = Slot(uri=NGRP.gyldigFraOgMed, name="Kjoenn_gyldig_fra_og_med", curie=NGRP.curie('gyldigFraOgMed'),
                   model_uri=DEFAULT_.Kjoenn_gyldig_fra_og_med, domain=Kjoenn, range=Optional[Union[str, XSDDate]])

slots.Sivilstand_sivilstand_type = Slot(uri=NGRP.sivilstandType, name="Sivilstand_sivilstand_type", curie=NGRP.curie('sivilstandType'),
                   model_uri=DEFAULT_.Sivilstand_sivilstand_type, domain=Sivilstand, range=Union[str, "SivilstandType"])

slots.Sivilstand_gyldig_fra_og_med = Slot(uri=NGRP.gyldigFraOgMed, name="Sivilstand_gyldig_fra_og_med", curie=NGRP.curie('gyldigFraOgMed'),
                   model_uri=DEFAULT_.Sivilstand_gyldig_fra_og_med, domain=Sivilstand, range=Optional[Union[str, XSDDate]])

slots.Sivilstand_relatert_ved_sivilstand = Slot(uri=NGRP.relatertVedSivilstand, name="Sivilstand_relatert_ved_sivilstand", curie=NGRP.curie('relatertVedSivilstand'),
                   model_uri=DEFAULT_.Sivilstand_relatert_ved_sivilstand, domain=Sivilstand, range=Optional[Union[str, PersonId]])

slots.Personstatus_personstatus_type = Slot(uri=NGRP.personstatusType, name="Personstatus_personstatus_type", curie=NGRP.curie('personstatusType'),
                   model_uri=DEFAULT_.Personstatus_personstatus_type, domain=Personstatus, range=Union[str, "PersonstatusType"])

slots.Personstatus_gyldig_fra_og_med = Slot(uri=NGRP.gyldigFraOgMed, name="Personstatus_gyldig_fra_og_med", curie=NGRP.curie('gyldigFraOgMed'),
                   model_uri=DEFAULT_.Personstatus_gyldig_fra_og_med, domain=Personstatus, range=Optional[Union[str, XSDDate]])

slots.Statsborgerskap_landkode = Slot(uri=NGRP.landkode, name="Statsborgerskap_landkode", curie=NGRP.curie('landkode'),
                   model_uri=DEFAULT_.Statsborgerskap_landkode, domain=Statsborgerskap, range=str)

slots.Statsborgerskap_gyldig_fra_og_med = Slot(uri=NGRP.gyldigFraOgMed, name="Statsborgerskap_gyldig_fra_og_med", curie=NGRP.curie('gyldigFraOgMed'),
                   model_uri=DEFAULT_.Statsborgerskap_gyldig_fra_og_med, domain=Statsborgerskap, range=Optional[Union[str, XSDDate]])

slots.Statsborgerskap_gyldig_til_og_med = Slot(uri=NGRP.gyldigTilOgMed, name="Statsborgerskap_gyldig_til_og_med", curie=NGRP.curie('gyldigTilOgMed'),
                   model_uri=DEFAULT_.Statsborgerskap_gyldig_til_og_med, domain=Statsborgerskap, range=Optional[Union[str, XSDDate]])

slots.Opphold_oppholds_type = Slot(uri=NGRP.oppholdType, name="Opphold_oppholds_type", curie=NGRP.curie('oppholdType'),
                   model_uri=DEFAULT_.Opphold_oppholds_type, domain=Opphold, range=Union[str, "OppholdstypeKode"])

slots.Opphold_gyldig_fra_og_med = Slot(uri=NGRP.gyldigFraOgMed, name="Opphold_gyldig_fra_og_med", curie=NGRP.curie('gyldigFraOgMed'),
                   model_uri=DEFAULT_.Opphold_gyldig_fra_og_med, domain=Opphold, range=Union[str, XSDDate])

slots.Opphold_gyldig_til_og_med = Slot(uri=NGRP.gyldigTilOgMed, name="Opphold_gyldig_til_og_med", curie=NGRP.curie('gyldigTilOgMed'),
                   model_uri=DEFAULT_.Opphold_gyldig_til_og_med, domain=Opphold, range=Optional[Union[str, XSDDate]])

slots.Foedsel_foedselsdato = Slot(uri=NGRP.foedselsdato, name="Foedsel_foedselsdato", curie=NGRP.curie('foedselsdato'),
                   model_uri=DEFAULT_.Foedsel_foedselsdato, domain=Foedsel, range=Optional[Union[str, XSDDate]])

slots.Foedsel_foedselsaar = Slot(uri=NGRP.foedselsaar, name="Foedsel_foedselsaar", curie=NGRP.curie('foedselsaar'),
                   model_uri=DEFAULT_.Foedsel_foedselsaar, domain=Foedsel, range=int)

slots.Foedsel_foedested = Slot(uri=NGRP.foedested, name="Foedsel_foedested", curie=NGRP.curie('foedested'),
                   model_uri=DEFAULT_.Foedsel_foedested, domain=Foedsel, range=Optional[str])

slots.Dodsfall_doedsdato = Slot(uri=NGRP.doedsdato, name="Dodsfall_doedsdato", curie=NGRP.curie('doedsdato'),
                   model_uri=DEFAULT_.Dodsfall_doedsdato, domain=Dodsfall, range=Union[str, XSDDate])

slots.Dodsfall_doedssted = Slot(uri=NGRP.doedssted, name="Dodsfall_doedssted", curie=NGRP.curie('doedssted'),
                   model_uri=DEFAULT_.Dodsfall_doedssted, domain=Dodsfall, range=Optional[str])

slots.KontaktinformasjonDoedsbo_navn = Slot(uri=NGRP.namn, name="KontaktinformasjonDoedsbo_navn", curie=NGRP.curie('namn'),
                   model_uri=DEFAULT_.KontaktinformasjonDoedsbo_navn, domain=KontaktinformasjonDoedsbo, range=str)

slots.KontaktinformasjonDoedsbo_telefonnummer = Slot(uri=NGRP.telefonnummer, name="KontaktinformasjonDoedsbo_telefonnummer", curie=NGRP.curie('telefonnummer'),
                   model_uri=DEFAULT_.KontaktinformasjonDoedsbo_telefonnummer, domain=KontaktinformasjonDoedsbo, range=Optional[str])

slots.KontaktinformasjonDoedsbo_epostadresse_verdi = Slot(uri=NGRP.epostadresse, name="KontaktinformasjonDoedsbo_epostadresse_verdi", curie=NGRP.curie('epostadresse'),
                   model_uri=DEFAULT_.KontaktinformasjonDoedsbo_epostadresse_verdi, domain=KontaktinformasjonDoedsbo, range=Optional[str])

slots.ForeldreansvarForelder_er_av_type_person = Slot(uri=NGRP.erAvTypePerson, name="ForeldreansvarForelder_er_av_type_person", curie=NGRP.curie('erAvTypePerson'),
                   model_uri=DEFAULT_.ForeldreansvarForelder_er_av_type_person, domain=ForeldreansvarForelder, range=Union[str, PersonId])

slots.ForeldreansvarForelder_ansvarsstatus = Slot(uri=NGRP.ansvarsstatus, name="ForeldreansvarForelder_ansvarsstatus", curie=NGRP.curie('ansvarsstatus'),
                   model_uri=DEFAULT_.ForeldreansvarForelder_ansvarsstatus, domain=ForeldreansvarForelder, range=Optional[str])

slots.ForeldreansvarBarn_er_av_type_person = Slot(uri=NGRP.erAvTypePerson, name="ForeldreansvarBarn_er_av_type_person", curie=NGRP.curie('erAvTypePerson'),
                   model_uri=DEFAULT_.ForeldreansvarBarn_er_av_type_person, domain=ForeldreansvarBarn, range=Union[str, PersonId])

slots.FamilierelasjonForelder_er_av_type_person = Slot(uri=NGRP.erAvTypePerson, name="FamilierelasjonForelder_er_av_type_person", curie=NGRP.curie('erAvTypePerson'),
                   model_uri=DEFAULT_.FamilierelasjonForelder_er_av_type_person, domain=FamilierelasjonForelder, range=Union[str, PersonId])

slots.FamilierelasjonForelder_foreldrerelasjon_type = Slot(uri=NGRP.foreldrerelasjonType, name="FamilierelasjonForelder_foreldrerelasjon_type", curie=NGRP.curie('foreldrerelasjonType'),
                   model_uri=DEFAULT_.FamilierelasjonForelder_foreldrerelasjon_type, domain=FamilierelasjonForelder, range=Optional[str])

slots.FamilierelasjonBarn_er_av_type_person = Slot(uri=NGRP.erAvTypePerson, name="FamilierelasjonBarn_er_av_type_person", curie=NGRP.curie('erAvTypePerson'),
                   model_uri=DEFAULT_.FamilierelasjonBarn_er_av_type_person, domain=FamilierelasjonBarn, range=Union[str, PersonId])

slots.FamilierelasjonEktefelle_er_av_type_person = Slot(uri=NGRP.erAvTypePerson, name="FamilierelasjonEktefelle_er_av_type_person", curie=NGRP.curie('erAvTypePerson'),
                   model_uri=DEFAULT_.FamilierelasjonEktefelle_er_av_type_person, domain=FamilierelasjonEktefelle, range=Union[str, PersonId])

slots.InnflyttingTilNorge_innflyttingsdato = Slot(uri=NGRP.innflyttingsdato, name="InnflyttingTilNorge_innflyttingsdato", curie=NGRP.curie('innflyttingsdato'),
                   model_uri=DEFAULT_.InnflyttingTilNorge_innflyttingsdato, domain=InnflyttingTilNorge, range=Union[str, XSDDate])

slots.InnflyttingTilNorge_fraflyttingsland = Slot(uri=NGRP.fraflyttingsland, name="InnflyttingTilNorge_fraflyttingsland", curie=NGRP.curie('fraflyttingsland'),
                   model_uri=DEFAULT_.InnflyttingTilNorge_fraflyttingsland, domain=InnflyttingTilNorge, range=Optional[str])

slots.InnflyttingTilNorge_fraflyttingssted_i_utlandet = Slot(uri=NGRP.fraflyttingsstedIUtlandet, name="InnflyttingTilNorge_fraflyttingssted_i_utlandet", curie=NGRP.curie('fraflyttingsstedIUtlandet'),
                   model_uri=DEFAULT_.InnflyttingTilNorge_fraflyttingssted_i_utlandet, domain=InnflyttingTilNorge, range=Optional[str])

slots.UtflyttingFraNorge_utflyttingsdato = Slot(uri=NGRP.utflyttingsdato, name="UtflyttingFraNorge_utflyttingsdato", curie=NGRP.curie('utflyttingsdato'),
                   model_uri=DEFAULT_.UtflyttingFraNorge_utflyttingsdato, domain=UtflyttingFraNorge, range=Union[str, XSDDate])

slots.UtflyttingFraNorge_tilflyttingsland = Slot(uri=NGRP.tilflyttingsland, name="UtflyttingFraNorge_tilflyttingsland", curie=NGRP.curie('tilflyttingsland'),
                   model_uri=DEFAULT_.UtflyttingFraNorge_tilflyttingsland, domain=UtflyttingFraNorge, range=Optional[str])

slots.UtflyttingFraNorge_tilflyttingssted_i_utlandet = Slot(uri=NGRP.tilflyttingsstedIUtlandet, name="UtflyttingFraNorge_tilflyttingssted_i_utlandet", curie=NGRP.curie('tilflyttingsstedIUtlandet'),
                   model_uri=DEFAULT_.UtflyttingFraNorge_tilflyttingssted_i_utlandet, domain=UtflyttingFraNorge, range=Optional[str])

slots.Bostedsadresse_gyldig_fra_og_med = Slot(uri=NGRP.gyldigFraOgMed, name="Bostedsadresse_gyldig_fra_og_med", curie=NGRP.curie('gyldigFraOgMed'),
                   model_uri=DEFAULT_.Bostedsadresse_gyldig_fra_og_med, domain=Bostedsadresse, range=Optional[Union[str, XSDDate]])

slots.Bostedsadresse_gyldig_til_og_med = Slot(uri=NGRP.gyldigTilOgMed, name="Bostedsadresse_gyldig_til_og_med", curie=NGRP.curie('gyldigTilOgMed'),
                   model_uri=DEFAULT_.Bostedsadresse_gyldig_til_og_med, domain=Bostedsadresse, range=Optional[Union[str, XSDDate]])

slots.Postadresse_gyldig_fra_og_med = Slot(uri=NGRP.gyldigFraOgMed, name="Postadresse_gyldig_fra_og_med", curie=NGRP.curie('gyldigFraOgMed'),
                   model_uri=DEFAULT_.Postadresse_gyldig_fra_og_med, domain=Postadresse, range=Optional[Union[str, XSDDate]])

slots.Postadresse_gyldig_til_og_med = Slot(uri=NGRP.gyldigTilOgMed, name="Postadresse_gyldig_til_og_med", curie=NGRP.curie('gyldigTilOgMed'),
                   model_uri=DEFAULT_.Postadresse_gyldig_til_og_med, domain=Postadresse, range=Optional[Union[str, XSDDate]])

slots.Oppholdsadresse_gyldig_fra_og_med = Slot(uri=NGRP.gyldigFraOgMed, name="Oppholdsadresse_gyldig_fra_og_med", curie=NGRP.curie('gyldigFraOgMed'),
                   model_uri=DEFAULT_.Oppholdsadresse_gyldig_fra_og_med, domain=Oppholdsadresse, range=Optional[Union[str, XSDDate]])

slots.Oppholdsadresse_gyldig_til_og_med = Slot(uri=NGRP.gyldigTilOgMed, name="Oppholdsadresse_gyldig_til_og_med", curie=NGRP.curie('gyldigTilOgMed'),
                   model_uri=DEFAULT_.Oppholdsadresse_gyldig_til_og_med, domain=Oppholdsadresse, range=Optional[Union[str, XSDDate]])

slots.Adressebeskyttelse_adressebeskyttelse_gradering = Slot(uri=NGRP.adressebeskyttelseGradering, name="Adressebeskyttelse_adressebeskyttelse_gradering", curie=NGRP.curie('adressebeskyttelseGradering'),
                   model_uri=DEFAULT_.Adressebeskyttelse_adressebeskyttelse_gradering, domain=Adressebeskyttelse, range=Union[str, "AdressebeskyttelseGradering"])

slots.Verge_er_av_type_person = Slot(uri=NGRP.erAvTypePerson, name="Verge_er_av_type_person", curie=NGRP.curie('erAvTypePerson'),
                   model_uri=DEFAULT_.Verge_er_av_type_person, domain=Verge, range=Union[str, PersonId])

slots.Verge_vergetype = Slot(uri=NGRP.vergetype, name="Verge_vergetype", curie=NGRP.curie('vergetype'),
                   model_uri=DEFAULT_.Verge_vergetype, domain=Verge, range=Optional[Union[str, "VergetypeKode"]])

slots.Verge_embete = Slot(uri=NGRP.embete, name="Verge_embete", curie=NGRP.curie('embete'),
                   model_uri=DEFAULT_.Verge_embete, domain=Verge, range=Optional[str])

slots.RettsligHandleevne_rettslig_handleevne_type = Slot(uri=NGRP.rettsligHandleevneType, name="RettsligHandleevne_rettslig_handleevne_type", curie=NGRP.curie('rettsligHandleevneType'),
                   model_uri=DEFAULT_.RettsligHandleevne_rettslig_handleevne_type, domain=RettsligHandleevne, range=Union[str, "RettsligHandleevneType"])

slots.RettsligHandleevne_omfang = Slot(uri=NGRP.omfang, name="RettsligHandleevne_omfang", curie=NGRP.curie('omfang'),
                   model_uri=DEFAULT_.RettsligHandleevne_omfang, domain=RettsligHandleevne, range=Optional[str])

slots.ReservasjonMotKommunikasjonPaaNett_er_reservert = Slot(uri=NGRP.erReservert, name="ReservasjonMotKommunikasjonPaaNett_er_reservert", curie=NGRP.curie('erReservert'),
                   model_uri=DEFAULT_.ReservasjonMotKommunikasjonPaaNett_er_reservert, domain=ReservasjonMotKommunikasjonPaaNett, range=Union[bool, Bool])

slots.ReservasjonMotKommunikasjonPaaNett_gyldig_fra_og_med = Slot(uri=NGRP.gyldigFraOgMed, name="ReservasjonMotKommunikasjonPaaNett_gyldig_fra_og_med", curie=NGRP.curie('gyldigFraOgMed'),
                   model_uri=DEFAULT_.ReservasjonMotKommunikasjonPaaNett_gyldig_fra_og_med, domain=ReservasjonMotKommunikasjonPaaNett, range=Optional[Union[str, XSDDate]])

slots.Kontaktopplysninger_epostadresse_verdi = Slot(uri=NGRP.epostadresse, name="Kontaktopplysninger_epostadresse_verdi", curie=NGRP.curie('epostadresse'),
                   model_uri=DEFAULT_.Kontaktopplysninger_epostadresse_verdi, domain=Kontaktopplysninger, range=Optional[str])

slots.Kontaktopplysninger_mobiltelefonnummer = Slot(uri=NGRP.mobiltelefonnummer, name="Kontaktopplysninger_mobiltelefonnummer", curie=NGRP.curie('mobiltelefonnummer'),
                   model_uri=DEFAULT_.Kontaktopplysninger_mobiltelefonnummer, domain=Kontaktopplysninger, range=Optional[str])

slots.Kontaktopplysninger_sist_oppdatert = Slot(uri=NGRP.sistOppdatert, name="Kontaktopplysninger_sist_oppdatert", curie=NGRP.curie('sistOppdatert'),
                   model_uri=DEFAULT_.Kontaktopplysninger_sist_oppdatert, domain=Kontaktopplysninger, range=Optional[Union[str, XSDDate]])

slots.SpraakForElektroniskKommunikasjon_spraakkode = Slot(uri=NGRP.spraakkode, name="SpraakForElektroniskKommunikasjon_spraakkode", curie=NGRP.curie('spraakkode'),
                   model_uri=DEFAULT_.SpraakForElektroniskKommunikasjon_spraakkode, domain=SpraakForElektroniskKommunikasjon, range=str)

