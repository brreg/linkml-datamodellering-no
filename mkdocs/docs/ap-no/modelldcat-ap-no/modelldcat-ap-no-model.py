# Auto generated from modelldcat-ap-no-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-27T14:51:39
# Schema: modelldcat-ap-no
#
# id: https://data.norge.no/ap-no/modelldcat-ap-no
# description: Norsk applikasjonsprofil for beskriving av informasjonsmodellar i DCAT-format, modellert i LinkML. Basert på https://data.norge.no/specification/modelldcat-ap-no
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

from linkml_runtime.linkml_model.types import Boolean, Date, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE, XSDDate

metamodel_version = "1.11.0"
version = "1.0"

# Namespaces
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms#')
CAPNO = CurieNamespace('capno', 'https://data.norge.no/ap-no/common-ap-no/')
CV = CurieNamespace('cv', 'http://data.europa.eu/m8g/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MODELLDCATNO = CurieNamespace('modelldcatno', 'https://data.norge.no/vocabulary/modelldcatno#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROF = CurieNamespace('prof', 'http://www.w3.org/ns/dx/prof/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns#')
XKOS = CurieNamespace('xkos', 'http://rdf-vocabulary.ddialliance.org/xkos#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://data.norge.no/ap-no/modelldcat-ap-no/')


# Types
class Spraak(str):
    """ Språk """
    type_class_uri = DCT["language"]
    type_class_curie = "dct:language"
    type_name = "Spraak"
    type_model_uri = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Spraak")


class LangString(str):
    """ Språktagget streng (rdf:langString). """
    type_class_uri = RDF["langString"]
    type_class_curie = "rdf:langString"
    type_name = "LangString"
    type_model_uri = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/LangString")


class NonNegativeInteger(int):
    """ Ikkje-negativ heltalsverdi (xsd:nonNegativeInteger). """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "NonNegativeInteger"
    type_model_uri = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/NonNegativeInteger")


class Duration(str):
    """ ISO 8601-varigheit (xsd:duration), t.d. PT15M. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "Duration"
    type_model_uri = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Duration")


class GYear(str):
    """ Gregorisk årstal (xsd:gYear), t.d. 2024. """
    type_class_uri = XSD["gYear"]
    type_class_curie = "xsd:gYear"
    type_name = "GYear"
    type_model_uri = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/GYear")


# Class references
class KatalogisertRessursId(URIorCURIE):
    pass


class AktorId(URIorCURIE):
    pass


class KontaktopplysningId(URIorCURIE):
    pass


class StandardId(URIorCURIE):
    pass


class LisensdokumentId(URIorCURIE):
    pass


class LokasjonId(URIorCURIE):
    pass


class TidsperiodeId(URIorCURIE):
    pass


class DokumentId(URIorCURIE):
    pass


class ModellkatalogId(URIorCURIE):
    pass


class InformasjonsmodellId(URIorCURIE):
    pass


class ModellelementId(URIorCURIE):
    pass


class ObjekttypeId(ModellelementId):
    pass


class RootObjekttypeId(ModellelementId):
    pass


class DatatypeId(ModellelementId):
    pass


class EnkelTypeId(ModellelementId):
    pass


class KodelisteId(ModellelementId):
    pass


class ModulId(ModellelementId):
    pass


class EigenskapId(URIorCURIE):
    pass


class AttributtId(EigenskapId):
    pass


class AssosiasjonId(EigenskapId):
    pass


class RolleId(EigenskapId):
    pass


class SpesialiseringId(EigenskapId):
    pass


class SammensetningId(EigenskapId):
    pass


class RealiseringId(EigenskapId):
    pass


class AbstraksjonId(EigenskapId):
    pass


class AvhengighetId(EigenskapId):
    pass


class SamlingId(EigenskapId):
    pass


class ValgId(EigenskapId):
    pass


class AlleAvId(ValgId):
    pass


class NoenAvId(ValgId):
    pass


class MerknadId(URIorCURIE):
    pass


class BetingelsesregelId(MerknadId):
    pass


class OgId(BetingelsesregelId):
    pass


class EllerId(BetingelsesregelId):
    pass


class XEllerYId(BetingelsesregelId):
    pass


class IkkeId(BetingelsesregelId):
    pass


class KodeelementId(URIorCURIE):
    pass


class MediatypeId(URIorCURIE):
    pass


class KonseptId(URIorCURIE):
    pass


class BegrepssamlingId(URIorCURIE):
    pass


@dataclass(repr=False)
class KatalogisertRessurs(YAMLRoot):
    """
    Basisklasse for ressursar som kan katalogiserast (dcat:Resource).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Resource"]
    class_class_curie: ClassVar[str] = "dcat:Resource"
    class_name: ClassVar[str] = "KatalogisertRessurs"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/KatalogisertRessurs")

    id: Union[str, KatalogisertRessursId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KatalogisertRessursId):
            self.id = KatalogisertRessursId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aktor(YAMLRoot):
    """
    Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Agent"]
    class_class_curie: ClassVar[str] = "foaf:Agent"
    class_name: ClassVar[str] = "Aktor"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Aktor")

    id: Union[str, AktorId] = None
    namn_aktor: Union[str, list[str]] = None
    identifikator_literal: Optional[str] = None
    type_concept: Optional[Union[str, KonseptId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AktorId):
            self.id = AktorId(self.id)

        if self._is_empty(self.namn_aktor):
            self.MissingRequiredField("namn_aktor")
        if not isinstance(self.namn_aktor, list):
            self.namn_aktor = [self.namn_aktor] if self.namn_aktor is not None else []
        self.namn_aktor = [v if isinstance(v, str) else str(v) for v in self.namn_aktor]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontaktopplysning(YAMLRoot):
    """
    Kontaktinformasjon (vcard:Organization).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VCARD["Organization"]
    class_class_curie: ClassVar[str] = "vcard:Organization"
    class_name: ClassVar[str] = "Kontaktopplysning"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Kontaktopplysning")

    id: Union[str, KontaktopplysningId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KontaktopplysningId):
            self.id = KontaktopplysningId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Standard(YAMLRoot):
    """
    Ein standard (dct:Standard).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["Standard"]
    class_class_curie: ClassVar[str] = "dct:Standard"
    class_name: ClassVar[str] = "Standard"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Standard")

    id: Union[str, StandardId] = None
    tittel: Union[str, list[str]] = None
    har_referanse: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
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

        if not isinstance(self.har_referanse, list):
            self.har_referanse = [self.har_referanse] if self.har_referanse is not None else []
        self.har_referanse = [v if isinstance(v, URI) else URI(v) for v in self.har_referanse]

        if self.har_versjonsnummer is not None and not isinstance(self.har_versjonsnummer, str):
            self.har_versjonsnummer = str(self.har_versjonsnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Lisensdokument(YAMLRoot):
    """
    Eit lisensdokument (dct:LicenseDocument).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["LicenseDocument"]
    class_class_curie: ClassVar[str] = "dct:LicenseDocument"
    class_name: ClassVar[str] = "Lisensdokument"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Lisensdokument")

    id: Union[str, LisensdokumentId] = None
    type_concept: Optional[Union[str, KonseptId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LisensdokumentId):
            self.id = LisensdokumentId(self.id)

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Lokasjon(YAMLRoot):
    """
    Eit geografisk område (dct:Location).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["Location"]
    class_class_curie: ClassVar[str] = "dct:Location"
    class_name: ClassVar[str] = "Lokasjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Lokasjon")

    id: Union[str, LokasjonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LokasjonId):
            self.id = LokasjonId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tidsperiode(YAMLRoot):
    """
    Eit tidsintervall med start- og sluttdato.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["PeriodOfTime"]
    class_class_curie: ClassVar[str] = "dct:PeriodOfTime"
    class_name: ClassVar[str] = "Tidsperiode"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Tidsperiode")

    id: Union[str, TidsperiodeId] = None
    startdato: Optional[Union[str, XSDDate]] = None
    sluttdato: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TidsperiodeId):
            self.id = TidsperiodeId(self.id)

        if self.startdato is not None and not isinstance(self.startdato, XSDDate):
            self.startdato = XSDDate(self.startdato)

        if self.sluttdato is not None and not isinstance(self.sluttdato, XSDDate):
            self.sluttdato = XSDDate(self.sluttdato)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dokument(YAMLRoot):
    """
    Eit dokument (foaf:Document).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Document"]
    class_class_curie: ClassVar[str] = "foaf:Document"
    class_name: ClassVar[str] = "Dokument"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Dokument")

    id: Union[str, DokumentId] = None
    tittel: Optional[Union[str, list[str]]] = empty_list()
    spraak: Optional[Union[str, list[str]]] = empty_list()
    format: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DokumentId):
            self.id = DokumentId(self.id)

        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Modellkatalog(YAMLRoot):
    """
    Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Catalog"]
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "Modellkatalog"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Modellkatalog")

    id: Union[str, ModellkatalogId] = None
    tittel: Union[str, list[str]] = None
    beskrivelse: Union[str, list[str]] = None
    har_del: Union[Union[str, KatalogisertRessursId], list[Union[str, KatalogisertRessursId]]] = None
    identifikator_literal: str = None
    kontaktpunkt: Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]] = None
    utgiver: Union[str, AktorId] = None
    endringsdato: Optional[Union[str, XSDDate]] = None
    heimeside: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    lisens: Optional[Union[str, LisensdokumentId]] = None
    modell: Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]] = empty_list()
    spraak: Optional[Union[str, list[str]]] = empty_list()
    tema: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    temaer: Optional[Union[Union[str, BegrepssamlingId], list[Union[str, BegrepssamlingId]]]] = empty_list()
    utgivelsesdato: Optional[Union[str, XSDDate]] = None
    er_del_av_katalog: Optional[Union[str, ModellkatalogId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModellkatalogId):
            self.id = ModellkatalogId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.beskrivelse):
            self.MissingRequiredField("beskrivelse")
        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self._is_empty(self.har_del):
            self.MissingRequiredField("har_del")
        if not isinstance(self.har_del, list):
            self.har_del = [self.har_del] if self.har_del is not None else []
        self.har_del = [v if isinstance(v, KatalogisertRessursId) else KatalogisertRessursId(v) for v in self.har_del]

        if self._is_empty(self.identifikator_literal):
            self.MissingRequiredField("identifikator_literal")
        if not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self._is_empty(self.kontaktpunkt):
            self.MissingRequiredField("kontaktpunkt")
        if not isinstance(self.kontaktpunkt, list):
            self.kontaktpunkt = [self.kontaktpunkt] if self.kontaktpunkt is not None else []
        self.kontaktpunkt = [v if isinstance(v, KontaktopplysningId) else KontaktopplysningId(v) for v in self.kontaktpunkt]

        if self._is_empty(self.utgiver):
            self.MissingRequiredField("utgiver")
        if not isinstance(self.utgiver, AktorId):
            self.utgiver = AktorId(self.utgiver)

        if self.endringsdato is not None and not isinstance(self.endringsdato, XSDDate):
            self.endringsdato = XSDDate(self.endringsdato)

        if not isinstance(self.heimeside, list):
            self.heimeside = [self.heimeside] if self.heimeside is not None else []
        self.heimeside = [v if isinstance(v, URI) else URI(v) for v in self.heimeside]

        if self.lisens is not None and not isinstance(self.lisens, LisensdokumentId):
            self.lisens = LisensdokumentId(self.lisens)

        if not isinstance(self.modell, list):
            self.modell = [self.modell] if self.modell is not None else []
        self.modell = [v if isinstance(v, InformasjonsmodellId) else InformasjonsmodellId(v) for v in self.modell]

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

        if not isinstance(self.tema, list):
            self.tema = [self.tema] if self.tema is not None else []
        self.tema = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.tema]

        if not isinstance(self.temaer, list):
            self.temaer = [self.temaer] if self.temaer is not None else []
        self.temaer = [v if isinstance(v, BegrepssamlingId) else BegrepssamlingId(v) for v in self.temaer]

        if self.utgivelsesdato is not None and not isinstance(self.utgivelsesdato, XSDDate):
            self.utgivelsesdato = XSDDate(self.utgivelsesdato)

        if self.er_del_av_katalog is not None and not isinstance(self.er_del_av_katalog, ModellkatalogId):
            self.er_del_av_katalog = ModellkatalogId(self.er_del_av_katalog)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Informasjonsmodell(YAMLRoot):
    """
    Ein informasjonsmodell som er katalogisert i ein modellkatalog (modelldcatno:InformationModel).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["InformationModel"]
    class_class_curie: ClassVar[str] = "modelldcatno:InformationModel"
    class_name: ClassVar[str] = "Informasjonsmodell"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Informasjonsmodell")

    id: Union[str, InformasjonsmodellId] = None
    tittel: Union[str, list[str]] = None
    utgiver: Union[str, AktorId] = None
    begrep: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()
    identifikator_literal: Optional[str] = None
    informasjonsmodellidentifikator: Optional[str] = None
    inneholder_modellelement: Optional[Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]]] = empty_list()
    kontaktpunkt: Optional[Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]]] = empty_list()
    lisens: Optional[Union[str, LisensdokumentId]] = None
    tema: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    dekningsomraade: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    endringsdato: Optional[Union[str, XSDDate]] = None
    er_del_av_modell: Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]] = empty_list()
    er_profil_av: Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]] = empty_list()
    er_erstatta_av: Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]] = empty_list()
    erstatter: Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]] = empty_list()
    har_del_modell: Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]] = empty_list()
    har_format: Optional[Union[Union[str, DokumentId], list[Union[str, DokumentId]]]] = empty_list()
    tidsperiode: Optional[Union[Union[str, TidsperiodeId], list[Union[str, TidsperiodeId]]]] = empty_list()
    heimeside: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    er_i_samsvar_med: Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]] = empty_list()
    status: Optional[Union[str, KonseptId]] = None
    nokkelord: Optional[Union[str, list[str]]] = empty_list()
    skapar: Optional[Union[str, AktorId]] = None
    spraak: Optional[Union[str, list[str]]] = empty_list()
    type_concept: Optional[Union[str, KonseptId]] = None
    utgivelsesdato: Optional[Union[str, XSDDate]] = None
    har_versjonsnummer: Optional[str] = None
    versjonsmerknad: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformasjonsmodellId):
            self.id = InformasjonsmodellId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self._is_empty(self.utgiver):
            self.MissingRequiredField("utgiver")
        if not isinstance(self.utgiver, AktorId):
            self.utgiver = AktorId(self.utgiver)

        if not isinstance(self.begrep, list):
            self.begrep = [self.begrep] if self.begrep is not None else []
        self.begrep = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.begrep]

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self.informasjonsmodellidentifikator is not None and not isinstance(self.informasjonsmodellidentifikator, str):
            self.informasjonsmodellidentifikator = str(self.informasjonsmodellidentifikator)

        if not isinstance(self.inneholder_modellelement, list):
            self.inneholder_modellelement = [self.inneholder_modellelement] if self.inneholder_modellelement is not None else []
        self.inneholder_modellelement = [v if isinstance(v, ModellelementId) else ModellelementId(v) for v in self.inneholder_modellelement]

        if not isinstance(self.kontaktpunkt, list):
            self.kontaktpunkt = [self.kontaktpunkt] if self.kontaktpunkt is not None else []
        self.kontaktpunkt = [v if isinstance(v, KontaktopplysningId) else KontaktopplysningId(v) for v in self.kontaktpunkt]

        if self.lisens is not None and not isinstance(self.lisens, LisensdokumentId):
            self.lisens = LisensdokumentId(self.lisens)

        if not isinstance(self.tema, list):
            self.tema = [self.tema] if self.tema is not None else []
        self.tema = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.tema]

        if not isinstance(self.dekningsomraade, list):
            self.dekningsomraade = [self.dekningsomraade] if self.dekningsomraade is not None else []
        self.dekningsomraade = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.dekningsomraade]

        if self.endringsdato is not None and not isinstance(self.endringsdato, XSDDate):
            self.endringsdato = XSDDate(self.endringsdato)

        if not isinstance(self.er_del_av_modell, list):
            self.er_del_av_modell = [self.er_del_av_modell] if self.er_del_av_modell is not None else []
        self.er_del_av_modell = [v if isinstance(v, InformasjonsmodellId) else InformasjonsmodellId(v) for v in self.er_del_av_modell]

        if not isinstance(self.er_profil_av, list):
            self.er_profil_av = [self.er_profil_av] if self.er_profil_av is not None else []
        self.er_profil_av = [v if isinstance(v, StandardId) else StandardId(v) for v in self.er_profil_av]

        if not isinstance(self.er_erstatta_av, list):
            self.er_erstatta_av = [self.er_erstatta_av] if self.er_erstatta_av is not None else []
        self.er_erstatta_av = [v if isinstance(v, InformasjonsmodellId) else InformasjonsmodellId(v) for v in self.er_erstatta_av]

        if not isinstance(self.erstatter, list):
            self.erstatter = [self.erstatter] if self.erstatter is not None else []
        self.erstatter = [v if isinstance(v, InformasjonsmodellId) else InformasjonsmodellId(v) for v in self.erstatter]

        if not isinstance(self.har_del_modell, list):
            self.har_del_modell = [self.har_del_modell] if self.har_del_modell is not None else []
        self.har_del_modell = [v if isinstance(v, InformasjonsmodellId) else InformasjonsmodellId(v) for v in self.har_del_modell]

        if not isinstance(self.har_format, list):
            self.har_format = [self.har_format] if self.har_format is not None else []
        self.har_format = [v if isinstance(v, DokumentId) else DokumentId(v) for v in self.har_format]

        if not isinstance(self.tidsperiode, list):
            self.tidsperiode = [self.tidsperiode] if self.tidsperiode is not None else []
        self.tidsperiode = [v if isinstance(v, TidsperiodeId) else TidsperiodeId(v) for v in self.tidsperiode]

        if not isinstance(self.heimeside, list):
            self.heimeside = [self.heimeside] if self.heimeside is not None else []
        self.heimeside = [v if isinstance(v, URI) else URI(v) for v in self.heimeside]

        if not isinstance(self.er_i_samsvar_med, list):
            self.er_i_samsvar_med = [self.er_i_samsvar_med] if self.er_i_samsvar_med is not None else []
        self.er_i_samsvar_med = [v if isinstance(v, StandardId) else StandardId(v) for v in self.er_i_samsvar_med]

        if self.status is not None and not isinstance(self.status, KonseptId):
            self.status = KonseptId(self.status)

        if not isinstance(self.nokkelord, list):
            self.nokkelord = [self.nokkelord] if self.nokkelord is not None else []
        self.nokkelord = [v if isinstance(v, str) else str(v) for v in self.nokkelord]

        if self.skapar is not None and not isinstance(self.skapar, AktorId):
            self.skapar = AktorId(self.skapar)

        if not isinstance(self.spraak, list):
            self.spraak = [self.spraak] if self.spraak is not None else []
        self.spraak = [v if isinstance(v, str) else str(v) for v in self.spraak]

        if self.type_concept is not None and not isinstance(self.type_concept, KonseptId):
            self.type_concept = KonseptId(self.type_concept)

        if self.utgivelsesdato is not None and not isinstance(self.utgivelsesdato, XSDDate):
            self.utgivelsesdato = XSDDate(self.utgivelsesdato)

        if self.har_versjonsnummer is not None and not isinstance(self.har_versjonsnummer, str):
            self.har_versjonsnummer = str(self.har_versjonsnummer)

        if not isinstance(self.versjonsmerknad, list):
            self.versjonsmerknad = [self.versjonsmerknad] if self.versjonsmerknad is not None else []
        self.versjonsmerknad = [v if isinstance(v, str) else str(v) for v in self.versjonsmerknad]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Modellelement(YAMLRoot):
    """
    Abstrakt basisklasse for alle modellelement i ein informasjonsmodell.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["ModelElement"]
    class_class_curie: ClassVar[str] = "modelldcatno:ModelElement"
    class_name: ClassVar[str] = "Modellelement"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Modellelement")

    id: Union[str, ModellelementId] = None
    tittel: Union[str, list[str]] = None
    begrep: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    identifikator_literal: Optional[str] = None
    har_eigenskap: Optional[Union[Union[str, EigenskapId], list[Union[str, EigenskapId]]]] = empty_list()
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()
    tilhorer_modul: Optional[Union[Union[str, ModulId], list[Union[str, ModulId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModellelementId):
            self.id = ModellelementId(self.id)

        if self._is_empty(self.tittel):
            self.MissingRequiredField("tittel")
        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if not isinstance(self.begrep, list):
            self.begrep = [self.begrep] if self.begrep is not None else []
        self.begrep = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.begrep]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if not isinstance(self.har_eigenskap, list):
            self.har_eigenskap = [self.har_eigenskap] if self.har_eigenskap is not None else []
        self.har_eigenskap = [v if isinstance(v, EigenskapId) else EigenskapId(v) for v in self.har_eigenskap]

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if not isinstance(self.tilhorer_modul, list):
            self.tilhorer_modul = [self.tilhorer_modul] if self.tilhorer_modul is not None else []
        self.tilhorer_modul = [v if isinstance(v, ModulId) else ModulId(v) for v in self.tilhorer_modul]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Objekttype(Modellelement):
    """
    Ein objekttype — ein klasse med eigenskapar i informasjonsmodellen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["ObjectType"]
    class_class_curie: ClassVar[str] = "modelldcatno:ObjectType"
    class_name: ClassVar[str] = "Objekttype"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Objekttype")

    id: Union[str, ObjekttypeId] = None
    tittel: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObjekttypeId):
            self.id = ObjekttypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RootObjekttype(Modellelement):
    """
    Ein rotobjekttype — toppnivå-klasse i informasjonsmodellen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["RootObjectType"]
    class_class_curie: ClassVar[str] = "modelldcatno:RootObjectType"
    class_name: ClassVar[str] = "RootObjekttype"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/RootObjekttype")

    id: Union[str, RootObjekttypeId] = None
    tittel: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RootObjekttypeId):
            self.id = RootObjekttypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Datatype(Modellelement):
    """
    Ein datatype — ein strukturert samansett type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["DataType"]
    class_class_curie: ClassVar[str] = "modelldcatno:DataType"
    class_name: ClassVar[str] = "Datatype"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Datatype")

    id: Union[str, DatatypeId] = None
    tittel: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatatypeId):
            self.id = DatatypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnkelType(Modellelement):
    """
    Ein enkel type med restriksjonar (xsd-fasettar).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["SimpleType"]
    class_class_curie: ClassVar[str] = "modelldcatno:SimpleType"
    class_name: ClassVar[str] = "EnkelType"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/EnkelType")

    id: Union[str, EnkelTypeId] = None
    tittel: Union[str, list[str]] = None
    typedefinisjon_referanse: Optional[Union[str, URI]] = None
    fraksjonssifre: Optional[int] = None
    lengde: Optional[int] = None
    maks_eksklusiv: Optional[str] = None
    maks_inklusiv: Optional[str] = None
    maks_lengde: Optional[int] = None
    min_eksklusiv: Optional[str] = None
    min_inklusiv: Optional[str] = None
    min_lengde: Optional[int] = None
    monster: Optional[str] = None
    totalt_sifre: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnkelTypeId):
            self.id = EnkelTypeId(self.id)

        if self.typedefinisjon_referanse is not None and not isinstance(self.typedefinisjon_referanse, URI):
            self.typedefinisjon_referanse = URI(self.typedefinisjon_referanse)

        if self.fraksjonssifre is not None and not isinstance(self.fraksjonssifre, int):
            self.fraksjonssifre = int(self.fraksjonssifre)

        if self.lengde is not None and not isinstance(self.lengde, int):
            self.lengde = int(self.lengde)

        if self.maks_eksklusiv is not None and not isinstance(self.maks_eksklusiv, str):
            self.maks_eksklusiv = str(self.maks_eksklusiv)

        if self.maks_inklusiv is not None and not isinstance(self.maks_inklusiv, str):
            self.maks_inklusiv = str(self.maks_inklusiv)

        if self.maks_lengde is not None and not isinstance(self.maks_lengde, int):
            self.maks_lengde = int(self.maks_lengde)

        if self.min_eksklusiv is not None and not isinstance(self.min_eksklusiv, str):
            self.min_eksklusiv = str(self.min_eksklusiv)

        if self.min_inklusiv is not None and not isinstance(self.min_inklusiv, str):
            self.min_inklusiv = str(self.min_inklusiv)

        if self.min_lengde is not None and not isinstance(self.min_lengde, int):
            self.min_lengde = int(self.min_lengde)

        if self.monster is not None and not isinstance(self.monster, str):
            self.monster = str(self.monster)

        if self.totalt_sifre is not None and not isinstance(self.totalt_sifre, int):
            self.totalt_sifre = int(self.totalt_sifre)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kodeliste(Modellelement):
    """
    Ei kodeliste — eit kontrollert vokabular av tillate verdiar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["CodeList"]
    class_class_curie: ClassVar[str] = "modelldcatno:CodeList"
    class_name: ClassVar[str] = "Kodeliste"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Kodeliste")

    id: Union[str, KodelisteId] = None
    tittel: Union[str, list[str]] = None
    har_referanse: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KodelisteId):
            self.id = KodelisteId(self.id)

        if not isinstance(self.har_referanse, list):
            self.har_referanse = [self.har_referanse] if self.har_referanse is not None else []
        self.har_referanse = [v if isinstance(v, URI) else URI(v) for v in self.har_referanse]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Modul(Modellelement):
    """
    Ein modul som grupperer modellelement i informasjonsmodellen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Module"]
    class_class_curie: ClassVar[str] = "modelldcatno:Module"
    class_name: ClassVar[str] = "Modul"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Modul")

    id: Union[str, ModulId] = None
    tittel: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModulId):
            self.id = ModulId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Eigenskap(YAMLRoot):
    """
    Abstrakt basisklasse for eigenskapar knytt til eit modellelement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Property"]
    class_class_curie: ClassVar[str] = "modelldcatno:Property"
    class_name: ClassVar[str] = "Eigenskap"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Eigenskap")

    id: Union[str, EigenskapId] = None
    begrep: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    identifikator_literal: Optional[str] = None
    navigerbar: Optional[Union[bool, Bool]] = None
    min_multiplisitet: Optional[int] = None
    tittel: Optional[Union[str, list[str]]] = empty_list()
    maks_multiplisitet: Optional[str] = None
    beskrivelse: Optional[Union[str, list[str]]] = empty_list()
    har_type: Optional[Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]]] = empty_list()
    relasjonsegenskapetikett: Optional[Union[str, list[str]]] = empty_list()
    sekvensnummer: Optional[int] = None
    tilhorer_modul: Optional[Union[Union[str, ModulId], list[Union[str, ModulId]]]] = empty_list()
    danner_symmetri_med: Optional[Union[str, EigenskapId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EigenskapId):
            self.id = EigenskapId(self.id)

        if not isinstance(self.begrep, list):
            self.begrep = [self.begrep] if self.begrep is not None else []
        self.begrep = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.begrep]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if self.navigerbar is not None and not isinstance(self.navigerbar, Bool):
            self.navigerbar = Bool(self.navigerbar)

        if self.min_multiplisitet is not None and not isinstance(self.min_multiplisitet, int):
            self.min_multiplisitet = int(self.min_multiplisitet)

        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if self.maks_multiplisitet is not None and not isinstance(self.maks_multiplisitet, str):
            self.maks_multiplisitet = str(self.maks_multiplisitet)

        if not isinstance(self.beskrivelse, list):
            self.beskrivelse = [self.beskrivelse] if self.beskrivelse is not None else []
        self.beskrivelse = [v if isinstance(v, str) else str(v) for v in self.beskrivelse]

        if not isinstance(self.har_type, list):
            self.har_type = [self.har_type] if self.har_type is not None else []
        self.har_type = [v if isinstance(v, ModellelementId) else ModellelementId(v) for v in self.har_type]

        if not isinstance(self.relasjonsegenskapetikett, list):
            self.relasjonsegenskapetikett = [self.relasjonsegenskapetikett] if self.relasjonsegenskapetikett is not None else []
        self.relasjonsegenskapetikett = [v if isinstance(v, str) else str(v) for v in self.relasjonsegenskapetikett]

        if self.sekvensnummer is not None and not isinstance(self.sekvensnummer, int):
            self.sekvensnummer = int(self.sekvensnummer)

        if not isinstance(self.tilhorer_modul, list):
            self.tilhorer_modul = [self.tilhorer_modul] if self.tilhorer_modul is not None else []
        self.tilhorer_modul = [v if isinstance(v, ModulId) else ModulId(v) for v in self.tilhorer_modul]

        if self.danner_symmetri_med is not None and not isinstance(self.danner_symmetri_med, EigenskapId):
            self.danner_symmetri_med = EigenskapId(self.danner_symmetri_med)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Attributt(Eigenskap):
    """
    Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Attribute"]
    class_class_curie: ClassVar[str] = "modelldcatno:Attribute"
    class_name: ClassVar[str] = "Attributt"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Attributt")

    id: Union[str, AttributtId] = None
    har_datatype: Optional[Union[Union[str, DatatypeId], list[Union[str, DatatypeId]]]] = empty_list()
    har_enkel_type: Optional[Union[Union[str, EnkelTypeId], list[Union[str, EnkelTypeId]]]] = empty_list()
    har_verdi_fra: Optional[Union[Union[str, KodelisteId], list[Union[str, KodelisteId]]]] = empty_list()
    inneholder_objekttype: Optional[Union[Union[str, ObjekttypeId], list[Union[str, ObjekttypeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AttributtId):
            self.id = AttributtId(self.id)

        if not isinstance(self.har_datatype, list):
            self.har_datatype = [self.har_datatype] if self.har_datatype is not None else []
        self.har_datatype = [v if isinstance(v, DatatypeId) else DatatypeId(v) for v in self.har_datatype]

        if not isinstance(self.har_enkel_type, list):
            self.har_enkel_type = [self.har_enkel_type] if self.har_enkel_type is not None else []
        self.har_enkel_type = [v if isinstance(v, EnkelTypeId) else EnkelTypeId(v) for v in self.har_enkel_type]

        if not isinstance(self.har_verdi_fra, list):
            self.har_verdi_fra = [self.har_verdi_fra] if self.har_verdi_fra is not None else []
        self.har_verdi_fra = [v if isinstance(v, KodelisteId) else KodelisteId(v) for v in self.har_verdi_fra]

        if not isinstance(self.inneholder_objekttype, list):
            self.inneholder_objekttype = [self.inneholder_objekttype] if self.inneholder_objekttype is not None else []
        self.inneholder_objekttype = [v if isinstance(v, ObjekttypeId) else ObjekttypeId(v) for v in self.inneholder_objekttype]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Assosiasjon(Eigenskap):
    """
    Ein assosiasjon — ein eigenskap som refererer til eit anna modellelement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Association"]
    class_class_curie: ClassVar[str] = "modelldcatno:Association"
    class_name: ClassVar[str] = "Assosiasjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Assosiasjon")

    id: Union[str, AssosiasjonId] = None
    refererer_til: Optional[Union[str, ModellelementId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssosiasjonId):
            self.id = AssosiasjonId(self.id)

        if self.refererer_til is not None and not isinstance(self.refererer_til, ModellelementId):
            self.refererer_til = ModellelementId(self.refererer_til)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rolle(Eigenskap):
    """
    Ein rolle — ein eigenskap som knyter ein objekttype til ein assosiasjon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Role"]
    class_class_curie: ClassVar[str] = "modelldcatno:Role"
    class_name: ClassVar[str] = "Rolle"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Rolle")

    id: Union[str, RolleId] = None
    har_objekttype: Optional[Union[str, ObjekttypeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RolleId):
            self.id = RolleId(self.id)

        if self.har_objekttype is not None and not isinstance(self.har_objekttype, ObjekttypeId):
            self.har_objekttype = ObjekttypeId(self.har_objekttype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Spesialisering(Eigenskap):
    """
    Ein spesialisering — eit arveforhold frå eit spesielt til eit generelt modellelement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Specialization"]
    class_class_curie: ClassVar[str] = "modelldcatno:Specialization"
    class_name: ClassVar[str] = "Spesialisering"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Spesialisering")

    id: Union[str, SpesialiseringId] = None
    har_generelt_begrep: Optional[Union[str, ModellelementId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpesialiseringId):
            self.id = SpesialiseringId(self.id)

        if self.har_generelt_begrep is not None and not isinstance(self.har_generelt_begrep, ModellelementId):
            self.har_generelt_begrep = ModellelementId(self.har_generelt_begrep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sammensetning(Eigenskap):
    """
    Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Composition"]
    class_class_curie: ClassVar[str] = "modelldcatno:Composition"
    class_name: ClassVar[str] = "Sammensetning"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Sammensetning")

    id: Union[str, SammensetningId] = None
    inneholder: Optional[Union[str, ModellelementId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SammensetningId):
            self.id = SammensetningId(self.id)

        if self.inneholder is not None and not isinstance(self.inneholder, ModellelementId):
            self.inneholder = ModellelementId(self.inneholder)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Realisering(Eigenskap):
    """
    Ein realisering — ein implementasjonsrelasjon mellom modellelement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Realization"]
    class_class_curie: ClassVar[str] = "modelldcatno:Realization"
    class_name: ClassVar[str] = "Realisering"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Realisering")

    id: Union[str, RealiseringId] = None
    har_leverandor: Optional[Union[str, ModellelementId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RealiseringId):
            self.id = RealiseringId(self.id)

        if self.har_leverandor is not None and not isinstance(self.har_leverandor, ModellelementId):
            self.har_leverandor = ModellelementId(self.har_leverandor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Abstraksjon(Eigenskap):
    """
    Ein abstraksjon — ein forenkling som representerer eit modellelement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Abstraction"]
    class_class_curie: ClassVar[str] = "modelldcatno:Abstraction"
    class_name: ClassVar[str] = "Abstraksjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Abstraksjon")

    id: Union[str, AbstraksjonId] = None
    er_abstraksjon_av: Optional[Union[str, ModellelementId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AbstraksjonId):
            self.id = AbstraksjonId(self.id)

        if self.er_abstraksjon_av is not None and not isinstance(self.er_abstraksjon_av, ModellelementId):
            self.er_abstraksjon_av = ModellelementId(self.er_abstraksjon_av)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Avhengighet(Eigenskap):
    """
    Ein avhengighet — ein relasjon der det eine modellelementet avheng av det andre.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Dependency"]
    class_class_curie: ClassVar[str] = "modelldcatno:Dependency"
    class_name: ClassVar[str] = "Avhengighet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Avhengighet")

    id: Union[str, AvhengighetId] = None
    avhengig_av: Optional[Union[str, ModellelementId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AvhengighetId):
            self.id = AvhengighetId(self.id)

        if self.avhengig_av is not None and not isinstance(self.avhengig_av, ModellelementId):
            self.avhengig_av = ModellelementId(self.avhengig_av)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Samling(Eigenskap):
    """
    Ein samling — ein eigenskap som representerer ei uordna mengd av modellelement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Collection"]
    class_class_curie: ClassVar[str] = "modelldcatno:Collection"
    class_name: ClassVar[str] = "Samling"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Samling")

    id: Union[str, SamlingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SamlingId):
            self.id = SamlingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Valg(Eigenskap):
    """
    Eit val — ein eigenskap som representerer eit val mellom modellelement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Choice"]
    class_class_curie: ClassVar[str] = "modelldcatno:Choice"
    class_name: ClassVar[str] = "Valg"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Valg")

    id: Union[str, ValgId] = None
    har_noe: Optional[Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ValgId):
            self.id = ValgId(self.id)

        if not isinstance(self.har_noe, list):
            self.har_noe = [self.har_noe] if self.har_noe is not None else []
        self.har_noe = [v if isinstance(v, ModellelementId) else ModellelementId(v) for v in self.har_noe]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlleAv(Valg):
    """
    Alle av — alle modellelementa i lista må gjelde (logisk OG-mengd).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["AllOf"]
    class_class_curie: ClassVar[str] = "modelldcatno:AllOf"
    class_name: ClassVar[str] = "AlleAv"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/AlleAv")

    id: Union[str, AlleAvId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlleAvId):
            self.id = AlleAvId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NoenAv(Valg):
    """
    Nokon av — minst eitt modellelement i lista må gjelde (logisk ELLER-mengd).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["AnyOf"]
    class_class_curie: ClassVar[str] = "modelldcatno:AnyOf"
    class_name: ClassVar[str] = "NoenAv"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/NoenAv")

    id: Union[str, NoenAvId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoenAvId):
            self.id = NoenAvId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Merknad(YAMLRoot):
    """
    Ei merknad knytt til eit modellelement eller eigenskap.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Note"]
    class_class_curie: ClassVar[str] = "modelldcatno:Note"
    class_name: ClassVar[str] = "Merknad"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Merknad")

    id: Union[str, MerknadId] = None
    annoterer: Optional[Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]]] = empty_list()
    eigenskapsmerknad: Optional[Union[str, list[str]]] = empty_list()
    identifikator_literal: Optional[str] = None
    tittel: Optional[Union[str, list[str]]] = empty_list()
    tilhorer_modul: Optional[Union[Union[str, ModulId], list[Union[str, ModulId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MerknadId):
            self.id = MerknadId(self.id)

        if not isinstance(self.annoterer, list):
            self.annoterer = [self.annoterer] if self.annoterer is not None else []
        self.annoterer = [v if isinstance(v, ModellelementId) else ModellelementId(v) for v in self.annoterer]

        if not isinstance(self.eigenskapsmerknad, list):
            self.eigenskapsmerknad = [self.eigenskapsmerknad] if self.eigenskapsmerknad is not None else []
        self.eigenskapsmerknad = [v if isinstance(v, str) else str(v) for v in self.eigenskapsmerknad]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if not isinstance(self.tittel, list):
            self.tittel = [self.tittel] if self.tittel is not None else []
        self.tittel = [v if isinstance(v, str) else str(v) for v in self.tittel]

        if not isinstance(self.tilhorer_modul, list):
            self.tilhorer_modul = [self.tilhorer_modul] if self.tilhorer_modul is not None else []
        self.tilhorer_modul = [v if isinstance(v, ModulId) else ModulId(v) for v in self.tilhorer_modul]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Betingelsesregel(Merknad):
    """
    Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskapar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["ConstraintRule"]
    class_class_curie: ClassVar[str] = "modelldcatno:ConstraintRule"
    class_name: ClassVar[str] = "Betingelsesregel"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Betingelsesregel")

    id: Union[str, BetingelsesregelId] = None
    betinger: Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]] = None
    betingelsesuttrykk: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BetingelsesregelId):
            self.id = BetingelsesregelId(self.id)

        if self._is_empty(self.betinger):
            self.MissingRequiredField("betinger")
        if not isinstance(self.betinger, list):
            self.betinger = [self.betinger] if self.betinger is not None else []
        self.betinger = [v if isinstance(v, ModellelementId) else ModellelementId(v) for v in self.betinger]

        if not isinstance(self.betingelsesuttrykk, list):
            self.betingelsesuttrykk = [self.betingelsesuttrykk] if self.betingelsesuttrykk is not None else []
        self.betingelsesuttrykk = [v if isinstance(v, str) else str(v) for v in self.betingelsesuttrykk]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Og(Betingelsesregel):
    """
    Og — logisk OG-betingelse; alle deltakande modellelement må gjelde.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["And"]
    class_class_curie: ClassVar[str] = "modelldcatno:And"
    class_name: ClassVar[str] = "Og"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Og")

    id: Union[str, OgId] = None
    betinger: Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OgId):
            self.id = OgId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Eller(Betingelsesregel):
    """
    Eller — logisk ELLER-betingelse; minst eitt modellelement må gjelde.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Or"]
    class_class_curie: ClassVar[str] = "modelldcatno:Or"
    class_name: ClassVar[str] = "Eller"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Eller")

    id: Union[str, EllerId] = None
    betinger: Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EllerId):
            self.id = EllerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XEllerY(Betingelsesregel):
    """
    Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Xor"]
    class_class_curie: ClassVar[str] = "modelldcatno:Xor"
    class_name: ClassVar[str] = "XEllerY"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/XEllerY")

    id: Union[str, XEllerYId] = None
    betinger: Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XEllerYId):
            self.id = XEllerYId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ikke(Betingelsesregel):
    """
    Ikkje — negasjon; modellelementet det refererer til må ikkje gjelde.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["Not"]
    class_class_curie: ClassVar[str] = "modelldcatno:Not"
    class_name: ClassVar[str] = "Ikke"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Ikke")

    id: Union[str, IkkeId] = None
    betinger: Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IkkeId):
            self.id = IkkeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kodeelement(YAMLRoot):
    """
    Eit element i ei kodeliste (modelldcatno:CodeElement).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MODELLDCATNO["CodeElement"]
    class_class_curie: ClassVar[str] = "modelldcatno:CodeElement"
    class_name: ClassVar[str] = "Kodeelement"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Kodeelement")

    id: Union[str, KodeelementId] = None
    i_skjema: Union[Union[str, KodelisteId], list[Union[str, KodelisteId]]] = None
    notasjon: str = None
    anbefalt_term: Optional[Union[str, list[str]]] = empty_list()
    begrep: Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]] = empty_list()
    identifikator_literal: Optional[str] = None
    topp_begrep_av: Optional[Union[Union[str, KodelisteId], list[Union[str, KodelisteId]]]] = empty_list()
    definisjon: Optional[Union[str, list[str]]] = empty_list()
    eksempel_kode: Optional[Union[str, list[str]]] = empty_list()
    eksklusjonsnotat: Optional[Union[str, list[str]]] = empty_list()
    forrige: Optional[Union[str, KodeelementId]] = None
    skjult_term: Optional[Union[str, list[str]]] = empty_list()
    inklusjonsnotat: Optional[Union[str, list[str]]] = empty_list()
    notat: Optional[Union[str, list[str]]] = empty_list()
    neste: Optional[Union[str, KodeelementId]] = None
    omfangsnotat: Optional[Union[str, list[str]]] = empty_list()
    alternativ_term: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KodeelementId):
            self.id = KodeelementId(self.id)

        if self._is_empty(self.i_skjema):
            self.MissingRequiredField("i_skjema")
        if not isinstance(self.i_skjema, list):
            self.i_skjema = [self.i_skjema] if self.i_skjema is not None else []
        self.i_skjema = [v if isinstance(v, KodelisteId) else KodelisteId(v) for v in self.i_skjema]

        if self._is_empty(self.notasjon):
            self.MissingRequiredField("notasjon")
        if not isinstance(self.notasjon, str):
            self.notasjon = str(self.notasjon)

        if not isinstance(self.anbefalt_term, list):
            self.anbefalt_term = [self.anbefalt_term] if self.anbefalt_term is not None else []
        self.anbefalt_term = [v if isinstance(v, str) else str(v) for v in self.anbefalt_term]

        if not isinstance(self.begrep, list):
            self.begrep = [self.begrep] if self.begrep is not None else []
        self.begrep = [v if isinstance(v, KonseptId) else KonseptId(v) for v in self.begrep]

        if self.identifikator_literal is not None and not isinstance(self.identifikator_literal, str):
            self.identifikator_literal = str(self.identifikator_literal)

        if not isinstance(self.topp_begrep_av, list):
            self.topp_begrep_av = [self.topp_begrep_av] if self.topp_begrep_av is not None else []
        self.topp_begrep_av = [v if isinstance(v, KodelisteId) else KodelisteId(v) for v in self.topp_begrep_av]

        if not isinstance(self.definisjon, list):
            self.definisjon = [self.definisjon] if self.definisjon is not None else []
        self.definisjon = [v if isinstance(v, str) else str(v) for v in self.definisjon]

        if not isinstance(self.eksempel_kode, list):
            self.eksempel_kode = [self.eksempel_kode] if self.eksempel_kode is not None else []
        self.eksempel_kode = [v if isinstance(v, str) else str(v) for v in self.eksempel_kode]

        if not isinstance(self.eksklusjonsnotat, list):
            self.eksklusjonsnotat = [self.eksklusjonsnotat] if self.eksklusjonsnotat is not None else []
        self.eksklusjonsnotat = [v if isinstance(v, str) else str(v) for v in self.eksklusjonsnotat]

        if self.forrige is not None and not isinstance(self.forrige, KodeelementId):
            self.forrige = KodeelementId(self.forrige)

        if not isinstance(self.skjult_term, list):
            self.skjult_term = [self.skjult_term] if self.skjult_term is not None else []
        self.skjult_term = [v if isinstance(v, str) else str(v) for v in self.skjult_term]

        if not isinstance(self.inklusjonsnotat, list):
            self.inklusjonsnotat = [self.inklusjonsnotat] if self.inklusjonsnotat is not None else []
        self.inklusjonsnotat = [v if isinstance(v, str) else str(v) for v in self.inklusjonsnotat]

        if not isinstance(self.notat, list):
            self.notat = [self.notat] if self.notat is not None else []
        self.notat = [v if isinstance(v, str) else str(v) for v in self.notat]

        if self.neste is not None and not isinstance(self.neste, KodeelementId):
            self.neste = KodeelementId(self.neste)

        if not isinstance(self.omfangsnotat, list):
            self.omfangsnotat = [self.omfangsnotat] if self.omfangsnotat is not None else []
        self.omfangsnotat = [v if isinstance(v, str) else str(v) for v in self.omfangsnotat]

        if not isinstance(self.alternativ_term, list):
            self.alternativ_term = [self.alternativ_term] if self.alternativ_term is not None else []
        self.alternativ_term = [v if isinstance(v, str) else str(v) for v in self.alternativ_term]

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Mediatype")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Konsept")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/ap-no/modelldcat-ap-no/Begrepssamling")

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

slots.namn_aktor = Slot(uri=FOAF.name, name="namn_aktor", curie=FOAF.curie('name'),
                   model_uri=DEFAULT_.namn_aktor, domain=None, range=Optional[Union[str, list[str]]])

slots.startdato = Slot(uri=DCAT.startDate, name="startdato", curie=DCAT.curie('startDate'),
                   model_uri=DEFAULT_.startdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.sluttdato = Slot(uri=DCAT.endDate, name="sluttdato", curie=DCAT.curie('endDate'),
                   model_uri=DEFAULT_.sluttdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.utgiver = Slot(uri=DCT.publisher, name="utgiver", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.utgiver, domain=None, range=Optional[Union[str, AktorId]])

slots.skapar = Slot(uri=DCT.creator, name="skapar", curie=DCT.curie('creator'),
                   model_uri=DEFAULT_.skapar, domain=None, range=Optional[Union[str, AktorId]])

slots.kontaktpunkt = Slot(uri=DCAT.contactPoint, name="kontaktpunkt", curie=DCAT.curie('contactPoint'),
                   model_uri=DEFAULT_.kontaktpunkt, domain=None, range=Optional[Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]]])

slots.lisens = Slot(uri=DCT.license, name="lisens", curie=DCT.curie('license'),
                   model_uri=DEFAULT_.lisens, domain=None, range=Optional[Union[str, LisensdokumentId]])

slots.tema = Slot(uri=DCAT.theme, name="tema", curie=DCAT.curie('theme'),
                   model_uri=DEFAULT_.tema, domain=None, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.temaer = Slot(uri=DCAT.themeTaxonomy, name="temaer", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=DEFAULT_.temaer, domain=None, range=Optional[Union[Union[str, BegrepssamlingId], list[Union[str, BegrepssamlingId]]]])

slots.begrep = Slot(uri=DCT.subject, name="begrep", curie=DCT.curie('subject'),
                   model_uri=DEFAULT_.begrep, domain=None, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.har_del = Slot(uri=DCT.hasPart, name="har_del", curie=DCT.curie('hasPart'),
                   model_uri=DEFAULT_.har_del, domain=None, range=Optional[Union[Union[str, KatalogisertRessursId], list[Union[str, KatalogisertRessursId]]]])

slots.har_del_modell = Slot(uri=DCT.hasPart, name="har_del_modell", curie=DCT.curie('hasPart'),
                   model_uri=DEFAULT_.har_del_modell, domain=None, range=Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]])

slots.modell = Slot(uri=MODELLDCATNO.model, name="modell", curie=MODELLDCATNO.curie('model'),
                   model_uri=DEFAULT_.modell, domain=None, range=Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]])

slots.er_del_av_katalog = Slot(uri=DCT.isPartOf, name="er_del_av_katalog", curie=DCT.curie('isPartOf'),
                   model_uri=DEFAULT_.er_del_av_katalog, domain=None, range=Optional[Union[str, ModellkatalogId]])

slots.er_del_av_modell = Slot(uri=DCT.isPartOf, name="er_del_av_modell", curie=DCT.curie('isPartOf'),
                   model_uri=DEFAULT_.er_del_av_modell, domain=None, range=Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]])

slots.er_profil_av = Slot(uri=PROF.isProfileOf, name="er_profil_av", curie=PROF.curie('isProfileOf'),
                   model_uri=DEFAULT_.er_profil_av, domain=None, range=Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]])

slots.er_erstatta_av = Slot(uri=DCT.isReplacedBy, name="er_erstatta_av", curie=DCT.curie('isReplacedBy'),
                   model_uri=DEFAULT_.er_erstatta_av, domain=None, range=Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]])

slots.erstatter = Slot(uri=DCT.replaces, name="erstatter", curie=DCT.curie('replaces'),
                   model_uri=DEFAULT_.erstatter, domain=None, range=Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]])

slots.har_format = Slot(uri=DCT.hasFormat, name="har_format", curie=DCT.curie('hasFormat'),
                   model_uri=DEFAULT_.har_format, domain=None, range=Optional[Union[Union[str, DokumentId], list[Union[str, DokumentId]]]])

slots.tidsperiode = Slot(uri=DCT.temporal, name="tidsperiode", curie=DCT.curie('temporal'),
                   model_uri=DEFAULT_.tidsperiode, domain=None, range=Optional[Union[Union[str, TidsperiodeId], list[Union[str, TidsperiodeId]]]])

slots.er_i_samsvar_med = Slot(uri=DCT.conformsTo, name="er_i_samsvar_med", curie=DCT.curie('conformsTo'),
                   model_uri=DEFAULT_.er_i_samsvar_med, domain=None, range=Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]])

slots.informasjonsmodellidentifikator = Slot(uri=MODELLDCATNO.informationModelIdentifier, name="informasjonsmodellidentifikator", curie=MODELLDCATNO.curie('informationModelIdentifier'),
                   model_uri=DEFAULT_.informasjonsmodellidentifikator, domain=None, range=Optional[str])

slots.inneholder_modellelement = Slot(uri=MODELLDCATNO.containsModelElement, name="inneholder_modellelement", curie=MODELLDCATNO.curie('containsModelElement'),
                   model_uri=DEFAULT_.inneholder_modellelement, domain=None, range=Optional[Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]]])

slots.har_eigenskap = Slot(uri=MODELLDCATNO.hasProperty, name="har_eigenskap", curie=MODELLDCATNO.curie('hasProperty'),
                   model_uri=DEFAULT_.har_eigenskap, domain=None, range=Optional[Union[Union[str, EigenskapId], list[Union[str, EigenskapId]]]])

slots.tilhorer_modul = Slot(uri=MODELLDCATNO.belongsToModule, name="tilhorer_modul", curie=MODELLDCATNO.curie('belongsToModule'),
                   model_uri=DEFAULT_.tilhorer_modul, domain=None, range=Optional[Union[Union[str, ModulId], list[Union[str, ModulId]]]])

slots.navigerbar = Slot(uri=MODELLDCATNO.navigable, name="navigerbar", curie=MODELLDCATNO.curie('navigable'),
                   model_uri=DEFAULT_.navigerbar, domain=None, range=Optional[Union[bool, Bool]])

slots.min_multiplisitet = Slot(uri=MODELLDCATNO.minOccurs, name="min_multiplisitet", curie=MODELLDCATNO.curie('minOccurs'),
                   model_uri=DEFAULT_.min_multiplisitet, domain=None, range=Optional[int])

slots.maks_multiplisitet = Slot(uri=MODELLDCATNO.maxOccurs, name="maks_multiplisitet", curie=MODELLDCATNO.curie('maxOccurs'),
                   model_uri=DEFAULT_.maks_multiplisitet, domain=None, range=Optional[str])

slots.relasjonsegenskapetikett = Slot(uri=MODELLDCATNO.relationPropertyLabel, name="relasjonsegenskapetikett", curie=MODELLDCATNO.curie('relationPropertyLabel'),
                   model_uri=DEFAULT_.relasjonsegenskapetikett, domain=None, range=Optional[Union[str, list[str]]])

slots.sekvensnummer = Slot(uri=MODELLDCATNO.sequenceNumber, name="sekvensnummer", curie=MODELLDCATNO.curie('sequenceNumber'),
                   model_uri=DEFAULT_.sekvensnummer, domain=None, range=Optional[int])

slots.danner_symmetri_med = Slot(uri=MODELLDCATNO.formsSymmetryWith, name="danner_symmetri_med", curie=MODELLDCATNO.curie('formsSymmetryWith'),
                   model_uri=DEFAULT_.danner_symmetri_med, domain=None, range=Optional[Union[str, EigenskapId]])

slots.har_type = Slot(uri=MODELLDCATNO.hasType, name="har_type", curie=MODELLDCATNO.curie('hasType'),
                   model_uri=DEFAULT_.har_type, domain=None, range=Optional[Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]]])

slots.har_datatype = Slot(uri=MODELLDCATNO.hasDataType, name="har_datatype", curie=MODELLDCATNO.curie('hasDataType'),
                   model_uri=DEFAULT_.har_datatype, domain=None, range=Optional[Union[Union[str, DatatypeId], list[Union[str, DatatypeId]]]])

slots.har_enkel_type = Slot(uri=MODELLDCATNO.hasSimpleType, name="har_enkel_type", curie=MODELLDCATNO.curie('hasSimpleType'),
                   model_uri=DEFAULT_.har_enkel_type, domain=None, range=Optional[Union[Union[str, EnkelTypeId], list[Union[str, EnkelTypeId]]]])

slots.har_verdi_fra = Slot(uri=MODELLDCATNO.hasValueFrom, name="har_verdi_fra", curie=MODELLDCATNO.curie('hasValueFrom'),
                   model_uri=DEFAULT_.har_verdi_fra, domain=None, range=Optional[Union[Union[str, KodelisteId], list[Union[str, KodelisteId]]]])

slots.inneholder_objekttype = Slot(uri=MODELLDCATNO.containsObjectType, name="inneholder_objekttype", curie=MODELLDCATNO.curie('containsObjectType'),
                   model_uri=DEFAULT_.inneholder_objekttype, domain=None, range=Optional[Union[Union[str, ObjekttypeId], list[Union[str, ObjekttypeId]]]])

slots.refererer_til = Slot(uri=MODELLDCATNO.refersTo, name="refererer_til", curie=MODELLDCATNO.curie('refersTo'),
                   model_uri=DEFAULT_.refererer_til, domain=None, range=Optional[Union[str, ModellelementId]])

slots.har_objekttype = Slot(uri=MODELLDCATNO.hasObjectType, name="har_objekttype", curie=MODELLDCATNO.curie('hasObjectType'),
                   model_uri=DEFAULT_.har_objekttype, domain=None, range=Optional[Union[str, ObjekttypeId]])

slots.har_generelt_begrep = Slot(uri=MODELLDCATNO.hasGeneralConcept, name="har_generelt_begrep", curie=MODELLDCATNO.curie('hasGeneralConcept'),
                   model_uri=DEFAULT_.har_generelt_begrep, domain=None, range=Optional[Union[str, ModellelementId]])

slots.inneholder = Slot(uri=MODELLDCATNO.contains, name="inneholder", curie=MODELLDCATNO.curie('contains'),
                   model_uri=DEFAULT_.inneholder, domain=None, range=Optional[Union[str, ModellelementId]])

slots.har_leverandor = Slot(uri=MODELLDCATNO.hasSupplier, name="har_leverandor", curie=MODELLDCATNO.curie('hasSupplier'),
                   model_uri=DEFAULT_.har_leverandor, domain=None, range=Optional[Union[str, ModellelementId]])

slots.er_abstraksjon_av = Slot(uri=MODELLDCATNO.isAbstractionOf, name="er_abstraksjon_av", curie=MODELLDCATNO.curie('isAbstractionOf'),
                   model_uri=DEFAULT_.er_abstraksjon_av, domain=None, range=Optional[Union[str, ModellelementId]])

slots.avhengig_av = Slot(uri=MODELLDCATNO.dependentOn, name="avhengig_av", curie=MODELLDCATNO.curie('dependentOn'),
                   model_uri=DEFAULT_.avhengig_av, domain=None, range=Optional[Union[str, ModellelementId]])

slots.har_noe = Slot(uri=MODELLDCATNO.hasSome, name="har_noe", curie=MODELLDCATNO.curie('hasSome'),
                   model_uri=DEFAULT_.har_noe, domain=None, range=Optional[Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]]])

slots.typedefinisjon_referanse = Slot(uri=MODELLDCATNO.typeDefinitionReference, name="typedefinisjon_referanse", curie=MODELLDCATNO.curie('typeDefinitionReference'),
                   model_uri=DEFAULT_.typedefinisjon_referanse, domain=None, range=Optional[Union[str, URI]])

slots.fraksjonssifre = Slot(uri=XSD.fractionDigits, name="fraksjonssifre", curie=XSD.curie('fractionDigits'),
                   model_uri=DEFAULT_.fraksjonssifre, domain=None, range=Optional[int])

slots.lengde = Slot(uri=XSD.length, name="lengde", curie=XSD.curie('length'),
                   model_uri=DEFAULT_.lengde, domain=None, range=Optional[int])

slots.maks_eksklusiv = Slot(uri=XSD.maxExclusive, name="maks_eksklusiv", curie=XSD.curie('maxExclusive'),
                   model_uri=DEFAULT_.maks_eksklusiv, domain=None, range=Optional[str])

slots.maks_inklusiv = Slot(uri=XSD.maxInclusive, name="maks_inklusiv", curie=XSD.curie('maxInclusive'),
                   model_uri=DEFAULT_.maks_inklusiv, domain=None, range=Optional[str])

slots.maks_lengde = Slot(uri=XSD.maxLength, name="maks_lengde", curie=XSD.curie('maxLength'),
                   model_uri=DEFAULT_.maks_lengde, domain=None, range=Optional[int])

slots.min_eksklusiv = Slot(uri=XSD.minExclusive, name="min_eksklusiv", curie=XSD.curie('minExclusive'),
                   model_uri=DEFAULT_.min_eksklusiv, domain=None, range=Optional[str])

slots.min_inklusiv = Slot(uri=XSD.minInclusive, name="min_inklusiv", curie=XSD.curie('minInclusive'),
                   model_uri=DEFAULT_.min_inklusiv, domain=None, range=Optional[str])

slots.min_lengde = Slot(uri=XSD.minLength, name="min_lengde", curie=XSD.curie('minLength'),
                   model_uri=DEFAULT_.min_lengde, domain=None, range=Optional[int])

slots.monster = Slot(uri=XSD.pattern, name="monster", curie=XSD.curie('pattern'),
                   model_uri=DEFAULT_.monster, domain=None, range=Optional[str])

slots.totalt_sifre = Slot(uri=XSD.totalDigits, name="totalt_sifre", curie=XSD.curie('totalDigits'),
                   model_uri=DEFAULT_.totalt_sifre, domain=None, range=Optional[int])

slots.i_skjema = Slot(uri=SKOS.inScheme, name="i_skjema", curie=SKOS.curie('inScheme'),
                   model_uri=DEFAULT_.i_skjema, domain=None, range=Optional[Union[Union[str, KodelisteId], list[Union[str, KodelisteId]]]])

slots.notasjon = Slot(uri=SKOS.notation, name="notasjon", curie=SKOS.curie('notation'),
                   model_uri=DEFAULT_.notasjon, domain=None, range=Optional[str])

slots.topp_begrep_av = Slot(uri=SKOS.topConceptOf, name="topp_begrep_av", curie=SKOS.curie('topConceptOf'),
                   model_uri=DEFAULT_.topp_begrep_av, domain=None, range=Optional[Union[Union[str, KodelisteId], list[Union[str, KodelisteId]]]])

slots.definisjon = Slot(uri=SKOS.definition, name="definisjon", curie=SKOS.curie('definition'),
                   model_uri=DEFAULT_.definisjon, domain=None, range=Optional[Union[str, list[str]]])

slots.eksempel_kode = Slot(uri=SKOS.example, name="eksempel_kode", curie=SKOS.curie('example'),
                   model_uri=DEFAULT_.eksempel_kode, domain=None, range=Optional[Union[str, list[str]]])

slots.eksklusjonsnotat = Slot(uri=XKOS.exclusionNote, name="eksklusjonsnotat", curie=XKOS.curie('exclusionNote'),
                   model_uri=DEFAULT_.eksklusjonsnotat, domain=None, range=Optional[Union[str, list[str]]])

slots.forrige = Slot(uri=XKOS.previous, name="forrige", curie=XKOS.curie('previous'),
                   model_uri=DEFAULT_.forrige, domain=None, range=Optional[Union[str, KodeelementId]])

slots.skjult_term = Slot(uri=SKOS.hiddenLabel, name="skjult_term", curie=SKOS.curie('hiddenLabel'),
                   model_uri=DEFAULT_.skjult_term, domain=None, range=Optional[Union[str, list[str]]])

slots.inklusjonsnotat = Slot(uri=XKOS.inclusionNote, name="inklusjonsnotat", curie=XKOS.curie('inclusionNote'),
                   model_uri=DEFAULT_.inklusjonsnotat, domain=None, range=Optional[Union[str, list[str]]])

slots.notat = Slot(uri=SKOS.note, name="notat", curie=SKOS.curie('note'),
                   model_uri=DEFAULT_.notat, domain=None, range=Optional[Union[str, list[str]]])

slots.neste = Slot(uri=XKOS.next, name="neste", curie=XKOS.curie('next'),
                   model_uri=DEFAULT_.neste, domain=None, range=Optional[Union[str, KodeelementId]])

slots.omfangsnotat = Slot(uri=SKOS.scopeNote, name="omfangsnotat", curie=SKOS.curie('scopeNote'),
                   model_uri=DEFAULT_.omfangsnotat, domain=None, range=Optional[Union[str, list[str]]])

slots.alternativ_term = Slot(uri=SKOS.altLabel, name="alternativ_term", curie=SKOS.curie('altLabel'),
                   model_uri=DEFAULT_.alternativ_term, domain=None, range=Optional[Union[str, list[str]]])

slots.annoterer = Slot(uri=MODELLDCATNO.annotates, name="annoterer", curie=MODELLDCATNO.curie('annotates'),
                   model_uri=DEFAULT_.annoterer, domain=None, range=Optional[Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]]])

slots.eigenskapsmerknad = Slot(uri=MODELLDCATNO.propertyNote, name="eigenskapsmerknad", curie=MODELLDCATNO.curie('propertyNote'),
                   model_uri=DEFAULT_.eigenskapsmerknad, domain=None, range=Optional[Union[str, list[str]]])

slots.betinger = Slot(uri=MODELLDCATNO.constrains, name="betinger", curie=MODELLDCATNO.curie('constrains'),
                   model_uri=DEFAULT_.betinger, domain=None, range=Optional[Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]]])

slots.betingelsesuttrykk = Slot(uri=MODELLDCATNO.constraintExpression, name="betingelsesuttrykk", curie=MODELLDCATNO.curie('constraintExpression'),
                   model_uri=DEFAULT_.betingelsesuttrykk, domain=None, range=Optional[Union[str, list[str]]])

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

slots.Aktor_namn_aktor = Slot(uri=FOAF.name, name="Aktor_namn_aktor", curie=FOAF.curie('name'),
                   model_uri=DEFAULT_.Aktor_namn_aktor, domain=Aktor, range=Union[str, list[str]])

slots.Standard_tittel = Slot(uri=DCT.title, name="Standard_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Standard_tittel, domain=Standard, range=Union[str, list[str]])

slots.Modellkatalog_tittel = Slot(uri=DCT.title, name="Modellkatalog_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Modellkatalog_tittel, domain=Modellkatalog, range=Union[str, list[str]])

slots.Modellkatalog_beskrivelse = Slot(uri=DCT.description, name="Modellkatalog_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.Modellkatalog_beskrivelse, domain=Modellkatalog, range=Union[str, list[str]])

slots.Modellkatalog_har_del = Slot(uri=DCT.hasPart, name="Modellkatalog_har_del", curie=DCT.curie('hasPart'),
                   model_uri=DEFAULT_.Modellkatalog_har_del, domain=Modellkatalog, range=Union[Union[str, KatalogisertRessursId], list[Union[str, KatalogisertRessursId]]])

slots.Modellkatalog_identifikator_literal = Slot(uri=DCT.identifier, name="Modellkatalog_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Modellkatalog_identifikator_literal, domain=Modellkatalog, range=str)

slots.Modellkatalog_kontaktpunkt = Slot(uri=DCAT.contactPoint, name="Modellkatalog_kontaktpunkt", curie=DCAT.curie('contactPoint'),
                   model_uri=DEFAULT_.Modellkatalog_kontaktpunkt, domain=Modellkatalog, range=Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]])

slots.Modellkatalog_utgiver = Slot(uri=DCT.publisher, name="Modellkatalog_utgiver", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.Modellkatalog_utgiver, domain=Modellkatalog, range=Union[str, AktorId])

slots.Modellkatalog_endringsdato = Slot(uri=DCT.modified, name="Modellkatalog_endringsdato", curie=DCT.curie('modified'),
                   model_uri=DEFAULT_.Modellkatalog_endringsdato, domain=Modellkatalog, range=Optional[Union[str, XSDDate]])

slots.Modellkatalog_heimeside = Slot(uri=FOAF.homepage, name="Modellkatalog_heimeside", curie=FOAF.curie('homepage'),
                   model_uri=DEFAULT_.Modellkatalog_heimeside, domain=Modellkatalog, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Modellkatalog_lisens = Slot(uri=DCT.license, name="Modellkatalog_lisens", curie=DCT.curie('license'),
                   model_uri=DEFAULT_.Modellkatalog_lisens, domain=Modellkatalog, range=Optional[Union[str, LisensdokumentId]])

slots.Modellkatalog_modell = Slot(uri=MODELLDCATNO.model, name="Modellkatalog_modell", curie=MODELLDCATNO.curie('model'),
                   model_uri=DEFAULT_.Modellkatalog_modell, domain=Modellkatalog, range=Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]])

slots.Modellkatalog_spraak = Slot(uri=DCT.language, name="Modellkatalog_spraak", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.Modellkatalog_spraak, domain=Modellkatalog, range=Optional[Union[str, list[str]]])

slots.Modellkatalog_tema = Slot(uri=DCAT.theme, name="Modellkatalog_tema", curie=DCAT.curie('theme'),
                   model_uri=DEFAULT_.Modellkatalog_tema, domain=Modellkatalog, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Modellkatalog_utgivelsesdato = Slot(uri=DCT.issued, name="Modellkatalog_utgivelsesdato", curie=DCT.curie('issued'),
                   model_uri=DEFAULT_.Modellkatalog_utgivelsesdato, domain=Modellkatalog, range=Optional[Union[str, XSDDate]])

slots.Modellkatalog_temaer = Slot(uri=DCAT.themeTaxonomy, name="Modellkatalog_temaer", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=DEFAULT_.Modellkatalog_temaer, domain=Modellkatalog, range=Optional[Union[Union[str, BegrepssamlingId], list[Union[str, BegrepssamlingId]]]])

slots.Modellkatalog_er_del_av_katalog = Slot(uri=DCT.isPartOf, name="Modellkatalog_er_del_av_katalog", curie=DCT.curie('isPartOf'),
                   model_uri=DEFAULT_.Modellkatalog_er_del_av_katalog, domain=Modellkatalog, range=Optional[Union[str, ModellkatalogId]])

slots.Informasjonsmodell_tittel = Slot(uri=DCT.title, name="Informasjonsmodell_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Informasjonsmodell_tittel, domain=Informasjonsmodell, range=Union[str, list[str]])

slots.Informasjonsmodell_utgiver = Slot(uri=DCT.publisher, name="Informasjonsmodell_utgiver", curie=DCT.curie('publisher'),
                   model_uri=DEFAULT_.Informasjonsmodell_utgiver, domain=Informasjonsmodell, range=Union[str, AktorId])

slots.Informasjonsmodell_begrep = Slot(uri=DCT.subject, name="Informasjonsmodell_begrep", curie=DCT.curie('subject'),
                   model_uri=DEFAULT_.Informasjonsmodell_begrep, domain=Informasjonsmodell, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Informasjonsmodell_beskrivelse = Slot(uri=DCT.description, name="Informasjonsmodell_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.Informasjonsmodell_beskrivelse, domain=Informasjonsmodell, range=Optional[Union[str, list[str]]])

slots.Informasjonsmodell_identifikator_literal = Slot(uri=DCT.identifier, name="Informasjonsmodell_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Informasjonsmodell_identifikator_literal, domain=Informasjonsmodell, range=Optional[str])

slots.Informasjonsmodell_informasjonsmodellidentifikator = Slot(uri=MODELLDCATNO.informationModelIdentifier, name="Informasjonsmodell_informasjonsmodellidentifikator", curie=MODELLDCATNO.curie('informationModelIdentifier'),
                   model_uri=DEFAULT_.Informasjonsmodell_informasjonsmodellidentifikator, domain=Informasjonsmodell, range=Optional[str])

slots.Informasjonsmodell_inneholder_modellelement = Slot(uri=MODELLDCATNO.containsModelElement, name="Informasjonsmodell_inneholder_modellelement", curie=MODELLDCATNO.curie('containsModelElement'),
                   model_uri=DEFAULT_.Informasjonsmodell_inneholder_modellelement, domain=Informasjonsmodell, range=Optional[Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]]])

slots.Informasjonsmodell_kontaktpunkt = Slot(uri=DCAT.contactPoint, name="Informasjonsmodell_kontaktpunkt", curie=DCAT.curie('contactPoint'),
                   model_uri=DEFAULT_.Informasjonsmodell_kontaktpunkt, domain=Informasjonsmodell, range=Optional[Union[Union[str, KontaktopplysningId], list[Union[str, KontaktopplysningId]]]])

slots.Informasjonsmodell_lisens = Slot(uri=DCT.license, name="Informasjonsmodell_lisens", curie=DCT.curie('license'),
                   model_uri=DEFAULT_.Informasjonsmodell_lisens, domain=Informasjonsmodell, range=Optional[Union[str, LisensdokumentId]])

slots.Informasjonsmodell_tema = Slot(uri=DCAT.theme, name="Informasjonsmodell_tema", curie=DCAT.curie('theme'),
                   model_uri=DEFAULT_.Informasjonsmodell_tema, domain=Informasjonsmodell, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Informasjonsmodell_dekningsomraade = Slot(uri=DCT.spatial, name="Informasjonsmodell_dekningsomraade", curie=DCT.curie('spatial'),
                   model_uri=DEFAULT_.Informasjonsmodell_dekningsomraade, domain=Informasjonsmodell, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Informasjonsmodell_endringsdato = Slot(uri=DCT.modified, name="Informasjonsmodell_endringsdato", curie=DCT.curie('modified'),
                   model_uri=DEFAULT_.Informasjonsmodell_endringsdato, domain=Informasjonsmodell, range=Optional[Union[str, XSDDate]])

slots.Informasjonsmodell_er_del_av_modell = Slot(uri=DCT.isPartOf, name="Informasjonsmodell_er_del_av_modell", curie=DCT.curie('isPartOf'),
                   model_uri=DEFAULT_.Informasjonsmodell_er_del_av_modell, domain=Informasjonsmodell, range=Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]])

slots.Informasjonsmodell_er_profil_av = Slot(uri=PROF.isProfileOf, name="Informasjonsmodell_er_profil_av", curie=PROF.curie('isProfileOf'),
                   model_uri=DEFAULT_.Informasjonsmodell_er_profil_av, domain=Informasjonsmodell, range=Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]])

slots.Informasjonsmodell_er_erstatta_av = Slot(uri=DCT.isReplacedBy, name="Informasjonsmodell_er_erstatta_av", curie=DCT.curie('isReplacedBy'),
                   model_uri=DEFAULT_.Informasjonsmodell_er_erstatta_av, domain=Informasjonsmodell, range=Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]])

slots.Informasjonsmodell_erstatter = Slot(uri=DCT.replaces, name="Informasjonsmodell_erstatter", curie=DCT.curie('replaces'),
                   model_uri=DEFAULT_.Informasjonsmodell_erstatter, domain=Informasjonsmodell, range=Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]])

slots.Informasjonsmodell_har_del_modell = Slot(uri=DCT.hasPart, name="Informasjonsmodell_har_del_modell", curie=DCT.curie('hasPart'),
                   model_uri=DEFAULT_.Informasjonsmodell_har_del_modell, domain=Informasjonsmodell, range=Optional[Union[Union[str, InformasjonsmodellId], list[Union[str, InformasjonsmodellId]]]])

slots.Informasjonsmodell_har_format = Slot(uri=DCT.hasFormat, name="Informasjonsmodell_har_format", curie=DCT.curie('hasFormat'),
                   model_uri=DEFAULT_.Informasjonsmodell_har_format, domain=Informasjonsmodell, range=Optional[Union[Union[str, DokumentId], list[Union[str, DokumentId]]]])

slots.Informasjonsmodell_tidsperiode = Slot(uri=DCT.temporal, name="Informasjonsmodell_tidsperiode", curie=DCT.curie('temporal'),
                   model_uri=DEFAULT_.Informasjonsmodell_tidsperiode, domain=Informasjonsmodell, range=Optional[Union[Union[str, TidsperiodeId], list[Union[str, TidsperiodeId]]]])

slots.Informasjonsmodell_heimeside = Slot(uri=FOAF.homepage, name="Informasjonsmodell_heimeside", curie=FOAF.curie('homepage'),
                   model_uri=DEFAULT_.Informasjonsmodell_heimeside, domain=Informasjonsmodell, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Informasjonsmodell_er_i_samsvar_med = Slot(uri=DCT.conformsTo, name="Informasjonsmodell_er_i_samsvar_med", curie=DCT.curie('conformsTo'),
                   model_uri=DEFAULT_.Informasjonsmodell_er_i_samsvar_med, domain=Informasjonsmodell, range=Optional[Union[Union[str, StandardId], list[Union[str, StandardId]]]])

slots.Informasjonsmodell_status = Slot(uri=ADMS.status, name="Informasjonsmodell_status", curie=ADMS.curie('status'),
                   model_uri=DEFAULT_.Informasjonsmodell_status, domain=Informasjonsmodell, range=Optional[Union[str, KonseptId]])

slots.Informasjonsmodell_nokkelord = Slot(uri=DCAT.keyword, name="Informasjonsmodell_nokkelord", curie=DCAT.curie('keyword'),
                   model_uri=DEFAULT_.Informasjonsmodell_nokkelord, domain=Informasjonsmodell, range=Optional[Union[str, list[str]]])

slots.Informasjonsmodell_skapar = Slot(uri=DCT.creator, name="Informasjonsmodell_skapar", curie=DCT.curie('creator'),
                   model_uri=DEFAULT_.Informasjonsmodell_skapar, domain=Informasjonsmodell, range=Optional[Union[str, AktorId]])

slots.Informasjonsmodell_spraak = Slot(uri=DCT.language, name="Informasjonsmodell_spraak", curie=DCT.curie('language'),
                   model_uri=DEFAULT_.Informasjonsmodell_spraak, domain=Informasjonsmodell, range=Optional[Union[str, list[str]]])

slots.Informasjonsmodell_type_concept = Slot(uri=DCT.type, name="Informasjonsmodell_type_concept", curie=DCT.curie('type'),
                   model_uri=DEFAULT_.Informasjonsmodell_type_concept, domain=Informasjonsmodell, range=Optional[Union[str, KonseptId]])

slots.Informasjonsmodell_utgivelsesdato = Slot(uri=DCT.issued, name="Informasjonsmodell_utgivelsesdato", curie=DCT.curie('issued'),
                   model_uri=DEFAULT_.Informasjonsmodell_utgivelsesdato, domain=Informasjonsmodell, range=Optional[Union[str, XSDDate]])

slots.Informasjonsmodell_har_versjonsnummer = Slot(uri=OWL.versionInfo, name="Informasjonsmodell_har_versjonsnummer", curie=OWL.curie('versionInfo'),
                   model_uri=DEFAULT_.Informasjonsmodell_har_versjonsnummer, domain=Informasjonsmodell, range=Optional[str])

slots.Informasjonsmodell_versjonsmerknad = Slot(uri=ADMS.versionNotes, name="Informasjonsmodell_versjonsmerknad", curie=ADMS.curie('versionNotes'),
                   model_uri=DEFAULT_.Informasjonsmodell_versjonsmerknad, domain=Informasjonsmodell, range=Optional[Union[str, list[str]]])

slots.Modellelement_tittel = Slot(uri=DCT.title, name="Modellelement_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Modellelement_tittel, domain=Modellelement, range=Union[str, list[str]])

slots.Modellelement_begrep = Slot(uri=DCT.subject, name="Modellelement_begrep", curie=DCT.curie('subject'),
                   model_uri=DEFAULT_.Modellelement_begrep, domain=Modellelement, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Modellelement_identifikator_literal = Slot(uri=DCT.identifier, name="Modellelement_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Modellelement_identifikator_literal, domain=Modellelement, range=Optional[str])

slots.Modellelement_har_eigenskap = Slot(uri=MODELLDCATNO.hasProperty, name="Modellelement_har_eigenskap", curie=MODELLDCATNO.curie('hasProperty'),
                   model_uri=DEFAULT_.Modellelement_har_eigenskap, domain=Modellelement, range=Optional[Union[Union[str, EigenskapId], list[Union[str, EigenskapId]]]])

slots.Modellelement_beskrivelse = Slot(uri=DCT.description, name="Modellelement_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.Modellelement_beskrivelse, domain=Modellelement, range=Optional[Union[str, list[str]]])

slots.Modellelement_tilhorer_modul = Slot(uri=MODELLDCATNO.belongsToModule, name="Modellelement_tilhorer_modul", curie=MODELLDCATNO.curie('belongsToModule'),
                   model_uri=DEFAULT_.Modellelement_tilhorer_modul, domain=Modellelement, range=Optional[Union[Union[str, ModulId], list[Union[str, ModulId]]]])

slots.EnkelType_typedefinisjon_referanse = Slot(uri=MODELLDCATNO.typeDefinitionReference, name="EnkelType_typedefinisjon_referanse", curie=MODELLDCATNO.curie('typeDefinitionReference'),
                   model_uri=DEFAULT_.EnkelType_typedefinisjon_referanse, domain=EnkelType, range=Optional[Union[str, URI]])

slots.Eigenskap_begrep = Slot(uri=DCT.subject, name="Eigenskap_begrep", curie=DCT.curie('subject'),
                   model_uri=DEFAULT_.Eigenskap_begrep, domain=Eigenskap, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Eigenskap_identifikator_literal = Slot(uri=DCT.identifier, name="Eigenskap_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Eigenskap_identifikator_literal, domain=Eigenskap, range=Optional[str])

slots.Eigenskap_navigerbar = Slot(uri=MODELLDCATNO.navigable, name="Eigenskap_navigerbar", curie=MODELLDCATNO.curie('navigable'),
                   model_uri=DEFAULT_.Eigenskap_navigerbar, domain=Eigenskap, range=Optional[Union[bool, Bool]])

slots.Eigenskap_min_multiplisitet = Slot(uri=MODELLDCATNO.minOccurs, name="Eigenskap_min_multiplisitet", curie=MODELLDCATNO.curie('minOccurs'),
                   model_uri=DEFAULT_.Eigenskap_min_multiplisitet, domain=Eigenskap, range=Optional[int])

slots.Eigenskap_tittel = Slot(uri=DCT.title, name="Eigenskap_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Eigenskap_tittel, domain=Eigenskap, range=Optional[Union[str, list[str]]])

slots.Eigenskap_maks_multiplisitet = Slot(uri=MODELLDCATNO.maxOccurs, name="Eigenskap_maks_multiplisitet", curie=MODELLDCATNO.curie('maxOccurs'),
                   model_uri=DEFAULT_.Eigenskap_maks_multiplisitet, domain=Eigenskap, range=Optional[str])

slots.Eigenskap_beskrivelse = Slot(uri=DCT.description, name="Eigenskap_beskrivelse", curie=DCT.curie('description'),
                   model_uri=DEFAULT_.Eigenskap_beskrivelse, domain=Eigenskap, range=Optional[Union[str, list[str]]])

slots.Eigenskap_har_type = Slot(uri=MODELLDCATNO.hasType, name="Eigenskap_har_type", curie=MODELLDCATNO.curie('hasType'),
                   model_uri=DEFAULT_.Eigenskap_har_type, domain=Eigenskap, range=Optional[Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]]])

slots.Eigenskap_relasjonsegenskapetikett = Slot(uri=MODELLDCATNO.relationPropertyLabel, name="Eigenskap_relasjonsegenskapetikett", curie=MODELLDCATNO.curie('relationPropertyLabel'),
                   model_uri=DEFAULT_.Eigenskap_relasjonsegenskapetikett, domain=Eigenskap, range=Optional[Union[str, list[str]]])

slots.Eigenskap_sekvensnummer = Slot(uri=MODELLDCATNO.sequenceNumber, name="Eigenskap_sekvensnummer", curie=MODELLDCATNO.curie('sequenceNumber'),
                   model_uri=DEFAULT_.Eigenskap_sekvensnummer, domain=Eigenskap, range=Optional[int])

slots.Eigenskap_tilhorer_modul = Slot(uri=MODELLDCATNO.belongsToModule, name="Eigenskap_tilhorer_modul", curie=MODELLDCATNO.curie('belongsToModule'),
                   model_uri=DEFAULT_.Eigenskap_tilhorer_modul, domain=Eigenskap, range=Optional[Union[Union[str, ModulId], list[Union[str, ModulId]]]])

slots.Eigenskap_danner_symmetri_med = Slot(uri=MODELLDCATNO.formsSymmetryWith, name="Eigenskap_danner_symmetri_med", curie=MODELLDCATNO.curie('formsSymmetryWith'),
                   model_uri=DEFAULT_.Eigenskap_danner_symmetri_med, domain=Eigenskap, range=Optional[Union[str, EigenskapId]])

slots.Attributt_har_datatype = Slot(uri=MODELLDCATNO.hasDataType, name="Attributt_har_datatype", curie=MODELLDCATNO.curie('hasDataType'),
                   model_uri=DEFAULT_.Attributt_har_datatype, domain=Attributt, range=Optional[Union[Union[str, DatatypeId], list[Union[str, DatatypeId]]]])

slots.Attributt_har_enkel_type = Slot(uri=MODELLDCATNO.hasSimpleType, name="Attributt_har_enkel_type", curie=MODELLDCATNO.curie('hasSimpleType'),
                   model_uri=DEFAULT_.Attributt_har_enkel_type, domain=Attributt, range=Optional[Union[Union[str, EnkelTypeId], list[Union[str, EnkelTypeId]]]])

slots.Attributt_har_verdi_fra = Slot(uri=MODELLDCATNO.hasValueFrom, name="Attributt_har_verdi_fra", curie=MODELLDCATNO.curie('hasValueFrom'),
                   model_uri=DEFAULT_.Attributt_har_verdi_fra, domain=Attributt, range=Optional[Union[Union[str, KodelisteId], list[Union[str, KodelisteId]]]])

slots.Attributt_inneholder_objekttype = Slot(uri=MODELLDCATNO.containsObjectType, name="Attributt_inneholder_objekttype", curie=MODELLDCATNO.curie('containsObjectType'),
                   model_uri=DEFAULT_.Attributt_inneholder_objekttype, domain=Attributt, range=Optional[Union[Union[str, ObjekttypeId], list[Union[str, ObjekttypeId]]]])

slots.Assosiasjon_refererer_til = Slot(uri=MODELLDCATNO.refersTo, name="Assosiasjon_refererer_til", curie=MODELLDCATNO.curie('refersTo'),
                   model_uri=DEFAULT_.Assosiasjon_refererer_til, domain=Assosiasjon, range=Optional[Union[str, ModellelementId]])

slots.Rolle_har_objekttype = Slot(uri=MODELLDCATNO.hasObjectType, name="Rolle_har_objekttype", curie=MODELLDCATNO.curie('hasObjectType'),
                   model_uri=DEFAULT_.Rolle_har_objekttype, domain=Rolle, range=Optional[Union[str, ObjekttypeId]])

slots.Spesialisering_har_generelt_begrep = Slot(uri=MODELLDCATNO.hasGeneralConcept, name="Spesialisering_har_generelt_begrep", curie=MODELLDCATNO.curie('hasGeneralConcept'),
                   model_uri=DEFAULT_.Spesialisering_har_generelt_begrep, domain=Spesialisering, range=Optional[Union[str, ModellelementId]])

slots.Sammensetning_inneholder = Slot(uri=MODELLDCATNO.contains, name="Sammensetning_inneholder", curie=MODELLDCATNO.curie('contains'),
                   model_uri=DEFAULT_.Sammensetning_inneholder, domain=Sammensetning, range=Optional[Union[str, ModellelementId]])

slots.Realisering_har_leverandor = Slot(uri=MODELLDCATNO.hasSupplier, name="Realisering_har_leverandor", curie=MODELLDCATNO.curie('hasSupplier'),
                   model_uri=DEFAULT_.Realisering_har_leverandor, domain=Realisering, range=Optional[Union[str, ModellelementId]])

slots.Abstraksjon_er_abstraksjon_av = Slot(uri=MODELLDCATNO.isAbstractionOf, name="Abstraksjon_er_abstraksjon_av", curie=MODELLDCATNO.curie('isAbstractionOf'),
                   model_uri=DEFAULT_.Abstraksjon_er_abstraksjon_av, domain=Abstraksjon, range=Optional[Union[str, ModellelementId]])

slots.Avhengighet_avhengig_av = Slot(uri=MODELLDCATNO.dependentOn, name="Avhengighet_avhengig_av", curie=MODELLDCATNO.curie('dependentOn'),
                   model_uri=DEFAULT_.Avhengighet_avhengig_av, domain=Avhengighet, range=Optional[Union[str, ModellelementId]])

slots.Valg_har_noe = Slot(uri=MODELLDCATNO.hasSome, name="Valg_har_noe", curie=MODELLDCATNO.curie('hasSome'),
                   model_uri=DEFAULT_.Valg_har_noe, domain=Valg, range=Optional[Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]]])

slots.Merknad_annoterer = Slot(uri=MODELLDCATNO.annotates, name="Merknad_annoterer", curie=MODELLDCATNO.curie('annotates'),
                   model_uri=DEFAULT_.Merknad_annoterer, domain=Merknad, range=Optional[Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]]])

slots.Merknad_eigenskapsmerknad = Slot(uri=MODELLDCATNO.propertyNote, name="Merknad_eigenskapsmerknad", curie=MODELLDCATNO.curie('propertyNote'),
                   model_uri=DEFAULT_.Merknad_eigenskapsmerknad, domain=Merknad, range=Optional[Union[str, list[str]]])

slots.Merknad_identifikator_literal = Slot(uri=DCT.identifier, name="Merknad_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Merknad_identifikator_literal, domain=Merknad, range=Optional[str])

slots.Merknad_tittel = Slot(uri=DCT.title, name="Merknad_tittel", curie=DCT.curie('title'),
                   model_uri=DEFAULT_.Merknad_tittel, domain=Merknad, range=Optional[Union[str, list[str]]])

slots.Merknad_tilhorer_modul = Slot(uri=MODELLDCATNO.belongsToModule, name="Merknad_tilhorer_modul", curie=MODELLDCATNO.curie('belongsToModule'),
                   model_uri=DEFAULT_.Merknad_tilhorer_modul, domain=Merknad, range=Optional[Union[Union[str, ModulId], list[Union[str, ModulId]]]])

slots.Betingelsesregel_betinger = Slot(uri=MODELLDCATNO.constrains, name="Betingelsesregel_betinger", curie=MODELLDCATNO.curie('constrains'),
                   model_uri=DEFAULT_.Betingelsesregel_betinger, domain=Betingelsesregel, range=Union[Union[str, ModellelementId], list[Union[str, ModellelementId]]])

slots.Betingelsesregel_betingelsesuttrykk = Slot(uri=MODELLDCATNO.constraintExpression, name="Betingelsesregel_betingelsesuttrykk", curie=MODELLDCATNO.curie('constraintExpression'),
                   model_uri=DEFAULT_.Betingelsesregel_betingelsesuttrykk, domain=Betingelsesregel, range=Optional[Union[str, list[str]]])

slots.Kodeelement_i_skjema = Slot(uri=SKOS.inScheme, name="Kodeelement_i_skjema", curie=SKOS.curie('inScheme'),
                   model_uri=DEFAULT_.Kodeelement_i_skjema, domain=Kodeelement, range=Union[Union[str, KodelisteId], list[Union[str, KodelisteId]]])

slots.Kodeelement_notasjon = Slot(uri=SKOS.notation, name="Kodeelement_notasjon", curie=SKOS.curie('notation'),
                   model_uri=DEFAULT_.Kodeelement_notasjon, domain=Kodeelement, range=str)

slots.Kodeelement_anbefalt_term = Slot(uri=SKOS.prefLabel, name="Kodeelement_anbefalt_term", curie=SKOS.curie('prefLabel'),
                   model_uri=DEFAULT_.Kodeelement_anbefalt_term, domain=Kodeelement, range=Optional[Union[str, list[str]]])

slots.Kodeelement_begrep = Slot(uri=DCT.subject, name="Kodeelement_begrep", curie=DCT.curie('subject'),
                   model_uri=DEFAULT_.Kodeelement_begrep, domain=Kodeelement, range=Optional[Union[Union[str, KonseptId], list[Union[str, KonseptId]]]])

slots.Kodeelement_identifikator_literal = Slot(uri=DCT.identifier, name="Kodeelement_identifikator_literal", curie=DCT.curie('identifier'),
                   model_uri=DEFAULT_.Kodeelement_identifikator_literal, domain=Kodeelement, range=Optional[str])

slots.Kodeelement_topp_begrep_av = Slot(uri=SKOS.topConceptOf, name="Kodeelement_topp_begrep_av", curie=SKOS.curie('topConceptOf'),
                   model_uri=DEFAULT_.Kodeelement_topp_begrep_av, domain=Kodeelement, range=Optional[Union[Union[str, KodelisteId], list[Union[str, KodelisteId]]]])

