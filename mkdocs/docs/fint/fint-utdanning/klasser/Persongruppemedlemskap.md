

# Slot: persongruppemedlemskap 


_Persongruppemedlemskap._





URI: [utd:persongruppemedlemskap](https://schema.fintlabs.no/utdanning/persongruppemedlemskap)
Alias: persongruppemedlemskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  yes  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Persongruppemedlemskap](persongruppemedlemskap.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Persongruppe](persongruppe.md) |
| Slot URI | [utd:persongruppemedlemskap](https://schema.fintlabs.no/utdanning/persongruppemedlemskap) |

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
| self | utd:persongruppemedlemskap |
| native | https://schema.fintlabs.no/utdanning/:persongruppemedlemskap |




## LinkML Source

<details>
```yaml
name: persongruppemedlemskap
description: Persongruppemedlemskap.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:persongruppemedlemskap
alias: persongruppemedlemskap
domain_of:
- UtdanningContainer
- Elevforhold
- Persongruppe
range: Persongruppemedlemskap
multivalued: true

```
</details>