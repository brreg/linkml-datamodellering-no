

# Slot: undervisningsgruppemedlemskap 


_Undervisningsgruppemedlemskap._





URI: [utd:undervisningsgruppemedlemskap](https://schema.fintlabs.no/utdanning/undervisningsgruppemedlemskap)
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
| Range | [Undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md) |
| Slot URI | [utd:undervisningsgruppemedlemskap](https://schema.fintlabs.no/utdanning/undervisningsgruppemedlemskap) |

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
| self | utd:undervisningsgruppemedlemskap |
| native | https://schema.fintlabs.no/utdanning/:undervisningsgruppemedlemskap |




## LinkML Source

<details>
```yaml
name: undervisningsgruppemedlemskap
description: Undervisningsgruppemedlemskap.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:undervisningsgruppemedlemskap
domain_of:
- UtdanningContainer
- Elevforhold
range: Undervisningsgruppemedlemskap
multivalued: true

```
</details>