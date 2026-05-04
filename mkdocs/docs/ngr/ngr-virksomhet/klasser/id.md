

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/ngr-virksomhet/id](https://data.norge.no/linkml/ngr-virksomhet/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sektorkode](Sektorkode.md) | Institusjonell sektorkode som klassifiserer kva sektor verksemda tilhøyrer (t |  no  |
| [Prokura](Prokura.md) | Prokura gjev ein person fullmakt til å handle på vegne av verksemda i nærings... |  no  |
| [Rolleinnehaver](Rolleinnehaver.md) | Den som innehar ein rolle i ei verksemd |  no  |
| [Aktivitet](Aktivitet.md) | Skildring av kva aktivitet ei hovudeining utøver |  no  |
| [GeografiskAdresse](GeografiskAdresse.md) | Abstrakt klasse for geografiske adresser |  no  |
| [Naeringskode](Naeringskode.md) | Næringskode basert på SSBs Standard for næringsgruppering (SN2007/NACE) |  no  |
| [Postadresse](Postadresse.md) | Postadressa verksemda mottar post på |  no  |
| [Underenhet](Underenhet.md) | Ei underleining er ein geografisk lokasjon der aktiviteten til ei hovudeining... |  no  |
| [Person](Person.md) | Ein fysisk person |  no  |
| [Tilstand](Tilstand.md) | Registrert tilstand (status) for ei verksemd i Enhetsregisteret, med gyldighe... |  no  |
| [Kontaktinformasjon](Kontaktinformasjon.md) | Kontaktinformasjon for verksemda registrert i Enhetsregisteret |  no  |
| [Hovedenhet](Hovedenhet.md) | Ei hovudeining er den juridiske eininga registrert i Enhetsregisteret (t |  no  |
| [Forretningsadresse](Forretningsadresse.md) | Forretningsadressa til hovudeininga – adressa der hovudkontoret held til |  no  |
| [Virksomhet](Virksomhet.md) | Abstrakt overklasse for alle einingar registrert i Enhetsregisteret |  no  |
| [Varslingsadresse](Varslingsadresse.md) | Offisiell varslingsadresse for verksemda – e-post eller mobilnummer som vert ... |  no  |
| [Beliggenhetsadresse](Beliggenhetsadresse.md) | Beliggenheitsadressa til underleininga – den fysiske adressa der aktiviteten ... |  no  |
| [Signaturrett](Signaturrett.md) | Bestemmelse om kven som har rett til å signere på vegne av verksemda (t |  no  |
| [Organisasjonsform](Organisasjonsform.md) | Klassifikasjon av juridisk organisasjonsform (t |  no  |
| [RolleIVirksomhet](RolleIVirksomhet.md) | Ein definert rolle i ei hovudeining (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Virksomhet](Virksomhet.md), [Tilstand](Tilstand.md), [Organisasjonsform](Organisasjonsform.md), [Naeringskode](Naeringskode.md), [Sektorkode](Sektorkode.md), [Kontaktinformasjon](Kontaktinformasjon.md), [Varslingsadresse](Varslingsadresse.md), [Aktivitet](Aktivitet.md), [RolleIVirksomhet](RolleIVirksomhet.md), [Rolleinnehaver](Rolleinnehaver.md), [Signaturrett](Signaturrett.md), [Prokura](Prokura.md), [GeografiskAdresse](GeografiskAdresse.md), [Person](Person.md) |

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