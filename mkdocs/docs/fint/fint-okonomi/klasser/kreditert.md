

# Slot: kreditert 


_Status på kreditering._





URI: [okn:kreditert](https://schema.fintlabs.no/okonomi/kreditert)
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
| Slot URI | [okn:kreditert](https://schema.fintlabs.no/okonomi/kreditert) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:kreditert |
| native | https://schema.fintlabs.no/okonomi/:kreditert |




## LinkML Source

<details>
```yaml
name: kreditert
description: Status på kreditering.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:kreditert
domain_of:
- Faktura
range: boolean

```
</details>