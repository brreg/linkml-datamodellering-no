

# Slot: belop 


_Beløp, i øre._





URI: [okn:belop](https://schema.fintlabs.no/okonomi/belop)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  yes  |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  yes  |
| [Postering](postering.md) | Føring på ein konto i rekneskapet |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Faktura](faktura.md), [Transaksjon](transaksjon.md), [Postering](postering.md) |
| Slot URI | [okn:belop](https://schema.fintlabs.no/okonomi/belop) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:belop |
| native | https://schema.fintlabs.no/okonomi/:belop |




## LinkML Source

<details>
```yaml
name: belop
description: Beløp, i øre.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:belop
domain_of:
- Faktura
- Transaksjon
- Postering
range: integer

```
</details>