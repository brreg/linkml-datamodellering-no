

# Slot: avskrevetAv 


_Person som avskriva journalposten._





URI: [ark:avskrevetAv](https://schema.fintlabs.no/arkiv/avskrevetAv)
Alias: avskrevetAv

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
| Slot URI | [ark:avskrevetAv](https://schema.fintlabs.no/arkiv/avskrevetAv) |

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
| self | ark:avskrevetAv |
| native | https://schema.fintlabs.no/arkiv/:avskrevetAv |




## LinkML Source

<details>
```yaml
name: avskrevetAv
description: Person som avskriva journalposten.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:avskrevetAv
alias: avskrevetAv
owner: Avskrivning
domain_of:
- Avskrivning
range: string
required: true

```
</details>