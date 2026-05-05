

# Slot: kommunenummer 


_Nummerering av kommunen i høve til SSB si offisielle liste._





URI: [fint:kommunenummer](https://schema.fintlabs.no/kommunenummer)
Alias: kommunenummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kommune](kommune.md) |
| Domain Of | [Matrikkelnummer](matrikkelnummer.md) |
| Slot URI | [fint:kommunenummer](https://schema.fintlabs.no/kommunenummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Matrikkelnummer](matrikkelnummer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kommunenummer |
| native | https://schema.fintlabs.no/ressurs/:kommunenummer |




## LinkML Source

<details>
```yaml
name: kommunenummer
description: Nummerering av kommunen i høve til SSB si offisielle liste.
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: fint:kommunenummer
alias: kommunenummer
owner: Matrikkelnummer
domain_of:
- Matrikkelnummer
range: Kommune

```
</details>