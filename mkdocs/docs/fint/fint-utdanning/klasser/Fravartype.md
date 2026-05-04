

# Slot: fravartype 


_Type fråvær._





URI: [utd:fravartype](https://schema.fintlabs.no/utdanning/fravartype)
Alias: fravartype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fraversregistrering](Fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fravartype](Fravartype.md) |
| Domain Of | [Fraversregistrering](Fraversregistrering.md) |
| Slot URI | [utd:fravartype](https://schema.fintlabs.no/utdanning/fravartype) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fraversregistrering](Fraversregistrering.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:fravartype |
| native | https://schema.fintlabs.no/utdanning/:fravartype |




## LinkML Source

<details>
```yaml
name: fravartype
description: Type fråvær.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:fravartype
alias: fravartype
owner: Fraversregistrering
domain_of:
- Fraversregistrering
range: Fravartype
required: true

```
</details>