

# Slot: transaksjonstidspunkt 


_Tidspunkt for registrering av transaksjonen._





URI: [okn:transaksjonstidspunkt](https://schema.fintlabs.no/okonomi/transaksjonstidspunkt)
Alias: transaksjonstidspunkt

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
| Slot URI | [okn:transaksjonstidspunkt](https://schema.fintlabs.no/okonomi/transaksjonstidspunkt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:transaksjonstidspunkt |
| native | https://schema.fintlabs.no/okonomi/:transaksjonstidspunkt |




## LinkML Source

<details>
```yaml
name: transaksjonstidspunkt
description: Tidspunkt for registrering av transaksjonen.
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:transaksjonstidspunkt
alias: transaksjonstidspunkt
domain_of:
- Transaksjon
range: datetime

```
</details>