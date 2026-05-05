

# Slot: fakturert 


_Status på utsending._





URI: [okn:fakturert](https://schema.fintlabs.no/okonomi/fakturert)
Alias: fakturert

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](boolean.md) |
| Domain Of | [Faktura](faktura.md) |
| Slot URI | [okn:fakturert](https://schema.fintlabs.no/okonomi/fakturert) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Faktura](faktura.md) |








## In Subsets


* [Anbefalt](anbefalt.md)






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