# fint-utdanning

## Artefacts

| Artefakt | Fil |
|----------|-----|
| SHACL shapes | [fint-utdanning-shapes.ttl](fint-utdanning-shapes.ttl) |
| JSON-LD kontekst | [fint-utdanning-context.jsonld](fint-utdanning-context.jsonld) |
| JSON Schema | [fint-utdanning-schema.json](fint-utdanning-schema.json) |
| OWL ontologi | [fint-utdanning-ontology.ttl](fint-utdanning-ontology.ttl) |
| Python-klasser | [fint-utdanning-model.py](fint-utdanning-model.py) |
| ER-diagram (Mermaid) | [fint-utdanning-erdiagram.md](fint-utdanning-erdiagram.md) |
| Eksempeldata (Turtle) | [fint-utdanning-eksempel.ttl](fint-utdanning-eksempel.ttl) |

## Oversiktsdiagram

```mermaid
erDiagram
Adresse {
    stringList adresselinje  
    string postnummer  
    string poststed  
}
Anmerkninger {
    uriorcurie id  
    integer atferd  
    integer orden  
}
Arstrinn {
    uriorcurie grepreferanse  
    uriorcurie vigoreferanse  
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Avbruddsaarsak {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
AvlagtProve {
    uriorcurie id  
    date provedato  
}
Betalingsstatus {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Bevistype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Brevtype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Eksamen {
    uriorcurie id  
    string beskrivelse  
    string navn  
    datetime oppmoetetidspunkt  
}
Eksamensform {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Eksamensgruppe {
    datetime eksamensdato  
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Eksamensgruppemedlemskap {
    boolean delegert  
    uriorcurie delegertTil  
    boolean foretrukketSensor  
    boolean foretrukketSkole  
    string kandidatnummer  
    uriorcurie id  
}
Eksamensvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Elev {
    uriorcurie id  
    uriorcurie person  
}
Elevforhold {
    uriorcurie id  
    date avbruddsdato  
    string beskrivelse  
    boolean tosprakligFagopplaering  
}
Elevfravar {
    uriorcurie id  
}
Elevkategori {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Elevtilrettelegging {
    uriorcurie id  
}
Elevvurdering {
    uriorcurie id  
}
Fag {
    uriorcurie grepreferanse  
    uriorcurie vigoreferanse  
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Faggruppe {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Faggruppemedlemskap {
    uriorcurie id  
}
Fagmerknad {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Fagstatus {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Fravarsoversikt {
    uriorcurie id  
}
Fravarsprosent {
    integer fravaerstimer  
    integer prosent  
    integer undervisningstimer  
}
Fravartype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Fraversregistrering {
    uriorcurie id  
    boolean forersPaaVitnemaal  
    string kommentar  
}
Fullfortkode {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Halvaarsfagvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Halvaarsordensvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Identifikator {
    string identifikatorverdi  
}
Karakterhistorie {
    uriorcurie id  
    datetime endretDato  
}
Karakterskala {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
    uriorcurie vigoreferanse  
}
Karakterstatus {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Karakterverdi {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Klasse {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Klassemedlemskap {
    uriorcurie id  
}
Kontaktlaerergruppe {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Kontaktlaerergruppemedlemskap {
    uriorcurie id  
}
Laerling {
    uriorcurie id  
    uriorcurie bedrift  
    string kontraktstype  
    uriorcurie person  
}
Landkode {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
OtEnhet {
    uriorcurie id  
    string kode  
    uriorcurie kommune  
    string navn  
    boolean passiv  
}
OtStatus {
    uriorcurie id  
    string beskrivelse  
    string kode  
    string navn  
    boolean passiv  
    string type  
}
OtUngdom {
    uriorcurie id  
    uriorcurie person  
}
Periode {
    string beskrivelse  
    datetime slutt  
    datetime start  
}
Persongruppe {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Persongruppemedlemskap {
    uriorcurie id  
}
Programomrade {
    uriorcurie grepreferanse  
    uriorcurie vigoreferanse  
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Programomrademedlemskap {
    uriorcurie id  
}
Provestatus {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Rom {
    uriorcurie id  
    string navn  
}
Sensor {
    uriorcurie id  
    boolean aktiv  
    integer sensornummer  
}
Skole {
    uriorcurie id  
    string domenenavn  
    string juridiskNavn  
    string navn  
    uriorcurie organisasjon  
    string organisasjonsnavn  
    uriorcurie vigoreferanse  
}
Skoleaar {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Skoleeiertype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Skoleressurs {
    uriorcurie id  
    uriorcurie person  
    uriorcurie personalressurs  
}
Sluttfagvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Sluttordensvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Termin {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Tilrettelegging {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Time {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Underveisfagvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Underveisordensvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Undervisningsforhold {
    uriorcurie arbeidsforhold  
    uriorcurie id  
    string beskrivelse  
}
Undervisningsgruppe {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Undervisningsgruppemedlemskap {
    uriorcurie id  
}
Utdanningsprogram {
    uriorcurie grepreferanse  
    uriorcurie vigoreferanse  
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Varsel {
    uriorcurie id  
    integer fravarsprosent  
    date sendt  
    string tekst  
}
Varseltype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Vitnemalsmerknad {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}

Adresse ||--|o Landkode : "land"
Anmerkninger ||--|o Skoleaar : "skoleaar"
Arstrinn ||--}o Klasse : "klasse"
Arstrinn ||--}o Programomrade : "programomrade"
Avbruddsaarsak ||--|o Periode : "gyldighetsperiode"
AvlagtProve ||--|o Bevistype : "bevistype"
AvlagtProve ||--|o Brevtype : "brevtype"
AvlagtProve ||--|o Fullfortkode : "fullfortkode"
AvlagtProve ||--|o Provestatus : "provestatus"
AvlagtProve ||--|| Laerling : "laerling"
Betalingsstatus ||--|o Periode : "gyldighetsperiode"
Bevistype ||--|o Periode : "gyldighetsperiode"
Brevtype ||--|o Periode : "gyldighetsperiode"
Eksamen ||--|o Eksamensgruppe : "eksamensgruppe"
Eksamen ||--|o Periode : "tidsrom"
Eksamen ||--}o Rom : "rom"
Eksamensform ||--|o Periode : "gyldighetsperiode"
Eksamensgruppe ||--|o Eksamen : "eksamen"
Eksamensgruppe ||--|o Eksamensform : "eksamensform"
Eksamensgruppe ||--|o Skoleaar : "skoleaar"
Eksamensgruppe ||--|| Fag : "fag"
Eksamensgruppe ||--|| Skole : "skole"
Eksamensgruppe ||--|| Termin : "termin"
Eksamensgruppe ||--}o Eksamensgruppemedlemskap : "gruppemedlemskap"
Eksamensgruppe ||--}o Sensor : "sensor"
Eksamensgruppe ||--}o Undervisningsforhold : "undervisningsforhold"
Eksamensgruppemedlemskap ||--|o Betalingsstatus : "betalingsstatus"
Eksamensgruppemedlemskap ||--|o Karakterstatus : "nus"
Eksamensgruppemedlemskap ||--|o Periode : "gyldighetsperiode"
Eksamensgruppemedlemskap ||--|| Eksamensgruppe : "eksamensgruppe"
Eksamensgruppemedlemskap ||--|| Elevforhold : "elevforhold"
Eksamensvurdering ||--|o Fag : "fag"
Eksamensvurdering ||--|o Karakterverdi : "karakter"
Eksamensvurdering ||--|o Skoleaar : "skoleaar"
Eksamensvurdering ||--|| Eksamensgruppe : "eksamensgruppe"
Eksamensvurdering ||--|| Elevvurdering : "elevvurdering"
Eksamensvurdering ||--}o Karakterhistorie : "karakterhistorie"
Elev ||--|o Identifikator : "elevnummer"
Elevforhold ||--|o Avbruddsaarsak : "avbruddsarsak"
Elevforhold ||--|o Elevkategori : "kategori"
Elevforhold ||--|o Elevvurdering : "elevvurdering"
Elevforhold ||--|o Fravarsoversikt : "elevfravar"
Elevforhold ||--|o Skoleaar : "skoleaar"
Elevforhold ||--|| Elev : "elev"
Elevforhold ||--|| Skole : "skole"
Elevforhold ||--}o Eksamensgruppemedlemskap : "eksamensgruppemedlemskap"
Elevforhold ||--}o Elevfravar : "fraversregistreringer"
Elevforhold ||--}o Elevtilrettelegging : "tilrettelegging"
Elevforhold ||--}o Faggruppemedlemskap : "faggruppemedlemskap"
Elevforhold ||--}o Klassemedlemskap : "klassemedlemskap"
Elevforhold ||--}o Kontaktlaerergruppemedlemskap : "kontaktlaerergruppemedlemskap"
Elevforhold ||--}o Persongruppemedlemskap : "persongruppemedlemskap"
Elevforhold ||--}o Programomrademedlemskap : "programomrademedlemskap"
Elevforhold ||--}o Undervisningsgruppemedlemskap : "undervisningsgruppemedlemskap"
Elevfravar ||--|| Elevforhold : "elevforhold"
Elevfravar ||--}o Fraversregistrering : "fraversregistrering"
Elevkategori ||--|o Periode : "gyldighetsperiode"
Elevtilrettelegging ||--|o Eksamensform : "eksamensform"
Elevtilrettelegging ||--|o Elevforhold : "elev"
Elevtilrettelegging ||--|o Tilrettelegging : "tilrettelegging"
Elevvurdering ||--|o Vitnemalsmerknad : "vitnemalsmerknad"
Elevvurdering ||--|| Elevforhold : "elevforhold"
Elevvurdering ||--}o Eksamensvurdering : "eksamensvurdering"
Elevvurdering ||--}o Halvaarsfagvurdering : "halvaarsfagvurdering"
Elevvurdering ||--}o Halvaarsordensvurdering : "halvaarsordensvurdering"
Elevvurdering ||--}o Sluttfagvurdering : "sluttfagvurdering"
Elevvurdering ||--}o Sluttordensvurdering : "sluttordensvurdering"
Elevvurdering ||--}o Underveisfagvurdering : "underveisfagvurdering"
Elevvurdering ||--}o Underveisordensvurdering : "underveisordensvurdering"
Fag ||--}o Eksamensgruppe : "eksamensgruppe"
Fag ||--}o Faggruppe : "faggruppe"
Fag ||--}o Programomrade : "programomrade"
Fag ||--}o Skole : "skole"
Fag ||--}o Tilrettelegging : "tilrettelegging"
Fag ||--}o Undervisningsgruppe : "undervisningsgruppe"
Faggruppe ||--|o Skole : "skole"
Faggruppe ||--|o Skoleaar : "skoleaar"
Faggruppe ||--|| Fag : "fag"
Faggruppe ||--}o Faggruppemedlemskap : "faggruppemedlemskap"
Faggruppemedlemskap ||--|o Elevforhold : "elevforhold"
Faggruppemedlemskap ||--|o Faggruppe : "faggruppe"
Faggruppemedlemskap ||--|o Fagmerknad : "fagmerknad"
Faggruppemedlemskap ||--|o Fagstatus : "fagstatus"
Faggruppemedlemskap ||--|o Periode : "gyldighetsperiode"
Faggruppemedlemskap ||--}o Varsel : "varsel"
Fagmerknad ||--|o Periode : "gyldighetsperiode"
Fagstatus ||--|o Periode : "gyldighetsperiode"
Fravarsoversikt ||--|| Elevforhold : "elevforhold"
Fravarsoversikt ||--|| Fag : "fag"
Fravarsoversikt ||--|| Fravarsprosent : "halvaar, skoleaarFravar"
Fravartype ||--|o Periode : "gyldighetsperiode"
Fraversregistrering ||--|o Faggruppe : "faggruppe"
Fraversregistrering ||--|o Skoleressurs : "registrertAv"
Fraversregistrering ||--|| Elevfravar : "elevfravar"
Fraversregistrering ||--|| Fravartype : "fravartype"
Fraversregistrering ||--|| Periode : "periode"
Fraversregistrering ||--|| Undervisningsgruppe : "undervisningsgruppe"
Fullfortkode ||--|o Periode : "gyldighetsperiode"
Halvaarsfagvurdering ||--|o Fag : "fag"
Halvaarsfagvurdering ||--|o Karakterverdi : "karakter"
Halvaarsfagvurdering ||--|o Skoleaar : "skoleaar"
Halvaarsfagvurdering ||--|| Elevvurdering : "elevvurdering"
Halvaarsordensvurdering ||--|o Karakterverdi : "atferd, orden"
Halvaarsordensvurdering ||--|o Skoleaar : "skoleaar"
Halvaarsordensvurdering ||--|| Elevvurdering : "elevvurdering"
Identifikator ||--|o Periode : "gyldighetsperiode"
Karakterhistorie ||--|o Karakterstatus : "karakterstatus, opprinneligKarakterstatus"
Karakterhistorie ||--|o Karakterverdi : "karakterverdi, opprinneligKarakterverdi"
Karakterhistorie ||--|o Skoleressurs : "oppdatertAv"
Karakterskala ||--|o Periode : "gyldighetsperiode"
Karakterskala ||--}o Karakterverdi : "verdi"
Karakterstatus ||--|o Periode : "gyldighetsperiode"
Karakterverdi ||--|o Periode : "gyldighetsperiode"
Karakterverdi ||--|| Karakterskala : "skala"
Klasse ||--|o Skole : "skole"
Klasse ||--|o Skoleaar : "skoleaar"
Klasse ||--}o Arstrinn : "trinn"
Klasse ||--}o Klassemedlemskap : "klassemedlemskap"
Klasse ||--}o Kontaktlaerergruppe : "kontaktlaerergruppe"
Klasse ||--}o Termin : "termin"
Klasse ||--}o Undervisningsforhold : "undervisningsforhold"
Klassemedlemskap ||--|o Elevforhold : "elevforhold"
Klassemedlemskap ||--|o Klasse : "klasse"
Klassemedlemskap ||--|o Periode : "gyldighetsperiode"
Kontaktlaerergruppe ||--|o Skole : "skole"
Kontaktlaerergruppe ||--|o Skoleaar : "skoleaar"
Kontaktlaerergruppe ||--}o Kontaktlaerergruppemedlemskap : "gruppemedlemskap"
Kontaktlaerergruppe ||--}o Termin : "termin"
Kontaktlaerergruppe ||--}o Undervisningsforhold : "undervisningsforhold"
Kontaktlaerergruppe ||--}| Klasse : "klasse"
Kontaktlaerergruppemedlemskap ||--|o Elevforhold : "elevforhold"
Kontaktlaerergruppemedlemskap ||--|o Kontaktlaerergruppe : "kontaktlaerergruppe"
Kontaktlaerergruppemedlemskap ||--|o Periode : "gyldighetsperiode"
Laerling ||--|o Periode : "laretid"
Laerling ||--|o Programomrade : "programomrade"
Laerling ||--}o AvlagtProve : "avlagtprove"
Landkode ||--|o Periode : "gyldighetsperiode"
OtEnhet ||--|o Periode : "gyldighetsperiode"
OtStatus ||--|o Periode : "gyldighetsperiode"
OtUngdom ||--|o OtEnhet : "enhet"
OtUngdom ||--|o OtStatus : "status"
OtUngdom ||--|o Programomrade : "programomrade"
Persongruppe ||--|o Skole : "skole"
Persongruppe ||--|o Skoleaar : "skoleaar"
Persongruppe ||--}o Elevforhold : "elev"
Persongruppe ||--}o Persongruppemedlemskap : "persongruppemedlemskap"
Persongruppe ||--}o Skoleressurs : "skoleressurs"
Persongruppe ||--}o Termin : "termin"
Persongruppe ||--}o Undervisningsforhold : "undervisningsforhold"
Persongruppemedlemskap ||--|o Elevforhold : "elevforhold"
Persongruppemedlemskap ||--|o Periode : "gyldighetsperiode"
Persongruppemedlemskap ||--|o Persongruppe : "persongruppe"
Programomrade ||--}o Arstrinn : "trinn"
Programomrade ||--}o Programomrademedlemskap : "gruppemedlemskap"
Programomrademedlemskap ||--|o Elevforhold : "elevforhold"
Programomrademedlemskap ||--|o Periode : "gyldighetsperiode"
Programomrademedlemskap ||--|o Programomrade : "programomrade"
Provestatus ||--|o Periode : "gyldighetsperiode"
Rom ||--}o Eksamen : "eksamen"
Rom ||--}o Time : "time"
Sensor ||--|| Eksamensgruppe : "eksamensgruppe"
Sensor ||--|| Skoleressurs : "skoleressurs"
Skole ||--|o Adresse : "forretningsadresse, postadresse"
Skole ||--|o Identifikator : "organisasjonsnummer, skolenummer"
Skole ||--|o Skoleeiertype : "skoleeierType"
Skole ||--}o Eksamensgruppe : "eksamensgruppe"
Skole ||--}o Fag : "fag"
Skole ||--}o Faggruppe : "faggruppe"
Skole ||--}o Klasse : "klasse"
Skole ||--}o Kontaktlaerergruppe : "kontaktlaerergruppe"
Skole ||--}o Skoleressurs : "skoleressurs"
Skole ||--}o Utdanningsprogram : "utdanningsprogram"
Skoleaar ||--|o Periode : "gyldighetsperiode"
Skoleeiertype ||--|o Periode : "gyldighetsperiode"
Skoleressurs ||--|o Identifikator : "feidenavn"
Skoleressurs ||--}o Sensor : "sensor"
Skoleressurs ||--}o Skole : "skole"
Sluttfagvurdering ||--|o Eksamensgruppe : "eksamensgruppe"
Sluttfagvurdering ||--|o Fag : "fag"
Sluttfagvurdering ||--|o Karakterverdi : "karakter"
Sluttfagvurdering ||--|o Skoleaar : "skoleaar"
Sluttfagvurdering ||--|| Elevvurdering : "elevvurdering"
Sluttfagvurdering ||--}o Karakterhistorie : "karakterhistorie"
Sluttordensvurdering ||--|o Karakterverdi : "atferd, orden"
Sluttordensvurdering ||--|o Skoleaar : "skoleaar"
Sluttordensvurdering ||--|| Elevvurdering : "elevvurdering"
Termin ||--|o Periode : "gyldighetsperiode"
Tilrettelegging ||--|o Periode : "gyldighetsperiode"
Time ||--|o Periode : "tidsrom"
Time ||--}o Rom : "rom"
Time ||--}| Undervisningsforhold : "undervisningsforhold"
Time ||--}| Undervisningsgruppe : "undervisningsgruppe"
Underveisfagvurdering ||--|o Fag : "fag"
Underveisfagvurdering ||--|o Karakterverdi : "karakter"
Underveisfagvurdering ||--|o Skoleaar : "skoleaar"
Underveisfagvurdering ||--|| Elevvurdering : "elevvurdering"
Underveisordensvurdering ||--|o Karakterverdi : "atferd, orden"
Underveisordensvurdering ||--|o Skoleaar : "skoleaar"
Underveisordensvurdering ||--|| Elevvurdering : "elevvurdering"
Undervisningsforhold ||--|o Skoleressurs : "skoleressurs"
Undervisningsforhold ||--}o Eksamensgruppe : "eksamensgruppe"
Undervisningsforhold ||--}o Klasse : "klasse"
Undervisningsforhold ||--}o Kontaktlaerergruppe : "kontaktlaerergruppe"
Undervisningsforhold ||--}o Time : "time"
Undervisningsgruppe ||--|o Skole : "skole"
Undervisningsgruppe ||--|o Skoleaar : "skoleaar"
Undervisningsgruppe ||--}o Termin : "termin"
Undervisningsgruppe ||--}o Time : "time"
Undervisningsgruppe ||--}o Undervisningsforhold : "undervisningsforhold"
Undervisningsgruppe ||--}o Undervisningsgruppemedlemskap : "gruppemedlemskap"
Undervisningsgruppe ||--}| Fag : "fag"
Undervisningsgruppemedlemskap ||--|o Elevforhold : "elevforhold"
Undervisningsgruppemedlemskap ||--|o Periode : "gyldighetsperiode"
Undervisningsgruppemedlemskap ||--|o Undervisningsgruppe : "undervisningsgruppe"
Utdanningsprogram ||--}o Programomrade : "programomrade"
Utdanningsprogram ||--}o Skole : "skole"
Varsel ||--|o Faggruppemedlemskap : "faggruppemedlemskap"
Varsel ||--|o Skoleressurs : "karakteransvarlig, utsteder"
Varsel ||--|o Varseltype : "type"
Varseltype ||--|o Periode : "gyldighetsperiode"
Vitnemalsmerknad ||--|o Periode : "gyldighetsperiode"

```



FINT-domenemodell for utdanning. Dekkjer elevar, skular, skoleressursar, elevforhold, undervisningsforhold, klasser, undervisningsgrupper, faggrupper, kontaktlærergrupper, utdanningsprogram, programområde, vurdering, lærling og OT.


URI: https://data.norge.no/linkml/fint-utdanning

Name: fint-utdanning



## Classes

| Class | Description |
| --- | --- |
| [Adresse](klasser/adresse.md) | Fysisk adresse eller postadresse |
| [Aktoer](klasser/aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Enhet](klasser/enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virksomhet](klasser/virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](klasser/person.md) | Fysiske private personar |
| [Anmerkninger](klasser/anmerkninger.md) | Åtferds- og ordensanmerkningar for ein elev i eit skoleår |
| [Avbruddsaarsak](klasser/avbruddsaarsak.md) | Årsak til avbrot frå opplæring |
| [AvlagtProve](klasser/avlagtprove.md) | Ei avlagt prøve for ein lærling |
| [Begrep](klasser/begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fylke](klasser/fylke.md) | Liste over Norges fylker |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kjonn](klasser/kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kommune](klasser/kommune.md) | Liste over Norges kommunar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Landkode](klasser/landkode.md) | Landskode i ISO 3166-1 alpha-2 format |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Spraak](klasser/spraak.md) | Verdiar for språk (2 bokstavar) |
| [Betalingsstatus](klasser/betalingsstatus.md) | Betalingsstatus for eksamensavgift |
| [Bevistype](klasser/bevistype.md) | Type kompetansebevis for lærling |
| [Brevtype](klasser/brevtype.md) | Type brev knytt til lærlingprøve |
| [Eksamen](klasser/eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |
| [Eksamensform](klasser/eksamensform.md) | Form for gjennomføring av eksamen |
| [Elev](klasser/elev.md) | Ein elev registrert i skulesystemet |
| [Elevforhold](klasser/elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |
| [Elevfravar](klasser/elevfravar.md) | Fråværsregistreringar for ein elev knytt til eit elevforhold |
| [Elevkategori](klasser/elevkategori.md) | Kategori for eit elevforhold (t |
| [Elevtilrettelegging](klasser/elevtilrettelegging.md) | Tilrettelegging for ein elev i eit elevforhold |
| [Elevvurdering](klasser/elevvurdering.md) | Samling av alle vurderingar for ein elev i eit elevforhold |
| [Fagmerknad](klasser/fagmerknad.md) | Merknad knytt til eit fag i ei faggruppe |
| [Fagstatus](klasser/fagstatus.md) | Status for eit fag i eit faggruppemedlemskap |
| [FagvurderingAbstrakt](klasser/fagvurderingabstrakt.md) | Abstrakt basisklasse for fagvurderingar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eksamensvurdering](klasser/eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Halvaarsfagvurdering](klasser/halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sluttfagvurdering](klasser/sluttfagvurdering.md) | Sluttkarakter i eit fag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Underveisfagvurdering](klasser/underveisfagvurdering.md) | Underveisfagvurdering for ein elev |
| [Fravarsoversikt](klasser/fravarsoversikt.md) | Oversikt over fråvær for ein elev i eit fag |
| [Fravarsprosent](klasser/fravarsprosent.md) | Kompleks type som representerer fråværsprosent for ein periode |
| [Fravartype](klasser/fravartype.md) | Type fråvær (t |
| [Fraversregistrering](klasser/fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |
| [Fullfortkode](klasser/fullfortkode.md) | Kode for fullførtresultat av lærling |
| [Gruppe](klasser/gruppe.md) | Abstrakt basisklasse for alle gruppetypar i utdanning |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Arstrinn](klasser/arstrinn.md) | Eit årstrinn i skulen (t |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eksamensgruppe](klasser/eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fag](klasser/fag.md) | Eit skulefag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Faggruppe](klasser/faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Klasse](klasser/klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kontaktlaerergruppe](klasser/kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Persongruppe](klasser/persongruppe.md) | Ei gruppe elevar definert for personlege føremål |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Programomrade](klasser/programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Undervisningsgruppe](klasser/undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Utdanningsprogram](klasser/utdanningsprogram.md) | Eit utdanningsprogram (t |
| [Gruppemedlemskap](klasser/gruppemedlemskap.md) | Abstrakt basisklasse for gruppemedlemskapar i utdanning |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eksamensgruppemedlemskap](klasser/eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Faggruppemedlemskap](klasser/faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Klassemedlemskap](klasser/klassemedlemskap.md) | Eit elevs medlemskap i ei klasse |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kontaktlaerergruppemedlemskap](klasser/kontaktlaerergruppemedlemskap.md) | Eit elevs medlemskap i ei kontaktlærargruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Persongruppemedlemskap](klasser/persongruppemedlemskap.md) | Eit elevs medlemskap i ei persongruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Programomrademedlemskap](klasser/programomrademedlemskap.md) | Eit elevs tilknyting til eit programområde |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Undervisningsgruppemedlemskap](klasser/undervisningsgruppemedlemskap.md) | Eit elevs medlemskap i ei undervisningsgruppe |
| [Identifikator](klasser/identifikator.md) | Unik identifikasjon til eit objekt |
| [Karakterhistorie](klasser/karakterhistorie.md) | Historikk over endringar i ein karakter |
| [Karakterskala](klasser/karakterskala.md) | Skala for karaktersetjing (t |
| [Karakterstatus](klasser/karakterstatus.md) | Status for ein karakter (t |
| [Karakterverdi](klasser/karakterverdi.md) | Ein konkret karakterverdi i ei karakterskala |
| [Kontaktinformasjon](klasser/kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |
| [Kontaktperson](klasser/kontaktperson.md) | Kontaktperson (pårørande) til ein person |
| [Laerling](klasser/laerling.md) | Ein lærling i yrkesopplæring |
| [Matrikkelnummer](klasser/matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |
| [OrdensvurderingAbstrakt](klasser/ordensvurderingabstrakt.md) | Abstrakt basisklasse for ordensvurderingar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Halvaarsordensvurdering](klasser/halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sluttordensvurdering](klasser/sluttordensvurdering.md) | Sluttordensvurdering for ein elev |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Underveisordensvurdering](klasser/underveisordensvurdering.md) | Underveisordensvurdering for ein elev |
| [OtEnhet](klasser/otenhet.md) | Eining i oppfølgingstenesta (OT) |
| [OtStatus](klasser/otstatus.md) | Status for ein ungdom i oppfølgingstenesta |
| [OtUngdom](klasser/otungdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |
| [Periode](klasser/periode.md) | Tidsperiode med obligatorisk start og valfri slutt |
| [Personnavn](klasser/personnavn.md) | Namn på ein person |
| [Provestatus](klasser/provestatus.md) | Status for ei lærlingprøve |
| [Rom](klasser/rom.md) | Eit rom eller lokale ved ein skule |
| [Sensor](klasser/sensor.md) | Ein sensor for ein eksamen |
| [Skole](klasser/skole.md) | Ein skule eller opplæringsinstitusjon |
| [Skoleaar](klasser/skoleaar.md) | Eit skoleår (t |
| [Skoleeiertype](klasser/skoleeiertype.md) | Type skuleeigartilknyting |
| [Skoleressurs](klasser/skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |
| [Termin](klasser/termin.md) | Ein skuleterm (t |
| [Tilrettelegging](klasser/tilrettelegging.md) | Type tilrettelegging for elevar (t |
| [Time](klasser/time.md) | Ein time i timeplanen |
| [UtdanningContainer](klasser/utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |
| [Utdanningsforhold](klasser/utdanningsforhold.md) | Abstrakt basisklasse for undervisningsforhold i utdanning |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Undervisningsforhold](klasser/undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |
| [Valuta](klasser/valuta.md) | Valutakodar for offisielle valutaer |
| [Varsel](klasser/varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |
| [Varseltype](klasser/varseltype.md) | Type varsel knytt til ein elev |
| [Vitnemalsmerknad](klasser/vitnemalsmerknad.md) | Merknad på vitnemål |



## Slots

| Slot | Description |
| --- | --- |
| [adresse](klasser/adresse.md) | Adresse til matrikkeleining |
| [adresselinje](klasser/adresselinje.md) | Adresseinformasjon |
| [aktiv](klasser/aktiv.md) | Angir om sensoren er aktiv |
| [anmerkningar](klasser/anmerkningar.md) |  |
| [arbeidsforhold](klasser/arbeidsforhold.md) | Referanse til Arbeidsforhold i Administrasjon-domenet |
| [arstrinn](klasser/arstrinn.md) |  |
| [atferd](klasser/atferd.md) | Karakterverdi for åtferd |
| [avbruddsaarsaker](klasser/avbruddsaarsaker.md) |  |
| [avbruddsarsak](klasser/avbruddsarsak.md) | Årsak til avbrot frå opplæring |
| [avbruddsdato](klasser/avbruddsdato.md) | Dato for avbrot frå opplæring |
| [avlagteprover](klasser/avlagteprover.md) |  |
| [avlagtprove](klasser/avlagtprove.md) | Avlagde prøver for lærlingen |
| [bedrift](klasser/bedrift.md) | Referanse til bedrifta lærlingen er i |
| [beskrivelse](klasser/beskrivelse.md) | Skildring av gruppa |
| [betalingsstatus](klasser/betalingsstatus.md) |  |
| [bevistypar](klasser/bevistypar.md) |  |
| [bevistype](klasser/bevistype.md) | Type kompetansebevis |
| [bilde](klasser/bilde.md) | HTTP(S)-lenkje til eit bilete av personen |
| [bokstavkode](klasser/bokstavkode.md) | Bokstavkode for aktuell valuta |
| [bostedsadresse](klasser/bostedsadresse.md) | Folkeregistrert adresse til personen |
| [brevtypar](klasser/brevtypar.md) |  |
| [brevtype](klasser/brevtype.md) | Type brev knytt til prøva |
| [bruksnummer](klasser/bruksnummer.md) | Fortløpande nummerering av bruk under gårdsnummer |
| [delegert](klasser/delegert.md) | Angir om deltakinga er delegert |
| [delegertTil](klasser/delegerttil.md) | Referanse til den deltakinga er delegert til |
| [domenenavn](klasser/domenenavn.md) | Domenenamn for skulen |
| [eksamen](klasser/eksamen.md) |  |
| [eksamensdato](klasser/eksamensdato.md) | Dato for eksamenen |
| [eksamensform](klasser/eksamensform.md) | Eksamensform knytt til tilrettelegginga |
| [eksamensformer](klasser/eksamensformer.md) |  |
| [eksamensgruppe](klasser/eksamensgruppe.md) | Eksamensgrupper ved skulen |
| [eksamensgruppemedlemskap](klasser/eksamensgruppemedlemskap.md) |  |
| [eksamensgrupper](klasser/eksamensgrupper.md) |  |
| [eksamensvurdering](klasser/eksamensvurdering.md) |  |
| [elev](klasser/elev.md) | Eleven dette forholdet gjeld |
| [elevar](klasser/elevar.md) |  |
| [elevforhold](klasser/elevforhold.md) |  |
| [elevfravar](klasser/elevfravar.md) |  |
| [elevkategoriar](klasser/elevkategoriar.md) |  |
| [elevnummer](klasser/elevnummer.md) | Skulens interne elevnummer |
| [elevtilrettelegging](klasser/elevtilrettelegging.md) |  |
| [elevvurdering](klasser/elevvurdering.md) |  |
| [endretDato](klasser/endretdato.md) | Dato og tidspunkt for endringa |
| [enhet](klasser/enhet.md) | OT-eining knytt til ungdommen |
| [epostadresse](klasser/epostadresse.md) | Namngitt elektronisk adresse for mottak av e-post |
| [etternavn](klasser/etternavn.md) | Etternamn til personen |
| [fag](klasser/fag.md) |  |
| [faggruppe](klasser/faggruppe.md) | Faggrupper ved skulen |
| [faggruppemedlemskap](klasser/faggruppemedlemskap.md) |  |
| [faggrupper](klasser/faggrupper.md) |  |
| [fagmerknad](klasser/fagmerknad.md) | Merknad til faget for dette medlemskapet |
| [fagmerknader](klasser/fagmerknader.md) |  |
| [fagstatus](klasser/fagstatus.md) |  |
| [feidenavn](klasser/feidenavn.md) | Feide-identifikator for skoleressursen |
| [festenummer](klasser/festenummer.md) | Fortløpande nummerering av festar under gårdsnummer/bruksnummer |
| [fodselsdato](klasser/fodselsdato.md) | Dato for fødsel |
| [fodselsnummer](klasser/fodselsnummer.md) | Fødselsnummer eller ein av dei fiktive variantane |
| [foreldre](klasser/foreldre.md) | Den/dei som har foreldreansvar til personen |
| [foreldreansvar](klasser/foreldreansvar.md) | Personar denne personen har foreldreansvar for |
| [forersPaaVitnemaal](klasser/forerspaavitnemaal.md) | Angir om fråværet vert ført på vitnemålet |
| [foretrukketSensor](klasser/foretrukketsensor.md) | Angir om sensor er føretrekt |
| [foretrukketSkole](klasser/foretrukketskole.md) | Angir om skulen er føretrekt for eksamenen |
| [fornavn](klasser/fornavn.md) | Fornamn til personen |
| [forretningsadresse](klasser/forretningsadresse.md) | Forretningsadresse til skulen |
| [fravaerstimer](klasser/fravaerstimer.md) | Antal fråværstimar |
| [fravarsoversikt](klasser/fravarsoversikt.md) |  |
| [fravarsprosent](klasser/fravarsprosent.md) | Fråværsprosent ved utsending av varselet |
| [fravartypar](klasser/fravartypar.md) |  |
| [fravartype](klasser/fravartype.md) | Type fråvær |
| [fraversregistrering](klasser/fraversregistrering.md) |  |
| [fraversregistreringer](klasser/fraversregistreringer.md) | Fråværsregistreringar knytt til elevforholdet |
| [fullfortkode](klasser/fullfortkode.md) | Kode for fullførtresultatet |
| [fullfortkoder](klasser/fullfortkoder.md) |  |
| [fylke](klasser/fylke.md) | Fylket kommunen høyrer til |
| [gaardsnummer](klasser/gaardsnummer.md) | Nummerering av gårdseiging i matrikkelen, unik innanfor kommune |
| [grepreferanse](klasser/grepreferanse.md) | Referanse til GREP-registeret |
| [gruppemedlemskap](klasser/gruppemedlemskap.md) | Medlemskapar i denne kontaktlærergruppa |
| [gyldighetsperiode](klasser/gyldighetsperiode.md) | Perioden medlemskapet er gyldig |
| [halvaar](klasser/halvaar.md) | Fråværsprosent for halvåret |
| [halvaarsfagvurdering](klasser/halvaarsfagvurdering.md) |  |
| [halvaarsordensvurdering](klasser/halvaarsordensvurdering.md) |  |
| [id](klasser/id.md) | URI-identifikator for ressursen |
| [identifikatorverdi](klasser/identifikatorverdi.md) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [juridiskNavn](klasser/juridisknavn.md) | Juridisk namn på skulen |
| [kandidatnummer](klasser/kandidatnummer.md) | Kandidatnummer for eksamenen |
| [karakter](klasser/karakter.md) | Karakterverdien gjeve i vurderinga |
| [karakteransvarlig](klasser/karakteransvarlig.md) | Skoleressurs som er ansvarleg for karakteren |
| [karakterhistorie](klasser/karakterhistorie.md) |  |
| [karakterskalaer](klasser/karakterskalaer.md) |  |
| [karakterstatus](klasser/karakterstatus.md) |  |
| [karakterverdi](klasser/karakterverdi.md) | Ny karakterverdi etter endringa |
| [karakterverdiar](klasser/karakterverdiar.md) |  |
| [kategori](klasser/kategori.md) | Kategori for elevforholdet |
| [kjonn](klasser/kjonn.md) | Kjønn for personen |
| [klasse](klasser/klasse.md) | Klassen dette medlemskapet er i |
| [klassemedlemskap](klasser/klassemedlemskap.md) |  |
| [klasser](klasser/klasser.md) |  |
| [kode](klasser/kode.md) |  |
| [kommentar](klasser/kommentar.md) | Kommentar til vurderinga |
| [kommune](klasser/kommune.md) | Referanse til kommunen OT-eininga dekker |
| [kommunenummer](klasser/kommunenummer.md) | Nummerering av kommunen i høve til SSB si offisielle liste |
| [kontaktinformasjon](klasser/kontaktinformasjon.md) | Den føretrekte måten å kome i kontakt med ein aktør |
| [kontaktlaerergruppe](klasser/kontaktlaerergruppe.md) | Kontaktlærergrupper knytt til klassen |
| [kontaktlaerergruppemedlemskap](klasser/kontaktlaerergruppemedlemskap.md) |  |
| [kontaktlaerergrupper](klasser/kontaktlaerergrupper.md) |  |
| [kontaktperson](klasser/kontaktperson.md) | Personar kontaktpersonen er pårørande for |
| [kontraktstype](klasser/kontraktstype.md) | Type kontrakt for lærlingen |
| [laerling](klasser/laerling.md) | Lærlingen som avla prøva |
| [laerlingar](klasser/laerlingar.md) |  |
| [land](klasser/land.md) | Land der adressa befinn seg |
| [laretid](klasser/laretid.md) | Læringstidsperiode for lærlingen |
| [maalform](klasser/maalform.md) | Målform personen føretrekkjer |
| [mellomnavn](klasser/mellomnavn.md) | Mellomnamn |
| [mobiltelefonnummer](klasser/mobiltelefonnummer.md) | Mobiltelefonnummer |
| [morsmaal](klasser/morsmaal.md) | Morsmål til personen |
| [navn](klasser/navn.md) | Namn på gruppa |
| [nettsted](klasser/nettsted.md) | Adresse til eit nettstad |
| [nummerkode](klasser/nummerkode.md) | Nummerkode for aktuell valuta |
| [nus](klasser/nus.md) | NUS-kode knytt til eksamensgruppemedlemskapet |
| [oppdatertAv](klasser/oppdatertav.md) | Skoleressurs som oppdaterte karakteren |
| [oppmoetetidspunkt](klasser/oppmoetetidspunkt.md) | Tidspunkt for oppmøte til eksamenen |
| [opprinneligKarakterstatus](klasser/opprinneligkarakterstatus.md) | Opphavleg karakterstatus før endringa |
| [opprinneligKarakterverdi](klasser/opprinneligkarakterverdi.md) | Opphavleg karakterverdi før endringa |
| [orden](klasser/orden.md) | Karakterverdi for orden |
| [organisasjon](klasser/organisasjon.md) | Referanse til Organisasjonselement i Administrasjon-domenet |
| [organisasjonsnavn](klasser/organisasjonsnavn.md) | Organisasjonsnamn for skulen |
| [organisasjonsnummer](klasser/organisasjonsnummer.md) | Organisasjonsnummer-identifikator |
| [otEnheter](klasser/otenheter.md) |  |
| [otStatus](klasser/otstatus.md) |  |
| [otUngdom](klasser/otungdom.md) |  |
| [otungdom](klasser/otungdom.md) | Referanse til OtUngdom (Utdanning) |
| [parorende](klasser/parorende.md) | Pårørande kontaktperson til personen |
| [passiv](klasser/passiv.md) |  |
| [periode](klasser/periode.md) | Perioden fråværet varte |
| [person](klasser/person.md) | Referanse til Person i Administrasjon-domenet |
| [personalressurs](klasser/personalressurs.md) | Referanse til Personalressurs i Administrasjon-domenet |
| [persongruppe](klasser/persongruppe.md) | Persongruppa dette medlemskapet er i |
| [persongruppemedlemskap](klasser/persongruppemedlemskap.md) |  |
| [persongrupper](klasser/persongrupper.md) |  |
| [postadresse](klasser/postadresse.md) | Postadresse til skulen |
| [postnummer](klasser/postnummer.md) | Postnummer |
| [poststed](klasser/poststed.md) | Poststad |
| [programomrade](klasser/programomrade.md) | Programområde knytt til årstrinnet |
| [programomrademedlemskap](klasser/programomrademedlemskap.md) |  |
| [programomrader](klasser/programomrader.md) |  |
| [prosent](klasser/prosent.md) | Fråværsprosent (heiltal) |
| [provedato](klasser/provedato.md) | Dato prøva vart avlagt |
| [provestatus](klasser/provestatus.md) | Status for prøva |
| [provestatuser](klasser/provestatuser.md) |  |
| [registrertAv](klasser/registrertav.md) | Skoleressurs som registrerte fråværet |
| [rom](klasser/rom.md) |  |
| [seksjonsnummer](klasser/seksjonsnummer.md) | Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer |
| [sendt](klasser/sendt.md) | Dato varselet vart sendt |
| [sensor](klasser/sensor.md) |  |
| [sensornummer](klasser/sensornummer.md) | Sensornummer |
| [sip](klasser/sip.md) | SIP-protokoll for VoIP (IP-telefoni) |
| [skala](klasser/skala.md) | Karakterskalaen denne verdien tilhøyrer |
| [skolar](klasser/skolar.md) |  |
| [skole](klasser/skole.md) | Skulen eleven er tilknytt |
| [skoleaar](klasser/skoleaar.md) |  |
| [skoleaarFravar](klasser/skoleaarfravar.md) | Fråværsprosent for heile skoleåret |
| [skoleeierType](klasser/skoleeiertype.md) | Kategori for skuleeigartilknyting |
| [skoleeijartypar](klasser/skoleeijartypar.md) |  |
| [skolenummer](klasser/skolenummer.md) | Nasjonal skulenummer-identifikator |
| [skoleressurs](klasser/skoleressurs.md) | Skoleressursar knytt til gruppa |
| [skoleressursar](klasser/skoleressursar.md) |  |
| [slutt](klasser/slutt.md) | Til tidspunkt |
| [sluttfagvurdering](klasser/sluttfagvurdering.md) |  |
| [sluttordensvurdering](klasser/sluttordensvurdering.md) |  |
| [start](klasser/start.md) | Frå tidspunkt |
| [statsborgerskap](klasser/statsborgerskap.md) | Alle statsborgarskap personen har |
| [status](klasser/status.md) | OT-status for ungdommen |
| [tekst](klasser/tekst.md) | Innhald i varselet |
| [telefonnummer](klasser/telefonnummer.md) | Telefonnummer |
| [termin](klasser/termin.md) | Terminar klassen er aktiv i |
| [terminar](klasser/terminar.md) |  |
| [tidsrom](klasser/tidsrom.md) | Tidsrom for eksamenen |
| [tilrettelegging](klasser/tilrettelegging.md) |  |
| [timar](klasser/timar.md) |  |
| [time](klasser/time.md) | Timar haldne i dette rommet |
| [tosprakligFagopplaering](klasser/tosprakligfagopplaering.md) | Indikerer om eleven har tospråkleg fagopplæring |
| [trinn](klasser/trinn.md) | Årstrinnet klassen tilhøyrer |
| [type](klasser/type.md) | Type varsel |
| [underveisfagvurdering](klasser/underveisfagvurdering.md) |  |
| [underveisordensvurdering](klasser/underveisordensvurdering.md) |  |
| [undervisningsforhold](klasser/undervisningsforhold.md) |  |
| [undervisningsgruppe](klasser/undervisningsgruppe.md) | Undervisningsgrupper som underviser i faget |
| [undervisningsgruppemedlemskap](klasser/undervisningsgruppemedlemskap.md) |  |
| [undervisningsgrupper](klasser/undervisningsgrupper.md) |  |
| [undervisningstimer](klasser/undervisningstimer.md) | Totalt antal undervisningstimar |
| [utdanningsprogram](klasser/utdanningsprogram.md) |  |
| [utsteder](klasser/utsteder.md) | Skoleressurs som sende varselet |
| [varsel](klasser/varsel.md) |  |
| [varseltypar](klasser/varseltypar.md) |  |
| [verdi](klasser/verdi.md) | Karakterverdiar i denne skalaen |
| [vigoreferanse](klasser/vigoreferanse.md) | Referanse til Vigo-systemet |
| [virksomhetsId](klasser/virksomhetsid.md) | Intern unik identifikator i økonomisystemet |
| [vitnemalsmerknad](klasser/vitnemalsmerknad.md) |  |
| [vurderingsdato](klasser/vurderingsdato.md) | Dato og tidspunkt for vurderinga |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](klasser/boolean.md) | A binary (true or false) value |
| [Curie](klasser/curie.md) | a compact URI |
| [Date](klasser/date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](klasser/dateordatetime.md) | Either a date or a datetime |
| [Datetime](klasser/datetime.md) | The combination of a date and time |
| [Decimal](klasser/decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](klasser/double.md) | A real number that conforms to the xsd:double specification |
| [Float](klasser/float.md) | A real number that conforms to the xsd:float specification |
| [Integer](klasser/integer.md) | An integer |
| [Jsonpath](klasser/jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](klasser/jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](klasser/ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](klasser/nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](klasser/objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](klasser/sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](klasser/string.md) | A character string |
| [Time](klasser/time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](klasser/uri.md) | a complete URI |
| [Uriorcurie](klasser/uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](klasser/anbefalt.md) | Anbefalt eigensskap |
| [Obligatorisk](klasser/obligatorisk.md) | Obligatorisk eigensskap |
| [Valgfri](klasser/valgfri.md) | Valfri eigensskap |
