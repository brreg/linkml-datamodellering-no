

# Slot: epostadresse 


_Namngitt elektronisk adresse for mottak av e-post._





URI: [fint:epostadresse](https://schema.fintlabs.no/epostadresse)
Alias: epostadresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktinformasjon](Kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Kontaktinformasjon](Kontaktinformasjon.md) |
| Slot URI | [fint:epostadresse](https://schema.fintlabs.no/epostadresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kontaktinformasjon](Kontaktinformasjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:epostadresse |
| native | https://schema.fintlabs.no/utdanning/:epostadresse |




## LinkML Source

<details>
```yaml
name: epostadresse
description: Namngitt elektronisk adresse for mottak av e-post.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: fint:epostadresse
alias: epostadresse
owner: Kontaktinformasjon
domain_of:
- Kontaktinformasjon
range: string

```
</details>