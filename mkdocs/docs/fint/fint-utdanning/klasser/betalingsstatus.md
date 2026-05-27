

# Slot: betalingsstatus 


_Betalingsstatus._





URI: [utd:betalingsstatus](https://schema.fintlabs.no/utdanning/betalingsstatus)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Betalingsstatus](betalingsstatus.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) |
| Slot URI | [utd:betalingsstatus](https://schema.fintlabs.no/utdanning/betalingsstatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:betalingsstatus |
| native | https://schema.fintlabs.no/utdanning/:betalingsstatus |




## LinkML Source

<details>
```yaml
name: betalingsstatus
description: Betalingsstatus.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:betalingsstatus
domain_of:
- UtdanningContainer
- Eksamensgruppemedlemskap
range: Betalingsstatus

```
</details>