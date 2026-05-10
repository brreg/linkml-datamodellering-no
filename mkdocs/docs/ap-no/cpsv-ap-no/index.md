# cpsv-ap-no

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
    SpraakList godtek_spraak  
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
    SpraakList spraak  
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
    SpraakList spraak  
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
    SpraakList spraak  
    LangStringList tittel  
}
Regel {
    uriorcurie id  
    LangStringList beskrivelse  
    string identifikator_literal  
    SpraakList spraak  
    LangStringList tittel  
}
RegulativRessurs {
    uriorcurie id  
    string identifikator_literal  
    LangStringList tittel  
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
    SpraakList spraak  
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
    SpraakList mogleg_spraak  
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
Gebyr ||--|o Konsept : "valuta"
Hendelse ||--|o Konsept : "type_concept"
Hendelse ||--}o Konsept : "tema"
Hendelse ||--}o OffentligTjeneste : "kan_utlose"
Hendelse ||--}| Kontaktpunkt : "har_kontaktpunkt"
Katalog ||--|o Konsept : "oppdateringsfrekvens"
Katalog ||--|| Aktor : "utgjevar"
Katalog ||--}o Hendelse : "inneheld_hending"
Katalog ||--}o Konsept : "dekningsomraade"
Katalog ||--}| Kontaktpunkt : "har_kontaktpunkt"
Katalog ||--}| OffentligTjeneste : "inneheld_teneste"
Livshendelse ||--|o Konsept : "type_concept"
Livshendelse ||--}o Konsept : "tema"
Livshendelse ||--}o OffentligTjeneste : "kan_utlose"
Livshendelse ||--}| Kontaktpunkt : "har_kontaktpunkt"
OffentligOrganisasjon ||--|o Adresse : "adresse_ref"
OffentligOrganisasjon ||--|o Konsept : "type_concept"
OffentligOrganisasjon ||--}o Deltagelse : "deltek_i"
OffentligOrganisasjon ||--}| Konsept : "dekningsomraade"
OffentligTjeneste ||--|o Konsept : "status, type_concept"
OffentligTjeneste ||--}o Deltagelse : "har_deltaking"
OffentligTjeneste ||--}o Dokumentasjonstype : "har_dokumentasjonstype"
OffentligTjeneste ||--}o Gebyr : "har_gebyr"
OffentligTjeneste ||--}o Hendelse : "er_gruppert_av"
OffentligTjeneste ||--}o Konsept : "dekningsomraade, er_klassifisert_av, malgruppe, sektor, tema, temaomrade"
OffentligTjeneste ||--}o Regel : "folger"
OffentligTjeneste ||--}o RegulativRessurs : "har_regulativ_ressurs"
OffentligTjeneste ||--}o Tjenestekanal : "har_tenestekanal"
OffentligTjeneste ||--}| Kontaktpunkt : "har_kontaktpunkt"
OffentligTjeneste ||--}| OffentligOrganisasjon : "har_ansvarleg_styremakt"
OffentligTjeneste ||--}| Tjenesteresultattype : "har_tenesteresultattype"
Regel ||--|o Konsept : "type_concept"
RegulativRessurs ||--|o Konsept : "type_concept"
Tjeneste ||--|o Konsept : "status, type_concept"
Tjeneste ||--}o Deltagelse : "har_deltaking"
Tjeneste ||--}o Dokumentasjonstype : "har_dokumentasjonstype"
Tjeneste ||--}o Gebyr : "har_gebyr"
Tjeneste ||--}o Hendelse : "er_gruppert_av"
Tjeneste ||--}o Konsept : "dekningsomraade, er_klassifisert_av, malgruppe, sektor, tema, temaomrade"
Tjeneste ||--}o Regel : "folger"
Tjeneste ||--}o RegulativRessurs : "har_regulativ_ressurs"
Tjeneste ||--}o Tjenestekanal : "har_tenestekanal"
Tjeneste ||--}| Aktor : "eigd_av"
Tjeneste ||--}| Kontaktpunkt : "har_kontaktpunkt"
Tjeneste ||--}| Tjenesteresultattype : "har_tenesteresultattype"
Tjenestekanal ||--|o Konsept : "type_concept"
Tjenesteresultattype ||--|o Konsept : "type_concept"
Tjenesteresultattype ||--}o Hendelse : "kan_skape_hending"
Virksomhetshendelse ||--|o Konsept : "type_concept"
Virksomhetshendelse ||--}o Konsept : "tema"
Virksomhetshendelse ||--}o OffentligTjeneste : "kan_utlose"
Virksomhetshendelse ||--}| Kontaktpunkt : "har_kontaktpunkt"

```



Norsk applikasjonsprofil av CPSV (Core Public Service Vocabulary), modellert i LinkML med lenking framfor inlining. Basert på https://informasjonsforvaltning.github.io/cpsv-ap-no/

URI: https://data.norge.no/linkml/cpsv-ap-no

Name: cpsv-ap-no



## Classes

| Class | Description |
| --- | --- |
| [Adresse](klasser/adresse.md) | Ei postadresse knytt til ein aktør, organisasjon eller kontaktpunkt |
| [Aktor](klasser/aktor.md) | Ein aktør (person eller organisasjon) relatert til ei teneste |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OffentligOrganisasjon](klasser/offentligorganisasjon.md) | Ein offentleg organisasjon som er ansvarleg for ei teneste |
| [Deltagelse](klasser/deltagelse.md) | Ei rolle ein aktør har i leveringa av ei teneste |
| [Dokumentasjonstype](klasser/dokumentasjonstype.md) | Ein type dokumentasjon som krevst for å levere ei teneste |
| [Gebyr](klasser/gebyr.md) | Eit gebyr knytt til ei teneste |
| [Hendelse](klasser/hendelse.md) | Ei hending som kan utløyse behov for ei offentleg teneste |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Livshendelse](klasser/livshendelse.md) | Ei livshending som kan utløyse behov for tenester (t |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virksomhetshendelse](klasser/virksomhetshendelse.md) | Ei verksemdhending som kan utløyse behov for tenester (t |
| [Katalog](klasser/katalog.md) | Ein katalog over offentlege tenester og hendingar |
| [Kontaktpunkt](klasser/kontaktpunkt.md) | Kontaktinformasjon for ei teneste eller ein organisasjon |
| [OffentligTjeneste](klasser/offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |
| [Regel](klasser/regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |
| [RegulativRessurs](klasser/regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |
| [Tjeneste](klasser/tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |
| [Tjenestekanal](klasser/tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |
| [Tjenesteresultattype](klasser/tjenesteresultattype.md) | Typen resultat som ei teneste produserer |
| [Tjenesteresultattypeliste](klasser/tjenesteresultattypeliste.md) | Ei liste over moglege tjenesteresultattypar |



## Slots

| Slot | Description |
| --- | --- |
| [adresse_ref](klasser/adresse_ref.md) | Postadresse knytt til aktøren |
| [behandlingstid](klasser/behandlingstid.md) | Forventa behandlingstid for tenesta eller kanalen (ISO 8601) |
| [deltakar](klasser/deltakar.md) | Aktøren som deltek |
| [deltek_i](klasser/deltek_i.md) | Deltakingar aktøren er del av |
| [eigd_av](klasser/eigd_av.md) | Aktør som eig eller er ansvarleg for tenesta |
| [epost](klasser/epost.md) | E-postadresse (mailto:-URI) |
| [er_beskrive_av](klasser/er_beskrive_av.md) | Datasett som beskriv ressursen |
| [er_del_av](klasser/er_del_av.md) | Tenesta er del av ei anna teneste |
| [er_gruppert_av](klasser/er_gruppert_av.md) | Hending(ar) som grupperer tenesta |
| [er_klassifisert_av](klasser/er_klassifisert_av.md) | Omgrep tenesta er klassifisert med |
| [er_spesifisert_i](klasser/er_spesifisert_i.md) | Liste eller spesifikasjon ressursen er del av |
| [folger](klasser/folger.md) | Regelverk tenesta følgjer |
| [foretrekt_namn](klasser/foretrekt_namn.md) | Føretrekt namn/term for organisasjonen |
| [full_adresse](klasser/full_adresse.md) | Full adresse som fritekst |
| [godtek_spraak](klasser/godtek_spraak.md) | Språk dokumentasjonstypen er akseptert i |
| [gyldig_i](klasser/gyldig_i.md) | Kor lenge dokumentasjonen er gyldig (ISO 8601 varigheit) |
| [har_ansvarleg_styremakt](klasser/har_ansvarleg_styremakt.md) | Offentleg organisasjon ansvarleg for tenesta |
| [har_del](klasser/har_del.md) | Deltenester som inngår i denne tenesta |
| [har_deltaking](klasser/har_deltaking.md) | Deltakarar med spesifikke roller i levering av tenesta |
| [har_dokumentasjonstype](klasser/har_dokumentasjonstype.md) | Dokumentasjon som krevst for tenesta |
| [har_gebyr](klasser/har_gebyr.md) | Gebyr knytt til tenesta |
| [har_kontaktpunkt](klasser/har_kontaktpunkt.md) | Kontaktpunkt for tenesta eller organisasjonen |
| [har_regulativ_ressurs](klasser/har_regulativ_ressurs.md) | Regulativ ressurs (lov, forskrift) knytt til tenesta |
| [har_rolle](klasser/har_rolle.md) | Rolla aktøren har i ei deltaking |
| [har_tenestekanal](klasser/har_tenestekanal.md) | Kanal for tilgang til tenesta |
| [har_tenesteresultattype](klasser/har_tenesteresultattype.md) | Typen resultat tenesta kan produsere |
| [inneheld_hending](klasser/inneheld_hending.md) | Hendingar i katalogen |
| [inneheld_teneste](klasser/inneheld_teneste.md) | Offentlege tenester i katalogen |
| [kan_skape_hending](klasser/kan_skape_hending.md) | Hending tenesteresultatet kan skape |
| [kan_utlose](klasser/kan_utlose.md) | Offentlege tenester hendinga kan utløyse |
| [kan_utlose_behov_for](klasser/kan_utlose_behov_for.md) | Tenester det kan oppstå behov for som følgje av hendinga |
| [kategori](klasser/kategori.md) | Kategori for kontaktpunktet |
| [klassifisering](klasser/klassifisering.md) | Klassifisering av dokumentasjonstypen |
| [kontaktside](klasser/kontaktside.md) | Kontaktside (nettadresse) |
| [krev](klasser/krev.md) | Teneste eller ressurs denne tenesta krev |
| [land](klasser/land.md) | Land (ISO 3166-1 alpha-2 kode) |
| [lisens](klasser/lisens.md) | Lisens for katalogen |
| [malgruppe](klasser/malgruppe.md) | Målgruppe for tenesta |
| [mogleg_spraak](klasser/mogleg_spraak.md) | Mogleg språk for tenesteresultatet |
| [nettside](klasser/nettside.md) | Nettside for tenestekanalane |
| [opningstider](klasser/opningstider.md) | Opningstider |
| [oppdateringsfrekvens](klasser/oppdateringsfrekvens.md) | Kor ofte katalogen vert oppdatert |
| [postnummer](klasser/postnummer.md) | Postnummer |
| [poststad](klasser/poststad.md) | Poststad/by |
| [relatert_teneste](klasser/relatert_teneste.md) | Relatert teneste |
| [sektor](klasser/sektor.md) | Industri/sektor tenesta tilhøyrer |
| [telefon](klasser/telefon.md) | Telefonnummer |
| [tema](klasser/tema.md) | Emne/tema tenesta handlar om |
| [temaomrade](klasser/temaomrade.md) | Tematisk område for tenesta |
| [utgjevar](klasser/utgjevar.md) | Utgjevar av katalogen |
| [utstedingsstad](klasser/utstedingsstad.md) | Stad dokumentasjonen er akseptert frå |
| [verdi](klasser/verdi.md) | Verdien av gebyret |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](klasser/anbefalt.md) | Anbefalte eigenskapar i ein AP-NO-profil |
| [Obligatorisk](klasser/obligatorisk.md) | Obligatoriske eigenskapar i ein AP-NO-profil |
| [Valgfri](klasser/valgfri.md) | Valfrie eigenskapar i ein AP-NO-profil |


## Generated artifacts

| Artefakt | Fil |
|----------|-----|
| SHACL shapes | [cpsv-ap-no-shapes.ttl](cpsv-ap-no-shapes.ttl) |
| JSON-LD kontekst | [cpsv-ap-no-context.jsonld](cpsv-ap-no-context.jsonld) |
| JSON Schema | [cpsv-ap-no-schema.json](cpsv-ap-no-schema.json) |
| OWL ontologi | [cpsv-ap-no-ontology.ttl](cpsv-ap-no-ontology.ttl) |
| RDF/Turtle skjema | [cpsv-ap-no-schema.ttl](cpsv-ap-no-schema.ttl) |
| Python-klasser | [cpsv-ap-no-model.py](cpsv-ap-no-model.py) |
| ER-diagram (Mermaid) | [cpsv-ap-no-erdiagram.md](cpsv-ap-no-erdiagram.md) |
| Eksempeldata (Turtle) | [cpsv-ap-no-eksempel.ttl](cpsv-ap-no-eksempel.ttl) |
