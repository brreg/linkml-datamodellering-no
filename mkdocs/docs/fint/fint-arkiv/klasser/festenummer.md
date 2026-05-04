

# Slot: festenummer 


_Fortløpande nummerering av festar under gårdsnummer/bruksnummer._





URI: [fint:festenummer](https://schema.fintlabs.no/festenummer)
Alias: festenummer

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
| Slot URI | [fint:festenummer](https://schema.fintlabs.no/festenummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Matrikkelnummer](Matrikkelnummer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:festenummer |
| native | https://schema.fintlabs.no/arkiv/:festenummer |




## LinkML Source

<details>
```yaml
name: festenummer
description: Fortløpande nummerering av festar under gårdsnummer/bruksnummer.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: fint:festenummer
alias: festenummer
owner: Matrikkelnummer
domain_of:
- Matrikkelnummer
range: string

```
</details>