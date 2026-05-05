```mermaid
erDiagram
Adresse {
    uriorcurie id  
    stringList full_adresse  
    string land  
    string postnummer  
    LangStringList poststad  
}
Aktor {
    uriorcurie id  
    string identifikator_literal  
    LangStringList tittel  
}
Begrepssamling {
    uriorcurie id  
}
Deltagelse {
    uriorcurie id  
}
Dokumentasjonstype {
    uriorcurie id  
    LangStringList beskrivelse  
    uriList er_beskrive_av  
    uriorcurie er_spesifisert_i  
    Duration gyldig_i  
    string identifikator_literal  
    LangStringList tittel  
}
Gebyr {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    float verdi  
}
Hendelse {
    uriorcurie id  
    LangStringList beskrivelse  
    uriList er_beskrive_av  
    string identifikator_literal  
    LangStringList tittel  
}
Katalog {
    uriorcurie id  
    LangStringList beskrivelse  
    date endringsdato  
    uriList heimeside  
    string identifikator_literal  
    uri lisens  
    LangStringList tittel  
}
Konsept {
    uriorcurie id  
}
Kontaktpunkt {
    uriorcurie id  
    uriList epost  
    stringList kategori  
    uriList kontaktside  
    stringList opningstider  
    stringList telefon  
}
Livshendelse {
    uriorcurieList kan_utlose_behov_for  
    uriorcurie id  
    LangStringList beskrivelse  
    uriList er_beskrive_av  
    string identifikator_literal  
    LangStringList tittel  
}
LovpalagtTjeneste {
    uriorcurie id  
    LangStringList beskrivelse  
    uriorcurie er_del_av  
    uriorcurieList har_del  
    uriList heimeside  
    string identifikator_literal  
    uriorcurieList krev  
    LangStringList nokkelord  
    LangStringList tittel  
}
Mediatype {
    uriorcurie id  
}
OffentligOrganisasjon {
    LangStringList foretrekt_namn  
    uriList heimeside  
    uriorcurie id  
    string identifikator_literal  
    LangStringList tittel  
}
OffentligTjeneste {
    uriorcurie id  
    Duration behandlingstid  
    LangStringList beskrivelse  
    uriList er_beskrive_av  
    uriorcurie er_del_av  
    uriorcurieList har_del  
    uriList heimeside  
    string identifikator_literal  
    uriorcurieList krev  
    LangStringList nokkelord  
    uriorcurieList relatert_teneste  
    LangStringList tittel  
}
Regel {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    LangStringList tittel  
}
RegulativRessurs {
    uriorcurie id  
    string identifikator_literal  
    LangStringList tittel  
}
Spraak {
    uriorcurie id  
}
Tjeneste {
    uriorcurie id  
    Duration behandlingstid  
    LangStringList beskrivelse  
    uriList er_beskrive_av  
    uriorcurie er_del_av  
    uriorcurieList har_del  
    uriList heimeside  
    string identifikator_literal  
    uriorcurieList krev  
    LangStringList nokkelord  
    uriorcurieList relatert_teneste  
    LangStringList tittel  
}
Tjenestekanal {
    uriorcurie id  
    Duration behandlingstid  
    LangStringList beskrivelse  
    string identifikator_literal  
    uriList nettside  
    stringList opningstider  
}
Tjenesteresultattype {
    uriorcurie id  
    LangStringList beskrivelse  
    uriList er_beskrive_av  
    uriorcurie er_spesifisert_i  
    string identifikator_literal  
    LangStringList tittel  
}
Tjenesteresultattypeliste {
    uriorcurie id  
    LangStringList beskrivelse  
    LangStringList tittel  
}
Virksomhetshendelse {
    uriorcurieList kan_utlose_behov_for  
    uriorcurie id  
    LangStringList beskrivelse  
    uriList er_beskrive_av  
    string identifikator_literal  
    LangStringList tittel  
}

Aktor ||--|o Adresse : "adresse_ref"
Aktor ||--}o Deltagelse : "deltek_i"
Deltagelse ||--|o Aktor : "deltakar"
Deltagelse ||--|o Konsept : "har_rolle"
Dokumentasjonstype ||--|o Konsept : "klassifisering, utstedingsstad"
Dokumentasjonstype ||--}o Spraak : "godtek_sprak"
Gebyr ||--|o Konsept : "valuta"
Hendelse ||--|o Konsept : "type_concept"
Hendelse ||--}o Konsept : "tema"
Hendelse ||--}o OffentligTjeneste : "kan_utlose"
Hendelse ||--}| Kontaktpunkt : "har_kontaktpunkt"
Katalog ||--|o Konsept : "oppdateringsfrekvens"
Katalog ||--|| Aktor : "utgjevar"
Katalog ||--}o Hendelse : "inneheld_hending"
Katalog ||--}o Konsept : "dekningsomrade"
Katalog ||--}o Spraak : "sprak"
Katalog ||--}| Kontaktpunkt : "har_kontaktpunkt"
Katalog ||--}| OffentligTjeneste : "inneheld_teneste"
Kontaktpunkt ||--}o Spraak : "sprak"
Livshendelse ||--|o Konsept : "type_concept"
Livshendelse ||--}o Konsept : "tema"
Livshendelse ||--}o OffentligTjeneste : "kan_utlose"
Livshendelse ||--}| Kontaktpunkt : "har_kontaktpunkt"
LovpalagtTjeneste ||--|o Konsept : "type_concept"
LovpalagtTjeneste ||--}o Dokumentasjonstype : "har_dokumentasjonstype"
LovpalagtTjeneste ||--}o Gebyr : "har_gebyr"
LovpalagtTjeneste ||--}o Hendelse : "er_gruppert_av"
LovpalagtTjeneste ||--}o Konsept : "dekningsomrade, er_klassifisert_av, malgruppe, sektor, tema, temaomrade"
LovpalagtTjeneste ||--}o Regel : "folger"
LovpalagtTjeneste ||--}o RegulativRessurs : "har_regulativ_ressurs"
LovpalagtTjeneste ||--}| Kontaktpunkt : "har_kontaktpunkt"
LovpalagtTjeneste ||--}| Tjenesteresultattype : "har_tenesteresultattype"
OffentligOrganisasjon ||--|o Adresse : "adresse_ref"
OffentligOrganisasjon ||--|o Konsept : "type_concept"
OffentligOrganisasjon ||--}o Deltagelse : "deltek_i"
OffentligOrganisasjon ||--}| Konsept : "dekningsomrade"
OffentligTjeneste ||--|o Konsept : "status, type_concept"
OffentligTjeneste ||--}o Deltagelse : "har_deltaking"
OffentligTjeneste ||--}o Dokumentasjonstype : "har_dokumentasjonstype"
OffentligTjeneste ||--}o Gebyr : "har_gebyr"
OffentligTjeneste ||--}o Hendelse : "er_gruppert_av"
OffentligTjeneste ||--}o Konsept : "dekningsomrade, er_klassifisert_av, malgruppe, sektor, tema, temaomrade"
OffentligTjeneste ||--}o LovpalagtTjeneste : "realiserer"
OffentligTjeneste ||--}o Regel : "folger"
OffentligTjeneste ||--}o RegulativRessurs : "har_regulativ_ressurs"
OffentligTjeneste ||--}o Spraak : "sprak"
OffentligTjeneste ||--}o Tjenestekanal : "har_tenestekanal"
OffentligTjeneste ||--}| Kontaktpunkt : "har_kontaktpunkt"
OffentligTjeneste ||--}| OffentligOrganisasjon : "har_ansvarleg_styremakt"
OffentligTjeneste ||--}| Tjenesteresultattype : "har_tenesteresultattype"
Regel ||--|o Konsept : "type_concept"
Regel ||--}o Spraak : "sprak"
RegulativRessurs ||--|o Konsept : "type_concept"
Tjeneste ||--|o Konsept : "status, type_concept"
Tjeneste ||--}o Deltagelse : "har_deltaking"
Tjeneste ||--}o Dokumentasjonstype : "har_dokumentasjonstype"
Tjeneste ||--}o Gebyr : "har_gebyr"
Tjeneste ||--}o Hendelse : "er_gruppert_av"
Tjeneste ||--}o Konsept : "dekningsomrade, er_klassifisert_av, malgruppe, sektor, tema, temaomrade"
Tjeneste ||--}o Regel : "folger"
Tjeneste ||--}o RegulativRessurs : "har_regulativ_ressurs"
Tjeneste ||--}o Spraak : "sprak"
Tjeneste ||--}o Tjenestekanal : "har_tenestekanal"
Tjeneste ||--}| Aktor : "eigd_av"
Tjeneste ||--}| Kontaktpunkt : "har_kontaktpunkt"
Tjeneste ||--}| Tjenesteresultattype : "har_tenesteresultattype"
Tjenestekanal ||--|o Konsept : "type_concept"
Tjenesteresultattype ||--|o Konsept : "type_concept"
Tjenesteresultattype ||--}o Hendelse : "kan_skape_hending"
Tjenesteresultattype ||--}o Spraak : "mogleg_sprak"
Virksomhetshendelse ||--|o Konsept : "type_concept"
Virksomhetshendelse ||--}o Konsept : "tema"
Virksomhetshendelse ||--}o OffentligTjeneste : "kan_utlose"
Virksomhetshendelse ||--}| Kontaktpunkt : "har_kontaktpunkt"

```

