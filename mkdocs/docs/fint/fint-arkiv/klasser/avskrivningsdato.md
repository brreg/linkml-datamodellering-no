

# Slot: avskrivningsdato 


_Dato og klokkeslett for avskrivinga._





URI: [ark:avskrivningsdato](https://schema.fintlabs.no/arkiv/avskrivningsdato)
Alias: avskrivningsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Avskrivning](avskrivning.md) | Avskriving av ein journalpost (markering som ferdigbehandla) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](datetime.md) |
| Domain Of | [Avskrivning](avskrivning.md) |
| Slot URI | [ark:avskrivningsdato](https://schema.fintlabs.no/arkiv/avskrivningsdato) |

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
| self | ark:avskrivningsdato |
| native | https://schema.fintlabs.no/arkiv/:avskrivningsdato |




## LinkML Source

<details>
```yaml
name: avskrivningsdato
description: Dato og klokkeslett for avskrivinga.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:avskrivningsdato
alias: avskrivningsdato
owner: Avskrivning
domain_of:
- Avskrivning
range: datetime
required: true

```
</details>