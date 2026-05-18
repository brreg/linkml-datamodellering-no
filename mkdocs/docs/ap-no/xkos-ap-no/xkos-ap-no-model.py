# Auto generated from xkos-ap-no-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-18T09:10:40
# Schema: xkos-ap-no
#
# id: https://data.norge.no/linkml/xkos-ap-no
# description: LinkML-modell for XKOS-AP-NO – norsk applikasjonsprofil for utvida SKOS-klassifikasjonar. Basert på https://data.norge.no/specification/xkos-ap-no
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

from linkml_runtime.linkml_model.types import Date, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms#')
CAPNO = CurieNamespace('capno', 'https://data.norge.no/linkml/common-ap-no/')
CV = CurieNamespace('cv', 'http://data.europa.eu/m8g/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
UNESKOS = CurieNamespace('uneskos', 'http://purl.org/umu/uneskos#')
XKOS = CurieNamespace('xkos', 'http://rdf-vocabulary.ddialliance.org/xkos#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://data.norge.no/linkml/xkos-ap-no/')


# Types
class Spraak(str):
    """ Språk """
    type_class_uri = DCT["language"]
    type_class_curie = "dct:language"
    type_name = "Spraak"
    type_model_uri = URIRef("https://data.norge.no/linkml/xkos-ap-no/Spraak")


class LangString(str):
    """ Språktagget streng (rdf:langString). """
    type_class_uri = RDF["langString"]
    type_class_curie = "rdf:langString"
    type_name = "LangString"
    type_model_uri = URIRef("https://data.norge.no/linkml/xkos-ap-no/LangString")


class NonNegativeInteger(int):
    """ Ikkje-negativ heltalsverdi (xsd:nonNegativeInteger). """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "NonNegativeInteger"
    type_model_uri = URIRef("https://data.norge.no/linkml/xkos-ap-no/NonNegativeInteger")


class Duration(str):
    """ ISO 8601-varigheit (xsd:duration), t.d. PT15M. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "Duration"
    type_model_uri = URIRef("https://data.norge.no/linkml/xkos-ap-no/Duration")


class GYear(str):
    """ Gregorisk årstal (xsd:gYear), t.d. 2024. """
    type_class_uri = XSD["gYear"]
    type_class_curie = "xsd:gYear"
    type_name = "GYear"
    type_model_uri = URIRef("https://data.norge.no/linkml/xkos-ap-no/GYear")


# Class references
class KlassifikasjonId(URIorCURIE):
    pass


class KlassifikasjonsnivaaId(URIorCURIE):
    pass


class KategoriId(URIorCURIE):
    pass


class KlassifikasjonssamanlikningId(URIorCURIE):
    pass


class KategorisamanlikningId(URIorCURIE):
    pass


class OrganisasjonId(URIorCURIE):
    pass


class TidsromId(URIorCURIE):
    pass


class MediatypeId(URIorCURIE):
    pass


class KonseptId(URIorCURIE):
    pass


class BegrepssamlingId(URIorCURIE):
    pass


@dataclass(repr=False)
class Klassifikasjon(YAMLRoot):
    """
    Ei klassifikasjon – ein systematisk struktur av kategoriar brukt til å klassifisere data (skos:ConceptScheme).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["ConceptScheme"]
    class_class_curie: ClassVar[str] = "skos:ConceptScheme"
    class_name: ClassVar[str] = "Klassifikasjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/xkos-ap-no/Klassifikasjon")

    id: Union[str, KlassifikasjonId] = None
    identifikator_literal: str = None
    tittel: Union[str, list[str]] = None
    utgjevar: Union[str, OrganisasjonId] = None
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()
    tema: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    nokkelord: Optional[Union[str, list[str]]] = empty_list()
    spraak: Optional[Union[str, list[str]]] = empty_list()
    har_versjonsnummer: Optional[str] = None
    endringsdato: Optional[Union[str, XSDDate]] = None
    utgivelsesdato: Optional[Union[str, XSDDate]] = None
    heimeside: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    gjeld_for_tidsrom: Optional[Union[str, TidsromId]] = None
    antall_nivaa: Optional[int] = None
    er_samanlikna_med: Optional[Union[Union[str, KlassifikasjonId], list[Union[str, KlassifikasjonId]]]] = empty_list()
    forste_nivaa: Optional[Union[Union[str, KlassifikasjonsnivaaId], list[Union[str, KlassifikasjonsnivaaId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KlassifikasjonId):
            self.id = KlassifikasjonId(self.id)

        if self._is_empty(self.identifikator_literal):
            self.MissingRequiredField("identifikator_literal")
        if not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.utgjevar):
            self.MissingRequiredField("utgjevar")
        if not isinstance(self.utgjevar, OrganisasjonId):
            self.utgjevar = OrganisasjonId(self.utgjevar)

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if not isinstance(self.tema, list):
            self.tema = [self.tema] if self.tema is not None else []
        self.tema = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.tema]

        if not isinstance(self.nokkelord, list):
            self.nokkelord = [self.nokkelord] if self.nokkelord is not None else []
        self.nokkelord = [v if isinstance(v, str) else str(v) for v in self.nokkelord]

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

        if self.har_versjonsnummer is not None and not isinstance(self.har_versjonsnummer, str):
            self.har_versjonsnummer = str(self.har_versjonsnummer)

        if self.endringsdato is not None and not isinstance(self.endringsdato, XSDDate):
            self.endringsdato = XSDDate(self.endringsdato)

        if self.utgivelsesdato is not None and not isinstance(self.utgivelsesdato, XSDDate):
            self.utgivelsesdato = XSDDate(self.utgivelsesdato)

        if not isinstance(self.heimeside, list):
            self.heimeside = [self.heimeside] if self.heimeside is not None else []
        self.heimeside = [v if isinstance(v, URI) else URI(v) for v in self.heimeside]

        if self.gjeld_for_tidsrom is not None and not isinstance(self.gjeld_for_tidsrom, TidsromId):
            self.gjeld_for_tidsrom = TidsromId(self.gjeld_for_tidsrom)

        if self.antall_nivaa is not None and not isinstance(self.antall_nivaa, int):
            self.antall_nivaa = int(self.antall_nivaa)

        if not isinstance(self.er_samanlikna_med, list):
            self.er_samanlikna_med = [self.er_samanlikna_med] if self.er_samanlikna_med is not None else []
        self.er_samanlikna_med = [v if isinstance(v, KlassifikasjonId) else KlassifikasjonId(v) for v in self.er_samanlikna_med]

        if not isinstance(self.forste_nivaa, list):
            self.forste_nivaa = [self.forste_nivaa] if self.forste_nivaa is not None else []
        self.forste_nivaa = [v if isinstance(v, KlassifikasjonsnivaaId) else KlassifikasjonsnivaaId(v) for v in self.forste_nivaa]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Klassifikasjonsnivaa(YAMLRoot):
    """
    Eit nivå i ein klassifikasjon (xkos:ClassificationLevel).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = XKOS["ClassificationLevel"]
    class_class_curie: ClassVar[str] = "xkos:ClassificationLevel"
    class_name: ClassVar[str] = "Klassifikasjonsnivaa"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/xkos-ap-no/Klassifikasjonsnivaa")

    id: Union[str, KlassifikasjonsnivaaId] = None
    nivaa_djupn: int = None
    har_medlem: Union[Union[str, KategoriId], list[Union[str, KategoriId]]] = None
    tittel: Optional[Union[str, list[str]]] = empty_list()
    underordna_klassifikasjonsnivaa: Optional[Union[Union[str, KlassifikasjonsnivaaId], list[Union[str, KlassifikasjonsnivaaId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KlassifikasjonsnivaaId):
            self.id = KlassifikasjonsnivaaId(self.id)

        if self._is_empty(self.nivaa_djupn):
            self.MissingRequiredField("nivaa_djupn")
        if not isinstance(self.nivaa_djupn, int):
            self.nivaa_djupn = int(self.nivaa_djupn)

        if self._is_empty(self.har_medlem):
            self.MissingRequiredField("har_medlem")
        if not isinstance(self.har_medlem, list):
            self.har_medlem = [self.har_medlem] if self.har_medlem is not None else []
        self.har_medlem = [v if isinstance(v, KategoriId) else KategoriId(v) for v in self.har_medlem]

        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if not isinstance(self.underordna_klassifikasjonsnivaa, list):
            self.underordna_klassifikasjonsnivaa = [self.underordna_klassifikasjonsnivaa] if self.underordna_klassifikasjonsnivaa is not None else []
        self.underordna_klassifikasjonsnivaa = [v if isinstance(v, KlassifikasjonsnivaaId) else KlassifikasjonsnivaaId(v) for v in self.underordna_klassifikasjonsnivaa]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kategori(YAMLRoot):
    """
    Ein kategori i ein klassifikasjon (skos:Concept).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["Concept"]
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "Kategori"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/xkos-ap-no/Kategori")

    id: Union[str, KategoriId] = None
    anbefalt_term: Union[str, list[str]] = None
    er_i_klassifikasjon: Union[str, KlassifikasjonId] = None
    tilhorande_klassifikasjonsnivaa: Optional[Union[str, KlassifikasjonsnivaaId]] = None
    overordna_kategori: Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]] = empty_list()
    underordna_kategori: Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]] = empty_list()
    har_notat: Optional[Union[str, list[str]]] = empty_list()
    er_ekvivalent_med: Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]] = empty_list()
    er_eksklusivt_ekvivalent_med: Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]] = empty_list()
    er_ikkje_ekvivalent_med: Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KategoriId):
            self.id = KategoriId(self.id)

        if self._is_empty(self.anbefalt_term):
            self.MissingRequiredField("anbefalt_term")
        if not isinstance(self.anbefalt_term, list):
            self.anbefalt_term = [self.anbefalt_term] if self.anbefalt_term is not None else []
        self.anbefalt_term = [v if isinstance(v, str) else str(v) for v in self.anbefalt_term]

        if self._is_empty(self.er_i_klassifikasjon):
            self.MissingRequiredField("er_i_klassifikasjon")
        if not isinstance(self.er_i_klassifikasjon, KlassifikasjonId):
            self.er_i_klassifikasjon = KlassifikasjonId(self.er_i_klassifikasjon)

        if self.tilhorande_klassifikasjonsnivaa is not None and not isinstance(self.tilhorande_klassifikasjonsnivaa, KlassifikasjonsnivaaId):
            self.tilhorande_klassifikasjonsnivaa = KlassifikasjonsnivaaId(self.tilhorande_klassifikasjonsnivaa)

        if not isinstance(self.overordna_kategori, list):
            self.overordna_kategori = [self.overordna_kategori] if self.overordna_kategori is not None else []
        self.overordna_kategori = [v if isinstance(v, KategoriId) else KategoriId(v) for v in self.overordna_kategori]

        if not isinstance(self.underordna_kategori, list):
            self.underordna_kategori = [self.underordna_kategori] if self.underordna_kategori is not None else []
        self.underordna_kategori = [v if isinstance(v, KategoriId) else KategoriId(v) for v in self.underordna_kategori]

        if not isinstance(self.har_notat, list):
            self.har_notat = [self.har_notat] if self.har_notat is not None else []
        self.har_notat = [v if isinstance(v, str) else str(v) for v in self.har_notat]

        if not isinstance(self.er_ekvivalent_med, list):
            self.er_ekvivalent_med = [self.er_ekvivalent_med] if self.er_ekvivalent_med is not None else []
        self.er_ekvivalent_med = [v if isinstance(v, KategoriId) else KategoriId(v) for v in self.er_ekvivalent_med]

        if not isinstance(self.er_eksklusivt_ekvivalent_med, list):
            self.er_eksklusivt_ekvivalent_med = [self.er_eksklusivt_ekvivalent_med] if self.er_eksklusivt_ekvivalent_med is not None else []
        self.er_eksklusivt_ekvivalent_med = [v if isinstance(v, KategoriId) else KategoriId(v) for v in self.er_eksklusivt_ekvivalent_med]

        if not isinstance(self.er_ikkje_ekvivalent_med, list):
            self.er_ikkje_ekvivalent_med = [self.er_ikkje_ekvivalent_med] if self.er_ikkje_ekvivalent_med is not None else []
        self.er_ikkje_ekvivalent_med = [v if isinstance(v, KategoriId) else KategoriId(v) for v in self.er_ikkje_ekvivalent_med]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Klassifikasjonssamanlikning(YAMLRoot):
    """
    Ein samanlikning mellom to klassifikasjonar (xkos:Correspondence).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = XKOS["Correspondence"]
    class_class_curie: ClassVar[str] = "xkos:Correspondence"
    class_name: ClassVar[str] = "Klassifikasjonssamanlikning"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/xkos-ap-no/Klassifikasjonssamanlikning")

    id: Union[str, KlassifikasjonssamanlikningId] = None
    identifikator_literal: str = None
    tittel: Union[str, list[str]] = None
    utgjevar: Union[str, OrganisasjonId] = None
    samanliknar: Union[Union[str, KlassifikasjonId], list[Union[str, KlassifikasjonId]]] = None
    bestar_av: Union[Union[str, KategorisamanlikningId], list[Union[str, KategorisamanlikningId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KlassifikasjonssamanlikningId):
            self.id = KlassifikasjonssamanlikningId(self.id)

        if self._is_empty(self.identifikator_literal):
            self.MissingRequiredField("identifikator_literal")
        if not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.utgjevar):
            self.MissingRequiredField("utgjevar")
        if not isinstance(self.utgjevar, OrganisasjonId):
            self.utgjevar = OrganisasjonId(self.utgjevar)

        if self._is_empty(self.samanliknar):
            self.MissingRequiredField("samanliknar")
        if not isinstance(self.samanliknar, list):
            self.samanliknar = [self.samanliknar] if self.samanliknar is not None else []
        self.samanliknar = [v if isinstance(v, KlassifikasjonId) else KlassifikasjonId(v) for v in self.samanliknar]

        if self._is_empty(self.bestar_av):
            self.MissingRequiredField("bestar_av")
        if not isinstance(self.bestar_av, list):
            self.bestar_av = [self.bestar_av] if self.bestar_av is not None else []
        self.bestar_av = [v if isinstance(v, KategorisamanlikningId) else KategorisamanlikningId(v) for v in self.bestar_av]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kategorisamanlikning(YAMLRoot):
    """
    Ein samanlikning mellom to kategoriar på tvers av klassifikasjonar (xkos:ConceptAssociation).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = XKOS["ConceptAssociation"]
    class_class_curie: ClassVar[str] = "xkos:ConceptAssociation"
    class_name: ClassVar[str] = "Kategorisamanlikning"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/xkos-ap-no/Kategorisamanlikning")

    id: Union[str, KategorisamanlikningId] = None
    kjeldeomgrep: Optional[Union[str, KategoriId]] = None
    maalomgrep: Optional[Union[str, KategoriId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KategorisamanlikningId):
            self.id = KategorisamanlikningId(self.id)

        if self.kjeldeomgrep is not None and not isinstance(self.kjeldeomgrep, KategoriId):
            self.kjeldeomgrep = KategoriId(self.kjeldeomgrep)

        if self.maalomgrep is not None and not isinstance(self.maalomgrep, KategoriId):
            self.maalomgrep = KategoriId(self.maalomgrep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organisasjon(YAMLRoot):
    """
    Ein organisasjon eller aktør (foaf:Agent).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Agent"]
    class_class_curie: ClassVar[str] = "foaf:Agent"
    class_name: ClassVar[str] = "Organisasjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/xkos-ap-no/Organisasjon")

    id: Union[str, OrganisasjonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganisasjonId):
            self.id = OrganisasjonId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tidsrom(YAMLRoot):
    """
    Eit tidsrom med start- og/eller sluttdato (dct:PeriodOfTime).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["PeriodOfTime"]
    class_class_curie: ClassVar[str] = "dct:PeriodOfTime"
    class_name: ClassVar[str] = "Tidsrom"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/xkos-ap-no/Tidsrom")

    id: Union[str, TidsromId] = None
    tidsrom_start: Optional[Union[str, XSDDate]] = None
    tidsrom_slutt: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TidsromId):
            self.id = TidsromId(self.id)

        if self.tidsrom_start is not None and not isinstance(self.tidsrom_start, XSDDate):
            self.tidsrom_start = XSDDate(self.tidsrom_start)

        if self.tidsrom_slutt is not None and not isinstance(self.tidsrom_slutt, XSDDate):
            self.tidsrom_slutt = XSDDate(self.tidsrom_slutt)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Mediatype(YAMLRoot):
    """
    Ein medietype eller filformat (dct:MediaTypeOrExtent).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["MediaTypeOrExtent"]
    class_class_curie: ClassVar[str] = "dct:MediaTypeOrExtent"
    class_name: ClassVar[str] = "Mediatype"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/xkos-ap-no/Mediatype")

    id: Union[str, MediatypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MediatypeId):
            self.id = MediatypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Konsept(YAMLRoot):
    """
    Referanse til eit SKOS-omgrep frå eit kontrollert vokabular.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["Concept"]
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "Konsept"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/xkos-ap-no/Konsept")

    id: Union[str, KonseptId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KonseptId):
            self.id = KonseptId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Begrepssamling(YAMLRoot):
    """
    Ei SKOS-omgrepssamling (temavokabular).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["ConceptScheme"]
    class_class_curie: ClassVar[str] = "skos:ConceptScheme"
    class_name: ClassVar[str] = "Begrepssamling"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/xkos-ap-no/Begrepssamling")

    id: Union[str, BegrepssamlingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BegrepssamlingId):
            self.id = BegrepssamlingId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.utgjevar = Slot(uri=DCT.publisher, name="utgjevar", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.utgjevar, domain=None, range=Optional[Union[str, OrganisasjonId]])

slots.tema = Slot(uri=DCT.subject, name="tema", curie=DCT.curie('subject'),
                   model_uri=DEFAULT_.tema, domain=None, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.antall_nivaa = Slot(uri=XKOS.numberOfLevels, name="antall_nivaa", curie=XKOS.curie('numberOfLevels'),
                   model_uri=DEFAULT_.antall_nivaa, domain=None, range=Optional[int])

slots.gjeld_for_tidsrom = Slot(uri=DCT.temporal, name="gjeld_for_tidsrom", curie=DCT.curie('temporal'),
                   model_uri=DEFAULT_.gjeld_for_tidsrom, domain=None, range=Optional[Union[str, TidsromId]])

slots.er_samanlikna_med = Slot(uri=XKOS.compares, name="er_samanlikna_med", curie=XKOS.curie('compares'),
                   model_uri=DEFAULT_.er_samanlikna_med, domain=None, range=Optional[Union[Union[str, KlassifikasjonId], list[Union[str, KlassifikasjonId]]]])

slots.forste_nivaa = Slot(uri=XKOS.levels, name="forste_nivaa", curie=XKOS.curie('levels'),
                   model_uri=DEFAULT_.forste_nivaa, domain=None, range=Optional[Union[Union[str, KlassifikasjonsnivaaId], list[Union[str, KlassifikasjonsnivaaId]]]])

slots.nivaa_djupn = Slot(uri=XKOS.depth, name="nivaa_djupn", curie=XKOS.curie('depth'),
                   model_uri=DEFAULT_.nivaa_djupn, domain=None, range=Optional[int])

slots.har_medlem = Slot(uri=SKOS.member, name="har_medlem", curie=SKOS.curie('member'),
                   model_uri=DEFAULT_.har_medlem, domain=None, range=Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]])

slots.underordna_klassifikasjonsnivaa = Slot(uri=XKOS.nextLevel, name="underordna_klassifikasjonsnivaa", curie=XKOS.curie('nextLevel'),
                   model_uri=DEFAULT_.underordna_klassifikasjonsnivaa, domain=None, range=Optional[Union[Union[str, KlassifikasjonsnivaaId], list[Union[str, KlassifikasjonsnivaaId]]]])

slots.er_i_klassifikasjon = Slot(uri=SKOS.inScheme, name="er_i_klassifikasjon", curie=SKOS.curie('inScheme'),
                   model_uri=DEFAULT_.er_i_klassifikasjon, domain=None, range=Optional[Union[str, KlassifikasjonId]])

slots.tilhorande_klassifikasjonsnivaa = Slot(uri=XKOS.belongsTo, name="tilhorande_klassifikasjonsnivaa", curie=XKOS.curie('belongsTo'),
                   model_uri=DEFAULT_.tilhorande_klassifikasjonsnivaa, domain=None, range=Optional[Union[str, KlassifikasjonsnivaaId]])

slots.overordna_kategori = Slot(uri=SKOS.broader, name="overordna_kategori", curie=SKOS.curie('broader'),
                   model_uri=DEFAULT_.overordna_kategori, domain=None, range=Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]])

slots.underordna_kategori = Slot(uri=SKOS.narrower, name="underordna_kategori", curie=SKOS.curie('narrower'),
                   model_uri=DEFAULT_.underordna_kategori, domain=None, range=Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]])

slots.har_notat = Slot(uri=SKOS.note, name="har_notat", curie=SKOS.curie('note'),
                   model_uri=DEFAULT_.har_notat, domain=None, range=Optional[Union[str, list[str]]])

slots.er_ekvivalent_med = Slot(uri=UNESKOS.broadMatch, name="er_ekvivalent_med", curie=UNESKOS.curie('broadMatch'),
                   model_uri=DEFAULT_.er_ekvivalent_med, domain=None, range=Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]])

slots.er_eksklusivt_ekvivalent_med = Slot(uri=XKOS.exclusivelyBroadMatch, name="er_eksklusivt_ekvivalent_med", curie=XKOS.curie('exclusivelyBroadMatch'),
                   model_uri=DEFAULT_.er_eksklusivt_ekvivalent_med, domain=None, range=Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]])

slots.er_ikkje_ekvivalent_med = Slot(uri=XKOS.disjointMatch, name="er_ikkje_ekvivalent_med", curie=XKOS.curie('disjointMatch'),
                   model_uri=DEFAULT_.er_ikkje_ekvivalent_med, domain=None, range=Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]])

slots.samanliknar = Slot(uri=XKOS.compares, name="samanliknar", curie=XKOS.curie('compares'),
                   model_uri=DEFAULT_.samanliknar, domain=None, range=Optional[Union[Union[str, KlassifikasjonId], list[Union[str, KlassifikasjonId]]]])

slots.bestar_av = Slot(uri=XKOS.madeOf, name="bestar_av", curie=XKOS.curie('madeOf'),
                   model_uri=DEFAULT_.bestar_av, domain=None, range=Optional[Union[Union[str, KategorisamanlikningId], list[Union[str, KategorisamanlikningId]]]])

slots.kjeldeomgrep = Slot(uri=XKOS.sourceConcept, name="kjeldeomgrep", curie=XKOS.curie('sourceConcept'),
                   model_uri=DEFAULT_.kjeldeomgrep, domain=None, range=Optional[Union[str, KategoriId]])

slots.maalomgrep = Slot(uri=XKOS.targetConcept, name="maalomgrep", curie=XKOS.curie('targetConcept'),
                   model_uri=DEFAULT_.maalomgrep, domain=None, range=Optional[Union[str, KategoriId]])

slots.tidsrom_start = Slot(uri=DCT.startDate, name="tidsrom_start", curie=DCT.curie('startDate'),
                   model_uri=DEFAULT_.tidsrom_start, domain=None, range=Optional[Union[str, XSDDate]])

slots.tidsrom_slutt = Slot(uri=DCT.endDate, name="tidsrom_slutt", curie=DCT.curie('endDate'),
                   model_uri=DEFAULT_.tidsrom_slutt, domain=None, range=Optional[Union[str, XSDDate]])

slots.id = Slot(uri=CAPNO.id, name="id", curie=CAPNO.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.tittel = Slot(uri=DCT.title, name="tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.tittel, domain=None, range=Optional[Union[str, list[str]]])

slots.beskrivelse = Slot(uri=DCT.description, name="beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.beskrivelse, domain=None, range=Optional[Union[str, list[str]]])

slots.identifikator_literal = Slot(uri=DCT.identifier, name="identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.identifikator_literal, domain=None, range=Optional[str])

slots.type_concept = Slot(uri=DCT.type, name="type_concept", curie=DCT.curie('type'),
                   model_uri=DEFAULT_.type_concept, domain=None, range=Optional[Union[str, KonseptId]])

slots.endringsdato = Slot(uri=DCT.modified, name="endringsdato", curie=DCT.curie('modified'),
                   model_uri=DEFAULT_.endringsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.utgivelsesdato = Slot(uri=DCT.issued, name="utgivelsesdato", curie=DCT.curie('issued'),
                   model_uri=DEFAULT_.utgivelsesdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.spraak = Slot(uri=DCT.language, name="spraak", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.spraak, domain=None, range=Optional[Union[str, list[str]]])

slots.format = Slot(uri=DCT.format, name="format", curie=DCT.curie('format'),
                   model_uri=DEFAULT_.format, domain=None, range=Optional[str])

slots.har_referanse = Slot(uri=RDFS.seeAlso, name="har_referanse", curie=RDFS.curie('seeAlso'),
                   model_uri=DEFAULT_.har_referanse, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.har_merknad = Slot(uri=RDFS.comment, name="har_merknad", curie=RDFS.curie('comment'),
                   model_uri=DEFAULT_.har_merknad, domain=None, range=Optional[Union[str, list[str]]])

slots.har_versjonsnummer = Slot(uri=OWL.versionInfo, name="har_versjonsnummer", curie=OWL.curie('versionInfo'),
                   model_uri=DEFAULT_.har_versjonsnummer, domain=None, range=Optional[str])

slots.nokkelord = Slot(uri=DCAT.keyword, name="nokkelord", curie=DCAT.curie('keyword'),
                   model_uri=DEFAULT_.nokkelord, domain=None, range=Optional[Union[str, list[str]]])

slots.dekningsomraade = Slot(uri=DCT.spatial, name="dekningsomraade", curie=DCT.curie('spatial'),
                   model_uri=DEFAULT_.dekningsomraade, domain=None, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.status = Slot(uri=ADMS.status, name="status", curie=ADMS.curie('status'),
                   model_uri=DEFAULT_.status, domain=None, range=Optional[Union[str, KonseptId]])

slots.valuta = Slot(uri=CV.currency, name="valuta", curie=CV.curie('currency'),
                   model_uri=DEFAULT_.valuta, domain=None, range=Optional[Union[str, KonseptId]])

slots.heimeside = Slot(uri=FOAF.homepage, name="heimeside", curie=FOAF.curie('homepage'),
                   model_uri=DEFAULT_.heimeside, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.anbefalt_term = Slot(uri=SKOS.prefLabel, name="anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=DEFAULT_.anbefalt_term, domain=None, range=Optional[Union[str, list[str]]])

slots.versjonsmerknad = Slot(uri=ADMS.versionNotes, name="versjonsmerknad", curie=ADMS.curie('versionNotes'),
                   model_uri=DEFAULT_.versjonsmerknad, domain=None, range=Optional[Union[str, list[str]]])

slots.Klassifikasjon_identifikator_literal = Slot(uri=DCT.identifier, name="Klassifikasjon_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Klassifikasjon_identifikator_literal, domain=Klassifikasjon, range=str)

slots.Klassifikasjon_tittel = Slot(uri=DCT.title, name="Klassifikasjon_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Klassifikasjon_tittel, domain=Klassifikasjon, range=Union[str, list[str]])

slots.Klassifikasjon_utgjevar = Slot(uri=DCT.publisher, name="Klassifikasjon_utgjevar", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.Klassifikasjon_utgjevar, domain=Klassifikasjon, range=Union[str, OrganisasjonId])

slots.Klassifikasjon_tema = Slot(uri=DCT.subject, name="Klassifikasjon_tema", curie=DCT.curie('subject'),
                   model_uri=DEFAULT_.Klassifikasjon_tema, domain=Klassifikasjon, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Klassifikasjon_nokkelord = Slot(uri=DCAT.keyword, name="Klassifikasjon_nokkelord", curie=DCAT.curie('keyword'),
                   model_uri=DEFAULT_.Klassifikasjon_nokkelord, domain=Klassifikasjon, range=Optional[Union[str, list[str]]])

slots.Klassifikasjon_spraak = Slot(uri=DCT.language, name="Klassifikasjon_spraak", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.Klassifikasjon_spraak, domain=Klassifikasjon, range=Optional[Union[str, list[str]]])

slots.Klassifikasjon_har_versjonsnummer = Slot(uri=OWL.versionInfo, name="Klassifikasjon_har_versjonsnummer", curie=OWL.curie('versionInfo'),
                   model_uri=DEFAULT_.Klassifikasjon_har_versjonsnummer, domain=Klassifikasjon, range=Optional[str])

slots.Klassifikasjon_endringsdato = Slot(uri=DCT.modified, name="Klassifikasjon_endringsdato", curie=DCT.curie('modified'),
                   model_uri=DEFAULT_.Klassifikasjon_endringsdato, domain=Klassifikasjon, range=Optional[Union[str, XSDDate]])

slots.Klassifikasjon_utgivelsesdato = Slot(uri=DCT.issued, name="Klassifikasjon_utgivelsesdato", curie=DCT.curie('issued'),
                   model_uri=DEFAULT_.Klassifikasjon_utgivelsesdato, domain=Klassifikasjon, range=Optional[Union[str, XSDDate]])

slots.Klassifikasjon_heimeside = Slot(uri=FOAF.homepage, name="Klassifikasjon_heimeside", curie=FOAF.curie('homepage'),
                   model_uri=DEFAULT_.Klassifikasjon_heimeside, domain=Klassifikasjon, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Klassifikasjon_gjeld_for_tidsrom = Slot(uri=DCT.temporal, name="Klassifikasjon_gjeld_for_tidsrom", curie=DCT.curie('temporal'),
                   model_uri=DEFAULT_.Klassifikasjon_gjeld_for_tidsrom, domain=Klassifikasjon, range=Optional[Union[str, TidsromId]])

slots.Klassifikasjon_antall_nivaa = Slot(uri=XKOS.numberOfLevels, name="Klassifikasjon_antall_nivaa", curie=XKOS.curie('numberOfLevels'),
                   model_uri=DEFAULT_.Klassifikasjon_antall_nivaa, domain=Klassifikasjon, range=Optional[int])

slots.Klassifikasjon_er_samanlikna_med = Slot(uri=XKOS.compares, name="Klassifikasjon_er_samanlikna_med", curie=XKOS.curie('compares'),
                   model_uri=DEFAULT_.Klassifikasjon_er_samanlikna_med, domain=Klassifikasjon, range=Optional[Union[Union[str, KlassifikasjonId], list[Union[str, KlassifikasjonId]]]])

slots.Klassifikasjon_forste_nivaa = Slot(uri=XKOS.levels, name="Klassifikasjon_forste_nivaa", curie=XKOS.curie('levels'),
                   model_uri=DEFAULT_.Klassifikasjon_forste_nivaa, domain=Klassifikasjon, range=Optional[Union[Union[str, KlassifikasjonsnivaaId], list[Union[str, KlassifikasjonsnivaaId]]]])

slots.Klassifikasjonsnivaa_tittel = Slot(uri=DCT.title, name="Klassifikasjonsnivaa_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Klassifikasjonsnivaa_tittel, domain=Klassifikasjonsnivaa, range=Optional[Union[str, list[str]]])

slots.Klassifikasjonsnivaa_nivaa_djupn = Slot(uri=XKOS.depth, name="Klassifikasjonsnivaa_nivaa_djupn", curie=XKOS.curie('depth'),
                   model_uri=DEFAULT_.Klassifikasjonsnivaa_nivaa_djupn, domain=Klassifikasjonsnivaa, range=int)

slots.Klassifikasjonsnivaa_har_medlem = Slot(uri=SKOS.member, name="Klassifikasjonsnivaa_har_medlem", curie=SKOS.curie('member'),
                   model_uri=DEFAULT_.Klassifikasjonsnivaa_har_medlem, domain=Klassifikasjonsnivaa, range=Union[Union[str, KategoriId], list[Union[str, KategoriId]]])

slots.Klassifikasjonsnivaa_underordna_klassifikasjonsnivaa = Slot(uri=XKOS.nextLevel, name="Klassifikasjonsnivaa_underordna_klassifikasjonsnivaa", curie=XKOS.curie('nextLevel'),
                   model_uri=DEFAULT_.Klassifikasjonsnivaa_underordna_klassifikasjonsnivaa, domain=Klassifikasjonsnivaa, range=Optional[Union[Union[str, KlassifikasjonsnivaaId], list[Union[str, KlassifikasjonsnivaaId]]]])

slots.Kategori_anbefalt_term = Slot(uri=SKOS.prefLabel, name="Kategori_anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=DEFAULT_.Kategori_anbefalt_term, domain=Kategori, range=Union[str, list[str]])

slots.Kategori_er_i_klassifikasjon = Slot(uri=SKOS.inScheme, name="Kategori_er_i_klassifikasjon", curie=SKOS.curie('inScheme'),
                   model_uri=DEFAULT_.Kategori_er_i_klassifikasjon, domain=Kategori, range=Union[str, KlassifikasjonId])

slots.Kategori_tilhorande_klassifikasjonsnivaa = Slot(uri=XKOS.belongsTo, name="Kategori_tilhorande_klassifikasjonsnivaa", curie=XKOS.curie('belongsTo'),
                   model_uri=DEFAULT_.Kategori_tilhorande_klassifikasjonsnivaa, domain=Kategori, range=Optional[Union[str, KlassifikasjonsnivaaId]])

slots.Kategori_overordna_kategori = Slot(uri=SKOS.broader, name="Kategori_overordna_kategori", curie=SKOS.curie('broader'),
                   model_uri=DEFAULT_.Kategori_overordna_kategori, domain=Kategori, range=Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]])

slots.Kategori_underordna_kategori = Slot(uri=SKOS.narrower, name="Kategori_underordna_kategori", curie=SKOS.curie('narrower'),
                   model_uri=DEFAULT_.Kategori_underordna_kategori, domain=Kategori, range=Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]])

slots.Kategori_har_notat = Slot(uri=SKOS.note, name="Kategori_har_notat", curie=SKOS.curie('note'),
                   model_uri=DEFAULT_.Kategori_har_notat, domain=Kategori, range=Optional[Union[str, list[str]]])

slots.Kategori_er_ekvivalent_med = Slot(uri=UNESKOS.broadMatch, name="Kategori_er_ekvivalent_med", curie=UNESKOS.curie('broadMatch'),
                   model_uri=DEFAULT_.Kategori_er_ekvivalent_med, domain=Kategori, range=Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]])

slots.Kategori_er_eksklusivt_ekvivalent_med = Slot(uri=XKOS.exclusivelyBroadMatch, name="Kategori_er_eksklusivt_ekvivalent_med", curie=XKOS.curie('exclusivelyBroadMatch'),
                   model_uri=DEFAULT_.Kategori_er_eksklusivt_ekvivalent_med, domain=Kategori, range=Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]])

slots.Kategori_er_ikkje_ekvivalent_med = Slot(uri=XKOS.disjointMatch, name="Kategori_er_ikkje_ekvivalent_med", curie=XKOS.curie('disjointMatch'),
                   model_uri=DEFAULT_.Kategori_er_ikkje_ekvivalent_med, domain=Kategori, range=Optional[Union[Union[str, KategoriId], list[Union[str, KategoriId]]]])

slots.Klassifikasjonssamanlikning_identifikator_literal = Slot(uri=DCT.identifier, name="Klassifikasjonssamanlikning_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Klassifikasjonssamanlikning_identifikator_literal, domain=Klassifikasjonssamanlikning, range=str)

slots.Klassifikasjonssamanlikning_tittel = Slot(uri=DCT.title, name="Klassifikasjonssamanlikning_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Klassifikasjonssamanlikning_tittel, domain=Klassifikasjonssamanlikning, range=Union[str, list[str]])

slots.Klassifikasjonssamanlikning_utgjevar = Slot(uri=DCT.publisher, name="Klassifikasjonssamanlikning_utgjevar", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.Klassifikasjonssamanlikning_utgjevar, domain=Klassifikasjonssamanlikning, range=Union[str, OrganisasjonId])

slots.Klassifikasjonssamanlikning_samanliknar = Slot(uri=XKOS.compares, name="Klassifikasjonssamanlikning_samanliknar", curie=XKOS.curie('compares'),
                   model_uri=DEFAULT_.Klassifikasjonssamanlikning_samanliknar, domain=Klassifikasjonssamanlikning, range=Union[Union[str, KlassifikasjonId], list[Union[str, KlassifikasjonId]]])

slots.Klassifikasjonssamanlikning_bestar_av = Slot(uri=XKOS.madeOf, name="Klassifikasjonssamanlikning_bestar_av", curie=XKOS.curie('madeOf'),
                   model_uri=DEFAULT_.Klassifikasjonssamanlikning_bestar_av, domain=Klassifikasjonssamanlikning, range=Union[Union[str, KategorisamanlikningId], list[Union[str, KategorisamanlikningId]]])

slots.Kategorisamanlikning_kjeldeomgrep = Slot(uri=XKOS.sourceConcept, name="Kategorisamanlikning_kjeldeomgrep", curie=XKOS.curie('sourceConcept'),
                   model_uri=DEFAULT_.Kategorisamanlikning_kjeldeomgrep, domain=Kategorisamanlikning, range=Optional[Union[str, KategoriId]])

slots.Kategorisamanlikning_maalomgrep = Slot(uri=XKOS.targetConcept, name="Kategorisamanlikning_maalomgrep", curie=XKOS.curie('targetConcept'),
                   model_uri=DEFAULT_.Kategorisamanlikning_maalomgrep, domain=Kategorisamanlikning, range=Optional[Union[str, KategoriId]])

