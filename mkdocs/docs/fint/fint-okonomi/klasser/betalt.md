

# Slot: betalt 


_Status på betaling._





URI: [okn:betalt](https://schema.fintlabs.no/okonomi/betalt)
Alias: betalt

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
| Slot URI | [okn:betalt](https://schema.fintlabs.no/okonomi/betalt) |

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
| self | okn:betalt |
| native | https://schema.fintlabs.no/okonomi/:betalt |




## LinkML Source

<details>
```yaml
name: betalt
description: Status på betaling.
in_subset:
- Anbefalt
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:betalt
alias: betalt
owner: Faktura
domain_of:
- Faktura
range: boolean

```
</details>