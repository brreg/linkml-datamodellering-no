# Auto generated from register-over-aksjeeiere-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-27T14:51:33
# Schema: register-over-aksjeeiere
#
# id: https://example.no/ontology/aksje-eierskap
# description: LinkML-modell for aksjeselskap, aksjar, eigarskap og eigarskapshendingar. Modellen er tilpassa RDF-generering, SHACL og Ontodia-visualisering.
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

from linkml_runtime.linkml_model.types import Date, Decimal, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Decimal, URIorCURIE, XSDDate

metamodel_version = "1.11.0"
version = None

# Namespaces
AKSJE = CurieNamespace('aksje', 'https://example.no/ontology/aksje#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://data.norge.no/oreg/register-over-aksjeeiere/')


# Types

# Class references
class AksjeselskapIdentifikator(URIorCURIE):
    pass


class AksjekapitalIdentifikator(URIorCURIE):
    pass


class AksjeIdentifikator(URIorCURIE):
    pass


class AksjeklasseIdentifikator(URIorCURIE):
    pass


class AksjeeierrettighetIdentifikator(URIorCURIE):
    pass


class AksjeeierIdentifikator(URIorCURIE):
    pass


class EierposisjonIdentifikator(URIorCURIE):
    pass


class AksjepostIdentifikator(URIorCURIE):
    pass


class UtbytteIdentifikator(URIorCURIE):
    pass


class UtdelingIdentifikator(URIorCURIE):
    pass


class EierskapstransaksjonIdentifikator(URIorCURIE):
    pass


class AksjeoverdragelseIdentifikator(URIorCURIE):
    pass


class VederlagIdentifikator(URIorCURIE):
    pass


class SelskapshendelseIdentifikator(URIorCURIE):
    pass


class AksjeinnskuddIdentifikator(URIorCURIE):
    pass


@dataclass(repr=False)
class AksjeeierContainer(YAMLRoot):
    """
    Containerklasse for alle forretningsobjekt i modellen. Gjer det mogleg å ha fleire instansar av kvar klasse i ei
    datafil.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "AksjeeierContainer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/AksjeeierContainer")

    aksjeselskaper: Optional[Union[dict[Union[str, AksjeselskapIdentifikator], Union[dict, "Aksjeselskap"]], list[Union[dict, "Aksjeselskap"]]]] = empty_dict()
    aksjekapitaler: Optional[Union[dict[Union[str, AksjekapitalIdentifikator], Union[dict, "Aksjekapital"]], list[Union[dict, "Aksjekapital"]]]] = empty_dict()
    aksjer: Optional[Union[dict[Union[str, AksjeIdentifikator], Union[dict, "Aksje"]], list[Union[dict, "Aksje"]]]] = empty_dict()
    aksjeklasser: Optional[Union[dict[Union[str, AksjeklasseIdentifikator], Union[dict, "Aksjeklasse"]], list[Union[dict, "Aksjeklasse"]]]] = empty_dict()
    aksjeeierrettigheter: Optional[Union[dict[Union[str, AksjeeierrettighetIdentifikator], Union[dict, "Aksjeeierrettighet"]], list[Union[dict, "Aksjeeierrettighet"]]]] = empty_dict()
    aksjeeiere: Optional[Union[dict[Union[str, AksjeeierIdentifikator], Union[dict, "Aksjeeier"]], list[Union[dict, "Aksjeeier"]]]] = empty_dict()
    aksjeposter: Optional[Union[dict[Union[str, AksjepostIdentifikator], Union[dict, "Aksjepost"]], list[Union[dict, "Aksjepost"]]]] = empty_dict()
    eierposisjoner: Optional[Union[dict[Union[str, EierposisjonIdentifikator], Union[dict, "Eierposisjon"]], list[Union[dict, "Eierposisjon"]]]] = empty_dict()
    eierskapstransaksjoner: Optional[Union[dict[Union[str, EierskapstransaksjonIdentifikator], Union[dict, "Eierskapstransaksjon"]], list[Union[dict, "Eierskapstransaksjon"]]]] = empty_dict()
    aksjeoverdragelser: Optional[Union[dict[Union[str, AksjeoverdragelseIdentifikator], Union[dict, "Aksjeoverdragelse"]], list[Union[dict, "Aksjeoverdragelse"]]]] = empty_dict()
    vederlager: Optional[Union[dict[Union[str, VederlagIdentifikator], Union[dict, "Vederlag"]], list[Union[dict, "Vederlag"]]]] = empty_dict()
    selskapshendelser: Optional[Union[dict[Union[str, SelskapshendelseIdentifikator], Union[dict, "Selskapshendelse"]], list[Union[dict, "Selskapshendelse"]]]] = empty_dict()
    aksjeinnskudder: Optional[Union[dict[Union[str, AksjeinnskuddIdentifikator], Union[dict, "Aksjeinnskudd"]], list[Union[dict, "Aksjeinnskudd"]]]] = empty_dict()
    utbytter: Optional[Union[dict[Union[str, UtbytteIdentifikator], Union[dict, "Utbytte"]], list[Union[dict, "Utbytte"]]]] = empty_dict()
    utdelinger: Optional[Union[dict[Union[str, UtdelingIdentifikator], Union[dict, "Utdeling"]], list[Union[dict, "Utdeling"]]]] = empty_dict()
    innbetalt_aksjekapitaler: Optional[Union[Union[dict, "InnbetaltAksjekapital"], list[Union[dict, "InnbetaltAksjekapital"]]]] = empty_list()
    innbetalt_overkurser: Optional[Union[Union[dict, "InnbetaltOverkurs"], list[Union[dict, "InnbetaltOverkurs"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="aksjeselskaper", slot_type=Aksjeselskap, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="aksjekapitaler", slot_type=Aksjekapital, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="aksjer", slot_type=Aksje, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="aksjeklasser", slot_type=Aksjeklasse, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="aksjeeierrettigheter", slot_type=Aksjeeierrettighet, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="aksjeeiere", slot_type=Aksjeeier, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="aksjeposter", slot_type=Aksjepost, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="eierposisjoner", slot_type=Eierposisjon, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="eierskapstransaksjoner", slot_type=Eierskapstransaksjon, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="aksjeoverdragelser", slot_type=Aksjeoverdragelse, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="vederlager", slot_type=Vederlag, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="selskapshendelser", slot_type=Selskapshendelse, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="aksjeinnskudder", slot_type=Aksjeinnskudd, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="utbytter", slot_type=Utbytte, key_name="identifikator", keyed=True)

        self._normalize_inlined_as_list(slot_name="utdelinger", slot_type=Utdeling, key_name="identifikator", keyed=True)

        if not isinstance(self.innbetalt_aksjekapitaler, list):
            self.innbetalt_aksjekapitaler = [self.innbetalt_aksjekapitaler] if self.innbetalt_aksjekapitaler is not None else []
        self.innbetalt_aksjekapitaler = [v if isinstance(v, InnbetaltAksjekapital) else InnbetaltAksjekapital(**as_dict(v)) for v in self.innbetalt_aksjekapitaler]

        if not isinstance(self.innbetalt_overkurser, list):
            self.innbetalt_overkurser = [self.innbetalt_overkurser] if self.innbetalt_overkurser is not None else []
        self.innbetalt_overkurser = [v if isinstance(v, InnbetaltOverkurs) else InnbetaltOverkurs(**as_dict(v)) for v in self.innbetalt_overkurser]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aksjeselskap(YAMLRoot):
    """
    Selskap som utsteder aksjar og har aksjekapital.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjeselskap")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Aksjeselskap"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjeselskap")

    identifikator: Union[str, AksjeselskapIdentifikator] = None
    navn: Optional[str] = None
    har_aksjekapital: Optional[Union[str, AksjekapitalIdentifikator]] = None
    utsteder_aksje: Optional[Union[str, AksjeIdentifikator]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, AksjeselskapIdentifikator):
            self.identifikator = AksjeselskapIdentifikator(self.identifikator)

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.har_aksjekapital is not None and not isinstance(self.har_aksjekapital, AksjekapitalIdentifikator):
            self.har_aksjekapital = AksjekapitalIdentifikator(self.har_aksjekapital)

        if self.utsteder_aksje is not None and not isinstance(self.utsteder_aksje, AksjeIdentifikator):
            self.utsteder_aksje = AksjeIdentifikator(self.utsteder_aksje)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aksjekapital(YAMLRoot):
    """
    Den registrerte aksjekapitalen i eit aksjeselskap.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjekapital")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Aksjekapital"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjekapital")

    identifikator: Union[str, AksjekapitalIdentifikator] = None
    har_antall_aksjer: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, AksjekapitalIdentifikator):
            self.identifikator = AksjekapitalIdentifikator(self.identifikator)

        if self.har_antall_aksjer is not None and not isinstance(self.har_antall_aksjer, int):
            self.har_antall_aksjer = int(self.har_antall_aksjer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aksje(YAMLRoot):
    """
    Ei enkelt aksje utstedt av eit aksjeselskap.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksje")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Aksje"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksje")

    identifikator: Union[str, AksjeIdentifikator] = None
    har_palydende_belop: Optional[Decimal] = None
    tilhorer_aksjeklasse: Optional[Union[str, AksjeklasseIdentifikator]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, AksjeIdentifikator):
            self.identifikator = AksjeIdentifikator(self.identifikator)

        if self.har_palydende_belop is not None and not isinstance(self.har_palydende_belop, Decimal):
            self.har_palydende_belop = Decimal(self.har_palydende_belop)

        if self.tilhorer_aksjeklasse is not None and not isinstance(self.tilhorer_aksjeklasse, AksjeklasseIdentifikator):
            self.tilhorer_aksjeklasse = AksjeklasseIdentifikator(self.tilhorer_aksjeklasse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aksjeklasse(YAMLRoot):
    """
    Klasse aksjar høyrer til, med eigne rettigheiter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjeklasse")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Aksjeklasse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjeklasse")

    identifikator: Union[str, AksjeklasseIdentifikator] = None
    navn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, AksjeklasseIdentifikator):
            self.identifikator = AksjeklasseIdentifikator(self.identifikator)

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aksjeeierrettighet(YAMLRoot):
    """
    Rettigheiter knytt til aksjar, til dømes stemmerett.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjeeierrettighet")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Aksjeeierrettighet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjeeierrettighet")

    identifikator: Union[str, AksjeeierrettighetIdentifikator] = None
    beskrivelse: Optional[str] = None
    gjelder_aksjer_i_aksjeklasse: Optional[Union[str, AksjeklasseIdentifikator]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, AksjeeierrettighetIdentifikator):
            self.identifikator = AksjeeierrettighetIdentifikator(self.identifikator)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if self.gjelder_aksjer_i_aksjeklasse is not None and not isinstance(self.gjelder_aksjer_i_aksjeklasse, AksjeklasseIdentifikator):
            self.gjelder_aksjer_i_aksjeklasse = AksjeklasseIdentifikator(self.gjelder_aksjer_i_aksjeklasse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aksjeeier(YAMLRoot):
    """
    Person eller organisasjon som eig aksjar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjeeier")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Aksjeeier"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjeeier")

    identifikator: Union[str, AksjeeierIdentifikator] = None
    navn: Optional[str] = None
    har_eierposisjon: Optional[Union[str, EierposisjonIdentifikator]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, AksjeeierIdentifikator):
            self.identifikator = AksjeeierIdentifikator(self.identifikator)

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.har_eierposisjon is not None and not isinstance(self.har_eierposisjon, EierposisjonIdentifikator):
            self.har_eierposisjon = EierposisjonIdentifikator(self.har_eierposisjon)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Eierposisjon(YAMLRoot):
    """
    Eierens samla posisjon i eit selskap.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Eierposisjon")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Eierposisjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Eierposisjon")

    identifikator: Union[str, EierposisjonIdentifikator] = None
    gjelder_aksjepost: Optional[Union[str, AksjepostIdentifikator]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, EierposisjonIdentifikator):
            self.identifikator = EierposisjonIdentifikator(self.identifikator)

        if self.gjelder_aksjepost is not None and not isinstance(self.gjelder_aksjepost, AksjepostIdentifikator):
            self.gjelder_aksjepost = AksjepostIdentifikator(self.gjelder_aksjepost)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aksjepost(YAMLRoot):
    """
    Samling aksjar eigd av ein aksjeeigar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjepost")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Aksjepost"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjepost")

    identifikator: Union[str, AksjepostIdentifikator] = None
    har_antall_aksjer: Optional[int] = None
    gjelder_aksjer_i_aksjeklasse: Optional[Union[str, AksjeklasseIdentifikator]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, AksjepostIdentifikator):
            self.identifikator = AksjepostIdentifikator(self.identifikator)

        if self.har_antall_aksjer is not None and not isinstance(self.har_antall_aksjer, int):
            self.har_antall_aksjer = int(self.har_antall_aksjer)

        if self.gjelder_aksjer_i_aksjeklasse is not None and not isinstance(self.gjelder_aksjer_i_aksjeklasse, AksjeklasseIdentifikator):
            self.gjelder_aksjer_i_aksjeklasse = AksjeklasseIdentifikator(self.gjelder_aksjer_i_aksjeklasse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Utbytte(YAMLRoot):
    """
    Utbytte knytt til ein eigarposisjon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Utbytte")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Utbytte"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Utbytte")

    identifikator: Union[str, UtbytteIdentifikator] = None
    tidspunkt: Optional[Union[str, XSDDate]] = None
    har_utdeling: Optional[Union[str, UtdelingIdentifikator]] = None
    er_basert_paa_eierposisjon: Optional[Union[str, EierposisjonIdentifikator]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, UtbytteIdentifikator):
            self.identifikator = UtbytteIdentifikator(self.identifikator)

        if self.tidspunkt is not None and not isinstance(self.tidspunkt, XSDDate):
            self.tidspunkt = XSDDate(self.tidspunkt)

        if self.har_utdeling is not None and not isinstance(self.har_utdeling, UtdelingIdentifikator):
            self.har_utdeling = UtdelingIdentifikator(self.har_utdeling)

        if self.er_basert_paa_eierposisjon is not None and not isinstance(self.er_basert_paa_eierposisjon, EierposisjonIdentifikator):
            self.er_basert_paa_eierposisjon = EierposisjonIdentifikator(self.er_basert_paa_eierposisjon)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Utdeling(YAMLRoot):
    """
    Konkret utdeling av verdiar til aksjeeigarar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Utdeling")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Utdeling"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Utdeling")

    identifikator: Union[str, UtdelingIdentifikator] = None
    belop: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, UtdelingIdentifikator):
            self.identifikator = UtdelingIdentifikator(self.identifikator)

        if self.belop is not None and not isinstance(self.belop, Decimal):
            self.belop = Decimal(self.belop)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tidspunkt(YAMLRoot):
    """
    Tidspunkt for ei hending.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Tidspunkt")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Tidspunkt"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Tidspunkt")

    dato: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.dato is not None and not isinstance(self.dato, XSDDate):
            self.dato = XSDDate(self.dato)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Eierskapstransaksjon(YAMLRoot):
    """
    Transaksjon som påverkar eigarskap i selskapet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Eierskapstransaksjon")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Eierskapstransaksjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Eierskapstransaksjon")

    identifikator: Union[str, EierskapstransaksjonIdentifikator] = None
    tidspunkt: Optional[Union[str, XSDDate]] = None
    kan_vaere_aksjeoverdragelse: Optional[Union[str, AksjeoverdragelseIdentifikator]] = None
    kan_vaere_selskapshendelse: Optional[Union[str, SelskapshendelseIdentifikator]] = None
    paavirker_eierposisjon: Optional[Union[str, EierposisjonIdentifikator]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, EierskapstransaksjonIdentifikator):
            self.identifikator = EierskapstransaksjonIdentifikator(self.identifikator)

        if self.tidspunkt is not None and not isinstance(self.tidspunkt, XSDDate):
            self.tidspunkt = XSDDate(self.tidspunkt)

        if self.kan_vaere_aksjeoverdragelse is not None and not isinstance(self.kan_vaere_aksjeoverdragelse, AksjeoverdragelseIdentifikator):
            self.kan_vaere_aksjeoverdragelse = AksjeoverdragelseIdentifikator(self.kan_vaere_aksjeoverdragelse)

        if self.kan_vaere_selskapshendelse is not None and not isinstance(self.kan_vaere_selskapshendelse, SelskapshendelseIdentifikator):
            self.kan_vaere_selskapshendelse = SelskapshendelseIdentifikator(self.kan_vaere_selskapshendelse)

        if self.paavirker_eierposisjon is not None and not isinstance(self.paavirker_eierposisjon, EierposisjonIdentifikator):
            self.paavirker_eierposisjon = EierposisjonIdentifikator(self.paavirker_eierposisjon)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aksjeoverdragelse(YAMLRoot):
    """
    Overdraging av aksjar mellom partar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjeoverdragelse")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Aksjeoverdragelse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjeoverdragelse")

    identifikator: Union[str, AksjeoverdragelseIdentifikator] = None
    kan_ha_vederlag: Optional[Union[str, VederlagIdentifikator]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, AksjeoverdragelseIdentifikator):
            self.identifikator = AksjeoverdragelseIdentifikator(self.identifikator)

        if self.kan_ha_vederlag is not None and not isinstance(self.kan_ha_vederlag, VederlagIdentifikator):
            self.kan_ha_vederlag = VederlagIdentifikator(self.kan_ha_vederlag)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Vederlag(YAMLRoot):
    """
    Vederlag knytt til ei aksjeoverdraging.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Vederlag")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Vederlag"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Vederlag")

    identifikator: Union[str, VederlagIdentifikator] = None
    belop: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, VederlagIdentifikator):
            self.identifikator = VederlagIdentifikator(self.identifikator)

        if self.belop is not None and not isinstance(self.belop, Decimal):
            self.belop = Decimal(self.belop)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Selskapshendelse(YAMLRoot):
    """
    Hending som påverkar selskapet sitt eigarskap eller kapital.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Selskapshendelse")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Selskapshendelse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Selskapshendelse")

    identifikator: Union[str, SelskapshendelseIdentifikator] = None
    kan_ha_aksjeinnskudd: Optional[Union[str, AksjeinnskuddIdentifikator]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, SelskapshendelseIdentifikator):
            self.identifikator = SelskapshendelseIdentifikator(self.identifikator)

        if self.kan_ha_aksjeinnskudd is not None and not isinstance(self.kan_ha_aksjeinnskudd, AksjeinnskuddIdentifikator):
            self.kan_ha_aksjeinnskudd = AksjeinnskuddIdentifikator(self.kan_ha_aksjeinnskudd)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aksjeinnskudd(YAMLRoot):
    """
    Innskot knytt til aksjar i samband med selskapshending.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjeinnskudd")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Aksjeinnskudd"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/Aksjeinnskudd")

    identifikator: Union[str, AksjeinnskuddIdentifikator] = None
    gjelder_innbetalt_aksjekapital: Optional[Decimal] = None
    gjelder_innbetalt_overkurs: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifikator):
            self.MissingRequiredField("identifikator")
        if not isinstance(self.identifikator, AksjeinnskuddIdentifikator):
            self.identifikator = AksjeinnskuddIdentifikator(self.identifikator)

        if self.gjelder_innbetalt_aksjekapital is not None and not isinstance(self.gjelder_innbetalt_aksjekapital, Decimal):
            self.gjelder_innbetalt_aksjekapital = Decimal(self.gjelder_innbetalt_aksjekapital)

        if self.gjelder_innbetalt_overkurs is not None and not isinstance(self.gjelder_innbetalt_overkurs, Decimal):
            self.gjelder_innbetalt_overkurs = Decimal(self.gjelder_innbetalt_overkurs)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InnbetaltAksjekapital(YAMLRoot):
    """
    Innbetalt aksjekapital.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/InnbetaltAksjekapital")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "InnbetaltAksjekapital"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/InnbetaltAksjekapital")

    belop: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.belop is not None and not isinstance(self.belop, Decimal):
            self.belop = Decimal(self.belop)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InnbetaltOverkurs(YAMLRoot):
    """
    Innbetalt overkurs utover pålydande.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/InnbetaltOverkurs")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "InnbetaltOverkurs"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/oreg/register-over-aksjeeiere/InnbetaltOverkurs")

    belop: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.belop is not None and not isinstance(self.belop, Decimal):
            self.belop = Decimal(self.belop)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.identifikator = Slot(uri=DEFAULT_.identifikator, name="identifikator", curie=DEFAULT_.curie('identifikator'),
                   model_uri=DEFAULT_.identifikator, domain=None, range=URIRef)

slots.navn = Slot(uri=DEFAULT_.navn, name="navn", curie=DEFAULT_.curie('navn'),
                   model_uri=DEFAULT_.navn, domain=None, range=Optional[str])

slots.beskrivelse = Slot(uri=DEFAULT_.beskrivelse, name="beskrivelse", curie=DEFAULT_.curie('beskrivelse'),
                   model_uri=DEFAULT_.beskrivelse, domain=None, range=Optional[str])

slots.antall = Slot(uri=DEFAULT_.antall, name="antall", curie=DEFAULT_.curie('antall'),
                   model_uri=DEFAULT_.antall, domain=None, range=Optional[int])

slots.belop = Slot(uri=DEFAULT_.belop, name="belop", curie=DEFAULT_.curie('belop'),
                   model_uri=DEFAULT_.belop, domain=None, range=Optional[Decimal])

slots.dato = Slot(uri=DEFAULT_.dato, name="dato", curie=DEFAULT_.curie('dato'),
                   model_uri=DEFAULT_.dato, domain=None, range=Optional[Union[str, XSDDate]])

slots.har_aksjekapital = Slot(uri=DEFAULT_.har_aksjekapital, name="har_aksjekapital", curie=DEFAULT_.curie('har_aksjekapital'),
                   model_uri=DEFAULT_.har_aksjekapital, domain=Aksjeselskap, range=Optional[Union[str, AksjekapitalIdentifikator]])

slots.har_antall_aksjer = Slot(uri=DEFAULT_.har_antall_aksjer, name="har_antall_aksjer", curie=DEFAULT_.curie('har_antall_aksjer'),
                   model_uri=DEFAULT_.har_antall_aksjer, domain=None, range=Optional[int])

slots.utsteder_aksje = Slot(uri=DEFAULT_.utsteder_aksje, name="utsteder_aksje", curie=DEFAULT_.curie('utsteder_aksje'),
                   model_uri=DEFAULT_.utsteder_aksje, domain=Aksjeselskap, range=Optional[Union[str, AksjeIdentifikator]])

slots.har_palydende_belop = Slot(uri=DEFAULT_.har_palydende_belop, name="har_palydende_belop", curie=DEFAULT_.curie('har_palydende_belop'),
                   model_uri=DEFAULT_.har_palydende_belop, domain=Aksje, range=Optional[Decimal])

slots.tilhorer_aksjeklasse = Slot(uri=DEFAULT_.tilhorer_aksjeklasse, name="tilhorer_aksjeklasse", curie=DEFAULT_.curie('tilhorer_aksjeklasse'),
                   model_uri=DEFAULT_.tilhorer_aksjeklasse, domain=Aksje, range=Optional[Union[str, AksjeklasseIdentifikator]])

slots.gjelder_aksjer_i_aksjeklasse = Slot(uri=DEFAULT_.gjelder_aksjer_i_aksjeklasse, name="gjelder_aksjer_i_aksjeklasse", curie=DEFAULT_.curie('gjelder_aksjer_i_aksjeklasse'),
                   model_uri=DEFAULT_.gjelder_aksjer_i_aksjeklasse, domain=None, range=Optional[Union[str, AksjeklasseIdentifikator]])

slots.har_eierposisjon = Slot(uri=DEFAULT_.har_eierposisjon, name="har_eierposisjon", curie=DEFAULT_.curie('har_eierposisjon'),
                   model_uri=DEFAULT_.har_eierposisjon, domain=Aksjeeier, range=Optional[Union[str, EierposisjonIdentifikator]])

slots.gjelder_aksjepost = Slot(uri=DEFAULT_.gjelder_aksjepost, name="gjelder_aksjepost", curie=DEFAULT_.curie('gjelder_aksjepost'),
                   model_uri=DEFAULT_.gjelder_aksjepost, domain=Eierposisjon, range=Optional[Union[str, AksjepostIdentifikator]])

slots.er_basert_paa_eierposisjon = Slot(uri=DEFAULT_.er_basert_paa_eierposisjon, name="er_basert_paa_eierposisjon", curie=DEFAULT_.curie('er_basert_paa_eierposisjon'),
                   model_uri=DEFAULT_.er_basert_paa_eierposisjon, domain=Utbytte, range=Optional[Union[str, EierposisjonIdentifikator]])

slots.paavirker_eierposisjon = Slot(uri=DEFAULT_.paavirker_eierposisjon, name="paavirker_eierposisjon", curie=DEFAULT_.curie('paavirker_eierposisjon'),
                   model_uri=DEFAULT_.paavirker_eierposisjon, domain=Eierskapstransaksjon, range=Optional[Union[str, EierposisjonIdentifikator]])

slots.har_utdeling = Slot(uri=DEFAULT_.har_utdeling, name="har_utdeling", curie=DEFAULT_.curie('har_utdeling'),
                   model_uri=DEFAULT_.har_utdeling, domain=Utbytte, range=Optional[Union[str, UtdelingIdentifikator]])

slots.tidspunkt = Slot(uri=DEFAULT_.tidspunkt, name="tidspunkt", curie=DEFAULT_.curie('tidspunkt'),
                   model_uri=DEFAULT_.tidspunkt, domain=None, range=Optional[Union[str, XSDDate]])

slots.kan_vaere_aksjeoverdragelse = Slot(uri=DEFAULT_.kan_vaere_aksjeoverdragelse, name="kan_vaere_aksjeoverdragelse", curie=DEFAULT_.curie('kan_vaere_aksjeoverdragelse'),
                   model_uri=DEFAULT_.kan_vaere_aksjeoverdragelse, domain=Eierskapstransaksjon, range=Optional[Union[str, AksjeoverdragelseIdentifikator]])

slots.kan_vaere_selskapshendelse = Slot(uri=DEFAULT_.kan_vaere_selskapshendelse, name="kan_vaere_selskapshendelse", curie=DEFAULT_.curie('kan_vaere_selskapshendelse'),
                   model_uri=DEFAULT_.kan_vaere_selskapshendelse, domain=Eierskapstransaksjon, range=Optional[Union[str, SelskapshendelseIdentifikator]])

slots.kan_ha_vederlag = Slot(uri=DEFAULT_.kan_ha_vederlag, name="kan_ha_vederlag", curie=DEFAULT_.curie('kan_ha_vederlag'),
                   model_uri=DEFAULT_.kan_ha_vederlag, domain=Aksjeoverdragelse, range=Optional[Union[str, VederlagIdentifikator]])

slots.kan_ha_aksjeinnskudd = Slot(uri=DEFAULT_.kan_ha_aksjeinnskudd, name="kan_ha_aksjeinnskudd", curie=DEFAULT_.curie('kan_ha_aksjeinnskudd'),
                   model_uri=DEFAULT_.kan_ha_aksjeinnskudd, domain=Selskapshendelse, range=Optional[Union[str, AksjeinnskuddIdentifikator]])

slots.gjelder_innbetalt_aksjekapital = Slot(uri=DEFAULT_.gjelder_innbetalt_aksjekapital, name="gjelder_innbetalt_aksjekapital", curie=DEFAULT_.curie('gjelder_innbetalt_aksjekapital'),
                   model_uri=DEFAULT_.gjelder_innbetalt_aksjekapital, domain=Aksjeinnskudd, range=Optional[Decimal])

slots.gjelder_innbetalt_overkurs = Slot(uri=DEFAULT_.gjelder_innbetalt_overkurs, name="gjelder_innbetalt_overkurs", curie=DEFAULT_.curie('gjelder_innbetalt_overkurs'),
                   model_uri=DEFAULT_.gjelder_innbetalt_overkurs, domain=Aksjeinnskudd, range=Optional[Decimal])

slots.aksjeeierContainer__aksjeselskaper = Slot(uri=DEFAULT_.aksjeselskaper, name="aksjeeierContainer__aksjeselskaper", curie=DEFAULT_.curie('aksjeselskaper'),
                   model_uri=DEFAULT_.aksjeeierContainer__aksjeselskaper, domain=None, range=Optional[Union[dict[Union[str, AksjeselskapIdentifikator], Union[dict, Aksjeselskap]], list[Union[dict, Aksjeselskap]]]])

slots.aksjeeierContainer__aksjekapitaler = Slot(uri=DEFAULT_.aksjekapitaler, name="aksjeeierContainer__aksjekapitaler", curie=DEFAULT_.curie('aksjekapitaler'),
                   model_uri=DEFAULT_.aksjeeierContainer__aksjekapitaler, domain=None, range=Optional[Union[dict[Union[str, AksjekapitalIdentifikator], Union[dict, Aksjekapital]], list[Union[dict, Aksjekapital]]]])

slots.aksjeeierContainer__aksjer = Slot(uri=DEFAULT_.aksjer, name="aksjeeierContainer__aksjer", curie=DEFAULT_.curie('aksjer'),
                   model_uri=DEFAULT_.aksjeeierContainer__aksjer, domain=None, range=Optional[Union[dict[Union[str, AksjeIdentifikator], Union[dict, Aksje]], list[Union[dict, Aksje]]]])

slots.aksjeeierContainer__aksjeklasser = Slot(uri=DEFAULT_.aksjeklasser, name="aksjeeierContainer__aksjeklasser", curie=DEFAULT_.curie('aksjeklasser'),
                   model_uri=DEFAULT_.aksjeeierContainer__aksjeklasser, domain=None, range=Optional[Union[dict[Union[str, AksjeklasseIdentifikator], Union[dict, Aksjeklasse]], list[Union[dict, Aksjeklasse]]]])

slots.aksjeeierContainer__aksjeeierrettigheter = Slot(uri=DEFAULT_.aksjeeierrettigheter, name="aksjeeierContainer__aksjeeierrettigheter", curie=DEFAULT_.curie('aksjeeierrettigheter'),
                   model_uri=DEFAULT_.aksjeeierContainer__aksjeeierrettigheter, domain=None, range=Optional[Union[dict[Union[str, AksjeeierrettighetIdentifikator], Union[dict, Aksjeeierrettighet]], list[Union[dict, Aksjeeierrettighet]]]])

slots.aksjeeierContainer__aksjeeiere = Slot(uri=DEFAULT_.aksjeeiere, name="aksjeeierContainer__aksjeeiere", curie=DEFAULT_.curie('aksjeeiere'),
                   model_uri=DEFAULT_.aksjeeierContainer__aksjeeiere, domain=None, range=Optional[Union[dict[Union[str, AksjeeierIdentifikator], Union[dict, Aksjeeier]], list[Union[dict, Aksjeeier]]]])

slots.aksjeeierContainer__aksjeposter = Slot(uri=DEFAULT_.aksjeposter, name="aksjeeierContainer__aksjeposter", curie=DEFAULT_.curie('aksjeposter'),
                   model_uri=DEFAULT_.aksjeeierContainer__aksjeposter, domain=None, range=Optional[Union[dict[Union[str, AksjepostIdentifikator], Union[dict, Aksjepost]], list[Union[dict, Aksjepost]]]])

slots.aksjeeierContainer__eierposisjoner = Slot(uri=DEFAULT_.eierposisjoner, name="aksjeeierContainer__eierposisjoner", curie=DEFAULT_.curie('eierposisjoner'),
                   model_uri=DEFAULT_.aksjeeierContainer__eierposisjoner, domain=None, range=Optional[Union[dict[Union[str, EierposisjonIdentifikator], Union[dict, Eierposisjon]], list[Union[dict, Eierposisjon]]]])

slots.aksjeeierContainer__eierskapstransaksjoner = Slot(uri=DEFAULT_.eierskapstransaksjoner, name="aksjeeierContainer__eierskapstransaksjoner", curie=DEFAULT_.curie('eierskapstransaksjoner'),
                   model_uri=DEFAULT_.aksjeeierContainer__eierskapstransaksjoner, domain=None, range=Optional[Union[dict[Union[str, EierskapstransaksjonIdentifikator], Union[dict, Eierskapstransaksjon]], list[Union[dict, Eierskapstransaksjon]]]])

slots.aksjeeierContainer__aksjeoverdragelser = Slot(uri=DEFAULT_.aksjeoverdragelser, name="aksjeeierContainer__aksjeoverdragelser", curie=DEFAULT_.curie('aksjeoverdragelser'),
                   model_uri=DEFAULT_.aksjeeierContainer__aksjeoverdragelser, domain=None, range=Optional[Union[dict[Union[str, AksjeoverdragelseIdentifikator], Union[dict, Aksjeoverdragelse]], list[Union[dict, Aksjeoverdragelse]]]])

slots.aksjeeierContainer__vederlager = Slot(uri=DEFAULT_.vederlager, name="aksjeeierContainer__vederlager", curie=DEFAULT_.curie('vederlager'),
                   model_uri=DEFAULT_.aksjeeierContainer__vederlager, domain=None, range=Optional[Union[dict[Union[str, VederlagIdentifikator], Union[dict, Vederlag]], list[Union[dict, Vederlag]]]])

slots.aksjeeierContainer__selskapshendelser = Slot(uri=DEFAULT_.selskapshendelser, name="aksjeeierContainer__selskapshendelser", curie=DEFAULT_.curie('selskapshendelser'),
                   model_uri=DEFAULT_.aksjeeierContainer__selskapshendelser, domain=None, range=Optional[Union[dict[Union[str, SelskapshendelseIdentifikator], Union[dict, Selskapshendelse]], list[Union[dict, Selskapshendelse]]]])

slots.aksjeeierContainer__aksjeinnskudder = Slot(uri=DEFAULT_.aksjeinnskudder, name="aksjeeierContainer__aksjeinnskudder", curie=DEFAULT_.curie('aksjeinnskudder'),
                   model_uri=DEFAULT_.aksjeeierContainer__aksjeinnskudder, domain=None, range=Optional[Union[dict[Union[str, AksjeinnskuddIdentifikator], Union[dict, Aksjeinnskudd]], list[Union[dict, Aksjeinnskudd]]]])

slots.aksjeeierContainer__utbytter = Slot(uri=DEFAULT_.utbytter, name="aksjeeierContainer__utbytter", curie=DEFAULT_.curie('utbytter'),
                   model_uri=DEFAULT_.aksjeeierContainer__utbytter, domain=None, range=Optional[Union[dict[Union[str, UtbytteIdentifikator], Union[dict, Utbytte]], list[Union[dict, Utbytte]]]])

slots.aksjeeierContainer__utdelinger = Slot(uri=DEFAULT_.utdelinger, name="aksjeeierContainer__utdelinger", curie=DEFAULT_.curie('utdelinger'),
                   model_uri=DEFAULT_.aksjeeierContainer__utdelinger, domain=None, range=Optional[Union[dict[Union[str, UtdelingIdentifikator], Union[dict, Utdeling]], list[Union[dict, Utdeling]]]])

slots.aksjeeierContainer__innbetalt_aksjekapitaler = Slot(uri=DEFAULT_.innbetalt_aksjekapitaler, name="aksjeeierContainer__innbetalt_aksjekapitaler", curie=DEFAULT_.curie('innbetalt_aksjekapitaler'),
                   model_uri=DEFAULT_.aksjeeierContainer__innbetalt_aksjekapitaler, domain=None, range=Optional[Union[Union[dict, InnbetaltAksjekapital], list[Union[dict, InnbetaltAksjekapital]]]])

slots.aksjeeierContainer__innbetalt_overkurser = Slot(uri=DEFAULT_.innbetalt_overkurser, name="aksjeeierContainer__innbetalt_overkurser", curie=DEFAULT_.curie('innbetalt_overkurser'),
                   model_uri=DEFAULT_.aksjeeierContainer__innbetalt_overkurser, domain=None, range=Optional[Union[Union[dict, InnbetaltOverkurs], list[Union[dict, InnbetaltOverkurs]]]])

