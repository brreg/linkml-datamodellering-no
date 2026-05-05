

# Slot: nummerkode 


_Nummerkode for aktuell valuta._





URI: [fint:nummerkode](https://schema.fintlabs.no/nummerkode)
Alias: nummerkode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Valuta](valuta.md) |
| Slot URI | [fint:nummerkode](https://schema.fintlabs.no/nummerkode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Valuta](valuta.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:nummerkode |
| native | https://schema.fintlabs.no/administrasjon/:nummerkode |




## LinkML Source

<details>
```yaml
name: nummerkode
description: Nummerkode for aktuell valuta.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: fint:nummerkode
alias: nummerkode
owner: Valuta
domain_of:
- Valuta
range: Identifikator
required: true
inlined: true

```
</details>