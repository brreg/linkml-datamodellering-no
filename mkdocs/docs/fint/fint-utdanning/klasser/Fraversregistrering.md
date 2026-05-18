

# Slot: fraversregistrering 


_Fråversregistreringar._





URI: [utd:fraversregistrering](https://schema.fintlabs.no/utdanning/fraversregistrering)
Alias: fraversregistrering

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |
| [Elevfravar](elevfravar.md) | Fråværsregistreringar for ein elev knytt til eit elevforhold |  yes  |






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


* from schema: https://data.norge.no/linkml/fint-utdanning




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
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:fraversregistrering
alias: fraversregistrering
domain_of:
- UtdanningContainer
- Elevfravar
range: Fraversregistrering
multivalued: true

```
</details>