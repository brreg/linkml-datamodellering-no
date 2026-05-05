

# Slot: funksjon 


_Funksjonskode (KOSTRA)._





URI: [okn:funksjon](https://schema.fintlabs.no/okonomi/funksjon)
Alias: funksjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Kontodimensjonar for ei postering (kompleks datatype) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Kontostreng](kontostreng.md) |
| Slot URI | [okn:funksjon](https://schema.fintlabs.no/okonomi/funksjon) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kontostreng](kontostreng.md) |








## In Subsets


* [Anbefalt](anbefalt.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:funksjon |
| native | https://schema.fintlabs.no/okonomi/:funksjon |




## LinkML Source

<details>
```yaml
name: funksjon
description: Funksjonskode (KOSTRA).
in_subset:
- Anbefalt
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:funksjon
alias: funksjon
owner: Kontostreng
domain_of:
- Kontostreng
range: string

```
</details>