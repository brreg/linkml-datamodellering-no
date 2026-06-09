# Auto generated from bvrinn-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-06-09T09:59:26
# Schema: generated
#
# id: https://example.org/generated
# description: Generert frå JSON Schema 'generated'.
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

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.11.0"
version = None

# Namespaces
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
GENERATED = CurieNamespace('generated', 'https://example.org/generated/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = GENERATED


# Types
class Versjonsnummer(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Versjonsnummer"
    type_model_uri = GENERATED.Versjonsnummer


class InnsendertjenesteType(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "InnsendertjenesteType"
    type_model_uri = GENERATED.InnsendertjenesteType


class DatoKlokkeslett(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "DatoKlokkeslett"
    type_model_uri = GENERATED.DatoKlokkeslett


class Tjenestevariant(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Tjenestevariant"
    type_model_uri = GENERATED.Tjenestevariant


class Organisasjonsform(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Organisasjonsform"
    type_model_uri = GENERATED.Organisasjonsform


class Virksomhetstype(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Virksomhetstype"
    type_model_uri = GENERATED.Virksomhetstype


class Organisasjonsnummer(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Organisasjonsnummer"
    type_model_uri = GENERATED.Organisasjonsnummer


class Virksomhetsnavn(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Virksomhetsnavn"
    type_model_uri = GENERATED.Virksomhetsnavn


class Dato(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["date"]
    type_class_curie = "xsd:date"
    type_name = "Dato"
    type_model_uri = GENERATED.Dato


class Ansvarsform(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Ansvarsform"
    type_model_uri = GENERATED.Ansvarsform


class Kommunenummer(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Kommunenummer"
    type_model_uri = GENERATED.Kommunenummer


class Postnummer(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Postnummer"
    type_model_uri = GENERATED.Postnummer


class Bruksenhetsnummer(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Bruksenhetsnummer"
    type_model_uri = GENERATED.Bruksenhetsnummer


class Husnummer(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Husnummer"
    type_model_uri = GENERATED.Husnummer


class Husbokstav(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Husbokstav"
    type_model_uri = GENERATED.Husbokstav


class InternasjonaltPrefiks(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "InternasjonaltPrefiks"
    type_model_uri = GENERATED.InternasjonaltPrefiks


class NasjonaltNummer(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "NasjonaltNummer"
    type_model_uri = GENERATED.NasjonaltNummer


class EPostadresse(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "E_postadresse"
    type_model_uri = GENERATED.EPostadresse


class Postboksnummer(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Postboksnummer"
    type_model_uri = GENERATED.Postboksnummer


class Landkode(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Landkode"
    type_model_uri = GENERATED.Landkode


class URL(str):
    """ Tester ikke på patterns siden lovlig patterns kan skifte. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "URL"
    type_model_uri = GENERATED.URL


class Aktivitetskode(int):
    """ TODO: beskriv typen """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "Aktivitetskode"
    type_model_uri = GENERATED.Aktivitetskode


class Tekst1000(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Tekst1000"
    type_model_uri = GENERATED.Tekst1000


class Rolletypegruppe2(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Rolletypegruppe_2"
    type_model_uri = GENERATED.Rolletypegruppe2


class PersonMappingId(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "PersonMappingId"
    type_model_uri = GENERATED.PersonMappingId


class ValgtAv(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ValgtAv"
    type_model_uri = GENERATED.ValgtAv


class SignaturrettEllerProkuraregel(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "SignaturrettEllerProkuraregel"
    type_model_uri = GENERATED.SignaturrettEllerProkuraregel


class Mengdeangivelse(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Mengdeangivelse"
    type_model_uri = GENERATED.Mengdeangivelse


class TilknyttetRegistertype(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "TilknyttetRegistertype"
    type_model_uri = GENERATED.TilknyttetRegistertype


class FagsystemId(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "FagsystemId"
    type_model_uri = GENERATED.FagsystemId


class Tekst50(str):
    """ TODO: beskriv typen """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Tekst50"
    type_model_uri = GENERATED.Tekst50


# Class references
class InnrapporteringId(URIorCURIE):
    pass


class VirksomhetsinformasjonHovedenhetId(URIorCURIE):
    pass


class ForretningsadresseId(URIorCURIE):
    pass


class StedsadresseId(URIorCURIE):
    pass


class VegadresseId(URIorCURIE):
    pass


class AdressenummerId(URIorCURIE):
    pass


class VarslingsadresseId(URIorCURIE):
    pass


class MobilnummerId(URIorCURIE):
    pass


class PostadresseId(URIorCURIE):
    pass


class PostboksadresseId(URIorCURIE):
    pass


class InternasjonalAdresseId(URIorCURIE):
    pass


class KontaktopplysningId(URIorCURIE):
    pass


class TelefonnummerId(URIorCURIE):
    pass


class VirksomhetsinformasjonUnderenhetId(URIorCURIE):
    pass


class BeliggenhetsadresseId(URIorCURIE):
    pass


class AktivitetId(URIorCURIE):
    pass


class TypeAktivitetId(URIorCURIE):
    pass


class OmdanningId(URIorCURIE):
    pass


class RolletypegruppeId(URIorCURIE):
    pass


class RolleId(URIorCURIE):
    pass


class RolleinnehaverId(URIorCURIE):
    pass


class AnsvarsandelId(URIorCURIE):
    pass


class BroekId(URIorCURIE):
    pass


class VirksomhetId(URIorCURIE):
    pass


class PersonId(URIorCURIE):
    pass


class ProkuraId(URIorCURIE):
    pass


class ProkurabestemmelseId(URIorCURIE):
    pass


class RollesettId(URIorCURIE):
    pass


class SignaturberettigetEllerProkuristId(URIorCURIE):
    pass


class SignaturrettId(URIorCURIE):
    pass


class SignaturrettsbestemmelseId(URIorCURIE):
    pass


class ForetaksinformasjonId(URIorCURIE):
    pass


class EierskifteAktivitetId(URIorCURIE):
    pass


class DelerEierskifteId(URIorCURIE):
    pass


class MatrikkelnummerId(URIorCURIE):
    pass


class InnsenderId(URIorCURIE):
    pass


class FagsystemreferanseId(URIorCURIE):
    pass


class SigneringId(URIorCURIE):
    pass


class GebyransvarligId(URIorCURIE):
    pass


@dataclass(repr=False)
class Innrapportering(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Innrapportering"]
    class_class_curie: ClassVar[str] = "generated:Innrapportering"
    class_name: ClassVar[str] = "Innrapportering"
    class_model_uri: ClassVar[URIRef] = GENERATED.Innrapportering

    id: Union[str, InnrapporteringId] = None
    versjon: str = None
    innsendertjenste: str = None
    innsendingstidspunkt: str = None
    maalformForTilbakemelding: Union[str, "Maalform"] = None
    tjenestevariant: str = None
    virksomhetsinformasjon: Union[str, VirksomhetsinformasjonHovedenhetId] = None
    innsender: Union[str, InnsenderId] = None
    fagsystemReferanse: Optional[Union[str, FagsystemreferanseId]] = None
    signering: Optional[Union[str, SigneringId]] = None
    gebyransvarlig: Optional[Union[str, GebyransvarligId]] = None
    lenkeForEttersending: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InnrapporteringId):
            self.id = InnrapporteringId(self.id)

        if self._is_empty(self.versjon):
            self.MissingRequiredField("versjon")
        if not isinstance(self.versjon, str):
            self.versjon = str(self.versjon)

        if self._is_empty(self.innsendertjenste):
            self.MissingRequiredField("innsendertjenste")
        if not isinstance(self.innsendertjenste, str):
            self.innsendertjenste = str(self.innsendertjenste)

        if self._is_empty(self.innsendingstidspunkt):
            self.MissingRequiredField("innsendingstidspunkt")
        if not isinstance(self.innsendingstidspunkt, str):
            self.innsendingstidspunkt = str(self.innsendingstidspunkt)

        if self._is_empty(self.maalformForTilbakemelding):
            self.MissingRequiredField("maalformForTilbakemelding")
        if not isinstance(self.maalformForTilbakemelding, Maalform):
            self.maalformForTilbakemelding = Maalform(self.maalformForTilbakemelding)

        if self._is_empty(self.tjenestevariant):
            self.MissingRequiredField("tjenestevariant")
        if not isinstance(self.tjenestevariant, str):
            self.tjenestevariant = str(self.tjenestevariant)

        if self._is_empty(self.virksomhetsinformasjon):
            self.MissingRequiredField("virksomhetsinformasjon")
        if not isinstance(self.virksomhetsinformasjon, VirksomhetsinformasjonHovedenhetId):
            self.virksomhetsinformasjon = VirksomhetsinformasjonHovedenhetId(self.virksomhetsinformasjon)

        if self._is_empty(self.innsender):
            self.MissingRequiredField("innsender")
        if not isinstance(self.innsender, InnsenderId):
            self.innsender = InnsenderId(self.innsender)

        if self.fagsystemReferanse is not None and not isinstance(self.fagsystemReferanse, FagsystemreferanseId):
            self.fagsystemReferanse = FagsystemreferanseId(self.fagsystemReferanse)

        if self.signering is not None and not isinstance(self.signering, SigneringId):
            self.signering = SigneringId(self.signering)

        if self.gebyransvarlig is not None and not isinstance(self.gebyransvarlig, GebyransvarligId):
            self.gebyransvarlig = GebyransvarligId(self.gebyransvarlig)

        if self.lenkeForEttersending is not None and not isinstance(self.lenkeForEttersending, str):
            self.lenkeForEttersending = str(self.lenkeForEttersending)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VirksomhetsinformasjonHovedenhet(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["VirksomhetsinformasjonHovedenhet"]
    class_class_curie: ClassVar[str] = "generated:VirksomhetsinformasjonHovedenhet"
    class_name: ClassVar[str] = "VirksomhetsinformasjonHovedenhet"
    class_model_uri: ClassVar[URIRef] = GENERATED.VirksomhetsinformasjonHovedenhet

    id: Union[str, VirksomhetsinformasjonHovedenhetId] = None
    organisasjonsform: str = None
    virksomhetstype: Optional[str] = None
    organisasjonsnummer: Optional[str] = None
    navn: Optional[str] = None
    maalform: Optional[Union[str, "Maalform"]] = None
    oppfyllerKravTilNaeringsvirksomhet: Optional[Union[bool, Bool]] = None
    venterAAFaaAnsatte: Optional[Union[bool, Bool]] = None
    datoForAvtale: Optional[str] = None
    stiftelsesdato: Optional[str] = None
    vedtektsdato: Optional[str] = None
    formaal: Optional[str] = None
    harAnsvarsbegrensning: Optional[Union[bool, Bool]] = None
    ansvarsform: Optional[str] = None
    forretningsadresse: Optional[Union[str, ForretningsadresseId]] = None
    varslingsadresse: Optional[Union[str, VarslingsadresseId]] = None
    postadresse: Optional[Union[str, PostadresseId]] = None
    kontaktopplysning: Optional[Union[str, KontaktopplysningId]] = None
    virksomhetsinformasjonUnderenhet: Optional[Union[Union[str, VirksomhetsinformasjonUnderenhetId], list[Union[str, VirksomhetsinformasjonUnderenhetId]]]] = empty_list()
    aktivitet: Optional[Union[str, AktivitetId]] = None
    omdanning: Optional[Union[str, OmdanningId]] = None
    rolletypegruppe: Optional[Union[Union[str, RolletypegruppeId], list[Union[str, RolletypegruppeId]]]] = empty_list()
    prokura: Optional[Union[str, ProkuraId]] = None
    signaturrett: Optional[Union[str, SignaturrettId]] = None
    meldtOpploesning: Optional[Union[bool, Bool]] = None
    meldtOmgjoeringAvOpploesning: Optional[Union[bool, Bool]] = None
    foretaksinformasjon: Optional[Union[str, ForetaksinformasjonId]] = None
    eierskifte: Optional[Union[Union[str, EierskifteAktivitetId], list[Union[str, EierskifteAktivitetId]]]] = empty_list()
    bekreftelseProtokollSletting: Optional[Union[bool, Bool]] = None
    matrikkelnummer: Optional[Union[Union[str, MatrikkelnummerId], list[Union[str, MatrikkelnummerId]]]] = empty_list()
    registrertITilknyttetRegister: Optional[Union[str, list[str]]] = empty_list()
    bekreftelseProtokollOpploesningOgOmgjoering: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VirksomhetsinformasjonHovedenhetId):
            self.id = VirksomhetsinformasjonHovedenhetId(self.id)

        if self._is_empty(self.organisasjonsform):
            self.MissingRequiredField("organisasjonsform")
        if not isinstance(self.organisasjonsform, str):
            self.organisasjonsform = str(self.organisasjonsform)

        if self.virksomhetstype is not None and not isinstance(self.virksomhetstype, str):
            self.virksomhetstype = str(self.virksomhetstype)

        if self.organisasjonsnummer is not None and not isinstance(self.organisasjonsnummer, str):
            self.organisasjonsnummer = str(self.organisasjonsnummer)

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.maalform is not None and not isinstance(self.maalform, Maalform):
            self.maalform = Maalform(self.maalform)

        if self.oppfyllerKravTilNaeringsvirksomhet is not None and not isinstance(self.oppfyllerKravTilNaeringsvirksomhet, Bool):
            self.oppfyllerKravTilNaeringsvirksomhet = Bool(self.oppfyllerKravTilNaeringsvirksomhet)

        if self.venterAAFaaAnsatte is not None and not isinstance(self.venterAAFaaAnsatte, Bool):
            self.venterAAFaaAnsatte = Bool(self.venterAAFaaAnsatte)

        if self.datoForAvtale is not None and not isinstance(self.datoForAvtale, str):
            self.datoForAvtale = str(self.datoForAvtale)

        if self.stiftelsesdato is not None and not isinstance(self.stiftelsesdato, str):
            self.stiftelsesdato = str(self.stiftelsesdato)

        if self.vedtektsdato is not None and not isinstance(self.vedtektsdato, str):
            self.vedtektsdato = str(self.vedtektsdato)

        if self.formaal is not None and not isinstance(self.formaal, str):
            self.formaal = str(self.formaal)

        if self.harAnsvarsbegrensning is not None and not isinstance(self.harAnsvarsbegrensning, Bool):
            self.harAnsvarsbegrensning = Bool(self.harAnsvarsbegrensning)

        if self.ansvarsform is not None and not isinstance(self.ansvarsform, str):
            self.ansvarsform = str(self.ansvarsform)

        if self.forretningsadresse is not None and not isinstance(self.forretningsadresse, ForretningsadresseId):
            self.forretningsadresse = ForretningsadresseId(self.forretningsadresse)

        if self.varslingsadresse is not None and not isinstance(self.varslingsadresse, VarslingsadresseId):
            self.varslingsadresse = VarslingsadresseId(self.varslingsadresse)

        if self.postadresse is not None and not isinstance(self.postadresse, PostadresseId):
            self.postadresse = PostadresseId(self.postadresse)

        if self.kontaktopplysning is not None and not isinstance(self.kontaktopplysning, KontaktopplysningId):
            self.kontaktopplysning = KontaktopplysningId(self.kontaktopplysning)

        if not isinstance(self.virksomhetsinformasjonUnderenhet, list):
            self.virksomhetsinformasjonUnderenhet = [self.virksomhetsinformasjonUnderenhet] if self.virksomhetsinformasjonUnderenhet is not None else []
        self.virksomhetsinformasjonUnderenhet = [v if isinstance(v, VirksomhetsinformasjonUnderenhetId) else VirksomhetsinformasjonUnderenhetId(v) for v in self.virksomhetsinformasjonUnderenhet]

        if self.aktivitet is not None and not isinstance(self.aktivitet, AktivitetId):
            self.aktivitet = AktivitetId(self.aktivitet)

        if self.omdanning is not None and not isinstance(self.omdanning, OmdanningId):
            self.omdanning = OmdanningId(self.omdanning)

        if not isinstance(self.rolletypegruppe, list):
            self.rolletypegruppe = [self.rolletypegruppe] if self.rolletypegruppe is not None else []
        self.rolletypegruppe = [v if isinstance(v, RolletypegruppeId) else RolletypegruppeId(v) for v in self.rolletypegruppe]

        if self.prokura is not None and not isinstance(self.prokura, ProkuraId):
            self.prokura = ProkuraId(self.prokura)

        if self.signaturrett is not None and not isinstance(self.signaturrett, SignaturrettId):
            self.signaturrett = SignaturrettId(self.signaturrett)

        if self.meldtOpploesning is not None and not isinstance(self.meldtOpploesning, Bool):
            self.meldtOpploesning = Bool(self.meldtOpploesning)

        if self.meldtOmgjoeringAvOpploesning is not None and not isinstance(self.meldtOmgjoeringAvOpploesning, Bool):
            self.meldtOmgjoeringAvOpploesning = Bool(self.meldtOmgjoeringAvOpploesning)

        if self.foretaksinformasjon is not None and not isinstance(self.foretaksinformasjon, ForetaksinformasjonId):
            self.foretaksinformasjon = ForetaksinformasjonId(self.foretaksinformasjon)

        if not isinstance(self.eierskifte, list):
            self.eierskifte = [self.eierskifte] if self.eierskifte is not None else []
        self.eierskifte = [v if isinstance(v, EierskifteAktivitetId) else EierskifteAktivitetId(v) for v in self.eierskifte]

        if self.bekreftelseProtokollSletting is not None and not isinstance(self.bekreftelseProtokollSletting, Bool):
            self.bekreftelseProtokollSletting = Bool(self.bekreftelseProtokollSletting)

        if not isinstance(self.matrikkelnummer, list):
            self.matrikkelnummer = [self.matrikkelnummer] if self.matrikkelnummer is not None else []
        self.matrikkelnummer = [v if isinstance(v, MatrikkelnummerId) else MatrikkelnummerId(v) for v in self.matrikkelnummer]

        if not isinstance(self.registrertITilknyttetRegister, list):
            self.registrertITilknyttetRegister = [self.registrertITilknyttetRegister] if self.registrertITilknyttetRegister is not None else []
        self.registrertITilknyttetRegister = [v if isinstance(v, str) else str(v) for v in self.registrertITilknyttetRegister]

        if self.bekreftelseProtokollOpploesningOgOmgjoering is not None and not isinstance(self.bekreftelseProtokollOpploesningOgOmgjoering, Bool):
            self.bekreftelseProtokollOpploesningOgOmgjoering = Bool(self.bekreftelseProtokollOpploesningOgOmgjoering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Forretningsadresse(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Forretningsadresse"]
    class_class_curie: ClassVar[str] = "generated:Forretningsadresse"
    class_name: ClassVar[str] = "Forretningsadresse"
    class_model_uri: ClassVar[URIRef] = GENERATED.Forretningsadresse

    id: Union[str, ForretningsadresseId] = None
    coNavn: Optional[str] = None
    vNavn: Optional[str] = None
    utgaar: Optional[Union[bool, Bool]] = None
    stedsadresse: Optional[Union[str, StedsadresseId]] = None
    vegadresse: Optional[Union[str, VegadresseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ForretningsadresseId):
            self.id = ForretningsadresseId(self.id)

        if self.coNavn is not None and not isinstance(self.coNavn, str):
            self.coNavn = str(self.coNavn)

        if self.vNavn is not None and not isinstance(self.vNavn, str):
            self.vNavn = str(self.vNavn)

        if self.utgaar is not None and not isinstance(self.utgaar, Bool):
            self.utgaar = Bool(self.utgaar)

        if self.stedsadresse is not None and not isinstance(self.stedsadresse, StedsadresseId):
            self.stedsadresse = StedsadresseId(self.stedsadresse)

        if self.vegadresse is not None and not isinstance(self.vegadresse, VegadresseId):
            self.vegadresse = VegadresseId(self.vegadresse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Stedsadresse(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Stedsadresse"]
    class_class_curie: ClassVar[str] = "generated:Stedsadresse"
    class_name: ClassVar[str] = "Stedsadresse"
    class_model_uri: ClassVar[URIRef] = GENERATED.Stedsadresse

    id: Union[str, StedsadresseId] = None
    kommunenummer: str = None
    postnummer: str = None
    stedsnavn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StedsadresseId):
            self.id = StedsadresseId(self.id)

        if self._is_empty(self.kommunenummer):
            self.MissingRequiredField("kommunenummer")
        if not isinstance(self.kommunenummer, str):
            self.kommunenummer = str(self.kommunenummer)

        if self._is_empty(self.postnummer):
            self.MissingRequiredField("postnummer")
        if not isinstance(self.postnummer, str):
            self.postnummer = str(self.postnummer)

        if self.stedsnavn is not None and not isinstance(self.stedsnavn, str):
            self.stedsnavn = str(self.stedsnavn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Vegadresse(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Vegadresse"]
    class_class_curie: ClassVar[str] = "generated:Vegadresse"
    class_name: ClassVar[str] = "Vegadresse"
    class_model_uri: ClassVar[URIRef] = GENERATED.Vegadresse

    id: Union[str, VegadresseId] = None
    adressenavn: str = None
    nummer: Union[str, AdressenummerId] = None
    kommunenummer: str = None
    postnummer: str = None
    vegadresseId: Optional[str] = None
    bruksenhetsnummer: Optional[str] = None
    adressetilleggsnavn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VegadresseId):
            self.id = VegadresseId(self.id)

        if self._is_empty(self.adressenavn):
            self.MissingRequiredField("adressenavn")
        if not isinstance(self.adressenavn, str):
            self.adressenavn = str(self.adressenavn)

        if self._is_empty(self.nummer):
            self.MissingRequiredField("nummer")
        if not isinstance(self.nummer, AdressenummerId):
            self.nummer = AdressenummerId(self.nummer)

        if self._is_empty(self.kommunenummer):
            self.MissingRequiredField("kommunenummer")
        if not isinstance(self.kommunenummer, str):
            self.kommunenummer = str(self.kommunenummer)

        if self._is_empty(self.postnummer):
            self.MissingRequiredField("postnummer")
        if not isinstance(self.postnummer, str):
            self.postnummer = str(self.postnummer)

        if self.vegadresseId is not None and not isinstance(self.vegadresseId, str):
            self.vegadresseId = str(self.vegadresseId)

        if self.bruksenhetsnummer is not None and not isinstance(self.bruksenhetsnummer, str):
            self.bruksenhetsnummer = str(self.bruksenhetsnummer)

        if self.adressetilleggsnavn is not None and not isinstance(self.adressetilleggsnavn, str):
            self.adressetilleggsnavn = str(self.adressetilleggsnavn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Adressenummer(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Adressenummer"]
    class_class_curie: ClassVar[str] = "generated:Adressenummer"
    class_name: ClassVar[str] = "Adressenummer"
    class_model_uri: ClassVar[URIRef] = GENERATED.Adressenummer

    id: Union[str, AdressenummerId] = None
    nummer: Union[str, AdressenummerId] = None
    bokstav: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdressenummerId):
            self.id = AdressenummerId(self.id)

        if self._is_empty(self.nummer):
            self.MissingRequiredField("nummer")
        if not isinstance(self.nummer, AdressenummerId):
            self.nummer = AdressenummerId(self.nummer)

        if self.bokstav is not None and not isinstance(self.bokstav, str):
            self.bokstav = str(self.bokstav)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Varslingsadresse(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Varslingsadresse"]
    class_class_curie: ClassVar[str] = "generated:Varslingsadresse"
    class_name: ClassVar[str] = "Varslingsadresse"
    class_model_uri: ClassVar[URIRef] = GENERATED.Varslingsadresse

    id: Union[str, VarslingsadresseId] = None
    mobilnummer: Optional[Union[str, MobilnummerId]] = None
    e_postadresse: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VarslingsadresseId):
            self.id = VarslingsadresseId(self.id)

        if self.mobilnummer is not None and not isinstance(self.mobilnummer, MobilnummerId):
            self.mobilnummer = MobilnummerId(self.mobilnummer)

        if self.e_postadresse is not None and not isinstance(self.e_postadresse, str):
            self.e_postadresse = str(self.e_postadresse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Mobilnummer(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Mobilnummer"]
    class_class_curie: ClassVar[str] = "generated:Mobilnummer"
    class_name: ClassVar[str] = "Mobilnummer"
    class_model_uri: ClassVar[URIRef] = GENERATED.Mobilnummer

    id: Union[str, MobilnummerId] = None
    nasjonaltNummer: str = None
    internasjonaltPrefiks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MobilnummerId):
            self.id = MobilnummerId(self.id)

        if self._is_empty(self.nasjonaltNummer):
            self.MissingRequiredField("nasjonaltNummer")
        if not isinstance(self.nasjonaltNummer, str):
            self.nasjonaltNummer = str(self.nasjonaltNummer)

        if self.internasjonaltPrefiks is not None and not isinstance(self.internasjonaltPrefiks, str):
            self.internasjonaltPrefiks = str(self.internasjonaltPrefiks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Postadresse(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Postadresse"]
    class_class_curie: ClassVar[str] = "generated:Postadresse"
    class_name: ClassVar[str] = "Postadresse"
    class_model_uri: ClassVar[URIRef] = GENERATED.Postadresse

    id: Union[str, PostadresseId] = None
    coNavn: Optional[str] = None
    vNavn: Optional[str] = None
    utgaar: Optional[Union[bool, Bool]] = None
    vegadresse: Optional[Union[str, VegadresseId]] = None
    postboksadresse: Optional[Union[str, PostboksadresseId]] = None
    internasjonalAdresse: Optional[Union[str, InternasjonalAdresseId]] = None
    stedsadresse: Optional[Union[str, StedsadresseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PostadresseId):
            self.id = PostadresseId(self.id)

        if self.coNavn is not None and not isinstance(self.coNavn, str):
            self.coNavn = str(self.coNavn)

        if self.vNavn is not None and not isinstance(self.vNavn, str):
            self.vNavn = str(self.vNavn)

        if self.utgaar is not None and not isinstance(self.utgaar, Bool):
            self.utgaar = Bool(self.utgaar)

        if self.vegadresse is not None and not isinstance(self.vegadresse, VegadresseId):
            self.vegadresse = VegadresseId(self.vegadresse)

        if self.postboksadresse is not None and not isinstance(self.postboksadresse, PostboksadresseId):
            self.postboksadresse = PostboksadresseId(self.postboksadresse)

        if self.internasjonalAdresse is not None and not isinstance(self.internasjonalAdresse, InternasjonalAdresseId):
            self.internasjonalAdresse = InternasjonalAdresseId(self.internasjonalAdresse)

        if self.stedsadresse is not None and not isinstance(self.stedsadresse, StedsadresseId):
            self.stedsadresse = StedsadresseId(self.stedsadresse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Postboksadresse(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Postboksadresse"]
    class_class_curie: ClassVar[str] = "generated:Postboksadresse"
    class_name: ClassVar[str] = "Postboksadresse"
    class_model_uri: ClassVar[URIRef] = GENERATED.Postboksadresse

    id: Union[str, PostboksadresseId] = None
    postboksnummer: str = None
    postnummer: str = None
    kommunenummer: str = None
    postboksanleggsnavn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PostboksadresseId):
            self.id = PostboksadresseId(self.id)

        if self._is_empty(self.postboksnummer):
            self.MissingRequiredField("postboksnummer")
        if not isinstance(self.postboksnummer, str):
            self.postboksnummer = str(self.postboksnummer)

        if self._is_empty(self.postnummer):
            self.MissingRequiredField("postnummer")
        if not isinstance(self.postnummer, str):
            self.postnummer = str(self.postnummer)

        if self._is_empty(self.kommunenummer):
            self.MissingRequiredField("kommunenummer")
        if not isinstance(self.kommunenummer, str):
            self.kommunenummer = str(self.kommunenummer)

        if self.postboksanleggsnavn is not None and not isinstance(self.postboksanleggsnavn, str):
            self.postboksanleggsnavn = str(self.postboksanleggsnavn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InternasjonalAdresse(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["InternasjonalAdresse"]
    class_class_curie: ClassVar[str] = "generated:InternasjonalAdresse"
    class_name: ClassVar[str] = "InternasjonalAdresse"
    class_model_uri: ClassVar[URIRef] = GENERATED.InternasjonalAdresse

    id: Union[str, InternasjonalAdresseId] = None
    landkode: str = None
    adressenavn: Optional[str] = None
    adressenummer: Optional[str] = None
    bygning: Optional[str] = None
    etasjenummer: Optional[str] = None
    boenhet: Optional[str] = None
    postboks: Optional[str] = None
    postkode: Optional[str] = None
    byEllerStedsnavn: Optional[str] = None
    region: Optional[str] = None
    distriktEllerBydel: Optional[str] = None
    friAdressetekst: Optional[Union[str, list[str]]] = empty_list()
    adresseidentifikator: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InternasjonalAdresseId):
            self.id = InternasjonalAdresseId(self.id)

        if self._is_empty(self.landkode):
            self.MissingRequiredField("landkode")
        if not isinstance(self.landkode, str):
            self.landkode = str(self.landkode)

        if self.adressenavn is not None and not isinstance(self.adressenavn, str):
            self.adressenavn = str(self.adressenavn)

        if self.adressenummer is not None and not isinstance(self.adressenummer, str):
            self.adressenummer = str(self.adressenummer)

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

        if self.byEllerStedsnavn is not None and not isinstance(self.byEllerStedsnavn, str):
            self.byEllerStedsnavn = str(self.byEllerStedsnavn)

        if self.region is not None and not isinstance(self.region, str):
            self.region = str(self.region)

        if self.distriktEllerBydel is not None and not isinstance(self.distriktEllerBydel, str):
            self.distriktEllerBydel = str(self.distriktEllerBydel)

        if not isinstance(self.friAdressetekst, list):
            self.friAdressetekst = [self.friAdressetekst] if self.friAdressetekst is not None else []
        self.friAdressetekst = [v if isinstance(v, str) else str(v) for v in self.friAdressetekst]

        if self.adresseidentifikator is not None and not isinstance(self.adresseidentifikator, str):
            self.adresseidentifikator = str(self.adresseidentifikator)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Kontaktopplysning(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Kontaktopplysning"]
    class_class_curie: ClassVar[str] = "generated:Kontaktopplysning"
    class_name: ClassVar[str] = "Kontaktopplysning"
    class_model_uri: ClassVar[URIRef] = GENERATED.Kontaktopplysning

    id: Union[str, KontaktopplysningId] = None
    mobilnummer: Optional[Union[str, MobilnummerId]] = None
    e_postadresse: Optional[str] = None
    nettadresse: Optional[str] = None
    mobilnummerUtgaar: Optional[Union[bool, Bool]] = None
    e_postadresseUtgaar: Optional[Union[bool, Bool]] = None
    nettadresseUtgaar: Optional[Union[bool, Bool]] = None
    telefonnummer: Optional[Union[str, TelefonnummerId]] = None
    telefonnummerUtgaar: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KontaktopplysningId):
            self.id = KontaktopplysningId(self.id)

        if self.mobilnummer is not None and not isinstance(self.mobilnummer, MobilnummerId):
            self.mobilnummer = MobilnummerId(self.mobilnummer)

        if self.e_postadresse is not None and not isinstance(self.e_postadresse, str):
            self.e_postadresse = str(self.e_postadresse)

        if self.nettadresse is not None and not isinstance(self.nettadresse, str):
            self.nettadresse = str(self.nettadresse)

        if self.mobilnummerUtgaar is not None and not isinstance(self.mobilnummerUtgaar, Bool):
            self.mobilnummerUtgaar = Bool(self.mobilnummerUtgaar)

        if self.e_postadresseUtgaar is not None and not isinstance(self.e_postadresseUtgaar, Bool):
            self.e_postadresseUtgaar = Bool(self.e_postadresseUtgaar)

        if self.nettadresseUtgaar is not None and not isinstance(self.nettadresseUtgaar, Bool):
            self.nettadresseUtgaar = Bool(self.nettadresseUtgaar)

        if self.telefonnummer is not None and not isinstance(self.telefonnummer, TelefonnummerId):
            self.telefonnummer = TelefonnummerId(self.telefonnummer)

        if self.telefonnummerUtgaar is not None and not isinstance(self.telefonnummerUtgaar, Bool):
            self.telefonnummerUtgaar = Bool(self.telefonnummerUtgaar)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Telefonnummer(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Telefonnummer"]
    class_class_curie: ClassVar[str] = "generated:Telefonnummer"
    class_name: ClassVar[str] = "Telefonnummer"
    class_model_uri: ClassVar[URIRef] = GENERATED.Telefonnummer

    id: Union[str, TelefonnummerId] = None
    nasjonaltNummer: str = None
    internasjonaltPrefiks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TelefonnummerId):
            self.id = TelefonnummerId(self.id)

        if self._is_empty(self.nasjonaltNummer):
            self.MissingRequiredField("nasjonaltNummer")
        if not isinstance(self.nasjonaltNummer, str):
            self.nasjonaltNummer = str(self.nasjonaltNummer)

        if self.internasjonaltPrefiks is not None and not isinstance(self.internasjonaltPrefiks, str):
            self.internasjonaltPrefiks = str(self.internasjonaltPrefiks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VirksomhetsinformasjonUnderenhet(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["VirksomhetsinformasjonUnderenhet"]
    class_class_curie: ClassVar[str] = "generated:VirksomhetsinformasjonUnderenhet"
    class_name: ClassVar[str] = "VirksomhetsinformasjonUnderenhet"
    class_model_uri: ClassVar[URIRef] = GENERATED.VirksomhetsinformasjonUnderenhet

    id: Union[str, VirksomhetsinformasjonUnderenhetId] = None
    oppstartsdato: Optional[str] = None
    navn: Optional[str] = None
    organisasjonsnummer: Optional[str] = None
    nedleggelsesdato: Optional[str] = None
    beliggenhetsadresse: Optional[Union[str, BeliggenhetsadresseId]] = None
    postadresse: Optional[Union[str, PostadresseId]] = None
    kontaktopplysning: Optional[Union[str, KontaktopplysningId]] = None
    aktivitet: Optional[Union[str, AktivitetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VirksomhetsinformasjonUnderenhetId):
            self.id = VirksomhetsinformasjonUnderenhetId(self.id)

        if self.oppstartsdato is not None and not isinstance(self.oppstartsdato, str):
            self.oppstartsdato = str(self.oppstartsdato)

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        if self.organisasjonsnummer is not None and not isinstance(self.organisasjonsnummer, str):
            self.organisasjonsnummer = str(self.organisasjonsnummer)

        if self.nedleggelsesdato is not None and not isinstance(self.nedleggelsesdato, str):
            self.nedleggelsesdato = str(self.nedleggelsesdato)

        if self.beliggenhetsadresse is not None and not isinstance(self.beliggenhetsadresse, BeliggenhetsadresseId):
            self.beliggenhetsadresse = BeliggenhetsadresseId(self.beliggenhetsadresse)

        if self.postadresse is not None and not isinstance(self.postadresse, PostadresseId):
            self.postadresse = PostadresseId(self.postadresse)

        if self.kontaktopplysning is not None and not isinstance(self.kontaktopplysning, KontaktopplysningId):
            self.kontaktopplysning = KontaktopplysningId(self.kontaktopplysning)

        if self.aktivitet is not None and not isinstance(self.aktivitet, AktivitetId):
            self.aktivitet = AktivitetId(self.aktivitet)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Beliggenhetsadresse(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Beliggenhetsadresse"]
    class_class_curie: ClassVar[str] = "generated:Beliggenhetsadresse"
    class_name: ClassVar[str] = "Beliggenhetsadresse"
    class_model_uri: ClassVar[URIRef] = GENERATED.Beliggenhetsadresse

    id: Union[str, BeliggenhetsadresseId] = None
    coNavn: Optional[str] = None
    vNavn: Optional[str] = None
    vegadresse: Optional[Union[str, VegadresseId]] = None
    stedsadresse: Optional[Union[str, StedsadresseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeliggenhetsadresseId):
            self.id = BeliggenhetsadresseId(self.id)

        if self.coNavn is not None and not isinstance(self.coNavn, str):
            self.coNavn = str(self.coNavn)

        if self.vNavn is not None and not isinstance(self.vNavn, str):
            self.vNavn = str(self.vNavn)

        if self.vegadresse is not None and not isinstance(self.vegadresse, VegadresseId):
            self.vegadresse = VegadresseId(self.vegadresse)

        if self.stedsadresse is not None and not isinstance(self.stedsadresse, StedsadresseId):
            self.stedsadresse = StedsadresseId(self.stedsadresse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aktivitet(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Aktivitet"]
    class_class_curie: ClassVar[str] = "generated:Aktivitet"
    class_name: ClassVar[str] = "Aktivitet"
    class_model_uri: ClassVar[URIRef] = GENERATED.Aktivitet

    id: Union[str, AktivitetId] = None
    aktivitet: Union[str, AktivitetId] = None
    datoGyldigFra: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AktivitetId):
            self.id = AktivitetId(self.id)

        if self._is_empty(self.aktivitet):
            self.MissingRequiredField("aktivitet")
        if not isinstance(self.aktivitet, AktivitetId):
            self.aktivitet = AktivitetId(self.aktivitet)

        if self.datoGyldigFra is not None and not isinstance(self.datoGyldigFra, str):
            self.datoGyldigFra = str(self.datoGyldigFra)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TypeAktivitet(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["TypeAktivitet"]
    class_class_curie: ClassVar[str] = "generated:TypeAktivitet"
    class_name: ClassVar[str] = "TypeAktivitet"
    class_model_uri: ClassVar[URIRef] = GENERATED.TypeAktivitet

    id: Union[str, TypeAktivitetId] = None
    rekkefoelge: int = None
    tekst: str = None
    aktivitetskode: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TypeAktivitetId):
            self.id = TypeAktivitetId(self.id)

        if self._is_empty(self.rekkefoelge):
            self.MissingRequiredField("rekkefoelge")
        if not isinstance(self.rekkefoelge, int):
            self.rekkefoelge = int(self.rekkefoelge)

        if self._is_empty(self.tekst):
            self.MissingRequiredField("tekst")
        if not isinstance(self.tekst, str):
            self.tekst = str(self.tekst)

        if self.aktivitetskode is not None and not isinstance(self.aktivitetskode, int):
            self.aktivitetskode = int(self.aktivitetskode)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Omdanning(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Omdanning"]
    class_class_curie: ClassVar[str] = "generated:Omdanning"
    class_name: ClassVar[str] = "Omdanning"
    class_model_uri: ClassVar[URIRef] = GENERATED.Omdanning

    id: Union[str, OmdanningId] = None
    nyOrganisasjonsform: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OmdanningId):
            self.id = OmdanningId(self.id)

        if self._is_empty(self.nyOrganisasjonsform):
            self.MissingRequiredField("nyOrganisasjonsform")
        if not isinstance(self.nyOrganisasjonsform, str):
            self.nyOrganisasjonsform = str(self.nyOrganisasjonsform)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rolletypegruppe(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Rolletypegruppe"]
    class_class_curie: ClassVar[str] = "generated:Rolletypegruppe"
    class_name: ClassVar[str] = "Rolletypegruppe"
    class_model_uri: ClassVar[URIRef] = GENERATED.Rolletypegruppe

    id: Union[str, RolletypegruppeId] = None
    rollegruppe: str = None
    utgaar: Optional[Union[bool, Bool]] = None
    kjoennssammensetningAnsattvalgte: Optional[Union[bool, Bool]] = None
    kjoennssammensetningStyre: Optional[Union[bool, Bool]] = None
    rolle: Optional[Union[Union[str, RolleId], list[Union[str, RolleId]]]] = empty_list()
    bekreftelseProtokoll: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RolletypegruppeId):
            self.id = RolletypegruppeId(self.id)

        if self._is_empty(self.rollegruppe):
            self.MissingRequiredField("rollegruppe")
        if not isinstance(self.rollegruppe, str):
            self.rollegruppe = str(self.rollegruppe)

        if self.utgaar is not None and not isinstance(self.utgaar, Bool):
            self.utgaar = Bool(self.utgaar)

        if self.kjoennssammensetningAnsattvalgte is not None and not isinstance(self.kjoennssammensetningAnsattvalgte, Bool):
            self.kjoennssammensetningAnsattvalgte = Bool(self.kjoennssammensetningAnsattvalgte)

        if self.kjoennssammensetningStyre is not None and not isinstance(self.kjoennssammensetningStyre, Bool):
            self.kjoennssammensetningStyre = Bool(self.kjoennssammensetningStyre)

        if not isinstance(self.rolle, list):
            self.rolle = [self.rolle] if self.rolle is not None else []
        self.rolle = [v if isinstance(v, RolleId) else RolleId(v) for v in self.rolle]

        if self.bekreftelseProtokoll is not None and not isinstance(self.bekreftelseProtokoll, Bool):
            self.bekreftelseProtokoll = Bool(self.bekreftelseProtokoll)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rolle(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Rolle"]
    class_class_curie: ClassVar[str] = "generated:Rolle"
    class_name: ClassVar[str] = "Rolle"
    class_model_uri: ClassVar[URIRef] = GENERATED.Rolle

    id: Union[str, RolleId] = None
    rolletype: Union[str, "Rolletype"] = None
    rolleinnehaver: Union[str, RolleinnehaverId] = None
    tildelerAvRolle: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RolleId):
            self.id = RolleId(self.id)

        if self._is_empty(self.rolletype):
            self.MissingRequiredField("rolletype")
        if not isinstance(self.rolletype, Rolletype):
            self.rolletype = Rolletype(self.rolletype)

        if self._is_empty(self.rolleinnehaver):
            self.MissingRequiredField("rolleinnehaver")
        if not isinstance(self.rolleinnehaver, RolleinnehaverId):
            self.rolleinnehaver = RolleinnehaverId(self.rolleinnehaver)

        if self.tildelerAvRolle is not None and not isinstance(self.tildelerAvRolle, str):
            self.tildelerAvRolle = str(self.tildelerAvRolle)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rolleinnehaver(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Rolleinnehaver"]
    class_class_curie: ClassVar[str] = "generated:Rolleinnehaver"
    class_name: ClassVar[str] = "Rolleinnehaver"
    class_model_uri: ClassVar[URIRef] = GENERATED.Rolleinnehaver

    id: Union[str, RolleinnehaverId] = None
    oenskerAAFratre: Optional[Union[bool, Bool]] = None
    ansvarsandel: Optional[Union[str, AnsvarsandelId]] = None
    avdelingskontor: Optional[str] = None
    fratredenErVarslet: Optional[Union[bool, Bool]] = None
    valgtAv: Optional[str] = None
    virksomhet: Optional[Union[str, VirksomhetId]] = None
    person: Optional[Union[str, PersonId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RolleinnehaverId):
            self.id = RolleinnehaverId(self.id)

        if self.oenskerAAFratre is not None and not isinstance(self.oenskerAAFratre, Bool):
            self.oenskerAAFratre = Bool(self.oenskerAAFratre)

        if self.ansvarsandel is not None and not isinstance(self.ansvarsandel, AnsvarsandelId):
            self.ansvarsandel = AnsvarsandelId(self.ansvarsandel)

        if self.avdelingskontor is not None and not isinstance(self.avdelingskontor, str):
            self.avdelingskontor = str(self.avdelingskontor)

        if self.fratredenErVarslet is not None and not isinstance(self.fratredenErVarslet, Bool):
            self.fratredenErVarslet = Bool(self.fratredenErVarslet)

        if self.valgtAv is not None and not isinstance(self.valgtAv, str):
            self.valgtAv = str(self.valgtAv)

        if self.virksomhet is not None and not isinstance(self.virksomhet, VirksomhetId):
            self.virksomhet = VirksomhetId(self.virksomhet)

        if self.person is not None and not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ansvarsandel(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Ansvarsandel"]
    class_class_curie: ClassVar[str] = "generated:Ansvarsandel"
    class_name: ClassVar[str] = "Ansvarsandel"
    class_model_uri: ClassVar[URIRef] = GENERATED.Ansvarsandel

    id: Union[str, AnsvarsandelId] = None
    broek: Optional[Union[str, BroekId]] = None
    prosent: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnsvarsandelId):
            self.id = AnsvarsandelId(self.id)

        if self.broek is not None and not isinstance(self.broek, BroekId):
            self.broek = BroekId(self.broek)

        if self.prosent is not None and not isinstance(self.prosent, float):
            self.prosent = float(self.prosent)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Broek(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Broek"]
    class_class_curie: ClassVar[str] = "generated:Broek"
    class_name: ClassVar[str] = "Broek"
    class_model_uri: ClassVar[URIRef] = GENERATED.Broek

    id: Union[str, BroekId] = None
    teller: Optional[int] = None
    nevner: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BroekId):
            self.id = BroekId(self.id)

        if self.teller is not None and not isinstance(self.teller, int):
            self.teller = int(self.teller)

        if self.nevner is not None and not isinstance(self.nevner, int):
            self.nevner = int(self.nevner)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Virksomhet(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Virksomhet"]
    class_class_curie: ClassVar[str] = "generated:Virksomhet"
    class_name: ClassVar[str] = "Virksomhet"
    class_model_uri: ClassVar[URIRef] = GENERATED.Virksomhet

    id: Union[str, VirksomhetId] = None
    virksomhetsidentifikator: str = None
    navn: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VirksomhetId):
            self.id = VirksomhetId(self.id)

        if self._is_empty(self.virksomhetsidentifikator):
            self.MissingRequiredField("virksomhetsidentifikator")
        if not isinstance(self.virksomhetsidentifikator, str):
            self.virksomhetsidentifikator = str(self.virksomhetsidentifikator)

        if self.navn is not None and not isinstance(self.navn, str):
            self.navn = str(self.navn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Person"]
    class_class_curie: ClassVar[str] = "generated:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = GENERATED.Person

    id: Union[str, PersonId] = None
    mappingId: str = None
    fulltNavn: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.mappingId):
            self.MissingRequiredField("mappingId")
        if not isinstance(self.mappingId, str):
            self.mappingId = str(self.mappingId)

        if self._is_empty(self.fulltNavn):
            self.MissingRequiredField("fulltNavn")
        if not isinstance(self.fulltNavn, str):
            self.fulltNavn = str(self.fulltNavn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Prokura(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Prokura"]
    class_class_curie: ClassVar[str] = "generated:Prokura"
    class_name: ClassVar[str] = "Prokura"
    class_model_uri: ClassVar[URIRef] = GENERATED.Prokura

    id: Union[str, ProkuraId] = None
    utgaar: Optional[Union[bool, Bool]] = None
    prokurabestemmelse: Optional[Union[Union[str, ProkurabestemmelseId], list[Union[str, ProkurabestemmelseId]]]] = empty_list()
    bekreftelseProtokoll: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProkuraId):
            self.id = ProkuraId(self.id)

        if self.utgaar is not None and not isinstance(self.utgaar, Bool):
            self.utgaar = Bool(self.utgaar)

        if not isinstance(self.prokurabestemmelse, list):
            self.prokurabestemmelse = [self.prokurabestemmelse] if self.prokurabestemmelse is not None else []
        self.prokurabestemmelse = [v if isinstance(v, ProkurabestemmelseId) else ProkurabestemmelseId(v) for v in self.prokurabestemmelse]

        if self.bekreftelseProtokoll is not None and not isinstance(self.bekreftelseProtokoll, Bool):
            self.bekreftelseProtokoll = Bool(self.bekreftelseProtokoll)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Prokurabestemmelse(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Prokurabestemmelse"]
    class_class_curie: ClassVar[str] = "generated:Prokurabestemmelse"
    class_name: ClassVar[str] = "Prokurabestemmelse"
    class_model_uri: ClassVar[URIRef] = GENERATED.Prokurabestemmelse

    id: Union[str, ProkurabestemmelseId] = None
    regel: str = None
    rollesett: Union[Union[str, RollesettId], list[Union[str, RollesettId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProkurabestemmelseId):
            self.id = ProkurabestemmelseId(self.id)

        if self._is_empty(self.regel):
            self.MissingRequiredField("regel")
        if not isinstance(self.regel, str):
            self.regel = str(self.regel)

        if self._is_empty(self.rollesett):
            self.MissingRequiredField("rollesett")
        if not isinstance(self.rollesett, list):
            self.rollesett = [self.rollesett] if self.rollesett is not None else []
        self.rollesett = [v if isinstance(v, RollesettId) else RollesettId(v) for v in self.rollesett]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rollesett(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Rollesett"]
    class_class_curie: ClassVar[str] = "generated:Rollesett"
    class_name: ClassVar[str] = "Rollesett"
    class_model_uri: ClassVar[URIRef] = GENERATED.Rollesett

    id: Union[str, RollesettId] = None
    rolletype: Union[str, "Rolletype"] = None
    signaturberettigetEllerProkurist: Optional[Union[Union[str, SignaturberettigetEllerProkuristId], list[Union[str, SignaturberettigetEllerProkuristId]]]] = empty_list()
    minsteMengdeangivelse: Optional[str] = None
    minsteAntall: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RollesettId):
            self.id = RollesettId(self.id)

        if self._is_empty(self.rolletype):
            self.MissingRequiredField("rolletype")
        if not isinstance(self.rolletype, Rolletype):
            self.rolletype = Rolletype(self.rolletype)

        if not isinstance(self.signaturberettigetEllerProkurist, list):
            self.signaturberettigetEllerProkurist = [self.signaturberettigetEllerProkurist] if self.signaturberettigetEllerProkurist is not None else []
        self.signaturberettigetEllerProkurist = [v if isinstance(v, SignaturberettigetEllerProkuristId) else SignaturberettigetEllerProkuristId(v) for v in self.signaturberettigetEllerProkurist]

        if self.minsteMengdeangivelse is not None and not isinstance(self.minsteMengdeangivelse, str):
            self.minsteMengdeangivelse = str(self.minsteMengdeangivelse)

        if self.minsteAntall is not None and not isinstance(self.minsteAntall, int):
            self.minsteAntall = int(self.minsteAntall)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SignaturberettigetEllerProkurist(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["SignaturberettigetEllerProkurist"]
    class_class_curie: ClassVar[str] = "generated:SignaturberettigetEllerProkurist"
    class_name: ClassVar[str] = "SignaturberettigetEllerProkurist"
    class_model_uri: ClassVar[URIRef] = GENERATED.SignaturberettigetEllerProkurist

    id: Union[str, SignaturberettigetEllerProkuristId] = None
    virksomhet: Optional[Union[str, VirksomhetId]] = None
    person: Optional[Union[str, PersonId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SignaturberettigetEllerProkuristId):
            self.id = SignaturberettigetEllerProkuristId(self.id)

        if self.virksomhet is not None and not isinstance(self.virksomhet, VirksomhetId):
            self.virksomhet = VirksomhetId(self.virksomhet)

        if self.person is not None and not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Signaturrett(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Signaturrett"]
    class_class_curie: ClassVar[str] = "generated:Signaturrett"
    class_name: ClassVar[str] = "Signaturrett"
    class_model_uri: ClassVar[URIRef] = GENERATED.Signaturrett

    id: Union[str, SignaturrettId] = None
    utgaar: Optional[Union[bool, Bool]] = None
    signaturrettsbestemmelsse: Optional[Union[Union[str, SignaturrettsbestemmelseId], list[Union[str, SignaturrettsbestemmelseId]]]] = empty_list()
    bekreftelseProtokoll: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SignaturrettId):
            self.id = SignaturrettId(self.id)

        if self.utgaar is not None and not isinstance(self.utgaar, Bool):
            self.utgaar = Bool(self.utgaar)

        if not isinstance(self.signaturrettsbestemmelsse, list):
            self.signaturrettsbestemmelsse = [self.signaturrettsbestemmelsse] if self.signaturrettsbestemmelsse is not None else []
        self.signaturrettsbestemmelsse = [v if isinstance(v, SignaturrettsbestemmelseId) else SignaturrettsbestemmelseId(v) for v in self.signaturrettsbestemmelsse]

        if self.bekreftelseProtokoll is not None and not isinstance(self.bekreftelseProtokoll, Bool):
            self.bekreftelseProtokoll = Bool(self.bekreftelseProtokoll)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Signaturrettsbestemmelse(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Signaturrettsbestemmelse"]
    class_class_curie: ClassVar[str] = "generated:Signaturrettsbestemmelse"
    class_name: ClassVar[str] = "Signaturrettsbestemmelse"
    class_model_uri: ClassVar[URIRef] = GENERATED.Signaturrettsbestemmelse

    id: Union[str, SignaturrettsbestemmelseId] = None
    regel: str = None
    rollesett: Union[Union[str, RollesettId], list[Union[str, RollesettId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SignaturrettsbestemmelseId):
            self.id = SignaturrettsbestemmelseId(self.id)

        if self._is_empty(self.regel):
            self.MissingRequiredField("regel")
        if not isinstance(self.regel, str):
            self.regel = str(self.regel)

        if self._is_empty(self.rollesett):
            self.MissingRequiredField("rollesett")
        if not isinstance(self.rollesett, list):
            self.rollesett = [self.rollesett] if self.rollesett is not None else []
        self.rollesett = [v if isinstance(v, RollesettId) else RollesettId(v) for v in self.rollesett]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Foretaksinformasjon(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Foretaksinformasjon"]
    class_class_curie: ClassVar[str] = "generated:Foretaksinformasjon"
    class_name: ClassVar[str] = "Foretaksinformasjon"
    class_model_uri: ClassVar[URIRef] = GENERATED.Foretaksinformasjon

    id: Union[str, ForetaksinformasjonId] = None
    oenskesRegistrertIForetaksregisteret: Optional[Union[bool, Bool]] = None
    oenskesSlettetIForetaksregisteret: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ForetaksinformasjonId):
            self.id = ForetaksinformasjonId(self.id)

        if self.oenskesRegistrertIForetaksregisteret is not None and not isinstance(self.oenskesRegistrertIForetaksregisteret, Bool):
            self.oenskesRegistrertIForetaksregisteret = Bool(self.oenskesRegistrertIForetaksregisteret)

        if self.oenskesSlettetIForetaksregisteret is not None and not isinstance(self.oenskesSlettetIForetaksregisteret, Bool):
            self.oenskesSlettetIForetaksregisteret = Bool(self.oenskesSlettetIForetaksregisteret)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EierskifteAktivitet(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["EierskifteAktivitet"]
    class_class_curie: ClassVar[str] = "generated:EierskifteAktivitet"
    class_name: ClassVar[str] = "EierskifteAktivitet"
    class_model_uri: ClassVar[URIRef] = GENERATED.EierskifteAktivitet

    id: Union[str, EierskifteAktivitetId] = None
    typeEierskifte: Union[str, "TypeEierskifte"] = None
    organisasjonsnummerHovedenhet: str = None
    gjelderHeleAktiviteten: Union[bool, Bool] = None
    eierskiftedato: str = None
    hvilkeDeler: Optional[Union[str, DelerEierskifteId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EierskifteAktivitetId):
            self.id = EierskifteAktivitetId(self.id)

        if self._is_empty(self.typeEierskifte):
            self.MissingRequiredField("typeEierskifte")
        if not isinstance(self.typeEierskifte, TypeEierskifte):
            self.typeEierskifte = TypeEierskifte(self.typeEierskifte)

        if self._is_empty(self.organisasjonsnummerHovedenhet):
            self.MissingRequiredField("organisasjonsnummerHovedenhet")
        if not isinstance(self.organisasjonsnummerHovedenhet, str):
            self.organisasjonsnummerHovedenhet = str(self.organisasjonsnummerHovedenhet)

        if self._is_empty(self.gjelderHeleAktiviteten):
            self.MissingRequiredField("gjelderHeleAktiviteten")
        if not isinstance(self.gjelderHeleAktiviteten, Bool):
            self.gjelderHeleAktiviteten = Bool(self.gjelderHeleAktiviteten)

        if self._is_empty(self.eierskiftedato):
            self.MissingRequiredField("eierskiftedato")
        if not isinstance(self.eierskiftedato, str):
            self.eierskiftedato = str(self.eierskiftedato)

        if self.hvilkeDeler is not None and not isinstance(self.hvilkeDeler, DelerEierskifteId):
            self.hvilkeDeler = DelerEierskifteId(self.hvilkeDeler)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelerEierskifte(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["DelerEierskifte"]
    class_class_curie: ClassVar[str] = "generated:DelerEierskifte"
    class_name: ClassVar[str] = "DelerEierskifte"
    class_model_uri: ClassVar[URIRef] = GENERATED.DelerEierskifte

    id: Union[str, DelerEierskifteId] = None
    beskrivelse: Optional[str] = None
    underenhet: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelerEierskifteId):
            self.id = DelerEierskifteId(self.id)

        if self.beskrivelse is not None and not isinstance(self.beskrivelse, str):
            self.beskrivelse = str(self.beskrivelse)

        if not isinstance(self.underenhet, list):
            self.underenhet = [self.underenhet] if self.underenhet is not None else []
        self.underenhet = [v if isinstance(v, str) else str(v) for v in self.underenhet]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Matrikkelnummer(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Matrikkelnummer"]
    class_class_curie: ClassVar[str] = "generated:Matrikkelnummer"
    class_name: ClassVar[str] = "Matrikkelnummer"
    class_model_uri: ClassVar[URIRef] = GENERATED.Matrikkelnummer

    id: Union[str, MatrikkelnummerId] = None
    kommunenummer: Optional[str] = None
    gaardsnummer: Optional[int] = None
    bruksnummer: Optional[int] = None
    festenummer: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MatrikkelnummerId):
            self.id = MatrikkelnummerId(self.id)

        if self.kommunenummer is not None and not isinstance(self.kommunenummer, str):
            self.kommunenummer = str(self.kommunenummer)

        if self.gaardsnummer is not None and not isinstance(self.gaardsnummer, int):
            self.gaardsnummer = int(self.gaardsnummer)

        if self.bruksnummer is not None and not isinstance(self.bruksnummer, int):
            self.bruksnummer = int(self.bruksnummer)

        if self.festenummer is not None and not isinstance(self.festenummer, int):
            self.festenummer = int(self.festenummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Innsender(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Innsender"]
    class_class_curie: ClassVar[str] = "generated:Innsender"
    class_name: ClassVar[str] = "Innsender"
    class_model_uri: ClassVar[URIRef] = GENERATED.Innsender

    id: Union[str, InnsenderId] = None
    test: str = None
    virksomhet: Optional[Union[str, VirksomhetId]] = None
    person: Optional[Union[str, PersonId]] = None
    e_postadresse: Optional[str] = None
    mobilnummer: Optional[Union[str, MobilnummerId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InnsenderId):
            self.id = InnsenderId(self.id)

        if self._is_empty(self.test):
            self.MissingRequiredField("test")
        if not isinstance(self.test, str):
            self.test = str(self.test)

        if self.virksomhet is not None and not isinstance(self.virksomhet, VirksomhetId):
            self.virksomhet = VirksomhetId(self.virksomhet)

        if self.person is not None and not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

        if self.e_postadresse is not None and not isinstance(self.e_postadresse, str):
            self.e_postadresse = str(self.e_postadresse)

        if self.mobilnummer is not None and not isinstance(self.mobilnummer, MobilnummerId):
            self.mobilnummer = MobilnummerId(self.mobilnummer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fagsystemreferanse(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Fagsystemreferanse"]
    class_class_curie: ClassVar[str] = "generated:Fagsystemreferanse"
    class_name: ClassVar[str] = "Fagsystemreferanse"
    class_model_uri: ClassVar[URIRef] = GENERATED.Fagsystemreferanse

    id: Union[str, FagsystemreferanseId] = None
    fagsystemID: str = None
    orgnrFagsystem: str = None
    referanseFagsystem: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FagsystemreferanseId):
            self.id = FagsystemreferanseId(self.id)

        if self._is_empty(self.fagsystemID):
            self.MissingRequiredField("fagsystemID")
        if not isinstance(self.fagsystemID, str):
            self.fagsystemID = str(self.fagsystemID)

        if self._is_empty(self.orgnrFagsystem):
            self.MissingRequiredField("orgnrFagsystem")
        if not isinstance(self.orgnrFagsystem, str):
            self.orgnrFagsystem = str(self.orgnrFagsystem)

        if self._is_empty(self.referanseFagsystem):
            self.MissingRequiredField("referanseFagsystem")
        if not isinstance(self.referanseFagsystem, str):
            self.referanseFagsystem = str(self.referanseFagsystem)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Signering(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Signering"]
    class_class_curie: ClassVar[str] = "generated:Signering"
    class_name: ClassVar[str] = "Signering"
    class_model_uri: ClassVar[URIRef] = GENERATED.Signering

    id: Union[str, SigneringId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SigneringId):
            self.id = SigneringId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Gebyransvarlig(YAMLRoot):
    """
    TODO: beskriv klassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["Gebyransvarlig"]
    class_class_curie: ClassVar[str] = "generated:Gebyransvarlig"
    class_name: ClassVar[str] = "Gebyransvarlig"
    class_model_uri: ClassVar[URIRef] = GENERATED.Gebyransvarlig

    id: Union[str, GebyransvarligId] = None
    gebyransvarligType: Union[str, "GebyransvarligType"] = None
    eksternFakturareferanse: Optional[str] = None
    virksomhet: Optional[Union[str, VirksomhetId]] = None
    person: Optional[Union[str, PersonId]] = None
    mobilnummer: Optional[Union[str, MobilnummerId]] = None
    e_postadresse: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GebyransvarligId):
            self.id = GebyransvarligId(self.id)

        if self._is_empty(self.gebyransvarligType):
            self.MissingRequiredField("gebyransvarligType")
        if not isinstance(self.gebyransvarligType, GebyransvarligType):
            self.gebyransvarligType = GebyransvarligType(self.gebyransvarligType)

        if self.eksternFakturareferanse is not None and not isinstance(self.eksternFakturareferanse, str):
            self.eksternFakturareferanse = str(self.eksternFakturareferanse)

        if self.virksomhet is not None and not isinstance(self.virksomhet, VirksomhetId):
            self.virksomhet = VirksomhetId(self.virksomhet)

        if self.person is not None and not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

        if self.mobilnummer is not None and not isinstance(self.mobilnummer, MobilnummerId):
            self.mobilnummer = MobilnummerId(self.mobilnummer)

        if self.e_postadresse is not None and not isinstance(self.e_postadresse, str):
            self.e_postadresse = str(self.e_postadresse)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneratedContainer(YAMLRoot):
    """
    TODO: beskriv containerklassen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERATED["GeneratedContainer"]
    class_class_curie: ClassVar[str] = "generated:GeneratedContainer"
    class_name: ClassVar[str] = "GeneratedContainer"
    class_model_uri: ClassVar[URIRef] = GENERATED.GeneratedContainer

    innrapporteringer: Optional[Union[dict[Union[str, InnrapporteringId], Union[dict, Innrapportering]], list[Union[dict, Innrapportering]]]] = empty_dict()
    virksomhetsinformasjonHovedenheter: Optional[Union[dict[Union[str, VirksomhetsinformasjonHovedenhetId], Union[dict, VirksomhetsinformasjonHovedenhet]], list[Union[dict, VirksomhetsinformasjonHovedenhet]]]] = empty_dict()
    forretningsadresseer: Optional[Union[dict[Union[str, ForretningsadresseId], Union[dict, Forretningsadresse]], list[Union[dict, Forretningsadresse]]]] = empty_dict()
    stedsadresseer: Optional[Union[dict[Union[str, StedsadresseId], Union[dict, Stedsadresse]], list[Union[dict, Stedsadresse]]]] = empty_dict()
    vegadresseer: Optional[Union[dict[Union[str, VegadresseId], Union[dict, Vegadresse]], list[Union[dict, Vegadresse]]]] = empty_dict()
    adressenummerer: Optional[Union[dict[Union[str, AdressenummerId], Union[dict, Adressenummer]], list[Union[dict, Adressenummer]]]] = empty_dict()
    varslingsadresseer: Optional[Union[dict[Union[str, VarslingsadresseId], Union[dict, Varslingsadresse]], list[Union[dict, Varslingsadresse]]]] = empty_dict()
    mobilnummerer: Optional[Union[dict[Union[str, MobilnummerId], Union[dict, Mobilnummer]], list[Union[dict, Mobilnummer]]]] = empty_dict()
    postadresseer: Optional[Union[dict[Union[str, PostadresseId], Union[dict, Postadresse]], list[Union[dict, Postadresse]]]] = empty_dict()
    postboksadresseer: Optional[Union[dict[Union[str, PostboksadresseId], Union[dict, Postboksadresse]], list[Union[dict, Postboksadresse]]]] = empty_dict()
    internasjonalAdresseer: Optional[Union[dict[Union[str, InternasjonalAdresseId], Union[dict, InternasjonalAdresse]], list[Union[dict, InternasjonalAdresse]]]] = empty_dict()
    kontaktopplysninger: Optional[Union[dict[Union[str, KontaktopplysningId], Union[dict, Kontaktopplysning]], list[Union[dict, Kontaktopplysning]]]] = empty_dict()
    telefonnummerer: Optional[Union[dict[Union[str, TelefonnummerId], Union[dict, Telefonnummer]], list[Union[dict, Telefonnummer]]]] = empty_dict()
    virksomhetsinformasjonUnderenheter: Optional[Union[dict[Union[str, VirksomhetsinformasjonUnderenhetId], Union[dict, VirksomhetsinformasjonUnderenhet]], list[Union[dict, VirksomhetsinformasjonUnderenhet]]]] = empty_dict()
    beliggenhetsadresseer: Optional[Union[dict[Union[str, BeliggenhetsadresseId], Union[dict, Beliggenhetsadresse]], list[Union[dict, Beliggenhetsadresse]]]] = empty_dict()
    aktiviteter: Optional[Union[dict[Union[str, AktivitetId], Union[dict, Aktivitet]], list[Union[dict, Aktivitet]]]] = empty_dict()
    typeAktiviteter: Optional[Union[dict[Union[str, TypeAktivitetId], Union[dict, TypeAktivitet]], list[Union[dict, TypeAktivitet]]]] = empty_dict()
    omdanninger: Optional[Union[dict[Union[str, OmdanningId], Union[dict, Omdanning]], list[Union[dict, Omdanning]]]] = empty_dict()
    rolletypegruppeer: Optional[Union[dict[Union[str, RolletypegruppeId], Union[dict, Rolletypegruppe]], list[Union[dict, Rolletypegruppe]]]] = empty_dict()
    rolleer: Optional[Union[dict[Union[str, RolleId], Union[dict, Rolle]], list[Union[dict, Rolle]]]] = empty_dict()
    rolleinnehaverer: Optional[Union[dict[Union[str, RolleinnehaverId], Union[dict, Rolleinnehaver]], list[Union[dict, Rolleinnehaver]]]] = empty_dict()
    ansvarsandeler: Optional[Union[dict[Union[str, AnsvarsandelId], Union[dict, Ansvarsandel]], list[Union[dict, Ansvarsandel]]]] = empty_dict()
    broeker: Optional[Union[dict[Union[str, BroekId], Union[dict, Broek]], list[Union[dict, Broek]]]] = empty_dict()
    virksomheter: Optional[Union[dict[Union[str, VirksomhetId], Union[dict, Virksomhet]], list[Union[dict, Virksomhet]]]] = empty_dict()
    personer: Optional[Union[dict[Union[str, PersonId], Union[dict, Person]], list[Union[dict, Person]]]] = empty_dict()
    prokuraer: Optional[Union[dict[Union[str, ProkuraId], Union[dict, Prokura]], list[Union[dict, Prokura]]]] = empty_dict()
    prokurabestemmelseer: Optional[Union[dict[Union[str, ProkurabestemmelseId], Union[dict, Prokurabestemmelse]], list[Union[dict, Prokurabestemmelse]]]] = empty_dict()
    rollesetter: Optional[Union[dict[Union[str, RollesettId], Union[dict, Rollesett]], list[Union[dict, Rollesett]]]] = empty_dict()
    signaturberettigetEllerProkurister: Optional[Union[dict[Union[str, SignaturberettigetEllerProkuristId], Union[dict, SignaturberettigetEllerProkurist]], list[Union[dict, SignaturberettigetEllerProkurist]]]] = empty_dict()
    signaturretter: Optional[Union[dict[Union[str, SignaturrettId], Union[dict, Signaturrett]], list[Union[dict, Signaturrett]]]] = empty_dict()
    signaturrettsbestemmelseer: Optional[Union[dict[Union[str, SignaturrettsbestemmelseId], Union[dict, Signaturrettsbestemmelse]], list[Union[dict, Signaturrettsbestemmelse]]]] = empty_dict()
    foretaksinformasjoner: Optional[Union[dict[Union[str, ForetaksinformasjonId], Union[dict, Foretaksinformasjon]], list[Union[dict, Foretaksinformasjon]]]] = empty_dict()
    eierskifteAktiviteter: Optional[Union[dict[Union[str, EierskifteAktivitetId], Union[dict, EierskifteAktivitet]], list[Union[dict, EierskifteAktivitet]]]] = empty_dict()
    delerEierskifteer: Optional[Union[dict[Union[str, DelerEierskifteId], Union[dict, DelerEierskifte]], list[Union[dict, DelerEierskifte]]]] = empty_dict()
    matrikkelnummerer: Optional[Union[dict[Union[str, MatrikkelnummerId], Union[dict, Matrikkelnummer]], list[Union[dict, Matrikkelnummer]]]] = empty_dict()
    innsenderer: Optional[Union[dict[Union[str, InnsenderId], Union[dict, Innsender]], list[Union[dict, Innsender]]]] = empty_dict()
    fagsystemreferanseer: Optional[Union[dict[Union[str, FagsystemreferanseId], Union[dict, Fagsystemreferanse]], list[Union[dict, Fagsystemreferanse]]]] = empty_dict()
    signeringer: Optional[Union[list[Union[str, SigneringId]], dict[Union[str, SigneringId], Union[dict, Signering]]]] = empty_dict()
    gebyransvarliger: Optional[Union[dict[Union[str, GebyransvarligId], Union[dict, Gebyransvarlig]], list[Union[dict, Gebyransvarlig]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="innrapporteringer", slot_type=Innrapportering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="virksomhetsinformasjonHovedenheter", slot_type=VirksomhetsinformasjonHovedenhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="forretningsadresseer", slot_type=Forretningsadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="stedsadresseer", slot_type=Stedsadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="vegadresseer", slot_type=Vegadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="adressenummerer", slot_type=Adressenummer, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="varslingsadresseer", slot_type=Varslingsadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="mobilnummerer", slot_type=Mobilnummer, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="postadresseer", slot_type=Postadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="postboksadresseer", slot_type=Postboksadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="internasjonalAdresseer", slot_type=InternasjonalAdresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="kontaktopplysninger", slot_type=Kontaktopplysning, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="telefonnummerer", slot_type=Telefonnummer, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="virksomhetsinformasjonUnderenheter", slot_type=VirksomhetsinformasjonUnderenhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="beliggenhetsadresseer", slot_type=Beliggenhetsadresse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aktiviteter", slot_type=Aktivitet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="typeAktiviteter", slot_type=TypeAktivitet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="omdanninger", slot_type=Omdanning, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rolletypegruppeer", slot_type=Rolletypegruppe, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rolleer", slot_type=Rolle, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rolleinnehaverer", slot_type=Rolleinnehaver, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ansvarsandeler", slot_type=Ansvarsandel, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="broeker", slot_type=Broek, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="virksomheter", slot_type=Virksomhet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="personer", slot_type=Person, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="prokuraer", slot_type=Prokura, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="prokurabestemmelseer", slot_type=Prokurabestemmelse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="rollesetter", slot_type=Rollesett, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="signaturberettigetEllerProkurister", slot_type=SignaturberettigetEllerProkurist, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="signaturretter", slot_type=Signaturrett, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="signaturrettsbestemmelseer", slot_type=Signaturrettsbestemmelse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="foretaksinformasjoner", slot_type=Foretaksinformasjon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="eierskifteAktiviteter", slot_type=EierskifteAktivitet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="delerEierskifteer", slot_type=DelerEierskifte, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="matrikkelnummerer", slot_type=Matrikkelnummer, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="innsenderer", slot_type=Innsender, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fagsystemreferanseer", slot_type=Fagsystemreferanse, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="signeringer", slot_type=Signering, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="gebyransvarliger", slot_type=Gebyransvarlig, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class Maalform(EnumDefinitionImpl):
    """
    TODO: beskriv enumet
    """
    nob = PermissibleValue(text="nob")
    nno = PermissibleValue(text="nno")

    _defn = EnumDefinition(
        name="Maalform",
        description="TODO: beskriv enumet",
    )

class Rolletype(EnumDefinitionImpl):
    """
    TODO: beskriv enumet
    """
    _defn = EnumDefinition(
        name="Rolletype",
        description="TODO: beskriv enumet",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "rolletype.dagligLeder",
            PermissibleValue(text="rolletype.dagligLeder"))
        setattr(cls, "rolletype.revisor",
            PermissibleValue(text="rolletype.revisor"))
        setattr(cls, "rolletype.prokurist",
            PermissibleValue(text="rolletype.prokurist"))
        setattr(cls, "rolletype.signaturberettiget",
            PermissibleValue(text="rolletype.signaturberettiget"))
        setattr(cls, "rolletype.forretningsfoerer",
            PermissibleValue(text="rolletype.forretningsfoerer"))
        setattr(cls, "rolletype.regnskapsfoerer",
            PermissibleValue(text="rolletype.regnskapsfoerer"))
        setattr(cls, "rolletype.innehaver",
            PermissibleValue(text="rolletype.innehaver"))
        setattr(cls, "rolletype.bostyrer",
            PermissibleValue(text="rolletype.bostyrer"))
        setattr(cls, "rolletype.kontaktperson",
            PermissibleValue(text="rolletype.kontaktperson"))
        setattr(cls, "rolletype.styreleder",
            PermissibleValue(text="rolletype.styreleder"))
        setattr(cls, "rolletype.nestleder",
            PermissibleValue(text="rolletype.nestleder"))
        setattr(cls, "rolletype.styremedlem",
            PermissibleValue(text="rolletype.styremedlem"))
        setattr(cls, "rolletype.varamedlem",
            PermissibleValue(text="rolletype.varamedlem"))
        setattr(cls, "rolletype.observatoer",
            PermissibleValue(text="rolletype.observatoer"))

class TypeEierskifte(EnumDefinitionImpl):
    """
    TODO: beskriv enumet
    """
    overtakelse = PermissibleValue(text="overtakelse")
    overdragelse = PermissibleValue(text="overdragelse")

    _defn = EnumDefinition(
        name="TypeEierskifte",
        description="TODO: beskriv enumet",
    )

class GebyransvarligType(EnumDefinitionImpl):
    """
    TODO: beskriv enumet
    """
    virksomhetenSelv = PermissibleValue(text="virksomhetenSelv")
    person = PermissibleValue(text="person")
    virksomhet = PermissibleValue(text="virksomhet")

    _defn = EnumDefinition(
        name="GebyransvarligType",
        description="TODO: beskriv enumet",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=GENERATED.id, name="id", curie=GENERATED.curie('id'),
                   model_uri=GENERATED.id, domain=None, range=URIRef)

slots.versjon = Slot(uri=GENERATED.versjon, name="versjon", curie=GENERATED.curie('versjon'),
                   model_uri=GENERATED.versjon, domain=None, range=Optional[str])

slots.innsendertjenste = Slot(uri=GENERATED.innsendertjenste, name="innsendertjenste", curie=GENERATED.curie('innsendertjenste'),
                   model_uri=GENERATED.innsendertjenste, domain=None, range=Optional[str])

slots.innsendingstidspunkt = Slot(uri=GENERATED.innsendingstidspunkt, name="innsendingstidspunkt", curie=GENERATED.curie('innsendingstidspunkt'),
                   model_uri=GENERATED.innsendingstidspunkt, domain=None, range=Optional[str])

slots.maalformForTilbakemelding = Slot(uri=GENERATED.maalformForTilbakemelding, name="maalformForTilbakemelding", curie=GENERATED.curie('maalformForTilbakemelding'),
                   model_uri=GENERATED.maalformForTilbakemelding, domain=None, range=Optional[Union[str, "Maalform"]])

slots.tjenestevariant = Slot(uri=GENERATED.tjenestevariant, name="tjenestevariant", curie=GENERATED.curie('tjenestevariant'),
                   model_uri=GENERATED.tjenestevariant, domain=None, range=Optional[str])

slots.virksomhetsinformasjon = Slot(uri=GENERATED.virksomhetsinformasjon, name="virksomhetsinformasjon", curie=GENERATED.curie('virksomhetsinformasjon'),
                   model_uri=GENERATED.virksomhetsinformasjon, domain=None, range=Optional[Union[str, VirksomhetsinformasjonHovedenhetId]])

slots.innsender = Slot(uri=GENERATED.innsender, name="innsender", curie=GENERATED.curie('innsender'),
                   model_uri=GENERATED.innsender, domain=None, range=Optional[Union[str, InnsenderId]])

slots.fagsystemReferanse = Slot(uri=GENERATED.fagsystemReferanse, name="fagsystemReferanse", curie=GENERATED.curie('fagsystemReferanse'),
                   model_uri=GENERATED.fagsystemReferanse, domain=None, range=Optional[Union[str, FagsystemreferanseId]])

slots.signering = Slot(uri=GENERATED.signering, name="signering", curie=GENERATED.curie('signering'),
                   model_uri=GENERATED.signering, domain=None, range=Optional[Union[str, SigneringId]])

slots.gebyransvarlig = Slot(uri=GENERATED.gebyransvarlig, name="gebyransvarlig", curie=GENERATED.curie('gebyransvarlig'),
                   model_uri=GENERATED.gebyransvarlig, domain=None, range=Optional[Union[str, GebyransvarligId]])

slots.lenkeForEttersending = Slot(uri=GENERATED.lenkeForEttersending, name="lenkeForEttersending", curie=GENERATED.curie('lenkeForEttersending'),
                   model_uri=GENERATED.lenkeForEttersending, domain=None, range=Optional[str])

slots.organisasjonsform = Slot(uri=GENERATED.organisasjonsform, name="organisasjonsform", curie=GENERATED.curie('organisasjonsform'),
                   model_uri=GENERATED.organisasjonsform, domain=None, range=Optional[str])

slots.virksomhetstype = Slot(uri=GENERATED.virksomhetstype, name="virksomhetstype", curie=GENERATED.curie('virksomhetstype'),
                   model_uri=GENERATED.virksomhetstype, domain=None, range=Optional[str])

slots.organisasjonsnummer = Slot(uri=GENERATED.organisasjonsnummer, name="organisasjonsnummer", curie=GENERATED.curie('organisasjonsnummer'),
                   model_uri=GENERATED.organisasjonsnummer, domain=None, range=Optional[str])

slots.navn = Slot(uri=GENERATED.navn, name="navn", curie=GENERATED.curie('navn'),
                   model_uri=GENERATED.navn, domain=None, range=Optional[str])

slots.maalform = Slot(uri=GENERATED.maalform, name="maalform", curie=GENERATED.curie('maalform'),
                   model_uri=GENERATED.maalform, domain=None, range=Optional[Union[str, "Maalform"]])

slots.oppfyllerKravTilNaeringsvirksomhet = Slot(uri=GENERATED.oppfyllerKravTilNaeringsvirksomhet, name="oppfyllerKravTilNaeringsvirksomhet", curie=GENERATED.curie('oppfyllerKravTilNaeringsvirksomhet'),
                   model_uri=GENERATED.oppfyllerKravTilNaeringsvirksomhet, domain=None, range=Optional[Union[bool, Bool]])

slots.venterAAFaaAnsatte = Slot(uri=GENERATED.venterAAFaaAnsatte, name="venterAAFaaAnsatte", curie=GENERATED.curie('venterAAFaaAnsatte'),
                   model_uri=GENERATED.venterAAFaaAnsatte, domain=None, range=Optional[Union[bool, Bool]])

slots.datoForAvtale = Slot(uri=GENERATED.datoForAvtale, name="datoForAvtale", curie=GENERATED.curie('datoForAvtale'),
                   model_uri=GENERATED.datoForAvtale, domain=None, range=Optional[str])

slots.stiftelsesdato = Slot(uri=GENERATED.stiftelsesdato, name="stiftelsesdato", curie=GENERATED.curie('stiftelsesdato'),
                   model_uri=GENERATED.stiftelsesdato, domain=None, range=Optional[str])

slots.vedtektsdato = Slot(uri=GENERATED.vedtektsdato, name="vedtektsdato", curie=GENERATED.curie('vedtektsdato'),
                   model_uri=GENERATED.vedtektsdato, domain=None, range=Optional[str])

slots.formaal = Slot(uri=GENERATED.formaal, name="formaal", curie=GENERATED.curie('formaal'),
                   model_uri=GENERATED.formaal, domain=None, range=Optional[str])

slots.harAnsvarsbegrensning = Slot(uri=GENERATED.harAnsvarsbegrensning, name="harAnsvarsbegrensning", curie=GENERATED.curie('harAnsvarsbegrensning'),
                   model_uri=GENERATED.harAnsvarsbegrensning, domain=None, range=Optional[Union[bool, Bool]])

slots.ansvarsform = Slot(uri=GENERATED.ansvarsform, name="ansvarsform", curie=GENERATED.curie('ansvarsform'),
                   model_uri=GENERATED.ansvarsform, domain=None, range=Optional[str])

slots.forretningsadresse = Slot(uri=GENERATED.forretningsadresse, name="forretningsadresse", curie=GENERATED.curie('forretningsadresse'),
                   model_uri=GENERATED.forretningsadresse, domain=None, range=Optional[Union[str, ForretningsadresseId]])

slots.varslingsadresse = Slot(uri=GENERATED.varslingsadresse, name="varslingsadresse", curie=GENERATED.curie('varslingsadresse'),
                   model_uri=GENERATED.varslingsadresse, domain=None, range=Optional[Union[str, VarslingsadresseId]])

slots.postadresse = Slot(uri=GENERATED.postadresse, name="postadresse", curie=GENERATED.curie('postadresse'),
                   model_uri=GENERATED.postadresse, domain=None, range=Optional[Union[str, PostadresseId]])

slots.kontaktopplysning = Slot(uri=GENERATED.kontaktopplysning, name="kontaktopplysning", curie=GENERATED.curie('kontaktopplysning'),
                   model_uri=GENERATED.kontaktopplysning, domain=None, range=Optional[Union[str, KontaktopplysningId]])

slots.virksomhetsinformasjonUnderenhet = Slot(uri=GENERATED.virksomhetsinformasjonUnderenhet, name="virksomhetsinformasjonUnderenhet", curie=GENERATED.curie('virksomhetsinformasjonUnderenhet'),
                   model_uri=GENERATED.virksomhetsinformasjonUnderenhet, domain=None, range=Optional[Union[Union[str, VirksomhetsinformasjonUnderenhetId], list[Union[str, VirksomhetsinformasjonUnderenhetId]]]])

slots.aktivitet = Slot(uri=GENERATED.aktivitet, name="aktivitet", curie=GENERATED.curie('aktivitet'),
                   model_uri=GENERATED.aktivitet, domain=None, range=Optional[Union[str, AktivitetId]])

slots.omdanning = Slot(uri=GENERATED.omdanning, name="omdanning", curie=GENERATED.curie('omdanning'),
                   model_uri=GENERATED.omdanning, domain=None, range=Optional[Union[str, OmdanningId]])

slots.rolletypegruppe = Slot(uri=GENERATED.rolletypegruppe, name="rolletypegruppe", curie=GENERATED.curie('rolletypegruppe'),
                   model_uri=GENERATED.rolletypegruppe, domain=None, range=Optional[Union[Union[str, RolletypegruppeId], list[Union[str, RolletypegruppeId]]]])

slots.prokura = Slot(uri=GENERATED.prokura, name="prokura", curie=GENERATED.curie('prokura'),
                   model_uri=GENERATED.prokura, domain=None, range=Optional[Union[str, ProkuraId]])

slots.signaturrett = Slot(uri=GENERATED.signaturrett, name="signaturrett", curie=GENERATED.curie('signaturrett'),
                   model_uri=GENERATED.signaturrett, domain=None, range=Optional[Union[str, SignaturrettId]])

slots.meldtOpploesning = Slot(uri=GENERATED.meldtOpploesning, name="meldtOpploesning", curie=GENERATED.curie('meldtOpploesning'),
                   model_uri=GENERATED.meldtOpploesning, domain=None, range=Optional[Union[bool, Bool]])

slots.meldtOmgjoeringAvOpploesning = Slot(uri=GENERATED.meldtOmgjoeringAvOpploesning, name="meldtOmgjoeringAvOpploesning", curie=GENERATED.curie('meldtOmgjoeringAvOpploesning'),
                   model_uri=GENERATED.meldtOmgjoeringAvOpploesning, domain=None, range=Optional[Union[bool, Bool]])

slots.foretaksinformasjon = Slot(uri=GENERATED.foretaksinformasjon, name="foretaksinformasjon", curie=GENERATED.curie('foretaksinformasjon'),
                   model_uri=GENERATED.foretaksinformasjon, domain=None, range=Optional[Union[str, ForetaksinformasjonId]])

slots.eierskifte = Slot(uri=GENERATED.eierskifte, name="eierskifte", curie=GENERATED.curie('eierskifte'),
                   model_uri=GENERATED.eierskifte, domain=None, range=Optional[Union[Union[str, EierskifteAktivitetId], list[Union[str, EierskifteAktivitetId]]]])

slots.bekreftelseProtokollSletting = Slot(uri=GENERATED.bekreftelseProtokollSletting, name="bekreftelseProtokollSletting", curie=GENERATED.curie('bekreftelseProtokollSletting'),
                   model_uri=GENERATED.bekreftelseProtokollSletting, domain=None, range=Optional[Union[bool, Bool]])

slots.matrikkelnummer = Slot(uri=GENERATED.matrikkelnummer, name="matrikkelnummer", curie=GENERATED.curie('matrikkelnummer'),
                   model_uri=GENERATED.matrikkelnummer, domain=None, range=Optional[Union[Union[str, MatrikkelnummerId], list[Union[str, MatrikkelnummerId]]]])

slots.registrertITilknyttetRegister = Slot(uri=GENERATED.registrertITilknyttetRegister, name="registrertITilknyttetRegister", curie=GENERATED.curie('registrertITilknyttetRegister'),
                   model_uri=GENERATED.registrertITilknyttetRegister, domain=None, range=Optional[Union[str, list[str]]])

slots.bekreftelseProtokollOpploesningOgOmgjoering = Slot(uri=GENERATED.bekreftelseProtokollOpploesningOgOmgjoering, name="bekreftelseProtokollOpploesningOgOmgjoering", curie=GENERATED.curie('bekreftelseProtokollOpploesningOgOmgjoering'),
                   model_uri=GENERATED.bekreftelseProtokollOpploesningOgOmgjoering, domain=None, range=Optional[Union[bool, Bool]])

slots.coNavn = Slot(uri=GENERATED.coNavn, name="coNavn", curie=GENERATED.curie('coNavn'),
                   model_uri=GENERATED.coNavn, domain=None, range=Optional[str])

slots.vNavn = Slot(uri=GENERATED.vNavn, name="vNavn", curie=GENERATED.curie('vNavn'),
                   model_uri=GENERATED.vNavn, domain=None, range=Optional[str])

slots.utgaar = Slot(uri=GENERATED.utgaar, name="utgaar", curie=GENERATED.curie('utgaar'),
                   model_uri=GENERATED.utgaar, domain=None, range=Optional[Union[bool, Bool]])

slots.stedsadresse = Slot(uri=GENERATED.stedsadresse, name="stedsadresse", curie=GENERATED.curie('stedsadresse'),
                   model_uri=GENERATED.stedsadresse, domain=None, range=Optional[Union[str, StedsadresseId]])

slots.vegadresse = Slot(uri=GENERATED.vegadresse, name="vegadresse", curie=GENERATED.curie('vegadresse'),
                   model_uri=GENERATED.vegadresse, domain=None, range=Optional[Union[str, VegadresseId]])

slots.stedsnavn = Slot(uri=GENERATED.stedsnavn, name="stedsnavn", curie=GENERATED.curie('stedsnavn'),
                   model_uri=GENERATED.stedsnavn, domain=None, range=Optional[str])

slots.kommunenummer = Slot(uri=GENERATED.kommunenummer, name="kommunenummer", curie=GENERATED.curie('kommunenummer'),
                   model_uri=GENERATED.kommunenummer, domain=None, range=Optional[str])

slots.postnummer = Slot(uri=GENERATED.postnummer, name="postnummer", curie=GENERATED.curie('postnummer'),
                   model_uri=GENERATED.postnummer, domain=None, range=Optional[str])

slots.vegadresseId = Slot(uri=GENERATED.vegadresseId, name="vegadresseId", curie=GENERATED.curie('vegadresseId'),
                   model_uri=GENERATED.vegadresseId, domain=None, range=Optional[str])

slots.adressenavn = Slot(uri=GENERATED.adressenavn, name="adressenavn", curie=GENERATED.curie('adressenavn'),
                   model_uri=GENERATED.adressenavn, domain=None, range=Optional[str])

slots.bruksenhetsnummer = Slot(uri=GENERATED.bruksenhetsnummer, name="bruksenhetsnummer", curie=GENERATED.curie('bruksenhetsnummer'),
                   model_uri=GENERATED.bruksenhetsnummer, domain=None, range=Optional[str])

slots.nummer = Slot(uri=GENERATED.nummer, name="nummer", curie=GENERATED.curie('nummer'),
                   model_uri=GENERATED.nummer, domain=None, range=Optional[Union[str, AdressenummerId]])

slots.adressetilleggsnavn = Slot(uri=GENERATED.adressetilleggsnavn, name="adressetilleggsnavn", curie=GENERATED.curie('adressetilleggsnavn'),
                   model_uri=GENERATED.adressetilleggsnavn, domain=None, range=Optional[str])

slots.bokstav = Slot(uri=GENERATED.bokstav, name="bokstav", curie=GENERATED.curie('bokstav'),
                   model_uri=GENERATED.bokstav, domain=None, range=Optional[str])

slots.mobilnummer = Slot(uri=GENERATED.mobilnummer, name="mobilnummer", curie=GENERATED.curie('mobilnummer'),
                   model_uri=GENERATED.mobilnummer, domain=None, range=Optional[Union[str, MobilnummerId]])

slots.e_postadresse = Slot(uri=GENERATED.e_postadresse, name="e_postadresse", curie=GENERATED.curie('e_postadresse'),
                   model_uri=GENERATED.e_postadresse, domain=None, range=Optional[str])

slots.internasjonaltPrefiks = Slot(uri=GENERATED.internasjonaltPrefiks, name="internasjonaltPrefiks", curie=GENERATED.curie('internasjonaltPrefiks'),
                   model_uri=GENERATED.internasjonaltPrefiks, domain=None, range=Optional[str])

slots.nasjonaltNummer = Slot(uri=GENERATED.nasjonaltNummer, name="nasjonaltNummer", curie=GENERATED.curie('nasjonaltNummer'),
                   model_uri=GENERATED.nasjonaltNummer, domain=None, range=Optional[str])

slots.postboksadresse = Slot(uri=GENERATED.postboksadresse, name="postboksadresse", curie=GENERATED.curie('postboksadresse'),
                   model_uri=GENERATED.postboksadresse, domain=None, range=Optional[Union[str, PostboksadresseId]])

slots.internasjonalAdresse = Slot(uri=GENERATED.internasjonalAdresse, name="internasjonalAdresse", curie=GENERATED.curie('internasjonalAdresse'),
                   model_uri=GENERATED.internasjonalAdresse, domain=None, range=Optional[Union[str, InternasjonalAdresseId]])

slots.postboksnummer = Slot(uri=GENERATED.postboksnummer, name="postboksnummer", curie=GENERATED.curie('postboksnummer'),
                   model_uri=GENERATED.postboksnummer, domain=None, range=Optional[str])

slots.postboksanleggsnavn = Slot(uri=GENERATED.postboksanleggsnavn, name="postboksanleggsnavn", curie=GENERATED.curie('postboksanleggsnavn'),
                   model_uri=GENERATED.postboksanleggsnavn, domain=None, range=Optional[str])

slots.adressenummer = Slot(uri=GENERATED.adressenummer, name="adressenummer", curie=GENERATED.curie('adressenummer'),
                   model_uri=GENERATED.adressenummer, domain=None, range=Optional[str])

slots.bygning = Slot(uri=GENERATED.bygning, name="bygning", curie=GENERATED.curie('bygning'),
                   model_uri=GENERATED.bygning, domain=None, range=Optional[str])

slots.etasjenummer = Slot(uri=GENERATED.etasjenummer, name="etasjenummer", curie=GENERATED.curie('etasjenummer'),
                   model_uri=GENERATED.etasjenummer, domain=None, range=Optional[str])

slots.boenhet = Slot(uri=GENERATED.boenhet, name="boenhet", curie=GENERATED.curie('boenhet'),
                   model_uri=GENERATED.boenhet, domain=None, range=Optional[str])

slots.postboks = Slot(uri=GENERATED.postboks, name="postboks", curie=GENERATED.curie('postboks'),
                   model_uri=GENERATED.postboks, domain=None, range=Optional[str])

slots.postkode = Slot(uri=GENERATED.postkode, name="postkode", curie=GENERATED.curie('postkode'),
                   model_uri=GENERATED.postkode, domain=None, range=Optional[str])

slots.byEllerStedsnavn = Slot(uri=GENERATED.byEllerStedsnavn, name="byEllerStedsnavn", curie=GENERATED.curie('byEllerStedsnavn'),
                   model_uri=GENERATED.byEllerStedsnavn, domain=None, range=Optional[str])

slots.region = Slot(uri=GENERATED.region, name="region", curie=GENERATED.curie('region'),
                   model_uri=GENERATED.region, domain=None, range=Optional[str])

slots.distriktEllerBydel = Slot(uri=GENERATED.distriktEllerBydel, name="distriktEllerBydel", curie=GENERATED.curie('distriktEllerBydel'),
                   model_uri=GENERATED.distriktEllerBydel, domain=None, range=Optional[str])

slots.friAdressetekst = Slot(uri=GENERATED.friAdressetekst, name="friAdressetekst", curie=GENERATED.curie('friAdressetekst'),
                   model_uri=GENERATED.friAdressetekst, domain=None, range=Optional[Union[str, list[str]]])

slots.adresseidentifikator = Slot(uri=GENERATED.adresseidentifikator, name="adresseidentifikator", curie=GENERATED.curie('adresseidentifikator'),
                   model_uri=GENERATED.adresseidentifikator, domain=None, range=Optional[str])

slots.landkode = Slot(uri=GENERATED.landkode, name="landkode", curie=GENERATED.curie('landkode'),
                   model_uri=GENERATED.landkode, domain=None, range=Optional[str])

slots.nettadresse = Slot(uri=GENERATED.nettadresse, name="nettadresse", curie=GENERATED.curie('nettadresse'),
                   model_uri=GENERATED.nettadresse, domain=None, range=Optional[str])

slots.mobilnummerUtgaar = Slot(uri=GENERATED.mobilnummerUtgaar, name="mobilnummerUtgaar", curie=GENERATED.curie('mobilnummerUtgaar'),
                   model_uri=GENERATED.mobilnummerUtgaar, domain=None, range=Optional[Union[bool, Bool]])

slots.e_postadresseUtgaar = Slot(uri=GENERATED.e_postadresseUtgaar, name="e_postadresseUtgaar", curie=GENERATED.curie('e_postadresseUtgaar'),
                   model_uri=GENERATED.e_postadresseUtgaar, domain=None, range=Optional[Union[bool, Bool]])

slots.nettadresseUtgaar = Slot(uri=GENERATED.nettadresseUtgaar, name="nettadresseUtgaar", curie=GENERATED.curie('nettadresseUtgaar'),
                   model_uri=GENERATED.nettadresseUtgaar, domain=None, range=Optional[Union[bool, Bool]])

slots.telefonnummer = Slot(uri=GENERATED.telefonnummer, name="telefonnummer", curie=GENERATED.curie('telefonnummer'),
                   model_uri=GENERATED.telefonnummer, domain=None, range=Optional[Union[str, TelefonnummerId]])

slots.telefonnummerUtgaar = Slot(uri=GENERATED.telefonnummerUtgaar, name="telefonnummerUtgaar", curie=GENERATED.curie('telefonnummerUtgaar'),
                   model_uri=GENERATED.telefonnummerUtgaar, domain=None, range=Optional[Union[bool, Bool]])

slots.oppstartsdato = Slot(uri=GENERATED.oppstartsdato, name="oppstartsdato", curie=GENERATED.curie('oppstartsdato'),
                   model_uri=GENERATED.oppstartsdato, domain=None, range=Optional[str])

slots.nedleggelsesdato = Slot(uri=GENERATED.nedleggelsesdato, name="nedleggelsesdato", curie=GENERATED.curie('nedleggelsesdato'),
                   model_uri=GENERATED.nedleggelsesdato, domain=None, range=Optional[str])

slots.beliggenhetsadresse = Slot(uri=GENERATED.beliggenhetsadresse, name="beliggenhetsadresse", curie=GENERATED.curie('beliggenhetsadresse'),
                   model_uri=GENERATED.beliggenhetsadresse, domain=None, range=Optional[Union[str, BeliggenhetsadresseId]])

slots.datoGyldigFra = Slot(uri=GENERATED.datoGyldigFra, name="datoGyldigFra", curie=GENERATED.curie('datoGyldigFra'),
                   model_uri=GENERATED.datoGyldigFra, domain=None, range=Optional[str])

slots.rekkefoelge = Slot(uri=GENERATED.rekkefoelge, name="rekkefoelge", curie=GENERATED.curie('rekkefoelge'),
                   model_uri=GENERATED.rekkefoelge, domain=None, range=Optional[int])

slots.aktivitetskode = Slot(uri=GENERATED.aktivitetskode, name="aktivitetskode", curie=GENERATED.curie('aktivitetskode'),
                   model_uri=GENERATED.aktivitetskode, domain=None, range=Optional[int])

slots.tekst = Slot(uri=GENERATED.tekst, name="tekst", curie=GENERATED.curie('tekst'),
                   model_uri=GENERATED.tekst, domain=None, range=Optional[str])

slots.nyOrganisasjonsform = Slot(uri=GENERATED.nyOrganisasjonsform, name="nyOrganisasjonsform", curie=GENERATED.curie('nyOrganisasjonsform'),
                   model_uri=GENERATED.nyOrganisasjonsform, domain=None, range=Optional[str])

slots.rollegruppe = Slot(uri=GENERATED.rollegruppe, name="rollegruppe", curie=GENERATED.curie('rollegruppe'),
                   model_uri=GENERATED.rollegruppe, domain=None, range=Optional[str])

slots.kjoennssammensetningAnsattvalgte = Slot(uri=GENERATED.kjoennssammensetningAnsattvalgte, name="kjoennssammensetningAnsattvalgte", curie=GENERATED.curie('kjoennssammensetningAnsattvalgte'),
                   model_uri=GENERATED.kjoennssammensetningAnsattvalgte, domain=None, range=Optional[Union[bool, Bool]])

slots.kjoennssammensetningStyre = Slot(uri=GENERATED.kjoennssammensetningStyre, name="kjoennssammensetningStyre", curie=GENERATED.curie('kjoennssammensetningStyre'),
                   model_uri=GENERATED.kjoennssammensetningStyre, domain=None, range=Optional[Union[bool, Bool]])

slots.rolle = Slot(uri=GENERATED.rolle, name="rolle", curie=GENERATED.curie('rolle'),
                   model_uri=GENERATED.rolle, domain=None, range=Optional[Union[Union[str, RolleId], list[Union[str, RolleId]]]])

slots.bekreftelseProtokoll = Slot(uri=GENERATED.bekreftelseProtokoll, name="bekreftelseProtokoll", curie=GENERATED.curie('bekreftelseProtokoll'),
                   model_uri=GENERATED.bekreftelseProtokoll, domain=None, range=Optional[Union[bool, Bool]])

slots.rolletype = Slot(uri=GENERATED.rolletype, name="rolletype", curie=GENERATED.curie('rolletype'),
                   model_uri=GENERATED.rolletype, domain=None, range=Optional[Union[str, "Rolletype"]])

slots.tildelerAvRolle = Slot(uri=GENERATED.tildelerAvRolle, name="tildelerAvRolle", curie=GENERATED.curie('tildelerAvRolle'),
                   model_uri=GENERATED.tildelerAvRolle, domain=None, range=Optional[str])

slots.rolleinnehaver = Slot(uri=GENERATED.rolleinnehaver, name="rolleinnehaver", curie=GENERATED.curie('rolleinnehaver'),
                   model_uri=GENERATED.rolleinnehaver, domain=None, range=Optional[Union[str, RolleinnehaverId]])

slots.oenskerAAFratre = Slot(uri=GENERATED.oenskerAAFratre, name="oenskerAAFratre", curie=GENERATED.curie('oenskerAAFratre'),
                   model_uri=GENERATED.oenskerAAFratre, domain=None, range=Optional[Union[bool, Bool]])

slots.ansvarsandel = Slot(uri=GENERATED.ansvarsandel, name="ansvarsandel", curie=GENERATED.curie('ansvarsandel'),
                   model_uri=GENERATED.ansvarsandel, domain=None, range=Optional[Union[str, AnsvarsandelId]])

slots.avdelingskontor = Slot(uri=GENERATED.avdelingskontor, name="avdelingskontor", curie=GENERATED.curie('avdelingskontor'),
                   model_uri=GENERATED.avdelingskontor, domain=None, range=Optional[str])

slots.fratredenErVarslet = Slot(uri=GENERATED.fratredenErVarslet, name="fratredenErVarslet", curie=GENERATED.curie('fratredenErVarslet'),
                   model_uri=GENERATED.fratredenErVarslet, domain=None, range=Optional[Union[bool, Bool]])

slots.valgtAv = Slot(uri=GENERATED.valgtAv, name="valgtAv", curie=GENERATED.curie('valgtAv'),
                   model_uri=GENERATED.valgtAv, domain=None, range=Optional[str])

slots.virksomhet = Slot(uri=GENERATED.virksomhet, name="virksomhet", curie=GENERATED.curie('virksomhet'),
                   model_uri=GENERATED.virksomhet, domain=None, range=Optional[Union[str, VirksomhetId]])

slots.person = Slot(uri=GENERATED.person, name="person", curie=GENERATED.curie('person'),
                   model_uri=GENERATED.person, domain=None, range=Optional[Union[str, PersonId]])

slots.broek = Slot(uri=GENERATED.broek, name="broek", curie=GENERATED.curie('broek'),
                   model_uri=GENERATED.broek, domain=None, range=Optional[Union[str, BroekId]])

slots.prosent = Slot(uri=GENERATED.prosent, name="prosent", curie=GENERATED.curie('prosent'),
                   model_uri=GENERATED.prosent, domain=None, range=Optional[float])

slots.teller = Slot(uri=GENERATED.teller, name="teller", curie=GENERATED.curie('teller'),
                   model_uri=GENERATED.teller, domain=None, range=Optional[int])

slots.nevner = Slot(uri=GENERATED.nevner, name="nevner", curie=GENERATED.curie('nevner'),
                   model_uri=GENERATED.nevner, domain=None, range=Optional[int])

slots.virksomhetsidentifikator = Slot(uri=GENERATED.virksomhetsidentifikator, name="virksomhetsidentifikator", curie=GENERATED.curie('virksomhetsidentifikator'),
                   model_uri=GENERATED.virksomhetsidentifikator, domain=None, range=Optional[str])

slots.mappingId = Slot(uri=GENERATED.mappingId, name="mappingId", curie=GENERATED.curie('mappingId'),
                   model_uri=GENERATED.mappingId, domain=None, range=Optional[str])

slots.fulltNavn = Slot(uri=GENERATED.fulltNavn, name="fulltNavn", curie=GENERATED.curie('fulltNavn'),
                   model_uri=GENERATED.fulltNavn, domain=None, range=Optional[str])

slots.prokurabestemmelse = Slot(uri=GENERATED.prokurabestemmelse, name="prokurabestemmelse", curie=GENERATED.curie('prokurabestemmelse'),
                   model_uri=GENERATED.prokurabestemmelse, domain=None, range=Optional[Union[Union[str, ProkurabestemmelseId], list[Union[str, ProkurabestemmelseId]]]])

slots.regel = Slot(uri=GENERATED.regel, name="regel", curie=GENERATED.curie('regel'),
                   model_uri=GENERATED.regel, domain=None, range=Optional[str])

slots.rollesett = Slot(uri=GENERATED.rollesett, name="rollesett", curie=GENERATED.curie('rollesett'),
                   model_uri=GENERATED.rollesett, domain=None, range=Optional[Union[Union[str, RollesettId], list[Union[str, RollesettId]]]])

slots.signaturberettigetEllerProkurist = Slot(uri=GENERATED.signaturberettigetEllerProkurist, name="signaturberettigetEllerProkurist", curie=GENERATED.curie('signaturberettigetEllerProkurist'),
                   model_uri=GENERATED.signaturberettigetEllerProkurist, domain=None, range=Optional[Union[Union[str, SignaturberettigetEllerProkuristId], list[Union[str, SignaturberettigetEllerProkuristId]]]])

slots.minsteMengdeangivelse = Slot(uri=GENERATED.minsteMengdeangivelse, name="minsteMengdeangivelse", curie=GENERATED.curie('minsteMengdeangivelse'),
                   model_uri=GENERATED.minsteMengdeangivelse, domain=None, range=Optional[str])

slots.minsteAntall = Slot(uri=GENERATED.minsteAntall, name="minsteAntall", curie=GENERATED.curie('minsteAntall'),
                   model_uri=GENERATED.minsteAntall, domain=None, range=Optional[int])

slots.signaturrettsbestemmelsse = Slot(uri=GENERATED.signaturrettsbestemmelsse, name="signaturrettsbestemmelsse", curie=GENERATED.curie('signaturrettsbestemmelsse'),
                   model_uri=GENERATED.signaturrettsbestemmelsse, domain=None, range=Optional[Union[Union[str, SignaturrettsbestemmelseId], list[Union[str, SignaturrettsbestemmelseId]]]])

slots.oenskesRegistrertIForetaksregisteret = Slot(uri=GENERATED.oenskesRegistrertIForetaksregisteret, name="oenskesRegistrertIForetaksregisteret", curie=GENERATED.curie('oenskesRegistrertIForetaksregisteret'),
                   model_uri=GENERATED.oenskesRegistrertIForetaksregisteret, domain=None, range=Optional[Union[bool, Bool]])

slots.oenskesSlettetIForetaksregisteret = Slot(uri=GENERATED.oenskesSlettetIForetaksregisteret, name="oenskesSlettetIForetaksregisteret", curie=GENERATED.curie('oenskesSlettetIForetaksregisteret'),
                   model_uri=GENERATED.oenskesSlettetIForetaksregisteret, domain=None, range=Optional[Union[bool, Bool]])

slots.typeEierskifte = Slot(uri=GENERATED.typeEierskifte, name="typeEierskifte", curie=GENERATED.curie('typeEierskifte'),
                   model_uri=GENERATED.typeEierskifte, domain=None, range=Optional[Union[str, "TypeEierskifte"]])

slots.organisasjonsnummerHovedenhet = Slot(uri=GENERATED.organisasjonsnummerHovedenhet, name="organisasjonsnummerHovedenhet", curie=GENERATED.curie('organisasjonsnummerHovedenhet'),
                   model_uri=GENERATED.organisasjonsnummerHovedenhet, domain=None, range=Optional[str])

slots.gjelderHeleAktiviteten = Slot(uri=GENERATED.gjelderHeleAktiviteten, name="gjelderHeleAktiviteten", curie=GENERATED.curie('gjelderHeleAktiviteten'),
                   model_uri=GENERATED.gjelderHeleAktiviteten, domain=None, range=Optional[Union[bool, Bool]])

slots.eierskiftedato = Slot(uri=GENERATED.eierskiftedato, name="eierskiftedato", curie=GENERATED.curie('eierskiftedato'),
                   model_uri=GENERATED.eierskiftedato, domain=None, range=Optional[str])

slots.hvilkeDeler = Slot(uri=GENERATED.hvilkeDeler, name="hvilkeDeler", curie=GENERATED.curie('hvilkeDeler'),
                   model_uri=GENERATED.hvilkeDeler, domain=None, range=Optional[Union[str, DelerEierskifteId]])

slots.beskrivelse = Slot(uri=GENERATED.beskrivelse, name="beskrivelse", curie=GENERATED.curie('beskrivelse'),
                   model_uri=GENERATED.beskrivelse, domain=None, range=Optional[str])

slots.underenhet = Slot(uri=GENERATED.underenhet, name="underenhet", curie=GENERATED.curie('underenhet'),
                   model_uri=GENERATED.underenhet, domain=None, range=Optional[Union[str, list[str]]])

slots.gaardsnummer = Slot(uri=GENERATED.gaardsnummer, name="gaardsnummer", curie=GENERATED.curie('gaardsnummer'),
                   model_uri=GENERATED.gaardsnummer, domain=None, range=Optional[int])

slots.bruksnummer = Slot(uri=GENERATED.bruksnummer, name="bruksnummer", curie=GENERATED.curie('bruksnummer'),
                   model_uri=GENERATED.bruksnummer, domain=None, range=Optional[int])

slots.festenummer = Slot(uri=GENERATED.festenummer, name="festenummer", curie=GENERATED.curie('festenummer'),
                   model_uri=GENERATED.festenummer, domain=None, range=Optional[int])

slots.test = Slot(uri=GENERATED.test, name="test", curie=GENERATED.curie('test'),
                   model_uri=GENERATED.test, domain=None, range=Optional[str])

slots.fagsystemID = Slot(uri=GENERATED.fagsystemID, name="fagsystemID", curie=GENERATED.curie('fagsystemID'),
                   model_uri=GENERATED.fagsystemID, domain=None, range=Optional[str])

slots.orgnrFagsystem = Slot(uri=GENERATED.orgnrFagsystem, name="orgnrFagsystem", curie=GENERATED.curie('orgnrFagsystem'),
                   model_uri=GENERATED.orgnrFagsystem, domain=None, range=Optional[str])

slots.referanseFagsystem = Slot(uri=GENERATED.referanseFagsystem, name="referanseFagsystem", curie=GENERATED.curie('referanseFagsystem'),
                   model_uri=GENERATED.referanseFagsystem, domain=None, range=Optional[str])

slots.eksternFakturareferanse = Slot(uri=GENERATED.eksternFakturareferanse, name="eksternFakturareferanse", curie=GENERATED.curie('eksternFakturareferanse'),
                   model_uri=GENERATED.eksternFakturareferanse, domain=None, range=Optional[str])

slots.gebyransvarligType = Slot(uri=GENERATED.gebyransvarligType, name="gebyransvarligType", curie=GENERATED.curie('gebyransvarligType'),
                   model_uri=GENERATED.gebyransvarligType, domain=None, range=Optional[Union[str, "GebyransvarligType"]])

slots.generatedContainer__innrapporteringer = Slot(uri=GENERATED.innrapporteringer, name="generatedContainer__innrapporteringer", curie=GENERATED.curie('innrapporteringer'),
                   model_uri=GENERATED.generatedContainer__innrapporteringer, domain=None, range=Optional[Union[dict[Union[str, InnrapporteringId], Union[dict, Innrapportering]], list[Union[dict, Innrapportering]]]])

slots.generatedContainer__virksomhetsinformasjonHovedenheter = Slot(uri=GENERATED.virksomhetsinformasjonHovedenheter, name="generatedContainer__virksomhetsinformasjonHovedenheter", curie=GENERATED.curie('virksomhetsinformasjonHovedenheter'),
                   model_uri=GENERATED.generatedContainer__virksomhetsinformasjonHovedenheter, domain=None, range=Optional[Union[dict[Union[str, VirksomhetsinformasjonHovedenhetId], Union[dict, VirksomhetsinformasjonHovedenhet]], list[Union[dict, VirksomhetsinformasjonHovedenhet]]]])

slots.generatedContainer__forretningsadresseer = Slot(uri=GENERATED.forretningsadresseer, name="generatedContainer__forretningsadresseer", curie=GENERATED.curie('forretningsadresseer'),
                   model_uri=GENERATED.generatedContainer__forretningsadresseer, domain=None, range=Optional[Union[dict[Union[str, ForretningsadresseId], Union[dict, Forretningsadresse]], list[Union[dict, Forretningsadresse]]]])

slots.generatedContainer__stedsadresseer = Slot(uri=GENERATED.stedsadresseer, name="generatedContainer__stedsadresseer", curie=GENERATED.curie('stedsadresseer'),
                   model_uri=GENERATED.generatedContainer__stedsadresseer, domain=None, range=Optional[Union[dict[Union[str, StedsadresseId], Union[dict, Stedsadresse]], list[Union[dict, Stedsadresse]]]])

slots.generatedContainer__vegadresseer = Slot(uri=GENERATED.vegadresseer, name="generatedContainer__vegadresseer", curie=GENERATED.curie('vegadresseer'),
                   model_uri=GENERATED.generatedContainer__vegadresseer, domain=None, range=Optional[Union[dict[Union[str, VegadresseId], Union[dict, Vegadresse]], list[Union[dict, Vegadresse]]]])

slots.generatedContainer__adressenummerer = Slot(uri=GENERATED.adressenummerer, name="generatedContainer__adressenummerer", curie=GENERATED.curie('adressenummerer'),
                   model_uri=GENERATED.generatedContainer__adressenummerer, domain=None, range=Optional[Union[dict[Union[str, AdressenummerId], Union[dict, Adressenummer]], list[Union[dict, Adressenummer]]]])

slots.generatedContainer__varslingsadresseer = Slot(uri=GENERATED.varslingsadresseer, name="generatedContainer__varslingsadresseer", curie=GENERATED.curie('varslingsadresseer'),
                   model_uri=GENERATED.generatedContainer__varslingsadresseer, domain=None, range=Optional[Union[dict[Union[str, VarslingsadresseId], Union[dict, Varslingsadresse]], list[Union[dict, Varslingsadresse]]]])

slots.generatedContainer__mobilnummerer = Slot(uri=GENERATED.mobilnummerer, name="generatedContainer__mobilnummerer", curie=GENERATED.curie('mobilnummerer'),
                   model_uri=GENERATED.generatedContainer__mobilnummerer, domain=None, range=Optional[Union[dict[Union[str, MobilnummerId], Union[dict, Mobilnummer]], list[Union[dict, Mobilnummer]]]])

slots.generatedContainer__postadresseer = Slot(uri=GENERATED.postadresseer, name="generatedContainer__postadresseer", curie=GENERATED.curie('postadresseer'),
                   model_uri=GENERATED.generatedContainer__postadresseer, domain=None, range=Optional[Union[dict[Union[str, PostadresseId], Union[dict, Postadresse]], list[Union[dict, Postadresse]]]])

slots.generatedContainer__postboksadresseer = Slot(uri=GENERATED.postboksadresseer, name="generatedContainer__postboksadresseer", curie=GENERATED.curie('postboksadresseer'),
                   model_uri=GENERATED.generatedContainer__postboksadresseer, domain=None, range=Optional[Union[dict[Union[str, PostboksadresseId], Union[dict, Postboksadresse]], list[Union[dict, Postboksadresse]]]])

slots.generatedContainer__internasjonalAdresseer = Slot(uri=GENERATED.internasjonalAdresseer, name="generatedContainer__internasjonalAdresseer", curie=GENERATED.curie('internasjonalAdresseer'),
                   model_uri=GENERATED.generatedContainer__internasjonalAdresseer, domain=None, range=Optional[Union[dict[Union[str, InternasjonalAdresseId], Union[dict, InternasjonalAdresse]], list[Union[dict, InternasjonalAdresse]]]])

slots.generatedContainer__kontaktopplysninger = Slot(uri=GENERATED.kontaktopplysninger, name="generatedContainer__kontaktopplysninger", curie=GENERATED.curie('kontaktopplysninger'),
                   model_uri=GENERATED.generatedContainer__kontaktopplysninger, domain=None, range=Optional[Union[dict[Union[str, KontaktopplysningId], Union[dict, Kontaktopplysning]], list[Union[dict, Kontaktopplysning]]]])

slots.generatedContainer__telefonnummerer = Slot(uri=GENERATED.telefonnummerer, name="generatedContainer__telefonnummerer", curie=GENERATED.curie('telefonnummerer'),
                   model_uri=GENERATED.generatedContainer__telefonnummerer, domain=None, range=Optional[Union[dict[Union[str, TelefonnummerId], Union[dict, Telefonnummer]], list[Union[dict, Telefonnummer]]]])

slots.generatedContainer__virksomhetsinformasjonUnderenheter = Slot(uri=GENERATED.virksomhetsinformasjonUnderenheter, name="generatedContainer__virksomhetsinformasjonUnderenheter", curie=GENERATED.curie('virksomhetsinformasjonUnderenheter'),
                   model_uri=GENERATED.generatedContainer__virksomhetsinformasjonUnderenheter, domain=None, range=Optional[Union[dict[Union[str, VirksomhetsinformasjonUnderenhetId], Union[dict, VirksomhetsinformasjonUnderenhet]], list[Union[dict, VirksomhetsinformasjonUnderenhet]]]])

slots.generatedContainer__beliggenhetsadresseer = Slot(uri=GENERATED.beliggenhetsadresseer, name="generatedContainer__beliggenhetsadresseer", curie=GENERATED.curie('beliggenhetsadresseer'),
                   model_uri=GENERATED.generatedContainer__beliggenhetsadresseer, domain=None, range=Optional[Union[dict[Union[str, BeliggenhetsadresseId], Union[dict, Beliggenhetsadresse]], list[Union[dict, Beliggenhetsadresse]]]])

slots.generatedContainer__aktiviteter = Slot(uri=GENERATED.aktiviteter, name="generatedContainer__aktiviteter", curie=GENERATED.curie('aktiviteter'),
                   model_uri=GENERATED.generatedContainer__aktiviteter, domain=None, range=Optional[Union[dict[Union[str, AktivitetId], Union[dict, Aktivitet]], list[Union[dict, Aktivitet]]]])

slots.generatedContainer__typeAktiviteter = Slot(uri=GENERATED.typeAktiviteter, name="generatedContainer__typeAktiviteter", curie=GENERATED.curie('typeAktiviteter'),
                   model_uri=GENERATED.generatedContainer__typeAktiviteter, domain=None, range=Optional[Union[dict[Union[str, TypeAktivitetId], Union[dict, TypeAktivitet]], list[Union[dict, TypeAktivitet]]]])

slots.generatedContainer__omdanninger = Slot(uri=GENERATED.omdanninger, name="generatedContainer__omdanninger", curie=GENERATED.curie('omdanninger'),
                   model_uri=GENERATED.generatedContainer__omdanninger, domain=None, range=Optional[Union[dict[Union[str, OmdanningId], Union[dict, Omdanning]], list[Union[dict, Omdanning]]]])

slots.generatedContainer__rolletypegruppeer = Slot(uri=GENERATED.rolletypegruppeer, name="generatedContainer__rolletypegruppeer", curie=GENERATED.curie('rolletypegruppeer'),
                   model_uri=GENERATED.generatedContainer__rolletypegruppeer, domain=None, range=Optional[Union[dict[Union[str, RolletypegruppeId], Union[dict, Rolletypegruppe]], list[Union[dict, Rolletypegruppe]]]])

slots.generatedContainer__rolleer = Slot(uri=GENERATED.rolleer, name="generatedContainer__rolleer", curie=GENERATED.curie('rolleer'),
                   model_uri=GENERATED.generatedContainer__rolleer, domain=None, range=Optional[Union[dict[Union[str, RolleId], Union[dict, Rolle]], list[Union[dict, Rolle]]]])

slots.generatedContainer__rolleinnehaverer = Slot(uri=GENERATED.rolleinnehaverer, name="generatedContainer__rolleinnehaverer", curie=GENERATED.curie('rolleinnehaverer'),
                   model_uri=GENERATED.generatedContainer__rolleinnehaverer, domain=None, range=Optional[Union[dict[Union[str, RolleinnehaverId], Union[dict, Rolleinnehaver]], list[Union[dict, Rolleinnehaver]]]])

slots.generatedContainer__ansvarsandeler = Slot(uri=GENERATED.ansvarsandeler, name="generatedContainer__ansvarsandeler", curie=GENERATED.curie('ansvarsandeler'),
                   model_uri=GENERATED.generatedContainer__ansvarsandeler, domain=None, range=Optional[Union[dict[Union[str, AnsvarsandelId], Union[dict, Ansvarsandel]], list[Union[dict, Ansvarsandel]]]])

slots.generatedContainer__broeker = Slot(uri=GENERATED.broeker, name="generatedContainer__broeker", curie=GENERATED.curie('broeker'),
                   model_uri=GENERATED.generatedContainer__broeker, domain=None, range=Optional[Union[dict[Union[str, BroekId], Union[dict, Broek]], list[Union[dict, Broek]]]])

slots.generatedContainer__virksomheter = Slot(uri=GENERATED.virksomheter, name="generatedContainer__virksomheter", curie=GENERATED.curie('virksomheter'),
                   model_uri=GENERATED.generatedContainer__virksomheter, domain=None, range=Optional[Union[dict[Union[str, VirksomhetId], Union[dict, Virksomhet]], list[Union[dict, Virksomhet]]]])

slots.generatedContainer__personer = Slot(uri=GENERATED.personer, name="generatedContainer__personer", curie=GENERATED.curie('personer'),
                   model_uri=GENERATED.generatedContainer__personer, domain=None, range=Optional[Union[dict[Union[str, PersonId], Union[dict, Person]], list[Union[dict, Person]]]])

slots.generatedContainer__prokuraer = Slot(uri=GENERATED.prokuraer, name="generatedContainer__prokuraer", curie=GENERATED.curie('prokuraer'),
                   model_uri=GENERATED.generatedContainer__prokuraer, domain=None, range=Optional[Union[dict[Union[str, ProkuraId], Union[dict, Prokura]], list[Union[dict, Prokura]]]])

slots.generatedContainer__prokurabestemmelseer = Slot(uri=GENERATED.prokurabestemmelseer, name="generatedContainer__prokurabestemmelseer", curie=GENERATED.curie('prokurabestemmelseer'),
                   model_uri=GENERATED.generatedContainer__prokurabestemmelseer, domain=None, range=Optional[Union[dict[Union[str, ProkurabestemmelseId], Union[dict, Prokurabestemmelse]], list[Union[dict, Prokurabestemmelse]]]])

slots.generatedContainer__rollesetter = Slot(uri=GENERATED.rollesetter, name="generatedContainer__rollesetter", curie=GENERATED.curie('rollesetter'),
                   model_uri=GENERATED.generatedContainer__rollesetter, domain=None, range=Optional[Union[dict[Union[str, RollesettId], Union[dict, Rollesett]], list[Union[dict, Rollesett]]]])

slots.generatedContainer__signaturberettigetEllerProkurister = Slot(uri=GENERATED.signaturberettigetEllerProkurister, name="generatedContainer__signaturberettigetEllerProkurister", curie=GENERATED.curie('signaturberettigetEllerProkurister'),
                   model_uri=GENERATED.generatedContainer__signaturberettigetEllerProkurister, domain=None, range=Optional[Union[dict[Union[str, SignaturberettigetEllerProkuristId], Union[dict, SignaturberettigetEllerProkurist]], list[Union[dict, SignaturberettigetEllerProkurist]]]])

slots.generatedContainer__signaturretter = Slot(uri=GENERATED.signaturretter, name="generatedContainer__signaturretter", curie=GENERATED.curie('signaturretter'),
                   model_uri=GENERATED.generatedContainer__signaturretter, domain=None, range=Optional[Union[dict[Union[str, SignaturrettId], Union[dict, Signaturrett]], list[Union[dict, Signaturrett]]]])

slots.generatedContainer__signaturrettsbestemmelseer = Slot(uri=GENERATED.signaturrettsbestemmelseer, name="generatedContainer__signaturrettsbestemmelseer", curie=GENERATED.curie('signaturrettsbestemmelseer'),
                   model_uri=GENERATED.generatedContainer__signaturrettsbestemmelseer, domain=None, range=Optional[Union[dict[Union[str, SignaturrettsbestemmelseId], Union[dict, Signaturrettsbestemmelse]], list[Union[dict, Signaturrettsbestemmelse]]]])

slots.generatedContainer__foretaksinformasjoner = Slot(uri=GENERATED.foretaksinformasjoner, name="generatedContainer__foretaksinformasjoner", curie=GENERATED.curie('foretaksinformasjoner'),
                   model_uri=GENERATED.generatedContainer__foretaksinformasjoner, domain=None, range=Optional[Union[dict[Union[str, ForetaksinformasjonId], Union[dict, Foretaksinformasjon]], list[Union[dict, Foretaksinformasjon]]]])

slots.generatedContainer__eierskifteAktiviteter = Slot(uri=GENERATED.eierskifteAktiviteter, name="generatedContainer__eierskifteAktiviteter", curie=GENERATED.curie('eierskifteAktiviteter'),
                   model_uri=GENERATED.generatedContainer__eierskifteAktiviteter, domain=None, range=Optional[Union[dict[Union[str, EierskifteAktivitetId], Union[dict, EierskifteAktivitet]], list[Union[dict, EierskifteAktivitet]]]])

slots.generatedContainer__delerEierskifteer = Slot(uri=GENERATED.delerEierskifteer, name="generatedContainer__delerEierskifteer", curie=GENERATED.curie('delerEierskifteer'),
                   model_uri=GENERATED.generatedContainer__delerEierskifteer, domain=None, range=Optional[Union[dict[Union[str, DelerEierskifteId], Union[dict, DelerEierskifte]], list[Union[dict, DelerEierskifte]]]])

slots.generatedContainer__matrikkelnummerer = Slot(uri=GENERATED.matrikkelnummerer, name="generatedContainer__matrikkelnummerer", curie=GENERATED.curie('matrikkelnummerer'),
                   model_uri=GENERATED.generatedContainer__matrikkelnummerer, domain=None, range=Optional[Union[dict[Union[str, MatrikkelnummerId], Union[dict, Matrikkelnummer]], list[Union[dict, Matrikkelnummer]]]])

slots.generatedContainer__innsenderer = Slot(uri=GENERATED.innsenderer, name="generatedContainer__innsenderer", curie=GENERATED.curie('innsenderer'),
                   model_uri=GENERATED.generatedContainer__innsenderer, domain=None, range=Optional[Union[dict[Union[str, InnsenderId], Union[dict, Innsender]], list[Union[dict, Innsender]]]])

slots.generatedContainer__fagsystemreferanseer = Slot(uri=GENERATED.fagsystemreferanseer, name="generatedContainer__fagsystemreferanseer", curie=GENERATED.curie('fagsystemreferanseer'),
                   model_uri=GENERATED.generatedContainer__fagsystemreferanseer, domain=None, range=Optional[Union[dict[Union[str, FagsystemreferanseId], Union[dict, Fagsystemreferanse]], list[Union[dict, Fagsystemreferanse]]]])

slots.generatedContainer__signeringer = Slot(uri=GENERATED.signeringer, name="generatedContainer__signeringer", curie=GENERATED.curie('signeringer'),
                   model_uri=GENERATED.generatedContainer__signeringer, domain=None, range=Optional[Union[list[Union[str, SigneringId]], dict[Union[str, SigneringId], Union[dict, Signering]]]])

slots.generatedContainer__gebyransvarliger = Slot(uri=GENERATED.gebyransvarliger, name="generatedContainer__gebyransvarliger", curie=GENERATED.curie('gebyransvarliger'),
                   model_uri=GENERATED.generatedContainer__gebyransvarliger, domain=None, range=Optional[Union[dict[Union[str, GebyransvarligId], Union[dict, Gebyransvarlig]], list[Union[dict, Gebyransvarlig]]]])

slots.Innrapportering_versjon = Slot(uri=GENERATED.versjon, name="Innrapportering_versjon", curie=GENERATED.curie('versjon'),
                   model_uri=GENERATED.Innrapportering_versjon, domain=Innrapportering, range=str)

slots.Innrapportering_innsendertjenste = Slot(uri=GENERATED.innsendertjenste, name="Innrapportering_innsendertjenste", curie=GENERATED.curie('innsendertjenste'),
                   model_uri=GENERATED.Innrapportering_innsendertjenste, domain=Innrapportering, range=str)

slots.Innrapportering_innsendingstidspunkt = Slot(uri=GENERATED.innsendingstidspunkt, name="Innrapportering_innsendingstidspunkt", curie=GENERATED.curie('innsendingstidspunkt'),
                   model_uri=GENERATED.Innrapportering_innsendingstidspunkt, domain=Innrapportering, range=str)

slots.Innrapportering_maalformForTilbakemelding = Slot(uri=GENERATED.maalformForTilbakemelding, name="Innrapportering_maalformForTilbakemelding", curie=GENERATED.curie('maalformForTilbakemelding'),
                   model_uri=GENERATED.Innrapportering_maalformForTilbakemelding, domain=Innrapportering, range=Union[str, "Maalform"])

slots.Innrapportering_tjenestevariant = Slot(uri=GENERATED.tjenestevariant, name="Innrapportering_tjenestevariant", curie=GENERATED.curie('tjenestevariant'),
                   model_uri=GENERATED.Innrapportering_tjenestevariant, domain=Innrapportering, range=str)

slots.Innrapportering_virksomhetsinformasjon = Slot(uri=GENERATED.virksomhetsinformasjon, name="Innrapportering_virksomhetsinformasjon", curie=GENERATED.curie('virksomhetsinformasjon'),
                   model_uri=GENERATED.Innrapportering_virksomhetsinformasjon, domain=Innrapportering, range=Union[str, VirksomhetsinformasjonHovedenhetId])

slots.Innrapportering_innsender = Slot(uri=GENERATED.innsender, name="Innrapportering_innsender", curie=GENERATED.curie('innsender'),
                   model_uri=GENERATED.Innrapportering_innsender, domain=Innrapportering, range=Union[str, InnsenderId])

slots.Innrapportering_fagsystemReferanse = Slot(uri=GENERATED.fagsystemReferanse, name="Innrapportering_fagsystemReferanse", curie=GENERATED.curie('fagsystemReferanse'),
                   model_uri=GENERATED.Innrapportering_fagsystemReferanse, domain=Innrapportering, range=Optional[Union[str, FagsystemreferanseId]])

slots.Innrapportering_signering = Slot(uri=GENERATED.signering, name="Innrapportering_signering", curie=GENERATED.curie('signering'),
                   model_uri=GENERATED.Innrapportering_signering, domain=Innrapportering, range=Optional[Union[str, SigneringId]])

slots.Innrapportering_gebyransvarlig = Slot(uri=GENERATED.gebyransvarlig, name="Innrapportering_gebyransvarlig", curie=GENERATED.curie('gebyransvarlig'),
                   model_uri=GENERATED.Innrapportering_gebyransvarlig, domain=Innrapportering, range=Optional[Union[str, GebyransvarligId]])

slots.Innrapportering_lenkeForEttersending = Slot(uri=GENERATED.lenkeForEttersending, name="Innrapportering_lenkeForEttersending", curie=GENERATED.curie('lenkeForEttersending'),
                   model_uri=GENERATED.Innrapportering_lenkeForEttersending, domain=Innrapportering, range=Optional[str])

slots.VirksomhetsinformasjonHovedenhet_organisasjonsform = Slot(uri=GENERATED.organisasjonsform, name="VirksomhetsinformasjonHovedenhet_organisasjonsform", curie=GENERATED.curie('organisasjonsform'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_organisasjonsform, domain=VirksomhetsinformasjonHovedenhet, range=str)

slots.VirksomhetsinformasjonHovedenhet_virksomhetstype = Slot(uri=GENERATED.virksomhetstype, name="VirksomhetsinformasjonHovedenhet_virksomhetstype", curie=GENERATED.curie('virksomhetstype'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_virksomhetstype, domain=VirksomhetsinformasjonHovedenhet, range=Optional[str])

slots.VirksomhetsinformasjonHovedenhet_organisasjonsnummer = Slot(uri=GENERATED.organisasjonsnummer, name="VirksomhetsinformasjonHovedenhet_organisasjonsnummer", curie=GENERATED.curie('organisasjonsnummer'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_organisasjonsnummer, domain=VirksomhetsinformasjonHovedenhet, range=Optional[str])

slots.VirksomhetsinformasjonHovedenhet_navn = Slot(uri=GENERATED.navn, name="VirksomhetsinformasjonHovedenhet_navn", curie=GENERATED.curie('navn'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_navn, domain=VirksomhetsinformasjonHovedenhet, range=Optional[str])

slots.VirksomhetsinformasjonHovedenhet_maalform = Slot(uri=GENERATED.maalform, name="VirksomhetsinformasjonHovedenhet_maalform", curie=GENERATED.curie('maalform'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_maalform, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[str, "Maalform"]])

slots.VirksomhetsinformasjonHovedenhet_oppfyllerKravTilNaeringsvirksomhet = Slot(uri=GENERATED.oppfyllerKravTilNaeringsvirksomhet, name="VirksomhetsinformasjonHovedenhet_oppfyllerKravTilNaeringsvirksomhet", curie=GENERATED.curie('oppfyllerKravTilNaeringsvirksomhet'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_oppfyllerKravTilNaeringsvirksomhet, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[bool, Bool]])

slots.VirksomhetsinformasjonHovedenhet_venterAAFaaAnsatte = Slot(uri=GENERATED.venterAAFaaAnsatte, name="VirksomhetsinformasjonHovedenhet_venterAAFaaAnsatte", curie=GENERATED.curie('venterAAFaaAnsatte'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_venterAAFaaAnsatte, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[bool, Bool]])

slots.VirksomhetsinformasjonHovedenhet_datoForAvtale = Slot(uri=GENERATED.datoForAvtale, name="VirksomhetsinformasjonHovedenhet_datoForAvtale", curie=GENERATED.curie('datoForAvtale'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_datoForAvtale, domain=VirksomhetsinformasjonHovedenhet, range=Optional[str])

slots.VirksomhetsinformasjonHovedenhet_stiftelsesdato = Slot(uri=GENERATED.stiftelsesdato, name="VirksomhetsinformasjonHovedenhet_stiftelsesdato", curie=GENERATED.curie('stiftelsesdato'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_stiftelsesdato, domain=VirksomhetsinformasjonHovedenhet, range=Optional[str])

slots.VirksomhetsinformasjonHovedenhet_vedtektsdato = Slot(uri=GENERATED.vedtektsdato, name="VirksomhetsinformasjonHovedenhet_vedtektsdato", curie=GENERATED.curie('vedtektsdato'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_vedtektsdato, domain=VirksomhetsinformasjonHovedenhet, range=Optional[str])

slots.VirksomhetsinformasjonHovedenhet_formaal = Slot(uri=GENERATED.formaal, name="VirksomhetsinformasjonHovedenhet_formaal", curie=GENERATED.curie('formaal'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_formaal, domain=VirksomhetsinformasjonHovedenhet, range=Optional[str])

slots.VirksomhetsinformasjonHovedenhet_harAnsvarsbegrensning = Slot(uri=GENERATED.harAnsvarsbegrensning, name="VirksomhetsinformasjonHovedenhet_harAnsvarsbegrensning", curie=GENERATED.curie('harAnsvarsbegrensning'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_harAnsvarsbegrensning, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[bool, Bool]])

slots.VirksomhetsinformasjonHovedenhet_ansvarsform = Slot(uri=GENERATED.ansvarsform, name="VirksomhetsinformasjonHovedenhet_ansvarsform", curie=GENERATED.curie('ansvarsform'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_ansvarsform, domain=VirksomhetsinformasjonHovedenhet, range=Optional[str])

slots.VirksomhetsinformasjonHovedenhet_forretningsadresse = Slot(uri=GENERATED.forretningsadresse, name="VirksomhetsinformasjonHovedenhet_forretningsadresse", curie=GENERATED.curie('forretningsadresse'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_forretningsadresse, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[str, ForretningsadresseId]])

slots.VirksomhetsinformasjonHovedenhet_varslingsadresse = Slot(uri=GENERATED.varslingsadresse, name="VirksomhetsinformasjonHovedenhet_varslingsadresse", curie=GENERATED.curie('varslingsadresse'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_varslingsadresse, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[str, VarslingsadresseId]])

slots.VirksomhetsinformasjonHovedenhet_postadresse = Slot(uri=GENERATED.postadresse, name="VirksomhetsinformasjonHovedenhet_postadresse", curie=GENERATED.curie('postadresse'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_postadresse, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[str, PostadresseId]])

slots.VirksomhetsinformasjonHovedenhet_kontaktopplysning = Slot(uri=GENERATED.kontaktopplysning, name="VirksomhetsinformasjonHovedenhet_kontaktopplysning", curie=GENERATED.curie('kontaktopplysning'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_kontaktopplysning, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[str, KontaktopplysningId]])

slots.VirksomhetsinformasjonHovedenhet_virksomhetsinformasjonUnderenhet = Slot(uri=GENERATED.virksomhetsinformasjonUnderenhet, name="VirksomhetsinformasjonHovedenhet_virksomhetsinformasjonUnderenhet", curie=GENERATED.curie('virksomhetsinformasjonUnderenhet'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_virksomhetsinformasjonUnderenhet, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[Union[str, VirksomhetsinformasjonUnderenhetId], list[Union[str, VirksomhetsinformasjonUnderenhetId]]]])

slots.VirksomhetsinformasjonHovedenhet_aktivitet = Slot(uri=GENERATED.aktivitet, name="VirksomhetsinformasjonHovedenhet_aktivitet", curie=GENERATED.curie('aktivitet'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_aktivitet, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[str, AktivitetId]])

slots.VirksomhetsinformasjonHovedenhet_omdanning = Slot(uri=GENERATED.omdanning, name="VirksomhetsinformasjonHovedenhet_omdanning", curie=GENERATED.curie('omdanning'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_omdanning, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[str, OmdanningId]])

slots.VirksomhetsinformasjonHovedenhet_rolletypegruppe = Slot(uri=GENERATED.rolletypegruppe, name="VirksomhetsinformasjonHovedenhet_rolletypegruppe", curie=GENERATED.curie('rolletypegruppe'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_rolletypegruppe, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[Union[str, RolletypegruppeId], list[Union[str, RolletypegruppeId]]]])

slots.VirksomhetsinformasjonHovedenhet_prokura = Slot(uri=GENERATED.prokura, name="VirksomhetsinformasjonHovedenhet_prokura", curie=GENERATED.curie('prokura'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_prokura, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[str, ProkuraId]])

slots.VirksomhetsinformasjonHovedenhet_signaturrett = Slot(uri=GENERATED.signaturrett, name="VirksomhetsinformasjonHovedenhet_signaturrett", curie=GENERATED.curie('signaturrett'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_signaturrett, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[str, SignaturrettId]])

slots.VirksomhetsinformasjonHovedenhet_meldtOpploesning = Slot(uri=GENERATED.meldtOpploesning, name="VirksomhetsinformasjonHovedenhet_meldtOpploesning", curie=GENERATED.curie('meldtOpploesning'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_meldtOpploesning, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[bool, Bool]])

slots.VirksomhetsinformasjonHovedenhet_meldtOmgjoeringAvOpploesning = Slot(uri=GENERATED.meldtOmgjoeringAvOpploesning, name="VirksomhetsinformasjonHovedenhet_meldtOmgjoeringAvOpploesning", curie=GENERATED.curie('meldtOmgjoeringAvOpploesning'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_meldtOmgjoeringAvOpploesning, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[bool, Bool]])

slots.VirksomhetsinformasjonHovedenhet_foretaksinformasjon = Slot(uri=GENERATED.foretaksinformasjon, name="VirksomhetsinformasjonHovedenhet_foretaksinformasjon", curie=GENERATED.curie('foretaksinformasjon'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_foretaksinformasjon, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[str, ForetaksinformasjonId]])

slots.VirksomhetsinformasjonHovedenhet_eierskifte = Slot(uri=GENERATED.eierskifte, name="VirksomhetsinformasjonHovedenhet_eierskifte", curie=GENERATED.curie('eierskifte'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_eierskifte, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[Union[str, EierskifteAktivitetId], list[Union[str, EierskifteAktivitetId]]]])

slots.VirksomhetsinformasjonHovedenhet_bekreftelseProtokollSletting = Slot(uri=GENERATED.bekreftelseProtokollSletting, name="VirksomhetsinformasjonHovedenhet_bekreftelseProtokollSletting", curie=GENERATED.curie('bekreftelseProtokollSletting'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_bekreftelseProtokollSletting, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[bool, Bool]])

slots.VirksomhetsinformasjonHovedenhet_matrikkelnummer = Slot(uri=GENERATED.matrikkelnummer, name="VirksomhetsinformasjonHovedenhet_matrikkelnummer", curie=GENERATED.curie('matrikkelnummer'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_matrikkelnummer, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[Union[str, MatrikkelnummerId], list[Union[str, MatrikkelnummerId]]]])

slots.VirksomhetsinformasjonHovedenhet_registrertITilknyttetRegister = Slot(uri=GENERATED.registrertITilknyttetRegister, name="VirksomhetsinformasjonHovedenhet_registrertITilknyttetRegister", curie=GENERATED.curie('registrertITilknyttetRegister'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_registrertITilknyttetRegister, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[str, list[str]]])

slots.VirksomhetsinformasjonHovedenhet_bekreftelseProtokollOpploesningOgOmgjoering = Slot(uri=GENERATED.bekreftelseProtokollOpploesningOgOmgjoering, name="VirksomhetsinformasjonHovedenhet_bekreftelseProtokollOpploesningOgOmgjoering", curie=GENERATED.curie('bekreftelseProtokollOpploesningOgOmgjoering'),
                   model_uri=GENERATED.VirksomhetsinformasjonHovedenhet_bekreftelseProtokollOpploesningOgOmgjoering, domain=VirksomhetsinformasjonHovedenhet, range=Optional[Union[bool, Bool]])

slots.Forretningsadresse_coNavn = Slot(uri=GENERATED.coNavn, name="Forretningsadresse_coNavn", curie=GENERATED.curie('coNavn'),
                   model_uri=GENERATED.Forretningsadresse_coNavn, domain=Forretningsadresse, range=Optional[str])

slots.Forretningsadresse_vNavn = Slot(uri=GENERATED.vNavn, name="Forretningsadresse_vNavn", curie=GENERATED.curie('vNavn'),
                   model_uri=GENERATED.Forretningsadresse_vNavn, domain=Forretningsadresse, range=Optional[str])

slots.Forretningsadresse_utgaar = Slot(uri=GENERATED.utgaar, name="Forretningsadresse_utgaar", curie=GENERATED.curie('utgaar'),
                   model_uri=GENERATED.Forretningsadresse_utgaar, domain=Forretningsadresse, range=Optional[Union[bool, Bool]])

slots.Forretningsadresse_stedsadresse = Slot(uri=GENERATED.stedsadresse, name="Forretningsadresse_stedsadresse", curie=GENERATED.curie('stedsadresse'),
                   model_uri=GENERATED.Forretningsadresse_stedsadresse, domain=Forretningsadresse, range=Optional[Union[str, StedsadresseId]])

slots.Forretningsadresse_vegadresse = Slot(uri=GENERATED.vegadresse, name="Forretningsadresse_vegadresse", curie=GENERATED.curie('vegadresse'),
                   model_uri=GENERATED.Forretningsadresse_vegadresse, domain=Forretningsadresse, range=Optional[Union[str, VegadresseId]])

slots.Stedsadresse_stedsnavn = Slot(uri=GENERATED.stedsnavn, name="Stedsadresse_stedsnavn", curie=GENERATED.curie('stedsnavn'),
                   model_uri=GENERATED.Stedsadresse_stedsnavn, domain=Stedsadresse, range=Optional[str])

slots.Stedsadresse_kommunenummer = Slot(uri=GENERATED.kommunenummer, name="Stedsadresse_kommunenummer", curie=GENERATED.curie('kommunenummer'),
                   model_uri=GENERATED.Stedsadresse_kommunenummer, domain=Stedsadresse, range=str)

slots.Stedsadresse_postnummer = Slot(uri=GENERATED.postnummer, name="Stedsadresse_postnummer", curie=GENERATED.curie('postnummer'),
                   model_uri=GENERATED.Stedsadresse_postnummer, domain=Stedsadresse, range=str)

slots.Vegadresse_vegadresseId = Slot(uri=GENERATED.vegadresseId, name="Vegadresse_vegadresseId", curie=GENERATED.curie('vegadresseId'),
                   model_uri=GENERATED.Vegadresse_vegadresseId, domain=Vegadresse, range=Optional[str])

slots.Vegadresse_adressenavn = Slot(uri=GENERATED.adressenavn, name="Vegadresse_adressenavn", curie=GENERATED.curie('adressenavn'),
                   model_uri=GENERATED.Vegadresse_adressenavn, domain=Vegadresse, range=str)

slots.Vegadresse_bruksenhetsnummer = Slot(uri=GENERATED.bruksenhetsnummer, name="Vegadresse_bruksenhetsnummer", curie=GENERATED.curie('bruksenhetsnummer'),
                   model_uri=GENERATED.Vegadresse_bruksenhetsnummer, domain=Vegadresse, range=Optional[str])

slots.Vegadresse_nummer = Slot(uri=GENERATED.nummer, name="Vegadresse_nummer", curie=GENERATED.curie('nummer'),
                   model_uri=GENERATED.Vegadresse_nummer, domain=Vegadresse, range=Union[str, AdressenummerId])

slots.Vegadresse_adressetilleggsnavn = Slot(uri=GENERATED.adressetilleggsnavn, name="Vegadresse_adressetilleggsnavn", curie=GENERATED.curie('adressetilleggsnavn'),
                   model_uri=GENERATED.Vegadresse_adressetilleggsnavn, domain=Vegadresse, range=Optional[str])

slots.Vegadresse_kommunenummer = Slot(uri=GENERATED.kommunenummer, name="Vegadresse_kommunenummer", curie=GENERATED.curie('kommunenummer'),
                   model_uri=GENERATED.Vegadresse_kommunenummer, domain=Vegadresse, range=str)

slots.Vegadresse_postnummer = Slot(uri=GENERATED.postnummer, name="Vegadresse_postnummer", curie=GENERATED.curie('postnummer'),
                   model_uri=GENERATED.Vegadresse_postnummer, domain=Vegadresse, range=str)

slots.Adressenummer_nummer = Slot(uri=GENERATED.nummer, name="Adressenummer_nummer", curie=GENERATED.curie('nummer'),
                   model_uri=GENERATED.Adressenummer_nummer, domain=Adressenummer, range=Union[str, AdressenummerId])

slots.Adressenummer_bokstav = Slot(uri=GENERATED.bokstav, name="Adressenummer_bokstav", curie=GENERATED.curie('bokstav'),
                   model_uri=GENERATED.Adressenummer_bokstav, domain=Adressenummer, range=Optional[str])

slots.Varslingsadresse_mobilnummer = Slot(uri=GENERATED.mobilnummer, name="Varslingsadresse_mobilnummer", curie=GENERATED.curie('mobilnummer'),
                   model_uri=GENERATED.Varslingsadresse_mobilnummer, domain=Varslingsadresse, range=Optional[Union[str, MobilnummerId]])

slots.Varslingsadresse_e_postadresse = Slot(uri=GENERATED.e_postadresse, name="Varslingsadresse_e_postadresse", curie=GENERATED.curie('e_postadresse'),
                   model_uri=GENERATED.Varslingsadresse_e_postadresse, domain=Varslingsadresse, range=Optional[str])

slots.Mobilnummer_internasjonaltPrefiks = Slot(uri=GENERATED.internasjonaltPrefiks, name="Mobilnummer_internasjonaltPrefiks", curie=GENERATED.curie('internasjonaltPrefiks'),
                   model_uri=GENERATED.Mobilnummer_internasjonaltPrefiks, domain=Mobilnummer, range=Optional[str])

slots.Mobilnummer_nasjonaltNummer = Slot(uri=GENERATED.nasjonaltNummer, name="Mobilnummer_nasjonaltNummer", curie=GENERATED.curie('nasjonaltNummer'),
                   model_uri=GENERATED.Mobilnummer_nasjonaltNummer, domain=Mobilnummer, range=str)

slots.Postadresse_coNavn = Slot(uri=GENERATED.coNavn, name="Postadresse_coNavn", curie=GENERATED.curie('coNavn'),
                   model_uri=GENERATED.Postadresse_coNavn, domain=Postadresse, range=Optional[str])

slots.Postadresse_vNavn = Slot(uri=GENERATED.vNavn, name="Postadresse_vNavn", curie=GENERATED.curie('vNavn'),
                   model_uri=GENERATED.Postadresse_vNavn, domain=Postadresse, range=Optional[str])

slots.Postadresse_utgaar = Slot(uri=GENERATED.utgaar, name="Postadresse_utgaar", curie=GENERATED.curie('utgaar'),
                   model_uri=GENERATED.Postadresse_utgaar, domain=Postadresse, range=Optional[Union[bool, Bool]])

slots.Postadresse_vegadresse = Slot(uri=GENERATED.vegadresse, name="Postadresse_vegadresse", curie=GENERATED.curie('vegadresse'),
                   model_uri=GENERATED.Postadresse_vegadresse, domain=Postadresse, range=Optional[Union[str, VegadresseId]])

slots.Postadresse_postboksadresse = Slot(uri=GENERATED.postboksadresse, name="Postadresse_postboksadresse", curie=GENERATED.curie('postboksadresse'),
                   model_uri=GENERATED.Postadresse_postboksadresse, domain=Postadresse, range=Optional[Union[str, PostboksadresseId]])

slots.Postadresse_internasjonalAdresse = Slot(uri=GENERATED.internasjonalAdresse, name="Postadresse_internasjonalAdresse", curie=GENERATED.curie('internasjonalAdresse'),
                   model_uri=GENERATED.Postadresse_internasjonalAdresse, domain=Postadresse, range=Optional[Union[str, InternasjonalAdresseId]])

slots.Postadresse_stedsadresse = Slot(uri=GENERATED.stedsadresse, name="Postadresse_stedsadresse", curie=GENERATED.curie('stedsadresse'),
                   model_uri=GENERATED.Postadresse_stedsadresse, domain=Postadresse, range=Optional[Union[str, StedsadresseId]])

slots.Postboksadresse_postboksnummer = Slot(uri=GENERATED.postboksnummer, name="Postboksadresse_postboksnummer", curie=GENERATED.curie('postboksnummer'),
                   model_uri=GENERATED.Postboksadresse_postboksnummer, domain=Postboksadresse, range=str)

slots.Postboksadresse_postboksanleggsnavn = Slot(uri=GENERATED.postboksanleggsnavn, name="Postboksadresse_postboksanleggsnavn", curie=GENERATED.curie('postboksanleggsnavn'),
                   model_uri=GENERATED.Postboksadresse_postboksanleggsnavn, domain=Postboksadresse, range=Optional[str])

slots.Postboksadresse_postnummer = Slot(uri=GENERATED.postnummer, name="Postboksadresse_postnummer", curie=GENERATED.curie('postnummer'),
                   model_uri=GENERATED.Postboksadresse_postnummer, domain=Postboksadresse, range=str)

slots.Postboksadresse_kommunenummer = Slot(uri=GENERATED.kommunenummer, name="Postboksadresse_kommunenummer", curie=GENERATED.curie('kommunenummer'),
                   model_uri=GENERATED.Postboksadresse_kommunenummer, domain=Postboksadresse, range=str)

slots.InternasjonalAdresse_adressenavn = Slot(uri=GENERATED.adressenavn, name="InternasjonalAdresse_adressenavn", curie=GENERATED.curie('adressenavn'),
                   model_uri=GENERATED.InternasjonalAdresse_adressenavn, domain=InternasjonalAdresse, range=Optional[str])

slots.InternasjonalAdresse_adressenummer = Slot(uri=GENERATED.adressenummer, name="InternasjonalAdresse_adressenummer", curie=GENERATED.curie('adressenummer'),
                   model_uri=GENERATED.InternasjonalAdresse_adressenummer, domain=InternasjonalAdresse, range=Optional[str])

slots.InternasjonalAdresse_bygning = Slot(uri=GENERATED.bygning, name="InternasjonalAdresse_bygning", curie=GENERATED.curie('bygning'),
                   model_uri=GENERATED.InternasjonalAdresse_bygning, domain=InternasjonalAdresse, range=Optional[str])

slots.InternasjonalAdresse_etasjenummer = Slot(uri=GENERATED.etasjenummer, name="InternasjonalAdresse_etasjenummer", curie=GENERATED.curie('etasjenummer'),
                   model_uri=GENERATED.InternasjonalAdresse_etasjenummer, domain=InternasjonalAdresse, range=Optional[str])

slots.InternasjonalAdresse_boenhet = Slot(uri=GENERATED.boenhet, name="InternasjonalAdresse_boenhet", curie=GENERATED.curie('boenhet'),
                   model_uri=GENERATED.InternasjonalAdresse_boenhet, domain=InternasjonalAdresse, range=Optional[str])

slots.InternasjonalAdresse_postboks = Slot(uri=GENERATED.postboks, name="InternasjonalAdresse_postboks", curie=GENERATED.curie('postboks'),
                   model_uri=GENERATED.InternasjonalAdresse_postboks, domain=InternasjonalAdresse, range=Optional[str])

slots.InternasjonalAdresse_postkode = Slot(uri=GENERATED.postkode, name="InternasjonalAdresse_postkode", curie=GENERATED.curie('postkode'),
                   model_uri=GENERATED.InternasjonalAdresse_postkode, domain=InternasjonalAdresse, range=Optional[str])

slots.InternasjonalAdresse_byEllerStedsnavn = Slot(uri=GENERATED.byEllerStedsnavn, name="InternasjonalAdresse_byEllerStedsnavn", curie=GENERATED.curie('byEllerStedsnavn'),
                   model_uri=GENERATED.InternasjonalAdresse_byEllerStedsnavn, domain=InternasjonalAdresse, range=Optional[str])

slots.InternasjonalAdresse_region = Slot(uri=GENERATED.region, name="InternasjonalAdresse_region", curie=GENERATED.curie('region'),
                   model_uri=GENERATED.InternasjonalAdresse_region, domain=InternasjonalAdresse, range=Optional[str])

slots.InternasjonalAdresse_distriktEllerBydel = Slot(uri=GENERATED.distriktEllerBydel, name="InternasjonalAdresse_distriktEllerBydel", curie=GENERATED.curie('distriktEllerBydel'),
                   model_uri=GENERATED.InternasjonalAdresse_distriktEllerBydel, domain=InternasjonalAdresse, range=Optional[str])

slots.InternasjonalAdresse_friAdressetekst = Slot(uri=GENERATED.friAdressetekst, name="InternasjonalAdresse_friAdressetekst", curie=GENERATED.curie('friAdressetekst'),
                   model_uri=GENERATED.InternasjonalAdresse_friAdressetekst, domain=InternasjonalAdresse, range=Optional[Union[str, list[str]]])

slots.InternasjonalAdresse_adresseidentifikator = Slot(uri=GENERATED.adresseidentifikator, name="InternasjonalAdresse_adresseidentifikator", curie=GENERATED.curie('adresseidentifikator'),
                   model_uri=GENERATED.InternasjonalAdresse_adresseidentifikator, domain=InternasjonalAdresse, range=Optional[str])

slots.InternasjonalAdresse_landkode = Slot(uri=GENERATED.landkode, name="InternasjonalAdresse_landkode", curie=GENERATED.curie('landkode'),
                   model_uri=GENERATED.InternasjonalAdresse_landkode, domain=InternasjonalAdresse, range=str)

slots.Kontaktopplysning_mobilnummer = Slot(uri=GENERATED.mobilnummer, name="Kontaktopplysning_mobilnummer", curie=GENERATED.curie('mobilnummer'),
                   model_uri=GENERATED.Kontaktopplysning_mobilnummer, domain=Kontaktopplysning, range=Optional[Union[str, MobilnummerId]])

slots.Kontaktopplysning_e_postadresse = Slot(uri=GENERATED.e_postadresse, name="Kontaktopplysning_e_postadresse", curie=GENERATED.curie('e_postadresse'),
                   model_uri=GENERATED.Kontaktopplysning_e_postadresse, domain=Kontaktopplysning, range=Optional[str])

slots.Kontaktopplysning_nettadresse = Slot(uri=GENERATED.nettadresse, name="Kontaktopplysning_nettadresse", curie=GENERATED.curie('nettadresse'),
                   model_uri=GENERATED.Kontaktopplysning_nettadresse, domain=Kontaktopplysning, range=Optional[str])

slots.Kontaktopplysning_mobilnummerUtgaar = Slot(uri=GENERATED.mobilnummerUtgaar, name="Kontaktopplysning_mobilnummerUtgaar", curie=GENERATED.curie('mobilnummerUtgaar'),
                   model_uri=GENERATED.Kontaktopplysning_mobilnummerUtgaar, domain=Kontaktopplysning, range=Optional[Union[bool, Bool]])

slots.Kontaktopplysning_e_postadresseUtgaar = Slot(uri=GENERATED.e_postadresseUtgaar, name="Kontaktopplysning_e_postadresseUtgaar", curie=GENERATED.curie('e_postadresseUtgaar'),
                   model_uri=GENERATED.Kontaktopplysning_e_postadresseUtgaar, domain=Kontaktopplysning, range=Optional[Union[bool, Bool]])

slots.Kontaktopplysning_nettadresseUtgaar = Slot(uri=GENERATED.nettadresseUtgaar, name="Kontaktopplysning_nettadresseUtgaar", curie=GENERATED.curie('nettadresseUtgaar'),
                   model_uri=GENERATED.Kontaktopplysning_nettadresseUtgaar, domain=Kontaktopplysning, range=Optional[Union[bool, Bool]])

slots.Kontaktopplysning_telefonnummer = Slot(uri=GENERATED.telefonnummer, name="Kontaktopplysning_telefonnummer", curie=GENERATED.curie('telefonnummer'),
                   model_uri=GENERATED.Kontaktopplysning_telefonnummer, domain=Kontaktopplysning, range=Optional[Union[str, TelefonnummerId]])

slots.Kontaktopplysning_telefonnummerUtgaar = Slot(uri=GENERATED.telefonnummerUtgaar, name="Kontaktopplysning_telefonnummerUtgaar", curie=GENERATED.curie('telefonnummerUtgaar'),
                   model_uri=GENERATED.Kontaktopplysning_telefonnummerUtgaar, domain=Kontaktopplysning, range=Optional[Union[bool, Bool]])

slots.Telefonnummer_internasjonaltPrefiks = Slot(uri=GENERATED.internasjonaltPrefiks, name="Telefonnummer_internasjonaltPrefiks", curie=GENERATED.curie('internasjonaltPrefiks'),
                   model_uri=GENERATED.Telefonnummer_internasjonaltPrefiks, domain=Telefonnummer, range=Optional[str])

slots.Telefonnummer_nasjonaltNummer = Slot(uri=GENERATED.nasjonaltNummer, name="Telefonnummer_nasjonaltNummer", curie=GENERATED.curie('nasjonaltNummer'),
                   model_uri=GENERATED.Telefonnummer_nasjonaltNummer, domain=Telefonnummer, range=str)

slots.VirksomhetsinformasjonUnderenhet_oppstartsdato = Slot(uri=GENERATED.oppstartsdato, name="VirksomhetsinformasjonUnderenhet_oppstartsdato", curie=GENERATED.curie('oppstartsdato'),
                   model_uri=GENERATED.VirksomhetsinformasjonUnderenhet_oppstartsdato, domain=VirksomhetsinformasjonUnderenhet, range=Optional[str])

slots.VirksomhetsinformasjonUnderenhet_navn = Slot(uri=GENERATED.navn, name="VirksomhetsinformasjonUnderenhet_navn", curie=GENERATED.curie('navn'),
                   model_uri=GENERATED.VirksomhetsinformasjonUnderenhet_navn, domain=VirksomhetsinformasjonUnderenhet, range=Optional[str])

slots.VirksomhetsinformasjonUnderenhet_organisasjonsnummer = Slot(uri=GENERATED.organisasjonsnummer, name="VirksomhetsinformasjonUnderenhet_organisasjonsnummer", curie=GENERATED.curie('organisasjonsnummer'),
                   model_uri=GENERATED.VirksomhetsinformasjonUnderenhet_organisasjonsnummer, domain=VirksomhetsinformasjonUnderenhet, range=Optional[str])

slots.VirksomhetsinformasjonUnderenhet_nedleggelsesdato = Slot(uri=GENERATED.nedleggelsesdato, name="VirksomhetsinformasjonUnderenhet_nedleggelsesdato", curie=GENERATED.curie('nedleggelsesdato'),
                   model_uri=GENERATED.VirksomhetsinformasjonUnderenhet_nedleggelsesdato, domain=VirksomhetsinformasjonUnderenhet, range=Optional[str])

slots.VirksomhetsinformasjonUnderenhet_beliggenhetsadresse = Slot(uri=GENERATED.beliggenhetsadresse, name="VirksomhetsinformasjonUnderenhet_beliggenhetsadresse", curie=GENERATED.curie('beliggenhetsadresse'),
                   model_uri=GENERATED.VirksomhetsinformasjonUnderenhet_beliggenhetsadresse, domain=VirksomhetsinformasjonUnderenhet, range=Optional[Union[str, BeliggenhetsadresseId]])

slots.VirksomhetsinformasjonUnderenhet_postadresse = Slot(uri=GENERATED.postadresse, name="VirksomhetsinformasjonUnderenhet_postadresse", curie=GENERATED.curie('postadresse'),
                   model_uri=GENERATED.VirksomhetsinformasjonUnderenhet_postadresse, domain=VirksomhetsinformasjonUnderenhet, range=Optional[Union[str, PostadresseId]])

slots.VirksomhetsinformasjonUnderenhet_kontaktopplysning = Slot(uri=GENERATED.kontaktopplysning, name="VirksomhetsinformasjonUnderenhet_kontaktopplysning", curie=GENERATED.curie('kontaktopplysning'),
                   model_uri=GENERATED.VirksomhetsinformasjonUnderenhet_kontaktopplysning, domain=VirksomhetsinformasjonUnderenhet, range=Optional[Union[str, KontaktopplysningId]])

slots.VirksomhetsinformasjonUnderenhet_aktivitet = Slot(uri=GENERATED.aktivitet, name="VirksomhetsinformasjonUnderenhet_aktivitet", curie=GENERATED.curie('aktivitet'),
                   model_uri=GENERATED.VirksomhetsinformasjonUnderenhet_aktivitet, domain=VirksomhetsinformasjonUnderenhet, range=Optional[Union[str, AktivitetId]])

slots.Beliggenhetsadresse_coNavn = Slot(uri=GENERATED.coNavn, name="Beliggenhetsadresse_coNavn", curie=GENERATED.curie('coNavn'),
                   model_uri=GENERATED.Beliggenhetsadresse_coNavn, domain=Beliggenhetsadresse, range=Optional[str])

slots.Beliggenhetsadresse_vNavn = Slot(uri=GENERATED.vNavn, name="Beliggenhetsadresse_vNavn", curie=GENERATED.curie('vNavn'),
                   model_uri=GENERATED.Beliggenhetsadresse_vNavn, domain=Beliggenhetsadresse, range=Optional[str])

slots.Beliggenhetsadresse_vegadresse = Slot(uri=GENERATED.vegadresse, name="Beliggenhetsadresse_vegadresse", curie=GENERATED.curie('vegadresse'),
                   model_uri=GENERATED.Beliggenhetsadresse_vegadresse, domain=Beliggenhetsadresse, range=Optional[Union[str, VegadresseId]])

slots.Beliggenhetsadresse_stedsadresse = Slot(uri=GENERATED.stedsadresse, name="Beliggenhetsadresse_stedsadresse", curie=GENERATED.curie('stedsadresse'),
                   model_uri=GENERATED.Beliggenhetsadresse_stedsadresse, domain=Beliggenhetsadresse, range=Optional[Union[str, StedsadresseId]])

slots.Aktivitet_aktivitet = Slot(uri=GENERATED.aktivitet, name="Aktivitet_aktivitet", curie=GENERATED.curie('aktivitet'),
                   model_uri=GENERATED.Aktivitet_aktivitet, domain=Aktivitet, range=Union[str, AktivitetId])

slots.Aktivitet_datoGyldigFra = Slot(uri=GENERATED.datoGyldigFra, name="Aktivitet_datoGyldigFra", curie=GENERATED.curie('datoGyldigFra'),
                   model_uri=GENERATED.Aktivitet_datoGyldigFra, domain=Aktivitet, range=Optional[str])

slots.TypeAktivitet_rekkefoelge = Slot(uri=GENERATED.rekkefoelge, name="TypeAktivitet_rekkefoelge", curie=GENERATED.curie('rekkefoelge'),
                   model_uri=GENERATED.TypeAktivitet_rekkefoelge, domain=TypeAktivitet, range=int)

slots.TypeAktivitet_aktivitetskode = Slot(uri=GENERATED.aktivitetskode, name="TypeAktivitet_aktivitetskode", curie=GENERATED.curie('aktivitetskode'),
                   model_uri=GENERATED.TypeAktivitet_aktivitetskode, domain=TypeAktivitet, range=Optional[int])

slots.TypeAktivitet_tekst = Slot(uri=GENERATED.tekst, name="TypeAktivitet_tekst", curie=GENERATED.curie('tekst'),
                   model_uri=GENERATED.TypeAktivitet_tekst, domain=TypeAktivitet, range=str)

slots.Omdanning_nyOrganisasjonsform = Slot(uri=GENERATED.nyOrganisasjonsform, name="Omdanning_nyOrganisasjonsform", curie=GENERATED.curie('nyOrganisasjonsform'),
                   model_uri=GENERATED.Omdanning_nyOrganisasjonsform, domain=Omdanning, range=str)

slots.Rolletypegruppe_rollegruppe = Slot(uri=GENERATED.rollegruppe, name="Rolletypegruppe_rollegruppe", curie=GENERATED.curie('rollegruppe'),
                   model_uri=GENERATED.Rolletypegruppe_rollegruppe, domain=Rolletypegruppe, range=str)

slots.Rolletypegruppe_utgaar = Slot(uri=GENERATED.utgaar, name="Rolletypegruppe_utgaar", curie=GENERATED.curie('utgaar'),
                   model_uri=GENERATED.Rolletypegruppe_utgaar, domain=Rolletypegruppe, range=Optional[Union[bool, Bool]])

slots.Rolletypegruppe_kjoennssammensetningAnsattvalgte = Slot(uri=GENERATED.kjoennssammensetningAnsattvalgte, name="Rolletypegruppe_kjoennssammensetningAnsattvalgte", curie=GENERATED.curie('kjoennssammensetningAnsattvalgte'),
                   model_uri=GENERATED.Rolletypegruppe_kjoennssammensetningAnsattvalgte, domain=Rolletypegruppe, range=Optional[Union[bool, Bool]])

slots.Rolletypegruppe_kjoennssammensetningStyre = Slot(uri=GENERATED.kjoennssammensetningStyre, name="Rolletypegruppe_kjoennssammensetningStyre", curie=GENERATED.curie('kjoennssammensetningStyre'),
                   model_uri=GENERATED.Rolletypegruppe_kjoennssammensetningStyre, domain=Rolletypegruppe, range=Optional[Union[bool, Bool]])

slots.Rolletypegruppe_rolle = Slot(uri=GENERATED.rolle, name="Rolletypegruppe_rolle", curie=GENERATED.curie('rolle'),
                   model_uri=GENERATED.Rolletypegruppe_rolle, domain=Rolletypegruppe, range=Optional[Union[Union[str, RolleId], list[Union[str, RolleId]]]])

slots.Rolletypegruppe_bekreftelseProtokoll = Slot(uri=GENERATED.bekreftelseProtokoll, name="Rolletypegruppe_bekreftelseProtokoll", curie=GENERATED.curie('bekreftelseProtokoll'),
                   model_uri=GENERATED.Rolletypegruppe_bekreftelseProtokoll, domain=Rolletypegruppe, range=Optional[Union[bool, Bool]])

slots.Rolle_rolletype = Slot(uri=GENERATED.rolletype, name="Rolle_rolletype", curie=GENERATED.curie('rolletype'),
                   model_uri=GENERATED.Rolle_rolletype, domain=Rolle, range=Union[str, "Rolletype"])

slots.Rolle_tildelerAvRolle = Slot(uri=GENERATED.tildelerAvRolle, name="Rolle_tildelerAvRolle", curie=GENERATED.curie('tildelerAvRolle'),
                   model_uri=GENERATED.Rolle_tildelerAvRolle, domain=Rolle, range=Optional[str])

slots.Rolle_rolleinnehaver = Slot(uri=GENERATED.rolleinnehaver, name="Rolle_rolleinnehaver", curie=GENERATED.curie('rolleinnehaver'),
                   model_uri=GENERATED.Rolle_rolleinnehaver, domain=Rolle, range=Union[str, RolleinnehaverId])

slots.Rolleinnehaver_oenskerAAFratre = Slot(uri=GENERATED.oenskerAAFratre, name="Rolleinnehaver_oenskerAAFratre", curie=GENERATED.curie('oenskerAAFratre'),
                   model_uri=GENERATED.Rolleinnehaver_oenskerAAFratre, domain=Rolleinnehaver, range=Optional[Union[bool, Bool]])

slots.Rolleinnehaver_ansvarsandel = Slot(uri=GENERATED.ansvarsandel, name="Rolleinnehaver_ansvarsandel", curie=GENERATED.curie('ansvarsandel'),
                   model_uri=GENERATED.Rolleinnehaver_ansvarsandel, domain=Rolleinnehaver, range=Optional[Union[str, AnsvarsandelId]])

slots.Rolleinnehaver_avdelingskontor = Slot(uri=GENERATED.avdelingskontor, name="Rolleinnehaver_avdelingskontor", curie=GENERATED.curie('avdelingskontor'),
                   model_uri=GENERATED.Rolleinnehaver_avdelingskontor, domain=Rolleinnehaver, range=Optional[str])

slots.Rolleinnehaver_fratredenErVarslet = Slot(uri=GENERATED.fratredenErVarslet, name="Rolleinnehaver_fratredenErVarslet", curie=GENERATED.curie('fratredenErVarslet'),
                   model_uri=GENERATED.Rolleinnehaver_fratredenErVarslet, domain=Rolleinnehaver, range=Optional[Union[bool, Bool]])

slots.Rolleinnehaver_valgtAv = Slot(uri=GENERATED.valgtAv, name="Rolleinnehaver_valgtAv", curie=GENERATED.curie('valgtAv'),
                   model_uri=GENERATED.Rolleinnehaver_valgtAv, domain=Rolleinnehaver, range=Optional[str])

slots.Rolleinnehaver_virksomhet = Slot(uri=GENERATED.virksomhet, name="Rolleinnehaver_virksomhet", curie=GENERATED.curie('virksomhet'),
                   model_uri=GENERATED.Rolleinnehaver_virksomhet, domain=Rolleinnehaver, range=Optional[Union[str, VirksomhetId]])

slots.Rolleinnehaver_person = Slot(uri=GENERATED.person, name="Rolleinnehaver_person", curie=GENERATED.curie('person'),
                   model_uri=GENERATED.Rolleinnehaver_person, domain=Rolleinnehaver, range=Optional[Union[str, PersonId]])

slots.Ansvarsandel_broek = Slot(uri=GENERATED.broek, name="Ansvarsandel_broek", curie=GENERATED.curie('broek'),
                   model_uri=GENERATED.Ansvarsandel_broek, domain=Ansvarsandel, range=Optional[Union[str, BroekId]])

slots.Ansvarsandel_prosent = Slot(uri=GENERATED.prosent, name="Ansvarsandel_prosent", curie=GENERATED.curie('prosent'),
                   model_uri=GENERATED.Ansvarsandel_prosent, domain=Ansvarsandel, range=Optional[float])

slots.Broek_teller = Slot(uri=GENERATED.teller, name="Broek_teller", curie=GENERATED.curie('teller'),
                   model_uri=GENERATED.Broek_teller, domain=Broek, range=Optional[int])

slots.Broek_nevner = Slot(uri=GENERATED.nevner, name="Broek_nevner", curie=GENERATED.curie('nevner'),
                   model_uri=GENERATED.Broek_nevner, domain=Broek, range=Optional[int])

slots.Virksomhet_virksomhetsidentifikator = Slot(uri=GENERATED.virksomhetsidentifikator, name="Virksomhet_virksomhetsidentifikator", curie=GENERATED.curie('virksomhetsidentifikator'),
                   model_uri=GENERATED.Virksomhet_virksomhetsidentifikator, domain=Virksomhet, range=str)

slots.Virksomhet_navn = Slot(uri=GENERATED.navn, name="Virksomhet_navn", curie=GENERATED.curie('navn'),
                   model_uri=GENERATED.Virksomhet_navn, domain=Virksomhet, range=Optional[str])

slots.Person_mappingId = Slot(uri=GENERATED.mappingId, name="Person_mappingId", curie=GENERATED.curie('mappingId'),
                   model_uri=GENERATED.Person_mappingId, domain=Person, range=str)

slots.Person_fulltNavn = Slot(uri=GENERATED.fulltNavn, name="Person_fulltNavn", curie=GENERATED.curie('fulltNavn'),
                   model_uri=GENERATED.Person_fulltNavn, domain=Person, range=str)

slots.Prokura_utgaar = Slot(uri=GENERATED.utgaar, name="Prokura_utgaar", curie=GENERATED.curie('utgaar'),
                   model_uri=GENERATED.Prokura_utgaar, domain=Prokura, range=Optional[Union[bool, Bool]])

slots.Prokura_prokurabestemmelse = Slot(uri=GENERATED.prokurabestemmelse, name="Prokura_prokurabestemmelse", curie=GENERATED.curie('prokurabestemmelse'),
                   model_uri=GENERATED.Prokura_prokurabestemmelse, domain=Prokura, range=Optional[Union[Union[str, ProkurabestemmelseId], list[Union[str, ProkurabestemmelseId]]]])

slots.Prokura_bekreftelseProtokoll = Slot(uri=GENERATED.bekreftelseProtokoll, name="Prokura_bekreftelseProtokoll", curie=GENERATED.curie('bekreftelseProtokoll'),
                   model_uri=GENERATED.Prokura_bekreftelseProtokoll, domain=Prokura, range=Optional[Union[bool, Bool]])

slots.Prokurabestemmelse_regel = Slot(uri=GENERATED.regel, name="Prokurabestemmelse_regel", curie=GENERATED.curie('regel'),
                   model_uri=GENERATED.Prokurabestemmelse_regel, domain=Prokurabestemmelse, range=str)

slots.Prokurabestemmelse_rollesett = Slot(uri=GENERATED.rollesett, name="Prokurabestemmelse_rollesett", curie=GENERATED.curie('rollesett'),
                   model_uri=GENERATED.Prokurabestemmelse_rollesett, domain=Prokurabestemmelse, range=Union[Union[str, RollesettId], list[Union[str, RollesettId]]])

slots.Rollesett_rolletype = Slot(uri=GENERATED.rolletype, name="Rollesett_rolletype", curie=GENERATED.curie('rolletype'),
                   model_uri=GENERATED.Rollesett_rolletype, domain=Rollesett, range=Union[str, "Rolletype"])

slots.Rollesett_signaturberettigetEllerProkurist = Slot(uri=GENERATED.signaturberettigetEllerProkurist, name="Rollesett_signaturberettigetEllerProkurist", curie=GENERATED.curie('signaturberettigetEllerProkurist'),
                   model_uri=GENERATED.Rollesett_signaturberettigetEllerProkurist, domain=Rollesett, range=Optional[Union[Union[str, SignaturberettigetEllerProkuristId], list[Union[str, SignaturberettigetEllerProkuristId]]]])

slots.Rollesett_minsteMengdeangivelse = Slot(uri=GENERATED.minsteMengdeangivelse, name="Rollesett_minsteMengdeangivelse", curie=GENERATED.curie('minsteMengdeangivelse'),
                   model_uri=GENERATED.Rollesett_minsteMengdeangivelse, domain=Rollesett, range=Optional[str])

slots.Rollesett_minsteAntall = Slot(uri=GENERATED.minsteAntall, name="Rollesett_minsteAntall", curie=GENERATED.curie('minsteAntall'),
                   model_uri=GENERATED.Rollesett_minsteAntall, domain=Rollesett, range=Optional[int])

slots.SignaturberettigetEllerProkurist_virksomhet = Slot(uri=GENERATED.virksomhet, name="SignaturberettigetEllerProkurist_virksomhet", curie=GENERATED.curie('virksomhet'),
                   model_uri=GENERATED.SignaturberettigetEllerProkurist_virksomhet, domain=SignaturberettigetEllerProkurist, range=Optional[Union[str, VirksomhetId]])

slots.SignaturberettigetEllerProkurist_person = Slot(uri=GENERATED.person, name="SignaturberettigetEllerProkurist_person", curie=GENERATED.curie('person'),
                   model_uri=GENERATED.SignaturberettigetEllerProkurist_person, domain=SignaturberettigetEllerProkurist, range=Optional[Union[str, PersonId]])

slots.Signaturrett_utgaar = Slot(uri=GENERATED.utgaar, name="Signaturrett_utgaar", curie=GENERATED.curie('utgaar'),
                   model_uri=GENERATED.Signaturrett_utgaar, domain=Signaturrett, range=Optional[Union[bool, Bool]])

slots.Signaturrett_signaturrettsbestemmelsse = Slot(uri=GENERATED.signaturrettsbestemmelsse, name="Signaturrett_signaturrettsbestemmelsse", curie=GENERATED.curie('signaturrettsbestemmelsse'),
                   model_uri=GENERATED.Signaturrett_signaturrettsbestemmelsse, domain=Signaturrett, range=Optional[Union[Union[str, SignaturrettsbestemmelseId], list[Union[str, SignaturrettsbestemmelseId]]]])

slots.Signaturrett_bekreftelseProtokoll = Slot(uri=GENERATED.bekreftelseProtokoll, name="Signaturrett_bekreftelseProtokoll", curie=GENERATED.curie('bekreftelseProtokoll'),
                   model_uri=GENERATED.Signaturrett_bekreftelseProtokoll, domain=Signaturrett, range=Optional[Union[bool, Bool]])

slots.Signaturrettsbestemmelse_regel = Slot(uri=GENERATED.regel, name="Signaturrettsbestemmelse_regel", curie=GENERATED.curie('regel'),
                   model_uri=GENERATED.Signaturrettsbestemmelse_regel, domain=Signaturrettsbestemmelse, range=str)

slots.Signaturrettsbestemmelse_rollesett = Slot(uri=GENERATED.rollesett, name="Signaturrettsbestemmelse_rollesett", curie=GENERATED.curie('rollesett'),
                   model_uri=GENERATED.Signaturrettsbestemmelse_rollesett, domain=Signaturrettsbestemmelse, range=Union[Union[str, RollesettId], list[Union[str, RollesettId]]])

slots.Foretaksinformasjon_oenskesRegistrertIForetaksregisteret = Slot(uri=GENERATED.oenskesRegistrertIForetaksregisteret, name="Foretaksinformasjon_oenskesRegistrertIForetaksregisteret", curie=GENERATED.curie('oenskesRegistrertIForetaksregisteret'),
                   model_uri=GENERATED.Foretaksinformasjon_oenskesRegistrertIForetaksregisteret, domain=Foretaksinformasjon, range=Optional[Union[bool, Bool]])

slots.Foretaksinformasjon_oenskesSlettetIForetaksregisteret = Slot(uri=GENERATED.oenskesSlettetIForetaksregisteret, name="Foretaksinformasjon_oenskesSlettetIForetaksregisteret", curie=GENERATED.curie('oenskesSlettetIForetaksregisteret'),
                   model_uri=GENERATED.Foretaksinformasjon_oenskesSlettetIForetaksregisteret, domain=Foretaksinformasjon, range=Optional[Union[bool, Bool]])

slots.EierskifteAktivitet_typeEierskifte = Slot(uri=GENERATED.typeEierskifte, name="EierskifteAktivitet_typeEierskifte", curie=GENERATED.curie('typeEierskifte'),
                   model_uri=GENERATED.EierskifteAktivitet_typeEierskifte, domain=EierskifteAktivitet, range=Union[str, "TypeEierskifte"])

slots.EierskifteAktivitet_organisasjonsnummerHovedenhet = Slot(uri=GENERATED.organisasjonsnummerHovedenhet, name="EierskifteAktivitet_organisasjonsnummerHovedenhet", curie=GENERATED.curie('organisasjonsnummerHovedenhet'),
                   model_uri=GENERATED.EierskifteAktivitet_organisasjonsnummerHovedenhet, domain=EierskifteAktivitet, range=str)

slots.EierskifteAktivitet_gjelderHeleAktiviteten = Slot(uri=GENERATED.gjelderHeleAktiviteten, name="EierskifteAktivitet_gjelderHeleAktiviteten", curie=GENERATED.curie('gjelderHeleAktiviteten'),
                   model_uri=GENERATED.EierskifteAktivitet_gjelderHeleAktiviteten, domain=EierskifteAktivitet, range=Union[bool, Bool])

slots.EierskifteAktivitet_eierskiftedato = Slot(uri=GENERATED.eierskiftedato, name="EierskifteAktivitet_eierskiftedato", curie=GENERATED.curie('eierskiftedato'),
                   model_uri=GENERATED.EierskifteAktivitet_eierskiftedato, domain=EierskifteAktivitet, range=str)

slots.EierskifteAktivitet_hvilkeDeler = Slot(uri=GENERATED.hvilkeDeler, name="EierskifteAktivitet_hvilkeDeler", curie=GENERATED.curie('hvilkeDeler'),
                   model_uri=GENERATED.EierskifteAktivitet_hvilkeDeler, domain=EierskifteAktivitet, range=Optional[Union[str, DelerEierskifteId]])

slots.DelerEierskifte_beskrivelse = Slot(uri=GENERATED.beskrivelse, name="DelerEierskifte_beskrivelse", curie=GENERATED.curie('beskrivelse'),
                   model_uri=GENERATED.DelerEierskifte_beskrivelse, domain=DelerEierskifte, range=Optional[str])

slots.DelerEierskifte_underenhet = Slot(uri=GENERATED.underenhet, name="DelerEierskifte_underenhet", curie=GENERATED.curie('underenhet'),
                   model_uri=GENERATED.DelerEierskifte_underenhet, domain=DelerEierskifte, range=Optional[Union[str, list[str]]])

slots.Matrikkelnummer_kommunenummer = Slot(uri=GENERATED.kommunenummer, name="Matrikkelnummer_kommunenummer", curie=GENERATED.curie('kommunenummer'),
                   model_uri=GENERATED.Matrikkelnummer_kommunenummer, domain=Matrikkelnummer, range=Optional[str])

slots.Matrikkelnummer_gaardsnummer = Slot(uri=GENERATED.gaardsnummer, name="Matrikkelnummer_gaardsnummer", curie=GENERATED.curie('gaardsnummer'),
                   model_uri=GENERATED.Matrikkelnummer_gaardsnummer, domain=Matrikkelnummer, range=Optional[int])

slots.Matrikkelnummer_bruksnummer = Slot(uri=GENERATED.bruksnummer, name="Matrikkelnummer_bruksnummer", curie=GENERATED.curie('bruksnummer'),
                   model_uri=GENERATED.Matrikkelnummer_bruksnummer, domain=Matrikkelnummer, range=Optional[int])

slots.Matrikkelnummer_festenummer = Slot(uri=GENERATED.festenummer, name="Matrikkelnummer_festenummer", curie=GENERATED.curie('festenummer'),
                   model_uri=GENERATED.Matrikkelnummer_festenummer, domain=Matrikkelnummer, range=Optional[int])

slots.Innsender_virksomhet = Slot(uri=GENERATED.virksomhet, name="Innsender_virksomhet", curie=GENERATED.curie('virksomhet'),
                   model_uri=GENERATED.Innsender_virksomhet, domain=Innsender, range=Optional[Union[str, VirksomhetId]])

slots.Innsender_person = Slot(uri=GENERATED.person, name="Innsender_person", curie=GENERATED.curie('person'),
                   model_uri=GENERATED.Innsender_person, domain=Innsender, range=Optional[Union[str, PersonId]])

slots.Innsender_e_postadresse = Slot(uri=GENERATED.e_postadresse, name="Innsender_e_postadresse", curie=GENERATED.curie('e_postadresse'),
                   model_uri=GENERATED.Innsender_e_postadresse, domain=Innsender, range=Optional[str])

slots.Innsender_mobilnummer = Slot(uri=GENERATED.mobilnummer, name="Innsender_mobilnummer", curie=GENERATED.curie('mobilnummer'),
                   model_uri=GENERATED.Innsender_mobilnummer, domain=Innsender, range=Optional[Union[str, MobilnummerId]])

slots.Innsender_test = Slot(uri=GENERATED.test, name="Innsender_test", curie=GENERATED.curie('test'),
                   model_uri=GENERATED.Innsender_test, domain=Innsender, range=str)

slots.Fagsystemreferanse_fagsystemID = Slot(uri=GENERATED.fagsystemID, name="Fagsystemreferanse_fagsystemID", curie=GENERATED.curie('fagsystemID'),
                   model_uri=GENERATED.Fagsystemreferanse_fagsystemID, domain=Fagsystemreferanse, range=str)

slots.Fagsystemreferanse_orgnrFagsystem = Slot(uri=GENERATED.orgnrFagsystem, name="Fagsystemreferanse_orgnrFagsystem", curie=GENERATED.curie('orgnrFagsystem'),
                   model_uri=GENERATED.Fagsystemreferanse_orgnrFagsystem, domain=Fagsystemreferanse, range=str)

slots.Fagsystemreferanse_referanseFagsystem = Slot(uri=GENERATED.referanseFagsystem, name="Fagsystemreferanse_referanseFagsystem", curie=GENERATED.curie('referanseFagsystem'),
                   model_uri=GENERATED.Fagsystemreferanse_referanseFagsystem, domain=Fagsystemreferanse, range=str)

slots.Gebyransvarlig_eksternFakturareferanse = Slot(uri=GENERATED.eksternFakturareferanse, name="Gebyransvarlig_eksternFakturareferanse", curie=GENERATED.curie('eksternFakturareferanse'),
                   model_uri=GENERATED.Gebyransvarlig_eksternFakturareferanse, domain=Gebyransvarlig, range=Optional[str])

slots.Gebyransvarlig_gebyransvarligType = Slot(uri=GENERATED.gebyransvarligType, name="Gebyransvarlig_gebyransvarligType", curie=GENERATED.curie('gebyransvarligType'),
                   model_uri=GENERATED.Gebyransvarlig_gebyransvarligType, domain=Gebyransvarlig, range=Union[str, "GebyransvarligType"])

slots.Gebyransvarlig_virksomhet = Slot(uri=GENERATED.virksomhet, name="Gebyransvarlig_virksomhet", curie=GENERATED.curie('virksomhet'),
                   model_uri=GENERATED.Gebyransvarlig_virksomhet, domain=Gebyransvarlig, range=Optional[Union[str, VirksomhetId]])

slots.Gebyransvarlig_person = Slot(uri=GENERATED.person, name="Gebyransvarlig_person", curie=GENERATED.curie('person'),
                   model_uri=GENERATED.Gebyransvarlig_person, domain=Gebyransvarlig, range=Optional[Union[str, PersonId]])

slots.Gebyransvarlig_mobilnummer = Slot(uri=GENERATED.mobilnummer, name="Gebyransvarlig_mobilnummer", curie=GENERATED.curie('mobilnummer'),
                   model_uri=GENERATED.Gebyransvarlig_mobilnummer, domain=Gebyransvarlig, range=Optional[Union[str, MobilnummerId]])

slots.Gebyransvarlig_e_postadresse = Slot(uri=GENERATED.e_postadresse, name="Gebyransvarlig_e_postadresse", curie=GENERATED.curie('e_postadresse'),
                   model_uri=GENERATED.Gebyransvarlig_e_postadresse, domain=Gebyransvarlig, range=Optional[str])

