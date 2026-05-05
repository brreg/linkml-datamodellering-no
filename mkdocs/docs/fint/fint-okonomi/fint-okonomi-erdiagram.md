```mermaid
erDiagram
Adresse {
    stringList adresselinje  
    string postnummer  
    string poststed  
}
Bilag {
    date bilagsdato  
    string bilagsnummer  
    string data  
    string filnavn  
    string referanse  
    string url  
}
Faktura {
    uriorcurie id  
    integer belop  
    boolean betalt  
    date dato  
    boolean fakturert  
    date forfallsdato  
    boolean kreditert  
    string mottaker  
    integer restbelop  
}
Fakturagrunnlag {
    uriorcurie id  
    integer avgiftsbelop  
    date leveringsdato  
    integer nettobelop  
    integer totalbelop  
}
Fakturalinje {
    float antall  
    stringList fritekst  
    integer pris  
}
Fakturamottaker {
    uriorcurie person  
}
Fakturautsteder {
    uriorcurie id  
    string navn  
    uriorcurie organisasjonselement  
}
Identifikator {
    string identifikatorverdi  
}
Kontostreng {
    string ansvar  
    string art  
    string funksjon  
    string prosjekt  
}
Landkode {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Leverandor {
    uriorcurie id  
    string kontonummer  
    uriorcurie person  
    uriorcurie virksomhet  
}
Leverandorgruppe {
    uriorcurie id  
    string navn  
}
Merverdiavgift {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
    integer sats  
}
OkonomiValuta {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Periode {
    string beskrivelse  
    datetime slutt  
    datetime start  
}
Postering {
    uriorcurie id  
    integer belop  
    boolean debet  
}
Transaksjon {
    uriorcurie id  
    uriorcurie ansvarlig  
    integer belop  
    string beskrivelse  
    date forfallsdato  
    datetime oppdateringstidspunkt  
    datetime transaksjonstidspunkt  
}
Vare {
    uriorcurie id  
    string enhet  
    string kode  
    string navn  
    boolean passiv  
    integer pris  
}

Adresse ||--|o Landkode : "land"
Faktura ||--|o Adresse : "adresse"
Faktura ||--|| Fakturagrunnlag : "fakturagrunnlag"
Faktura ||--|| Identifikator : "fakturanummer"
Fakturagrunnlag ||--|| Fakturamottaker : "mottaker"
Fakturagrunnlag ||--|| Fakturautsteder : "fakturautsteder"
Fakturagrunnlag ||--|| Identifikator : "ordrenummer"
Fakturagrunnlag ||--}o Faktura : "faktura"
Fakturagrunnlag ||--}| Fakturalinje : "fakturalinjer"
Fakturalinje ||--|| Vare : "vare"
Fakturautsteder ||--}o Fakturagrunnlag : "fakturagrunnlag"
Fakturautsteder ||--}o Vare : "vare"
Identifikator ||--|o Periode : "gyldighetsperiode"
Landkode ||--|o Periode : "gyldighetsperiode"
Leverandor ||--|o Identifikator : "leverandornummer"
Leverandor ||--|o Leverandorgruppe : "leverandorgruppe"
Leverandorgruppe ||--}o Leverandor : "leverandor"
Merverdiavgift ||--|o Periode : "gyldighetsperiode"
OkonomiValuta ||--|o Periode : "gyldighetsperiode"
Postering ||--|o Transaksjon : "transaksjon"
Postering ||--|| Identifikator : "posteringsId"
Postering ||--|| Kontostreng : "kontering"
Transaksjon ||--|o Leverandor : "leverandor"
Transaksjon ||--|| Identifikator : "transaksjonsId"
Transaksjon ||--|| OkonomiValuta : "valuta"
Transaksjon ||--}o Bilag : "bilag"
Transaksjon ||--}| Postering : "postering"
Vare ||--|o Kontostreng : "kontering"
Vare ||--|o Periode : "gyldighetsperiode"
Vare ||--|| Fakturautsteder : "fakturautsteder"
Vare ||--|| Merverdiavgift : "merverdiavgift"

```

