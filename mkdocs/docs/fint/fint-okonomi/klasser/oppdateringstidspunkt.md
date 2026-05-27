

# Slot: oppdateringstidspunkt 


_Tidspunkt for siste endring i transaksjonen._





URI: [okn:oppdateringstidspunkt](https://schema.fintlabs.no/okonomi/oppdateringstidspunkt)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Transaksjon](transaksjon.md) |
| Slot URI | [okn:oppdateringstidspunkt](https://schema.fintlabs.no/okonomi/oppdateringstidspunkt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:oppdateringstidspunkt |
| native | https://schema.fintlabs.no/okonomi/:oppdateringstidspunkt |




## LinkML Source

<details>
```yaml
name: oppdateringstidspunkt
description: Tidspunkt for siste endring i transaksjonen.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:oppdateringstidspunkt
domain_of:
- Transaksjon
range: datetime

```
</details>