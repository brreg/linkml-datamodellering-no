```mermaid
erDiagram
Adressenummer {
    uriorcurie id  
    Husbokstav bokstav  
}
Aktivitet {
    uriorcurie id  
    Dato datoGyldigFra  
}
Ansvarsandel {
    uriorcurie id  
    float prosent  
}
Beliggenhetsadresse {
    uriorcurie id  
    string coNavn  
    string vNavn  
}
Broek {
    uriorcurie id  
    integer nevner  
    integer teller  
}
DelerEierskifte {
    uriorcurie id  
    string beskrivelse  
    OrganisasjonsnummerList underenhet  
}
EierskifteAktivitet {
    uriorcurie id  
    Dato eierskiftedato  
    boolean gjelderHeleAktiviteten  
    Organisasjonsnummer organisasjonsnummerHovedenhet  
    TypeEierskifte typeEierskifte  
}
Fagsystemreferanse {
    uriorcurie id  
    FagsystemId fagsystemID  
    Organisasjonsnummer orgnrFagsystem  
    Tekst50 referanseFagsystem  
}
Foretaksinformasjon {
    uriorcurie id  
    boolean oenskesRegistrertIForetaksregisteret  
    boolean oenskesSlettetIForetaksregisteret  
}
Forretningsadresse {
    uriorcurie id  
    string coNavn  
    boolean utgaar  
    string vNavn  
}
Gebyransvarlig {
    uriorcurie id  
    E_postadresse e_postadresse  
    string eksternFakturareferanse  
    GebyransvarligType gebyransvarligType  
}
Innrapportering {
    uriorcurie id  
    InnsendertjenesteType innsendertjenste  
    DatoKlokkeslett innsendingstidspunkt  
    URL lenkeForEttersending  
    Maalform maalformForTilbakemelding  
    Tjenestevariant tjenestevariant  
    Versjonsnummer versjon  
}
Innsender {
    uriorcurie id  
    E_postadresse e_postadresse  
    string test  
}
InternasjonalAdresse {
    uriorcurie id  
    string adresseidentifikator  
    string adressenavn  
    string adressenummer  
    string boenhet  
    string byEllerStedsnavn  
    string bygning  
    string distriktEllerBydel  
    string etasjenummer  
    stringList friAdressetekst  
    Landkode landkode  
    string postboks  
    string postkode  
    string region  
}
Kontaktopplysning {
    uriorcurie id  
    E_postadresse e_postadresse  
    boolean e_postadresseUtgaar  
    boolean mobilnummerUtgaar  
    URL nettadresse  
    boolean nettadresseUtgaar  
    boolean telefonnummerUtgaar  
}
Matrikkelnummer {
    uriorcurie id  
    integer bruksnummer  
    integer festenummer  
    integer gaardsnummer  
    Kommunenummer kommunenummer  
}
Mobilnummer {
    uriorcurie id  
    InternasjonaltPrefiks internasjonaltPrefiks  
    NasjonaltNummer nasjonaltNummer  
}
Omdanning {
    uriorcurie id  
    Organisasjonsform nyOrganisasjonsform  
}
Person {
    uriorcurie id  
    string fulltNavn  
    PersonMappingId mappingId  
}
Postadresse {
    uriorcurie id  
    string coNavn  
    boolean utgaar  
    string vNavn  
}
Postboksadresse {
    uriorcurie id  
    Kommunenummer kommunenummer  
    string postboksanleggsnavn  
    Postboksnummer postboksnummer  
    Postnummer postnummer  
}
Prokura {
    uriorcurie id  
    boolean bekreftelseProtokoll  
    boolean utgaar  
}
Prokurabestemmelse {
    uriorcurie id  
    SignaturrettEllerProkuraregel regel  
}
Rolle {
    uriorcurie id  
    Rolletype rolletype  
    PersonMappingId tildelerAvRolle  
}
Rolleinnehaver {
    uriorcurie id  
    Organisasjonsnummer avdelingskontor  
    boolean fratredenErVarslet  
    boolean oenskerAAFratre  
    ValgtAv valgtAv  
}
Rollesett {
    uriorcurie id  
    integer minsteAntall  
    Mengdeangivelse minsteMengdeangivelse  
    Rolletype rolletype  
}
Rolletypegruppe {
    uriorcurie id  
    boolean bekreftelseProtokoll  
    boolean kjoennssammensetningAnsattvalgte  
    boolean kjoennssammensetningStyre  
    Rolletypegruppe_2 rollegruppe  
    boolean utgaar  
}
SignaturberettigetEllerProkurist {
    uriorcurie id  
}
Signaturrett {
    uriorcurie id  
    boolean bekreftelseProtokoll  
    boolean utgaar  
}
Signaturrettsbestemmelse {
    uriorcurie id  
    SignaturrettEllerProkuraregel regel  
}
Signering {
    uriorcurie id  
}
Stedsadresse {
    uriorcurie id  
    Kommunenummer kommunenummer  
    Postnummer postnummer  
    string stedsnavn  
}
Telefonnummer {
    uriorcurie id  
    InternasjonaltPrefiks internasjonaltPrefiks  
    NasjonaltNummer nasjonaltNummer  
}
TypeAktivitet {
    uriorcurie id  
    Aktivitetskode aktivitetskode  
    integer rekkefoelge  
    Tekst1000 tekst  
}
Varslingsadresse {
    uriorcurie id  
    E_postadresse e_postadresse  
}
Vegadresse {
    uriorcurie id  
    string adressenavn  
    string adressetilleggsnavn  
    Bruksenhetsnummer bruksenhetsnummer  
    Kommunenummer kommunenummer  
    Postnummer postnummer  
    string vegadresseId  
}
Virksomhet {
    uriorcurie id  
    Virksomhetsnavn navn  
    Organisasjonsnummer virksomhetsidentifikator  
}
VirksomhetsinformasjonHovedenhet {
    uriorcurie id  
    Ansvarsform ansvarsform  
    boolean bekreftelseProtokollOpploesningOgOmgjoering  
    boolean bekreftelseProtokollSletting  
    Dato datoForAvtale  
    string formaal  
    boolean harAnsvarsbegrensning  
    Maalform maalform  
    boolean meldtOmgjoeringAvOpploesning  
    boolean meldtOpploesning  
    Virksomhetsnavn navn  
    boolean oppfyllerKravTilNaeringsvirksomhet  
    Organisasjonsform organisasjonsform  
    Organisasjonsnummer organisasjonsnummer  
    TilknyttetRegistertypeList registrertITilknyttetRegister  
    Dato stiftelsesdato  
    Dato vedtektsdato  
    boolean venterAAFaaAnsatte  
    Virksomhetstype virksomhetstype  
}
VirksomhetsinformasjonUnderenhet {
    uriorcurie id  
    Virksomhetsnavn navn  
    Dato nedleggelsesdato  
    Dato oppstartsdato  
    Organisasjonsnummer organisasjonsnummer  
}

Adressenummer ||--|| Adressenummer : "nummer"
Aktivitet ||--|| Aktivitet : "aktivitet"
Ansvarsandel ||--|o Broek : "broek"
Beliggenhetsadresse ||--|o Stedsadresse : "stedsadresse"
Beliggenhetsadresse ||--|o Vegadresse : "vegadresse"
EierskifteAktivitet ||--|o DelerEierskifte : "hvilkeDeler"
Forretningsadresse ||--|o Stedsadresse : "stedsadresse"
Forretningsadresse ||--|o Vegadresse : "vegadresse"
Gebyransvarlig ||--|o Mobilnummer : "mobilnummer"
Gebyransvarlig ||--|o Person : "person"
Gebyransvarlig ||--|o Virksomhet : "virksomhet"
Innrapportering ||--|o Fagsystemreferanse : "fagsystemReferanse"
Innrapportering ||--|o Gebyransvarlig : "gebyransvarlig"
Innrapportering ||--|o Signering : "signering"
Innrapportering ||--|| Innsender : "innsender"
Innrapportering ||--|| VirksomhetsinformasjonHovedenhet : "virksomhetsinformasjon"
Innsender ||--|o Mobilnummer : "mobilnummer"
Innsender ||--|o Person : "person"
Innsender ||--|o Virksomhet : "virksomhet"
Kontaktopplysning ||--|o Mobilnummer : "mobilnummer"
Kontaktopplysning ||--|o Telefonnummer : "telefonnummer"
Postadresse ||--|o InternasjonalAdresse : "internasjonalAdresse"
Postadresse ||--|o Postboksadresse : "postboksadresse"
Postadresse ||--|o Stedsadresse : "stedsadresse"
Postadresse ||--|o Vegadresse : "vegadresse"
Prokura ||--}o Prokurabestemmelse : "prokurabestemmelse"
Prokurabestemmelse ||--}| Rollesett : "rollesett"
Rolle ||--|| Rolleinnehaver : "rolleinnehaver"
Rolleinnehaver ||--|o Ansvarsandel : "ansvarsandel"
Rolleinnehaver ||--|o Person : "person"
Rolleinnehaver ||--|o Virksomhet : "virksomhet"
Rollesett ||--}o SignaturberettigetEllerProkurist : "signaturberettigetEllerProkurist"
Rolletypegruppe ||--}o Rolle : "rolle"
SignaturberettigetEllerProkurist ||--|o Person : "person"
SignaturberettigetEllerProkurist ||--|o Virksomhet : "virksomhet"
Signaturrett ||--}o Signaturrettsbestemmelse : "signaturrettsbestemmelsse"
Signaturrettsbestemmelse ||--}| Rollesett : "rollesett"
Varslingsadresse ||--|o Mobilnummer : "mobilnummer"
Vegadresse ||--|| Adressenummer : "nummer"
VirksomhetsinformasjonHovedenhet ||--|o Aktivitet : "aktivitet"
VirksomhetsinformasjonHovedenhet ||--|o Foretaksinformasjon : "foretaksinformasjon"
VirksomhetsinformasjonHovedenhet ||--|o Forretningsadresse : "forretningsadresse"
VirksomhetsinformasjonHovedenhet ||--|o Kontaktopplysning : "kontaktopplysning"
VirksomhetsinformasjonHovedenhet ||--|o Omdanning : "omdanning"
VirksomhetsinformasjonHovedenhet ||--|o Postadresse : "postadresse"
VirksomhetsinformasjonHovedenhet ||--|o Prokura : "prokura"
VirksomhetsinformasjonHovedenhet ||--|o Signaturrett : "signaturrett"
VirksomhetsinformasjonHovedenhet ||--|o Varslingsadresse : "varslingsadresse"
VirksomhetsinformasjonHovedenhet ||--}o EierskifteAktivitet : "eierskifte"
VirksomhetsinformasjonHovedenhet ||--}o Matrikkelnummer : "matrikkelnummer"
VirksomhetsinformasjonHovedenhet ||--}o Rolletypegruppe : "rolletypegruppe"
VirksomhetsinformasjonHovedenhet ||--}o VirksomhetsinformasjonUnderenhet : "virksomhetsinformasjonUnderenhet"
VirksomhetsinformasjonUnderenhet ||--|o Aktivitet : "aktivitet"
VirksomhetsinformasjonUnderenhet ||--|o Beliggenhetsadresse : "beliggenhetsadresse"
VirksomhetsinformasjonUnderenhet ||--|o Kontaktopplysning : "kontaktopplysning"
VirksomhetsinformasjonUnderenhet ||--|o Postadresse : "postadresse"

```

