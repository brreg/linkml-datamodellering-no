

# Slot: tilknyttetAv 


_Person som knytte dokumentet til registreringa._





URI: [ark:tilknyttetAv](https://schema.fintlabs.no/arkiv/tilknyttetAv)
Alias: tilknyttetAv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arkivressurs](arkivressurs.md) |
| Domain Of | [Dokumentbeskrivelse](dokumentbeskrivelse.md) |
| Slot URI | [ark:tilknyttetAv](https://schema.fintlabs.no/arkiv/tilknyttetAv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentbeskrivelse](dokumentbeskrivelse.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:tilknyttetAv |
| native | https://schema.fintlabs.no/arkiv/:tilknyttetAv |




## LinkML Source

<details>
```yaml
name: tilknyttetAv
description: Person som knytte dokumentet til registreringa.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:tilknyttetAv
alias: tilknyttetAv
owner: Dokumentbeskrivelse
domain_of:
- Dokumentbeskrivelse
range: Arkivressurs
required: true

```
</details>