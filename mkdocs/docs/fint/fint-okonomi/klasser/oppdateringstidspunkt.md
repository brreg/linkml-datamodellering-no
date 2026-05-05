

# Slot: oppdateringstidspunkt 


_Tidspunkt for siste endring i transaksjonen._





URI: [okn:oppdateringstidspunkt](https://schema.fintlabs.no/okonomi/oppdateringstidspunkt)
Alias: oppdateringstidspunkt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](datetime.md) |
| Domain Of | [Transaksjon](transaksjon.md) |
| Slot URI | [okn:oppdateringstidspunkt](https://schema.fintlabs.no/okonomi/oppdateringstidspunkt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Transaksjon](transaksjon.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




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
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:oppdateringstidspunkt
alias: oppdateringstidspunkt
owner: Transaksjon
domain_of:
- Transaksjon
range: datetime

```
</details>