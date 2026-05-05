

# Slot: bilagsnummer 


_Nummer på bilaget._





URI: [okn:bilagsnummer](https://schema.fintlabs.no/okonomi/bilagsnummer)
Alias: bilagsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bilag](bilag.md) | Dokumentasjon til ein transaksjon (kompleks datatype) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Bilag](bilag.md) |
| Slot URI | [okn:bilagsnummer](https://schema.fintlabs.no/okonomi/bilagsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Bilag](bilag.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:bilagsnummer |
| native | https://schema.fintlabs.no/okonomi/:bilagsnummer |




## LinkML Source

<details>
```yaml
name: bilagsnummer
description: Nummer på bilaget.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:bilagsnummer
alias: bilagsnummer
owner: Bilag
domain_of:
- Bilag
range: string

```
</details>