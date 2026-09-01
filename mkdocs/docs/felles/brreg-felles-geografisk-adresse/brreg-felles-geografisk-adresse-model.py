# Auto generated from brreg-felles-geografisk-adresse-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-09-01T05:18:49
# Schema: brreg-felles-geografisk-adresse
#
# id: https://data.norge.no/felles/brreg-felles-geografisk-adresse
# description: Gjenbrukbare geografiske adresseklassar utleia frå Brønnøysundregistrene (BR) sin interne BRReferansemodell_v3 (MagicDraw/XMI), pakken "Adresse" (GeografiskAdresse-hierarkiet), pluss dei adresse-relaterte komplekstypane frå Strukturtypekatalog_v1 (Poststed, Kommune, Fylke, Matrikkelnummer, Adressenummer) som adressehierarkiet er avhengig av. Sjå specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md for bakgrunn, metode og avklaringane denne modellen byggjer på.
# license: https://data.norge.no/nlod/no/2.0

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

from linkml_runtime.linkml_model.types import Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.11.0"
version = "0.1.0"

# Namespaces
BRREG_FELLES_GEOGRAFISK_ADRESSE = CurieNamespace('brreg_felles_geografisk_adresse', 'https://data.norge.no/felles/brreg-felles-geografisk-adresse/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LOCN = CurieNamespace('locn', 'http://www.w3.org/ns/locn#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BRREG_FELLES_GEOGRAFISK_ADRESSE


# Types
class AnyURI(str):
    """ Ein absolutt eller relativ URI (xsd:anyURI). """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "AnyURI"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.AnyURI


class DateTime(str):
    """ Dato og klokkeslett (xsd:dateTime). """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "DateTime"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.DateTime


class Long(str):
    """ Eit 64-bits heiltal (xsd:long). """
    type_class_uri = XSD["long"]
    type_class_curie = "xsd:long"
    type_name = "Long"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Long


class BrregGYear(str):
    """ Eit årstal (xsd:gYear). """
    type_class_uri = XSD["gYear"]
    type_class_curie = "xsd:gYear"
    type_name = "BrregGYear"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.BrregGYear


class GYearMonth(str):
    """ Månad og år (xsd:gYearMonth). """
    type_class_uri = XSD["gYearMonth"]
    type_class_curie = "xsd:gYearMonth"
    type_name = "GYearMonth"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.GYearMonth


class Int(str):
    """ Eit heiltal, opphavleg xsd:int i kjelda. """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "Int"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Int


class Short(str):
    """ Eit 16-bits heiltal (xsd:short). """
    type_class_uri = XSD["short"]
    type_class_curie = "xsd:short"
    type_name = "Short"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Short


class NegativeInteger(str):
    """ Eit heiltal mindre enn null (xsd:negativeInteger). """
    type_class_uri = XSD["negativeInteger"]
    type_class_curie = "xsd:negativeInteger"
    type_name = "NegativeInteger"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.NegativeInteger


class NonPositiveInteger(str):
    """ Eit heiltal mindre enn eller lik null (xsd:nonPositiveInteger). """
    type_class_uri = XSD["nonPositiveInteger"]
    type_class_curie = "xsd:nonPositiveInteger"
    type_name = "NonPositiveInteger"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.NonPositiveInteger


class PositiveInteger(str):
    """ Eit heiltal større enn null (xsd:positiveInteger). """
    type_class_uri = XSD["positiveInteger"]
    type_class_curie = "xsd:positiveInteger"
    type_name = "PositiveInteger"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.PositiveInteger


class BrregNonNegativeInteger(str):
    """ Eit heiltal større enn eller lik null (xsd:nonNegativeInteger). """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "BrregNonNegativeInteger"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.BrregNonNegativeInteger


class HexBinary(str):
    """ Binærdata heksadesimalt koda (xsd:hexBinary). """
    type_class_uri = XSD["hexBinary"]
    type_class_curie = "xsd:hexBinary"
    type_name = "HexBinary"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.HexBinary


class Base64Binary(str):
    """ Binærdata base64-koda (xsd:base64Binary). """
    type_class_uri = XSD["base64Binary"]
    type_class_curie = "xsd:base64Binary"
    type_name = "Base64Binary"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Base64Binary


class Token(str):
    """ Ein normalisert tekststreng utan linjeskift/dobbelt mellomrom (xsd:token). """
    type_class_uri = XSD["token"]
    type_class_curie = "xsd:token"
    type_name = "Token"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Token


class Saksstatus(str):
    """ Kode for status på ei sak hos BR. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Saksstatus"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Saksstatus


class Fylkesnummer(str):
    """ Nummerkode for fylke, jf. SSB sin fylkesinndeling. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Fylkesnummer"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Fylkesnummer


class Spraakkode(str):
    """ Kode for skriftspråk/målform. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Spraakkode"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Spraakkode


class InstitusjonellSektorkode(str):
    """ SSB sin institusjonelle sektorkode for ei verksemd. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "InstitusjonellSektorkode"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.InstitusjonellSektorkode


class Valutakode(str):
    """ ISO 4217-valutakode. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Valutakode"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Valutakode


class Landkode(str):
    """ Kode for land. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Landkode"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Landkode


class Postnummer(str):
    """ Norsk postnummer (4 sifer). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Postnummer"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Postnummer


class Organisasjonsform(str):
    """ Kode for organisasjonsform, jf. Einingsregisteret sitt kodeverk. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Organisasjonsform"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Organisasjonsform


class Kommunenummer(str):
    """ Norsk kommunenummer (4 sifer). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Kommunenummer"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Kommunenummer


class Virksomhetsstatus(str):
    """ Kode for status på ei verksemd (t.d. aktiv, konkurs, oppløyst). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Virksomhetsstatus"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Virksomhetsstatus


class Naeringskode(str):
    """ Kode frå SSB sin standard for næringsgruppering (SN2007). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Naeringskode"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Naeringskode


class PersonstatusType(str):
    """ Kode for status på ein person i BR sine register. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "PersonstatusType"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.PersonstatusType


class LandkodeIsoAlpha3(str):
    """ ISO 3166-1 alpha-3-landkode (t.d. NOR). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "LandkodeIsoAlpha3"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.LandkodeIsoAlpha3


class Epostadresse(str):
    """ Ei e-postadresse. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Epostadresse"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Epostadresse


class PrefiksMedNasjonalKode(str):
    """ Internasjonalt telefonprefiks (landkode), t.d. "+47". """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "PrefiksMedNasjonalKode"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.PrefiksMedNasjonalKode


class Husbokstav(str):
    """ Husbokstav i ei vegadresse. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Husbokstav"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Husbokstav


class Husnummer(str):
    """ Husnummer i ei vegadresse. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Husnummer"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Husnummer


class NasjonaltNummer(str):
    """ Telefonnummer utan landkode/prefiks. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "NasjonaltNummer"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.NasjonaltNummer


class Virksomhetsnavn(str):
    """ Namnet på ei verksemd, slik det er registrert i Einingsregisteret. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Virksomhetsnavn"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Virksomhetsnavn


class Organisasjonsnummer(str):
    """ Organisasjonsnummer for ei norsk verksemd (9 sifer), jf. Einingsregisteret. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Organisasjonsnummer"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Organisasjonsnummer


class BRPersonId(str):
    """ BR sin interne identifikator for ein person. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "BRPersonId"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.BRPersonId


class Kontonummer(str):
    """ Norsk bankkontonummer (11 sifer). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Kontonummer"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Kontonummer


class Aktivitetskode(str):
    """ Kode for ein aktivitetstype i BR sine register. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Aktivitetskode"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Aktivitetskode


class AktoerId(str):
    """ BR sin interne identifikator for ein aktør (person eller verksemd). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "AktoerId"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.AktoerId


class Foedselsnummer(str):
    """ Norsk fødselsnummer eller D-nummer (11 sifer). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Foedselsnummer"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Foedselsnummer


class Binaerobjekt(str):
    """ Eit vedlagt binærobjekt (t.d. eit dokument), base64-koda. """
    type_class_uri = XSD["base64Binary"]
    type_class_curie = "xsd:base64Binary"
    type_name = "Binaerobjekt"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Binaerobjekt


class URI(str):
    """ Ein Uniform Resource Identifier. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "URI"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.URI


class URL(str):
    """ Ein Uniform Resource Locator (nettadresse). """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "URL"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.URL


class UUID(str):
    """ Ein universelt unik identifikator (UUID/GUID). Strukturtypekatalog_v1 kallar den tilsvarande typen sin "GUID" — denne modellen brukar "UUID" konsekvent, jf. avklaring i specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "UUID"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.UUID


class Beloep(str):
    """ Eit pengebeløp. """
    type_class_uri = XSD["decimal"]
    type_class_curie = "xsd:decimal"
    type_name = "Beloep"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Beloep


class MappeId(str):
    """ BR sin interne identifikator for ei saksmappe. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "MappeId"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.MappeId


class Tekst50(str):
    """ Fritekst avgrensa til 50 teikn. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Tekst50"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Tekst50


class Tekst255(str):
    """ Fritekst avgrensa til 255 teikn. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Tekst255"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Tekst255


class Tekst1000(str):
    """ Fritekst avgrensa til 1000 teikn. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Tekst1000"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Tekst1000


class Postboksnummer(str):
    """ Nummeret på ein postboks. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Postboksnummer"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Postboksnummer


class BRAdresseId(str):
    """ BR sin interne identifikator for ei adresse. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "BRAdresseId"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.BRAdresseId


class Tekst175(str):
    """ Fritekst avgrensa til 175 teikn. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Tekst175"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Tekst175


class Bruksenhetsnummer(str):
    """ Bruksenhetsnummer (bustadnummer) i ei vegadresse, t.d. "H0101". """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Bruksenhetsnummer"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Bruksenhetsnummer


class Tekst100(str):
    """ Fritekst avgrensa til 100 teikn. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Tekst100"
    type_model_uri = BRREG_FELLES_GEOGRAFISK_ADRESSE.Tekst100


# Class references
class GeografiskAdresseId(URIorCURIE):
    pass


class PostboksadresseId(GeografiskAdresseId):
    pass


class StedsadresseId(GeografiskAdresseId):
    pass


class VegadresseId(GeografiskAdresseId):
    pass


class MatrikkeladresseId(GeografiskAdresseId):
    pass


class InternasjonalAdresseId(GeografiskAdresseId):
    pass


class PoststedId(URIorCURIE):
    pass


class KommuneId(URIorCURIE):
    pass


class FylkeId(URIorCURIE):
    pass


class MatrikkelnummerId(URIorCURIE):
    pass


class AdressenummerId(URIorCURIE):
    pass


@dataclass(repr=False)
class GeografiskAdresse(YAMLRoot):
    """
    Ei geografisk adresse. Abstrakt basisklasse for dei konkrete adressetypane under.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCN["Address"]
    class_class_curie: ClassVar[str] = "locn:Address"
    class_name: ClassVar[str] = "GeografiskAdresse"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE.GeografiskAdresse

    id: Union[str, GeografiskAdresseId] = None
    br_adresse_id: Optional[str] = None
    co_navn: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeografiskAdresseId):
            self.id = GeografiskAdresseId(self.id)

        if self.br_adresse_id is not None and not isinstance(self.br_adresse_id, str):
            self.br_adresse_id = str(self.br_adresse_id)

        if self.co_navn is not None and not isinstance(self.co_navn, str):
            self.co_navn = str(self.co_navn)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Postboksadresse(GeografiskAdresse):
    """
    Ei postboksadresse.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE["Postboksadresse"]
    class_class_curie: ClassVar[str] = "brreg_felles_geografisk_adresse:Postboksadresse"
    class_name: ClassVar[str] = "Postboksadresse"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE.Postboksadresse

    id: Union[str, PostboksadresseId] = None
    postboksnummer: Optional[str] = None
    anleggsnavn: Optional[str] = None
    poststed: Optional[Union[str, PoststedId]] = None
    kommune: Optional[Union[str, KommuneId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PostboksadresseId):
            self.id = PostboksadresseId(self.id)

        if self.postboksnummer is not None and not isinstance(self.postboksnummer, str):
            self.postboksnummer = str(self.postboksnummer)

        if self.anleggsnavn is not None and not isinstance(self.anleggsnavn, str):
            self.anleggsnavn = str(self.anleggsnavn)

        if self.poststed is not None and not isinstance(self.poststed, PoststedId):
            self.poststed = PoststedId(self.poststed)

        if self.kommune is not None and not isinstance(self.kommune, KommuneId):
            self.kommune = KommuneId(self.kommune)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Stedsadresse(GeografiskAdresse):
    """
    Ei stadfesta adresse utan vegadresse (t.d. i utmark).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE["Stedsadresse"]
    class_class_curie: ClassVar[str] = "brreg_felles_geografisk_adresse:Stedsadresse"
    class_name: ClassVar[str] = "Stedsadresse"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE.Stedsadresse

    id: Union[str, StedsadresseId] = None
    stedsnavn: Optional[str] = None
    poststed: Optional[Union[str, PoststedId]] = None
    kommune: Optional[Union[str, KommuneId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StedsadresseId):
            self.id = StedsadresseId(self.id)

        if self.stedsnavn is not None and not isinstance(self.stedsnavn, str):
            self.stedsnavn = str(self.stedsnavn)

        if self.poststed is not None and not isinstance(self.poststed, PoststedId):
            self.poststed = PoststedId(self.poststed)

        if self.kommune is not None and not isinstance(self.kommune, KommuneId):
            self.kommune = KommuneId(self.kommune)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Vegadresse(GeografiskAdresse):
    """
    Ei vegadresse (adressenavn + adressenummer).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE["Vegadresse"]
    class_class_curie: ClassVar[str] = "brreg_felles_geografisk_adresse:Vegadresse"
    class_name: ClassVar[str] = "Vegadresse"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE.Vegadresse

    id: Union[str, VegadresseId] = None
    vegadresse_id: Optional[str] = None
    bruksenhetsnummer: Optional[str] = None
    adressenavn: Optional[str] = None
    kort_adressenavn: Optional[str] = None
    adressenummer: Optional[Union[str, AdressenummerId]] = None
    poststed: Optional[Union[str, PoststedId]] = None
    adressetilleggsnavn: Optional[str] = None
    kommune: Optional[Union[str, KommuneId]] = None
    fylke: Optional[Union[str, FylkeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VegadresseId):
            self.id = VegadresseId(self.id)

        if self.vegadresse_id is not None and not isinstance(self.vegadresse_id, str):
            self.vegadresse_id = str(self.vegadresse_id)

        if self.bruksenhetsnummer is not None and not isinstance(self.bruksenhetsnummer, str):
            self.bruksenhetsnummer = str(self.bruksenhetsnummer)

        if self.adressenavn is not None and not isinstance(self.adressenavn, str):
            self.adressenavn = str(self.adressenavn)

        if self.kort_adressenavn is not None and not isinstance(self.kort_adressenavn, str):
            self.kort_adressenavn = str(self.kort_adressenavn)

        if self.adressenummer is not None and not isinstance(self.adressenummer, AdressenummerId):
            self.adressenummer = AdressenummerId(self.adressenummer)

        if self.poststed is not None and not isinstance(self.poststed, PoststedId):
            self.poststed = PoststedId(self.poststed)

        if self.adressetilleggsnavn is not None and not isinstance(self.adressetilleggsnavn, str):
            self.adressetilleggsnavn = str(self.adressetilleggsnavn)

        if self.kommune is not None and not isinstance(self.kommune, KommuneId):
            self.kommune = KommuneId(self.kommune)

        if self.fylke is not None and not isinstance(self.fylke, FylkeId):
            self.fylke = FylkeId(self.fylke)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Matrikkeladresse(GeografiskAdresse):
    """
    Ei matrikkeladresse (knytt til eit matrikkelnummer).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE["Matrikkeladresse"]
    class_class_curie: ClassVar[str] = "brreg_felles_geografisk_adresse:Matrikkeladresse"
    class_name: ClassVar[str] = "Matrikkeladresse"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE.Matrikkeladresse

    id: Union[str, MatrikkeladresseId] = None
    matrikkeladresse_id: Optional[str] = None
    bruksenhetsnummer: Optional[str] = None
    adressetilleggsnavn: Optional[str] = None
    matrikkelnummer: Optional[Union[str, MatrikkelnummerId]] = None
    undernummer: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MatrikkeladresseId):
            self.id = MatrikkeladresseId(self.id)

        if self.matrikkeladresse_id is not None and not isinstance(self.matrikkeladresse_id, str):
            self.matrikkeladresse_id = str(self.matrikkeladresse_id)

        if self.bruksenhetsnummer is not None and not isinstance(self.bruksenhetsnummer, str):
            self.bruksenhetsnummer = str(self.bruksenhetsnummer)

        if self.adressetilleggsnavn is not None and not isinstance(self.adressetilleggsnavn, str):
            self.adressetilleggsnavn = str(self.adressetilleggsnavn)

        if self.matrikkelnummer is not None and not isinstance(self.matrikkelnummer, MatrikkelnummerId):
            self.matrikkelnummer = MatrikkelnummerId(self.matrikkelnummer)

        if self.undernummer is not None and not isinstance(self.undernummer, int):
            self.undernummer = int(self.undernummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InternasjonalAdresse(GeografiskAdresse):
    """
    Ei adresse i eit anna land enn Noreg, i fri form.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE["InternasjonalAdresse"]
    class_class_curie: ClassVar[str] = "brreg_felles_geografisk_adresse:InternasjonalAdresse"
    class_name: ClassVar[str] = "InternasjonalAdresse"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE.InternasjonalAdresse

    id: Union[str, InternasjonalAdresseId] = None
    adressenavn: Optional[str] = None
    adressenummer_tekst: Optional[str] = None
    bygning: Optional[str] = None
    etasjenummer: Optional[str] = None
    boenhet: Optional[str] = None
    postboks: Optional[str] = None
    postkode: Optional[str] = None
    by_eller_stedsnavn: Optional[str] = None
    region: Optional[str] = None
    distrikt_eller_bydel: Optional[str] = None
    landkode: Optional[str] = None
    fri_adressetekst: Optional[str] = None
    adresseidentifikator: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InternasjonalAdresseId):
            self.id = InternasjonalAdresseId(self.id)

        if self.adressenavn is not None and not isinstance(self.adressenavn, str):
            self.adressenavn = str(self.adressenavn)

        if self.adressenummer_tekst is not None and not isinstance(self.adressenummer_tekst, str):
            self.adressenummer_tekst = str(self.adressenummer_tekst)

        if self.bygning is not None and not isinstance(self.bygning, str):
            self.bygning = str(self.bygning)

        if self.etasjenummer is not None and not isinstance(self.etasjenummer, str):
            self.etasjenummer = str(self.etasjenummer)

        if self.boenhet is not None and not isinstance(self.boenhet, str):
            self.boenhet = str(self.boenhet)

        if self.postboks is not None and not isinstance(self.postboks, str):
            self.postboks = str(self.postboks)

        if self.postkode is not None and not isinstance(self.postkode, str):
            self.postkode = str(self.postkode)

        if self.by_eller_stedsnavn is not None and not isinstance(self.by_eller_stedsnavn, str):
            self.by_eller_stedsnavn = str(self.by_eller_stedsnavn)

        if self.region is not None and not isinstance(self.region, str):
            self.region = str(self.region)

        if self.distrikt_eller_bydel is not None and not isinstance(self.distrikt_eller_bydel, str):
            self.distrikt_eller_bydel = str(self.distrikt_eller_bydel)

        if self.landkode is not None and not isinstance(self.landkode, str):
            self.landkode = str(self.landkode)

        if self.fri_adressetekst is not None and not isinstance(self.fri_adressetekst, str):
            self.fri_adressetekst = str(self.fri_adressetekst)

        if self.adresseidentifikator is not None and not isinstance(self.adresseidentifikator, str):
            self.adresseidentifikator = str(self.adresseidentifikator)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Poststed(YAMLRoot):
    """
    Eit poststed knytt til eit postnummer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE["Poststed"]
    class_class_curie: ClassVar[str] = "brreg_felles_geografisk_adresse:Poststed"
    class_name: ClassVar[str] = "Poststed"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE.Poststed

    id: Union[str, PoststedId] = None
    navn: str = None
    postnummer: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PoststedId):
            self.id = PoststedId(self.id)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self._is_empty(self.postnummer):
            self.MissingRequiredField("postnummer")
        if not isinstance(self.postnummer, str):
            self.postnummer = str(self.postnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kommune(YAMLRoot):
    """
    Ein norsk kommune.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE["Kommune"]
    class_class_curie: ClassVar[str] = "brreg_felles_geografisk_adresse:Kommune"
    class_name: ClassVar[str] = "Kommune"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE.Kommune

    id: Union[str, KommuneId] = None
    kommunenummer: str = None
    kommunenavn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KommuneId):
            self.id = KommuneId(self.id)

        if self._is_empty(self.kommunenummer):
            self.MissingRequiredField("kommunenummer")
        if not isinstance(self.kommunenummer, str):
            self.kommunenummer = str(self.kommunenummer)

        if self._is_empty(self.kommunenavn):
            self.MissingRequiredField("kommunenavn")
        if not isinstance(self.kommunenavn, str):
            self.kommunenavn = str(self.kommunenavn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fylke(YAMLRoot):
    """
    Eit norsk fylke.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE["Fylke"]
    class_class_curie: ClassVar[str] = "brreg_felles_geografisk_adresse:Fylke"
    class_name: ClassVar[str] = "Fylke"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE.Fylke

    id: Union[str, FylkeId] = None
    fylkesnummer: str = None
    fylkesnavn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FylkeId):
            self.id = FylkeId(self.id)

        if self._is_empty(self.fylkesnummer):
            self.MissingRequiredField("fylkesnummer")
        if not isinstance(self.fylkesnummer, str):
            self.fylkesnummer = str(self.fylkesnummer)

        if self._is_empty(self.fylkesnavn):
            self.MissingRequiredField("fylkesnavn")
        if not isinstance(self.fylkesnavn, str):
            self.fylkesnavn = str(self.fylkesnavn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Matrikkelnummer(YAMLRoot):
    """
    Eit matrikkelnummer (gårds-, bruks-, feste- og seksjonsnummer).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE["Matrikkelnummer"]
    class_class_curie: ClassVar[str] = "brreg_felles_geografisk_adresse:Matrikkelnummer"
    class_name: ClassVar[str] = "Matrikkelnummer"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE.Matrikkelnummer

    id: Union[str, MatrikkelnummerId] = None
    kommunenummer: str = None
    gaardsnummer: int = None
    bruksnummer: int = None
    festenummer: Optional[int] = None
    seksjonsnummer: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MatrikkelnummerId):
            self.id = MatrikkelnummerId(self.id)

        if self._is_empty(self.kommunenummer):
            self.MissingRequiredField("kommunenummer")
        if not isinstance(self.kommunenummer, str):
            self.kommunenummer = str(self.kommunenummer)

        if self._is_empty(self.gaardsnummer):
            self.MissingRequiredField("gaardsnummer")
        if not isinstance(self.gaardsnummer, int):
            self.gaardsnummer = int(self.gaardsnummer)

        if self._is_empty(self.bruksnummer):
            self.MissingRequiredField("bruksnummer")
        if not isinstance(self.bruksnummer, int):
            self.bruksnummer = int(self.bruksnummer)

        if self.festenummer is not None and not isinstance(self.festenummer, int):
            self.festenummer = int(self.festenummer)

        if self.seksjonsnummer is not None and not isinstance(self.seksjonsnummer, int):
            self.seksjonsnummer = int(self.seksjonsnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Adressenummer(YAMLRoot):
    """
    Adressenummeret (husnummer og eventuell husbokstav) i ei vegadresse.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE["Adressenummer"]
    class_class_curie: ClassVar[str] = "brreg_felles_geografisk_adresse:Adressenummer"
    class_name: ClassVar[str] = "Adressenummer"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_GEOGRAFISK_ADRESSE.Adressenummer

    id: Union[str, AdressenummerId] = None
    nummer: str = None
    bokstav: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdressenummerId):
            self.id = AdressenummerId(self.id)

        if self._is_empty(self.nummer):
            self.MissingRequiredField("nummer")
        if not isinstance(self.nummer, str):
            self.nummer = str(self.nummer)

        if self.bokstav is not None and not isinstance(self.bokstav, str):
            self.bokstav = str(self.bokstav)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.id, name="id", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('id'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.id, domain=None, range=URIRef)

slots.br_adresse_id = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.brAdresseId, name="br_adresse_id", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('brAdresseId'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.br_adresse_id, domain=None, range=Optional[str])

slots.co_navn = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.coNavn, name="co_navn", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('coNavn'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.co_navn, domain=None, range=Optional[str])

slots.type = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.type, name="type", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('type'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.type, domain=None, range=Optional[str])

slots.postboksnummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.postboksnummer, name="postboksnummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('postboksnummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.postboksnummer, domain=None, range=Optional[str])

slots.anleggsnavn = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.anleggsnavn, name="anleggsnavn", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('anleggsnavn'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.anleggsnavn, domain=None, range=Optional[str])

slots.poststed = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.poststed, name="poststed", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('poststed'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.poststed, domain=None, range=Optional[Union[str, PoststedId]])

slots.kommune = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.kommune, name="kommune", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('kommune'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.kommune, domain=None, range=Optional[Union[str, KommuneId]])

slots.stedsnavn = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.stedsnavn, name="stedsnavn", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('stedsnavn'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.stedsnavn, domain=None, range=Optional[str])

slots.vegadresse_id = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.vegadresseId, name="vegadresse_id", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('vegadresseId'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.vegadresse_id, domain=None, range=Optional[str])

slots.bruksenhetsnummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.bruksenhetsnummer, name="bruksenhetsnummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('bruksenhetsnummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.bruksenhetsnummer, domain=None, range=Optional[str])

slots.adressenavn = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.adressenavn, name="adressenavn", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('adressenavn'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.adressenavn, domain=None, range=Optional[str])

slots.kort_adressenavn = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.kortAdressenavn, name="kort_adressenavn", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('kortAdressenavn'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.kort_adressenavn, domain=None, range=Optional[str])

slots.adressenummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.adressenummer, name="adressenummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('adressenummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.adressenummer, domain=None, range=Optional[Union[str, AdressenummerId]])

slots.adressetilleggsnavn = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.adressetilleggsnavn, name="adressetilleggsnavn", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('adressetilleggsnavn'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.adressetilleggsnavn, domain=None, range=Optional[str])

slots.fylke = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.fylke, name="fylke", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('fylke'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.fylke, domain=None, range=Optional[Union[str, FylkeId]])

slots.matrikkeladresse_id = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.matrikkeladresseId, name="matrikkeladresse_id", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('matrikkeladresseId'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.matrikkeladresse_id, domain=None, range=Optional[str])

slots.matrikkelnummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.matrikkelnummer, name="matrikkelnummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('matrikkelnummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.matrikkelnummer, domain=None, range=Optional[Union[str, MatrikkelnummerId]])

slots.undernummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.undernummer, name="undernummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('undernummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.undernummer, domain=None, range=Optional[int])

slots.adressenummer_tekst = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.adressenummerTekst, name="adressenummer_tekst", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('adressenummerTekst'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.adressenummer_tekst, domain=None, range=Optional[str])

slots.bygning = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.bygning, name="bygning", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('bygning'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.bygning, domain=None, range=Optional[str])

slots.etasjenummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.etasjenummer, name="etasjenummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('etasjenummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.etasjenummer, domain=None, range=Optional[str])

slots.boenhet = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.boenhet, name="boenhet", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('boenhet'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.boenhet, domain=None, range=Optional[str])

slots.postboks = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.postboks, name="postboks", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('postboks'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.postboks, domain=None, range=Optional[str])

slots.postkode = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.postkode, name="postkode", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('postkode'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.postkode, domain=None, range=Optional[str])

slots.by_eller_stedsnavn = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.byEllerStedsnavn, name="by_eller_stedsnavn", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('byEllerStedsnavn'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.by_eller_stedsnavn, domain=None, range=Optional[str])

slots.region = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.region, name="region", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('region'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.region, domain=None, range=Optional[str])

slots.distrikt_eller_bydel = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.distriktEllerBydel, name="distrikt_eller_bydel", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('distriktEllerBydel'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.distrikt_eller_bydel, domain=None, range=Optional[str])

slots.landkode = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.landkode, name="landkode", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('landkode'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.landkode, domain=None, range=Optional[str])

slots.fri_adressetekst = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.friAdressetekst, name="fri_adressetekst", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('friAdressetekst'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.fri_adressetekst, domain=None, range=Optional[str])

slots.adresseidentifikator = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.adresseidentifikator, name="adresseidentifikator", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('adresseidentifikator'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.adresseidentifikator, domain=None, range=Optional[str])

slots.navn = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.navn, name="navn", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('navn'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.navn, domain=None, range=Optional[str])

slots.postnummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.postnummer, name="postnummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('postnummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.postnummer, domain=None, range=Optional[str])

slots.kommunenummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.kommunenummer, name="kommunenummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('kommunenummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.kommunenummer, domain=None, range=Optional[str])

slots.kommunenavn = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.kommunenavn, name="kommunenavn", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('kommunenavn'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.kommunenavn, domain=None, range=Optional[str])

slots.fylkesnummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.fylkesnummer, name="fylkesnummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('fylkesnummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.fylkesnummer, domain=None, range=Optional[str])

slots.fylkesnavn = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.fylkesnavn, name="fylkesnavn", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('fylkesnavn'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.fylkesnavn, domain=None, range=Optional[str])

slots.gaardsnummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.gaardsnummer, name="gaardsnummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('gaardsnummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.gaardsnummer, domain=None, range=Optional[int])

slots.bruksnummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.bruksnummer, name="bruksnummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('bruksnummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.bruksnummer, domain=None, range=Optional[int])

slots.festenummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.festenummer, name="festenummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('festenummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.festenummer, domain=None, range=Optional[int])

slots.seksjonsnummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.seksjonsnummer, name="seksjonsnummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('seksjonsnummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.seksjonsnummer, domain=None, range=Optional[int])

slots.nummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.nummer, name="nummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('nummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.nummer, domain=None, range=Optional[str])

slots.bokstav = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.bokstav, name="bokstav", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('bokstav'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.bokstav, domain=None, range=Optional[str])

slots.GeografiskAdresse_br_adresse_id = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.brAdresseId, name="GeografiskAdresse_br_adresse_id", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('brAdresseId'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.GeografiskAdresse_br_adresse_id, domain=GeografiskAdresse, range=Optional[str])

slots.GeografiskAdresse_type = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.type, name="GeografiskAdresse_type", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('type'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.GeografiskAdresse_type, domain=GeografiskAdresse, range=Optional[str])

slots.Vegadresse_vegadresse_id = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.vegadresseId, name="Vegadresse_vegadresse_id", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('vegadresseId'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.Vegadresse_vegadresse_id, domain=Vegadresse, range=Optional[str])

slots.Matrikkeladresse_matrikkeladresse_id = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.matrikkeladresseId, name="Matrikkeladresse_matrikkeladresse_id", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('matrikkeladresseId'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.Matrikkeladresse_matrikkeladresse_id, domain=Matrikkeladresse, range=Optional[str])

slots.InternasjonalAdresse_adressenummer_tekst = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.adressenummerTekst, name="InternasjonalAdresse_adressenummer_tekst", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('adressenummerTekst'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.InternasjonalAdresse_adressenummer_tekst, domain=InternasjonalAdresse, range=Optional[str])

slots.Poststed_navn = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.navn, name="Poststed_navn", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('navn'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.Poststed_navn, domain=Poststed, range=str)

slots.Poststed_postnummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.postnummer, name="Poststed_postnummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('postnummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.Poststed_postnummer, domain=Poststed, range=str)

slots.Kommune_kommunenummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.kommunenummer, name="Kommune_kommunenummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('kommunenummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.Kommune_kommunenummer, domain=Kommune, range=str)

slots.Kommune_kommunenavn = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.kommunenavn, name="Kommune_kommunenavn", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('kommunenavn'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.Kommune_kommunenavn, domain=Kommune, range=str)

slots.Fylke_fylkesnummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.fylkesnummer, name="Fylke_fylkesnummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('fylkesnummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.Fylke_fylkesnummer, domain=Fylke, range=str)

slots.Fylke_fylkesnavn = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.fylkesnavn, name="Fylke_fylkesnavn", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('fylkesnavn'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.Fylke_fylkesnavn, domain=Fylke, range=str)

slots.Matrikkelnummer_kommunenummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.kommunenummer, name="Matrikkelnummer_kommunenummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('kommunenummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.Matrikkelnummer_kommunenummer, domain=Matrikkelnummer, range=str)

slots.Matrikkelnummer_gaardsnummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.gaardsnummer, name="Matrikkelnummer_gaardsnummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('gaardsnummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.Matrikkelnummer_gaardsnummer, domain=Matrikkelnummer, range=int)

slots.Matrikkelnummer_bruksnummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.bruksnummer, name="Matrikkelnummer_bruksnummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('bruksnummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.Matrikkelnummer_bruksnummer, domain=Matrikkelnummer, range=int)

slots.Adressenummer_nummer = Slot(uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.nummer, name="Adressenummer_nummer", curie=BRREG_FELLES_GEOGRAFISK_ADRESSE.curie('nummer'),
                   model_uri=BRREG_FELLES_GEOGRAFISK_ADRESSE.Adressenummer_nummer, domain=Adressenummer, range=str)

