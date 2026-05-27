

# Slot: programomrademedlemskap 


_Programområdemedlemskap._





URI: [utd:programomrademedlemskap](https://schema.fintlabs.no/utdanning/programomrademedlemskap)
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
| Range | [Programomrademedlemskap](programomrademedlemskap.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md) |
| Slot URI | [utd:programomrademedlemskap](https://schema.fintlabs.no/utdanning/programomrademedlemskap) |

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
| self | utd:programomrademedlemskap |
| native | https://schema.fintlabs.no/utdanning/:programomrademedlemskap |




## LinkML Source

<details>
```yaml
name: programomrademedlemskap
description: Programområdemedlemskap.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:programomrademedlemskap
domain_of:
- UtdanningContainer
- Elevforhold
range: Programomrademedlemskap
multivalued: true

```
</details>