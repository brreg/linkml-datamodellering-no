# Auto generated from fair-metadata-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-27T14:51:27
# Schema: fair-metadata
#
# id: https://data.norge.no/fair/fair-metadata
# description: FAIR metadata-overbygning som utfyllar norske applikasjonsprofilar for å sikre maskin-aksjonerbar FAIR-konformitet i tråd med FAIR-prinsippa (Findable, Accessible, Interoperable, Reusable).
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

from linkml_runtime.linkml_model.types import Boolean, Date, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.11.0"
version = "1.0.0"

# Namespaces
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
FAIR = CurieNamespace('fair', 'https://data.norge.no/fair#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
DEFAULT_ = FAIR


# Types

# Class references
class FAIRMetadataId(URIorCURIE):
    pass


@dataclass(repr=False)
class FAIRMetadata(YAMLRoot):
    """
    Maskin-aksjonerbar metadata som beskriver ein digital ressurs i tråd med FAIR-prinsippa.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAIR["FAIRMetadata"]
    class_class_curie: ClassVar[str] = "fair:FAIRMetadata"
    class_name: ClassVar[str] = "FAIRMetadata"
    class_model_uri: ClassVar[URIRef] = FAIR.FAIRMetadata

    id: Union[str, FAIRMetadataId] = None
    ressursIdentifikator: Union[str, URIorCURIE] = None
    ressurstype: Union[str, URIorCURIE] = None
    beskrivelse: Optional[Union[str, URIorCURIE]] = None
    tilgangsmetadata: Optional[Union[dict, "Tilgangsmetadata"]] = None
    gjenbruksmetadata: Optional[Union[dict, "Gjenbruksmetadata"]] = None
    proveniensmetadata: Optional[Union[dict, "Proveniensmetadata"]] = None
    katalogregistrering: Optional[Union[dict, "Katalogregistrering"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FAIRMetadataId):
            self.id = FAIRMetadataId(self.id)

        if self._is_empty(self.ressursIdentifikator):
            self.MissingRequiredField("ressursIdentifikator")
        if not isinstance(self.ressursIdentifikator, URIorCURIE):
            self.ressursIdentifikator = URIorCURIE(self.ressursIdentifikator)

        if self._is_empty(self.ressurstype):
            self.MissingRequiredField("ressurstype")
        if not isinstance(self.ressurstype, URIorCURIE):
            self.ressurstype = URIorCURIE(self.ressurstype)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, URIorCURIE):
            self.beskrivelse = URIorCURIE(self.beskrivelse)

        if self.tilgangsmetadata is not None and not isinstance(self.tilgangsmetadata, Tilgangsmetadata):
            self.tilgangsmetadata = Tilgangsmetadata(**as_dict(self.tilgangsmetadata))

        if self.gjenbruksmetadata is not None and not isinstance(self.gjenbruksmetadata, Gjenbruksmetadata):
            self.gjenbruksmetadata = Gjenbruksmetadata(**as_dict(self.gjenbruksmetadata))

        if self.proveniensmetadata is not None and not isinstance(self.proveniensmetadata, Proveniensmetadata):
            self.proveniensmetadata = Proveniensmetadata(**as_dict(self.proveniensmetadata))

        if self.katalogregistrering is not None and not isinstance(self.katalogregistrering, Katalogregistrering):
            self.katalogregistrering = Katalogregistrering(**as_dict(self.katalogregistrering))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tilgangsmetadata(YAMLRoot):
    """
    Metadata for tilgang, autentisering og tilgjengelegheit (FAIR A1/A2).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAIR["Tilgangsmetadata"]
    class_class_curie: ClassVar[str] = "fair:Tilgangsmetadata"
    class_name: ClassVar[str] = "Tilgangsmetadata"
    class_model_uri: ClassVar[URIRef] = FAIR.Tilgangsmetadata

    tilgangsURL: Optional[Union[str, URIorCURIE]] = None
    tilgangsprotokoll: Optional[str] = None
    tilgangsrettar: Optional[Union[str, URIorCURIE]] = None
    autentiseringPaakrevd: Optional[Union[bool, Bool]] = None
    metadataPersistens: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.tilgangsURL is not None and not isinstance(self.tilgangsURL, URIorCURIE):
            self.tilgangsURL = URIorCURIE(self.tilgangsURL)

        if self.tilgangsprotokoll is not None and not isinstance(self.tilgangsprotokoll, str):
            self.tilgangsprotokoll = str(self.tilgangsprotokoll)

        if self.tilgangsrettar is not None and not isinstance(self.tilgangsrettar, URIorCURIE):
            self.tilgangsrettar = URIorCURIE(self.tilgangsrettar)

        if self.autentiseringPaakrevd is not None and not isinstance(self.autentiseringPaakrevd, Bool):
            self.autentiseringPaakrevd = Bool(self.autentiseringPaakrevd)

        if self.metadataPersistens is not None and not isinstance(self.metadataPersistens, Bool):
            self.metadataPersistens = Bool(self.metadataPersistens)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Gjenbruksmetadata(YAMLRoot):
    """
    Metadata som støttar gjenbruk av ressursen (FAIR R1.1, R1.3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAIR["Gjenbruksmetadata"]
    class_class_curie: ClassVar[str] = "fair:Gjenbruksmetadata"
    class_name: ClassVar[str] = "Gjenbruksmetadata"
    class_model_uri: ClassVar[URIRef] = FAIR.Gjenbruksmetadata

    lisens: Optional[Union[str, URIorCURIE]] = None
    bruksavgrensingar: Optional[str] = None
    standardoverensstemming: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    vokabular: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.lisens is not None and not isinstance(self.lisens, URIorCURIE):
            self.lisens = URIorCURIE(self.lisens)

        if self.bruksavgrensingar is not None and not isinstance(self.bruksavgrensingar, str):
            self.bruksavgrensingar = str(self.bruksavgrensingar)

        if not isinstance(self.standardoverensstemming, list):
            self.standardoverensstemming = [self.standardoverensstemming] if self.standardoverensstemming is not None else []
        self.standardoverensstemming = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.standardoverensstemming]

        if not isinstance(self.vokabular, list):
            self.vokabular = [self.vokabular] if self.vokabular is not None else []
        self.vokabular = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.vokabular]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Proveniensmetadata(YAMLRoot):
    """
    Metadata om opphav og endringshistorie (FAIR R1.2).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAIR["Proveniensmetadata"]
    class_class_curie: ClassVar[str] = "fair:Proveniensmetadata"
    class_name: ClassVar[str] = "Proveniensmetadata"
    class_model_uri: ClassVar[URIRef] = FAIR.Proveniensmetadata

    ansvarlegAktoer: Optional[Union[str, URIorCURIE]] = None
    generertAvAktivitet: Optional[Union[str, URIorCURIE]] = None
    opprettingsdato: Optional[Union[str, XSDDate]] = None
    endringsdato: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ansvarlegAktoer is not None and not isinstance(self.ansvarlegAktoer, URIorCURIE):
            self.ansvarlegAktoer = URIorCURIE(self.ansvarlegAktoer)

        if self.generertAvAktivitet is not None and not isinstance(self.generertAvAktivitet, URIorCURIE):
            self.generertAvAktivitet = URIorCURIE(self.generertAvAktivitet)

        if self.opprettingsdato is not None and not isinstance(self.opprettingsdato, XSDDate):
            self.opprettingsdato = XSDDate(self.opprettingsdato)

        if self.endringsdato is not None and not isinstance(self.endringsdato, XSDDate):
            self.endringsdato = XSDDate(self.endringsdato)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Katalogregistrering(YAMLRoot):
    """
    Dokumenterer registrering i søkbar katalog (FAIR F4).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FAIR["Katalogregistrering"]
    class_class_curie: ClassVar[str] = "fair:Katalogregistrering"
    class_name: ClassVar[str] = "Katalogregistrering"
    class_model_uri: ClassVar[URIRef] = FAIR.Katalogregistrering

    registrertIKatalog: Optional[Union[str, URIorCURIE]] = None
    katalogOppfoeringURL: Optional[Union[str, URIorCURIE]] = None
    registreringsdato: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.registrertIKatalog is not None and not isinstance(self.registrertIKatalog, URIorCURIE):
            self.registrertIKatalog = URIorCURIE(self.registrertIKatalog)

        if self.katalogOppfoeringURL is not None and not isinstance(self.katalogOppfoeringURL, URIorCURIE):
            self.katalogOppfoeringURL = URIorCURIE(self.katalogOppfoeringURL)

        if self.registreringsdato is not None and not isinstance(self.registreringsdato, XSDDate):
            self.registreringsdato = XSDDate(self.registreringsdato)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=DCT.identifier, name="id", curie=DCT.curie('identifier'),
                   model_uri=FAIR.id, domain=None, range=URIRef)

slots.ressursIdentifikator = Slot(uri=DCT.identifier, name="ressursIdentifikator", curie=DCT.curie('identifier'),
                   model_uri=FAIR.ressursIdentifikator, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.ressurstype = Slot(uri=DCT.type, name="ressurstype", curie=DCT.curie('type'),
                   model_uri=FAIR.ressurstype, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.beskrivelse = Slot(uri=DCT.subject, name="beskrivelse", curie=DCT.curie('subject'),
                   model_uri=FAIR.beskrivelse, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.tilgangsmetadata = Slot(uri=FAIR.tilgangsmetadata, name="tilgangsmetadata", curie=FAIR.curie('tilgangsmetadata'),
                   model_uri=FAIR.tilgangsmetadata, domain=None, range=Optional[Union[dict, Tilgangsmetadata]])

slots.gjenbruksmetadata = Slot(uri=FAIR.gjenbruksmetadata, name="gjenbruksmetadata", curie=FAIR.curie('gjenbruksmetadata'),
                   model_uri=FAIR.gjenbruksmetadata, domain=None, range=Optional[Union[dict, Gjenbruksmetadata]])

slots.proveniensmetadata = Slot(uri=FAIR.proveniensmetadata, name="proveniensmetadata", curie=FAIR.curie('proveniensmetadata'),
                   model_uri=FAIR.proveniensmetadata, domain=None, range=Optional[Union[dict, Proveniensmetadata]])

slots.katalogregistrering = Slot(uri=FAIR.katalogregistrering, name="katalogregistrering", curie=FAIR.curie('katalogregistrering'),
                   model_uri=FAIR.katalogregistrering, domain=None, range=Optional[Union[dict, Katalogregistrering]])

slots.tilgangsURL = Slot(uri=DCAT.accessURL, name="tilgangsURL", curie=DCAT.curie('accessURL'),
                   model_uri=FAIR.tilgangsURL, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.tilgangsprotokoll = Slot(uri=FAIR.tilgangsprotokoll, name="tilgangsprotokoll", curie=FAIR.curie('tilgangsprotokoll'),
                   model_uri=FAIR.tilgangsprotokoll, domain=None, range=Optional[str])

slots.tilgangsrettar = Slot(uri=DCT.accessRights, name="tilgangsrettar", curie=DCT.curie('accessRights'),
                   model_uri=FAIR.tilgangsrettar, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.autentiseringPaakrevd = Slot(uri=FAIR.autentiseringPaakrevd, name="autentiseringPaakrevd", curie=FAIR.curie('autentiseringPaakrevd'),
                   model_uri=FAIR.autentiseringPaakrevd, domain=None, range=Optional[Union[bool, Bool]])

slots.metadataPersistens = Slot(uri=FAIR.metadataPersistens, name="metadataPersistens", curie=FAIR.curie('metadataPersistens'),
                   model_uri=FAIR.metadataPersistens, domain=None, range=Optional[Union[bool, Bool]])

slots.lisens = Slot(uri=DCT.license, name="lisens", curie=DCT.curie('license'),
                   model_uri=FAIR.lisens, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.bruksavgrensingar = Slot(uri=DCT.rights, name="bruksavgrensingar", curie=DCT.curie('rights'),
                   model_uri=FAIR.bruksavgrensingar, domain=None, range=Optional[str])

slots.standardoverensstemming = Slot(uri=DCT.conformsTo, name="standardoverensstemming", curie=DCT.curie('conformsTo'),
                   model_uri=FAIR.standardoverensstemming, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.vokabular = Slot(uri=FAIR.vokabular, name="vokabular", curie=FAIR.curie('vokabular'),
                   model_uri=FAIR.vokabular, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.ansvarlegAktoer = Slot(uri=PROV.wasAttributedTo, name="ansvarlegAktoer", curie=PROV.curie('wasAttributedTo'),
                   model_uri=FAIR.ansvarlegAktoer, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.generertAvAktivitet = Slot(uri=PROV.wasGeneratedBy, name="generertAvAktivitet", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=FAIR.generertAvAktivitet, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.opprettingsdato = Slot(uri=DCT.created, name="opprettingsdato", curie=DCT.curie('created'),
                   model_uri=FAIR.opprettingsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.endringsdato = Slot(uri=DCT.modified, name="endringsdato", curie=DCT.curie('modified'),
                   model_uri=FAIR.endringsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.registrertIKatalog = Slot(uri=FAIR.registrertIKatalog, name="registrertIKatalog", curie=FAIR.curie('registrertIKatalog'),
                   model_uri=FAIR.registrertIKatalog, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.katalogOppfoeringURL = Slot(uri=FAIR.katalogOppfoeringURL, name="katalogOppfoeringURL", curie=FAIR.curie('katalogOppfoeringURL'),
                   model_uri=FAIR.katalogOppfoeringURL, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.registreringsdato = Slot(uri=FAIR.registreringsdato, name="registreringsdato", curie=FAIR.curie('registreringsdato'),
                   model_uri=FAIR.registreringsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.FAIRMetadata_ressursIdentifikator = Slot(uri=DCT.identifier, name="FAIRMetadata_ressursIdentifikator", curie=DCT.curie('identifier'),
                   model_uri=FAIR.FAIRMetadata_ressursIdentifikator, domain=FAIRMetadata, range=Union[str, URIorCURIE])

slots.FAIRMetadata_ressurstype = Slot(uri=DCT.type, name="FAIRMetadata_ressurstype", curie=DCT.curie('type'),
                   model_uri=FAIR.FAIRMetadata_ressurstype, domain=FAIRMetadata, range=Union[str, URIorCURIE])

slots.FAIRMetadata_beskrivelse = Slot(uri=DCT.subject, name="FAIRMetadata_beskrivelse", curie=DCT.curie('subject'),
                   model_uri=FAIR.FAIRMetadata_beskrivelse, domain=FAIRMetadata, range=Optional[Union[str, URIorCURIE]])

slots.FAIRMetadata_tilgangsmetadata = Slot(uri=FAIR.tilgangsmetadata, name="FAIRMetadata_tilgangsmetadata", curie=FAIR.curie('tilgangsmetadata'),
                   model_uri=FAIR.FAIRMetadata_tilgangsmetadata, domain=FAIRMetadata, range=Optional[Union[dict, "Tilgangsmetadata"]])

slots.FAIRMetadata_gjenbruksmetadata = Slot(uri=FAIR.gjenbruksmetadata, name="FAIRMetadata_gjenbruksmetadata", curie=FAIR.curie('gjenbruksmetadata'),
                   model_uri=FAIR.FAIRMetadata_gjenbruksmetadata, domain=FAIRMetadata, range=Optional[Union[dict, "Gjenbruksmetadata"]])

slots.FAIRMetadata_proveniensmetadata = Slot(uri=FAIR.proveniensmetadata, name="FAIRMetadata_proveniensmetadata", curie=FAIR.curie('proveniensmetadata'),
                   model_uri=FAIR.FAIRMetadata_proveniensmetadata, domain=FAIRMetadata, range=Optional[Union[dict, "Proveniensmetadata"]])

slots.FAIRMetadata_katalogregistrering = Slot(uri=FAIR.katalogregistrering, name="FAIRMetadata_katalogregistrering", curie=FAIR.curie('katalogregistrering'),
                   model_uri=FAIR.FAIRMetadata_katalogregistrering, domain=FAIRMetadata, range=Optional[Union[dict, "Katalogregistrering"]])

slots.Tilgangsmetadata_tilgangsURL = Slot(uri=DCAT.accessURL, name="Tilgangsmetadata_tilgangsURL", curie=DCAT.curie('accessURL'),
                   model_uri=FAIR.Tilgangsmetadata_tilgangsURL, domain=Tilgangsmetadata, range=Optional[Union[str, URIorCURIE]])

slots.Tilgangsmetadata_tilgangsprotokoll = Slot(uri=FAIR.tilgangsprotokoll, name="Tilgangsmetadata_tilgangsprotokoll", curie=FAIR.curie('tilgangsprotokoll'),
                   model_uri=FAIR.Tilgangsmetadata_tilgangsprotokoll, domain=Tilgangsmetadata, range=Optional[str])

slots.Tilgangsmetadata_tilgangsrettar = Slot(uri=DCT.accessRights, name="Tilgangsmetadata_tilgangsrettar", curie=DCT.curie('accessRights'),
                   model_uri=FAIR.Tilgangsmetadata_tilgangsrettar, domain=Tilgangsmetadata, range=Optional[Union[str, URIorCURIE]])

slots.Tilgangsmetadata_autentiseringPaakrevd = Slot(uri=FAIR.autentiseringPaakrevd, name="Tilgangsmetadata_autentiseringPaakrevd", curie=FAIR.curie('autentiseringPaakrevd'),
                   model_uri=FAIR.Tilgangsmetadata_autentiseringPaakrevd, domain=Tilgangsmetadata, range=Optional[Union[bool, Bool]])

slots.Tilgangsmetadata_metadataPersistens = Slot(uri=FAIR.metadataPersistens, name="Tilgangsmetadata_metadataPersistens", curie=FAIR.curie('metadataPersistens'),
                   model_uri=FAIR.Tilgangsmetadata_metadataPersistens, domain=Tilgangsmetadata, range=Optional[Union[bool, Bool]])

slots.Gjenbruksmetadata_lisens = Slot(uri=DCT.license, name="Gjenbruksmetadata_lisens", curie=DCT.curie('license'),
                   model_uri=FAIR.Gjenbruksmetadata_lisens, domain=Gjenbruksmetadata, range=Optional[Union[str, URIorCURIE]])

slots.Gjenbruksmetadata_bruksavgrensingar = Slot(uri=DCT.rights, name="Gjenbruksmetadata_bruksavgrensingar", curie=DCT.curie('rights'),
                   model_uri=FAIR.Gjenbruksmetadata_bruksavgrensingar, domain=Gjenbruksmetadata, range=Optional[str])

slots.Gjenbruksmetadata_standardoverensstemming = Slot(uri=DCT.conformsTo, name="Gjenbruksmetadata_standardoverensstemming", curie=DCT.curie('conformsTo'),
                   model_uri=FAIR.Gjenbruksmetadata_standardoverensstemming, domain=Gjenbruksmetadata, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Gjenbruksmetadata_vokabular = Slot(uri=FAIR.vokabular, name="Gjenbruksmetadata_vokabular", curie=FAIR.curie('vokabular'),
                   model_uri=FAIR.Gjenbruksmetadata_vokabular, domain=Gjenbruksmetadata, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Proveniensmetadata_ansvarlegAktoer = Slot(uri=PROV.wasAttributedTo, name="Proveniensmetadata_ansvarlegAktoer", curie=PROV.curie('wasAttributedTo'),
                   model_uri=FAIR.Proveniensmetadata_ansvarlegAktoer, domain=Proveniensmetadata, range=Optional[Union[str, URIorCURIE]])

slots.Proveniensmetadata_generertAvAktivitet = Slot(uri=PROV.wasGeneratedBy, name="Proveniensmetadata_generertAvAktivitet", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=FAIR.Proveniensmetadata_generertAvAktivitet, domain=Proveniensmetadata, range=Optional[Union[str, URIorCURIE]])

slots.Proveniensmetadata_opprettingsdato = Slot(uri=DCT.created, name="Proveniensmetadata_opprettingsdato", curie=DCT.curie('created'),
                   model_uri=FAIR.Proveniensmetadata_opprettingsdato, domain=Proveniensmetadata, range=Optional[Union[str, XSDDate]])

slots.Proveniensmetadata_endringsdato = Slot(uri=DCT.modified, name="Proveniensmetadata_endringsdato", curie=DCT.curie('modified'),
                   model_uri=FAIR.Proveniensmetadata_endringsdato, domain=Proveniensmetadata, range=Optional[Union[str, XSDDate]])

slots.Katalogregistrering_registrertIKatalog = Slot(uri=FAIR.registrertIKatalog, name="Katalogregistrering_registrertIKatalog", curie=FAIR.curie('registrertIKatalog'),
                   model_uri=FAIR.Katalogregistrering_registrertIKatalog, domain=Katalogregistrering, range=Optional[Union[str, URIorCURIE]])

slots.Katalogregistrering_katalogOppfoeringURL = Slot(uri=FAIR.katalogOppfoeringURL, name="Katalogregistrering_katalogOppfoeringURL", curie=FAIR.curie('katalogOppfoeringURL'),
                   model_uri=FAIR.Katalogregistrering_katalogOppfoeringURL, domain=Katalogregistrering, range=Optional[Union[str, URIorCURIE]])

slots.Katalogregistrering_registreringsdato = Slot(uri=FAIR.registreringsdato, name="Katalogregistrering_registreringsdato", curie=FAIR.curie('registreringsdato'),
                   model_uri=FAIR.Katalogregistrering_registreringsdato, domain=Katalogregistrering, range=Optional[Union[str, XSDDate]])

