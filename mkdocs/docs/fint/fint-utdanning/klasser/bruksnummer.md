

# Slot: bruksnummer 


_Fortløpande nummerering av bruk under gårdsnummer._





URI: [fint:bruksnummer](https://schema.fintlabs.no/bruksnummer)
Alias: bruksnummer

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
| Slot URI | [fint:bruksnummer](https://schema.fintlabs.no/bruksnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Matrikkelnummer](Matrikkelnummer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:bruksnummer |
| native | https://schema.fintlabs.no/utdanning/:bruksnummer |




## LinkML Source

<details>
```yaml
name: bruksnummer
description: Fortløpande nummerering av bruk under gårdsnummer.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: fint:bruksnummer
alias: bruksnummer
owner: Matrikkelnummer
domain_of:
- Matrikkelnummer
range: string

```
</details>