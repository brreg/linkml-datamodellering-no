

# Slot: forersPaaVitnemaal 


_Angir om fråværet vert ført på vitnemålet._





URI: [utd:forersPaaVitnemaal](https://schema.fintlabs.no/utdanning/forersPaaVitnemaal)
Alias: forersPaaVitnemaal

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fraversregistrering](fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](boolean.md) |
| Domain Of | [Fraversregistrering](fraversregistrering.md) |
| Slot URI | [utd:forersPaaVitnemaal](https://schema.fintlabs.no/utdanning/forersPaaVitnemaal) |

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
| self | utd:forersPaaVitnemaal |
| native | https://schema.fintlabs.no/utdanning/:forersPaaVitnemaal |




## LinkML Source

<details>
```yaml
name: forersPaaVitnemaal
description: Angir om fråværet vert ført på vitnemålet.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:forersPaaVitnemaal
alias: forersPaaVitnemaal
owner: Fraversregistrering
domain_of:
- Fraversregistrering
range: boolean
required: true

```
</details>