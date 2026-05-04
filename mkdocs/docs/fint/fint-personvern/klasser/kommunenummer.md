

# Slot: kommunenummer 


_Nummerering av kommunen i høve til SSB si offisielle liste._





URI: [fint:kommunenummer](https://schema.fintlabs.no/kommunenummer)
Alias: kommunenummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelnummer](Matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kommune](Kommune.md) |
| Domain Of | [Matrikkelnummer](Matrikkelnummer.md) |
| Slot URI | [fint:kommunenummer](https://schema.fintlabs.no/kommunenummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Matrikkelnummer](Matrikkelnummer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kommunenummer |
| native | https://schema.fintlabs.no/personvern/:kommunenummer |




## LinkML Source

<details>
```yaml
name: kommunenummer
description: Nummerering av kommunen i høve til SSB si offisielle liste.
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: fint:kommunenummer
alias: kommunenummer
owner: Matrikkelnummer
domain_of:
- Matrikkelnummer
range: Kommune

```
</details>