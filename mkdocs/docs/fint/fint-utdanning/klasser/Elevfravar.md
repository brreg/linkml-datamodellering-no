

# Slot: elevfravar 


_Fråværsobjekt for elev._





URI: [utd:elevfravar](https://schema.fintlabs.no/utdanning/elevfravar)
Alias: elevfravar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fraversregistrering](fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  yes  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elevfravar](elevfravar.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Fraversregistrering](fraversregistrering.md) |
| Slot URI | [utd:elevfravar](https://schema.fintlabs.no/utdanning/elevfravar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:elevfravar |
| native | https://schema.fintlabs.no/utdanning/:elevfravar |




## LinkML Source

<details>
```yaml
name: elevfravar
description: Fråværsobjekt for elev.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:elevfravar
alias: elevfravar
domain_of:
- UtdanningContainer
- Elevforhold
- Fraversregistrering
range: Elevfravar

```
</details>