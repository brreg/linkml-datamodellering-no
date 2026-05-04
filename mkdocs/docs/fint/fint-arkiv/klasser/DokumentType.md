

# Slot: dokumentType 


_Namn på type dokument._





URI: [ark:dokumentType](https://schema.fintlabs.no/arkiv/dokumentType)
Alias: dokumentType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentbeskrivelse](Dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DokumentType](DokumentType.md) |
| Domain Of | [Dokumentbeskrivelse](Dokumentbeskrivelse.md) |
| Slot URI | [ark:dokumentType](https://schema.fintlabs.no/arkiv/dokumentType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentbeskrivelse](Dokumentbeskrivelse.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:dokumentType |
| native | https://schema.fintlabs.no/arkiv/:dokumentType |




## LinkML Source

<details>
```yaml
name: dokumentType
description: Namn på type dokument.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:dokumentType
alias: dokumentType
owner: Dokumentbeskrivelse
domain_of:
- Dokumentbeskrivelse
range: DokumentType
required: true

```
</details>