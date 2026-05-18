

# Slot: forfallsdato 


_Frist for betaling eller forfallsdato for transaksjon._





URI: [okn:forfallsdato](https://schema.fintlabs.no/okonomi/forfallsdato)
Alias: forfallsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  yes  |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Faktura](faktura.md), [Transaksjon](transaksjon.md) |
| Slot URI | [okn:forfallsdato](https://schema.fintlabs.no/okonomi/forfallsdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:forfallsdato |
| native | https://schema.fintlabs.no/okonomi/:forfallsdato |




## LinkML Source

<details>
```yaml
name: forfallsdato
description: Frist for betaling eller forfallsdato for transaksjon.
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:forfallsdato
alias: forfallsdato
domain_of:
- Faktura
- Transaksjon
range: date

```
</details>