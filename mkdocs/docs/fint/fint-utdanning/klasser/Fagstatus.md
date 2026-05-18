

# Slot: fagstatus 


_Fagstatus._





URI: [utd:fagstatus](https://schema.fintlabs.no/utdanning/fagstatus)
Alias: fagstatus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |
| [Faggruppemedlemskap](faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fagstatus](fagstatus.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Faggruppemedlemskap](faggruppemedlemskap.md) |
| Slot URI | [utd:fagstatus](https://schema.fintlabs.no/utdanning/fagstatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:fagstatus |
| native | https://schema.fintlabs.no/utdanning/:fagstatus |




## LinkML Source

<details>
```yaml
name: fagstatus
description: Fagstatus.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:fagstatus
alias: fagstatus
domain_of:
- UtdanningContainer
- Faggruppemedlemskap
range: Fagstatus

```
</details>