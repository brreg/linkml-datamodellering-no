

# Slot: fakturert 


_Status på utsending._





URI: [okn:fakturert](https://schema.fintlabs.no/okonomi/fakturert)
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
| Slot URI | [okn:fakturert](https://schema.fintlabs.no/okonomi/fakturert) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




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
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:fakturert
domain_of:
- Faktura
range: boolean

```
</details>