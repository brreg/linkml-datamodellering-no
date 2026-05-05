

# Slot: restbelop 


_Gjenståande beløp å betale, i øre (restbeløp)._





URI: [okn:restbelop](https://schema.fintlabs.no/okonomi/restbelop)
Alias: restbelop

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](integer.md) |
| Domain Of | [Faktura](faktura.md) |
| Slot URI | [okn:restbelop](https://schema.fintlabs.no/okonomi/restbelop) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Faktura](faktura.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:restbelop |
| native | https://schema.fintlabs.no/okonomi/:restbelop |




## LinkML Source

<details>
```yaml
name: restbelop
description: Gjenståande beløp å betale, i øre (restbeløp).
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:restbelop
alias: restbelop
owner: Faktura
domain_of:
- Faktura
range: integer

```
</details>