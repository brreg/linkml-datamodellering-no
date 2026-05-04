

# Slot: seksjonsnummer 


_Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer._





URI: [fint:seksjonsnummer](https://schema.fintlabs.no/seksjonsnummer)
Alias: seksjonsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelnummer](Matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Matrikkelnummer](Matrikkelnummer.md) |
| Slot URI | [fint:seksjonsnummer](https://schema.fintlabs.no/seksjonsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Matrikkelnummer](Matrikkelnummer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:seksjonsnummer |
| native | https://schema.fintlabs.no/ressurs/:seksjonsnummer |




## LinkML Source

<details>
```yaml
name: seksjonsnummer
description: Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer.
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: fint:seksjonsnummer
alias: seksjonsnummer
owner: Matrikkelnummer
domain_of:
- Matrikkelnummer
range: string

```
</details>