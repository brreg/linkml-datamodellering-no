# Auto generated from dqv-ap-no-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-05T13:23:23
# Schema: dqv-ap-no
#
# id: https://data.norge.no/linkml/dqv-ap-no
# description: Norsk applikasjonsprofil av DQV (Data Quality Vocabulary), modellert i LinkML med lenking framfor inlining. Basert på https://informasjonsforvaltning.github.io/dqv-ap-no/
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
version = "1.0"

# Namespaces
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms#')
CAPNO = CurieNamespace('capno', 'https://data.norge.no/linkml/common-ap-no/')
CV = CurieNamespace('cv', 'http://data.europa.eu/m8g/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DQV = CurieNamespace('dqv', 'http://www.w3.org/ns/dqv#')
DQVNO = CurieNamespace('dqvno', 'https://data.norge.no/vocabulary/dqvno#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OA = CurieNamespace('oa', 'http://www.w3.org/ns/oa#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://data.norge.no/linkml/dqv-ap-no/')


# Types
class LangString(str):
    """ Språktagget streng (rdf:langString). """
    type_class_uri = RDF["langString"]
    type_class_curie = "rdf:langString"
    type_name = "LangString"
    type_model_uri = URIRef("https://data.norge.no/linkml/dqv-ap-no/LangString")


class NonNegativeInteger(int):
    """ Ikkje-negativ heltalsverdi (xsd:nonNegativeInteger). """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "NonNegativeInteger"
    type_model_uri = URIRef("https://data.norge.no/linkml/dqv-ap-no/NonNegativeInteger")


class Duration(str):
    """ ISO 8601-varigheit (xsd:duration), t.d. PT15M. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "Duration"
    type_model_uri = URIRef("https://data.norge.no/linkml/dqv-ap-no/Duration")


class GYear(str):
    """ Gregorisk årstal (xsd:gYear), t.d. 2024. """
    type_class_uri = XSD["gYear"]
    type_class_curie = "xsd:gYear"
    type_name = "GYear"
    type_model_uri = URIRef("https://data.norge.no/linkml/dqv-ap-no/GYear")


# Class references
class DcatRessursId(URIorCURIE):
    pass


class DatasettId(URIorCURIE):
    pass


class KvalitetsdimensjonId(URIorCURIE):
    pass


class KvalitetsdeldimensjonId(KvalitetsdimensjonId):
    pass


class KvalitetsmaalId(URIorCURIE):
    pass


class KvalitetsmerknadId(URIorCURIE):
    pass


class BrukartilbakemeldingId(KvalitetsmerknadId):
    pass


class KvalitetssertifikatId(KvalitetsmerknadId):
    pass


class KvalitetsmaalingId(URIorCURIE):
    pass


class StandardId(URIorCURIE):
    pass


class TekstdelId(URIorCURIE):
    pass


class MotivasjonId(URIorCURIE):
    pass


class SpraakId(URIorCURIE):
    pass


class MediatypeId(URIorCURIE):
    pass


class KonseptId(URIorCURIE):
    pass


class BegrepssamlingId(URIorCURIE):
    pass


@dataclass(repr=False)
class DcatRessurs(YAMLRoot):
    """
    Ein katalogisert ressurs (brukt som målklasse for oa:hasTarget).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Resource"]
    class_class_curie: ClassVar[str] = "dcat:Resource"
    class_name: ClassVar[str] = "DcatRessurs"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/DcatRessurs")

    id: Union[str, DcatRessursId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DcatRessursId):
            self.id = DcatRessursId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Datasett(YAMLRoot):
    """
    Eit datasett (dcat:Dataset) utvida med DQV-AP-NO-eigenskapar for kvalitetsinformasjon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "Datasett"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Datasett")

    id: Union[str, DatasettId] = None
    er_i_samsvar_med: Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]] = empty_list()
    har_kvalitetsmerknad: Optional[Union[Union[str, KvalitetsmerknadId], list[Union[str, KvalitetsmerknadId]]]] = empty_list()
    har_kvalitetsmaaling: Optional[Union[Union[str, KvalitetsmaalingId], list[Union[str, KvalitetsmaalingId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasettId):
            self.id = DatasettId(self.id)

        if not isinstance(self.er_i_samsvar_med, list):
            self.er_i_samsvar_med = [self.er_i_samsvar_med] if self.er_i_samsvar_med is not None else []
        self.er_i_samsvar_med = [v if isinstance(v, StandardId) else StandardId(v) for v in self.er_i_samsvar_med]

        if not isinstance(self.har_kvalitetsmerknad, list):
            self.har_kvalitetsmerknad = [self.har_kvalitetsmerknad] if self.har_kvalitetsmerknad is not None else []
        self.har_kvalitetsmerknad = [v if isinstance(v, KvalitetsmerknadId) else KvalitetsmerknadId(v) for v in self.har_kvalitetsmerknad]

        if not isinstance(self.har_kvalitetsmaaling, list):
            self.har_kvalitetsmaaling = [self.har_kvalitetsmaaling] if self.har_kvalitetsmaaling is not None else []
        self.har_kvalitetsmaaling = [v if isinstance(v, KvalitetsmaalingId) else KvalitetsmaalingId(v) for v in self.har_kvalitetsmaaling]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kvalitetsdimensjon(YAMLRoot):
    """
    Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQV["Dimension"]
    class_class_curie: ClassVar[str] = "dqv:Dimension"
    class_name: ClassVar[str] = "Kvalitetsdimensjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Kvalitetsdimensjon")

    id: Union[str, KvalitetsdimensjonId] = None
    har_anbefalt_term: Optional[Union[str, list[str]]] = empty_list()
    har_definisjon: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KvalitetsdimensjonId):
            self.id = KvalitetsdimensjonId(self.id)

        if not isinstance(self.har_anbefalt_term, list):
            self.har_anbefalt_term = [self.har_anbefalt_term] if self.har_anbefalt_term is not None else []
        self.har_anbefalt_term = [v if isinstance(v, str) else str(v) for v in self.har_anbefalt_term]

        if not isinstance(self.har_definisjon, list):
            self.har_definisjon = [self.har_definisjon] if self.har_definisjon is not None else []
        self.har_definisjon = [v if isinstance(v, str) else str(v) for v in self.har_definisjon]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kvalitetsdeldimensjon(Kvalitetsdimensjon):
    """
    Ein deldimensjon av ein kvalitetsdimensjon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQVNO["SubDimension"]
    class_class_curie: ClassVar[str] = "dqvno:SubDimension"
    class_name: ClassVar[str] = "Kvalitetsdeldimensjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Kvalitetsdeldimensjon")

    id: Union[str, KvalitetsdeldimensjonId] = None
    er_deldimensjon_av: Union[str, KvalitetsdimensjonId] = None
    har_anbefalt_term: Optional[Union[str, list[str]]] = empty_list()
    har_definisjon: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KvalitetsdeldimensjonId):
            self.id = KvalitetsdeldimensjonId(self.id)

        if self._is_empty(self.er_deldimensjon_av):
            self.MissingRequiredField("er_deldimensjon_av")
        if not isinstance(self.er_deldimensjon_av, KvalitetsdimensjonId):
            self.er_deldimensjon_av = KvalitetsdimensjonId(self.er_deldimensjon_av)

        if not isinstance(self.har_anbefalt_term, list):
            self.har_anbefalt_term = [self.har_anbefalt_term] if self.har_anbefalt_term is not None else []
        self.har_anbefalt_term = [v if isinstance(v, str) else str(v) for v in self.har_anbefalt_term]

        if not isinstance(self.har_definisjon, list):
            self.har_definisjon = [self.har_definisjon] if self.har_definisjon is not None else []
        self.har_definisjon = [v if isinstance(v, str) else str(v) for v in self.har_definisjon]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kvalitetsmaal(YAMLRoot):
    """
    Eit kvalitetsmål som operasjonaliserer ein kvalitetsdeldimensjon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQV["Metric"]
    class_class_curie: ClassVar[str] = "dqv:Metric"
    class_name: ClassVar[str] = "Kvalitetsmaal"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Kvalitetsmaal")

    id: Union[str, KvalitetsmaalId] = None
    er_i_kvalitetsdeldimensjon: Union[str, KvalitetsdeldimensjonId] = None
    har_forventet_datatype: Optional[Union[str, URIorCURIE]] = None
    har_anbefalt_term: Optional[Union[str, list[str]]] = empty_list()
    har_definisjon: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KvalitetsmaalId):
            self.id = KvalitetsmaalId(self.id)

        if self._is_empty(self.er_i_kvalitetsdeldimensjon):
            self.MissingRequiredField("er_i_kvalitetsdeldimensjon")
        if not isinstance(self.er_i_kvalitetsdeldimensjon, KvalitetsdeldimensjonId):
            self.er_i_kvalitetsdeldimensjon = KvalitetsdeldimensjonId(self.er_i_kvalitetsdeldimensjon)

        if self.har_forventet_datatype is not None and not isinstance(self.har_forventet_datatype, URIorCURIE):
            self.har_forventet_datatype = URIorCURIE(self.har_forventet_datatype)

        if not isinstance(self.har_anbefalt_term, list):
            self.har_anbefalt_term = [self.har_anbefalt_term] if self.har_anbefalt_term is not None else []
        self.har_anbefalt_term = [v if isinstance(v, str) else str(v) for v in self.har_anbefalt_term]

        if not isinstance(self.har_definisjon, list):
            self.har_definisjon = [self.har_definisjon] if self.har_definisjon is not None else []
        self.har_definisjon = [v if isinstance(v, str) else str(v) for v in self.har_definisjon]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kvalitetsmerknad(YAMLRoot):
    """
    Ein merknad om kvaliteten til eit datasett.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQV["QualityAnnotation"]
    class_class_curie: ClassVar[str] = "dqv:QualityAnnotation"
    class_name: ClassVar[str] = "Kvalitetsmerknad"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Kvalitetsmerknad")

    id: Union[str, KvalitetsmerknadId] = None
    er_motivert_av: Union[str, URIorCURIE] = None
    er_i_kvalitetsdimensjon: Optional[Union[str, KvalitetsdimensjonId]] = None
    har_tekstdel: Optional[Union[str, TekstdelId]] = None
    har_merknad: Optional[Union[str, list[str]]] = empty_list()
    har_maal: Optional[Union[str, DcatRessursId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KvalitetsmerknadId):
            self.id = KvalitetsmerknadId(self.id)

        if self._is_empty(self.er_motivert_av):
            self.MissingRequiredField("er_motivert_av")
        if not isinstance(self.er_motivert_av, URIorCURIE):
            self.er_motivert_av = URIorCURIE(self.er_motivert_av)

        if self.er_i_kvalitetsdimensjon is not None and not isinstance(self.er_i_kvalitetsdimensjon, KvalitetsdimensjonId):
            self.er_i_kvalitetsdimensjon = KvalitetsdimensjonId(self.er_i_kvalitetsdimensjon)

        if self.har_tekstdel is not None and not isinstance(self.har_tekstdel, TekstdelId):
            self.har_tekstdel = TekstdelId(self.har_tekstdel)

        if not isinstance(self.har_merknad, list):
            self.har_merknad = [self.har_merknad] if self.har_merknad is not None else []
        self.har_merknad = [v if isinstance(v, str) else str(v) for v in self.har_merknad]

        if self.har_maal is not None and not isinstance(self.har_maal, DcatRessursId):
            self.har_maal = DcatRessursId(self.har_maal)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Brukartilbakemelding(Kvalitetsmerknad):
    """
    Tilbakemelding frå ein brukar om kvaliteten til eit datasett.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQV["UserQualityFeedback"]
    class_class_curie: ClassVar[str] = "dqv:UserQualityFeedback"
    class_name: ClassVar[str] = "Brukartilbakemelding"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Brukartilbakemelding")

    id: Union[str, BrukartilbakemeldingId] = None
    er_motivert_av: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BrukartilbakemeldingId):
            self.id = BrukartilbakemeldingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kvalitetssertifikat(Kvalitetsmerknad):
    """
    Eit sertifikat som stadfester kvaliteten til eit datasett.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQV["QualityCertificate"]
    class_class_curie: ClassVar[str] = "dqv:QualityCertificate"
    class_name: ClassVar[str] = "Kvalitetssertifikat"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Kvalitetssertifikat")

    id: Union[str, KvalitetssertifikatId] = None
    er_motivert_av: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KvalitetssertifikatId):
            self.id = KvalitetssertifikatId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kvalitetsmaaling(YAMLRoot):
    """
    Ei konkret måling av eit kvalitetsmål for eit datasett.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DQV["QualityMeasurement"]
    class_class_curie: ClassVar[str] = "dqv:QualityMeasurement"
    class_name: ClassVar[str] = "Kvalitetsmaaling"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Kvalitetsmaaling")

    id: Union[str, KvalitetsmaalingId] = None
    er_kvalitetsmaaling_av: Union[str, KvalitetsmaalId] = None
    har_verdi: Optional[str] = None
    har_merknad: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KvalitetsmaalingId):
            self.id = KvalitetsmaalingId(self.id)

        if self._is_empty(self.er_kvalitetsmaaling_av):
            self.MissingRequiredField("er_kvalitetsmaaling_av")
        if not isinstance(self.er_kvalitetsmaaling_av, KvalitetsmaalId):
            self.er_kvalitetsmaaling_av = KvalitetsmaalId(self.er_kvalitetsmaaling_av)

        if self.har_verdi is not None and not isinstance(self.har_verdi, str):
            self.har_verdi = str(self.har_verdi)

        if not isinstance(self.har_merknad, list):
            self.har_merknad = [self.har_merknad] if self.har_merknad is not None else []
        self.har_merknad = [v if isinstance(v, str) else str(v) for v in self.har_merknad]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Standard(YAMLRoot):
    """
    Ein standard eller spesifikasjon som eit datasett er i samsvar med.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["Standard"]
    class_class_curie: ClassVar[str] = "dct:Standard"
    class_name: ClassVar[str] = "Standard"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Standard")

    id: Union[str, StandardId] = None
    tittel: Union[str, list[str]] = None
    er_i_kvalitetsdimensjon: Optional[Union[str, KvalitetsdimensjonId]] = None
    har_referanse: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    har_merknad: Optional[Union[str, list[str]]] = empty_list()
    har_versjonsnummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StandardId):
            self.id = StandardId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self.er_i_kvalitetsdimensjon is not None and not isinstance(self.er_i_kvalitetsdimensjon, KvalitetsdimensjonId):
            self.er_i_kvalitetsdimensjon = KvalitetsdimensjonId(self.er_i_kvalitetsdimensjon)

        if not isinstance(self.har_referanse, list):
            self.har_referanse = [self.har_referanse] if self.har_referanse is not None else []
        self.har_referanse = [v if isinstance(v, URI) else URI(v) for v in self.har_referanse]

        if not isinstance(self.har_merknad, list):
            self.har_merknad = [self.har_merknad] if self.har_merknad is not None else []
        self.har_merknad = [v if isinstance(v, str) else str(v) for v in self.har_merknad]

        if self.har_versjonsnummer is not None and not isinstance(self.har_versjonsnummer, str):
            self.har_versjonsnummer = str(self.har_versjonsnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tekstdel(YAMLRoot):
    """
    Ein tekstleg del av ein kvalitetsmerknad (Web Annotation).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OA["TextualBody"]
    class_class_curie: ClassVar[str] = "oa:TextualBody"
    class_name: ClassVar[str] = "Tekstdel"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Tekstdel")

    id: Union[str, TekstdelId] = None
    har_verdi_tekstdel: str = None
    format: Optional[Union[str, MediatypeId]] = None
    sprak: Optional[Union[Union[str, SpraakId], list[Union[str, SpraakId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TekstdelId):
            self.id = TekstdelId(self.id)

        if self._is_empty(self.har_verdi_tekstdel):
            self.MissingRequiredField("har_verdi_tekstdel")
        if not isinstance(self.har_verdi_tekstdel, str):
            self.har_verdi_tekstdel = str(self.har_verdi_tekstdel)

        if self.format is not None and not isinstance(self.format, MediatypeId):
            self.format = MediatypeId(self.format)

        if not isinstance(self.sprak, list):
            self.sprak = [self.sprak] if self.sprak is not None else []
        self.sprak = [v if isinstance(v, SpraakId) else SpraakId(v) for v in self.sprak]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Motivasjon(YAMLRoot):
    """
    Motivasjonen bak ein kvalitetsmerknad (Web Annotation).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OA["Motivation"]
    class_class_curie: ClassVar[str] = "oa:Motivation"
    class_name: ClassVar[str] = "Motivasjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Motivasjon")

    id: Union[str, MotivasjonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MotivasjonId):
            self.id = MotivasjonId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Spraak(YAMLRoot):
    """
    Ein språkreferanse (dct:LinguisticSystem).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["LinguisticSystem"]
    class_class_curie: ClassVar[str] = "dct:LinguisticSystem"
    class_name: ClassVar[str] = "Spraak"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Spraak")

    id: Union[str, SpraakId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpraakId):
            self.id = SpraakId(self.id)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Mediatype")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Konsept")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/dqv-ap-no/Begrepssamling")

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

slots.er_i_samsvar_med = Slot(uri=DCT.conformsTo, name="er_i_samsvar_med", curie=DCT.curie('conformsTo'),
                   model_uri=DEFAULT_.er_i_samsvar_med, domain=None, range=Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]])

slots.har_kvalitetsmerknad = Slot(uri=DQV.hasQualityAnnotation, name="har_kvalitetsmerknad", curie=DQV.curie('hasQualityAnnotation'),
                   model_uri=DEFAULT_.har_kvalitetsmerknad, domain=None, range=Optional[Union[Union[str, KvalitetsmerknadId], list[Union[str, KvalitetsmerknadId]]]])

slots.har_kvalitetsmaaling = Slot(uri=DQV.hasQualityMeasurement, name="har_kvalitetsmaaling", curie=DQV.curie('hasQualityMeasurement'),
                   model_uri=DEFAULT_.har_kvalitetsmaaling, domain=None, range=Optional[Union[Union[str, KvalitetsmaalingId], list[Union[str, KvalitetsmaalingId]]]])

slots.er_deldimensjon_av = Slot(uri=SKOS.broader, name="er_deldimensjon_av", curie=SKOS.curie('broader'),
                   model_uri=DEFAULT_.er_deldimensjon_av, domain=None, range=Optional[Union[str, KvalitetsdimensjonId]])

slots.har_anbefalt_term = Slot(uri=SKOS.prefLabel, name="har_anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=DEFAULT_.har_anbefalt_term, domain=None, range=Optional[Union[str, list[str]]])

slots.har_definisjon = Slot(uri=SKOS.definition, name="har_definisjon", curie=SKOS.curie('definition'),
                   model_uri=DEFAULT_.har_definisjon, domain=None, range=Optional[Union[str, list[str]]])

slots.er_i_kvalitetsdeldimensjon = Slot(uri=DQVNO.inSubDimension, name="er_i_kvalitetsdeldimensjon", curie=DQVNO.curie('inSubDimension'),
                   model_uri=DEFAULT_.er_i_kvalitetsdeldimensjon, domain=None, range=Optional[Union[str, KvalitetsdeldimensjonId]])

slots.har_forventet_datatype = Slot(uri=DQV.expectedDataType, name="har_forventet_datatype", curie=DQV.curie('expectedDataType'),
                   model_uri=DEFAULT_.har_forventet_datatype, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.er_motivert_av = Slot(uri=OA.motivatedBy, name="er_motivert_av", curie=OA.curie('motivatedBy'),
                   model_uri=DEFAULT_.er_motivert_av, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.er_i_kvalitetsdimensjon = Slot(uri=DQV.inDimension, name="er_i_kvalitetsdimensjon", curie=DQV.curie('inDimension'),
                   model_uri=DEFAULT_.er_i_kvalitetsdimensjon, domain=None, range=Optional[Union[str, KvalitetsdimensjonId]])

slots.har_tekstdel = Slot(uri=OA.hasBody, name="har_tekstdel", curie=OA.curie('hasBody'),
                   model_uri=DEFAULT_.har_tekstdel, domain=None, range=Optional[Union[str, TekstdelId]])

slots.har_maal = Slot(uri=OA.hasTarget, name="har_maal", curie=OA.curie('hasTarget'),
                   model_uri=DEFAULT_.har_maal, domain=None, range=Optional[Union[str, DcatRessursId]])

slots.er_kvalitetsmaaling_av = Slot(uri=DQV.isMeasurementOf, name="er_kvalitetsmaaling_av", curie=DQV.curie('isMeasurementOf'),
                   model_uri=DEFAULT_.er_kvalitetsmaaling_av, domain=None, range=Optional[Union[str, KvalitetsmaalId]])

slots.har_verdi = Slot(uri=DQV.value, name="har_verdi", curie=DQV.curie('value'),
                   model_uri=DEFAULT_.har_verdi, domain=None, range=Optional[str])

slots.har_verdi_tekstdel = Slot(uri=RDFS.value, name="har_verdi_tekstdel", curie=RDFS.curie('value'),
                   model_uri=DEFAULT_.har_verdi_tekstdel, domain=None, range=Optional[str])

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

slots.sprak = Slot(uri=DCT.language, name="sprak", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.sprak, domain=None, range=Optional[Union[Union[str, SpraakId], list[Union[str, SpraakId]]]])

slots.format = Slot(uri=DCT.format, name="format", curie=DCT.curie('format'),
                   model_uri=DEFAULT_.format, domain=None, range=Optional[Union[str, MediatypeId]])

slots.har_referanse = Slot(uri=RDFS.seeAlso, name="har_referanse", curie=RDFS.curie('seeAlso'),
                   model_uri=DEFAULT_.har_referanse, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.har_merknad = Slot(uri=RDFS.comment, name="har_merknad", curie=RDFS.curie('comment'),
                   model_uri=DEFAULT_.har_merknad, domain=None, range=Optional[Union[str, list[str]]])

slots.har_versjonsnummer = Slot(uri=OWL.versionInfo, name="har_versjonsnummer", curie=OWL.curie('versionInfo'),
                   model_uri=DEFAULT_.har_versjonsnummer, domain=None, range=Optional[str])

slots.nokkelord = Slot(uri=DCAT.keyword, name="nokkelord", curie=DCAT.curie('keyword'),
                   model_uri=DEFAULT_.nokkelord, domain=None, range=Optional[Union[str, list[str]]])

slots.dekningsomrade = Slot(uri=DCT.spatial, name="dekningsomrade", curie=DCT.curie('spatial'),
                   model_uri=DEFAULT_.dekningsomrade, domain=None, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

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

slots.Datasett_er_i_samsvar_med = Slot(uri=DCT.conformsTo, name="Datasett_er_i_samsvar_med", curie=DCT.curie('conformsTo'),
                   model_uri=DEFAULT_.Datasett_er_i_samsvar_med, domain=Datasett, range=Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]])

slots.Datasett_har_kvalitetsmerknad = Slot(uri=DQV.hasQualityAnnotation, name="Datasett_har_kvalitetsmerknad", curie=DQV.curie('hasQualityAnnotation'),
                   model_uri=DEFAULT_.Datasett_har_kvalitetsmerknad, domain=Datasett, range=Optional[Union[Union[str, KvalitetsmerknadId], list[Union[str, KvalitetsmerknadId]]]])

slots.Datasett_har_kvalitetsmaaling = Slot(uri=DQV.hasQualityMeasurement, name="Datasett_har_kvalitetsmaaling", curie=DQV.curie('hasQualityMeasurement'),
                   model_uri=DEFAULT_.Datasett_har_kvalitetsmaaling, domain=Datasett, range=Optional[Union[Union[str, KvalitetsmaalingId], list[Union[str, KvalitetsmaalingId]]]])

slots.Kvalitetsdimensjon_har_anbefalt_term = Slot(uri=SKOS.prefLabel, name="Kvalitetsdimensjon_har_anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=DEFAULT_.Kvalitetsdimensjon_har_anbefalt_term, domain=Kvalitetsdimensjon, range=Optional[Union[str, list[str]]])

slots.Kvalitetsdimensjon_har_definisjon = Slot(uri=SKOS.definition, name="Kvalitetsdimensjon_har_definisjon", curie=SKOS.curie('definition'),
                   model_uri=DEFAULT_.Kvalitetsdimensjon_har_definisjon, domain=Kvalitetsdimensjon, range=Optional[Union[str, list[str]]])

slots.Kvalitetsdeldimensjon_er_deldimensjon_av = Slot(uri=SKOS.broader, name="Kvalitetsdeldimensjon_er_deldimensjon_av", curie=SKOS.curie('broader'),
                   model_uri=DEFAULT_.Kvalitetsdeldimensjon_er_deldimensjon_av, domain=Kvalitetsdeldimensjon, range=Union[str, KvalitetsdimensjonId])

slots.Kvalitetsdeldimensjon_har_anbefalt_term = Slot(uri=SKOS.prefLabel, name="Kvalitetsdeldimensjon_har_anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=DEFAULT_.Kvalitetsdeldimensjon_har_anbefalt_term, domain=Kvalitetsdeldimensjon, range=Optional[Union[str, list[str]]])

slots.Kvalitetsdeldimensjon_har_definisjon = Slot(uri=SKOS.definition, name="Kvalitetsdeldimensjon_har_definisjon", curie=SKOS.curie('definition'),
                   model_uri=DEFAULT_.Kvalitetsdeldimensjon_har_definisjon, domain=Kvalitetsdeldimensjon, range=Optional[Union[str, list[str]]])

slots.Kvalitetsmaal_er_i_kvalitetsdeldimensjon = Slot(uri=DQVNO.inSubDimension, name="Kvalitetsmaal_er_i_kvalitetsdeldimensjon", curie=DQVNO.curie('inSubDimension'),
                   model_uri=DEFAULT_.Kvalitetsmaal_er_i_kvalitetsdeldimensjon, domain=Kvalitetsmaal, range=Union[str, KvalitetsdeldimensjonId])

slots.Kvalitetsmaal_har_forventet_datatype = Slot(uri=DQV.expectedDataType, name="Kvalitetsmaal_har_forventet_datatype", curie=DQV.curie('expectedDataType'),
                   model_uri=DEFAULT_.Kvalitetsmaal_har_forventet_datatype, domain=Kvalitetsmaal, range=Optional[Union[str, URIorCURIE]])

slots.Kvalitetsmaal_har_anbefalt_term = Slot(uri=SKOS.prefLabel, name="Kvalitetsmaal_har_anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=DEFAULT_.Kvalitetsmaal_har_anbefalt_term, domain=Kvalitetsmaal, range=Optional[Union[str, list[str]]])

slots.Kvalitetsmaal_har_definisjon = Slot(uri=SKOS.definition, name="Kvalitetsmaal_har_definisjon", curie=SKOS.curie('definition'),
                   model_uri=DEFAULT_.Kvalitetsmaal_har_definisjon, domain=Kvalitetsmaal, range=Optional[Union[str, list[str]]])

slots.Kvalitetsmerknad_er_motivert_av = Slot(uri=OA.motivatedBy, name="Kvalitetsmerknad_er_motivert_av", curie=OA.curie('motivatedBy'),
                   model_uri=DEFAULT_.Kvalitetsmerknad_er_motivert_av, domain=Kvalitetsmerknad, range=Union[str, URIorCURIE])

slots.Kvalitetsmerknad_er_i_kvalitetsdimensjon = Slot(uri=DQV.inDimension, name="Kvalitetsmerknad_er_i_kvalitetsdimensjon", curie=DQV.curie('inDimension'),
                   model_uri=DEFAULT_.Kvalitetsmerknad_er_i_kvalitetsdimensjon, domain=Kvalitetsmerknad, range=Optional[Union[str, KvalitetsdimensjonId]])

slots.Kvalitetsmerknad_har_tekstdel = Slot(uri=OA.hasBody, name="Kvalitetsmerknad_har_tekstdel", curie=OA.curie('hasBody'),
                   model_uri=DEFAULT_.Kvalitetsmerknad_har_tekstdel, domain=Kvalitetsmerknad, range=Optional[Union[str, TekstdelId]])

slots.Kvalitetsmerknad_har_merknad = Slot(uri=RDFS.comment, name="Kvalitetsmerknad_har_merknad", curie=RDFS.curie('comment'),
                   model_uri=DEFAULT_.Kvalitetsmerknad_har_merknad, domain=Kvalitetsmerknad, range=Optional[Union[str, list[str]]])

slots.Kvalitetsmerknad_har_maal = Slot(uri=OA.hasTarget, name="Kvalitetsmerknad_har_maal", curie=OA.curie('hasTarget'),
                   model_uri=DEFAULT_.Kvalitetsmerknad_har_maal, domain=Kvalitetsmerknad, range=Optional[Union[str, DcatRessursId]])

slots.Kvalitetsmaaling_er_kvalitetsmaaling_av = Slot(uri=DQV.isMeasurementOf, name="Kvalitetsmaaling_er_kvalitetsmaaling_av", curie=DQV.curie('isMeasurementOf'),
                   model_uri=DEFAULT_.Kvalitetsmaaling_er_kvalitetsmaaling_av, domain=Kvalitetsmaaling, range=Union[str, KvalitetsmaalId])

slots.Kvalitetsmaaling_har_verdi = Slot(uri=DQV.value, name="Kvalitetsmaaling_har_verdi", curie=DQV.curie('value'),
                   model_uri=DEFAULT_.Kvalitetsmaaling_har_verdi, domain=Kvalitetsmaaling, range=Optional[str])

slots.Kvalitetsmaaling_har_merknad = Slot(uri=RDFS.comment, name="Kvalitetsmaaling_har_merknad", curie=RDFS.curie('comment'),
                   model_uri=DEFAULT_.Kvalitetsmaaling_har_merknad, domain=Kvalitetsmaaling, range=Optional[Union[str, list[str]]])

slots.Standard_tittel = Slot(uri=DCT.title, name="Standard_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Standard_tittel, domain=Standard, range=Union[str, list[str]])

slots.Standard_er_i_kvalitetsdimensjon = Slot(uri=DQV.inDimension, name="Standard_er_i_kvalitetsdimensjon", curie=DQV.curie('inDimension'),
                   model_uri=DEFAULT_.Standard_er_i_kvalitetsdimensjon, domain=Standard, range=Optional[Union[str, KvalitetsdimensjonId]])

slots.Standard_har_referanse = Slot(uri=RDFS.seeAlso, name="Standard_har_referanse", curie=RDFS.curie('seeAlso'),
                   model_uri=DEFAULT_.Standard_har_referanse, domain=Standard, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Standard_har_merknad = Slot(uri=RDFS.comment, name="Standard_har_merknad", curie=RDFS.curie('comment'),
                   model_uri=DEFAULT_.Standard_har_merknad, domain=Standard, range=Optional[Union[str, list[str]]])

slots.Standard_har_versjonsnummer = Slot(uri=OWL.versionInfo, name="Standard_har_versjonsnummer", curie=OWL.curie('versionInfo'),
                   model_uri=DEFAULT_.Standard_har_versjonsnummer, domain=Standard, range=Optional[str])

slots.Tekstdel_har_verdi_tekstdel = Slot(uri=RDFS.value, name="Tekstdel_har_verdi_tekstdel", curie=RDFS.curie('value'),
                   model_uri=DEFAULT_.Tekstdel_har_verdi_tekstdel, domain=Tekstdel, range=str)

slots.Tekstdel_format = Slot(uri=DCT.format, name="Tekstdel_format", curie=DCT.curie('format'),
                   model_uri=DEFAULT_.Tekstdel_format, domain=Tekstdel, range=Optional[Union[str, MediatypeId]])

slots.Tekstdel_sprak = Slot(uri=DCT.language, name="Tekstdel_sprak", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.Tekstdel_sprak, domain=Tekstdel, range=Optional[Union[Union[str, SpraakId], list[Union[str, SpraakId]]]])

