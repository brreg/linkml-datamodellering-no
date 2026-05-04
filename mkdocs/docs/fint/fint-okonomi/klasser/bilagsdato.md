

# Slot: bilagsdato 


_Dato bilaget er registrert._





URI: [okn:bilagsdato](https://schema.fintlabs.no/okonomi/bilagsdato)
Alias: bilagsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bilag](Bilag.md) | Dokumentasjon til ein transaksjon (kompleks datatype) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Bilag](Bilag.md) |
| Slot URI | [okn:bilagsdato](https://schema.fintlabs.no/okonomi/bilagsdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Bilag](Bilag.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:bilagsdato |
| native | https://schema.fintlabs.no/okonomi/:bilagsdato |




## LinkML Source

<details>
```yaml
name: bilagsdato
description: Dato bilaget er registrert.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:bilagsdato
alias: bilagsdato
owner: Bilag
domain_of:
- Bilag
range: date
required: true

```
</details>