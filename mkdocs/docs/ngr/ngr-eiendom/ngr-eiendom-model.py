# Auto generated from ngr-eiendom-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-18T09:10:49
# Schema: ngr-eiendom
#
# id: https://data.norge.no/linkml/ngr-eiendom
# description: Domenemodell for norske eigedomsdata basert på Nasjonale grunndata (utkast). Modellerer Fast eiendom, Borettslagsandel, Matrikkelenhet, Bygning, Eierforhold og tilknytta klasser. Basert på https://informasjonsforvaltning.github.io/nasjonale-grunndata/
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

metamodel_version = "1.7.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NGRE = CurieNamespace('ngre', 'https://data.norge.no/vocabulary/ngr-eiendom#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://data.norge.no/linkml/ngr-eiendom/')


# Types

# Class references
class FastEiendomId(URIorCURIE):
    pass


class SamletFastEiendomId(URIorCURIE):
    pass


class BorettslagsandelId(URIorCURIE):
    pass


class MatrikkelenhetId(URIorCURIE):
    pass


class GrunneiendomId(MatrikkelenhetId):
    pass


class FestegrunnId(MatrikkelenhetId):
    pass


class JordsameieId(MatrikkelenhetId):
    pass


class EierseksjonId(MatrikkelenhetId):
    pass


class AnleggseiendomId(MatrikkelenhetId):
    pass


class AnnenMatrikkelenhetId(MatrikkelenhetId):
    pass


class MatrikkelnummerId(URIorCURIE):
    pass


class KommunenummerId(URIorCURIE):
    pass


class GaardsnummerId(URIorCURIE):
    pass


class BruksnummerId(URIorCURIE):
    pass


class FestenummerId(URIorCURIE):
    pass


class SeksjonsnummerId(URIorCURIE):
    pass


class BygningId(URIorCURIE):
    pass


class BygningsnummerId(URIorCURIE):
    pass


class RepresentasjonspunktId(URIorCURIE):
    pass


class YtreInngangId(URIorCURIE):
    pass


class BruksenhetId(URIorCURIE):
    pass


class BruksenhetsnummerId(URIorCURIE):
    pass


class EtasjeId(URIorCURIE):
    pass


class TeigId(URIorCURIE):
    pass


class AnleggsprojeksjonsflateId(URIorCURIE):
    pass


class EierforholdId(URIorCURIE):
    pass


class TinglystEierforholdId(EierforholdId):
    pass


class IkkeTinglystEierforholdId(EierforholdId):
    pass


class HjemmelId(URIorCURIE):
    pass


class HjemmelTilEiendomsrettId(HjemmelId):
    pass


class HjemmelTilFesterettId(HjemmelId):
    pass


class HjemmelTilFramfesterettId(HjemmelId):
    pass


class AndelId(URIorCURIE):
    pass


class RettighetshaverId(URIorCURIE):
    pass


class TinglystHeftelseId(URIorCURIE):
    pass


class RettighetForAaBenytteEiendomId(URIorCURIE):
    pass


class BorettslagId(URIorCURIE):
    pass


class OffisiellAdresseId(URIorCURIE):
    pass


class PersonId(URIorCURIE):
    pass


class HovedenhetId(URIorCURIE):
    pass


class KommuneId(URIorCURIE):
    pass


@dataclass(repr=False)
class EiendomContainer(YAMLRoot):
    """
    Rotklasse for NGR-eiendom-datafiler. Held flate lister av alle instansierbare klassar; referansar mellom objekt
    brukar URI-lenking.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/EiendomContainer")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EiendomContainer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/EiendomContainer")

    fasteEiendommer: Optional[Union[dict[Union[str, FastEiendomId], Union[dict, "FastEiendom"]], list[Union[dict, "FastEiendom"]]]] = empty_dict()
    samlinger: Optional[Union[dict[Union[str, SamletFastEiendomId], Union[dict, "SamletFastEiendom"]], list[Union[dict, "SamletFastEiendom"]]]] = empty_dict()
    borettslagsandeler: Optional[Union[dict[Union[str, BorettslagsandelId], Union[dict, "Borettslagsandel"]], list[Union[dict, "Borettslagsandel"]]]] = empty_dict()
    grunneiendommer: Optional[Union[dict[Union[str, GrunneiendomId], Union[dict, "Grunneiendom"]], list[Union[dict, "Grunneiendom"]]]] = empty_dict()
    festegrunn: Optional[Union[dict[Union[str, FestegrunnId], Union[dict, "Festegrunn"]], list[Union[dict, "Festegrunn"]]]] = empty_dict()
    jordsameier: Optional[Union[dict[Union[str, JordsameieId], Union[dict, "Jordsameie"]], list[Union[dict, "Jordsameie"]]]] = empty_dict()
    eierseksjoner: Optional[Union[dict[Union[str, EierseksjonId], Union[dict, "Eierseksjon"]], list[Union[dict, "Eierseksjon"]]]] = empty_dict()
    anleggseiendommer: Optional[Union[dict[Union[str, AnleggseiendomId], Union[dict, "Anleggseiendom"]], list[Union[dict, "Anleggseiendom"]]]] = empty_dict()
    andreMatrikkelenheter: Optional[Union[dict[Union[str, AnnenMatrikkelenhetId], Union[dict, "AnnenMatrikkelenhet"]], list[Union[dict, "AnnenMatrikkelenhet"]]]] = empty_dict()
    matrikkelnumre: Optional[Union[dict[Union[str, MatrikkelnummerId], Union[dict, "Matrikkelnummer"]], list[Union[dict, "Matrikkelnummer"]]]] = empty_dict()
    bygninger: Optional[Union[dict[Union[str, BygningId], Union[dict, "Bygning"]], list[Union[dict, "Bygning"]]]] = empty_dict()
    ytreInnganger: Optional[Union[dict[Union[str, YtreInngangId], Union[dict, "YtreInngang"]], list[Union[dict, "YtreInngang"]]]] = empty_dict()
    bruksenheter: Optional[Union[dict[Union[str, BruksenhetId], Union[dict, "Bruksenhet"]], list[Union[dict, "Bruksenhet"]]]] = empty_dict()
    etasjer: Optional[Union[dict[Union[str, EtasjeId], Union[dict, "Etasje"]], list[Union[dict, "Etasje"]]]] = empty_dict()
    teiger: Optional[Union[list[Union[str, TeigId]], dict[Union[str, TeigId], Union[dict, "Teig"]]]] = empty_dict()
    tinglystEierforhold: Optional[Union[dict[Union[str, TinglystEierforholdId], Union[dict, "TinglystEierforhold"]], list[Union[dict, "TinglystEierforhold"]]]] = empty_dict()
    ikkeTinglystEierforhold: Optional[Union[dict[Union[str, IkkeTinglystEierforholdId], Union[dict, "IkkeTinglystEierforhold"]], list[Union[dict, "IkkeTinglystEierforhold"]]]] = empty_dict()
    hjemmelEiendomsrett: Optional[Union[dict[Union[str, HjemmelTilEiendomsrettId], Union[dict, "HjemmelTilEiendomsrett"]], list[Union[dict, "HjemmelTilEiendomsrett"]]]] = empty_dict()
    hjemmelFesterett: Optional[Union[dict[Union[str, HjemmelTilFesterettId], Union[dict, "HjemmelTilFesterett"]], list[Union[dict, "HjemmelTilFesterett"]]]] = empty_dict()
    hjemmelFramfesterett: Optional[Union[dict[Union[str, HjemmelTilFramfesterettId], Union[dict, "HjemmelTilFramfesterett"]], list[Union[dict, "HjemmelTilFramfesterett"]]]] = empty_dict()
    andeler: Optional[Union[dict[Union[str, AndelId], Union[dict, "Andel"]], list[Union[dict, "Andel"]]]] = empty_dict()
    rettighetshavere: Optional[Union[dict[Union[str, RettighetshaverId], Union[dict, "Rettighetshaver"]], list[Union[dict, "Rettighetshaver"]]]] = empty_dict()
    tinglystHeftelser: Optional[Union[list[Union[str, TinglystHeftelseId]], dict[Union[str, TinglystHeftelseId], Union[dict, "TinglystHeftelse"]]]] = empty_dict()
    rettigheter: Optional[Union[list[Union[str, RettighetForAaBenytteEiendomId]], dict[Union[str, RettighetForAaBenytteEiendomId], Union[dict, "RettighetForAaBenytteEiendom"]]]] = empty_dict()
    borettslag: Optional[Union[dict[Union[str, BorettslagId], Union[dict, "Borettslag"]], list[Union[dict, "Borettslag"]]]] = empty_dict()
    representasjonspunkt: Optional[Union[dict[Union[str, RepresentasjonspunktId], Union[dict, "Representasjonspunkt"]], list[Union[dict, "Representasjonspunkt"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fasteEiendommer", slot_type=FastEiendom, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="samlinger", slot_type=SamletFastEiendom, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="borettslagsandeler", slot_type=Borettslagsandel, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="grunneiendommer", slot_type=Grunneiendom, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="festegrunn", slot_type=Festegrunn, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="jordsameier", slot_type=Jordsameie, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="eierseksjoner", slot_type=Eierseksjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="anleggseiendommer", slot_type=Anleggseiendom, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="andreMatrikkelenheter", slot_type=AnnenMatrikkelenhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="matrikkelnumre", slot_type=Matrikkelnummer, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="bygninger", slot_type=Bygning, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ytreInnganger", slot_type=YtreInngang, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="bruksenheter", slot_type=Bruksenhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="etasjer", slot_type=Etasje, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="teiger", slot_type=Teig, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tinglystEierforhold", slot_type=TinglystEierforhold, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ikkeTinglystEierforhold", slot_type=IkkeTinglystEierforhold, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="hjemmelEiendomsrett", slot_type=HjemmelTilEiendomsrett, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="hjemmelFesterett", slot_type=HjemmelTilFesterett, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="hjemmelFramfesterett", slot_type=HjemmelTilFramfesterett, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="andeler", slot_type=Andel, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rettighetshavere", slot_type=Rettighetshaver, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tinglystHeftelser", slot_type=TinglystHeftelse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rettigheter", slot_type=RettighetForAaBenytteEiendom, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="borettslag", slot_type=Borettslag, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="representasjonspunkt", slot_type=Representasjonspunkt, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FastEiendom(YAMLRoot):
    """
    Fast eiendom er eit grunnomgrep i eigedomsdomenet. Identifiserast av og består av éi matrikkelenheit, og kan
    innehalde bygningar og rettar som er nødvendige for å benytte eigedommen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["FastEiendom"]
    class_class_curie: ClassVar[str] = "ngre:FastEiendom"
    class_name: ClassVar[str] = "FastEiendom"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/FastEiendom")

    id: Union[str, FastEiendomId] = None
    identifiseres_av: Union[str, MatrikkelenhetId] = None
    bestar_av_matrikkelenhet: Union[str, MatrikkelenhetId] = None
    bestar_av_bygning: Optional[Union[Union[str, BygningId], list[Union[str, BygningId]]]] = empty_list()
    bestar_av_rettighet: Optional[Union[Union[str, RettighetForAaBenytteEiendomId], list[Union[str, RettighetForAaBenytteEiendomId]]]] = empty_list()
    har_eierforhold: Optional[Union[Union[str, EierforholdId], list[Union[str, EierforholdId]]]] = empty_list()
    har_tinglyst_heftelse: Optional[Union[Union[str, TinglystHeftelseId], list[Union[str, TinglystHeftelseId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FastEiendomId):
            self.id = FastEiendomId(self.id)

        if self._is_empty(self.identifiseres_av):
            self.MissingRequiredField("identifiseres_av")
        if not isinstance(self.identifiseres_av, MatrikkelenhetId):
            self.identifiseres_av = MatrikkelenhetId(self.identifiseres_av)

        if self._is_empty(self.bestar_av_matrikkelenhet):
            self.MissingRequiredField("bestar_av_matrikkelenhet")
        if not isinstance(self.bestar_av_matrikkelenhet, MatrikkelenhetId):
            self.bestar_av_matrikkelenhet = MatrikkelenhetId(self.bestar_av_matrikkelenhet)

        if not isinstance(self.bestar_av_bygning, list):
            self.bestar_av_bygning = [self.bestar_av_bygning] if self.bestar_av_bygning is not None else []
        self.bestar_av_bygning = [v if isinstance(v, BygningId) else BygningId(v) for v in self.bestar_av_bygning]

        if not isinstance(self.bestar_av_rettighet, list):
            self.bestar_av_rettighet = [self.bestar_av_rettighet] if self.bestar_av_rettighet is not None else []
        self.bestar_av_rettighet = [v if isinstance(v, RettighetForAaBenytteEiendomId) else RettighetForAaBenytteEiendomId(v) for v in self.bestar_av_rettighet]

        if not isinstance(self.har_eierforhold, list):
            self.har_eierforhold = [self.har_eierforhold] if self.har_eierforhold is not None else []
        self.har_eierforhold = [v if isinstance(v, EierforholdId) else EierforholdId(v) for v in self.har_eierforhold]

        if not isinstance(self.har_tinglyst_heftelse, list):
            self.har_tinglyst_heftelse = [self.har_tinglyst_heftelse] if self.har_tinglyst_heftelse is not None else []
        self.har_tinglyst_heftelse = [v if isinstance(v, TinglystHeftelseId) else TinglystHeftelseId(v) for v in self.har_tinglyst_heftelse]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SamletFastEiendom(YAMLRoot):
    """
    Samling av to eller fleire faste eigedommar som er organiserte saman. Lite brukt i praksis i dag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["SamletFastEiendom"]
    class_class_curie: ClassVar[str] = "ngre:SamletFastEiendom"
    class_name: ClassVar[str] = "SamletFastEiendom"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/SamletFastEiendom")

    id: Union[str, SamletFastEiendomId] = None
    bestar_av_fast_eiendom: Union[Union[str, FastEiendomId], list[Union[str, FastEiendomId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SamletFastEiendomId):
            self.id = SamletFastEiendomId(self.id)

        if self._is_empty(self.bestar_av_fast_eiendom):
            self.MissingRequiredField("bestar_av_fast_eiendom")
        if not isinstance(self.bestar_av_fast_eiendom, list):
            self.bestar_av_fast_eiendom = [self.bestar_av_fast_eiendom] if self.bestar_av_fast_eiendom is not None else []
        self.bestar_av_fast_eiendom = [v if isinstance(v, FastEiendomId) else FastEiendomId(v) for v in self.bestar_av_fast_eiendom]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Borettslagsandel(YAMLRoot):
    """
    Ein andel i eit burettslag som gir eksklusiv bruksrett til ein bestemt bustad i burettslagsbygningen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Borettslagsandel"]
    class_class_curie: ClassVar[str] = "ngre:Borettslagsandel"
    class_name: ClassVar[str] = "Borettslagsandel"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Borettslagsandel")

    id: Union[str, BorettslagsandelId] = None
    tilhoerer_borettslag: Union[str, BorettslagId] = None
    har_eierforhold: Optional[Union[Union[str, EierforholdId], list[Union[str, EierforholdId]]]] = empty_list()
    har_tinglyst_heftelse: Optional[Union[Union[str, TinglystHeftelseId], list[Union[str, TinglystHeftelseId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BorettslagsandelId):
            self.id = BorettslagsandelId(self.id)

        if self._is_empty(self.tilhoerer_borettslag):
            self.MissingRequiredField("tilhoerer_borettslag")
        if not isinstance(self.tilhoerer_borettslag, BorettslagId):
            self.tilhoerer_borettslag = BorettslagId(self.tilhoerer_borettslag)

        if not isinstance(self.har_eierforhold, list):
            self.har_eierforhold = [self.har_eierforhold] if self.har_eierforhold is not None else []
        self.har_eierforhold = [v if isinstance(v, EierforholdId) else EierforholdId(v) for v in self.har_eierforhold]

        if not isinstance(self.har_tinglyst_heftelse, list):
            self.har_tinglyst_heftelse = [self.har_tinglyst_heftelse] if self.har_tinglyst_heftelse is not None else []
        self.har_tinglyst_heftelse = [v if isinstance(v, TinglystHeftelseId) else TinglystHeftelseId(v) for v in self.har_tinglyst_heftelse]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Matrikkelenhet(YAMLRoot):
    """
    Abstrakt overklasse for alle typar matrikkeleiningar registrert i Matrikkelen. Ei matrikkelenheit er den
    grunnleggjande eininga for registrering av fast eigedom i Noreg.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Matrikkelenhet"]
    class_class_curie: ClassVar[str] = "ngre:Matrikkelenhet"
    class_name: ClassVar[str] = "Matrikkelenhet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Matrikkelenhet")

    id: Union[str, MatrikkelenhetId] = None
    identifiseres_med: Union[str, MatrikkelnummerId] = None
    ligger_innenfor_kommune: Union[str, KommuneId] = None
    er_del_av_teig: Optional[Union[Union[str, TeigId], list[Union[str, TeigId]]]] = empty_list()
    har_teig: Optional[Union[Union[str, TeigId], list[Union[str, TeigId]]]] = empty_list()
    har_anleggsprojeksjonsflate: Optional[Union[str, AnleggsprojeksjonsflateId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MatrikkelenhetId):
            self.id = MatrikkelenhetId(self.id)

        if self._is_empty(self.identifiseres_med):
            self.MissingRequiredField("identifiseres_med")
        if not isinstance(self.identifiseres_med, MatrikkelnummerId):
            self.identifiseres_med = MatrikkelnummerId(self.identifiseres_med)

        if self._is_empty(self.ligger_innenfor_kommune):
            self.MissingRequiredField("ligger_innenfor_kommune")
        if not isinstance(self.ligger_innenfor_kommune, KommuneId):
            self.ligger_innenfor_kommune = KommuneId(self.ligger_innenfor_kommune)

        if not isinstance(self.er_del_av_teig, list):
            self.er_del_av_teig = [self.er_del_av_teig] if self.er_del_av_teig is not None else []
        self.er_del_av_teig = [v if isinstance(v, TeigId) else TeigId(v) for v in self.er_del_av_teig]

        if not isinstance(self.har_teig, list):
            self.har_teig = [self.har_teig] if self.har_teig is not None else []
        self.har_teig = [v if isinstance(v, TeigId) else TeigId(v) for v in self.har_teig]

        if self.har_anleggsprojeksjonsflate is not None and not isinstance(self.har_anleggsprojeksjonsflate, AnleggsprojeksjonsflateId):
            self.har_anleggsprojeksjonsflate = AnleggsprojeksjonsflateId(self.har_anleggsprojeksjonsflate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Grunneiendom(Matrikkelenhet):
    """
    Den vanlegaste typen matrikkelenheit. Eit avgrensa areal av jord- eller vassoverflate (eventuelt med undergrunn og
    luftrom) innanfor ein kommune.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Grunneiendom"]
    class_class_curie: ClassVar[str] = "ngre:Grunneiendom"
    class_name: ClassVar[str] = "Grunneiendom"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Grunneiendom")

    id: Union[str, GrunneiendomId] = None
    identifiseres_med: Union[str, MatrikkelnummerId] = None
    ligger_innenfor_kommune: Union[str, KommuneId] = None
    kan_vaere_pa: Optional[Union[str, MatrikkelenhetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GrunneiendomId):
            self.id = GrunneiendomId(self.id)

        if self.kan_vaere_pa is not None and not isinstance(self.kan_vaere_pa, MatrikkelenhetId):
            self.kan_vaere_pa = MatrikkelenhetId(self.kan_vaere_pa)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Festegrunn(Matrikkelenhet):
    """
    Ein del av ei grunneigendom eller eit jordsameige som nokon har festa til. Ein festekontrakt gir eksklusiv og
    langvarig bruksrett til festegrunnen. Kan vere eit bestemt areal eller eit punktfeste.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Festegrunn"]
    class_class_curie: ClassVar[str] = "ngre:Festegrunn"
    class_name: ClassVar[str] = "Festegrunn"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Festegrunn")

    id: Union[str, FestegrunnId] = None
    identifiseres_med: Union[str, MatrikkelnummerId] = None
    ligger_innenfor_kommune: Union[str, KommuneId] = None
    kan_vaere_pa: Optional[Union[str, MatrikkelenhetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FestegrunnId):
            self.id = FestegrunnId(self.id)

        if self.kan_vaere_pa is not None and not isinstance(self.kan_vaere_pa, MatrikkelenhetId):
            self.kan_vaere_pa = MatrikkelenhetId(self.kan_vaere_pa)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Jordsameie(Matrikkelenhet):
    """
    Eit fellesareal som vert eigd av fleire eigedommar. Jordsameige er ein type realsameige. Eit umatrikulert
    jordsameige er eit eksisterande sameige som ikkje er registrert som eigen matrikkelenheit.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Jordsameie"]
    class_class_curie: ClassVar[str] = "ngre:Jordsameie"
    class_name: ClassVar[str] = "Jordsameie"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Jordsameie")

    id: Union[str, JordsameieId] = None
    identifiseres_med: Union[str, MatrikkelnummerId] = None
    ligger_innenfor_kommune: Union[str, KommuneId] = None
    kan_vaere_pa: Optional[Union[str, MatrikkelenhetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JordsameieId):
            self.id = JordsameieId(self.id)

        if self.kan_vaere_pa is not None and not isinstance(self.kan_vaere_pa, MatrikkelenhetId):
            self.kan_vaere_pa = MatrikkelenhetId(self.kan_vaere_pa)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Eierseksjon(Matrikkelenhet):
    """
    Ein eigarseksjon er ein eigarandel i ein seksjonert eigedom. Eigaren har einerett til å bruke ein bestemt del av
    eigedommen, medan heile eigedommen er i sameige med dei andre seksjonseigarane. Eigedommen som er seksjonert kan
    vere grunneigendom, festegrunn eller anleggseigendom.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Eierseksjon"]
    class_class_curie: ClassVar[str] = "ngre:Eierseksjon"
    class_name: ClassVar[str] = "Eierseksjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Eierseksjon")

    id: Union[str, EierseksjonId] = None
    identifiseres_med: Union[str, MatrikkelnummerId] = None
    ligger_innenfor_kommune: Union[str, KommuneId] = None
    kan_vaere_pa: Optional[Union[str, MatrikkelenhetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EierseksjonId):
            self.id = EierseksjonId(self.id)

        if self.kan_vaere_pa is not None and not isinstance(self.kan_vaere_pa, MatrikkelenhetId):
            self.kan_vaere_pa = MatrikkelenhetId(self.kan_vaere_pa)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Anleggseiendom(Matrikkelenhet):
    """
    Eit volum – ein bygning eller konstruksjon – oppretta frå ei eller fleire grunneigedommar eller anleggseigedommar.
    Strekkjer seg over og/eller under andre matrikkeleiningar. Kan også opprettast ved okkupasjon frå eierløs
    undergrunn eller sjøgrunn.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Anleggseiendom"]
    class_class_curie: ClassVar[str] = "ngre:Anleggseiendom"
    class_name: ClassVar[str] = "Anleggseiendom"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Anleggseiendom")

    id: Union[str, AnleggseiendomId] = None
    identifiseres_med: Union[str, MatrikkelnummerId] = None
    ligger_innenfor_kommune: Union[str, KommuneId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnleggseiendomId):
            self.id = AnleggseiendomId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnnenMatrikkelenhet(Matrikkelenhet):
    """
    Matrikkelenheit som ikkje fell inn under dei andre underklassane.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["AnnenMatrikkelenhet"]
    class_class_curie: ClassVar[str] = "ngre:AnnenMatrikkelenhet"
    class_name: ClassVar[str] = "AnnenMatrikkelenhet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/AnnenMatrikkelenhet")

    id: Union[str, AnnenMatrikkelenhetId] = None
    identifiseres_med: Union[str, MatrikkelnummerId] = None
    ligger_innenfor_kommune: Union[str, KommuneId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnnenMatrikkelenhetId):
            self.id = AnnenMatrikkelenhetId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Matrikkelnummer(YAMLRoot):
    """
    Offisiell identifikator for ei matrikkelenheit, beståande av kommunenummer, gards-, bruks- og eventuelt feste- og
    seksjonsnummer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Matrikkelnummer"]
    class_class_curie: ClassVar[str] = "ngre:Matrikkelnummer"
    class_name: ClassVar[str] = "Matrikkelnummer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Matrikkelnummer")

    id: Union[str, MatrikkelnummerId] = None
    bestar_av_kommunenummer: Union[str, KommunenummerId] = None
    bestar_av_gaardsnummer: Union[str, GaardsnummerId] = None
    bestar_av_bruksnummer: Union[str, BruksnummerId] = None
    bestar_av_festenummer: Optional[Union[str, FestenummerId]] = None
    bestar_av_seksjonsnummer: Optional[Union[str, SeksjonsnummerId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MatrikkelnummerId):
            self.id = MatrikkelnummerId(self.id)

        if self._is_empty(self.bestar_av_kommunenummer):
            self.MissingRequiredField("bestar_av_kommunenummer")
        if not isinstance(self.bestar_av_kommunenummer, KommunenummerId):
            self.bestar_av_kommunenummer = KommunenummerId(self.bestar_av_kommunenummer)

        if self._is_empty(self.bestar_av_gaardsnummer):
            self.MissingRequiredField("bestar_av_gaardsnummer")
        if not isinstance(self.bestar_av_gaardsnummer, GaardsnummerId):
            self.bestar_av_gaardsnummer = GaardsnummerId(self.bestar_av_gaardsnummer)

        if self._is_empty(self.bestar_av_bruksnummer):
            self.MissingRequiredField("bestar_av_bruksnummer")
        if not isinstance(self.bestar_av_bruksnummer, BruksnummerId):
            self.bestar_av_bruksnummer = BruksnummerId(self.bestar_av_bruksnummer)

        if self.bestar_av_festenummer is not None and not isinstance(self.bestar_av_festenummer, FestenummerId):
            self.bestar_av_festenummer = FestenummerId(self.bestar_av_festenummer)

        if self.bestar_av_seksjonsnummer is not None and not isinstance(self.bestar_av_seksjonsnummer, SeksjonsnummerId):
            self.bestar_av_seksjonsnummer = SeksjonsnummerId(self.bestar_av_seksjonsnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kommunenummer(YAMLRoot):
    """
    Firesifra kommunenummer (t.d. 0301 for Oslo).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Kommunenummer"]
    class_class_curie: ClassVar[str] = "ngre:Kommunenummer"
    class_name: ClassVar[str] = "Kommunenummer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Kommunenummer")

    id: Union[str, KommunenummerId] = None
    kommunenummer_verdi: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KommunenummerId):
            self.id = KommunenummerId(self.id)

        if self._is_empty(self.kommunenummer_verdi):
            self.MissingRequiredField("kommunenummer_verdi")
        if not isinstance(self.kommunenummer_verdi, str):
            self.kommunenummer_verdi = str(self.kommunenummer_verdi)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Gaardsnummer(YAMLRoot):
    """
    Gårdsnummer innanfor kommunen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Gaardsnummer"]
    class_class_curie: ClassVar[str] = "ngre:Gaardsnummer"
    class_name: ClassVar[str] = "Gaardsnummer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Gaardsnummer")

    id: Union[str, GaardsnummerId] = None
    gaardsnummer_verdi: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GaardsnummerId):
            self.id = GaardsnummerId(self.id)

        if self._is_empty(self.gaardsnummer_verdi):
            self.MissingRequiredField("gaardsnummer_verdi")
        if not isinstance(self.gaardsnummer_verdi, int):
            self.gaardsnummer_verdi = int(self.gaardsnummer_verdi)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bruksnummer(YAMLRoot):
    """
    Bruksnummer innanfor gardsnamnet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Bruksnummer"]
    class_class_curie: ClassVar[str] = "ngre:Bruksnummer"
    class_name: ClassVar[str] = "Bruksnummer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Bruksnummer")

    id: Union[str, BruksnummerId] = None
    bruksnummer_verdi: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BruksnummerId):
            self.id = BruksnummerId(self.id)

        if self._is_empty(self.bruksnummer_verdi):
            self.MissingRequiredField("bruksnummer_verdi")
        if not isinstance(self.bruksnummer_verdi, int):
            self.bruksnummer_verdi = int(self.bruksnummer_verdi)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Festenummer(YAMLRoot):
    """
    Festenummer, aktuelt berre for festegrunn (0..1 i matrikkelnummeret).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Festenummer"]
    class_class_curie: ClassVar[str] = "ngre:Festenummer"
    class_name: ClassVar[str] = "Festenummer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Festenummer")

    id: Union[str, FestenummerId] = None
    festenummer_verdi: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FestenummerId):
            self.id = FestenummerId(self.id)

        if self._is_empty(self.festenummer_verdi):
            self.MissingRequiredField("festenummer_verdi")
        if not isinstance(self.festenummer_verdi, int):
            self.festenummer_verdi = int(self.festenummer_verdi)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Seksjonsnummer(YAMLRoot):
    """
    Seksjonsnummer, aktuelt berre for eigarseksjonar (0..1 i matrikkelnummeret).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Seksjonsnummer"]
    class_class_curie: ClassVar[str] = "ngre:Seksjonsnummer"
    class_name: ClassVar[str] = "Seksjonsnummer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Seksjonsnummer")

    id: Union[str, SeksjonsnummerId] = None
    seksjonsnummer_verdi: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SeksjonsnummerId):
            self.id = SeksjonsnummerId(self.id)

        if self._is_empty(self.seksjonsnummer_verdi):
            self.MissingRequiredField("seksjonsnummer_verdi")
        if not isinstance(self.seksjonsnummer_verdi, int):
            self.seksjonsnummer_verdi = int(self.seksjonsnummer_verdi)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bygning(YAMLRoot):
    """
    Ein bygning registrert i Matrikkelen. Knytt til éi matrikkelenheit og kan ha fleire ytre innganger, brukseiningar
    og etasjar. Bygningsinformasjon er i dag spreidd i fleire databasar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Bygning"]
    class_class_curie: ClassVar[str] = "ngre:Bygning"
    class_name: ClassVar[str] = "Bygning"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Bygning")

    id: Union[str, BygningId] = None
    har_bygningsnummer: Union[str, BygningsnummerId] = None
    har_representasjonspunkt: Union[str, RepresentasjonspunktId] = None
    er_knyttet_til_matrikkelenhet: Union[str, MatrikkelenhetId] = None
    har_ytre_inngang: Optional[Union[Union[str, YtreInngangId], list[Union[str, YtreInngangId]]]] = empty_list()
    har_bruksenhet: Optional[Union[Union[str, BruksenhetId], list[Union[str, BruksenhetId]]]] = empty_list()
    har_etasje: Optional[Union[Union[str, EtasjeId], list[Union[str, EtasjeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BygningId):
            self.id = BygningId(self.id)

        if self._is_empty(self.har_bygningsnummer):
            self.MissingRequiredField("har_bygningsnummer")
        if not isinstance(self.har_bygningsnummer, BygningsnummerId):
            self.har_bygningsnummer = BygningsnummerId(self.har_bygningsnummer)

        if self._is_empty(self.har_representasjonspunkt):
            self.MissingRequiredField("har_representasjonspunkt")
        if not isinstance(self.har_representasjonspunkt, RepresentasjonspunktId):
            self.har_representasjonspunkt = RepresentasjonspunktId(self.har_representasjonspunkt)

        if self._is_empty(self.er_knyttet_til_matrikkelenhet):
            self.MissingRequiredField("er_knyttet_til_matrikkelenhet")
        if not isinstance(self.er_knyttet_til_matrikkelenhet, MatrikkelenhetId):
            self.er_knyttet_til_matrikkelenhet = MatrikkelenhetId(self.er_knyttet_til_matrikkelenhet)

        if not isinstance(self.har_ytre_inngang, list):
            self.har_ytre_inngang = [self.har_ytre_inngang] if self.har_ytre_inngang is not None else []
        self.har_ytre_inngang = [v if isinstance(v, YtreInngangId) else YtreInngangId(v) for v in self.har_ytre_inngang]

        if not isinstance(self.har_bruksenhet, list):
            self.har_bruksenhet = [self.har_bruksenhet] if self.har_bruksenhet is not None else []
        self.har_bruksenhet = [v if isinstance(v, BruksenhetId) else BruksenhetId(v) for v in self.har_bruksenhet]

        if not isinstance(self.har_etasje, list):
            self.har_etasje = [self.har_etasje] if self.har_etasje is not None else []
        self.har_etasje = [v if isinstance(v, EtasjeId) else EtasjeId(v) for v in self.har_etasje]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bygningsnummer(YAMLRoot):
    """
    Offisiell identifikator for ein bygning i Matrikkelen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Bygningsnummer"]
    class_class_curie: ClassVar[str] = "ngre:Bygningsnummer"
    class_name: ClassVar[str] = "Bygningsnummer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Bygningsnummer")

    id: Union[str, BygningsnummerId] = None
    bygningsnummer_verdi: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BygningsnummerId):
            self.id = BygningsnummerId(self.id)

        if self._is_empty(self.bygningsnummer_verdi):
            self.MissingRequiredField("bygningsnummer_verdi")
        if not isinstance(self.bygningsnummer_verdi, int):
            self.bygningsnummer_verdi = int(self.bygningsnummer_verdi)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Representasjonspunkt(YAMLRoot):
    """
    Geografisk punkt (koordinatpar) som representerer posisjonen til bygningen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Representasjonspunkt"]
    class_class_curie: ClassVar[str] = "ngre:Representasjonspunkt"
    class_name: ClassVar[str] = "Representasjonspunkt"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Representasjonspunkt")

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
class YtreInngang(YAMLRoot):
    """
    Ytre inngang til ein bygning. Registrerast ikkje som eige objekt i Matrikkelen, men adressepunktet refererer til
    ytre inngang. Gir tilgang til éi eller fleire brukseiningar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["YtreInngang"]
    class_class_curie: ClassVar[str] = "ngre:YtreInngang"
    class_name: ClassVar[str] = "YtreInngang"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/YtreInngang")

    id: Union[str, YtreInngangId] = None
    gjelder_bruksenhet: Union[Union[str, BruksenhetId], list[Union[str, BruksenhetId]]] = None
    har_offisiell_adresse: Optional[Union[str, OffisiellAdresseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, YtreInngangId):
            self.id = YtreInngangId(self.id)

        if self._is_empty(self.gjelder_bruksenhet):
            self.MissingRequiredField("gjelder_bruksenhet")
        if not isinstance(self.gjelder_bruksenhet, list):
            self.gjelder_bruksenhet = [self.gjelder_bruksenhet] if self.gjelder_bruksenhet is not None else []
        self.gjelder_bruksenhet = [v if isinstance(v, BruksenhetId) else BruksenhetId(v) for v in self.gjelder_bruksenhet]

        if self.har_offisiell_adresse is not None and not isinstance(self.har_offisiell_adresse, OffisiellAdresseId):
            self.har_offisiell_adresse = OffisiellAdresseId(self.har_offisiell_adresse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bruksenhet(YAMLRoot):
    """
    Ei brukseining (leilegheit, kontor o.l.) innanfor ein bygning. Har eit bruksenheitsnummer, ligg i minst éi etasje
    og kan vere knytt til ei matrikkelenheit.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Bruksenhet"]
    class_class_curie: ClassVar[str] = "ngre:Bruksenhet"
    class_name: ClassVar[str] = "Bruksenhet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Bruksenhet")

    id: Union[str, BruksenhetId] = None
    har_bruksenhetsnummer: Union[str, BruksenhetsnummerId] = None
    ligger_i_etasje: Union[Union[str, EtasjeId], list[Union[str, EtasjeId]]] = None
    er_tilknyttet_matrikkelenhet: Optional[Union[str, MatrikkelenhetId]] = None
    har_offisiell_adresse: Optional[Union[str, OffisiellAdresseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BruksenhetId):
            self.id = BruksenhetId(self.id)

        if self._is_empty(self.har_bruksenhetsnummer):
            self.MissingRequiredField("har_bruksenhetsnummer")
        if not isinstance(self.har_bruksenhetsnummer, BruksenhetsnummerId):
            self.har_bruksenhetsnummer = BruksenhetsnummerId(self.har_bruksenhetsnummer)

        if self._is_empty(self.ligger_i_etasje):
            self.MissingRequiredField("ligger_i_etasje")
        if not isinstance(self.ligger_i_etasje, list):
            self.ligger_i_etasje = [self.ligger_i_etasje] if self.ligger_i_etasje is not None else []
        self.ligger_i_etasje = [v if isinstance(v, EtasjeId) else EtasjeId(v) for v in self.ligger_i_etasje]

        if self.er_tilknyttet_matrikkelenhet is not None and not isinstance(self.er_tilknyttet_matrikkelenhet, MatrikkelenhetId):
            self.er_tilknyttet_matrikkelenhet = MatrikkelenhetId(self.er_tilknyttet_matrikkelenhet)

        if self.har_offisiell_adresse is not None and not isinstance(self.har_offisiell_adresse, OffisiellAdresseId):
            self.har_offisiell_adresse = OffisiellAdresseId(self.har_offisiell_adresse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bruksenhetsnummer(YAMLRoot):
    """
    Identifikator for ei brukseining innanfor ein bygning, t.d. H0201 = 2. etasje, eining 1 (etasjeplan + etasjenummer
    + nummerering).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Bruksenhetsnummer"]
    class_class_curie: ClassVar[str] = "ngre:Bruksenhetsnummer"
    class_name: ClassVar[str] = "Bruksenhetsnummer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Bruksenhetsnummer")

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
class Etasje(YAMLRoot):
    """
    Ei etasje i ein bygning.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Etasje"]
    class_class_curie: ClassVar[str] = "ngre:Etasje"
    class_name: ClassVar[str] = "Etasje"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Etasje")

    id: Union[str, EtasjeId] = None
    etasjenummer: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EtasjeId):
            self.id = EtasjeId(self.id)

        if self._is_empty(self.etasjenummer):
            self.MissingRequiredField("etasjenummer")
        if not isinstance(self.etasjenummer, int):
            self.etasjenummer = int(self.etasjenummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Teig(YAMLRoot):
    """
    Eit samanhengande areal med same type grenser. Mangler ofte vannareal som høyrer til eigedommen. Grensene kan ha
    manglande eller dårleg nøyaktigheit.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Teig"]
    class_class_curie: ClassVar[str] = "ngre:Teig"
    class_name: ClassVar[str] = "Teig"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Teig")

    id: Union[str, TeigId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TeigId):
            self.id = TeigId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Anleggsprojeksjonsflate(YAMLRoot):
    """
    Fotavtrykk av 3D-eigedommar (anleggseigedommar). Manglar volumet og må supplerast på oppdrag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Anleggsprojeksjonsflate"]
    class_class_curie: ClassVar[str] = "ngre:Anleggsprojeksjonsflate"
    class_name: ClassVar[str] = "Anleggsprojeksjonsflate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Anleggsprojeksjonsflate")

    id: Union[str, AnleggsprojeksjonsflateId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnleggsprojeksjonsflateId):
            self.id = AnleggsprojeksjonsflateId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Eierforhold(YAMLRoot):
    """
    Abstrakt klasse for eigarforhold forvalta av Grunnboka. Eit eigarforhold gjeld éi matrikkelenheit og kan eventuelt
    gjelde ein burettslagsandel. Inneheld heimelsdokument som fastset kven som er eigar og på kva vilkår.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Eierforhold"]
    class_class_curie: ClassVar[str] = "ngre:Eierforhold"
    class_name: ClassVar[str] = "Eierforhold"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Eierforhold")

    id: Union[str, EierforholdId] = None
    gjelder_matrikkelenhet: Union[str, MatrikkelenhetId] = None
    kan_gjelde_borettslagsandel: Optional[Union[str, BorettslagsandelId]] = None
    gjelder_hjemmel_eiendomsrett: Optional[Union[str, HjemmelTilEiendomsrettId]] = None
    gjelder_hjemmel_festerett: Optional[Union[str, HjemmelTilFesterettId]] = None
    gjelder_hjemmel_framfesterett: Optional[Union[str, HjemmelTilFramfesterettId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EierforholdId):
            self.id = EierforholdId(self.id)

        if self._is_empty(self.gjelder_matrikkelenhet):
            self.MissingRequiredField("gjelder_matrikkelenhet")
        if not isinstance(self.gjelder_matrikkelenhet, MatrikkelenhetId):
            self.gjelder_matrikkelenhet = MatrikkelenhetId(self.gjelder_matrikkelenhet)

        if self.kan_gjelde_borettslagsandel is not None and not isinstance(self.kan_gjelde_borettslagsandel, BorettslagsandelId):
            self.kan_gjelde_borettslagsandel = BorettslagsandelId(self.kan_gjelde_borettslagsandel)

        if self.gjelder_hjemmel_eiendomsrett is not None and not isinstance(self.gjelder_hjemmel_eiendomsrett, HjemmelTilEiendomsrettId):
            self.gjelder_hjemmel_eiendomsrett = HjemmelTilEiendomsrettId(self.gjelder_hjemmel_eiendomsrett)

        if self.gjelder_hjemmel_festerett is not None and not isinstance(self.gjelder_hjemmel_festerett, HjemmelTilFesterettId):
            self.gjelder_hjemmel_festerett = HjemmelTilFesterettId(self.gjelder_hjemmel_festerett)

        if self.gjelder_hjemmel_framfesterett is not None and not isinstance(self.gjelder_hjemmel_framfesterett, HjemmelTilFramfesterettId):
            self.gjelder_hjemmel_framfesterett = HjemmelTilFramfesterettId(self.gjelder_hjemmel_framfesterett)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TinglystEierforhold(Eierforhold):
    """
    Eigarforhold registrert (tinglyst) i Grunnboka.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["TinglystEierforhold"]
    class_class_curie: ClassVar[str] = "ngre:TinglystEierforhold"
    class_name: ClassVar[str] = "TinglystEierforhold"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/TinglystEierforhold")

    id: Union[str, TinglystEierforholdId] = None
    gjelder_matrikkelenhet: Union[str, MatrikkelenhetId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TinglystEierforholdId):
            self.id = TinglystEierforholdId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IkkeTinglystEierforhold(Eierforhold):
    """
    Eigarforhold som ikkje er registrert i Grunnboka. Det kan finnast eigarforhold som ikkje samsvarer med det
    tinglyste eigarforholdet. Gjeld også bygningar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["IkkeTinglystEierforhold"]
    class_class_curie: ClassVar[str] = "ngre:IkkeTinglystEierforhold"
    class_name: ClassVar[str] = "IkkeTinglystEierforhold"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/IkkeTinglystEierforhold")

    id: Union[str, IkkeTinglystEierforholdId] = None
    gjelder_matrikkelenhet: Union[str, MatrikkelenhetId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IkkeTinglystEierforholdId):
            self.id = IkkeTinglystEierforholdId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Hjemmel(YAMLRoot):
    """
    Abstrakt klasse for heimelsdokument. Eit heimelsdokument fastset kven som har rett til eigedommen og i kva form,
    og består av ein eller fleire andeler med kvar sin rettigheitshavar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Hjemmel"]
    class_class_curie: ClassVar[str] = "ngre:Hjemmel"
    class_name: ClassVar[str] = "Hjemmel"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Hjemmel")

    id: Union[str, HjemmelId] = None
    har_andel: Union[Union[str, AndelId], list[Union[str, AndelId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HjemmelId):
            self.id = HjemmelId(self.id)

        if self._is_empty(self.har_andel):
            self.MissingRequiredField("har_andel")
        if not isinstance(self.har_andel, list):
            self.har_andel = [self.har_andel] if self.har_andel is not None else []
        self.har_andel = [v if isinstance(v, AndelId) else AndelId(v) for v in self.har_andel]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HjemmelTilEiendomsrett(Hjemmel):
    """
    Heimelsdokument for eigedomsrett (full eigarrett).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["HjemmelTilEiendomsrett"]
    class_class_curie: ClassVar[str] = "ngre:HjemmelTilEiendomsrett"
    class_name: ClassVar[str] = "HjemmelTilEiendomsrett"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/HjemmelTilEiendomsrett")

    id: Union[str, HjemmelTilEiendomsrettId] = None
    har_andel: Union[Union[str, AndelId], list[Union[str, AndelId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HjemmelTilEiendomsrettId):
            self.id = HjemmelTilEiendomsrettId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HjemmelTilFesterett(Hjemmel):
    """
    Heimelsdokument for festerett (langvarig bruksrett til festegrunn).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["HjemmelTilFesterett"]
    class_class_curie: ClassVar[str] = "ngre:HjemmelTilFesterett"
    class_name: ClassVar[str] = "HjemmelTilFesterett"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/HjemmelTilFesterett")

    id: Union[str, HjemmelTilFesterettId] = None
    har_andel: Union[Union[str, AndelId], list[Union[str, AndelId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HjemmelTilFesterettId):
            self.id = HjemmelTilFesterettId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HjemmelTilFramfesterett(Hjemmel):
    """
    Heimelsdokument for framfesterett (vidarefestekontrakt).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["HjemmelTilFramfesterett"]
    class_class_curie: ClassVar[str] = "ngre:HjemmelTilFramfesterett"
    class_name: ClassVar[str] = "HjemmelTilFramfesterett"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/HjemmelTilFramfesterett")

    id: Union[str, HjemmelTilFramfesterettId] = None
    har_andel: Union[Union[str, AndelId], list[Union[str, AndelId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HjemmelTilFramfesterettId):
            self.id = HjemmelTilFramfesterettId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Andel(YAMLRoot):
    """
    Ein eigarandel i eit heimelsdokument (også kalt eierandel). Kvar andel har ein eller fleire rettigheitshavarar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Andel"]
    class_class_curie: ClassVar[str] = "ngre:Andel"
    class_name: ClassVar[str] = "Andel"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Andel")

    id: Union[str, AndelId] = None
    har_rettighetshaver: Union[Union[str, RettighetshaverId], list[Union[str, RettighetshaverId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AndelId):
            self.id = AndelId(self.id)

        if self._is_empty(self.har_rettighetshaver):
            self.MissingRequiredField("har_rettighetshaver")
        if not isinstance(self.har_rettighetshaver, list):
            self.har_rettighetshaver = [self.har_rettighetshaver] if self.har_rettighetshaver is not None else []
        self.har_rettighetshaver = [v if isinstance(v, RettighetshaverId) else RettighetshaverId(v) for v in self.har_rettighetshaver]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rettighetshaver(YAMLRoot):
    """
    Den som har ein rett knytt til ein eigedom. Kan vere ein fysisk person eller ei hovudeining (juridisk person).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Rettighetshaver"]
    class_class_curie: ClassVar[str] = "ngre:Rettighetshaver"
    class_name: ClassVar[str] = "Rettighetshaver"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Rettighetshaver")

    id: Union[str, RettighetshaverId] = None
    er_av_type_person: Optional[Union[str, PersonId]] = None
    er_av_type_hovedenhet: Optional[Union[str, HovedenhetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RettighetshaverId):
            self.id = RettighetshaverId(self.id)

        if self.er_av_type_person is not None and not isinstance(self.er_av_type_person, PersonId):
            self.er_av_type_person = PersonId(self.er_av_type_person)

        if self.er_av_type_hovedenhet is not None and not isinstance(self.er_av_type_hovedenhet, HovedenhetId):
            self.er_av_type_hovedenhet = HovedenhetId(self.er_av_type_hovedenhet)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TinglystHeftelse(YAMLRoot):
    """
    Heftelse tinglyst i Grunnboka mot ein eigedom eller burettslagsandel. Nokre heftingar har avgrensa geografisk
    utbreiing og manglar stadfestring.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["TinglystHeftelse"]
    class_class_curie: ClassVar[str] = "ngre:TinglystHeftelse"
    class_name: ClassVar[str] = "TinglystHeftelse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/TinglystHeftelse")

    id: Union[str, TinglystHeftelseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TinglystHeftelseId):
            self.id = TinglystHeftelseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RettighetForAaBenytteEiendom(YAMLRoot):
    """
    Rettar og avtalar som er nødvendige for å kunne benytte eigedommen. Desse er registrerte som heftingar i Grunnboka
    på teneleg eigedom.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["RettighetForAaBenytteEiendom"]
    class_class_curie: ClassVar[str] = "ngre:RettighetForAaBenytteEiendom"
    class_name: ClassVar[str] = "RettighetForAaBenytteEiendom"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/RettighetForAaBenytteEiendom")

    id: Union[str, RettighetForAaBenytteEiendomId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RettighetForAaBenytteEiendomId):
            self.id = RettighetForAaBenytteEiendomId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Borettslag(YAMLRoot):
    """
    Eit burettslag er ein type hovudeining (juridisk person) som eig burettslagsbygningen. Burettslagsandelar
    tilhøyrer eit burettslag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Borettslag"]
    class_class_curie: ClassVar[str] = "ngre:Borettslag"
    class_name: ClassVar[str] = "Borettslag"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Borettslag")

    id: Union[str, BorettslagId] = None
    er_av_type_hovedenhet: Union[str, HovedenhetId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BorettslagId):
            self.id = BorettslagId(self.id)

        if self._is_empty(self.er_av_type_hovedenhet):
            self.MissingRequiredField("er_av_type_hovedenhet")
        if not isinstance(self.er_av_type_hovedenhet, HovedenhetId):
            self.er_av_type_hovedenhet = HovedenhetId(self.er_av_type_hovedenhet)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OffisiellAdresse(YAMLRoot):
    """
    Offisiell adresse tildelt av kommunen. Tilhøyrer Domene adresse og forvaltast av Matrikkelen via NGR-adresse.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["OffisiellAdresse"]
    class_class_curie: ClassVar[str] = "ngre:OffisiellAdresse"
    class_name: ClassVar[str] = "OffisiellAdresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/OffisiellAdresse")

    id: Union[str, OffisiellAdresseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OffisiellAdresseId):
            self.id = OffisiellAdresseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    """
    Ein fysisk person. Tilhøyrer Domene person.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Person"]
    class_class_curie: ClassVar[str] = "ngre:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Person")

    id: Union[str, PersonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Hovedenhet(YAMLRoot):
    """
    Ei hovudeining i Einingsregisteret. Juridisk person som kan ha undereiningar. Tilhøyrer Domene virksomhet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Hovedenhet"]
    class_class_curie: ClassVar[str] = "ngre:Hovedenhet"
    class_name: ClassVar[str] = "Hovedenhet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Hovedenhet")

    id: Union[str, HovedenhetId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HovedenhetId):
            self.id = HovedenhetId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kommune(YAMLRoot):
    """
    Norsk kommune. Tilhøyrer Domene nasjonal inndelingsbase og forvaltast av Nasjonal inndelingsbase.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRE["Kommune"]
    class_class_curie: ClassVar[str] = "ngre:Kommune"
    class_name: ClassVar[str] = "Kommune"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-eiendom/Kommune")

    id: Union[str, KommuneId] = None
    kommunenummer_verdi: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KommuneId):
            self.id = KommuneId(self.id)

        if self._is_empty(self.kommunenummer_verdi):
            self.MissingRequiredField("kommunenummer_verdi")
        if not isinstance(self.kommunenummer_verdi, str):
            self.kommunenummer_verdi = str(self.kommunenummer_verdi)

        super().__post_init__(**kwargs)


# Enumerations
class Etasjeplan(EnumDefinitionImpl):
    """
    Kode for kva del av bygningen ei brukseining ligg i.
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
        description="Kode for kva del av bygningen ei brukseining ligg i.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.identifiseres_av = Slot(uri=NGRE.identifiseresAv, name="identifiseres_av", curie=NGRE.curie('identifiseresAv'),
                   model_uri=DEFAULT_.identifiseres_av, domain=None, range=Optional[Union[str, MatrikkelenhetId]])

slots.bestar_av_matrikkelenhet = Slot(uri=NGRE.bestarAvMatrikkelenhet, name="bestar_av_matrikkelenhet", curie=NGRE.curie('bestarAvMatrikkelenhet'),
                   model_uri=DEFAULT_.bestar_av_matrikkelenhet, domain=None, range=Optional[Union[str, MatrikkelenhetId]])

slots.bestar_av_bygning = Slot(uri=NGRE.bestarAvBygning, name="bestar_av_bygning", curie=NGRE.curie('bestarAvBygning'),
                   model_uri=DEFAULT_.bestar_av_bygning, domain=None, range=Optional[Union[Union[str, BygningId], list[Union[str, BygningId]]]])

slots.bestar_av_rettighet = Slot(uri=NGRE.bestarAvRettighet, name="bestar_av_rettighet", curie=NGRE.curie('bestarAvRettighet'),
                   model_uri=DEFAULT_.bestar_av_rettighet, domain=None, range=Optional[Union[Union[str, RettighetForAaBenytteEiendomId], list[Union[str, RettighetForAaBenytteEiendomId]]]])

slots.bestar_av_fast_eiendom = Slot(uri=NGRE.bestarAvFastEiendom, name="bestar_av_fast_eiendom", curie=NGRE.curie('bestarAvFastEiendom'),
                   model_uri=DEFAULT_.bestar_av_fast_eiendom, domain=None, range=Optional[Union[Union[str, FastEiendomId], list[Union[str, FastEiendomId]]]])

slots.har_eierforhold = Slot(uri=NGRE.harEierforhold, name="har_eierforhold", curie=NGRE.curie('harEierforhold'),
                   model_uri=DEFAULT_.har_eierforhold, domain=None, range=Optional[Union[Union[str, EierforholdId], list[Union[str, EierforholdId]]]])

slots.har_tinglyst_heftelse = Slot(uri=NGRE.harTinglystHeftelse, name="har_tinglyst_heftelse", curie=NGRE.curie('harTinglystHeftelse'),
                   model_uri=DEFAULT_.har_tinglyst_heftelse, domain=None, range=Optional[Union[Union[str, TinglystHeftelseId], list[Union[str, TinglystHeftelseId]]]])

slots.tilhoerer_borettslag = Slot(uri=NGRE.tilhoererBorettslag, name="tilhoerer_borettslag", curie=NGRE.curie('tilhoererBorettslag'),
                   model_uri=DEFAULT_.tilhoerer_borettslag, domain=None, range=Optional[Union[str, BorettslagId]])

slots.identifiseres_med = Slot(uri=NGRE.identifiseresMed, name="identifiseres_med", curie=NGRE.curie('identifiseresMed'),
                   model_uri=DEFAULT_.identifiseres_med, domain=None, range=Optional[Union[str, MatrikkelnummerId]])

slots.ligger_innenfor_kommune = Slot(uri=NGRE.liggerInnenforKommune, name="ligger_innenfor_kommune", curie=NGRE.curie('liggerInnenforKommune'),
                   model_uri=DEFAULT_.ligger_innenfor_kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.er_del_av_teig = Slot(uri=NGRE.erDelAvTeig, name="er_del_av_teig", curie=NGRE.curie('erDelAvTeig'),
                   model_uri=DEFAULT_.er_del_av_teig, domain=None, range=Optional[Union[Union[str, TeigId], list[Union[str, TeigId]]]])

slots.har_teig = Slot(uri=NGRE.harTeig, name="har_teig", curie=NGRE.curie('harTeig'),
                   model_uri=DEFAULT_.har_teig, domain=None, range=Optional[Union[Union[str, TeigId], list[Union[str, TeigId]]]])

slots.har_anleggsprojeksjonsflate = Slot(uri=NGRE.harAnleggsprojeksjonsflate, name="har_anleggsprojeksjonsflate", curie=NGRE.curie('harAnleggsprojeksjonsflate'),
                   model_uri=DEFAULT_.har_anleggsprojeksjonsflate, domain=None, range=Optional[Union[str, AnleggsprojeksjonsflateId]])

slots.kan_vaere_pa = Slot(uri=NGRE.kanVaerePa, name="kan_vaere_pa", curie=NGRE.curie('kanVaerePa'),
                   model_uri=DEFAULT_.kan_vaere_pa, domain=None, range=Optional[Union[str, MatrikkelenhetId]])

slots.bestar_av_kommunenummer = Slot(uri=NGRE.bestarAvKommunenummer, name="bestar_av_kommunenummer", curie=NGRE.curie('bestarAvKommunenummer'),
                   model_uri=DEFAULT_.bestar_av_kommunenummer, domain=None, range=Optional[Union[str, KommunenummerId]])

slots.bestar_av_gaardsnummer = Slot(uri=NGRE.bestarAvGaardsnummer, name="bestar_av_gaardsnummer", curie=NGRE.curie('bestarAvGaardsnummer'),
                   model_uri=DEFAULT_.bestar_av_gaardsnummer, domain=None, range=Optional[Union[str, GaardsnummerId]])

slots.bestar_av_bruksnummer = Slot(uri=NGRE.bestarAvBruksnummer, name="bestar_av_bruksnummer", curie=NGRE.curie('bestarAvBruksnummer'),
                   model_uri=DEFAULT_.bestar_av_bruksnummer, domain=None, range=Optional[Union[str, BruksnummerId]])

slots.bestar_av_festenummer = Slot(uri=NGRE.bestarAvFestenummer, name="bestar_av_festenummer", curie=NGRE.curie('bestarAvFestenummer'),
                   model_uri=DEFAULT_.bestar_av_festenummer, domain=None, range=Optional[Union[str, FestenummerId]])

slots.bestar_av_seksjonsnummer = Slot(uri=NGRE.bestarAvSeksjonsnummer, name="bestar_av_seksjonsnummer", curie=NGRE.curie('bestarAvSeksjonsnummer'),
                   model_uri=DEFAULT_.bestar_av_seksjonsnummer, domain=None, range=Optional[Union[str, SeksjonsnummerId]])

slots.har_bygningsnummer = Slot(uri=NGRE.harBygningsnummer, name="har_bygningsnummer", curie=NGRE.curie('harBygningsnummer'),
                   model_uri=DEFAULT_.har_bygningsnummer, domain=None, range=Optional[Union[str, BygningsnummerId]])

slots.har_representasjonspunkt = Slot(uri=NGRE.harRepresentasjonspunkt, name="har_representasjonspunkt", curie=NGRE.curie('harRepresentasjonspunkt'),
                   model_uri=DEFAULT_.har_representasjonspunkt, domain=None, range=Optional[Union[str, RepresentasjonspunktId]])

slots.er_knyttet_til_matrikkelenhet = Slot(uri=NGRE.erKnyttetTilMatrikkelenhet, name="er_knyttet_til_matrikkelenhet", curie=NGRE.curie('erKnyttetTilMatrikkelenhet'),
                   model_uri=DEFAULT_.er_knyttet_til_matrikkelenhet, domain=None, range=Optional[Union[str, MatrikkelenhetId]])

slots.har_ytre_inngang = Slot(uri=NGRE.harYtreInngang, name="har_ytre_inngang", curie=NGRE.curie('harYtreInngang'),
                   model_uri=DEFAULT_.har_ytre_inngang, domain=None, range=Optional[Union[Union[str, YtreInngangId], list[Union[str, YtreInngangId]]]])

slots.har_bruksenhet = Slot(uri=NGRE.harBruksenhet, name="har_bruksenhet", curie=NGRE.curie('harBruksenhet'),
                   model_uri=DEFAULT_.har_bruksenhet, domain=None, range=Optional[Union[Union[str, BruksenhetId], list[Union[str, BruksenhetId]]]])

slots.har_etasje = Slot(uri=NGRE.harEtasje, name="har_etasje", curie=NGRE.curie('harEtasje'),
                   model_uri=DEFAULT_.har_etasje, domain=None, range=Optional[Union[Union[str, EtasjeId], list[Union[str, EtasjeId]]]])

slots.gjelder_bruksenhet = Slot(uri=NGRE.gjelderBruksenhet, name="gjelder_bruksenhet", curie=NGRE.curie('gjelderBruksenhet'),
                   model_uri=DEFAULT_.gjelder_bruksenhet, domain=None, range=Optional[Union[Union[str, BruksenhetId], list[Union[str, BruksenhetId]]]])

slots.har_offisiell_adresse = Slot(uri=NGRE.harOffisiellAdresse, name="har_offisiell_adresse", curie=NGRE.curie('harOffisiellAdresse'),
                   model_uri=DEFAULT_.har_offisiell_adresse, domain=None, range=Optional[Union[str, OffisiellAdresseId]])

slots.har_bruksenhetsnummer = Slot(uri=NGRE.harBruksenhetsnummer, name="har_bruksenhetsnummer", curie=NGRE.curie('harBruksenhetsnummer'),
                   model_uri=DEFAULT_.har_bruksenhetsnummer, domain=None, range=Optional[Union[str, BruksenhetsnummerId]])

slots.er_tilknyttet_matrikkelenhet = Slot(uri=NGRE.erTilknyttetMatrikkelenhet, name="er_tilknyttet_matrikkelenhet", curie=NGRE.curie('erTilknyttetMatrikkelenhet'),
                   model_uri=DEFAULT_.er_tilknyttet_matrikkelenhet, domain=None, range=Optional[Union[str, MatrikkelenhetId]])

slots.ligger_i_etasje = Slot(uri=NGRE.liggerIEtasje, name="ligger_i_etasje", curie=NGRE.curie('liggerIEtasje'),
                   model_uri=DEFAULT_.ligger_i_etasje, domain=None, range=Optional[Union[Union[str, EtasjeId], list[Union[str, EtasjeId]]]])

slots.gjelder_matrikkelenhet = Slot(uri=NGRE.gjelderMatrikkelenhet, name="gjelder_matrikkelenhet", curie=NGRE.curie('gjelderMatrikkelenhet'),
                   model_uri=DEFAULT_.gjelder_matrikkelenhet, domain=None, range=Optional[Union[str, MatrikkelenhetId]])

slots.kan_gjelde_borettslagsandel = Slot(uri=NGRE.kanGjeldeBorettslagsandel, name="kan_gjelde_borettslagsandel", curie=NGRE.curie('kanGjeldeBorettslagsandel'),
                   model_uri=DEFAULT_.kan_gjelde_borettslagsandel, domain=None, range=Optional[Union[str, BorettslagsandelId]])

slots.gjelder_hjemmel_eiendomsrett = Slot(uri=NGRE.gjelderHjemmelEiendomsrett, name="gjelder_hjemmel_eiendomsrett", curie=NGRE.curie('gjelderHjemmelEiendomsrett'),
                   model_uri=DEFAULT_.gjelder_hjemmel_eiendomsrett, domain=None, range=Optional[Union[str, HjemmelTilEiendomsrettId]])

slots.gjelder_hjemmel_festerett = Slot(uri=NGRE.gjelderHjemmelFesterett, name="gjelder_hjemmel_festerett", curie=NGRE.curie('gjelderHjemmelFesterett'),
                   model_uri=DEFAULT_.gjelder_hjemmel_festerett, domain=None, range=Optional[Union[str, HjemmelTilFesterettId]])

slots.gjelder_hjemmel_framfesterett = Slot(uri=NGRE.gjelderHjemmelFramfesterett, name="gjelder_hjemmel_framfesterett", curie=NGRE.curie('gjelderHjemmelFramfesterett'),
                   model_uri=DEFAULT_.gjelder_hjemmel_framfesterett, domain=None, range=Optional[Union[str, HjemmelTilFramfesterettId]])

slots.har_andel = Slot(uri=NGRE.harAndel, name="har_andel", curie=NGRE.curie('harAndel'),
                   model_uri=DEFAULT_.har_andel, domain=None, range=Optional[Union[Union[str, AndelId], list[Union[str, AndelId]]]])

slots.har_rettighetshaver = Slot(uri=NGRE.harRettighetshaver, name="har_rettighetshaver", curie=NGRE.curie('harRettighetshaver'),
                   model_uri=DEFAULT_.har_rettighetshaver, domain=None, range=Optional[Union[Union[str, RettighetshaverId], list[Union[str, RettighetshaverId]]]])

slots.er_av_type_person = Slot(uri=NGRE.erAvTypePerson, name="er_av_type_person", curie=NGRE.curie('erAvTypePerson'),
                   model_uri=DEFAULT_.er_av_type_person, domain=None, range=Optional[Union[str, PersonId]])

slots.er_av_type_hovedenhet = Slot(uri=NGRE.erAvTypeHovedenhet, name="er_av_type_hovedenhet", curie=NGRE.curie('erAvTypeHovedenhet'),
                   model_uri=DEFAULT_.er_av_type_hovedenhet, domain=None, range=Optional[Union[str, HovedenhetId]])

slots.kommunenummer_verdi = Slot(uri=NGRE.kommunenummer, name="kommunenummer_verdi", curie=NGRE.curie('kommunenummer'),
                   model_uri=DEFAULT_.kommunenummer_verdi, domain=None, range=Optional[str])

slots.gaardsnummer_verdi = Slot(uri=NGRE.gaardsnummer, name="gaardsnummer_verdi", curie=NGRE.curie('gaardsnummer'),
                   model_uri=DEFAULT_.gaardsnummer_verdi, domain=None, range=Optional[int])

slots.bruksnummer_verdi = Slot(uri=NGRE.bruksnummer, name="bruksnummer_verdi", curie=NGRE.curie('bruksnummer'),
                   model_uri=DEFAULT_.bruksnummer_verdi, domain=None, range=Optional[int])

slots.festenummer_verdi = Slot(uri=NGRE.festenummer, name="festenummer_verdi", curie=NGRE.curie('festenummer'),
                   model_uri=DEFAULT_.festenummer_verdi, domain=None, range=Optional[int])

slots.seksjonsnummer_verdi = Slot(uri=NGRE.seksjonsnummer, name="seksjonsnummer_verdi", curie=NGRE.curie('seksjonsnummer'),
                   model_uri=DEFAULT_.seksjonsnummer_verdi, domain=None, range=Optional[int])

slots.bygningsnummer_verdi = Slot(uri=NGRE.bygningsnummer, name="bygningsnummer_verdi", curie=NGRE.curie('bygningsnummer'),
                   model_uri=DEFAULT_.bygningsnummer_verdi, domain=None, range=Optional[int])

slots.koordinat_ost = Slot(uri=NGRE.koordinatOst, name="koordinat_ost", curie=NGRE.curie('koordinatOst'),
                   model_uri=DEFAULT_.koordinat_ost, domain=None, range=Optional[float])

slots.koordinat_nord = Slot(uri=NGRE.koordinatNord, name="koordinat_nord", curie=NGRE.curie('koordinatNord'),
                   model_uri=DEFAULT_.koordinat_nord, domain=None, range=Optional[float])

slots.koordinatsystem = Slot(uri=NGRE.koordinatsystem, name="koordinatsystem", curie=NGRE.curie('koordinatsystem'),
                   model_uri=DEFAULT_.koordinatsystem, domain=None, range=Optional[str])

slots.etasjeplan = Slot(uri=NGRE.etasjeplan, name="etasjeplan", curie=NGRE.curie('etasjeplan'),
                   model_uri=DEFAULT_.etasjeplan, domain=None, range=Optional[Union[str, "Etasjeplan"]])

slots.etasjenummer = Slot(uri=NGRE.etasjenummer, name="etasjenummer", curie=NGRE.curie('etasjenummer'),
                   model_uri=DEFAULT_.etasjenummer, domain=None, range=Optional[int])

slots.nummerering_i_etasjen = Slot(uri=NGRE.nummereringIEtasjen, name="nummerering_i_etasjen", curie=NGRE.curie('nummereringIEtasjen'),
                   model_uri=DEFAULT_.nummerering_i_etasjen, domain=None, range=Optional[int])

slots.eiendomContainer__fasteEiendommer = Slot(uri=DEFAULT_.fasteEiendommer, name="eiendomContainer__fasteEiendommer", curie=DEFAULT_.curie('fasteEiendommer'),
                   model_uri=DEFAULT_.eiendomContainer__fasteEiendommer, domain=None, range=Optional[Union[dict[Union[str, FastEiendomId], Union[dict, FastEiendom]], list[Union[dict, FastEiendom]]]])

slots.eiendomContainer__samlinger = Slot(uri=DEFAULT_.samlinger, name="eiendomContainer__samlinger", curie=DEFAULT_.curie('samlinger'),
                   model_uri=DEFAULT_.eiendomContainer__samlinger, domain=None, range=Optional[Union[dict[Union[str, SamletFastEiendomId], Union[dict, SamletFastEiendom]], list[Union[dict, SamletFastEiendom]]]])

slots.eiendomContainer__borettslagsandeler = Slot(uri=DEFAULT_.borettslagsandeler, name="eiendomContainer__borettslagsandeler", curie=DEFAULT_.curie('borettslagsandeler'),
                   model_uri=DEFAULT_.eiendomContainer__borettslagsandeler, domain=None, range=Optional[Union[dict[Union[str, BorettslagsandelId], Union[dict, Borettslagsandel]], list[Union[dict, Borettslagsandel]]]])

slots.eiendomContainer__grunneiendommer = Slot(uri=DEFAULT_.grunneiendommer, name="eiendomContainer__grunneiendommer", curie=DEFAULT_.curie('grunneiendommer'),
                   model_uri=DEFAULT_.eiendomContainer__grunneiendommer, domain=None, range=Optional[Union[dict[Union[str, GrunneiendomId], Union[dict, Grunneiendom]], list[Union[dict, Grunneiendom]]]])

slots.eiendomContainer__festegrunn = Slot(uri=DEFAULT_.festegrunn, name="eiendomContainer__festegrunn", curie=DEFAULT_.curie('festegrunn'),
                   model_uri=DEFAULT_.eiendomContainer__festegrunn, domain=None, range=Optional[Union[dict[Union[str, FestegrunnId], Union[dict, Festegrunn]], list[Union[dict, Festegrunn]]]])

slots.eiendomContainer__jordsameier = Slot(uri=DEFAULT_.jordsameier, name="eiendomContainer__jordsameier", curie=DEFAULT_.curie('jordsameier'),
                   model_uri=DEFAULT_.eiendomContainer__jordsameier, domain=None, range=Optional[Union[dict[Union[str, JordsameieId], Union[dict, Jordsameie]], list[Union[dict, Jordsameie]]]])

slots.eiendomContainer__eierseksjoner = Slot(uri=DEFAULT_.eierseksjoner, name="eiendomContainer__eierseksjoner", curie=DEFAULT_.curie('eierseksjoner'),
                   model_uri=DEFAULT_.eiendomContainer__eierseksjoner, domain=None, range=Optional[Union[dict[Union[str, EierseksjonId], Union[dict, Eierseksjon]], list[Union[dict, Eierseksjon]]]])

slots.eiendomContainer__anleggseiendommer = Slot(uri=DEFAULT_.anleggseiendommer, name="eiendomContainer__anleggseiendommer", curie=DEFAULT_.curie('anleggseiendommer'),
                   model_uri=DEFAULT_.eiendomContainer__anleggseiendommer, domain=None, range=Optional[Union[dict[Union[str, AnleggseiendomId], Union[dict, Anleggseiendom]], list[Union[dict, Anleggseiendom]]]])

slots.eiendomContainer__andreMatrikkelenheter = Slot(uri=DEFAULT_.andreMatrikkelenheter, name="eiendomContainer__andreMatrikkelenheter", curie=DEFAULT_.curie('andreMatrikkelenheter'),
                   model_uri=DEFAULT_.eiendomContainer__andreMatrikkelenheter, domain=None, range=Optional[Union[dict[Union[str, AnnenMatrikkelenhetId], Union[dict, AnnenMatrikkelenhet]], list[Union[dict, AnnenMatrikkelenhet]]]])

slots.eiendomContainer__matrikkelnumre = Slot(uri=DEFAULT_.matrikkelnumre, name="eiendomContainer__matrikkelnumre", curie=DEFAULT_.curie('matrikkelnumre'),
                   model_uri=DEFAULT_.eiendomContainer__matrikkelnumre, domain=None, range=Optional[Union[dict[Union[str, MatrikkelnummerId], Union[dict, Matrikkelnummer]], list[Union[dict, Matrikkelnummer]]]])

slots.eiendomContainer__bygninger = Slot(uri=DEFAULT_.bygninger, name="eiendomContainer__bygninger", curie=DEFAULT_.curie('bygninger'),
                   model_uri=DEFAULT_.eiendomContainer__bygninger, domain=None, range=Optional[Union[dict[Union[str, BygningId], Union[dict, Bygning]], list[Union[dict, Bygning]]]])

slots.eiendomContainer__ytreInnganger = Slot(uri=DEFAULT_.ytreInnganger, name="eiendomContainer__ytreInnganger", curie=DEFAULT_.curie('ytreInnganger'),
                   model_uri=DEFAULT_.eiendomContainer__ytreInnganger, domain=None, range=Optional[Union[dict[Union[str, YtreInngangId], Union[dict, YtreInngang]], list[Union[dict, YtreInngang]]]])

slots.eiendomContainer__bruksenheter = Slot(uri=DEFAULT_.bruksenheter, name="eiendomContainer__bruksenheter", curie=DEFAULT_.curie('bruksenheter'),
                   model_uri=DEFAULT_.eiendomContainer__bruksenheter, domain=None, range=Optional[Union[dict[Union[str, BruksenhetId], Union[dict, Bruksenhet]], list[Union[dict, Bruksenhet]]]])

slots.eiendomContainer__etasjer = Slot(uri=DEFAULT_.etasjer, name="eiendomContainer__etasjer", curie=DEFAULT_.curie('etasjer'),
                   model_uri=DEFAULT_.eiendomContainer__etasjer, domain=None, range=Optional[Union[dict[Union[str, EtasjeId], Union[dict, Etasje]], list[Union[dict, Etasje]]]])

slots.eiendomContainer__teiger = Slot(uri=DEFAULT_.teiger, name="eiendomContainer__teiger", curie=DEFAULT_.curie('teiger'),
                   model_uri=DEFAULT_.eiendomContainer__teiger, domain=None, range=Optional[Union[list[Union[str, TeigId]], dict[Union[str, TeigId], Union[dict, Teig]]]])

slots.eiendomContainer__tinglystEierforhold = Slot(uri=DEFAULT_.tinglystEierforhold, name="eiendomContainer__tinglystEierforhold", curie=DEFAULT_.curie('tinglystEierforhold'),
                   model_uri=DEFAULT_.eiendomContainer__tinglystEierforhold, domain=None, range=Optional[Union[dict[Union[str, TinglystEierforholdId], Union[dict, TinglystEierforhold]], list[Union[dict, TinglystEierforhold]]]])

slots.eiendomContainer__ikkeTinglystEierforhold = Slot(uri=DEFAULT_.ikkeTinglystEierforhold, name="eiendomContainer__ikkeTinglystEierforhold", curie=DEFAULT_.curie('ikkeTinglystEierforhold'),
                   model_uri=DEFAULT_.eiendomContainer__ikkeTinglystEierforhold, domain=None, range=Optional[Union[dict[Union[str, IkkeTinglystEierforholdId], Union[dict, IkkeTinglystEierforhold]], list[Union[dict, IkkeTinglystEierforhold]]]])

slots.eiendomContainer__hjemmelEiendomsrett = Slot(uri=DEFAULT_.hjemmelEiendomsrett, name="eiendomContainer__hjemmelEiendomsrett", curie=DEFAULT_.curie('hjemmelEiendomsrett'),
                   model_uri=DEFAULT_.eiendomContainer__hjemmelEiendomsrett, domain=None, range=Optional[Union[dict[Union[str, HjemmelTilEiendomsrettId], Union[dict, HjemmelTilEiendomsrett]], list[Union[dict, HjemmelTilEiendomsrett]]]])

slots.eiendomContainer__hjemmelFesterett = Slot(uri=DEFAULT_.hjemmelFesterett, name="eiendomContainer__hjemmelFesterett", curie=DEFAULT_.curie('hjemmelFesterett'),
                   model_uri=DEFAULT_.eiendomContainer__hjemmelFesterett, domain=None, range=Optional[Union[dict[Union[str, HjemmelTilFesterettId], Union[dict, HjemmelTilFesterett]], list[Union[dict, HjemmelTilFesterett]]]])

slots.eiendomContainer__hjemmelFramfesterett = Slot(uri=DEFAULT_.hjemmelFramfesterett, name="eiendomContainer__hjemmelFramfesterett", curie=DEFAULT_.curie('hjemmelFramfesterett'),
                   model_uri=DEFAULT_.eiendomContainer__hjemmelFramfesterett, domain=None, range=Optional[Union[dict[Union[str, HjemmelTilFramfesterettId], Union[dict, HjemmelTilFramfesterett]], list[Union[dict, HjemmelTilFramfesterett]]]])

slots.eiendomContainer__andeler = Slot(uri=DEFAULT_.andeler, name="eiendomContainer__andeler", curie=DEFAULT_.curie('andeler'),
                   model_uri=DEFAULT_.eiendomContainer__andeler, domain=None, range=Optional[Union[dict[Union[str, AndelId], Union[dict, Andel]], list[Union[dict, Andel]]]])

slots.eiendomContainer__rettighetshavere = Slot(uri=DEFAULT_.rettighetshavere, name="eiendomContainer__rettighetshavere", curie=DEFAULT_.curie('rettighetshavere'),
                   model_uri=DEFAULT_.eiendomContainer__rettighetshavere, domain=None, range=Optional[Union[dict[Union[str, RettighetshaverId], Union[dict, Rettighetshaver]], list[Union[dict, Rettighetshaver]]]])

slots.eiendomContainer__tinglystHeftelser = Slot(uri=DEFAULT_.tinglystHeftelser, name="eiendomContainer__tinglystHeftelser", curie=DEFAULT_.curie('tinglystHeftelser'),
                   model_uri=DEFAULT_.eiendomContainer__tinglystHeftelser, domain=None, range=Optional[Union[list[Union[str, TinglystHeftelseId]], dict[Union[str, TinglystHeftelseId], Union[dict, TinglystHeftelse]]]])

slots.eiendomContainer__rettigheter = Slot(uri=DEFAULT_.rettigheter, name="eiendomContainer__rettigheter", curie=DEFAULT_.curie('rettigheter'),
                   model_uri=DEFAULT_.eiendomContainer__rettigheter, domain=None, range=Optional[Union[list[Union[str, RettighetForAaBenytteEiendomId]], dict[Union[str, RettighetForAaBenytteEiendomId], Union[dict, RettighetForAaBenytteEiendom]]]])

slots.eiendomContainer__borettslag = Slot(uri=DEFAULT_.borettslag, name="eiendomContainer__borettslag", curie=DEFAULT_.curie('borettslag'),
                   model_uri=DEFAULT_.eiendomContainer__borettslag, domain=None, range=Optional[Union[dict[Union[str, BorettslagId], Union[dict, Borettslag]], list[Union[dict, Borettslag]]]])

slots.eiendomContainer__representasjonspunkt = Slot(uri=DEFAULT_.representasjonspunkt, name="eiendomContainer__representasjonspunkt", curie=DEFAULT_.curie('representasjonspunkt'),
                   model_uri=DEFAULT_.eiendomContainer__representasjonspunkt, domain=None, range=Optional[Union[dict[Union[str, RepresentasjonspunktId], Union[dict, Representasjonspunkt]], list[Union[dict, Representasjonspunkt]]]])

slots.FastEiendom_identifiseres_av = Slot(uri=NGRE.identifiseresAv, name="FastEiendom_identifiseres_av", curie=NGRE.curie('identifiseresAv'),
                   model_uri=DEFAULT_.FastEiendom_identifiseres_av, domain=FastEiendom, range=Union[str, MatrikkelenhetId])

slots.FastEiendom_bestar_av_matrikkelenhet = Slot(uri=NGRE.bestarAvMatrikkelenhet, name="FastEiendom_bestar_av_matrikkelenhet", curie=NGRE.curie('bestarAvMatrikkelenhet'),
                   model_uri=DEFAULT_.FastEiendom_bestar_av_matrikkelenhet, domain=FastEiendom, range=Union[str, MatrikkelenhetId])

slots.FastEiendom_bestar_av_bygning = Slot(uri=NGRE.bestarAvBygning, name="FastEiendom_bestar_av_bygning", curie=NGRE.curie('bestarAvBygning'),
                   model_uri=DEFAULT_.FastEiendom_bestar_av_bygning, domain=FastEiendom, range=Optional[Union[Union[str, BygningId], list[Union[str, BygningId]]]])

slots.FastEiendom_bestar_av_rettighet = Slot(uri=NGRE.bestarAvRettighet, name="FastEiendom_bestar_av_rettighet", curie=NGRE.curie('bestarAvRettighet'),
                   model_uri=DEFAULT_.FastEiendom_bestar_av_rettighet, domain=FastEiendom, range=Optional[Union[Union[str, RettighetForAaBenytteEiendomId], list[Union[str, RettighetForAaBenytteEiendomId]]]])

slots.FastEiendom_har_eierforhold = Slot(uri=NGRE.harEierforhold, name="FastEiendom_har_eierforhold", curie=NGRE.curie('harEierforhold'),
                   model_uri=DEFAULT_.FastEiendom_har_eierforhold, domain=FastEiendom, range=Optional[Union[Union[str, EierforholdId], list[Union[str, EierforholdId]]]])

slots.FastEiendom_har_tinglyst_heftelse = Slot(uri=NGRE.harTinglystHeftelse, name="FastEiendom_har_tinglyst_heftelse", curie=NGRE.curie('harTinglystHeftelse'),
                   model_uri=DEFAULT_.FastEiendom_har_tinglyst_heftelse, domain=FastEiendom, range=Optional[Union[Union[str, TinglystHeftelseId], list[Union[str, TinglystHeftelseId]]]])

slots.SamletFastEiendom_bestar_av_fast_eiendom = Slot(uri=NGRE.bestarAvFastEiendom, name="SamletFastEiendom_bestar_av_fast_eiendom", curie=NGRE.curie('bestarAvFastEiendom'),
                   model_uri=DEFAULT_.SamletFastEiendom_bestar_av_fast_eiendom, domain=SamletFastEiendom, range=Union[Union[str, FastEiendomId], list[Union[str, FastEiendomId]]])

slots.Borettslagsandel_tilhoerer_borettslag = Slot(uri=NGRE.tilhoererBorettslag, name="Borettslagsandel_tilhoerer_borettslag", curie=NGRE.curie('tilhoererBorettslag'),
                   model_uri=DEFAULT_.Borettslagsandel_tilhoerer_borettslag, domain=Borettslagsandel, range=Union[str, BorettslagId])

slots.Borettslagsandel_har_eierforhold = Slot(uri=NGRE.harEierforhold, name="Borettslagsandel_har_eierforhold", curie=NGRE.curie('harEierforhold'),
                   model_uri=DEFAULT_.Borettslagsandel_har_eierforhold, domain=Borettslagsandel, range=Optional[Union[Union[str, EierforholdId], list[Union[str, EierforholdId]]]])

slots.Borettslagsandel_har_tinglyst_heftelse = Slot(uri=NGRE.harTinglystHeftelse, name="Borettslagsandel_har_tinglyst_heftelse", curie=NGRE.curie('harTinglystHeftelse'),
                   model_uri=DEFAULT_.Borettslagsandel_har_tinglyst_heftelse, domain=Borettslagsandel, range=Optional[Union[Union[str, TinglystHeftelseId], list[Union[str, TinglystHeftelseId]]]])

slots.Matrikkelenhet_identifiseres_med = Slot(uri=NGRE.identifiseresMed, name="Matrikkelenhet_identifiseres_med", curie=NGRE.curie('identifiseresMed'),
                   model_uri=DEFAULT_.Matrikkelenhet_identifiseres_med, domain=Matrikkelenhet, range=Union[str, MatrikkelnummerId])

slots.Matrikkelenhet_ligger_innenfor_kommune = Slot(uri=NGRE.liggerInnenforKommune, name="Matrikkelenhet_ligger_innenfor_kommune", curie=NGRE.curie('liggerInnenforKommune'),
                   model_uri=DEFAULT_.Matrikkelenhet_ligger_innenfor_kommune, domain=Matrikkelenhet, range=Union[str, KommuneId])

slots.Matrikkelenhet_er_del_av_teig = Slot(uri=NGRE.erDelAvTeig, name="Matrikkelenhet_er_del_av_teig", curie=NGRE.curie('erDelAvTeig'),
                   model_uri=DEFAULT_.Matrikkelenhet_er_del_av_teig, domain=Matrikkelenhet, range=Optional[Union[Union[str, TeigId], list[Union[str, TeigId]]]])

slots.Matrikkelenhet_har_teig = Slot(uri=NGRE.harTeig, name="Matrikkelenhet_har_teig", curie=NGRE.curie('harTeig'),
                   model_uri=DEFAULT_.Matrikkelenhet_har_teig, domain=Matrikkelenhet, range=Optional[Union[Union[str, TeigId], list[Union[str, TeigId]]]])

slots.Matrikkelenhet_har_anleggsprojeksjonsflate = Slot(uri=NGRE.harAnleggsprojeksjonsflate, name="Matrikkelenhet_har_anleggsprojeksjonsflate", curie=NGRE.curie('harAnleggsprojeksjonsflate'),
                   model_uri=DEFAULT_.Matrikkelenhet_har_anleggsprojeksjonsflate, domain=Matrikkelenhet, range=Optional[Union[str, AnleggsprojeksjonsflateId]])

slots.Grunneiendom_kan_vaere_pa = Slot(uri=NGRE.kanVaerePa, name="Grunneiendom_kan_vaere_pa", curie=NGRE.curie('kanVaerePa'),
                   model_uri=DEFAULT_.Grunneiendom_kan_vaere_pa, domain=Grunneiendom, range=Optional[Union[str, MatrikkelenhetId]])

slots.Festegrunn_kan_vaere_pa = Slot(uri=NGRE.kanVaerePa, name="Festegrunn_kan_vaere_pa", curie=NGRE.curie('kanVaerePa'),
                   model_uri=DEFAULT_.Festegrunn_kan_vaere_pa, domain=Festegrunn, range=Optional[Union[str, MatrikkelenhetId]])

slots.Jordsameie_kan_vaere_pa = Slot(uri=NGRE.kanVaerePa, name="Jordsameie_kan_vaere_pa", curie=NGRE.curie('kanVaerePa'),
                   model_uri=DEFAULT_.Jordsameie_kan_vaere_pa, domain=Jordsameie, range=Optional[Union[str, MatrikkelenhetId]])

slots.Eierseksjon_kan_vaere_pa = Slot(uri=NGRE.kanVaerePa, name="Eierseksjon_kan_vaere_pa", curie=NGRE.curie('kanVaerePa'),
                   model_uri=DEFAULT_.Eierseksjon_kan_vaere_pa, domain=Eierseksjon, range=Optional[Union[str, MatrikkelenhetId]])

slots.Matrikkelnummer_bestar_av_kommunenummer = Slot(uri=NGRE.bestarAvKommunenummer, name="Matrikkelnummer_bestar_av_kommunenummer", curie=NGRE.curie('bestarAvKommunenummer'),
                   model_uri=DEFAULT_.Matrikkelnummer_bestar_av_kommunenummer, domain=Matrikkelnummer, range=Union[str, KommunenummerId])

slots.Matrikkelnummer_bestar_av_gaardsnummer = Slot(uri=NGRE.bestarAvGaardsnummer, name="Matrikkelnummer_bestar_av_gaardsnummer", curie=NGRE.curie('bestarAvGaardsnummer'),
                   model_uri=DEFAULT_.Matrikkelnummer_bestar_av_gaardsnummer, domain=Matrikkelnummer, range=Union[str, GaardsnummerId])

slots.Matrikkelnummer_bestar_av_bruksnummer = Slot(uri=NGRE.bestarAvBruksnummer, name="Matrikkelnummer_bestar_av_bruksnummer", curie=NGRE.curie('bestarAvBruksnummer'),
                   model_uri=DEFAULT_.Matrikkelnummer_bestar_av_bruksnummer, domain=Matrikkelnummer, range=Union[str, BruksnummerId])

slots.Matrikkelnummer_bestar_av_festenummer = Slot(uri=NGRE.bestarAvFestenummer, name="Matrikkelnummer_bestar_av_festenummer", curie=NGRE.curie('bestarAvFestenummer'),
                   model_uri=DEFAULT_.Matrikkelnummer_bestar_av_festenummer, domain=Matrikkelnummer, range=Optional[Union[str, FestenummerId]])

slots.Matrikkelnummer_bestar_av_seksjonsnummer = Slot(uri=NGRE.bestarAvSeksjonsnummer, name="Matrikkelnummer_bestar_av_seksjonsnummer", curie=NGRE.curie('bestarAvSeksjonsnummer'),
                   model_uri=DEFAULT_.Matrikkelnummer_bestar_av_seksjonsnummer, domain=Matrikkelnummer, range=Optional[Union[str, SeksjonsnummerId]])

slots.Kommunenummer_kommunenummer_verdi = Slot(uri=NGRE.kommunenummer, name="Kommunenummer_kommunenummer_verdi", curie=NGRE.curie('kommunenummer'),
                   model_uri=DEFAULT_.Kommunenummer_kommunenummer_verdi, domain=Kommunenummer, range=str)

slots.Gaardsnummer_gaardsnummer_verdi = Slot(uri=NGRE.gaardsnummer, name="Gaardsnummer_gaardsnummer_verdi", curie=NGRE.curie('gaardsnummer'),
                   model_uri=DEFAULT_.Gaardsnummer_gaardsnummer_verdi, domain=Gaardsnummer, range=int)

slots.Bruksnummer_bruksnummer_verdi = Slot(uri=NGRE.bruksnummer, name="Bruksnummer_bruksnummer_verdi", curie=NGRE.curie('bruksnummer'),
                   model_uri=DEFAULT_.Bruksnummer_bruksnummer_verdi, domain=Bruksnummer, range=int)

slots.Festenummer_festenummer_verdi = Slot(uri=NGRE.festenummer, name="Festenummer_festenummer_verdi", curie=NGRE.curie('festenummer'),
                   model_uri=DEFAULT_.Festenummer_festenummer_verdi, domain=Festenummer, range=int)

slots.Seksjonsnummer_seksjonsnummer_verdi = Slot(uri=NGRE.seksjonsnummer, name="Seksjonsnummer_seksjonsnummer_verdi", curie=NGRE.curie('seksjonsnummer'),
                   model_uri=DEFAULT_.Seksjonsnummer_seksjonsnummer_verdi, domain=Seksjonsnummer, range=int)

slots.Bygning_har_bygningsnummer = Slot(uri=NGRE.harBygningsnummer, name="Bygning_har_bygningsnummer", curie=NGRE.curie('harBygningsnummer'),
                   model_uri=DEFAULT_.Bygning_har_bygningsnummer, domain=Bygning, range=Union[str, BygningsnummerId])

slots.Bygning_har_representasjonspunkt = Slot(uri=NGRE.harRepresentasjonspunkt, name="Bygning_har_representasjonspunkt", curie=NGRE.curie('harRepresentasjonspunkt'),
                   model_uri=DEFAULT_.Bygning_har_representasjonspunkt, domain=Bygning, range=Union[str, RepresentasjonspunktId])

slots.Bygning_er_knyttet_til_matrikkelenhet = Slot(uri=NGRE.erKnyttetTilMatrikkelenhet, name="Bygning_er_knyttet_til_matrikkelenhet", curie=NGRE.curie('erKnyttetTilMatrikkelenhet'),
                   model_uri=DEFAULT_.Bygning_er_knyttet_til_matrikkelenhet, domain=Bygning, range=Union[str, MatrikkelenhetId])

slots.Bygning_har_ytre_inngang = Slot(uri=NGRE.harYtreInngang, name="Bygning_har_ytre_inngang", curie=NGRE.curie('harYtreInngang'),
                   model_uri=DEFAULT_.Bygning_har_ytre_inngang, domain=Bygning, range=Optional[Union[Union[str, YtreInngangId], list[Union[str, YtreInngangId]]]])

slots.Bygning_har_bruksenhet = Slot(uri=NGRE.harBruksenhet, name="Bygning_har_bruksenhet", curie=NGRE.curie('harBruksenhet'),
                   model_uri=DEFAULT_.Bygning_har_bruksenhet, domain=Bygning, range=Optional[Union[Union[str, BruksenhetId], list[Union[str, BruksenhetId]]]])

slots.Bygning_har_etasje = Slot(uri=NGRE.harEtasje, name="Bygning_har_etasje", curie=NGRE.curie('harEtasje'),
                   model_uri=DEFAULT_.Bygning_har_etasje, domain=Bygning, range=Optional[Union[Union[str, EtasjeId], list[Union[str, EtasjeId]]]])

slots.Bygningsnummer_bygningsnummer_verdi = Slot(uri=NGRE.bygningsnummer, name="Bygningsnummer_bygningsnummer_verdi", curie=NGRE.curie('bygningsnummer'),
                   model_uri=DEFAULT_.Bygningsnummer_bygningsnummer_verdi, domain=Bygningsnummer, range=int)

slots.Representasjonspunkt_koordinat_ost = Slot(uri=NGRE.koordinatOst, name="Representasjonspunkt_koordinat_ost", curie=NGRE.curie('koordinatOst'),
                   model_uri=DEFAULT_.Representasjonspunkt_koordinat_ost, domain=Representasjonspunkt, range=float)

slots.Representasjonspunkt_koordinat_nord = Slot(uri=NGRE.koordinatNord, name="Representasjonspunkt_koordinat_nord", curie=NGRE.curie('koordinatNord'),
                   model_uri=DEFAULT_.Representasjonspunkt_koordinat_nord, domain=Representasjonspunkt, range=float)

slots.Representasjonspunkt_koordinatsystem = Slot(uri=NGRE.koordinatsystem, name="Representasjonspunkt_koordinatsystem", curie=NGRE.curie('koordinatsystem'),
                   model_uri=DEFAULT_.Representasjonspunkt_koordinatsystem, domain=Representasjonspunkt, range=Optional[str])

slots.YtreInngang_gjelder_bruksenhet = Slot(uri=NGRE.gjelderBruksenhet, name="YtreInngang_gjelder_bruksenhet", curie=NGRE.curie('gjelderBruksenhet'),
                   model_uri=DEFAULT_.YtreInngang_gjelder_bruksenhet, domain=YtreInngang, range=Union[Union[str, BruksenhetId], list[Union[str, BruksenhetId]]])

slots.YtreInngang_har_offisiell_adresse = Slot(uri=NGRE.harOffisiellAdresse, name="YtreInngang_har_offisiell_adresse", curie=NGRE.curie('harOffisiellAdresse'),
                   model_uri=DEFAULT_.YtreInngang_har_offisiell_adresse, domain=YtreInngang, range=Optional[Union[str, OffisiellAdresseId]])

slots.Bruksenhet_har_bruksenhetsnummer = Slot(uri=NGRE.harBruksenhetsnummer, name="Bruksenhet_har_bruksenhetsnummer", curie=NGRE.curie('harBruksenhetsnummer'),
                   model_uri=DEFAULT_.Bruksenhet_har_bruksenhetsnummer, domain=Bruksenhet, range=Union[str, BruksenhetsnummerId])

slots.Bruksenhet_ligger_i_etasje = Slot(uri=NGRE.liggerIEtasje, name="Bruksenhet_ligger_i_etasje", curie=NGRE.curie('liggerIEtasje'),
                   model_uri=DEFAULT_.Bruksenhet_ligger_i_etasje, domain=Bruksenhet, range=Union[Union[str, EtasjeId], list[Union[str, EtasjeId]]])

slots.Bruksenhet_er_tilknyttet_matrikkelenhet = Slot(uri=NGRE.erTilknyttetMatrikkelenhet, name="Bruksenhet_er_tilknyttet_matrikkelenhet", curie=NGRE.curie('erTilknyttetMatrikkelenhet'),
                   model_uri=DEFAULT_.Bruksenhet_er_tilknyttet_matrikkelenhet, domain=Bruksenhet, range=Optional[Union[str, MatrikkelenhetId]])

slots.Bruksenhet_har_offisiell_adresse = Slot(uri=NGRE.harOffisiellAdresse, name="Bruksenhet_har_offisiell_adresse", curie=NGRE.curie('harOffisiellAdresse'),
                   model_uri=DEFAULT_.Bruksenhet_har_offisiell_adresse, domain=Bruksenhet, range=Optional[Union[str, OffisiellAdresseId]])

slots.Bruksenhetsnummer_etasjeplan = Slot(uri=NGRE.etasjeplan, name="Bruksenhetsnummer_etasjeplan", curie=NGRE.curie('etasjeplan'),
                   model_uri=DEFAULT_.Bruksenhetsnummer_etasjeplan, domain=Bruksenhetsnummer, range=Union[str, "Etasjeplan"])

slots.Bruksenhetsnummer_etasjenummer = Slot(uri=NGRE.etasjenummer, name="Bruksenhetsnummer_etasjenummer", curie=NGRE.curie('etasjenummer'),
                   model_uri=DEFAULT_.Bruksenhetsnummer_etasjenummer, domain=Bruksenhetsnummer, range=int)

slots.Bruksenhetsnummer_nummerering_i_etasjen = Slot(uri=NGRE.nummereringIEtasjen, name="Bruksenhetsnummer_nummerering_i_etasjen", curie=NGRE.curie('nummereringIEtasjen'),
                   model_uri=DEFAULT_.Bruksenhetsnummer_nummerering_i_etasjen, domain=Bruksenhetsnummer, range=int)

slots.Etasje_etasjenummer = Slot(uri=NGRE.etasjenummer, name="Etasje_etasjenummer", curie=NGRE.curie('etasjenummer'),
                   model_uri=DEFAULT_.Etasje_etasjenummer, domain=Etasje, range=int)

slots.Eierforhold_gjelder_matrikkelenhet = Slot(uri=NGRE.gjelderMatrikkelenhet, name="Eierforhold_gjelder_matrikkelenhet", curie=NGRE.curie('gjelderMatrikkelenhet'),
                   model_uri=DEFAULT_.Eierforhold_gjelder_matrikkelenhet, domain=Eierforhold, range=Union[str, MatrikkelenhetId])

slots.Eierforhold_kan_gjelde_borettslagsandel = Slot(uri=NGRE.kanGjeldeBorettslagsandel, name="Eierforhold_kan_gjelde_borettslagsandel", curie=NGRE.curie('kanGjeldeBorettslagsandel'),
                   model_uri=DEFAULT_.Eierforhold_kan_gjelde_borettslagsandel, domain=Eierforhold, range=Optional[Union[str, BorettslagsandelId]])

slots.Eierforhold_gjelder_hjemmel_eiendomsrett = Slot(uri=NGRE.gjelderHjemmelEiendomsrett, name="Eierforhold_gjelder_hjemmel_eiendomsrett", curie=NGRE.curie('gjelderHjemmelEiendomsrett'),
                   model_uri=DEFAULT_.Eierforhold_gjelder_hjemmel_eiendomsrett, domain=Eierforhold, range=Optional[Union[str, HjemmelTilEiendomsrettId]])

slots.Eierforhold_gjelder_hjemmel_festerett = Slot(uri=NGRE.gjelderHjemmelFesterett, name="Eierforhold_gjelder_hjemmel_festerett", curie=NGRE.curie('gjelderHjemmelFesterett'),
                   model_uri=DEFAULT_.Eierforhold_gjelder_hjemmel_festerett, domain=Eierforhold, range=Optional[Union[str, HjemmelTilFesterettId]])

slots.Eierforhold_gjelder_hjemmel_framfesterett = Slot(uri=NGRE.gjelderHjemmelFramfesterett, name="Eierforhold_gjelder_hjemmel_framfesterett", curie=NGRE.curie('gjelderHjemmelFramfesterett'),
                   model_uri=DEFAULT_.Eierforhold_gjelder_hjemmel_framfesterett, domain=Eierforhold, range=Optional[Union[str, HjemmelTilFramfesterettId]])

slots.Hjemmel_har_andel = Slot(uri=NGRE.harAndel, name="Hjemmel_har_andel", curie=NGRE.curie('harAndel'),
                   model_uri=DEFAULT_.Hjemmel_har_andel, domain=Hjemmel, range=Union[Union[str, AndelId], list[Union[str, AndelId]]])

slots.Andel_har_rettighetshaver = Slot(uri=NGRE.harRettighetshaver, name="Andel_har_rettighetshaver", curie=NGRE.curie('harRettighetshaver'),
                   model_uri=DEFAULT_.Andel_har_rettighetshaver, domain=Andel, range=Union[Union[str, RettighetshaverId], list[Union[str, RettighetshaverId]]])

slots.Rettighetshaver_er_av_type_person = Slot(uri=NGRE.erAvTypePerson, name="Rettighetshaver_er_av_type_person", curie=NGRE.curie('erAvTypePerson'),
                   model_uri=DEFAULT_.Rettighetshaver_er_av_type_person, domain=Rettighetshaver, range=Optional[Union[str, PersonId]])

slots.Rettighetshaver_er_av_type_hovedenhet = Slot(uri=NGRE.erAvTypeHovedenhet, name="Rettighetshaver_er_av_type_hovedenhet", curie=NGRE.curie('erAvTypeHovedenhet'),
                   model_uri=DEFAULT_.Rettighetshaver_er_av_type_hovedenhet, domain=Rettighetshaver, range=Optional[Union[str, HovedenhetId]])

slots.Borettslag_er_av_type_hovedenhet = Slot(uri=NGRE.erAvTypeHovedenhet, name="Borettslag_er_av_type_hovedenhet", curie=NGRE.curie('erAvTypeHovedenhet'),
                   model_uri=DEFAULT_.Borettslag_er_av_type_hovedenhet, domain=Borettslag, range=Union[str, HovedenhetId])

slots.Kommune_kommunenummer_verdi = Slot(uri=NGRE.kommunenummer, name="Kommune_kommunenummer_verdi", curie=NGRE.curie('kommunenummer'),
                   model_uri=DEFAULT_.Kommune_kommunenummer_verdi, domain=Kommune, range=str)

