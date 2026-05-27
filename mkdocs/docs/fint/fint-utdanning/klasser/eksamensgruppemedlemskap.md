

# Slot: eksamensgruppemedlemskap 


_Eksamensgruppemedlemskap._





URI: [utd:eksamensgruppemedlemskap](https://schema.fintlabs.no/utdanning/eksamensgruppemedlemskap)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md) |
| Slot URI | [utd:eksamensgruppemedlemskap](https://schema.fintlabs.no/utdanning/eksamensgruppemedlemskap) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:eksamensgruppemedlemskap |
| native | https://schema.fintlabs.no/utdanning/:eksamensgruppemedlemskap |




## LinkML Source

<details>
```yaml
name: eksamensgruppemedlemskap
description: Eksamensgruppemedlemskap.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:eksamensgruppemedlemskap
domain_of:
- UtdanningContainer
- Elevforhold
range: Eksamensgruppemedlemskap
multivalued: true

```
</details>