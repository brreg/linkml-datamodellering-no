# Auto generated from brreg-felles-digital-adresse-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-09-01T05:18:49
# Schema: brreg-felles-digital-adresse
#
# id: https://data.norge.no/felles/brreg-felles-digital-adresse
# description: Gjenbrukbare digitale adresseklassar utleia frå Brønnøysundregistrene (BR) sin interne BRReferansemodell_v3 (MagicDraw/XMI), pakken "Adresse" (DigitalAdresse-hierarkiet). Sjå specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md for bakgrunn, metode og avklaringane denne modellen byggjer på.
#   BR sin eigen `Nettadresse`-undertype "Aksesspunkt" er medvite utelaten her: feltet `aksesspunktoperatoer` peikar til `Virksomhet` (definert i brreg-felles-aktoer, som importerer denne modellen) og ville gjort importgrafen sirkulær. Sjå nemnde spec § Funn 4.
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

from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.11.0"
version = "0.1.0"

# Namespaces
BRREG_FELLES_DIGITAL_ADRESSE = CurieNamespace('brreg_felles_digital_adresse', 'https://data.norge.no/felles/brreg-felles-digital-adresse/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BRREG_FELLES_DIGITAL_ADRESSE


# Types
class AnyURI(str):
    """ Ein absolutt eller relativ URI (xsd:anyURI). """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "AnyURI"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.AnyURI


class DateTime(str):
    """ Dato og klokkeslett (xsd:dateTime). """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "DateTime"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.DateTime


class Long(str):
    """ Eit 64-bits heiltal (xsd:long). """
    type_class_uri = XSD["long"]
    type_class_curie = "xsd:long"
    type_name = "Long"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Long


class BrregGYear(str):
    """ Eit årstal (xsd:gYear). """
    type_class_uri = XSD["gYear"]
    type_class_curie = "xsd:gYear"
    type_name = "BrregGYear"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.BrregGYear


class GYearMonth(str):
    """ Månad og år (xsd:gYearMonth). """
    type_class_uri = XSD["gYearMonth"]
    type_class_curie = "xsd:gYearMonth"
    type_name = "GYearMonth"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.GYearMonth


class Int(str):
    """ Eit heiltal, opphavleg xsd:int i kjelda. """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "Int"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Int


class Short(str):
    """ Eit 16-bits heiltal (xsd:short). """
    type_class_uri = XSD["short"]
    type_class_curie = "xsd:short"
    type_name = "Short"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Short


class NegativeInteger(str):
    """ Eit heiltal mindre enn null (xsd:negativeInteger). """
    type_class_uri = XSD["negativeInteger"]
    type_class_curie = "xsd:negativeInteger"
    type_name = "NegativeInteger"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.NegativeInteger


class NonPositiveInteger(str):
    """ Eit heiltal mindre enn eller lik null (xsd:nonPositiveInteger). """
    type_class_uri = XSD["nonPositiveInteger"]
    type_class_curie = "xsd:nonPositiveInteger"
    type_name = "NonPositiveInteger"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.NonPositiveInteger


class PositiveInteger(str):
    """ Eit heiltal større enn null (xsd:positiveInteger). """
    type_class_uri = XSD["positiveInteger"]
    type_class_curie = "xsd:positiveInteger"
    type_name = "PositiveInteger"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.PositiveInteger


class BrregNonNegativeInteger(str):
    """ Eit heiltal større enn eller lik null (xsd:nonNegativeInteger). """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "BrregNonNegativeInteger"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.BrregNonNegativeInteger


class HexBinary(str):
    """ Binærdata heksadesimalt koda (xsd:hexBinary). """
    type_class_uri = XSD["hexBinary"]
    type_class_curie = "xsd:hexBinary"
    type_name = "HexBinary"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.HexBinary


class Base64Binary(str):
    """ Binærdata base64-koda (xsd:base64Binary). """
    type_class_uri = XSD["base64Binary"]
    type_class_curie = "xsd:base64Binary"
    type_name = "Base64Binary"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Base64Binary


class Token(str):
    """ Ein normalisert tekststreng utan linjeskift/dobbelt mellomrom (xsd:token). """
    type_class_uri = XSD["token"]
    type_class_curie = "xsd:token"
    type_name = "Token"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Token


class Saksstatus(str):
    """ Kode for status på ei sak hos BR. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Saksstatus"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Saksstatus


class Fylkesnummer(str):
    """ Nummerkode for fylke, jf. SSB sin fylkesinndeling. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Fylkesnummer"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Fylkesnummer


class Spraakkode(str):
    """ Kode for skriftspråk/målform. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Spraakkode"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Spraakkode


class InstitusjonellSektorkode(str):
    """ SSB sin institusjonelle sektorkode for ei verksemd. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "InstitusjonellSektorkode"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.InstitusjonellSektorkode


class Valutakode(str):
    """ ISO 4217-valutakode. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Valutakode"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Valutakode


class Landkode(str):
    """ Kode for land. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Landkode"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Landkode


class Postnummer(str):
    """ Norsk postnummer (4 sifer). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Postnummer"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Postnummer


class Organisasjonsform(str):
    """ Kode for organisasjonsform, jf. Einingsregisteret sitt kodeverk. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Organisasjonsform"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Organisasjonsform


class Kommunenummer(str):
    """ Norsk kommunenummer (4 sifer). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Kommunenummer"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Kommunenummer


class Virksomhetsstatus(str):
    """ Kode for status på ei verksemd (t.d. aktiv, konkurs, oppløyst). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Virksomhetsstatus"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Virksomhetsstatus


class Naeringskode(str):
    """ Kode frå SSB sin standard for næringsgruppering (SN2007). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Naeringskode"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Naeringskode


class PersonstatusType(str):
    """ Kode for status på ein person i BR sine register. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "PersonstatusType"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.PersonstatusType


class LandkodeIsoAlpha3(str):
    """ ISO 3166-1 alpha-3-landkode (t.d. NOR). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "LandkodeIsoAlpha3"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.LandkodeIsoAlpha3


class Epostadresse(str):
    """ Ei e-postadresse. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Epostadresse"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Epostadresse


class PrefiksMedNasjonalKode(str):
    """ Internasjonalt telefonprefiks (landkode), t.d. "+47". """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "PrefiksMedNasjonalKode"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.PrefiksMedNasjonalKode


class Husbokstav(str):
    """ Husbokstav i ei vegadresse. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Husbokstav"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Husbokstav


class Husnummer(str):
    """ Husnummer i ei vegadresse. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Husnummer"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Husnummer


class NasjonaltNummer(str):
    """ Telefonnummer utan landkode/prefiks. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "NasjonaltNummer"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.NasjonaltNummer


class Virksomhetsnavn(str):
    """ Namnet på ei verksemd, slik det er registrert i Einingsregisteret. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Virksomhetsnavn"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Virksomhetsnavn


class Organisasjonsnummer(str):
    """ Organisasjonsnummer for ei norsk verksemd (9 sifer), jf. Einingsregisteret. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Organisasjonsnummer"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Organisasjonsnummer


class BRPersonId(str):
    """ BR sin interne identifikator for ein person. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "BRPersonId"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.BRPersonId


class Kontonummer(str):
    """ Norsk bankkontonummer (11 sifer). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Kontonummer"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Kontonummer


class Aktivitetskode(str):
    """ Kode for ein aktivitetstype i BR sine register. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Aktivitetskode"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Aktivitetskode


class AktoerId(str):
    """ BR sin interne identifikator for ein aktør (person eller verksemd). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "AktoerId"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.AktoerId


class Foedselsnummer(str):
    """ Norsk fødselsnummer eller D-nummer (11 sifer). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Foedselsnummer"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Foedselsnummer


class Binaerobjekt(str):
    """ Eit vedlagt binærobjekt (t.d. eit dokument), base64-koda. """
    type_class_uri = XSD["base64Binary"]
    type_class_curie = "xsd:base64Binary"
    type_name = "Binaerobjekt"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Binaerobjekt


class URI(str):
    """ Ein Uniform Resource Identifier. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "URI"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.URI


class URL(str):
    """ Ein Uniform Resource Locator (nettadresse). """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "URL"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.URL


class UUID(str):
    """ Ein universelt unik identifikator (UUID/GUID). Strukturtypekatalog_v1 kallar den tilsvarande typen sin "GUID" — denne modellen brukar "UUID" konsekvent, jf. avklaring i specs/done/felles-typar-enhetsregisteret-fra-br-katalogar.md. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "UUID"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.UUID


class Beloep(str):
    """ Eit pengebeløp. """
    type_class_uri = XSD["decimal"]
    type_class_curie = "xsd:decimal"
    type_name = "Beloep"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Beloep


class MappeId(str):
    """ BR sin interne identifikator for ei saksmappe. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "MappeId"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.MappeId


class Tekst50(str):
    """ Fritekst avgrensa til 50 teikn. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Tekst50"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Tekst50


class Tekst255(str):
    """ Fritekst avgrensa til 255 teikn. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Tekst255"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Tekst255


class Tekst1000(str):
    """ Fritekst avgrensa til 1000 teikn. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Tekst1000"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Tekst1000


class Postboksnummer(str):
    """ Nummeret på ein postboks. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Postboksnummer"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Postboksnummer


class BRAdresseId(str):
    """ BR sin interne identifikator for ei adresse. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "BRAdresseId"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.BRAdresseId


class Tekst175(str):
    """ Fritekst avgrensa til 175 teikn. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Tekst175"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Tekst175


class Bruksenhetsnummer(str):
    """ Bruksenhetsnummer (bustadnummer) i ei vegadresse, t.d. "H0101". """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Bruksenhetsnummer"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Bruksenhetsnummer


class Tekst100(str):
    """ Fritekst avgrensa til 100 teikn. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Tekst100"
    type_model_uri = BRREG_FELLES_DIGITAL_ADRESSE.Tekst100


# Class references
class DigitalAdresseId(URIorCURIE):
    pass


class IPAdresseId(DigitalAdresseId):
    pass


class EPostadresseId(DigitalAdresseId):
    pass


class NettadresseId(DigitalAdresseId):
    pass


class MeldingsboksId(DigitalAdresseId):
    pass


class MobiltelefonnummerId(DigitalAdresseId):
    pass


class TelefonnummerId(DigitalAdresseId):
    pass


@dataclass(repr=False)
class DigitalAdresse(YAMLRoot):
    """
    Ei digital adresse. Abstrakt basisklasse for dei konkrete digitale adressetypane under.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE["DigitalAdresse"]
    class_class_curie: ClassVar[str] = "brreg_felles_digital_adresse:DigitalAdresse"
    class_name: ClassVar[str] = "DigitalAdresse"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE.DigitalAdresse

    id: Union[str, DigitalAdresseId] = None
    identifikator: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DigitalAdresseId):
            self.id = DigitalAdresseId(self.id)

        if self.identifikator is not None and not isinstance(self.identifikator, str):
            self.identifikator = str(self.identifikator)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IPAdresse(DigitalAdresse):
    """
    Ei IP-adresse.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE["IPAdresse"]
    class_class_curie: ClassVar[str] = "brreg_felles_digital_adresse:IPAdresse"
    class_name: ClassVar[str] = "IPAdresse"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE.IPAdresse

    id: Union[str, IPAdresseId] = None
    ip_nummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IPAdresseId):
            self.id = IPAdresseId(self.id)

        if self.ip_nummer is not None and not isinstance(self.ip_nummer, str):
            self.ip_nummer = str(self.ip_nummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EPostadresse(DigitalAdresse):
    """
    Ei e-postadresse, delt opp i brukarnamn og domenenavn.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE["EPostadresse"]
    class_class_curie: ClassVar[str] = "brreg_felles_digital_adresse:EPostadresse"
    class_name: ClassVar[str] = "EPostadresse"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE.EPostadresse

    id: Union[str, EPostadresseId] = None
    domenenavn: Optional[str] = None
    brukernavn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EPostadresseId):
            self.id = EPostadresseId(self.id)

        if self.domenenavn is not None and not isinstance(self.domenenavn, str):
            self.domenenavn = str(self.domenenavn)

        if self.brukernavn is not None and not isinstance(self.brukernavn, str):
            self.brukernavn = str(self.brukernavn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Nettadresse(DigitalAdresse):
    """
    Ei nettadresse (protokoll, domenenavn og filsti).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE["Nettadresse"]
    class_class_curie: ClassVar[str] = "brreg_felles_digital_adresse:Nettadresse"
    class_name: ClassVar[str] = "Nettadresse"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE.Nettadresse

    id: Union[str, NettadresseId] = None
    protokoll: Optional[str] = None
    domenenavn: Optional[str] = None
    filsti: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NettadresseId):
            self.id = NettadresseId(self.id)

        if self.protokoll is not None and not isinstance(self.protokoll, str):
            self.protokoll = str(self.protokoll)

        if self.domenenavn is not None and not isinstance(self.domenenavn, str):
            self.domenenavn = str(self.domenenavn)

        if self.filsti is not None and not isinstance(self.filsti, str):
            self.filsti = str(self.filsti)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Meldingsboks(DigitalAdresse):
    """
    Ei digital meldingsboks (t.d. Altinn).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE["Meldingsboks"]
    class_class_curie: ClassVar[str] = "brreg_felles_digital_adresse:Meldingsboks"
    class_name: ClassVar[str] = "Meldingsboks"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE.Meldingsboks

    id: Union[str, MeldingsboksId] = None
    meldingsbokstype: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MeldingsboksId):
            self.id = MeldingsboksId(self.id)

        if self.meldingsbokstype is not None and not isinstance(self.meldingsbokstype, str):
            self.meldingsbokstype = str(self.meldingsbokstype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Mobiltelefonnummer(DigitalAdresse):
    """
    Eit mobiltelefonnummer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE["Mobiltelefonnummer"]
    class_class_curie: ClassVar[str] = "brreg_felles_digital_adresse:Mobiltelefonnummer"
    class_name: ClassVar[str] = "Mobiltelefonnummer"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE.Mobiltelefonnummer

    id: Union[str, MobiltelefonnummerId] = None
    prefiks_med_nasjonal_kode: Optional[str] = None
    nasjonalt_nummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MobiltelefonnummerId):
            self.id = MobiltelefonnummerId(self.id)

        if self.prefiks_med_nasjonal_kode is not None and not isinstance(self.prefiks_med_nasjonal_kode, str):
            self.prefiks_med_nasjonal_kode = str(self.prefiks_med_nasjonal_kode)

        if self.nasjonalt_nummer is not None and not isinstance(self.nasjonalt_nummer, str):
            self.nasjonalt_nummer = str(self.nasjonalt_nummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Telefonnummer(DigitalAdresse):
    """
    Eit fasttelefonnummer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE["Telefonnummer"]
    class_class_curie: ClassVar[str] = "brreg_felles_digital_adresse:Telefonnummer"
    class_name: ClassVar[str] = "Telefonnummer"
    class_model_uri: ClassVar[URIRef] = BRREG_FELLES_DIGITAL_ADRESSE.Telefonnummer

    id: Union[str, TelefonnummerId] = None
    prefiks_med_nasjonal_kode: Optional[str] = None
    nasjonalt_nummer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TelefonnummerId):
            self.id = TelefonnummerId(self.id)

        if self.prefiks_med_nasjonal_kode is not None and not isinstance(self.prefiks_med_nasjonal_kode, str):
            self.prefiks_med_nasjonal_kode = str(self.prefiks_med_nasjonal_kode)

        if self.nasjonalt_nummer is not None and not isinstance(self.nasjonalt_nummer, str):
            self.nasjonalt_nummer = str(self.nasjonalt_nummer)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.digital_adresse_id = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.id, name="digital_adresse_id", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('id'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.digital_adresse_id, domain=None, range=URIRef)

slots.digital_adresse_type = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.type, name="digital_adresse_type", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('type'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.digital_adresse_type, domain=None, range=Optional[str])

slots.identifikator = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.identifikator, name="identifikator", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('identifikator'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.identifikator, domain=None, range=Optional[str])

slots.ip_nummer = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.ipNummer, name="ip_nummer", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('ipNummer'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.ip_nummer, domain=None, range=Optional[str])

slots.domenenavn = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.domenenavn, name="domenenavn", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('domenenavn'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.domenenavn, domain=None, range=Optional[str])

slots.brukernavn = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.brukernavn, name="brukernavn", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('brukernavn'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.brukernavn, domain=None, range=Optional[str])

slots.protokoll = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.protokoll, name="protokoll", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('protokoll'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.protokoll, domain=None, range=Optional[str])

slots.filsti = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.filsti, name="filsti", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('filsti'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.filsti, domain=None, range=Optional[str])

slots.meldingsbokstype = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.meldingsbokstype, name="meldingsbokstype", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('meldingsbokstype'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.meldingsbokstype, domain=None, range=Optional[str])

slots.prefiks_med_nasjonal_kode = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.prefiksMedNasjonalKode, name="prefiks_med_nasjonal_kode", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('prefiksMedNasjonalKode'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.prefiks_med_nasjonal_kode, domain=None, range=Optional[str])

slots.nasjonalt_nummer = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.nasjonaltNummer, name="nasjonalt_nummer", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('nasjonaltNummer'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.nasjonalt_nummer, domain=None, range=Optional[str])

slots.DigitalAdresse_identifikator = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.identifikator, name="DigitalAdresse_identifikator", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('identifikator'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.DigitalAdresse_identifikator, domain=DigitalAdresse, range=Optional[str])

slots.DigitalAdresse_digital_adresse_type = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.type, name="DigitalAdresse_digital_adresse_type", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('type'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.DigitalAdresse_digital_adresse_type, domain=DigitalAdresse, range=Optional[str])

slots.IPAdresse_ip_nummer = Slot(uri=BRREG_FELLES_DIGITAL_ADRESSE.ipNummer, name="IPAdresse_ip_nummer", curie=BRREG_FELLES_DIGITAL_ADRESSE.curie('ipNummer'),
                   model_uri=BRREG_FELLES_DIGITAL_ADRESSE.IPAdresse_ip_nummer, domain=IPAdresse, range=Optional[str])

