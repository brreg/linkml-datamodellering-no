

# Slot: posteringsId 


_Intern unik identifikator i økonomisystemet._





URI: [okn:posteringsId](https://schema.fintlabs.no/okonomi/posteringsId)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Postering](postering.md) | Føring på ein konto i rekneskapet |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Postering](postering.md) |
| Slot URI | [okn:posteringsId](https://schema.fintlabs.no/okonomi/posteringsId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:posteringsId |
| native | https://schema.fintlabs.no/okonomi/:posteringsId |




## LinkML Source

<details>
```yaml
name: posteringsId
description: Intern unik identifikator i økonomisystemet.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:posteringsId
domain_of:
- Postering
range: Identifikator
inlined: true

```
</details>