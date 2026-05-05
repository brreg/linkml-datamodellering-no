

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/ngr-virksomhet/id](https://data.norge.no/linkml/ngr-virksomhet/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Hovedenhet](hovedenhet.md) | Ei hovudeining er den juridiske eininga registrert i Enhetsregisteret (t |  no  |
| [Signaturrett](signaturrett.md) | Bestemmelse om kven som har rett til å signere på vegne av verksemda (t |  no  |
| [Postadresse](postadresse.md) | Postadressa verksemda mottar post på |  no  |
| [Beliggenhetsadresse](beliggenhetsadresse.md) | Beliggenheitsadressa til underleininga – den fysiske adressa der aktiviteten ... |  no  |
| [Varslingsadresse](varslingsadresse.md) | Offisiell varslingsadresse for verksemda – e-post eller mobilnummer som vert ... |  no  |
| [Underenhet](underenhet.md) | Ei underleining er ein geografisk lokasjon der aktiviteten til ei hovudeining... |  no  |
| [RolleIVirksomhet](rolleivirksomhet.md) | Ein definert rolle i ei hovudeining (t |  no  |
| [Person](person.md) | Ein fysisk person |  no  |
| [Rolleinnehaver](rolleinnehaver.md) | Den som innehar ein rolle i ei verksemd |  no  |
| [Organisasjonsform](organisasjonsform.md) | Klassifikasjon av juridisk organisasjonsform (t |  no  |
| [Sektorkode](sektorkode.md) | Institusjonell sektorkode som klassifiserer kva sektor verksemda tilhøyrer (t |  no  |
| [Forretningsadresse](forretningsadresse.md) | Forretningsadressa til hovudeininga – adressa der hovudkontoret held til |  no  |
| [Tilstand](tilstand.md) | Registrert tilstand (status) for ei verksemd i Enhetsregisteret, med gyldighe... |  no  |
| [Kontaktinformasjon](kontaktinformasjon.md) | Kontaktinformasjon for verksemda registrert i Enhetsregisteret |  no  |
| [Aktivitet](aktivitet.md) | Skildring av kva aktivitet ei hovudeining utøver |  no  |
| [Naeringskode](naeringskode.md) | Næringskode basert på SSBs Standard for næringsgruppering (SN2007/NACE) |  no  |
| [Virksomhet](virksomhet.md) | Abstrakt overklasse for alle einingar registrert i Enhetsregisteret |  no  |
| [GeografiskAdresse](geografiskadresse.md) | Abstrakt klasse for geografiske adresser |  no  |
| [Prokura](prokura.md) | Prokura gjev ein person fullmakt til å handle på vegne av verksemda i nærings... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Virksomhet](virksomhet.md), [Tilstand](tilstand.md), [Organisasjonsform](organisasjonsform.md), [Naeringskode](naeringskode.md), [Sektorkode](sektorkode.md), [Kontaktinformasjon](kontaktinformasjon.md), [Varslingsadresse](varslingsadresse.md), [Aktivitet](aktivitet.md), [RolleIVirksomhet](rolleivirksomhet.md), [Rolleinnehaver](rolleinnehaver.md), [Signaturrett](signaturrett.md), [Prokura](prokura.md), [GeografiskAdresse](geografiskadresse.md), [Person](person.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/ngr-virksomhet/id |
| native | https://data.norge.no/linkml/ngr-virksomhet/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
identifier: true
alias: id
domain_of:
- Virksomhet
- Tilstand
- Organisasjonsform
- Naeringskode
- Sektorkode
- Kontaktinformasjon
- Varslingsadresse
- Aktivitet
- RolleIVirksomhet
- Rolleinnehaver
- Signaturrett
- Prokura
- GeografiskAdresse
- Person
range: uriorcurie
required: true

```
</details>