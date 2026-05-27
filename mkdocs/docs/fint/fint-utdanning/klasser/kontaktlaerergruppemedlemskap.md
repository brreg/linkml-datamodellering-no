

# Slot: kontaktlaerergruppemedlemskap 


_Kontaktlærergruppemedlemskap._





URI: [utd:kontaktlaerergruppemedlemskap](https://schema.fintlabs.no/utdanning/kontaktlaerergruppemedlemskap)
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
| Range | [Kontaktlaerergruppemedlemskap](kontaktlaerergruppemedlemskap.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md) |
| Slot URI | [utd:kontaktlaerergruppemedlemskap](https://schema.fintlabs.no/utdanning/kontaktlaerergruppemedlemskap) |

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
| self | utd:kontaktlaerergruppemedlemskap |
| native | https://schema.fintlabs.no/utdanning/:kontaktlaerergruppemedlemskap |




## LinkML Source

<details>
```yaml
name: kontaktlaerergruppemedlemskap
description: Kontaktlærergruppemedlemskap.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:kontaktlaerergruppemedlemskap
domain_of:
- UtdanningContainer
- Elevforhold
range: Kontaktlaerergruppemedlemskap
multivalued: true

```
</details>