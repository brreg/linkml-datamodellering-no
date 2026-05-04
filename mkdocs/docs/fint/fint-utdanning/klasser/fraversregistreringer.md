

# Slot: fraversregistreringer 


_Fråværsregistreringar knytt til elevforholdet._





URI: [utd:fraversregistreringer](https://schema.fintlabs.no/utdanning/fraversregistreringer)
Alias: fraversregistreringer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevforhold](Elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elevfravar](Elevfravar.md) |
| Domain Of | [Elevforhold](Elevforhold.md) |
| Slot URI | [utd:fraversregistreringer](https://schema.fintlabs.no/utdanning/fraversregistreringer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Elevforhold](Elevforhold.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




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
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:fraversregistreringer
alias: fraversregistreringer
owner: Elevforhold
domain_of:
- Elevforhold
range: Elevfravar
multivalued: true

```
</details>