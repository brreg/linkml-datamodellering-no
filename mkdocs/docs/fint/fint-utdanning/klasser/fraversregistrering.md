

# Slot: fraversregistrering 


_Fråversregistreringar._





URI: [utd:fraversregistrering](https://schema.fintlabs.no/utdanning/fraversregistrering)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevfravar](elevfravar.md) | Fråværsregistreringar for ein elev knytt til eit elevforhold |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fraversregistrering](fraversregistrering.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevfravar](elevfravar.md) |
| Slot URI | [utd:fraversregistrering](https://schema.fintlabs.no/utdanning/fraversregistrering) |

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
| self | utd:fraversregistrering |
| native | https://schema.fintlabs.no/utdanning/:fraversregistrering |




## LinkML Source

<details>
```yaml
name: fraversregistrering
description: Fråversregistreringar.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:fraversregistrering
domain_of:
- UtdanningContainer
- Elevfravar
range: Fraversregistrering
multivalued: true

```
</details>