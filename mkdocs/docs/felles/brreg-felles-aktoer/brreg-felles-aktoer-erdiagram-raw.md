```mermaid
erDiagram
Adressenummer {
    uriorcurie id  
    Husbokstav bokstav  
    Husnummer nummer  
}
Aktoer {
    uriorcurie id  
    string identifikator  
}
DigitalAdresse {
    uriorcurie id  
    string identifikator  
    string type  
}
EPostadresse {
    string brukernavn  
    string domenenavn  
    uriorcurie id  
    string identifikator  
    string type  
}
Fylke {
    uriorcurie id  
    string fylkesnavn  
    Fylkesnummer fylkesnummer  
}
GeografiskAdresse {
    uriorcurie id  
    string br_adresse_id  
    string co_navn  
    string type  
}
IPAdresse {
    string ip_nummer  
    uriorcurie id  
    string identifikator  
    string type  
}
InternasjonalAdresse {
    string adresseidentifikator  
    string adressenavn  
    string adressenummer_tekst  
    string boenhet  
    string by_eller_stedsnavn  
    string bygning  
    string distrikt_eller_bydel  
    string etasjenummer  
    string fri_adressetekst  
    Landkode landkode  
    string postboks  
    string postkode  
    string region  
    uriorcurie id  
    string br_adresse_id  
    string co_navn  
    string type  
}
Kommune {
    uriorcurie id  
    string kommunenavn  
    Kommunenummer kommunenummer  
}
Kontaktinformasjon {
    uriorcurie id  
}
Matrikkeladresse {
    string adressetilleggsnavn  
    Bruksenhetsnummer bruksenhetsnummer  
    string matrikkeladresse_id  
    integer undernummer  
    uriorcurie id  
    string br_adresse_id  
    string co_navn  
    string type  
}
Matrikkelnummer {
    uriorcurie id  
    integer bruksnummer  
    integer festenummer  
    integer gaardsnummer  
    Kommunenummer kommunenummer  
    integer seksjonsnummer  
}
Meldingsboks {
    string meldingsbokstype  
    uriorcurie id  
    string identifikator  
    string type  
}
Mobiltelefonnummer {
    NasjonaltNummer nasjonalt_nummer  
    PrefiksMedNasjonalKode prefiks_med_nasjonal_kode  
    uriorcurie id  
    string identifikator  
    string type  
}
Nettadresse {
    string domenenavn  
    string filsti  
    string protokoll  
    uriorcurie id  
    string identifikator  
    string type  
}
Person {
    BRPersonId br_person_id  
    Foedselsnummer foedsel_eller_d_nummer  
    PersonstatusType personstatus  
    Landkode statsborgerskap  
    uriorcurie id  
    string identifikator  
}
Personidentifikator {
    uriorcurie id  
    PersonidentifikatorType personidentifikator_type  
    string verdi  
}
Personnavn {
    uriorcurie id  
    string etternavn  
    string fornavn  
    string mellomnavn  
}
Postboksadresse {
    string anleggsnavn  
    Postboksnummer postboksnummer  
    uriorcurie id  
    string br_adresse_id  
    string co_navn  
    string type  
}
Poststed {
    uriorcurie id  
    string navn  
    Postnummer postnummer  
}
Relasjon {
    uriorcurie id  
    string type  
}
Rolle {
    uriorcurie id  
    string type  
}
Rolletypegruppe {
    uriorcurie id  
    string type  
}
Stedsadresse {
    string stedsnavn  
    uriorcurie id  
    string br_adresse_id  
    string co_navn  
    string type  
}
Telefonnummer {
    NasjonaltNummer nasjonalt_nummer  
    PrefiksMedNasjonalKode prefiks_med_nasjonal_kode  
    uriorcurie id  
    string identifikator  
    string type  
}
Vegadresse {
    string adressenavn  
    string adressetilleggsnavn  
    Bruksenhetsnummer bruksenhetsnummer  
    string kort_adressenavn  
    string vegadresse_id  
    uriorcurie id  
    string br_adresse_id  
    string co_navn  
    string type  
}
Virksomhet {
    Organisasjonsnummer organisasjonsnummer  
    Virksomhetsnavn virksomhetsnavn  
    Virksomhetsstatus virksomhetsstatus  
    uriorcurie id  
    string identifikator  
}
Virksomhetsidentifikator {
    uriorcurie id  
    string verdi  
    VirksomhetsidentifikatorType virksomhetsidentifikator_type  
}

Aktoer ||--|o DigitalAdresse : "digital_adresse"
Aktoer ||--|o GeografiskAdresse : "geografisk_adresse"
Aktoer ||--|o Kontaktinformasjon : "kontaktinformasjon"
Aktoer ||--}o Relasjon : "relasjon"
Aktoer ||--}o Rolle : "rolle"
Kontaktinformasjon ||--|o DigitalAdresse : "digital_adresse"
Kontaktinformasjon ||--|o GeografiskAdresse : "geografisk_adresse"
Matrikkeladresse ||--|o Matrikkelnummer : "matrikkelnummer"
Person ||--|o DigitalAdresse : "digital_adresse"
Person ||--|o GeografiskAdresse : "geografisk_adresse"
Person ||--|o Kontaktinformasjon : "kontaktinformasjon"
Person ||--|o Personidentifikator : "personidentifikator"
Person ||--|o Personnavn : "personnavn"
Person ||--}o Relasjon : "relasjon"
Person ||--}o Rolle : "rolle"
Postboksadresse ||--|o Kommune : "kommune"
Postboksadresse ||--|o Poststed : "poststed"
Relasjon ||--|o Aktoer : "aktoer"
Rolle ||--|o Aktoer : "rolleinnehaver"
Rolle ||--|o DigitalAdresse : "digital_adresse"
Rolle ||--|o GeografiskAdresse : "geografisk_adresse"
Rolle ||--|o Kontaktinformasjon : "kontaktinformasjon"
Rolle ||--|o Rolletypegruppe : "rolletypegruppe"
Rolletypegruppe ||--}o Rolle : "rolle"
Stedsadresse ||--|o Kommune : "kommune"
Stedsadresse ||--|o Poststed : "poststed"
Vegadresse ||--|o Adressenummer : "adressenummer"
Vegadresse ||--|o Fylke : "fylke"
Vegadresse ||--|o Kommune : "kommune"
Vegadresse ||--|o Poststed : "poststed"
Virksomhet ||--|o DigitalAdresse : "digital_adresse"
Virksomhet ||--|o GeografiskAdresse : "geografisk_adresse"
Virksomhet ||--|o Kontaktinformasjon : "kontaktinformasjon"
Virksomhet ||--|o Virksomhetsidentifikator : "virksomhetsidentifikator"
Virksomhet ||--}o Relasjon : "relasjon"
Virksomhet ||--}o Rolle : "rolle"

```

