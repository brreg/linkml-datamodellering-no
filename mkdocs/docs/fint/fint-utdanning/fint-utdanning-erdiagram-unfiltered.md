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
    uriorcurieList laerling  
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
Fylke {
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
Kjonn {
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
Kommune {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Kontaktinformasjon {
    string epostadresse  
    string mobiltelefonnummer  
    string nettsted  
    string sip  
    string telefonnummer  
}
Kontaktlaerergruppe {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Kontaktlaerergruppemedlemskap {
    uriorcurie id  
}
Kontaktperson {
    uriorcurie id  
    string type  
}
Laerling {
    uriorcurie id  
    uriorcurie bedrift  
    string kontraktstype  
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
}
Periode {
    string beskrivelse  
    datetime slutt  
    datetime start  
}
Person {
    uriorcurie id  
    string bilde  
    date fodselsdato  
    uriorcurieList laerling  
    uriorcurie otungdom  
    uriorcurie personalressurs  
}
Persongruppe {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Persongruppemedlemskap {
    uriorcurie id  
}
Personnavn {
    string etternavn  
    string fornavn  
    string mellomnavn  
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
Spraak {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
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
Elev ||--|o Person : "person"
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
Fraversregistrering ||--|o Elevfravar : "elevfravar"
Fraversregistrering ||--|o Faggruppe : "faggruppe"
Fraversregistrering ||--|o Skoleressurs : "registrertAv"
Fraversregistrering ||--|| Fravartype : "fravartype"
Fraversregistrering ||--|| Periode : "periode"
Fraversregistrering ||--|| Undervisningsgruppe : "undervisningsgruppe"
Fullfortkode ||--|o Periode : "gyldighetsperiode"
Fylke ||--|o Periode : "gyldighetsperiode"
Fylke ||--}o Kommune : "kommune"
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
Kjonn ||--|o Periode : "gyldighetsperiode"
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
Kommune ||--|o Periode : "gyldighetsperiode"
Kommune ||--|| Fylke : "fylke"
Kontaktlaerergruppe ||--|o Skole : "skole"
Kontaktlaerergruppe ||--|o Skoleaar : "skoleaar"
Kontaktlaerergruppe ||--}o Kontaktlaerergruppemedlemskap : "gruppemedlemskap"
Kontaktlaerergruppe ||--}o Termin : "termin"
Kontaktlaerergruppe ||--}o Undervisningsforhold : "undervisningsforhold"
Kontaktlaerergruppe ||--}| Klasse : "klasse"
Kontaktlaerergruppemedlemskap ||--|o Elevforhold : "elevforhold"
Kontaktlaerergruppemedlemskap ||--|o Kontaktlaerergruppe : "kontaktlaerergruppe"
Kontaktlaerergruppemedlemskap ||--|o Periode : "gyldighetsperiode"
Kontaktperson ||--|o Kontaktinformasjon : "kontaktinformasjon"
Kontaktperson ||--|o Personnavn : "kontaktperson_navn"
Kontaktperson ||--}o Person : "kontaktperson"
Laerling ||--|o Periode : "laretid"
Laerling ||--|o Programomrade : "programomrade"
Laerling ||--|| Person : "person"
Laerling ||--}o AvlagtProve : "avlagtprove"
Landkode ||--|o Periode : "gyldighetsperiode"
OtEnhet ||--|o Periode : "gyldighetsperiode"
OtEnhet ||--|| Kommune : "kommune"
OtStatus ||--|o Periode : "gyldighetsperiode"
OtUngdom ||--|o OtEnhet : "enhet"
OtUngdom ||--|o OtStatus : "status"
OtUngdom ||--|o Programomrade : "programomrade"
OtUngdom ||--|| Person : "person"
Person ||--|o Adresse : "bostedsadresse, postadresse"
Person ||--|o Elev : "elev"
Person ||--|o Kjonn : "kjonn"
Person ||--|o Kommune : "kommune"
Person ||--|o Kontaktinformasjon : "kontaktinformasjon"
Person ||--|o Spraak : "maalform, morsmaal"
Person ||--|| Identifikator : "fodselsnummer"
Person ||--|| Personnavn : "person_navn"
Person ||--}o Kontaktperson : "parorende"
Person ||--}o Landkode : "statsborgerskap"
Person ||--}o Person : "foreldre, foreldreansvar"
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
Rom ||--}o Time : "skuletime"
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
Skoleressurs ||--|o Person : "person"
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
Spraak ||--|o Periode : "gyldighetsperiode"
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
Undervisningsforhold ||--}o Time : "skuletime"
Undervisningsgruppe ||--|o Skole : "skole"
Undervisningsgruppe ||--|o Skoleaar : "skoleaar"
Undervisningsgruppe ||--}o Termin : "termin"
Undervisningsgruppe ||--}o Time : "skuletime"
Undervisningsgruppe ||--}o Undervisningsforhold : "undervisningsforhold"
Undervisningsgruppe ||--}o Undervisningsgruppemedlemskap : "gruppemedlemskap"
Undervisningsgruppe ||--}| Fag : "fag"
Undervisningsgruppemedlemskap ||--|o Elevforhold : "elevforhold"
Undervisningsgruppemedlemskap ||--|o Periode : "gyldighetsperiode"
Undervisningsgruppemedlemskap ||--|o Undervisningsgruppe : "undervisningsgruppe"
Utdanningsprogram ||--}o Programomrade : "programomrade"
Utdanningsprogram ||--}o Skole : "skole"
Varsel ||--|o Skoleressurs : "karakteransvarlig, utsteder"
Varsel ||--|o Varseltype : "type"
Varsel ||--}o Faggruppemedlemskap : "faggruppemedlemskap"
Varseltype ||--|o Periode : "gyldighetsperiode"
Vitnemalsmerknad ||--|o Periode : "gyldighetsperiode"

```

