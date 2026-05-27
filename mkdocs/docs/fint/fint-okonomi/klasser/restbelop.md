

# Slot: restbelop 


_Gjenståande beløp å betale, i øre._





URI: [okn:restbelop](https://schema.fintlabs.no/okonomi/restbelop)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Faktura](faktura.md) |
| Slot URI | [okn:restbelop](https://schema.fintlabs.no/okonomi/restbelop) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:restbelop |
| native | https://schema.fintlabs.no/okonomi/:restbelop |




## LinkML Source

<details>
```yaml
name: restbelop
description: Gjenståande beløp å betale, i øre.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:restbelop
domain_of:
- Faktura
range: integer

```
</details>