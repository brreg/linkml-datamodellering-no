

# Slot: data 


_Bilagets fil, koda som Base64._





URI: [okn:data](https://schema.fintlabs.no/okonomi/data)
Alias: data

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
| Slot URI | [okn:data](https://schema.fintlabs.no/okonomi/data) |

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
| self | okn:data |
| native | https://schema.fintlabs.no/okonomi/:data |




## LinkML Source

<details>
```yaml
name: data
description: Bilagets fil, koda som Base64.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:data
alias: data
owner: Bilag
domain_of:
- Bilag
range: string

```
</details>