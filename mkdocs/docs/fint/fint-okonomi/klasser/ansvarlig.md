

# Slot: ansvarlig 


_Referanse til Personalressurs (Administrasjon) som er ansvarleg for å godkjenne transaksjonen._





URI: [okn:ansvarlig](https://schema.fintlabs.no/okonomi/ansvarlig)
Alias: ansvarlig

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Transaksjon](transaksjon.md) |
| Slot URI | [okn:ansvarlig](https://schema.fintlabs.no/okonomi/ansvarlig) |

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
| self | okn:ansvarlig |
| native | https://schema.fintlabs.no/okonomi/:ansvarlig |




## LinkML Source

<details>
```yaml
name: ansvarlig
description: Referanse til Personalressurs (Administrasjon) som er ansvarleg for å
  godkjenne transaksjonen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:ansvarlig
alias: ansvarlig
owner: Transaksjon
domain_of:
- Transaksjon
range: uriorcurie

```
</details>