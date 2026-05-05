

# Slot: avskrivningsmate 


_Korleis journalposten er avskriven._





URI: [ark:avskrivningsmate](https://schema.fintlabs.no/arkiv/avskrivningsmate)
Alias: avskrivningsmate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Avskrivning](avskrivning.md) | Avskriving av ein journalpost (markering som ferdigbehandla) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Avskrivning](avskrivning.md) |
| Slot URI | [ark:avskrivningsmate](https://schema.fintlabs.no/arkiv/avskrivningsmate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Avskrivning](avskrivning.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:avskrivningsmate |
| native | https://schema.fintlabs.no/arkiv/:avskrivningsmate |




## LinkML Source

<details>
```yaml
name: avskrivningsmate
description: Korleis journalposten er avskriven.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:avskrivningsmate
alias: avskrivningsmate
owner: Avskrivning
domain_of:
- Avskrivning
range: string
required: true

```
</details>