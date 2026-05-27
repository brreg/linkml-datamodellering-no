

# Slot: betalt 


_Status på betaling._





URI: [okn:betalt](https://schema.fintlabs.no/okonomi/betalt)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) |
| Domain Of | [Faktura](faktura.md) |
| Slot URI | [okn:betalt](https://schema.fintlabs.no/okonomi/betalt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




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
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:betalt
domain_of:
- Faktura
range: boolean

```
</details>