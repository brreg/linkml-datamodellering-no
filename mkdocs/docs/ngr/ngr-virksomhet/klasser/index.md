# Nasjonale grunndata – Virksomhet

Domenemodell for verksemdsdata basert på Nasjonale grunndata (utkast). Modellerer Virksomhet med Underenhet og Hovudeining, roller, adresser og klassifikasjonar frå Enhetsregisteret. Basert på https://informasjonsforvaltning.github.io/nasjonale-grunndata/

URI: https://data.norge.no/linkml/ngr-virksomhet

Name: ngr-virksomhet



## Classes

| Class | Description |
| --- | --- |
| [Aktivitet](Aktivitet.md) | Skildring av kva aktivitet ei hovudeining utøver |
| [GeografiskAdresse](GeografiskAdresse.md) | Abstrakt klasse for geografiske adresser |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Beliggenhetsadresse](Beliggenhetsadresse.md) | Beliggenheitsadressa til underleininga – den fysiske adressa der aktiviteten ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Forretningsadresse](Forretningsadresse.md) | Forretningsadressa til hovudeininga – adressa der hovudkontoret held til |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Postadresse](Postadresse.md) | Postadressa verksemda mottar post på |
| [Kontaktinformasjon](Kontaktinformasjon.md) | Kontaktinformasjon for verksemda registrert i Enhetsregisteret |
| [Naeringskode](Naeringskode.md) | Næringskode basert på SSBs Standard for næringsgruppering (SN2007/NACE) |
| [Organisasjonsform](Organisasjonsform.md) | Klassifikasjon av juridisk organisasjonsform (t |
| [Person](Person.md) | Ein fysisk person |
| [Prokura](Prokura.md) | Prokura gjev ein person fullmakt til å handle på vegne av verksemda i nærings... |
| [Rolleinnehaver](Rolleinnehaver.md) | Den som innehar ein rolle i ei verksemd |
| [RolleIVirksomhet](RolleIVirksomhet.md) | Ein definert rolle i ei hovudeining (t |
| [Sektorkode](Sektorkode.md) | Institusjonell sektorkode som klassifiserer kva sektor verksemda tilhøyrer (t |
| [Signaturrett](Signaturrett.md) | Bestemmelse om kven som har rett til å signere på vegne av verksemda (t |
| [Tilstand](Tilstand.md) | Registrert tilstand (status) for ei verksemd i Enhetsregisteret, med gyldighe... |
| [Varslingsadresse](Varslingsadresse.md) | Offisiell varslingsadresse for verksemda – e-post eller mobilnummer som vert ... |
| [Virksomhet](Virksomhet.md) | Abstrakt overklasse for alle einingar registrert i Enhetsregisteret |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Hovedenhet](Hovedenhet.md) | Ei hovudeining er den juridiske eininga registrert i Enhetsregisteret (t |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Underenhet](Underenhet.md) | Ei underleining er ein geografisk lokasjon der aktiviteten til ei hovudeining... |
| [VirksomhetContainer](VirksomhetContainer.md) | Rotklasse for NGR-virksomhet-datafiler |



## Slots

| Slot | Description |
| --- | --- |
| [aktivitet_beskrivelse](aktivitet_beskrivelse.md) | Skildring av kva aktivitet verksemda utøver (formålsparagraf o |
| [aktivitetar](aktivitetar.md) |  |
| [antall_ansatte](antall_ansatte.md) | Antal tilsette i verksemda (rapportert til a-ordninga) |
| [beliggenhetsadresser](beliggenhetsadresser.md) |  |
| [eierskiftedatoer](eierskiftedatoer.md) | Dato(ar) for eigarskifte i underleininga |
| [epostadresse](epostadresse.md) | E-postadresse for verksemda |
| [er_hovednaeringskode](er_hovednaeringskode.md) | Om dette er hovudnæringskoden til verksemda |
| [er_klassifisert_i_naeringskode](er_klassifisert_i_naeringskode.md) | Næringskode(r) verksemda er klassifisert under (1–3) |
| [er_klassifisert_i_sektorkode](er_klassifisert_i_sektorkode.md) | Institusjonell sektorkode for hovudeininga |
| [er_klassifisert_som_organisasjonsform](er_klassifisert_som_organisasjonsform.md) | Organisasjonsform (juridisk form) for verksemda |
| [forretningsadresser](forretningsadresser.md) |  |
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
| [hovedenheter](hovedenheter.md) |  |
| [id](id.md) | URI-identifikator for ressursen |
| [kan_vaere_av_type_person](kan_vaere_av_type_person.md) | Personen som er rolleinnehavar (frå Folkeregisteret) |
| [kontaktinformasjon](kontaktinformasjon.md) |  |
| [mobiltelefonnummer](mobiltelefonnummer.md) | Mobiltelefonnummer for verksemda |
| [mottar_post_paa](mottar_post_paa.md) | Postadressa verksemda mottar post på |
| [naeringskode_beskrivelse](naeringskode_beskrivelse.md) | Tekstleg skildring av næringskoden |
| [naeringskode_kode](naeringskode_kode.md) | NACE-kode for næringsgruppering (t |
| [naeringskoder](naeringskoder.md) |  |
| [navn](navn.md) | Registrert namn på verksemda i Enhetsregisteret |
| [nedleggelsesdato](nedleggelsesdato.md) | Datoen underleininga vart lagt ned |
| [nettside](nettside.md) | URL til nettsida til verksemda |
| [oppstartsdato](oppstartsdato.md) | Datoen underleininga vart oppretta/starta |
| [organisasjonsform_beskrivelse](organisasjonsform_beskrivelse.md) | Tekstleg skildring av organisasjonsforma |
| [organisasjonsform_kode](organisasjonsform_kode.md) | Kode for organisasjonsform (t |
| [organisasjonsformer](organisasjonsformer.md) |  |
| [organisasjonsnummer](organisasjonsnummer.md) | Niesifra organisasjonsnummer tildelt av Enhetsregisteret |
| [postadresser](postadresser.md) |  |
| [prokura_bestemmelse](prokura_bestemmelse.md) | Tekstleg bestemmelse om prokura og kven som er tildelt den |
| [prokuraer](prokuraer.md) |  |
| [rollebetegnelse](rollebetegnelse.md) | Kva type rolle dette er (dagleg leiar, styreleiar o |
| [rolleinnehaver_navn](rolleinnehaver_navn.md) | Namn på rolleinnehavar (nyttes for institusjonelle rollehavarar) |
| [rolleinnehavere](rolleinnehavere.md) |  |
| [rollerIVirksomhet](rollerIVirksomhet.md) |  |
| [sektorkode_beskrivelse](sektorkode_beskrivelse.md) | Tekstleg skildring av sektorkoden |
| [sektorkode_kode](sektorkode_kode.md) | Institusjonell sektorkode (t |
| [sektorkoder](sektorkoder.md) |  |
| [signaturrett_bestemmelse](signaturrett_bestemmelse.md) | Tekstleg bestemmelse om signaturrett (t |
| [signaturrettar](signaturrettar.md) |  |
| [stiftelsesdato](stiftelsesdato.md) | Datoen hovudeininga vart stifta |
| [telefonnummer](telefonnummer.md) | Telefonnummer for verksemda |
| [tilstander](tilstander.md) |  |
| [tilstandstype](tilstandstype.md) | Type tilstand (AKTIV, UNDER_KONKURS o |
| [underenheter](underenheter.md) |  |
| [utoevar_aktivitet](utoevar_aktivitet.md) | Aktiviteten hovudeininga utøver |
| [varslingsadresser](varslingsadresser.md) |  |
| [varslingstype](varslingstype.md) | Kanaltype for varsling (EPOST eller MOBILTELEFON) |
| [varslingsverdi](varslingsverdi.md) | Verdien for varslingskanalen (e-postadresse eller mobilnummer) |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [RolleType](RolleType.md) | Type rolle ein person eller eining kan ha i ei verksemd |
| [TilstandType](TilstandType.md) | Status for ei verksemd registrert i Enhetsregisteret |
| [VarslingType](VarslingType.md) | Kanaltype for varsling til verksemda |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](Anbefalt.md) | Anbefalte eigenskapar i domenemodellen |
| [Obligatorisk](Obligatorisk.md) | Obligatoriske eigenskapar i domenemodellen |
| [Valgfri](Valgfri.md) | Valfrie eigenskapar i domenemodellen |
