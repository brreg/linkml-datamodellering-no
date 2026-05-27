

# Slot: klassemedlemskap 


_Klassemedlemskap._





URI: [utd:klassemedlemskap](https://schema.fintlabs.no/utdanning/klassemedlemskap)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Klassemedlemskap](klassemedlemskap.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Klasse](klasse.md) |
| Slot URI | [utd:klassemedlemskap](https://schema.fintlabs.no/utdanning/klassemedlemskap) |

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
| self | utd:klassemedlemskap |
| native | https://schema.fintlabs.no/utdanning/:klassemedlemskap |




## LinkML Source

<details>
```yaml
name: klassemedlemskap
description: Klassemedlemskap.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:klassemedlemskap
domain_of:
- UtdanningContainer
- Elevforhold
- Klasse
range: Klassemedlemskap
multivalued: true

```
</details>