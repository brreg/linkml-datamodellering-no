

# Slot: fraversregistreringer 


_Fråværsregistreringar knytt til elevforholdet._





URI: [utd:fraversregistreringer](https://schema.fintlabs.no/utdanning/fraversregistreringer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elevfravar](elevfravar.md) |
| Domain Of | [Elevforhold](elevforhold.md) |
| Slot URI | [utd:fraversregistreringer](https://schema.fintlabs.no/utdanning/fraversregistreringer) |

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
| self | utd:fraversregistreringer |
| native | https://schema.fintlabs.no/utdanning/:fraversregistreringer |




## LinkML Source

<details>
```yaml
name: fraversregistreringer
description: Fråværsregistreringar knytt til elevforholdet.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:fraversregistreringer
domain_of:
- Elevforhold
range: Elevfravar
multivalued: true

```
</details>