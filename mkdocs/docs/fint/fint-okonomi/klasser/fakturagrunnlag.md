

# Slot: fakturagrunnlag 


_Grunnlag for fakturering._





URI: [okn:fakturagrunnlag](https://schema.fintlabs.no/okonomi/fakturagrunnlag)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  yes  |
| [Fakturautsteder](fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |  yes  |
| [OkonomiContainer](okonomicontainer.md) | Rotcontainer for FINT Økonomi-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fakturagrunnlag](fakturagrunnlag.md) |
| Domain Of | [OkonomiContainer](okonomicontainer.md), [Faktura](faktura.md), [Fakturautsteder](fakturautsteder.md) |
| Slot URI | [okn:fakturagrunnlag](https://schema.fintlabs.no/okonomi/fakturagrunnlag) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:fakturagrunnlag |
| native | https://schema.fintlabs.no/okonomi/:fakturagrunnlag |




## LinkML Source

<details>
```yaml
name: fakturagrunnlag
description: Grunnlag for fakturering.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:fakturagrunnlag
domain_of:
- OkonomiContainer
- Faktura
- Fakturautsteder
range: Fakturagrunnlag

```
</details>