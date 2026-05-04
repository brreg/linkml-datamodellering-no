

# Slot: fakturert 


_Status på utsending._





URI: [okn:fakturert](https://schema.fintlabs.no/okonomi/fakturert)
Alias: fakturert

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faktura](Faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Faktura](Faktura.md) |
| Slot URI | [okn:fakturert](https://schema.fintlabs.no/okonomi/fakturert) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Faktura](Faktura.md) |








## In Subsets


* [Anbefalt](Anbefalt.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:fakturert |
| native | https://schema.fintlabs.no/okonomi/:fakturert |




## LinkML Source

<details>
```yaml
name: fakturert
description: Status på utsending.
in_subset:
- Anbefalt
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:fakturert
alias: fakturert
owner: Faktura
domain_of:
- Faktura
range: boolean

```
</details>