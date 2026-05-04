

# Slot: dato 


_Dato for utferding av faktura._





URI: [okn:dato](https://schema.fintlabs.no/okonomi/dato)
Alias: dato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faktura](Faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Faktura](Faktura.md) |
| Slot URI | [okn:dato](https://schema.fintlabs.no/okonomi/dato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Faktura](Faktura.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:dato |
| native | https://schema.fintlabs.no/okonomi/:dato |




## LinkML Source

<details>
```yaml
name: dato
description: Dato for utferding av faktura.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:dato
alias: dato
owner: Faktura
domain_of:
- Faktura
range: date
required: true

```
</details>