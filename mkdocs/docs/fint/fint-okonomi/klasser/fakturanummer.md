

# Slot: fakturanummer 


_Identifikator oppretta i fakturaprogrammet._





URI: [okn:fakturanummer](https://schema.fintlabs.no/okonomi/fakturanummer)
Alias: fakturanummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faktura](Faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](Identifikator.md) |
| Domain Of | [Faktura](Faktura.md) |
| Slot URI | [okn:fakturanummer](https://schema.fintlabs.no/okonomi/fakturanummer) |

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
| self | okn:fakturanummer |
| native | https://schema.fintlabs.no/okonomi/:fakturanummer |




## LinkML Source

<details>
```yaml
name: fakturanummer
description: Identifikator oppretta i fakturaprogrammet.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:fakturanummer
alias: fakturanummer
owner: Faktura
domain_of:
- Faktura
range: Identifikator
required: true
inlined: true

```
</details>