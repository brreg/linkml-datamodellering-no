

# Slot: klasseId 


_Eintydig identifikasjon av klassen innanfor klassifikasjonssystemet._





URI: [ark:klasseId](https://schema.fintlabs.no/arkiv/klasseId)
Alias: klasseId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Klasse](klasse.md) | Ein klasse i eit klassifikasjonssystem |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Klasse](klasse.md) |
| Slot URI | [ark:klasseId](https://schema.fintlabs.no/arkiv/klasseId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Klasse](klasse.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:klasseId |
| native | https://schema.fintlabs.no/arkiv/:klasseId |




## LinkML Source

<details>
```yaml
name: klasseId
description: Eintydig identifikasjon av klassen innanfor klassifikasjonssystemet.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:klasseId
alias: klasseId
owner: Klasse
domain_of:
- Klasse
range: string
required: true

```
</details>