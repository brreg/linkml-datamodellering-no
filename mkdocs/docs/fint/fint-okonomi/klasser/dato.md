

# Slot: dato 


_Dato for utferding av faktura._





URI: [okn:dato](https://schema.fintlabs.no/okonomi/dato)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Faktura](faktura.md) |
| Slot URI | [okn:dato](https://schema.fintlabs.no/okonomi/dato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




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
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:dato
domain_of:
- Faktura
range: date

```
</details>