

# Slot: varsel 


_Varsel._





URI: [utd:varsel](https://schema.fintlabs.no/utdanning/varsel)
Alias: varsel

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
| Range | [Varsel](varsel.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Faggruppemedlemskap](faggruppemedlemskap.md) |
| Slot URI | [utd:varsel](https://schema.fintlabs.no/utdanning/varsel) |

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
| self | utd:varsel |
| native | https://schema.fintlabs.no/utdanning/:varsel |




## LinkML Source

<details>
```yaml
name: varsel
description: Varsel.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:varsel
alias: varsel
domain_of:
- UtdanningContainer
- Faggruppemedlemskap
range: Varsel
multivalued: true

```
</details>