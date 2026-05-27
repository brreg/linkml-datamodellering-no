

# Slot: fakturanummer 


_Identifikator oppretta i fakturaprogrammet._





URI: [okn:fakturanummer](https://schema.fintlabs.no/okonomi/fakturanummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Faktura](faktura.md) |
| Slot URI | [okn:fakturanummer](https://schema.fintlabs.no/okonomi/fakturanummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:fakturanummer |
| native | https://schema.fintlabs.no/okonomi/:fakturanummer |




## LinkML Source

<details>
```yaml
name: fakturanummer
description: Identifikator oppretta i fakturaprogrammet.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:fakturanummer
domain_of:
- Faktura
range: Identifikator
inlined: true

```
</details>