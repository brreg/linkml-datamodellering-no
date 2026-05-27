# Auto generated from ngr-adresse-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-27T14:51:28
# Schema: ngr-adresse
#
# id: https://data.norge.no/ngr/ngr-adresse
# description: Domenemodell for norske adressar basert på Nasjonale grunndata (utkast). Modellerer Offisiell adresse og Postboksadresse med tilhøyrande geografiske inndelingar og adressekomponentar. Basert på https://informasjonsforvaltning.github.io/nasjonale-grunndata/#Adresse
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

from linkml_runtime.linkml_model.types import Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.11.0"
version = None

# Namespaces
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
GEO = CurieNamespace('geo', 'http://www.opengis.net/ont/geosparql#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LOCN = CurieNamespace('locn', 'http://www.w3.org/ns/locn#')
NGR = CurieNamespace('ngr', 'https://data.norge.no/vocabulary/ngr-adresse#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://data.norge.no/ngr/ngr-adresse/')


# Types

# Class references
class GeografiskAdresseId(URIorCURIE):
    pass


class OffisiellAdresseId(GeografiskAdresseId):
    pass


class PostboksadresseId(GeografiskAdresseId):
    pass


class AdressenavnId(URIorCURIE):
    pass


class AdresseomradeId(URIorCURIE):
    pass


class AdressekodeId(URIorCURIE):
    pass


class HusnummerId(URIorCURIE):
    pass


class BruksenhetsnummerId(URIorCURIE):
    pass


class RepresentasjonspunktId(URIorCURIE):
    pass


class GeografiskOmradeId(URIorCURIE):
    pass


class FylkeId(GeografiskOmradeId):
    pass


class KommuneId(GeografiskOmradeId):
    pass


class PoststedId(GeografiskOmradeId):
    pass


class GrunnkretsId(GeografiskOmradeId):
    pass


class TettstedId(GeografiskOmradeId):
    pass


class KirkesoknId(GeografiskOmradeId):
    pass


class StemmekretsId(GeografiskOmradeId):
    pass


class KommunalKretsId(GeografiskOmradeId):
    pass


class SvalbardId(GeografiskOmradeId):
    pass


class PostboksId(URIorCURIE):
    pass


class BygningId(URIorCURIE):
    pass


class BruksenhetId(URIorCURIE):
    pass


@dataclass(repr=False)
class AdresseContainer(YAMLRoot):
    """
    Rotklasse for NGR-adresse-datafiler. Held flate lister av alle instansierbare klassar; referansar mellom objekt
    brukar URI-lenking.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/AdresseContainer")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AdresseContainer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/AdresseContainer")

    offisielleAdresser: Optional[Union[dict[Union[str, OffisiellAdresseId], Union[dict, "OffisiellAdresse"]], list[Union[dict, "OffisiellAdresse"]]]] = empty_dict()
    postboksadresser: Optional[Union[dict[Union[str, PostboksadresseId], Union[dict, "Postboksadresse"]], list[Union[dict, "Postboksadresse"]]]] = empty_dict()
    adressenavn: Optional[Union[dict[Union[str, AdressenavnId], Union[dict, "Adressenavn"]], list[Union[dict, "Adressenavn"]]]] = empty_dict()
    adresseomrader: Optional[Union[dict[Union[str, AdresseomradeId], Union[dict, "Adresseomrade"]], list[Union[dict, "Adresseomrade"]]]] = empty_dict()
    adressekoder: Optional[Union[dict[Union[str, AdressekodeId], Union[dict, "Adressekode"]], list[Union[dict, "Adressekode"]]]] = empty_dict()
    husnummer: Optional[Union[dict[Union[str, HusnummerId], Union[dict, "Husnummer"]], list[Union[dict, "Husnummer"]]]] = empty_dict()
    bruksenhetsnummer: Optional[Union[dict[Union[str, BruksenhetsnummerId], Union[dict, "Bruksenhetsnummer"]], list[Union[dict, "Bruksenhetsnummer"]]]] = empty_dict()
    kommunar: Optional[Union[dict[Union[str, KommuneId], Union[dict, "Kommune"]], list[Union[dict, "Kommune"]]]] = empty_dict()
    fylke: Optional[Union[dict[Union[str, FylkeId], Union[dict, "Fylke"]], list[Union[dict, "Fylke"]]]] = empty_dict()
    poststeder: Optional[Union[dict[Union[str, PoststedId], Union[dict, "Poststed"]], list[Union[dict, "Poststed"]]]] = empty_dict()
    grunnkretsar: Optional[Union[dict[Union[str, GrunnkretsId], Union[dict, "Grunnkrets"]], list[Union[dict, "Grunnkrets"]]]] = empty_dict()
    tettstadar: Optional[Union[dict[Union[str, TettstedId], Union[dict, "Tettsted"]], list[Union[dict, "Tettsted"]]]] = empty_dict()
    kirkesokn: Optional[Union[dict[Union[str, KirkesoknId], Union[dict, "Kirkesokn"]], list[Union[dict, "Kirkesokn"]]]] = empty_dict()
    stemmekretsar: Optional[Union[dict[Union[str, StemmekretsId], Union[dict, "Stemmekrets"]], list[Union[dict, "Stemmekrets"]]]] = empty_dict()
    kommunaleKretsar: Optional[Union[dict[Union[str, KommunalKretsId], Union[dict, "KommunalKrets"]], list[Union[dict, "KommunalKrets"]]]] = empty_dict()
    svalbardOmrader: Optional[Union[dict[Union[str, SvalbardId], Union[dict, "Svalbard"]], list[Union[dict, "Svalbard"]]]] = empty_dict()
    postboksar: Optional[Union[dict[Union[str, PostboksId], Union[dict, "Postboks"]], list[Union[dict, "Postboks"]]]] = empty_dict()
    representasjonspunkt: Optional[Union[dict[Union[str, RepresentasjonspunktId], Union[dict, "Representasjonspunkt"]], list[Union[dict, "Representasjonspunkt"]]]] = empty_dict()
    bygningar: Optional[Union[list[Union[str, BygningId]], dict[Union[str, BygningId], Union[dict, "Bygning"]]]] = empty_dict()
    bruksenheter: Optional[Union[list[Union[str, BruksenhetId]], dict[Union[str, BruksenhetId], Union[dict, "Bruksenhet"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="offisielleAdresser", slot_type=OffisiellAdresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="postboksadresser", slot_type=Postboksadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="adressenavn", slot_type=Adressenavn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="adresseomrader", slot_type=Adresseomrade, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="adressekoder", slot_type=Adressekode, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="husnummer", slot_type=Husnummer, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="bruksenhetsnummer", slot_type=Bruksenhetsnummer, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kommunar", slot_type=Kommune, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fylke", slot_type=Fylke, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="poststeder", slot_type=Poststed, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="grunnkretsar", slot_type=Grunnkrets, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tettstadar", slot_type=Tettsted, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kirkesokn", slot_type=Kirkesokn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="stemmekretsar", slot_type=Stemmekrets, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kommunaleKretsar", slot_type=KommunalKrets, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="svalbardOmrader", slot_type=Svalbard, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="postboksar", slot_type=Postboks, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="representasjonspunkt", slot_type=Representasjonspunkt, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="bygningar", slot_type=Bygning, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="bruksenheter", slot_type=Bruksenhet, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeografiskAdresse(YAMLRoot):
    """
    Abstrakt basisklasse for norske adressar. Konkrete subklassar er OffisiellAdresse og Postboksadresse.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCN["Address"]
    class_class_curie: ClassVar[str] = "locn:Address"
    class_name: ClassVar[str] = "GeografiskAdresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/GeografiskAdresse")

    id: Union[str, GeografiskAdresseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeografiskAdresseId):
            self.id = GeografiskAdresseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OffisiellAdresse(GeografiskAdresse):
    """
    Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenavn + husnummer) eller matrikkelnummer.
    Forvaltas av Matrikkelen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["OffisiellAdresse"]
    class_class_curie: ClassVar[str] = "ngr:OffisiellAdresse"
    class_name: ClassVar[str] = "OffisiellAdresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/OffisiellAdresse")

    id: Union[str, OffisiellAdresseId] = None
    kommunenummer_ref: Union[str, KommuneId] = None
    adressenavn_ref: Union[str, AdressenavnId] = None
    adressekode_ref: Union[str, AdressekodeId] = None
    geografisk_omrade: Union[Union[str, GeografiskOmradeId], list[Union[str, GeografiskOmradeId]]] = None
    husnummer_ref: Optional[Union[str, HusnummerId]] = None
    bruksenhetsnummer_ref: Optional[Union[str, BruksenhetsnummerId]] = None
    representasjonspunkt_ref: Optional[Union[str, RepresentasjonspunktId]] = None
    adressetilleggsnavn: Optional[str] = None
    matrikkelnummer: Optional[str] = None
    adresserer_bygning: Optional[Union[str, BygningId]] = None
    adresserer_bruksenhet: Optional[Union[str, BruksenhetId]] = None
    adresserer_annet_objekt: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OffisiellAdresseId):
            self.id = OffisiellAdresseId(self.id)

        if self._is_empty(self.kommunenummer_ref):
            self.MissingRequiredField("kommunenummer_ref")
        if not isinstance(self.kommunenummer_ref, KommuneId):
            self.kommunenummer_ref = KommuneId(self.kommunenummer_ref)

        if self._is_empty(self.adressenavn_ref):
            self.MissingRequiredField("adressenavn_ref")
        if not isinstance(self.adressenavn_ref, AdressenavnId):
            self.adressenavn_ref = AdressenavnId(self.adressenavn_ref)

        if self._is_empty(self.adressekode_ref):
            self.MissingRequiredField("adressekode_ref")
        if not isinstance(self.adressekode_ref, AdressekodeId):
            self.adressekode_ref = AdressekodeId(self.adressekode_ref)

        if self._is_empty(self.geografisk_omrade):
            self.MissingRequiredField("geografisk_omrade")
        if not isinstance(self.geografisk_omrade, list):
            self.geografisk_omrade = [self.geografisk_omrade] if self.geografisk_omrade is not None else []
        self.geografisk_omrade = [v if isinstance(v, GeografiskOmradeId) else GeografiskOmradeId(v) for v in self.geografisk_omrade]

        if self.husnummer_ref is not None and not isinstance(self.husnummer_ref, HusnummerId):
            self.husnummer_ref = HusnummerId(self.husnummer_ref)

        if self.bruksenhetsnummer_ref is not None and not isinstance(self.bruksenhetsnummer_ref, BruksenhetsnummerId):
            self.bruksenhetsnummer_ref = BruksenhetsnummerId(self.bruksenhetsnummer_ref)

        if self.representasjonspunkt_ref is not None and not isinstance(self.representasjonspunkt_ref, RepresentasjonspunktId):
            self.representasjonspunkt_ref = RepresentasjonspunktId(self.representasjonspunkt_ref)

        if self.adressetilleggsnavn is not None and not isinstance(self.adressetilleggsnavn, str):
            self.adressetilleggsnavn = str(self.adressetilleggsnavn)

        if self.matrikkelnummer is not None and not isinstance(self.matrikkelnummer, str):
            self.matrikkelnummer = str(self.matrikkelnummer)

        if self.adresserer_bygning is not None and not isinstance(self.adresserer_bygning, BygningId):
            self.adresserer_bygning = BygningId(self.adresserer_bygning)

        if self.adresserer_bruksenhet is not None and not isinstance(self.adresserer_bruksenhet, BruksenhetId):
            self.adresserer_bruksenhet = BruksenhetId(self.adresserer_bruksenhet)

        if self.adresserer_annet_objekt is not None and not isinstance(self.adresserer_annet_objekt, URIorCURIE):
            self.adresserer_annet_objekt = URIorCURIE(self.adresserer_annet_objekt)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Postboksadresse(GeografiskAdresse):
    """
    Ei postboksadresse registrert i Postboksregisteret (Posten Norge).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Postboksadresse"]
    class_class_curie: ClassVar[str] = "ngr:Postboksadresse"
    class_name: ClassVar[str] = "Postboksadresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Postboksadresse")

    id: Union[str, PostboksadresseId] = None
    postboks_ref: Union[str, PostboksId] = None
    poststed_ref: Union[str, PoststedId] = None
    postboksanleggsnavn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PostboksadresseId):
            self.id = PostboksadresseId(self.id)

        if self._is_empty(self.postboks_ref):
            self.MissingRequiredField("postboks_ref")
        if not isinstance(self.postboks_ref, PostboksId):
            self.postboks_ref = PostboksId(self.postboks_ref)

        if self._is_empty(self.poststed_ref):
            self.MissingRequiredField("poststed_ref")
        if not isinstance(self.poststed_ref, PoststedId):
            self.poststed_ref = PoststedId(self.poststed_ref)

        if self.postboksanleggsnavn is not None and not isinstance(self.postboksanleggsnavn, str):
            self.postboksanleggsnavn = str(self.postboksanleggsnavn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Adressenavn(YAMLRoot):
    """
    Offisielt namn på ei veglenke eller eit adresseobjekt i ein kommune, tildelt av kommunen og godkjent av Kartverket.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Adressenavn"]
    class_class_curie: ClassVar[str] = "ngr:Adressenavn"
    class_name: ClassVar[str] = "Adressenavn"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Adressenavn")

    id: Union[str, AdressenavnId] = None
    adressenavn_tekst: str = None
    adresseomrade_ref: Union[str, AdresseomradeId] = None
    har_adressekode: Union[str, AdressekodeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdressenavnId):
            self.id = AdressenavnId(self.id)

        if self._is_empty(self.adressenavn_tekst):
            self.MissingRequiredField("adressenavn_tekst")
        if not isinstance(self.adressenavn_tekst, str):
            self.adressenavn_tekst = str(self.adressenavn_tekst)

        if self._is_empty(self.adresseomrade_ref):
            self.MissingRequiredField("adresseomrade_ref")
        if not isinstance(self.adresseomrade_ref, AdresseomradeId):
            self.adresseomrade_ref = AdresseomradeId(self.adresseomrade_ref)

        if self._is_empty(self.har_adressekode):
            self.MissingRequiredField("har_adressekode")
        if not isinstance(self.har_adressekode, AdressekodeId):
            self.har_adressekode = AdressekodeId(self.har_adressekode)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Adresseomrade(YAMLRoot):
    """
    Geografisk område eit adressenavn høyrer til, t.d. ei gate, eit veg eller eit stadnamn.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Adresseomrade"]
    class_class_curie: ClassVar[str] = "ngr:Adresseomrade"
    class_name: ClassVar[str] = "Adresseomrade"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Adresseomrade")

    id: Union[str, AdresseomradeId] = None
    namn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdresseomradeId):
            self.id = AdresseomradeId(self.id)

        if self.namn is not None and not isinstance(self.namn, str):
            self.namn = str(self.namn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Adressekode(YAMLRoot):
    """
    Firesifra kommunal kode som identifiserer eit adressenavn.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Adressekode"]
    class_class_curie: ClassVar[str] = "ngr:Adressekode"
    class_name: ClassVar[str] = "Adressekode"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Adressekode")

    id: Union[str, AdressekodeId] = None
    kode: int = None
    adresseomrade_ref: Optional[Union[str, AdresseomradeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdressekodeId):
            self.id = AdressekodeId(self.id)

        if self._is_empty(self.kode):
            self.MissingRequiredField("kode")
        if not isinstance(self.kode, int):
            self.kode = int(self.kode)

        if self.adresseomrade_ref is not None and not isinstance(self.adresseomrade_ref, AdresseomradeId):
            self.adresseomrade_ref = AdresseomradeId(self.adresseomrade_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Husnummer(YAMLRoot):
    """
    Husnummer beståande av eit obligatorisk nummer og ein valfri bokstav (t.d. 12 eller 12B).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Husnummer"]
    class_class_curie: ClassVar[str] = "ngr:Husnummer"
    class_name: ClassVar[str] = "Husnummer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Husnummer")

    id: Union[str, HusnummerId] = None
    nummer: int = None
    bokstav: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HusnummerId):
            self.id = HusnummerId(self.id)

        if self._is_empty(self.nummer):
            self.MissingRequiredField("nummer")
        if not isinstance(self.nummer, int):
            self.nummer = int(self.nummer)

        if self.bokstav is not None and not isinstance(self.bokstav, str):
            self.bokstav = str(self.bokstav)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bruksenhetsnummer(YAMLRoot):
    """
    Identifikator for ei brukseining (leilegheit o.l.) innanfor ein bygning, t.d. H0201 = 2. etasje, eining 1.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Bruksenhetsnummer"]
    class_class_curie: ClassVar[str] = "ngr:Bruksenhetsnummer"
    class_name: ClassVar[str] = "Bruksenhetsnummer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Bruksenhetsnummer")

    id: Union[str, BruksenhetsnummerId] = None
    etasjeplan: Union[str, "Etasjeplan"] = None
    etasjenummer: int = None
    nummerering_i_etasjen: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BruksenhetsnummerId):
            self.id = BruksenhetsnummerId(self.id)

        if self._is_empty(self.etasjeplan):
            self.MissingRequiredField("etasjeplan")
        if not isinstance(self.etasjeplan, Etasjeplan):
            self.etasjeplan = Etasjeplan(self.etasjeplan)

        if self._is_empty(self.etasjenummer):
            self.MissingRequiredField("etasjenummer")
        if not isinstance(self.etasjenummer, int):
            self.etasjenummer = int(self.etasjenummer)

        if self._is_empty(self.nummerering_i_etasjen):
            self.MissingRequiredField("nummerering_i_etasjen")
        if not isinstance(self.nummerering_i_etasjen, int):
            self.nummerering_i_etasjen = int(self.nummerering_i_etasjen)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Representasjonspunkt(YAMLRoot):
    """
    Eit geografisk punkt (koordinatpar) som representerer posisjonen til adressa.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Representasjonspunkt"]
    class_class_curie: ClassVar[str] = "ngr:Representasjonspunkt"
    class_name: ClassVar[str] = "Representasjonspunkt"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Representasjonspunkt")

    id: Union[str, RepresentasjonspunktId] = None
    koordinat_ost: float = None
    koordinat_nord: float = None
    koordinatsystem: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RepresentasjonspunktId):
            self.id = RepresentasjonspunktId(self.id)

        if self._is_empty(self.koordinat_ost):
            self.MissingRequiredField("koordinat_ost")
        if not isinstance(self.koordinat_ost, float):
            self.koordinat_ost = float(self.koordinat_ost)

        if self._is_empty(self.koordinat_nord):
            self.MissingRequiredField("koordinat_nord")
        if not isinstance(self.koordinat_nord, float):
            self.koordinat_nord = float(self.koordinat_nord)

        if self.koordinatsystem is not None and not isinstance(self.koordinatsystem, str):
            self.koordinatsystem = str(self.koordinatsystem)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeografiskOmrade(YAMLRoot):
    """
    Abstrakt klasse for geografiske inndelingar som offisielle adressar refererer til.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["GeografiskOmrade"]
    class_class_curie: ClassVar[str] = "ngr:GeografiskOmrade"
    class_name: ClassVar[str] = "GeografiskOmrade"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/GeografiskOmrade")

    id: Union[str, GeografiskOmradeId] = None
    namn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeografiskOmradeId):
            self.id = GeografiskOmradeId(self.id)

        if self.namn is not None and not isinstance(self.namn, str):
            self.namn = str(self.namn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fylke(GeografiskOmrade):
    """
    Eit norsk fylke.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Fylke"]
    class_class_curie: ClassVar[str] = "ngr:Fylke"
    class_name: ClassVar[str] = "Fylke"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Fylke")

    id: Union[str, FylkeId] = None
    fylkesnummer: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FylkeId):
            self.id = FylkeId(self.id)

        if self._is_empty(self.fylkesnummer):
            self.MissingRequiredField("fylkesnummer")
        if not isinstance(self.fylkesnummer, str):
            self.fylkesnummer = str(self.fylkesnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kommune(GeografiskOmrade):
    """
    Ein norsk kommune.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Kommune"]
    class_class_curie: ClassVar[str] = "ngr:Kommune"
    class_name: ClassVar[str] = "Kommune"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Kommune")

    id: Union[str, KommuneId] = None
    kommunenummer_kode: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KommuneId):
            self.id = KommuneId(self.id)

        if self._is_empty(self.kommunenummer_kode):
            self.MissingRequiredField("kommunenummer_kode")
        if not isinstance(self.kommunenummer_kode, str):
            self.kommunenummer_kode = str(self.kommunenummer_kode)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Poststed(GeografiskOmrade):
    """
    Eit poststed identifisert med postnummer, forvalta av Postnummerregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Poststed"]
    class_class_curie: ClassVar[str] = "ngr:Poststed"
    class_name: ClassVar[str] = "Poststed"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Poststed")

    id: Union[str, PoststedId] = None
    postnummer: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PoststedId):
            self.id = PoststedId(self.id)

        if self._is_empty(self.postnummer):
            self.MissingRequiredField("postnummer")
        if not isinstance(self.postnummer, str):
            self.postnummer = str(self.postnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Grunnkrets(GeografiskOmrade):
    """
    Ei grunnkrets – minste geografiske eining i statistisk inndeling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Grunnkrets"]
    class_class_curie: ClassVar[str] = "ngr:Grunnkrets"
    class_name: ClassVar[str] = "Grunnkrets"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Grunnkrets")

    id: Union[str, GrunnkretsId] = None
    grunnkretsnummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GrunnkretsId):
            self.id = GrunnkretsId(self.id)

        if self.grunnkretsnummer is not None and not isinstance(self.grunnkretsnummer, str):
            self.grunnkretsnummer = str(self.grunnkretsnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tettsted(GeografiskOmrade):
    """
    Eit tettbygd område definert av SSB.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Tettsted"]
    class_class_curie: ClassVar[str] = "ngr:Tettsted"
    class_name: ClassVar[str] = "Tettsted"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Tettsted")

    id: Union[str, TettstedId] = None
    tettstedsnummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TettstedId):
            self.id = TettstedId(self.id)

        if self.tettstedsnummer is not None and not isinstance(self.tettstedsnummer, str):
            self.tettstedsnummer = str(self.tettstedsnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kirkesokn(GeografiskOmrade):
    """
    Eit kyrkjesokn.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Kirkesokn"]
    class_class_curie: ClassVar[str] = "ngr:Kirkesokn"
    class_name: ClassVar[str] = "Kirkesokn"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Kirkesokn")

    id: Union[str, KirkesoknId] = None
    kirkesoknnummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KirkesoknId):
            self.id = KirkesoknId(self.id)

        if self.kirkesoknnummer is not None and not isinstance(self.kirkesoknnummer, str):
            self.kirkesoknnummer = str(self.kirkesoknnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Stemmekrets(GeografiskOmrade):
    """
    Ei stemmekrets brukt ved val.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Stemmekrets"]
    class_class_curie: ClassVar[str] = "ngr:Stemmekrets"
    class_name: ClassVar[str] = "Stemmekrets"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Stemmekrets")

    id: Union[str, StemmekretsId] = None
    stemmekretsnummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StemmekretsId):
            self.id = StemmekretsId(self.id)

        if self.stemmekretsnummer is not None and not isinstance(self.stemmekretsnummer, str):
            self.stemmekretsnummer = str(self.stemmekretsnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KommunalKrets(GeografiskOmrade):
    """
    Ein kommunal krets (administrativ inndeling definert av kommunen).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["KommunalKrets"]
    class_class_curie: ClassVar[str] = "ngr:KommunalKrets"
    class_name: ClassVar[str] = "KommunalKrets"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/KommunalKrets")

    id: Union[str, KommunalKretsId] = None
    kretsnummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KommunalKretsId):
            self.id = KommunalKretsId(self.id)

        if self.kretsnummer is not None and not isinstance(self.kretsnummer, str):
            self.kretsnummer = str(self.kretsnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Svalbard(GeografiskOmrade):
    """
    Svalbard som særskild geografisk område.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Svalbard"]
    class_class_curie: ClassVar[str] = "ngr:Svalbard"
    class_name: ClassVar[str] = "Svalbard"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Svalbard")

    id: Union[str, SvalbardId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SvalbardId):
            self.id = SvalbardId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Postboks(YAMLRoot):
    """
    Ei postboks registrert i Postboksregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Postboks"]
    class_class_curie: ClassVar[str] = "ngr:Postboks"
    class_name: ClassVar[str] = "Postboks"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Postboks")

    id: Union[str, PostboksId] = None
    postboksnummer: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PostboksId):
            self.id = PostboksId(self.id)

        if self._is_empty(self.postboksnummer):
            self.MissingRequiredField("postboksnummer")
        if not isinstance(self.postboksnummer, int):
            self.postboksnummer = int(self.postboksnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bygning(YAMLRoot):
    """
    Referanse til ein bygning i Matrikkelen. Offisiell adresse kan adressere ytre inngang(ar) til bygningen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Bygning"]
    class_class_curie: ClassVar[str] = "ngr:Bygning"
    class_name: ClassVar[str] = "Bygning"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Bygning")

    id: Union[str, BygningId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BygningId):
            self.id = BygningId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bruksenhet(YAMLRoot):
    """
    Referanse til ei brukseining (leilegheit/lokale) i Matrikkelen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGR["Bruksenhet"]
    class_class_curie: ClassVar[str] = "ngr:Bruksenhet"
    class_name: ClassVar[str] = "Bruksenhet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ngr/ngr-adresse/Bruksenhet")

    id: Union[str, BruksenhetId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BruksenhetId):
            self.id = BruksenhetId(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class Etasjeplan(EnumDefinitionImpl):
    """
    Kode for kva del av bygningen eit bruksenhetsnummer refererer til.
    """
    H = PermissibleValue(
        text="H",
        description="Høgde (over bakkenivå)")
    U = PermissibleValue(
        text="U",
        description="Under bakkenivå")
    K = PermissibleValue(
        text="K",
        description="Kjellar")
    L = PermissibleValue(
        text="L",
        description="Loft")
    M = PermissibleValue(
        text="M",
        description="Mesanin")

    _defn = EnumDefinition(
        name="Etasjeplan",
        description="Kode for kva del av bygningen eit bruksenhetsnummer refererer til.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.kommunenummer_ref = Slot(uri=NGR.harKommunenummer, name="kommunenummer_ref", curie=NGR.curie('harKommunenummer'),
                   model_uri=DEFAULT_.kommunenummer_ref, domain=None, range=Optional[Union[str, KommuneId]])

slots.adressenavn_ref = Slot(uri=NGR.harAdressenavn, name="adressenavn_ref", curie=NGR.curie('harAdressenavn'),
                   model_uri=DEFAULT_.adressenavn_ref, domain=None, range=Optional[Union[str, AdressenavnId]])

slots.adressekode_ref = Slot(uri=NGR.harAdressekode, name="adressekode_ref", curie=NGR.curie('harAdressekode'),
                   model_uri=DEFAULT_.adressekode_ref, domain=None, range=Optional[Union[str, AdressekodeId]])

slots.husnummer_ref = Slot(uri=NGR.harHusnummer, name="husnummer_ref", curie=NGR.curie('harHusnummer'),
                   model_uri=DEFAULT_.husnummer_ref, domain=None, range=Optional[Union[str, HusnummerId]])

slots.bruksenhetsnummer_ref = Slot(uri=NGR.harBruksenhetsnummer, name="bruksenhetsnummer_ref", curie=NGR.curie('harBruksenhetsnummer'),
                   model_uri=DEFAULT_.bruksenhetsnummer_ref, domain=None, range=Optional[Union[str, BruksenhetsnummerId]])

slots.representasjonspunkt_ref = Slot(uri=NGR.harRepresentasjonspunkt, name="representasjonspunkt_ref", curie=NGR.curie('harRepresentasjonspunkt'),
                   model_uri=DEFAULT_.representasjonspunkt_ref, domain=None, range=Optional[Union[str, RepresentasjonspunktId]])

slots.adresseomrade_ref = Slot(uri=NGR.harAdresseomrade, name="adresseomrade_ref", curie=NGR.curie('harAdresseomrade'),
                   model_uri=DEFAULT_.adresseomrade_ref, domain=None, range=Optional[Union[str, AdresseomradeId]])

slots.har_adressekode = Slot(uri=NGR.harAdressekode, name="har_adressekode", curie=NGR.curie('harAdressekode'),
                   model_uri=DEFAULT_.har_adressekode, domain=None, range=Optional[Union[str, AdressekodeId]])

slots.geografisk_omrade = Slot(uri=NGR.referererTilGeografiskOmrade, name="geografisk_omrade", curie=NGR.curie('referererTilGeografiskOmrade'),
                   model_uri=DEFAULT_.geografisk_omrade, domain=None, range=Optional[Union[Union[str, GeografiskOmradeId], list[Union[str, GeografiskOmradeId]]]])

slots.adresserer_bygning = Slot(uri=NGR.adressererBygning, name="adresserer_bygning", curie=NGR.curie('adressererBygning'),
                   model_uri=DEFAULT_.adresserer_bygning, domain=None, range=Optional[Union[str, BygningId]])

slots.adresserer_bruksenhet = Slot(uri=NGR.adressererBruksenhet, name="adresserer_bruksenhet", curie=NGR.curie('adressererBruksenhet'),
                   model_uri=DEFAULT_.adresserer_bruksenhet, domain=None, range=Optional[Union[str, BruksenhetId]])

slots.adresserer_annet_objekt = Slot(uri=NGR.adressererAnnetObjekt, name="adresserer_annet_objekt", curie=NGR.curie('adressererAnnetObjekt'),
                   model_uri=DEFAULT_.adresserer_annet_objekt, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.postboks_ref = Slot(uri=NGR.harPostboks, name="postboks_ref", curie=NGR.curie('harPostboks'),
                   model_uri=DEFAULT_.postboks_ref, domain=None, range=Optional[Union[str, PostboksId]])

slots.poststed_ref = Slot(uri=NGR.referererTilPoststed, name="poststed_ref", curie=NGR.curie('referererTilPoststed'),
                   model_uri=DEFAULT_.poststed_ref, domain=None, range=Optional[Union[str, PoststedId]])

slots.adressenavn_tekst = Slot(uri=LOCN.thoroughfare, name="adressenavn_tekst", curie=LOCN.curie('thoroughfare'),
                   model_uri=DEFAULT_.adressenavn_tekst, domain=None, range=Optional[str])

slots.adressetilleggsnavn = Slot(uri=NGR.adressetilleggsnavn, name="adressetilleggsnavn", curie=NGR.curie('adressetilleggsnavn'),
                   model_uri=DEFAULT_.adressetilleggsnavn, domain=None, range=Optional[str])

slots.matrikkelnummer = Slot(uri=NGR.matrikkelnummer, name="matrikkelnummer", curie=NGR.curie('matrikkelnummer'),
                   model_uri=DEFAULT_.matrikkelnummer, domain=None, range=Optional[str])

slots.namn = Slot(uri=NGR.namn, name="namn", curie=NGR.curie('namn'),
                   model_uri=DEFAULT_.namn, domain=None, range=Optional[str])

slots.kode = Slot(uri=NGR.kode, name="kode", curie=NGR.curie('kode'),
                   model_uri=DEFAULT_.kode, domain=None, range=Optional[int])

slots.postboksanleggsnavn = Slot(uri=NGR.postboksanleggsnavn, name="postboksanleggsnavn", curie=NGR.curie('postboksanleggsnavn'),
                   model_uri=DEFAULT_.postboksanleggsnavn, domain=None, range=Optional[str])

slots.kommunenummer_kode = Slot(uri=NGR.kommunenummer, name="kommunenummer_kode", curie=NGR.curie('kommunenummer'),
                   model_uri=DEFAULT_.kommunenummer_kode, domain=None, range=Optional[str])

slots.fylkesnummer = Slot(uri=NGR.fylkesnummer, name="fylkesnummer", curie=NGR.curie('fylkesnummer'),
                   model_uri=DEFAULT_.fylkesnummer, domain=None, range=Optional[str])

slots.postnummer = Slot(uri=LOCN.postCode, name="postnummer", curie=LOCN.curie('postCode'),
                   model_uri=DEFAULT_.postnummer, domain=None, range=Optional[str])

slots.postboksnummer = Slot(uri=NGR.postboksnummer, name="postboksnummer", curie=NGR.curie('postboksnummer'),
                   model_uri=DEFAULT_.postboksnummer, domain=None, range=Optional[int])

slots.grunnkretsnummer = Slot(uri=NGR.grunnkretsnummer, name="grunnkretsnummer", curie=NGR.curie('grunnkretsnummer'),
                   model_uri=DEFAULT_.grunnkretsnummer, domain=None, range=Optional[str])

slots.tettstedsnummer = Slot(uri=NGR.tettstedsnummer, name="tettstedsnummer", curie=NGR.curie('tettstedsnummer'),
                   model_uri=DEFAULT_.tettstedsnummer, domain=None, range=Optional[str])

slots.kirkesoknnummer = Slot(uri=NGR.kirkesoknnummer, name="kirkesoknnummer", curie=NGR.curie('kirkesoknnummer'),
                   model_uri=DEFAULT_.kirkesoknnummer, domain=None, range=Optional[str])

slots.stemmekretsnummer = Slot(uri=NGR.stemmekretsnummer, name="stemmekretsnummer", curie=NGR.curie('stemmekretsnummer'),
                   model_uri=DEFAULT_.stemmekretsnummer, domain=None, range=Optional[str])

slots.kretsnummer = Slot(uri=NGR.kretsnummer, name="kretsnummer", curie=NGR.curie('kretsnummer'),
                   model_uri=DEFAULT_.kretsnummer, domain=None, range=Optional[str])

slots.nummer = Slot(uri=NGR.nummer, name="nummer", curie=NGR.curie('nummer'),
                   model_uri=DEFAULT_.nummer, domain=None, range=Optional[int])

slots.bokstav = Slot(uri=NGR.bokstav, name="bokstav", curie=NGR.curie('bokstav'),
                   model_uri=DEFAULT_.bokstav, domain=None, range=Optional[str])

slots.etasjeplan = Slot(uri=NGR.etasjeplan, name="etasjeplan", curie=NGR.curie('etasjeplan'),
                   model_uri=DEFAULT_.etasjeplan, domain=None, range=Optional[Union[str, "Etasjeplan"]])

slots.etasjenummer = Slot(uri=NGR.etasjenummer, name="etasjenummer", curie=NGR.curie('etasjenummer'),
                   model_uri=DEFAULT_.etasjenummer, domain=None, range=Optional[int])

slots.nummerering_i_etasjen = Slot(uri=NGR.nummereringIEtasjen, name="nummerering_i_etasjen", curie=NGR.curie('nummereringIEtasjen'),
                   model_uri=DEFAULT_.nummerering_i_etasjen, domain=None, range=Optional[int])

slots.koordinat_ost = Slot(uri=NGR.koordinatOst, name="koordinat_ost", curie=NGR.curie('koordinatOst'),
                   model_uri=DEFAULT_.koordinat_ost, domain=None, range=Optional[float])

slots.koordinat_nord = Slot(uri=NGR.koordinatNord, name="koordinat_nord", curie=NGR.curie('koordinatNord'),
                   model_uri=DEFAULT_.koordinat_nord, domain=None, range=Optional[float])

slots.koordinatsystem = Slot(uri=NGR.koordinatsystem, name="koordinatsystem", curie=NGR.curie('koordinatsystem'),
                   model_uri=DEFAULT_.koordinatsystem, domain=None, range=Optional[str])

slots.adresseContainer__offisielleAdresser = Slot(uri=DEFAULT_.offisielleAdresser, name="adresseContainer__offisielleAdresser", curie=DEFAULT_.curie('offisielleAdresser'),
                   model_uri=DEFAULT_.adresseContainer__offisielleAdresser, domain=None, range=Optional[Union[dict[Union[str, OffisiellAdresseId], Union[dict, OffisiellAdresse]], list[Union[dict, OffisiellAdresse]]]])

slots.adresseContainer__postboksadresser = Slot(uri=DEFAULT_.postboksadresser, name="adresseContainer__postboksadresser", curie=DEFAULT_.curie('postboksadresser'),
                   model_uri=DEFAULT_.adresseContainer__postboksadresser, domain=None, range=Optional[Union[dict[Union[str, PostboksadresseId], Union[dict, Postboksadresse]], list[Union[dict, Postboksadresse]]]])

slots.adresseContainer__adressenavn = Slot(uri=DEFAULT_.adressenavn, name="adresseContainer__adressenavn", curie=DEFAULT_.curie('adressenavn'),
                   model_uri=DEFAULT_.adresseContainer__adressenavn, domain=None, range=Optional[Union[dict[Union[str, AdressenavnId], Union[dict, Adressenavn]], list[Union[dict, Adressenavn]]]])

slots.adresseContainer__adresseomrader = Slot(uri=DEFAULT_.adresseomrader, name="adresseContainer__adresseomrader", curie=DEFAULT_.curie('adresseomrader'),
                   model_uri=DEFAULT_.adresseContainer__adresseomrader, domain=None, range=Optional[Union[dict[Union[str, AdresseomradeId], Union[dict, Adresseomrade]], list[Union[dict, Adresseomrade]]]])

slots.adresseContainer__adressekoder = Slot(uri=DEFAULT_.adressekoder, name="adresseContainer__adressekoder", curie=DEFAULT_.curie('adressekoder'),
                   model_uri=DEFAULT_.adresseContainer__adressekoder, domain=None, range=Optional[Union[dict[Union[str, AdressekodeId], Union[dict, Adressekode]], list[Union[dict, Adressekode]]]])

slots.adresseContainer__husnummer = Slot(uri=DEFAULT_.husnummer, name="adresseContainer__husnummer", curie=DEFAULT_.curie('husnummer'),
                   model_uri=DEFAULT_.adresseContainer__husnummer, domain=None, range=Optional[Union[dict[Union[str, HusnummerId], Union[dict, Husnummer]], list[Union[dict, Husnummer]]]])

slots.adresseContainer__bruksenhetsnummer = Slot(uri=DEFAULT_.bruksenhetsnummer, name="adresseContainer__bruksenhetsnummer", curie=DEFAULT_.curie('bruksenhetsnummer'),
                   model_uri=DEFAULT_.adresseContainer__bruksenhetsnummer, domain=None, range=Optional[Union[dict[Union[str, BruksenhetsnummerId], Union[dict, Bruksenhetsnummer]], list[Union[dict, Bruksenhetsnummer]]]])

slots.adresseContainer__kommunar = Slot(uri=DEFAULT_.kommunar, name="adresseContainer__kommunar", curie=DEFAULT_.curie('kommunar'),
                   model_uri=DEFAULT_.adresseContainer__kommunar, domain=None, range=Optional[Union[dict[Union[str, KommuneId], Union[dict, Kommune]], list[Union[dict, Kommune]]]])

slots.adresseContainer__fylke = Slot(uri=DEFAULT_.fylke, name="adresseContainer__fylke", curie=DEFAULT_.curie('fylke'),
                   model_uri=DEFAULT_.adresseContainer__fylke, domain=None, range=Optional[Union[dict[Union[str, FylkeId], Union[dict, Fylke]], list[Union[dict, Fylke]]]])

slots.adresseContainer__poststeder = Slot(uri=DEFAULT_.poststeder, name="adresseContainer__poststeder", curie=DEFAULT_.curie('poststeder'),
                   model_uri=DEFAULT_.adresseContainer__poststeder, domain=None, range=Optional[Union[dict[Union[str, PoststedId], Union[dict, Poststed]], list[Union[dict, Poststed]]]])

slots.adresseContainer__grunnkretsar = Slot(uri=DEFAULT_.grunnkretsar, name="adresseContainer__grunnkretsar", curie=DEFAULT_.curie('grunnkretsar'),
                   model_uri=DEFAULT_.adresseContainer__grunnkretsar, domain=None, range=Optional[Union[dict[Union[str, GrunnkretsId], Union[dict, Grunnkrets]], list[Union[dict, Grunnkrets]]]])

slots.adresseContainer__tettstadar = Slot(uri=DEFAULT_.tettstadar, name="adresseContainer__tettstadar", curie=DEFAULT_.curie('tettstadar'),
                   model_uri=DEFAULT_.adresseContainer__tettstadar, domain=None, range=Optional[Union[dict[Union[str, TettstedId], Union[dict, Tettsted]], list[Union[dict, Tettsted]]]])

slots.adresseContainer__kirkesokn = Slot(uri=DEFAULT_.kirkesokn, name="adresseContainer__kirkesokn", curie=DEFAULT_.curie('kirkesokn'),
                   model_uri=DEFAULT_.adresseContainer__kirkesokn, domain=None, range=Optional[Union[dict[Union[str, KirkesoknId], Union[dict, Kirkesokn]], list[Union[dict, Kirkesokn]]]])

slots.adresseContainer__stemmekretsar = Slot(uri=DEFAULT_.stemmekretsar, name="adresseContainer__stemmekretsar", curie=DEFAULT_.curie('stemmekretsar'),
                   model_uri=DEFAULT_.adresseContainer__stemmekretsar, domain=None, range=Optional[Union[dict[Union[str, StemmekretsId], Union[dict, Stemmekrets]], list[Union[dict, Stemmekrets]]]])

slots.adresseContainer__kommunaleKretsar = Slot(uri=DEFAULT_.kommunaleKretsar, name="adresseContainer__kommunaleKretsar", curie=DEFAULT_.curie('kommunaleKretsar'),
                   model_uri=DEFAULT_.adresseContainer__kommunaleKretsar, domain=None, range=Optional[Union[dict[Union[str, KommunalKretsId], Union[dict, KommunalKrets]], list[Union[dict, KommunalKrets]]]])

slots.adresseContainer__svalbardOmrader = Slot(uri=DEFAULT_.svalbardOmrader, name="adresseContainer__svalbardOmrader", curie=DEFAULT_.curie('svalbardOmrader'),
                   model_uri=DEFAULT_.adresseContainer__svalbardOmrader, domain=None, range=Optional[Union[dict[Union[str, SvalbardId], Union[dict, Svalbard]], list[Union[dict, Svalbard]]]])

slots.adresseContainer__postboksar = Slot(uri=DEFAULT_.postboksar, name="adresseContainer__postboksar", curie=DEFAULT_.curie('postboksar'),
                   model_uri=DEFAULT_.adresseContainer__postboksar, domain=None, range=Optional[Union[dict[Union[str, PostboksId], Union[dict, Postboks]], list[Union[dict, Postboks]]]])

slots.adresseContainer__representasjonspunkt = Slot(uri=DEFAULT_.representasjonspunkt, name="adresseContainer__representasjonspunkt", curie=DEFAULT_.curie('representasjonspunkt'),
                   model_uri=DEFAULT_.adresseContainer__representasjonspunkt, domain=None, range=Optional[Union[dict[Union[str, RepresentasjonspunktId], Union[dict, Representasjonspunkt]], list[Union[dict, Representasjonspunkt]]]])

slots.adresseContainer__bygningar = Slot(uri=DEFAULT_.bygningar, name="adresseContainer__bygningar", curie=DEFAULT_.curie('bygningar'),
                   model_uri=DEFAULT_.adresseContainer__bygningar, domain=None, range=Optional[Union[list[Union[str, BygningId]], dict[Union[str, BygningId], Union[dict, Bygning]]]])

slots.adresseContainer__bruksenheter = Slot(uri=DEFAULT_.bruksenheter, name="adresseContainer__bruksenheter", curie=DEFAULT_.curie('bruksenheter'),
                   model_uri=DEFAULT_.adresseContainer__bruksenheter, domain=None, range=Optional[Union[list[Union[str, BruksenhetId]], dict[Union[str, BruksenhetId], Union[dict, Bruksenhet]]]])

slots.OffisiellAdresse_kommunenummer_ref = Slot(uri=NGR.harKommunenummer, name="OffisiellAdresse_kommunenummer_ref", curie=NGR.curie('harKommunenummer'),
                   model_uri=DEFAULT_.OffisiellAdresse_kommunenummer_ref, domain=OffisiellAdresse, range=Union[str, KommuneId])

slots.OffisiellAdresse_adressenavn_ref = Slot(uri=NGR.harAdressenavn, name="OffisiellAdresse_adressenavn_ref", curie=NGR.curie('harAdressenavn'),
                   model_uri=DEFAULT_.OffisiellAdresse_adressenavn_ref, domain=OffisiellAdresse, range=Union[str, AdressenavnId])

slots.OffisiellAdresse_adressekode_ref = Slot(uri=NGR.harAdressekode, name="OffisiellAdresse_adressekode_ref", curie=NGR.curie('harAdressekode'),
                   model_uri=DEFAULT_.OffisiellAdresse_adressekode_ref, domain=OffisiellAdresse, range=Union[str, AdressekodeId])

slots.OffisiellAdresse_husnummer_ref = Slot(uri=NGR.harHusnummer, name="OffisiellAdresse_husnummer_ref", curie=NGR.curie('harHusnummer'),
                   model_uri=DEFAULT_.OffisiellAdresse_husnummer_ref, domain=OffisiellAdresse, range=Optional[Union[str, HusnummerId]])

slots.OffisiellAdresse_representasjonspunkt_ref = Slot(uri=NGR.harRepresentasjonspunkt, name="OffisiellAdresse_representasjonspunkt_ref", curie=NGR.curie('harRepresentasjonspunkt'),
                   model_uri=DEFAULT_.OffisiellAdresse_representasjonspunkt_ref, domain=OffisiellAdresse, range=Optional[Union[str, RepresentasjonspunktId]])

slots.OffisiellAdresse_geografisk_omrade = Slot(uri=NGR.referererTilGeografiskOmrade, name="OffisiellAdresse_geografisk_omrade", curie=NGR.curie('referererTilGeografiskOmrade'),
                   model_uri=DEFAULT_.OffisiellAdresse_geografisk_omrade, domain=OffisiellAdresse, range=Union[Union[str, GeografiskOmradeId], list[Union[str, GeografiskOmradeId]]])

slots.OffisiellAdresse_bruksenhetsnummer_ref = Slot(uri=NGR.harBruksenhetsnummer, name="OffisiellAdresse_bruksenhetsnummer_ref", curie=NGR.curie('harBruksenhetsnummer'),
                   model_uri=DEFAULT_.OffisiellAdresse_bruksenhetsnummer_ref, domain=OffisiellAdresse, range=Optional[Union[str, BruksenhetsnummerId]])

slots.OffisiellAdresse_adressetilleggsnavn = Slot(uri=NGR.adressetilleggsnavn, name="OffisiellAdresse_adressetilleggsnavn", curie=NGR.curie('adressetilleggsnavn'),
                   model_uri=DEFAULT_.OffisiellAdresse_adressetilleggsnavn, domain=OffisiellAdresse, range=Optional[str])

slots.OffisiellAdresse_matrikkelnummer = Slot(uri=NGR.matrikkelnummer, name="OffisiellAdresse_matrikkelnummer", curie=NGR.curie('matrikkelnummer'),
                   model_uri=DEFAULT_.OffisiellAdresse_matrikkelnummer, domain=OffisiellAdresse, range=Optional[str])

slots.OffisiellAdresse_adresserer_bygning = Slot(uri=NGR.adressererBygning, name="OffisiellAdresse_adresserer_bygning", curie=NGR.curie('adressererBygning'),
                   model_uri=DEFAULT_.OffisiellAdresse_adresserer_bygning, domain=OffisiellAdresse, range=Optional[Union[str, BygningId]])

slots.OffisiellAdresse_adresserer_bruksenhet = Slot(uri=NGR.adressererBruksenhet, name="OffisiellAdresse_adresserer_bruksenhet", curie=NGR.curie('adressererBruksenhet'),
                   model_uri=DEFAULT_.OffisiellAdresse_adresserer_bruksenhet, domain=OffisiellAdresse, range=Optional[Union[str, BruksenhetId]])

slots.OffisiellAdresse_adresserer_annet_objekt = Slot(uri=NGR.adressererAnnetObjekt, name="OffisiellAdresse_adresserer_annet_objekt", curie=NGR.curie('adressererAnnetObjekt'),
                   model_uri=DEFAULT_.OffisiellAdresse_adresserer_annet_objekt, domain=OffisiellAdresse, range=Optional[Union[str, URIorCURIE]])

slots.Postboksadresse_postboks_ref = Slot(uri=NGR.harPostboks, name="Postboksadresse_postboks_ref", curie=NGR.curie('harPostboks'),
                   model_uri=DEFAULT_.Postboksadresse_postboks_ref, domain=Postboksadresse, range=Union[str, PostboksId])

slots.Postboksadresse_poststed_ref = Slot(uri=NGR.referererTilPoststed, name="Postboksadresse_poststed_ref", curie=NGR.curie('referererTilPoststed'),
                   model_uri=DEFAULT_.Postboksadresse_poststed_ref, domain=Postboksadresse, range=Union[str, PoststedId])

slots.Postboksadresse_postboksanleggsnavn = Slot(uri=NGR.postboksanleggsnavn, name="Postboksadresse_postboksanleggsnavn", curie=NGR.curie('postboksanleggsnavn'),
                   model_uri=DEFAULT_.Postboksadresse_postboksanleggsnavn, domain=Postboksadresse, range=Optional[str])

slots.Adressenavn_adressenavn_tekst = Slot(uri=LOCN.thoroughfare, name="Adressenavn_adressenavn_tekst", curie=LOCN.curie('thoroughfare'),
                   model_uri=DEFAULT_.Adressenavn_adressenavn_tekst, domain=Adressenavn, range=str)

slots.Adressenavn_adresseomrade_ref = Slot(uri=NGR.harAdresseomrade, name="Adressenavn_adresseomrade_ref", curie=NGR.curie('harAdresseomrade'),
                   model_uri=DEFAULT_.Adressenavn_adresseomrade_ref, domain=Adressenavn, range=Union[str, AdresseomradeId])

slots.Adressenavn_har_adressekode = Slot(uri=NGR.harAdressekode, name="Adressenavn_har_adressekode", curie=NGR.curie('harAdressekode'),
                   model_uri=DEFAULT_.Adressenavn_har_adressekode, domain=Adressenavn, range=Union[str, AdressekodeId])

slots.Adressekode_kode = Slot(uri=NGR.kode, name="Adressekode_kode", curie=NGR.curie('kode'),
                   model_uri=DEFAULT_.Adressekode_kode, domain=Adressekode, range=int)

slots.Husnummer_nummer = Slot(uri=NGR.nummer, name="Husnummer_nummer", curie=NGR.curie('nummer'),
                   model_uri=DEFAULT_.Husnummer_nummer, domain=Husnummer, range=int)

slots.Husnummer_bokstav = Slot(uri=NGR.bokstav, name="Husnummer_bokstav", curie=NGR.curie('bokstav'),
                   model_uri=DEFAULT_.Husnummer_bokstav, domain=Husnummer, range=Optional[str])

slots.Bruksenhetsnummer_etasjeplan = Slot(uri=NGR.etasjeplan, name="Bruksenhetsnummer_etasjeplan", curie=NGR.curie('etasjeplan'),
                   model_uri=DEFAULT_.Bruksenhetsnummer_etasjeplan, domain=Bruksenhetsnummer, range=Union[str, "Etasjeplan"])

slots.Bruksenhetsnummer_etasjenummer = Slot(uri=NGR.etasjenummer, name="Bruksenhetsnummer_etasjenummer", curie=NGR.curie('etasjenummer'),
                   model_uri=DEFAULT_.Bruksenhetsnummer_etasjenummer, domain=Bruksenhetsnummer, range=int)

slots.Bruksenhetsnummer_nummerering_i_etasjen = Slot(uri=NGR.nummereringIEtasjen, name="Bruksenhetsnummer_nummerering_i_etasjen", curie=NGR.curie('nummereringIEtasjen'),
                   model_uri=DEFAULT_.Bruksenhetsnummer_nummerering_i_etasjen, domain=Bruksenhetsnummer, range=int)

slots.Representasjonspunkt_koordinat_ost = Slot(uri=NGR.koordinatOst, name="Representasjonspunkt_koordinat_ost", curie=NGR.curie('koordinatOst'),
                   model_uri=DEFAULT_.Representasjonspunkt_koordinat_ost, domain=Representasjonspunkt, range=float)

slots.Representasjonspunkt_koordinat_nord = Slot(uri=NGR.koordinatNord, name="Representasjonspunkt_koordinat_nord", curie=NGR.curie('koordinatNord'),
                   model_uri=DEFAULT_.Representasjonspunkt_koordinat_nord, domain=Representasjonspunkt, range=float)

slots.Representasjonspunkt_koordinatsystem = Slot(uri=NGR.koordinatsystem, name="Representasjonspunkt_koordinatsystem", curie=NGR.curie('koordinatsystem'),
                   model_uri=DEFAULT_.Representasjonspunkt_koordinatsystem, domain=Representasjonspunkt, range=Optional[str])

slots.Fylke_fylkesnummer = Slot(uri=NGR.fylkesnummer, name="Fylke_fylkesnummer", curie=NGR.curie('fylkesnummer'),
                   model_uri=DEFAULT_.Fylke_fylkesnummer, domain=Fylke, range=str)

slots.Kommune_kommunenummer_kode = Slot(uri=NGR.kommunenummer, name="Kommune_kommunenummer_kode", curie=NGR.curie('kommunenummer'),
                   model_uri=DEFAULT_.Kommune_kommunenummer_kode, domain=Kommune, range=str)

slots.Poststed_postnummer = Slot(uri=LOCN.postCode, name="Poststed_postnummer", curie=LOCN.curie('postCode'),
                   model_uri=DEFAULT_.Poststed_postnummer, domain=Poststed, range=str)

slots.Postboks_postboksnummer = Slot(uri=NGR.postboksnummer, name="Postboks_postboksnummer", curie=NGR.curie('postboksnummer'),
                   model_uri=DEFAULT_.Postboks_postboksnummer, domain=Postboks, range=int)

