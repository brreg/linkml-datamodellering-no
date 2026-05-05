

# Slot: festenummer 


_Fortløpande nummerering av festar under gårdsnummer/bruksnummer._





URI: [fint:festenummer](https://schema.fintlabs.no/festenummer)
Alias: festenummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Matrikkelnummer](matrikkelnummer.md) |
| Slot URI | [fint:festenummer](https://schema.fintlabs.no/festenummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Matrikkelnummer](matrikkelnummer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:festenummer |
| native | https://schema.fintlabs.no/administrasjon/:festenummer |




## LinkML Source

<details>
```yaml
name: festenummer
description: Fortløpande nummerering av festar under gårdsnummer/bruksnummer.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: fint:festenummer
alias: festenummer
owner: Matrikkelnummer
domain_of:
- Matrikkelnummer
range: string

```
</details>