# Auto generated from ngr-virksomhet-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-18T09:10:48
# Schema: ngr-virksomhet
#
# id: https://data.norge.no/linkml/ngr-virksomhet
# description: Domenemodell for verksemdsdata basert på Nasjonale grunndata (utkast). Modellerer Virksomhet med Underenhet og Hovudeining, roller, adresser og klassifikasjonar frå Enhetsregisteret. Basert på https://informasjonsforvaltning.github.io/nasjonale-grunndata/
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

metamodel_version = "1.7.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NGRV = CurieNamespace('ngrv', 'https://data.norge.no/vocabulary/ngr-virksomhet#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://data.norge.no/linkml/ngr-virksomhet/')


# Types

# Class references
class VirksomhetId(URIorCURIE):
    pass


class UnderenhetId(VirksomhetId):
    pass


class HovedenhetId(VirksomhetId):
    pass


class TilstandId(URIorCURIE):
    pass


class OrganisasjonsformId(URIorCURIE):
    pass


class NaeringskodeId(URIorCURIE):
    pass


class SektorkodeId(URIorCURIE):
    pass


class KontaktinformasjonId(URIorCURIE):
    pass


class VarslingsadresseId(URIorCURIE):
    pass


class AktivitetId(URIorCURIE):
    pass


class RolleIVirksomhetId(URIorCURIE):
    pass


class RolleinnehaverId(URIorCURIE):
    pass


class SignaturrettId(URIorCURIE):
    pass


class ProkuraId(URIorCURIE):
    pass


class GeografiskAdresseId(URIorCURIE):
    pass


class PostadresseId(GeografiskAdresseId):
    pass


class ForretningsadresseId(GeografiskAdresseId):
    pass


class BeliggenhetsadresseId(GeografiskAdresseId):
    pass


class PersonId(URIorCURIE):
    pass


@dataclass(repr=False)
class VirksomhetContainer(YAMLRoot):
    """
    Rotklasse for NGR-virksomhet-datafiler. Held flate lister av alle instansierbare klassar; referansar mellom objekt
    brukar URI-lenking.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/VirksomhetContainer")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VirksomhetContainer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/VirksomhetContainer")

    underenheter: Optional[Union[dict[Union[str, UnderenhetId], Union[dict, "Underenhet"]], list[Union[dict, "Underenhet"]]]] = empty_dict()
    hovedenheter: Optional[Union[dict[Union[str, HovedenhetId], Union[dict, "Hovedenhet"]], list[Union[dict, "Hovedenhet"]]]] = empty_dict()
    tilstander: Optional[Union[dict[Union[str, TilstandId], Union[dict, "Tilstand"]], list[Union[dict, "Tilstand"]]]] = empty_dict()
    organisasjonsformer: Optional[Union[dict[Union[str, OrganisasjonsformId], Union[dict, "Organisasjonsform"]], list[Union[dict, "Organisasjonsform"]]]] = empty_dict()
    naeringskoder: Optional[Union[dict[Union[str, NaeringskodeId], Union[dict, "Naeringskode"]], list[Union[dict, "Naeringskode"]]]] = empty_dict()
    kontaktinformasjon: Optional[Union[dict[Union[str, KontaktinformasjonId], Union[dict, "Kontaktinformasjon"]], list[Union[dict, "Kontaktinformasjon"]]]] = empty_dict()
    varslingsadresser: Optional[Union[dict[Union[str, VarslingsadresseId], Union[dict, "Varslingsadresse"]], list[Union[dict, "Varslingsadresse"]]]] = empty_dict()
    aktivitetar: Optional[Union[dict[Union[str, AktivitetId], Union[dict, "Aktivitet"]], list[Union[dict, "Aktivitet"]]]] = empty_dict()
    sektorkoder: Optional[Union[dict[Union[str, SektorkodeId], Union[dict, "Sektorkode"]], list[Union[dict, "Sektorkode"]]]] = empty_dict()
    rollerIVirksomhet: Optional[Union[dict[Union[str, RolleIVirksomhetId], Union[dict, "RolleIVirksomhet"]], list[Union[dict, "RolleIVirksomhet"]]]] = empty_dict()
    rolleinnehavere: Optional[Union[dict[Union[str, RolleinnehaverId], Union[dict, "Rolleinnehaver"]], list[Union[dict, "Rolleinnehaver"]]]] = empty_dict()
    signaturrettar: Optional[Union[dict[Union[str, SignaturrettId], Union[dict, "Signaturrett"]], list[Union[dict, "Signaturrett"]]]] = empty_dict()
    prokuraer: Optional[Union[dict[Union[str, ProkuraId], Union[dict, "Prokura"]], list[Union[dict, "Prokura"]]]] = empty_dict()
    postadresser: Optional[Union[list[Union[str, PostadresseId]], dict[Union[str, PostadresseId], Union[dict, "Postadresse"]]]] = empty_dict()
    forretningsadresser: Optional[Union[list[Union[str, ForretningsadresseId]], dict[Union[str, ForretningsadresseId], Union[dict, "Forretningsadresse"]]]] = empty_dict()
    beliggenhetsadresser: Optional[Union[list[Union[str, BeliggenhetsadresseId]], dict[Union[str, BeliggenhetsadresseId], Union[dict, "Beliggenhetsadresse"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="underenheter", slot_type=Underenhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="hovedenheter", slot_type=Hovedenhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tilstander", slot_type=Tilstand, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="organisasjonsformer", slot_type=Organisasjonsform, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="naeringskoder", slot_type=Naeringskode, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kontaktinformasjon", slot_type=Kontaktinformasjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="varslingsadresser", slot_type=Varslingsadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aktivitetar", slot_type=Aktivitet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sektorkoder", slot_type=Sektorkode, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rollerIVirksomhet", slot_type=RolleIVirksomhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rolleinnehavere", slot_type=Rolleinnehaver, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="signaturrettar", slot_type=Signaturrett, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="prokuraer", slot_type=Prokura, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="postadresser", slot_type=Postadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="forretningsadresser", slot_type=Forretningsadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="beliggenhetsadresser", slot_type=Beliggenhetsadresse, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Virksomhet(YAMLRoot):
    """
    Abstrakt overklasse for alle einingar registrert i Enhetsregisteret. Ei verksemd er alltid anten ei underleining
    eller ei hovudeining.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Virksomhet"]
    class_class_curie: ClassVar[str] = "ngrv:Virksomhet"
    class_name: ClassVar[str] = "Virksomhet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Virksomhet")

    id: Union[str, VirksomhetId] = None
    organisasjonsnummer: str = None
    navn: str = None
    er_klassifisert_som_organisasjonsform: Union[str, OrganisasjonsformId] = None
    har_varslingsadresse: Union[str, VarslingsadresseId] = None
    er_klassifisert_i_naeringskode: Union[Union[str, NaeringskodeId], list[Union[str, NaeringskodeId]]] = None
    har_tilstand: Optional[Union[Union[str, TilstandId], list[Union[str, TilstandId]]]] = empty_list()
    mottar_post_paa: Optional[Union[str, PostadresseId]] = None
    har_kontaktinformasjon: Optional[Union[str, KontaktinformasjonId]] = None
    antall_ansatte: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VirksomhetId):
            self.id = VirksomhetId(self.id)

        if self._is_empty(self.organisasjonsnummer):
            self.MissingRequiredField("organisasjonsnummer")
        if not isinstance(self.organisasjonsnummer, str):
            self.organisasjonsnummer = str(self.organisasjonsnummer)

        if self._is_empty(self.navn):
            self.MissingRequiredField("navn")
        if not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self._is_empty(self.er_klassifisert_som_organisasjonsform):
            self.MissingRequiredField("er_klassifisert_som_organisasjonsform")
        if not isinstance(self.er_klassifisert_som_organisasjonsform, OrganisasjonsformId):
            self.er_klassifisert_som_organisasjonsform = OrganisasjonsformId(self.er_klassifisert_som_organisasjonsform)

        if self._is_empty(self.har_varslingsadresse):
            self.MissingRequiredField("har_varslingsadresse")
        if not isinstance(self.har_varslingsadresse, VarslingsadresseId):
            self.har_varslingsadresse = VarslingsadresseId(self.har_varslingsadresse)

        if self._is_empty(self.er_klassifisert_i_naeringskode):
            self.MissingRequiredField("er_klassifisert_i_naeringskode")
        if not isinstance(self.er_klassifisert_i_naeringskode, list):
            self.er_klassifisert_i_naeringskode = [self.er_klassifisert_i_naeringskode] if self.er_klassifisert_i_naeringskode is not None else []
        self.er_klassifisert_i_naeringskode = [v if isinstance(v, NaeringskodeId) else NaeringskodeId(v) for v in self.er_klassifisert_i_naeringskode]

        if not isinstance(self.har_tilstand, list):
            self.har_tilstand = [self.har_tilstand] if self.har_tilstand is not None else []
        self.har_tilstand = [v if isinstance(v, TilstandId) else TilstandId(v) for v in self.har_tilstand]

        if self.mottar_post_paa is not None and not isinstance(self.mottar_post_paa, PostadresseId):
            self.mottar_post_paa = PostadresseId(self.mottar_post_paa)

        if self.har_kontaktinformasjon is not None and not isinstance(self.har_kontaktinformasjon, KontaktinformasjonId):
            self.har_kontaktinformasjon = KontaktinformasjonId(self.har_kontaktinformasjon)

        if self.antall_ansatte is not None and not isinstance(self.antall_ansatte, int):
            self.antall_ansatte = int(self.antall_ansatte)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Underenhet(Virksomhet):
    """
    Ei underleining er ein geografisk lokasjon der aktiviteten til ei hovudeining vert utøvd. Knyt seg til ei
    hovudeining via organisasjonsnummeret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Underenhet"]
    class_class_curie: ClassVar[str] = "ngrv:Underenhet"
    class_name: ClassVar[str] = "Underenhet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Underenhet")

    id: Union[str, UnderenhetId] = None
    organisasjonsnummer: str = None
    navn: str = None
    er_klassifisert_som_organisasjonsform: Union[str, OrganisasjonsformId] = None
    har_varslingsadresse: Union[str, VarslingsadresseId] = None
    er_klassifisert_i_naeringskode: Union[Union[str, NaeringskodeId], list[Union[str, NaeringskodeId]]] = None
    oppstartsdato: Union[str, XSDDate] = None
    har_beliggenhetsadresse: Union[str, BeliggenhetsadresseId] = None
    eierskiftedatoer: Optional[Union[Union[str, XSDDate], list[Union[str, XSDDate]]]] = empty_list()
    nedleggelsesdato: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnderenhetId):
            self.id = UnderenhetId(self.id)

        if self._is_empty(self.oppstartsdato):
            self.MissingRequiredField("oppstartsdato")
        if not isinstance(self.oppstartsdato, XSDDate):
            self.oppstartsdato = XSDDate(self.oppstartsdato)

        if self._is_empty(self.har_beliggenhetsadresse):
            self.MissingRequiredField("har_beliggenhetsadresse")
        if not isinstance(self.har_beliggenhetsadresse, BeliggenhetsadresseId):
            self.har_beliggenhetsadresse = BeliggenhetsadresseId(self.har_beliggenhetsadresse)

        if not isinstance(self.eierskiftedatoer, list):
            self.eierskiftedatoer = [self.eierskiftedatoer] if self.eierskiftedatoer is not None else []
        self.eierskiftedatoer = [v if isinstance(v, XSDDate) else XSDDate(v) for v in self.eierskiftedatoer]

        if self.nedleggelsesdato is not None and not isinstance(self.nedleggelsesdato, XSDDate):
            self.nedleggelsesdato = XSDDate(self.nedleggelsesdato)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Hovedenhet(Virksomhet):
    """
    Ei hovudeining er den juridiske eininga registrert i Enhetsregisteret (t.d. AS, ENK, BA). Kan ha undereiningar og
    rolleinnehavarar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Hovedenhet"]
    class_class_curie: ClassVar[str] = "ngrv:Hovedenhet"
    class_name: ClassVar[str] = "Hovedenhet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Hovedenhet")

    id: Union[str, HovedenhetId] = None
    organisasjonsnummer: str = None
    navn: str = None
    er_klassifisert_som_organisasjonsform: Union[str, OrganisasjonsformId] = None
    har_varslingsadresse: Union[str, VarslingsadresseId] = None
    er_klassifisert_i_naeringskode: Union[Union[str, NaeringskodeId], list[Union[str, NaeringskodeId]]] = None
    utoevar_aktivitet: Union[str, AktivitetId] = None
    har_rolle_i_virksomhet: Union[Union[str, RolleIVirksomhetId], list[Union[str, RolleIVirksomhetId]]] = None
    er_klassifisert_i_sektorkode: Optional[Union[str, SektorkodeId]] = None
    har_bestemmelser_om_signaturrett: Optional[Union[str, SignaturrettId]] = None
    har_bestemmelser_om_prokura: Optional[Union[Union[str, ProkuraId], list[Union[str, ProkuraId]]]] = empty_list()
    stiftelsesdato: Optional[Union[str, XSDDate]] = None
    har_forretningsadresse: Optional[Union[str, ForretningsadresseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HovedenhetId):
            self.id = HovedenhetId(self.id)

        if self._is_empty(self.utoevar_aktivitet):
            self.MissingRequiredField("utoevar_aktivitet")
        if not isinstance(self.utoevar_aktivitet, AktivitetId):
            self.utoevar_aktivitet = AktivitetId(self.utoevar_aktivitet)

        if self._is_empty(self.har_rolle_i_virksomhet):
            self.MissingRequiredField("har_rolle_i_virksomhet")
        if not isinstance(self.har_rolle_i_virksomhet, list):
            self.har_rolle_i_virksomhet = [self.har_rolle_i_virksomhet] if self.har_rolle_i_virksomhet is not None else []
        self.har_rolle_i_virksomhet = [v if isinstance(v, RolleIVirksomhetId) else RolleIVirksomhetId(v) for v in self.har_rolle_i_virksomhet]

        if self.er_klassifisert_i_sektorkode is not None and not isinstance(self.er_klassifisert_i_sektorkode, SektorkodeId):
            self.er_klassifisert_i_sektorkode = SektorkodeId(self.er_klassifisert_i_sektorkode)

        if self.har_bestemmelser_om_signaturrett is not None and not isinstance(self.har_bestemmelser_om_signaturrett, SignaturrettId):
            self.har_bestemmelser_om_signaturrett = SignaturrettId(self.har_bestemmelser_om_signaturrett)

        if not isinstance(self.har_bestemmelser_om_prokura, list):
            self.har_bestemmelser_om_prokura = [self.har_bestemmelser_om_prokura] if self.har_bestemmelser_om_prokura is not None else []
        self.har_bestemmelser_om_prokura = [v if isinstance(v, ProkuraId) else ProkuraId(v) for v in self.har_bestemmelser_om_prokura]

        if self.stiftelsesdato is not None and not isinstance(self.stiftelsesdato, XSDDate):
            self.stiftelsesdato = XSDDate(self.stiftelsesdato)

        if self.har_forretningsadresse is not None and not isinstance(self.har_forretningsadresse, ForretningsadresseId):
            self.har_forretningsadresse = ForretningsadresseId(self.har_forretningsadresse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tilstand(YAMLRoot):
    """
    Registrert tilstand (status) for ei verksemd i Enhetsregisteret, med gyldigheitsperiode for historisk sporing.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Tilstand"]
    class_class_curie: ClassVar[str] = "ngrv:Tilstand"
    class_name: ClassVar[str] = "Tilstand"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Tilstand")

    id: Union[str, TilstandId] = None
    tilstandstype: Union[str, "TilstandType"] = None
    gyldig_fra: Union[str, XSDDate] = None
    gyldig_til: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TilstandId):
            self.id = TilstandId(self.id)

        if self._is_empty(self.tilstandstype):
            self.MissingRequiredField("tilstandstype")
        if not isinstance(self.tilstandstype, TilstandType):
            self.tilstandstype = TilstandType(self.tilstandstype)

        if self._is_empty(self.gyldig_fra):
            self.MissingRequiredField("gyldig_fra")
        if not isinstance(self.gyldig_fra, XSDDate):
            self.gyldig_fra = XSDDate(self.gyldig_fra)

        if self.gyldig_til is not None and not isinstance(self.gyldig_til, XSDDate):
            self.gyldig_til = XSDDate(self.gyldig_til)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organisasjonsform(YAMLRoot):
    """
    Klassifikasjon av juridisk organisasjonsform (t.d. AS, ENK, BA, NUF). Kodeverk forvalta av Enhetsregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Organisasjonsform"]
    class_class_curie: ClassVar[str] = "ngrv:Organisasjonsform"
    class_name: ClassVar[str] = "Organisasjonsform"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Organisasjonsform")

    id: Union[str, OrganisasjonsformId] = None
    organisasjonsform_kode: str = None
    organisasjonsform_beskrivelse: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganisasjonsformId):
            self.id = OrganisasjonsformId(self.id)

        if self._is_empty(self.organisasjonsform_kode):
            self.MissingRequiredField("organisasjonsform_kode")
        if not isinstance(self.organisasjonsform_kode, str):
            self.organisasjonsform_kode = str(self.organisasjonsform_kode)

        if self.organisasjonsform_beskrivelse is not None and not isinstance(self.organisasjonsform_beskrivelse, str):
            self.organisasjonsform_beskrivelse = str(self.organisasjonsform_beskrivelse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Naeringskode(YAMLRoot):
    """
    Næringskode basert på SSBs Standard for næringsgruppering (SN2007/NACE). Ei verksemd kan ha 1–3 næringskoder.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Naeringskode"]
    class_class_curie: ClassVar[str] = "ngrv:Naeringskode"
    class_name: ClassVar[str] = "Naeringskode"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Naeringskode")

    id: Union[str, NaeringskodeId] = None
    naeringskode_kode: str = None
    naeringskode_beskrivelse: Optional[str] = None
    er_hovednaeringskode: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NaeringskodeId):
            self.id = NaeringskodeId(self.id)

        if self._is_empty(self.naeringskode_kode):
            self.MissingRequiredField("naeringskode_kode")
        if not isinstance(self.naeringskode_kode, str):
            self.naeringskode_kode = str(self.naeringskode_kode)

        if self.naeringskode_beskrivelse is not None and not isinstance(self.naeringskode_beskrivelse, str):
            self.naeringskode_beskrivelse = str(self.naeringskode_beskrivelse)

        if self.er_hovednaeringskode is not None and not isinstance(self.er_hovednaeringskode, Bool):
            self.er_hovednaeringskode = Bool(self.er_hovednaeringskode)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sektorkode(YAMLRoot):
    """
    Institusjonell sektorkode som klassifiserer kva sektor verksemda tilhøyrer (t.d. offentleg, privat).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Sektorkode"]
    class_class_curie: ClassVar[str] = "ngrv:Sektorkode"
    class_name: ClassVar[str] = "Sektorkode"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Sektorkode")

    id: Union[str, SektorkodeId] = None
    sektorkode_kode: str = None
    sektorkode_beskrivelse: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SektorkodeId):
            self.id = SektorkodeId(self.id)

        if self._is_empty(self.sektorkode_kode):
            self.MissingRequiredField("sektorkode_kode")
        if not isinstance(self.sektorkode_kode, str):
            self.sektorkode_kode = str(self.sektorkode_kode)

        if self.sektorkode_beskrivelse is not None and not isinstance(self.sektorkode_beskrivelse, str):
            self.sektorkode_beskrivelse = str(self.sektorkode_beskrivelse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontaktinformasjon(YAMLRoot):
    """
    Kontaktinformasjon for verksemda registrert i Enhetsregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Kontaktinformasjon"]
    class_class_curie: ClassVar[str] = "ngrv:Kontaktinformasjon"
    class_name: ClassVar[str] = "Kontaktinformasjon"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Kontaktinformasjon")

    id: Union[str, KontaktinformasjonId] = None
    epostadresse: Optional[str] = None
    telefonnummer: Optional[str] = None
    mobiltelefonnummer: Optional[str] = None
    nettside: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KontaktinformasjonId):
            self.id = KontaktinformasjonId(self.id)

        if self.epostadresse is not None and not isinstance(self.epostadresse, str):
            self.epostadresse = str(self.epostadresse)

        if self.telefonnummer is not None and not isinstance(self.telefonnummer, str):
            self.telefonnummer = str(self.telefonnummer)

        if self.mobiltelefonnummer is not None and not isinstance(self.mobiltelefonnummer, str):
            self.mobiltelefonnummer = str(self.mobiltelefonnummer)

        if self.nettside is not None and not isinstance(self.nettside, str):
            self.nettside = str(self.nettside)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Varslingsadresse(YAMLRoot):
    """
    Offisiell varslingsadresse for verksemda – e-post eller mobilnummer som vert brukt for offisielle meldingar frå
    offentlege styresmakter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Varslingsadresse"]
    class_class_curie: ClassVar[str] = "ngrv:Varslingsadresse"
    class_name: ClassVar[str] = "Varslingsadresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Varslingsadresse")

    id: Union[str, VarslingsadresseId] = None
    varslingstype: Union[str, "VarslingType"] = None
    varslingsverdi: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VarslingsadresseId):
            self.id = VarslingsadresseId(self.id)

        if self._is_empty(self.varslingstype):
            self.MissingRequiredField("varslingstype")
        if not isinstance(self.varslingstype, VarslingType):
            self.varslingstype = VarslingType(self.varslingstype)

        if self._is_empty(self.varslingsverdi):
            self.MissingRequiredField("varslingsverdi")
        if not isinstance(self.varslingsverdi, str):
            self.varslingsverdi = str(self.varslingsverdi)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aktivitet(YAMLRoot):
    """
    Skildring av kva aktivitet ei hovudeining utøver. Svarer til formålsparagrafen eller føremålet til verksemda.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Aktivitet"]
    class_class_curie: ClassVar[str] = "ngrv:Aktivitet"
    class_name: ClassVar[str] = "Aktivitet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Aktivitet")

    id: Union[str, AktivitetId] = None
    aktivitet_beskrivelse: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AktivitetId):
            self.id = AktivitetId(self.id)

        if self._is_empty(self.aktivitet_beskrivelse):
            self.MissingRequiredField("aktivitet_beskrivelse")
        if not isinstance(self.aktivitet_beskrivelse, str):
            self.aktivitet_beskrivelse = str(self.aktivitet_beskrivelse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RolleIVirksomhet(YAMLRoot):
    """
    Ein definert rolle i ei hovudeining (t.d. dagleg leiar, styreleiar). Kvar rolle kan ha éin eller fleire
    rolleinnehavarar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["RolleIVirksomhet"]
    class_class_curie: ClassVar[str] = "ngrv:RolleIVirksomhet"
    class_name: ClassVar[str] = "RolleIVirksomhet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/RolleIVirksomhet")

    id: Union[str, RolleIVirksomhetId] = None
    rollebetegnelse: Union[str, "RolleType"] = None
    har_rolleinnehaver: Optional[Union[Union[str, RolleinnehaverId], list[Union[str, RolleinnehaverId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RolleIVirksomhetId):
            self.id = RolleIVirksomhetId(self.id)

        if self._is_empty(self.rollebetegnelse):
            self.MissingRequiredField("rollebetegnelse")
        if not isinstance(self.rollebetegnelse, RolleType):
            self.rollebetegnelse = RolleType(self.rollebetegnelse)

        if not isinstance(self.har_rolleinnehaver, list):
            self.har_rolleinnehaver = [self.har_rolleinnehaver] if self.har_rolleinnehaver is not None else []
        self.har_rolleinnehaver = [v if isinstance(v, RolleinnehaverId) else RolleinnehaverId(v) for v in self.har_rolleinnehaver]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rolleinnehaver(YAMLRoot):
    """
    Den som innehar ein rolle i ei verksemd. Kan vere ein fysisk person (frå Folkeregisteret) eller ei anna eining.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Rolleinnehaver"]
    class_class_curie: ClassVar[str] = "ngrv:Rolleinnehaver"
    class_name: ClassVar[str] = "Rolleinnehaver"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Rolleinnehaver")

    id: Union[str, RolleinnehaverId] = None
    kan_vaere_av_type_person: Optional[Union[str, PersonId]] = None
    rolleinnehaver_navn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RolleinnehaverId):
            self.id = RolleinnehaverId(self.id)

        if self.kan_vaere_av_type_person is not None and not isinstance(self.kan_vaere_av_type_person, PersonId):
            self.kan_vaere_av_type_person = PersonId(self.kan_vaere_av_type_person)

        if self.rolleinnehaver_navn is not None and not isinstance(self.rolleinnehaver_navn, str):
            self.rolleinnehaver_navn = str(self.rolleinnehaver_navn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Signaturrett(YAMLRoot):
    """
    Bestemmelse om kven som har rett til å signere på vegne av verksemda (t.d. "Styret i fellesskap" eller "Dagleg
    leiar aleine").
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Signaturrett"]
    class_class_curie: ClassVar[str] = "ngrv:Signaturrett"
    class_name: ClassVar[str] = "Signaturrett"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Signaturrett")

    id: Union[str, SignaturrettId] = None
    signaturrett_bestemmelse: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SignaturrettId):
            self.id = SignaturrettId(self.id)

        if self._is_empty(self.signaturrett_bestemmelse):
            self.MissingRequiredField("signaturrett_bestemmelse")
        if not isinstance(self.signaturrett_bestemmelse, str):
            self.signaturrett_bestemmelse = str(self.signaturrett_bestemmelse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Prokura(YAMLRoot):
    """
    Prokura gjev ein person fullmakt til å handle på vegne av verksemda i næringssaker. Verksemda kan ha fleire
    prokuraistar.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Prokura"]
    class_class_curie: ClassVar[str] = "ngrv:Prokura"
    class_name: ClassVar[str] = "Prokura"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Prokura")

    id: Union[str, ProkuraId] = None
    prokura_bestemmelse: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProkuraId):
            self.id = ProkuraId(self.id)

        if self._is_empty(self.prokura_bestemmelse):
            self.MissingRequiredField("prokura_bestemmelse")
        if not isinstance(self.prokura_bestemmelse, str):
            self.prokura_bestemmelse = str(self.prokura_bestemmelse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeografiskAdresse(YAMLRoot):
    """
    Abstrakt klasse for geografiske adresser. Tilhøyrer Domene adresse og forvaltast av Matrikkelen. Enhetsregisteret
    nyttar Kartverket som kjelde til vegadresse, og gjer jamnleg vask mot Posten sitt adresseregister.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["GeografiskAdresse"]
    class_class_curie: ClassVar[str] = "ngrv:GeografiskAdresse"
    class_name: ClassVar[str] = "GeografiskAdresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/GeografiskAdresse")

    id: Union[str, GeografiskAdresseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeografiskAdresseId):
            self.id = GeografiskAdresseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Postadresse(GeografiskAdresse):
    """
    Postadressa verksemda mottar post på.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Postadresse"]
    class_class_curie: ClassVar[str] = "ngrv:Postadresse"
    class_name: ClassVar[str] = "Postadresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Postadresse")

    id: Union[str, PostadresseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PostadresseId):
            self.id = PostadresseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Forretningsadresse(GeografiskAdresse):
    """
    Forretningsadressa til hovudeininga – adressa der hovudkontoret held til.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Forretningsadresse"]
    class_class_curie: ClassVar[str] = "ngrv:Forretningsadresse"
    class_name: ClassVar[str] = "Forretningsadresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Forretningsadresse")

    id: Union[str, ForretningsadresseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ForretningsadresseId):
            self.id = ForretningsadresseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Beliggenhetsadresse(GeografiskAdresse):
    """
    Beliggenheitsadressa til underleininga – den fysiske adressa der aktiviteten vert utøvd.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Beliggenhetsadresse"]
    class_class_curie: ClassVar[str] = "ngrv:Beliggenhetsadresse"
    class_name: ClassVar[str] = "Beliggenhetsadresse"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Beliggenhetsadresse")

    id: Union[str, BeliggenhetsadresseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeliggenhetsadresseId):
            self.id = BeliggenhetsadresseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    """
    Ein fysisk person. Tilhøyrer Domene person og forvaltast av Folkeregisteret. Enhetsregisteret nyttar kopi av data
    frå Folkeregisteret.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NGRV["Person"]
    class_class_curie: ClassVar[str] = "ngrv:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = URIRef("https://data.norge.no/linkml/ngr-virksomhet/Person")

    id: Union[str, PersonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class TilstandType(EnumDefinitionImpl):
    """
    Status for ei verksemd registrert i Enhetsregisteret.
    """
    AKTIV = PermissibleValue(
        text="AKTIV",
        description="Aktiv og registrert eining")
    UNDER_TVANGSAVVIKLING = PermissibleValue(
        text="UNDER_TVANGSAVVIKLING",
        description="Under tvangsavvikling")
    UNDER_KONKURS = PermissibleValue(
        text="UNDER_KONKURS",
        description="Under konkursbehandling")
    AVVIKLET = PermissibleValue(
        text="AVVIKLET",
        description="Avvikla")
    SLETTET = PermissibleValue(
        text="SLETTET",
        description="Sletta frå registeret")
    OPPLØST = PermissibleValue(
        text="OPPLØST",
        description="Oppløyst")

    _defn = EnumDefinition(
        name="TilstandType",
        description="Status for ei verksemd registrert i Enhetsregisteret.",
    )

class VarslingType(EnumDefinitionImpl):
    """
    Kanaltype for varsling til verksemda.
    """
    EPOST = PermissibleValue(
        text="EPOST",
        description="Varsling via e-post")
    MOBILTELEFON = PermissibleValue(
        text="MOBILTELEFON",
        description="Varsling via SMS til mobiltelefon")

    _defn = EnumDefinition(
        name="VarslingType",
        description="Kanaltype for varsling til verksemda.",
    )

class RolleType(EnumDefinitionImpl):
    """
    Type rolle ein person eller eining kan ha i ei verksemd.
    """
    DAGLIG_LEDER = PermissibleValue(
        text="DAGLIG_LEDER",
        description="Dagleg leiar")
    STYRELEDER = PermissibleValue(
        text="STYRELEDER",
        description="Styreleiar")
    STYREMEDLEM = PermissibleValue(
        text="STYREMEDLEM",
        description="Styremedlem")
    VARAMEDLEM = PermissibleValue(
        text="VARAMEDLEM",
        description="Varamedlem til styret")
    KONTAKTPERSON = PermissibleValue(
        text="KONTAKTPERSON",
        description="Kontaktperson")
    KOMPLEMENTAR = PermissibleValue(
        text="KOMPLEMENTAR",
        description="Komplementar (i kommandittselskap)")
    DELTAKER = PermissibleValue(
        text="DELTAKER",
        description="Deltakar (i ansvarleg selskap)")
    BESTYRENDE_REDAKTOR = PermissibleValue(
        text="BESTYRENDE_REDAKTOR",
        description="Bestyrande redaktør")
    FORRETNINGSFORER = PermissibleValue(
        text="FORRETNINGSFORER",
        description="Forretningsførar")
    REVISOR = PermissibleValue(
        text="REVISOR",
        description="Revisor")
    REGNSKAPSFORER = PermissibleValue(
        text="REGNSKAPSFORER",
        description="Rekneskapsførar")
    NORSK_REPRESENTANT = PermissibleValue(
        text="NORSK_REPRESENTANT",
        description="Norsk representant for utanlandsk eining")

    _defn = EnumDefinition(
        name="RolleType",
        description="Type rolle ein person eller eining kan ha i ei verksemd.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.organisasjonsnummer = Slot(uri=NGRV.organisasjonsnummer, name="organisasjonsnummer", curie=NGRV.curie('organisasjonsnummer'),
                   model_uri=DEFAULT_.organisasjonsnummer, domain=None, range=Optional[str])

slots.navn = Slot(uri=NGRV.navn, name="navn", curie=NGRV.curie('navn'),
                   model_uri=DEFAULT_.navn, domain=None, range=Optional[str])

slots.antall_ansatte = Slot(uri=NGRV.antallAnsatte, name="antall_ansatte", curie=NGRV.curie('antallAnsatte'),
                   model_uri=DEFAULT_.antall_ansatte, domain=None, range=Optional[int])

slots.har_tilstand = Slot(uri=NGRV.harTilstand, name="har_tilstand", curie=NGRV.curie('harTilstand'),
                   model_uri=DEFAULT_.har_tilstand, domain=None, range=Optional[Union[Union[str, TilstandId], list[Union[str, TilstandId]]]])

slots.mottar_post_paa = Slot(uri=NGRV.mottarPostPaa, name="mottar_post_paa", curie=NGRV.curie('mottarPostPaa'),
                   model_uri=DEFAULT_.mottar_post_paa, domain=None, range=Optional[Union[str, PostadresseId]])

slots.er_klassifisert_som_organisasjonsform = Slot(uri=NGRV.erKlassifisertSomOrganisasjonsform, name="er_klassifisert_som_organisasjonsform", curie=NGRV.curie('erKlassifisertSomOrganisasjonsform'),
                   model_uri=DEFAULT_.er_klassifisert_som_organisasjonsform, domain=None, range=Optional[Union[str, OrganisasjonsformId]])

slots.har_kontaktinformasjon = Slot(uri=NGRV.harKontaktinformasjon, name="har_kontaktinformasjon", curie=NGRV.curie('harKontaktinformasjon'),
                   model_uri=DEFAULT_.har_kontaktinformasjon, domain=None, range=Optional[Union[str, KontaktinformasjonId]])

slots.har_varslingsadresse = Slot(uri=NGRV.harVarslingsadresse, name="har_varslingsadresse", curie=NGRV.curie('harVarslingsadresse'),
                   model_uri=DEFAULT_.har_varslingsadresse, domain=None, range=Optional[Union[str, VarslingsadresseId]])

slots.er_klassifisert_i_naeringskode = Slot(uri=NGRV.erKlassifisertINaeringskode, name="er_klassifisert_i_naeringskode", curie=NGRV.curie('erKlassifisertINaeringskode'),
                   model_uri=DEFAULT_.er_klassifisert_i_naeringskode, domain=None, range=Optional[Union[Union[str, NaeringskodeId], list[Union[str, NaeringskodeId]]]])

slots.oppstartsdato = Slot(uri=NGRV.oppstartsdato, name="oppstartsdato", curie=NGRV.curie('oppstartsdato'),
                   model_uri=DEFAULT_.oppstartsdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.eierskiftedatoer = Slot(uri=NGRV.eierskiftedato, name="eierskiftedatoer", curie=NGRV.curie('eierskiftedato'),
                   model_uri=DEFAULT_.eierskiftedatoer, domain=None, range=Optional[Union[Union[str, XSDDate], list[Union[str, XSDDate]]]])

slots.nedleggelsesdato = Slot(uri=NGRV.nedleggelsesdato, name="nedleggelsesdato", curie=NGRV.curie('nedleggelsesdato'),
                   model_uri=DEFAULT_.nedleggelsesdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.har_beliggenhetsadresse = Slot(uri=NGRV.harBeliggenhetsadresse, name="har_beliggenhetsadresse", curie=NGRV.curie('harBeliggenhetsadresse'),
                   model_uri=DEFAULT_.har_beliggenhetsadresse, domain=None, range=Optional[Union[str, BeliggenhetsadresseId]])

slots.utoevar_aktivitet = Slot(uri=NGRV.utoevarAktivitet, name="utoevar_aktivitet", curie=NGRV.curie('utoevarAktivitet'),
                   model_uri=DEFAULT_.utoevar_aktivitet, domain=None, range=Optional[Union[str, AktivitetId]])

slots.er_klassifisert_i_sektorkode = Slot(uri=NGRV.erKlassifisertISektorkode, name="er_klassifisert_i_sektorkode", curie=NGRV.curie('erKlassifisertISektorkode'),
                   model_uri=DEFAULT_.er_klassifisert_i_sektorkode, domain=None, range=Optional[Union[str, SektorkodeId]])

slots.har_rolle_i_virksomhet = Slot(uri=NGRV.harRolleIVirksomhet, name="har_rolle_i_virksomhet", curie=NGRV.curie('harRolleIVirksomhet'),
                   model_uri=DEFAULT_.har_rolle_i_virksomhet, domain=None, range=Optional[Union[Union[str, RolleIVirksomhetId], list[Union[str, RolleIVirksomhetId]]]])

slots.har_bestemmelser_om_signaturrett = Slot(uri=NGRV.harBestemmelserOmSignaturrett, name="har_bestemmelser_om_signaturrett", curie=NGRV.curie('harBestemmelserOmSignaturrett'),
                   model_uri=DEFAULT_.har_bestemmelser_om_signaturrett, domain=None, range=Optional[Union[str, SignaturrettId]])

slots.har_bestemmelser_om_prokura = Slot(uri=NGRV.harBestemmelserOmProkura, name="har_bestemmelser_om_prokura", curie=NGRV.curie('harBestemmelserOmProkura'),
                   model_uri=DEFAULT_.har_bestemmelser_om_prokura, domain=None, range=Optional[Union[Union[str, ProkuraId], list[Union[str, ProkuraId]]]])

slots.stiftelsesdato = Slot(uri=NGRV.stiftelsesdato, name="stiftelsesdato", curie=NGRV.curie('stiftelsesdato'),
                   model_uri=DEFAULT_.stiftelsesdato, domain=None, range=Optional[Union[str, XSDDate]])

slots.har_forretningsadresse = Slot(uri=NGRV.harForretningsadresse, name="har_forretningsadresse", curie=NGRV.curie('harForretningsadresse'),
                   model_uri=DEFAULT_.har_forretningsadresse, domain=None, range=Optional[Union[str, ForretningsadresseId]])

slots.rollebetegnelse = Slot(uri=NGRV.rollebetegnelse, name="rollebetegnelse", curie=NGRV.curie('rollebetegnelse'),
                   model_uri=DEFAULT_.rollebetegnelse, domain=None, range=Optional[Union[str, "RolleType"]])

slots.har_rolleinnehaver = Slot(uri=NGRV.harRolleinnehaver, name="har_rolleinnehaver", curie=NGRV.curie('harRolleinnehaver'),
                   model_uri=DEFAULT_.har_rolleinnehaver, domain=None, range=Optional[Union[Union[str, RolleinnehaverId], list[Union[str, RolleinnehaverId]]]])

slots.kan_vaere_av_type_person = Slot(uri=NGRV.kanVaereAvTypePerson, name="kan_vaere_av_type_person", curie=NGRV.curie('kanVaereAvTypePerson'),
                   model_uri=DEFAULT_.kan_vaere_av_type_person, domain=None, range=Optional[Union[str, PersonId]])

slots.rolleinnehaver_navn = Slot(uri=NGRV.rolleinnehaverNavn, name="rolleinnehaver_navn", curie=NGRV.curie('rolleinnehaverNavn'),
                   model_uri=DEFAULT_.rolleinnehaver_navn, domain=None, range=Optional[str])

slots.tilstandstype = Slot(uri=NGRV.tilstandstype, name="tilstandstype", curie=NGRV.curie('tilstandstype'),
                   model_uri=DEFAULT_.tilstandstype, domain=None, range=Optional[Union[str, "TilstandType"]])

slots.gyldig_fra = Slot(uri=NGRV.gyldigFra, name="gyldig_fra", curie=NGRV.curie('gyldigFra'),
                   model_uri=DEFAULT_.gyldig_fra, domain=None, range=Optional[Union[str, XSDDate]])

slots.gyldig_til = Slot(uri=NGRV.gyldigTil, name="gyldig_til", curie=NGRV.curie('gyldigTil'),
                   model_uri=DEFAULT_.gyldig_til, domain=None, range=Optional[Union[str, XSDDate]])

slots.organisasjonsform_kode = Slot(uri=NGRV.organisasjonsformKode, name="organisasjonsform_kode", curie=NGRV.curie('organisasjonsformKode'),
                   model_uri=DEFAULT_.organisasjonsform_kode, domain=None, range=Optional[str])

slots.organisasjonsform_beskrivelse = Slot(uri=NGRV.organisasjonsformBeskrivelse, name="organisasjonsform_beskrivelse", curie=NGRV.curie('organisasjonsformBeskrivelse'),
                   model_uri=DEFAULT_.organisasjonsform_beskrivelse, domain=None, range=Optional[str])

slots.naeringskode_kode = Slot(uri=NGRV.naeringskodeKode, name="naeringskode_kode", curie=NGRV.curie('naeringskodeKode'),
                   model_uri=DEFAULT_.naeringskode_kode, domain=None, range=Optional[str])

slots.naeringskode_beskrivelse = Slot(uri=NGRV.naeringskodeBeskrivelse, name="naeringskode_beskrivelse", curie=NGRV.curie('naeringskodeBeskrivelse'),
                   model_uri=DEFAULT_.naeringskode_beskrivelse, domain=None, range=Optional[str])

slots.er_hovednaeringskode = Slot(uri=NGRV.erHovednaeringskode, name="er_hovednaeringskode", curie=NGRV.curie('erHovednaeringskode'),
                   model_uri=DEFAULT_.er_hovednaeringskode, domain=None, range=Optional[Union[bool, Bool]])

slots.sektorkode_kode = Slot(uri=NGRV.sektorkodeKode, name="sektorkode_kode", curie=NGRV.curie('sektorkodeKode'),
                   model_uri=DEFAULT_.sektorkode_kode, domain=None, range=Optional[str])

slots.sektorkode_beskrivelse = Slot(uri=NGRV.sektorkodeBeskrivelse, name="sektorkode_beskrivelse", curie=NGRV.curie('sektorkodeBeskrivelse'),
                   model_uri=DEFAULT_.sektorkode_beskrivelse, domain=None, range=Optional[str])

slots.epostadresse = Slot(uri=NGRV.epostadresse, name="epostadresse", curie=NGRV.curie('epostadresse'),
                   model_uri=DEFAULT_.epostadresse, domain=None, range=Optional[str])

slots.telefonnummer = Slot(uri=NGRV.telefonnummer, name="telefonnummer", curie=NGRV.curie('telefonnummer'),
                   model_uri=DEFAULT_.telefonnummer, domain=None, range=Optional[str])

slots.mobiltelefonnummer = Slot(uri=NGRV.mobiltelefonnummer, name="mobiltelefonnummer", curie=NGRV.curie('mobiltelefonnummer'),
                   model_uri=DEFAULT_.mobiltelefonnummer, domain=None, range=Optional[str])

slots.nettside = Slot(uri=NGRV.nettside, name="nettside", curie=NGRV.curie('nettside'),
                   model_uri=DEFAULT_.nettside, domain=None, range=Optional[str])

slots.varslingstype = Slot(uri=NGRV.varslingstype, name="varslingstype", curie=NGRV.curie('varslingstype'),
                   model_uri=DEFAULT_.varslingstype, domain=None, range=Optional[Union[str, "VarslingType"]])

slots.varslingsverdi = Slot(uri=NGRV.varslingsverdi, name="varslingsverdi", curie=NGRV.curie('varslingsverdi'),
                   model_uri=DEFAULT_.varslingsverdi, domain=None, range=Optional[str])

slots.aktivitet_beskrivelse = Slot(uri=NGRV.aktivitetBeskrivelse, name="aktivitet_beskrivelse", curie=NGRV.curie('aktivitetBeskrivelse'),
                   model_uri=DEFAULT_.aktivitet_beskrivelse, domain=None, range=Optional[str])

slots.signaturrett_bestemmelse = Slot(uri=NGRV.signaturrettBestemmelse, name="signaturrett_bestemmelse", curie=NGRV.curie('signaturrettBestemmelse'),
                   model_uri=DEFAULT_.signaturrett_bestemmelse, domain=None, range=Optional[str])

slots.prokura_bestemmelse = Slot(uri=NGRV.prokurabEstemmelse, name="prokura_bestemmelse", curie=NGRV.curie('prokurabEstemmelse'),
                   model_uri=DEFAULT_.prokura_bestemmelse, domain=None, range=Optional[str])

slots.virksomhetContainer__underenheter = Slot(uri=DEFAULT_.underenheter, name="virksomhetContainer__underenheter", curie=DEFAULT_.curie('underenheter'),
                   model_uri=DEFAULT_.virksomhetContainer__underenheter, domain=None, range=Optional[Union[dict[Union[str, UnderenhetId], Union[dict, Underenhet]], list[Union[dict, Underenhet]]]])

slots.virksomhetContainer__hovedenheter = Slot(uri=DEFAULT_.hovedenheter, name="virksomhetContainer__hovedenheter", curie=DEFAULT_.curie('hovedenheter'),
                   model_uri=DEFAULT_.virksomhetContainer__hovedenheter, domain=None, range=Optional[Union[dict[Union[str, HovedenhetId], Union[dict, Hovedenhet]], list[Union[dict, Hovedenhet]]]])

slots.virksomhetContainer__tilstander = Slot(uri=DEFAULT_.tilstander, name="virksomhetContainer__tilstander", curie=DEFAULT_.curie('tilstander'),
                   model_uri=DEFAULT_.virksomhetContainer__tilstander, domain=None, range=Optional[Union[dict[Union[str, TilstandId], Union[dict, Tilstand]], list[Union[dict, Tilstand]]]])

slots.virksomhetContainer__organisasjonsformer = Slot(uri=DEFAULT_.organisasjonsformer, name="virksomhetContainer__organisasjonsformer", curie=DEFAULT_.curie('organisasjonsformer'),
                   model_uri=DEFAULT_.virksomhetContainer__organisasjonsformer, domain=None, range=Optional[Union[dict[Union[str, OrganisasjonsformId], Union[dict, Organisasjonsform]], list[Union[dict, Organisasjonsform]]]])

slots.virksomhetContainer__naeringskoder = Slot(uri=DEFAULT_.naeringskoder, name="virksomhetContainer__naeringskoder", curie=DEFAULT_.curie('naeringskoder'),
                   model_uri=DEFAULT_.virksomhetContainer__naeringskoder, domain=None, range=Optional[Union[dict[Union[str, NaeringskodeId], Union[dict, Naeringskode]], list[Union[dict, Naeringskode]]]])

slots.virksomhetContainer__kontaktinformasjon = Slot(uri=DEFAULT_.kontaktinformasjon, name="virksomhetContainer__kontaktinformasjon", curie=DEFAULT_.curie('kontaktinformasjon'),
                   model_uri=DEFAULT_.virksomhetContainer__kontaktinformasjon, domain=None, range=Optional[Union[dict[Union[str, KontaktinformasjonId], Union[dict, Kontaktinformasjon]], list[Union[dict, Kontaktinformasjon]]]])

slots.virksomhetContainer__varslingsadresser = Slot(uri=DEFAULT_.varslingsadresser, name="virksomhetContainer__varslingsadresser", curie=DEFAULT_.curie('varslingsadresser'),
                   model_uri=DEFAULT_.virksomhetContainer__varslingsadresser, domain=None, range=Optional[Union[dict[Union[str, VarslingsadresseId], Union[dict, Varslingsadresse]], list[Union[dict, Varslingsadresse]]]])

slots.virksomhetContainer__aktivitetar = Slot(uri=DEFAULT_.aktivitetar, name="virksomhetContainer__aktivitetar", curie=DEFAULT_.curie('aktivitetar'),
                   model_uri=DEFAULT_.virksomhetContainer__aktivitetar, domain=None, range=Optional[Union[dict[Union[str, AktivitetId], Union[dict, Aktivitet]], list[Union[dict, Aktivitet]]]])

slots.virksomhetContainer__sektorkoder = Slot(uri=DEFAULT_.sektorkoder, name="virksomhetContainer__sektorkoder", curie=DEFAULT_.curie('sektorkoder'),
                   model_uri=DEFAULT_.virksomhetContainer__sektorkoder, domain=None, range=Optional[Union[dict[Union[str, SektorkodeId], Union[dict, Sektorkode]], list[Union[dict, Sektorkode]]]])

slots.virksomhetContainer__rollerIVirksomhet = Slot(uri=DEFAULT_.rollerIVirksomhet, name="virksomhetContainer__rollerIVirksomhet", curie=DEFAULT_.curie('rollerIVirksomhet'),
                   model_uri=DEFAULT_.virksomhetContainer__rollerIVirksomhet, domain=None, range=Optional[Union[dict[Union[str, RolleIVirksomhetId], Union[dict, RolleIVirksomhet]], list[Union[dict, RolleIVirksomhet]]]])

slots.virksomhetContainer__rolleinnehavere = Slot(uri=DEFAULT_.rolleinnehavere, name="virksomhetContainer__rolleinnehavere", curie=DEFAULT_.curie('rolleinnehavere'),
                   model_uri=DEFAULT_.virksomhetContainer__rolleinnehavere, domain=None, range=Optional[Union[dict[Union[str, RolleinnehaverId], Union[dict, Rolleinnehaver]], list[Union[dict, Rolleinnehaver]]]])

slots.virksomhetContainer__signaturrettar = Slot(uri=DEFAULT_.signaturrettar, name="virksomhetContainer__signaturrettar", curie=DEFAULT_.curie('signaturrettar'),
                   model_uri=DEFAULT_.virksomhetContainer__signaturrettar, domain=None, range=Optional[Union[dict[Union[str, SignaturrettId], Union[dict, Signaturrett]], list[Union[dict, Signaturrett]]]])

slots.virksomhetContainer__prokuraer = Slot(uri=DEFAULT_.prokuraer, name="virksomhetContainer__prokuraer", curie=DEFAULT_.curie('prokuraer'),
                   model_uri=DEFAULT_.virksomhetContainer__prokuraer, domain=None, range=Optional[Union[dict[Union[str, ProkuraId], Union[dict, Prokura]], list[Union[dict, Prokura]]]])

slots.virksomhetContainer__postadresser = Slot(uri=DEFAULT_.postadresser, name="virksomhetContainer__postadresser", curie=DEFAULT_.curie('postadresser'),
                   model_uri=DEFAULT_.virksomhetContainer__postadresser, domain=None, range=Optional[Union[list[Union[str, PostadresseId]], dict[Union[str, PostadresseId], Union[dict, Postadresse]]]])

slots.virksomhetContainer__forretningsadresser = Slot(uri=DEFAULT_.forretningsadresser, name="virksomhetContainer__forretningsadresser", curie=DEFAULT_.curie('forretningsadresser'),
                   model_uri=DEFAULT_.virksomhetContainer__forretningsadresser, domain=None, range=Optional[Union[list[Union[str, ForretningsadresseId]], dict[Union[str, ForretningsadresseId], Union[dict, Forretningsadresse]]]])

slots.virksomhetContainer__beliggenhetsadresser = Slot(uri=DEFAULT_.beliggenhetsadresser, name="virksomhetContainer__beliggenhetsadresser", curie=DEFAULT_.curie('beliggenhetsadresser'),
                   model_uri=DEFAULT_.virksomhetContainer__beliggenhetsadresser, domain=None, range=Optional[Union[list[Union[str, BeliggenhetsadresseId]], dict[Union[str, BeliggenhetsadresseId], Union[dict, Beliggenhetsadresse]]]])

slots.Virksomhet_organisasjonsnummer = Slot(uri=NGRV.organisasjonsnummer, name="Virksomhet_organisasjonsnummer", curie=NGRV.curie('organisasjonsnummer'),
                   model_uri=DEFAULT_.Virksomhet_organisasjonsnummer, domain=Virksomhet, range=str)

slots.Virksomhet_navn = Slot(uri=NGRV.navn, name="Virksomhet_navn", curie=NGRV.curie('navn'),
                   model_uri=DEFAULT_.Virksomhet_navn, domain=Virksomhet, range=str)

slots.Virksomhet_er_klassifisert_som_organisasjonsform = Slot(uri=NGRV.erKlassifisertSomOrganisasjonsform, name="Virksomhet_er_klassifisert_som_organisasjonsform", curie=NGRV.curie('erKlassifisertSomOrganisasjonsform'),
                   model_uri=DEFAULT_.Virksomhet_er_klassifisert_som_organisasjonsform, domain=Virksomhet, range=Union[str, OrganisasjonsformId])

slots.Virksomhet_har_varslingsadresse = Slot(uri=NGRV.harVarslingsadresse, name="Virksomhet_har_varslingsadresse", curie=NGRV.curie('harVarslingsadresse'),
                   model_uri=DEFAULT_.Virksomhet_har_varslingsadresse, domain=Virksomhet, range=Union[str, VarslingsadresseId])

slots.Virksomhet_er_klassifisert_i_naeringskode = Slot(uri=NGRV.erKlassifisertINaeringskode, name="Virksomhet_er_klassifisert_i_naeringskode", curie=NGRV.curie('erKlassifisertINaeringskode'),
                   model_uri=DEFAULT_.Virksomhet_er_klassifisert_i_naeringskode, domain=Virksomhet, range=Union[Union[str, NaeringskodeId], list[Union[str, NaeringskodeId]]])

slots.Virksomhet_har_tilstand = Slot(uri=NGRV.harTilstand, name="Virksomhet_har_tilstand", curie=NGRV.curie('harTilstand'),
                   model_uri=DEFAULT_.Virksomhet_har_tilstand, domain=Virksomhet, range=Optional[Union[Union[str, TilstandId], list[Union[str, TilstandId]]]])

slots.Virksomhet_mottar_post_paa = Slot(uri=NGRV.mottarPostPaa, name="Virksomhet_mottar_post_paa", curie=NGRV.curie('mottarPostPaa'),
                   model_uri=DEFAULT_.Virksomhet_mottar_post_paa, domain=Virksomhet, range=Optional[Union[str, PostadresseId]])

slots.Virksomhet_har_kontaktinformasjon = Slot(uri=NGRV.harKontaktinformasjon, name="Virksomhet_har_kontaktinformasjon", curie=NGRV.curie('harKontaktinformasjon'),
                   model_uri=DEFAULT_.Virksomhet_har_kontaktinformasjon, domain=Virksomhet, range=Optional[Union[str, KontaktinformasjonId]])

slots.Virksomhet_antall_ansatte = Slot(uri=NGRV.antallAnsatte, name="Virksomhet_antall_ansatte", curie=NGRV.curie('antallAnsatte'),
                   model_uri=DEFAULT_.Virksomhet_antall_ansatte, domain=Virksomhet, range=Optional[int])

slots.Underenhet_oppstartsdato = Slot(uri=NGRV.oppstartsdato, name="Underenhet_oppstartsdato", curie=NGRV.curie('oppstartsdato'),
                   model_uri=DEFAULT_.Underenhet_oppstartsdato, domain=Underenhet, range=Union[str, XSDDate])

slots.Underenhet_har_beliggenhetsadresse = Slot(uri=NGRV.harBeliggenhetsadresse, name="Underenhet_har_beliggenhetsadresse", curie=NGRV.curie('harBeliggenhetsadresse'),
                   model_uri=DEFAULT_.Underenhet_har_beliggenhetsadresse, domain=Underenhet, range=Union[str, BeliggenhetsadresseId])

slots.Underenhet_eierskiftedatoer = Slot(uri=NGRV.eierskiftedato, name="Underenhet_eierskiftedatoer", curie=NGRV.curie('eierskiftedato'),
                   model_uri=DEFAULT_.Underenhet_eierskiftedatoer, domain=Underenhet, range=Optional[Union[Union[str, XSDDate], list[Union[str, XSDDate]]]])

slots.Underenhet_nedleggelsesdato = Slot(uri=NGRV.nedleggelsesdato, name="Underenhet_nedleggelsesdato", curie=NGRV.curie('nedleggelsesdato'),
                   model_uri=DEFAULT_.Underenhet_nedleggelsesdato, domain=Underenhet, range=Optional[Union[str, XSDDate]])

slots.Hovedenhet_utoevar_aktivitet = Slot(uri=NGRV.utoevarAktivitet, name="Hovedenhet_utoevar_aktivitet", curie=NGRV.curie('utoevarAktivitet'),
                   model_uri=DEFAULT_.Hovedenhet_utoevar_aktivitet, domain=Hovedenhet, range=Union[str, AktivitetId])

slots.Hovedenhet_har_rolle_i_virksomhet = Slot(uri=NGRV.harRolleIVirksomhet, name="Hovedenhet_har_rolle_i_virksomhet", curie=NGRV.curie('harRolleIVirksomhet'),
                   model_uri=DEFAULT_.Hovedenhet_har_rolle_i_virksomhet, domain=Hovedenhet, range=Union[Union[str, RolleIVirksomhetId], list[Union[str, RolleIVirksomhetId]]])

slots.Hovedenhet_er_klassifisert_i_sektorkode = Slot(uri=NGRV.erKlassifisertISektorkode, name="Hovedenhet_er_klassifisert_i_sektorkode", curie=NGRV.curie('erKlassifisertISektorkode'),
                   model_uri=DEFAULT_.Hovedenhet_er_klassifisert_i_sektorkode, domain=Hovedenhet, range=Optional[Union[str, SektorkodeId]])

slots.Hovedenhet_stiftelsesdato = Slot(uri=NGRV.stiftelsesdato, name="Hovedenhet_stiftelsesdato", curie=NGRV.curie('stiftelsesdato'),
                   model_uri=DEFAULT_.Hovedenhet_stiftelsesdato, domain=Hovedenhet, range=Optional[Union[str, XSDDate]])

slots.Hovedenhet_har_bestemmelser_om_signaturrett = Slot(uri=NGRV.harBestemmelserOmSignaturrett, name="Hovedenhet_har_bestemmelser_om_signaturrett", curie=NGRV.curie('harBestemmelserOmSignaturrett'),
                   model_uri=DEFAULT_.Hovedenhet_har_bestemmelser_om_signaturrett, domain=Hovedenhet, range=Optional[Union[str, SignaturrettId]])

slots.Hovedenhet_har_bestemmelser_om_prokura = Slot(uri=NGRV.harBestemmelserOmProkura, name="Hovedenhet_har_bestemmelser_om_prokura", curie=NGRV.curie('harBestemmelserOmProkura'),
                   model_uri=DEFAULT_.Hovedenhet_har_bestemmelser_om_prokura, domain=Hovedenhet, range=Optional[Union[Union[str, ProkuraId], list[Union[str, ProkuraId]]]])

slots.Hovedenhet_har_forretningsadresse = Slot(uri=NGRV.harForretningsadresse, name="Hovedenhet_har_forretningsadresse", curie=NGRV.curie('harForretningsadresse'),
                   model_uri=DEFAULT_.Hovedenhet_har_forretningsadresse, domain=Hovedenhet, range=Optional[Union[str, ForretningsadresseId]])

slots.Tilstand_tilstandstype = Slot(uri=NGRV.tilstandstype, name="Tilstand_tilstandstype", curie=NGRV.curie('tilstandstype'),
                   model_uri=DEFAULT_.Tilstand_tilstandstype, domain=Tilstand, range=Union[str, "TilstandType"])

slots.Tilstand_gyldig_fra = Slot(uri=NGRV.gyldigFra, name="Tilstand_gyldig_fra", curie=NGRV.curie('gyldigFra'),
                   model_uri=DEFAULT_.Tilstand_gyldig_fra, domain=Tilstand, range=Union[str, XSDDate])

slots.Tilstand_gyldig_til = Slot(uri=NGRV.gyldigTil, name="Tilstand_gyldig_til", curie=NGRV.curie('gyldigTil'),
                   model_uri=DEFAULT_.Tilstand_gyldig_til, domain=Tilstand, range=Optional[Union[str, XSDDate]])

slots.Organisasjonsform_organisasjonsform_kode = Slot(uri=NGRV.organisasjonsformKode, name="Organisasjonsform_organisasjonsform_kode", curie=NGRV.curie('organisasjonsformKode'),
                   model_uri=DEFAULT_.Organisasjonsform_organisasjonsform_kode, domain=Organisasjonsform, range=str)

slots.Organisasjonsform_organisasjonsform_beskrivelse = Slot(uri=NGRV.organisasjonsformBeskrivelse, name="Organisasjonsform_organisasjonsform_beskrivelse", curie=NGRV.curie('organisasjonsformBeskrivelse'),
                   model_uri=DEFAULT_.Organisasjonsform_organisasjonsform_beskrivelse, domain=Organisasjonsform, range=Optional[str])

slots.Naeringskode_naeringskode_kode = Slot(uri=NGRV.naeringskodeKode, name="Naeringskode_naeringskode_kode", curie=NGRV.curie('naeringskodeKode'),
                   model_uri=DEFAULT_.Naeringskode_naeringskode_kode, domain=Naeringskode, range=str)

slots.Naeringskode_naeringskode_beskrivelse = Slot(uri=NGRV.naeringskodeBeskrivelse, name="Naeringskode_naeringskode_beskrivelse", curie=NGRV.curie('naeringskodeBeskrivelse'),
                   model_uri=DEFAULT_.Naeringskode_naeringskode_beskrivelse, domain=Naeringskode, range=Optional[str])

slots.Naeringskode_er_hovednaeringskode = Slot(uri=NGRV.erHovednaeringskode, name="Naeringskode_er_hovednaeringskode", curie=NGRV.curie('erHovednaeringskode'),
                   model_uri=DEFAULT_.Naeringskode_er_hovednaeringskode, domain=Naeringskode, range=Optional[Union[bool, Bool]])

slots.Sektorkode_sektorkode_kode = Slot(uri=NGRV.sektorkodeKode, name="Sektorkode_sektorkode_kode", curie=NGRV.curie('sektorkodeKode'),
                   model_uri=DEFAULT_.Sektorkode_sektorkode_kode, domain=Sektorkode, range=str)

slots.Sektorkode_sektorkode_beskrivelse = Slot(uri=NGRV.sektorkodeBeskrivelse, name="Sektorkode_sektorkode_beskrivelse", curie=NGRV.curie('sektorkodeBeskrivelse'),
                   model_uri=DEFAULT_.Sektorkode_sektorkode_beskrivelse, domain=Sektorkode, range=Optional[str])

slots.Kontaktinformasjon_epostadresse = Slot(uri=NGRV.epostadresse, name="Kontaktinformasjon_epostadresse", curie=NGRV.curie('epostadresse'),
                   model_uri=DEFAULT_.Kontaktinformasjon_epostadresse, domain=Kontaktinformasjon, range=Optional[str])

slots.Kontaktinformasjon_telefonnummer = Slot(uri=NGRV.telefonnummer, name="Kontaktinformasjon_telefonnummer", curie=NGRV.curie('telefonnummer'),
                   model_uri=DEFAULT_.Kontaktinformasjon_telefonnummer, domain=Kontaktinformasjon, range=Optional[str])

slots.Kontaktinformasjon_mobiltelefonnummer = Slot(uri=NGRV.mobiltelefonnummer, name="Kontaktinformasjon_mobiltelefonnummer", curie=NGRV.curie('mobiltelefonnummer'),
                   model_uri=DEFAULT_.Kontaktinformasjon_mobiltelefonnummer, domain=Kontaktinformasjon, range=Optional[str])

slots.Kontaktinformasjon_nettside = Slot(uri=NGRV.nettside, name="Kontaktinformasjon_nettside", curie=NGRV.curie('nettside'),
                   model_uri=DEFAULT_.Kontaktinformasjon_nettside, domain=Kontaktinformasjon, range=Optional[str])

slots.Varslingsadresse_varslingstype = Slot(uri=NGRV.varslingstype, name="Varslingsadresse_varslingstype", curie=NGRV.curie('varslingstype'),
                   model_uri=DEFAULT_.Varslingsadresse_varslingstype, domain=Varslingsadresse, range=Union[str, "VarslingType"])

slots.Varslingsadresse_varslingsverdi = Slot(uri=NGRV.varslingsverdi, name="Varslingsadresse_varslingsverdi", curie=NGRV.curie('varslingsverdi'),
                   model_uri=DEFAULT_.Varslingsadresse_varslingsverdi, domain=Varslingsadresse, range=str)

slots.Aktivitet_aktivitet_beskrivelse = Slot(uri=NGRV.aktivitetBeskrivelse, name="Aktivitet_aktivitet_beskrivelse", curie=NGRV.curie('aktivitetBeskrivelse'),
                   model_uri=DEFAULT_.Aktivitet_aktivitet_beskrivelse, domain=Aktivitet, range=str)

slots.RolleIVirksomhet_rollebetegnelse = Slot(uri=NGRV.rollebetegnelse, name="RolleIVirksomhet_rollebetegnelse", curie=NGRV.curie('rollebetegnelse'),
                   model_uri=DEFAULT_.RolleIVirksomhet_rollebetegnelse, domain=RolleIVirksomhet, range=Union[str, "RolleType"])

slots.RolleIVirksomhet_har_rolleinnehaver = Slot(uri=NGRV.harRolleinnehaver, name="RolleIVirksomhet_har_rolleinnehaver", curie=NGRV.curie('harRolleinnehaver'),
                   model_uri=DEFAULT_.RolleIVirksomhet_har_rolleinnehaver, domain=RolleIVirksomhet, range=Optional[Union[Union[str, RolleinnehaverId], list[Union[str, RolleinnehaverId]]]])

slots.Rolleinnehaver_kan_vaere_av_type_person = Slot(uri=NGRV.kanVaereAvTypePerson, name="Rolleinnehaver_kan_vaere_av_type_person", curie=NGRV.curie('kanVaereAvTypePerson'),
                   model_uri=DEFAULT_.Rolleinnehaver_kan_vaere_av_type_person, domain=Rolleinnehaver, range=Optional[Union[str, PersonId]])

slots.Rolleinnehaver_rolleinnehaver_navn = Slot(uri=NGRV.rolleinnehaverNavn, name="Rolleinnehaver_rolleinnehaver_navn", curie=NGRV.curie('rolleinnehaverNavn'),
                   model_uri=DEFAULT_.Rolleinnehaver_rolleinnehaver_navn, domain=Rolleinnehaver, range=Optional[str])

slots.Signaturrett_signaturrett_bestemmelse = Slot(uri=NGRV.signaturrettBestemmelse, name="Signaturrett_signaturrett_bestemmelse", curie=NGRV.curie('signaturrettBestemmelse'),
                   model_uri=DEFAULT_.Signaturrett_signaturrett_bestemmelse, domain=Signaturrett, range=str)

slots.Prokura_prokura_bestemmelse = Slot(uri=NGRV.prokurabEstemmelse, name="Prokura_prokura_bestemmelse", curie=NGRV.curie('prokurabEstemmelse'),
                   model_uri=DEFAULT_.Prokura_prokura_bestemmelse, domain=Prokura, range=str)

