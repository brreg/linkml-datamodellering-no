

# Slot: faggruppemedlemskap 


_Faggruppemedlemskap._





URI: [utd:faggruppemedlemskap](https://schema.fintlabs.no/utdanning/faggruppemedlemskap)
Alias: faggruppemedlemskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  yes  |
| [Faggruppe](faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  yes  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Faggruppemedlemskap](faggruppemedlemskap.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Varsel](varsel.md), [Faggruppe](faggruppe.md) |
| Slot URI | [utd:faggruppemedlemskap](https://schema.fintlabs.no/utdanning/faggruppemedlemskap) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:faggruppemedlemskap |
| native | https://schema.fintlabs.no/utdanning/:faggruppemedlemskap |




## LinkML Source

<details>
```yaml
name: faggruppemedlemskap
description: Faggruppemedlemskap.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:faggruppemedlemskap
alias: faggruppemedlemskap
domain_of:
- UtdanningContainer
- Elevforhold
- Varsel
- Faggruppe
range: Faggruppemedlemskap
multivalued: true

```
</details>