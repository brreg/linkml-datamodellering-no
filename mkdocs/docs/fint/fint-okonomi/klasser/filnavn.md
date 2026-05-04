

# Slot: filnavn 


_Namn på bilagets fil._





URI: [okn:filnavn](https://schema.fintlabs.no/okonomi/filnavn)
Alias: filnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bilag](Bilag.md) | Dokumentasjon til ein transaksjon (kompleks datatype) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Bilag](Bilag.md) |
| Slot URI | [okn:filnavn](https://schema.fintlabs.no/okonomi/filnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Bilag](Bilag.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:filnavn |
| native | https://schema.fintlabs.no/okonomi/:filnavn |




## LinkML Source

<details>
```yaml
name: filnavn
description: Namn på bilagets fil.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:filnavn
alias: filnavn
owner: Bilag
domain_of:
- Bilag
range: string

```
</details>