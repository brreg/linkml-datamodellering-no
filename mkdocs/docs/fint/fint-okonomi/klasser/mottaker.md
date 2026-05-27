

# Slot: mottaker 


_Namn på mottakar._





URI: [okn:mottaker](https://schema.fintlabs.no/okonomi/mottaker)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Faktura](faktura.md) |
| Slot URI | [okn:mottaker](https://schema.fintlabs.no/okonomi/mottaker) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:mottaker |
| native | https://schema.fintlabs.no/okonomi/:mottaker |




## LinkML Source

<details>
```yaml
name: mottaker
description: Namn på mottakar.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:mottaker
domain_of:
- Faktura
range: string

```
</details>