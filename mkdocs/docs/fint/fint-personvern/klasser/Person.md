

# Slot: person 


_Referanse til Person (Administrasjon) som har gjeve samtykke._





URI: [pvn:person](https://schema.fintlabs.no/personvern/person)
Alias: person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Samtykke](Samtykke.md) | Tillating til behandling av personopplysning |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Samtykke](Samtykke.md) |
| Slot URI | [pvn:person](https://schema.fintlabs.no/personvern/person) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Samtykke](Samtykke.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pvn:person |
| native | https://schema.fintlabs.no/personvern/:person |




## LinkML Source

<details>
```yaml
name: person
description: Referanse til Person (Administrasjon) som har gjeve samtykke.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:person
alias: person
owner: Samtykke
domain_of:
- Samtykke
range: uriorcurie
required: true

```
</details>