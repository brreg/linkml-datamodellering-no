

# Slot: periode 


_Perioden fråværet varte._





URI: [utd:periode](https://schema.fintlabs.no/utdanning/periode)
Alias: periode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fraversregistrering](fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Periode](periode.md) |
| Domain Of | [Fraversregistrering](fraversregistrering.md) |
| Slot URI | [utd:periode](https://schema.fintlabs.no/utdanning/periode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fraversregistrering](fraversregistrering.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:periode |
| native | https://schema.fintlabs.no/utdanning/:periode |




## LinkML Source

<details>
```yaml
name: periode
description: Perioden fråværet varte.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:periode
alias: periode
owner: Fraversregistrering
domain_of:
- Fraversregistrering
range: Periode
required: true
inlined: true

```
</details>