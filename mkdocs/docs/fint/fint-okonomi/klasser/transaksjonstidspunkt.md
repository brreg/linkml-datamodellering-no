

# Slot: transaksjonstidspunkt 


_Tidspunkt for registrering av transaksjonen._





URI: [okn:transaksjonstidspunkt](https://schema.fintlabs.no/okonomi/transaksjonstidspunkt)
Alias: transaksjonstidspunkt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](Transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Transaksjon](Transaksjon.md) |
| Slot URI | [okn:transaksjonstidspunkt](https://schema.fintlabs.no/okonomi/transaksjonstidspunkt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Transaksjon](Transaksjon.md) |








## In Subsets


* [Valgfri](Valgfri.md)






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
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:transaksjonstidspunkt
alias: transaksjonstidspunkt
owner: Transaksjon
domain_of:
- Transaksjon
range: datetime

```
</details>