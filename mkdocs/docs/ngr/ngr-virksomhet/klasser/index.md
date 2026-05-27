# Nasjonale grunndata – Virksomhet

Domenemodell for verksemdsdata basert på Nasjonale grunndata (utkast). Modellerer Virksomhet med Underenhet og Hovudeining, roller, adresser og klassifikasjonar frå Enhetsregisteret. Basert på https://informasjonsforvaltning.github.io/nasjonale-grunndata/

URI: https://data.norge.no/ngr/ngr-virksomhet

Name: ngr-virksomhet



## Classes







### Obligatorisk

| Class | Description |
| --- | --- |
| [Aktivitet](aktivitet.md) | Skildring av kva aktivitet ei hovudeining utøver |
| [Hovedenhet](hovedenhet.md) | Ei hovudeining er den juridiske eininga registrert i Enhetsregisteret (t |
| [Naeringskode](naeringskode.md) | Næringskode basert på SSBs Standard for næringsgruppering (SN2007/NACE) |
| [Organisasjonsform](organisasjonsform.md) | Klassifikasjon av juridisk organisasjonsform (t |
| [Prokura](prokura.md) | Prokura gjev ein person fullmakt til å handle på vegne av verksemda i nærings... |
| [RolleIVirksomhet](rolleivirksomhet.md) | Ein definert rolle i ei hovudeining (t |
| [Sektorkode](sektorkode.md) | Institusjonell sektorkode som klassifiserer kva sektor verksemda tilhøyrer (t |
| [Signaturrett](signaturrett.md) | Bestemmelse om kven som har rett til å signere på vegne av verksemda (t |
| [Tilstand](tilstand.md) | Registrert tilstand (status) for ei verksemd i Enhetsregisteret, med gyldighe... |
| [Underenhet](underenhet.md) | Ei underleining er ein geografisk lokasjon der aktiviteten til ei hovudeining... |
| [Varslingsadresse](varslingsadresse.md) | Offisiell varslingsadresse for verksemda – e-post eller mobilnummer som vert ... |
| [Virksomhet](virksomhet.md) | Abstrakt overklasse for alle einingar registrert i Enhetsregisteret |




### Anbefalt

| Class | Description |
| --- | --- |
| [Kontaktinformasjon](kontaktinformasjon.md) | Kontaktinformasjon for verksemda registrert i Enhetsregisteret |
| [Rolleinnehaver](rolleinnehaver.md) | Den som innehar ein rolle i ei verksemd |






### Andre

| Class | Description |
| --- | --- |
| [Beliggenhetsadresse](beliggenhetsadresse.md) | Beliggenheitsadressa til underleininga – den fysiske adressa der aktiviteten ... |
| [Forretningsadresse](forretningsadresse.md) | Forretningsadressa til hovudeininga – adressa der hovudkontoret held til |
| [GeografiskAdresse](geografiskadresse.md) | Abstrakt klasse for geografiske adresser |
| [Person](person.md) | Ein fysisk person |
| [Postadresse](postadresse.md) | Postadressa verksemda mottar post på |





## Slots

| Slot | Description |
| --- | --- |
| [aktivitet_beskrivelse](aktivitet_beskrivelse.md) | Skildring av kva aktivitet verksemda utøver (formålsparagraf o |
| [antall_ansatte](antall_ansatte.md) | Antal tilsette i verksemda (rapportert til a-ordninga) |
| [eierskiftedatoer](eierskiftedatoer.md) | Dato(ar) for eigarskifte i underleininga |
| [epostadresse](epostadresse.md) | E-postadresse for verksemda |
| [er_hovednaeringskode](er_hovednaeringskode.md) | Om dette er hovudnæringskoden til verksemda |
| [er_klassifisert_i_naeringskode](er_klassifisert_i_naeringskode.md) | Næringskode(r) verksemda er klassifisert under (1–3) |
| [er_klassifisert_i_sektorkode](er_klassifisert_i_sektorkode.md) | Institusjonell sektorkode for hovudeininga |
| [er_klassifisert_som_organisasjonsform](er_klassifisert_som_organisasjonsform.md) | Organisasjonsform (juridisk form) for verksemda |
| [gyldig_fra](gyldig_fra.md) | Datoen tilstanden vart gyldig frå |
| [gyldig_til](gyldig_til.md) | Datoen tilstanden vart gyldig til |
| [har_beliggenhetsadresse](har_beliggenhetsadresse.md) | Beliggenheitsadressa til underleininga |
| [har_bestemmelser_om_prokura](har_bestemmelser_om_prokura.md) | Prokurabestemmelse(r) for hovudeininga |
| [har_bestemmelser_om_signaturrett](har_bestemmelser_om_signaturrett.md) | Bestemmelse om signaturrett for hovudeininga |
| [har_forretningsadresse](har_forretningsadresse.md) | Forretningsadressa (hovudkontor) til hovudeininga |
| [har_kontaktinformasjon](har_kontaktinformasjon.md) | Kontaktinformasjon registrert på verksemda |
| [har_rolle_i_virksomhet](har_rolle_i_virksomhet.md) | Roller registrert i hovudeininga (minimum 1) |
| [har_rolleinnehaver](har_rolleinnehaver.md) | Rolleinnehavar(ar) for denne rolla |
| [har_tilstand](har_tilstand.md) | Registrert tilstand (status) for verksemda, inkl |
| [har_varslingsadresse](har_varslingsadresse.md) | Offisiell varslingsadresse for offentlege meldingar |
| [id](id.md) | URI-identifikator for ressursen |
| [kan_vaere_av_type_person](kan_vaere_av_type_person.md) | Personen som er rolleinnehavar (frå Folkeregisteret) |
| [mobiltelefonnummer](mobiltelefonnummer.md) | Mobiltelefonnummer for verksemda |
| [mottar_post_paa](mottar_post_paa.md) | Postadressa verksemda mottar post på |
| [naeringskode_beskrivelse](naeringskode_beskrivelse.md) | Tekstleg skildring av næringskoden |
| [naeringskode_kode](naeringskode_kode.md) | NACE-kode for næringsgruppering (t |
| [navn](navn.md) | Registrert namn på verksemda i Enhetsregisteret |
| [nedleggelsesdato](nedleggelsesdato.md) | Datoen underleininga vart lagt ned |
| [nettside](nettside.md) | URL til nettsida til verksemda |
| [oppstartsdato](oppstartsdato.md) | Datoen underleininga vart oppretta/starta |
| [organisasjonsform_beskrivelse](organisasjonsform_beskrivelse.md) | Tekstleg skildring av organisasjonsforma |
| [organisasjonsform_kode](organisasjonsform_kode.md) | Kode for organisasjonsform (t |
| [organisasjonsnummer](organisasjonsnummer.md) | Niesifra organisasjonsnummer tildelt av Enhetsregisteret |
| [prokura_bestemmelse](prokura_bestemmelse.md) | Tekstleg bestemmelse om prokura og kven som er tildelt den |
| [rollebetegnelse](rollebetegnelse.md) | Kva type rolle dette er (dagleg leiar, styreleiar o |
| [rolleinnehaver_navn](rolleinnehaver_navn.md) | Namn på rolleinnehavar (nyttes for institusjonelle rollehavarar) |
| [sektorkode_beskrivelse](sektorkode_beskrivelse.md) | Tekstleg skildring av sektorkoden |
| [sektorkode_kode](sektorkode_kode.md) | Institusjonell sektorkode (t |
| [signaturrett_bestemmelse](signaturrett_bestemmelse.md) | Tekstleg bestemmelse om signaturrett (t |
| [stiftelsesdato](stiftelsesdato.md) | Datoen hovudeininga vart stifta |
| [telefonnummer](telefonnummer.md) | Telefonnummer for verksemda |
| [tilstandstype](tilstandstype.md) | Type tilstand (AKTIV, UNDER_KONKURS o |
| [utoevar_aktivitet](utoevar_aktivitet.md) | Aktiviteten hovudeininga utøver |
| [varslingstype](varslingstype.md) | Kanaltype for varsling (EPOST eller MOBILTELEFON) |
| [varslingsverdi](varslingsverdi.md) | Verdien for varslingskanalen (e-postadresse eller mobilnummer) |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [RolleType](rolletype.md) | Type rolle ein person eller eining kan ha i ei verksemd |
| [TilstandType](tilstandtype.md) | Status for ei verksemd registrert i Enhetsregisteret |
| [VarslingType](varslingtype.md) | Kanaltype for varsling til verksemda |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](anbefalt.md) | Anbefalte eigenskapar i domenemodellen |
| [Obligatorisk](obligatorisk.md) | Obligatoriske eigenskapar i domenemodellen |
| [Valgfri](valgfri.md) | Valfrie eigenskapar i domenemodellen |
