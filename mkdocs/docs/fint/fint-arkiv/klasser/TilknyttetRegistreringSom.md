

# Slot: tilknyttetRegistreringSom 


_Rolle dokumentet har i høve registreringa._





URI: [ark:tilknyttetRegistreringSom](https://schema.fintlabs.no/arkiv/tilknyttetRegistreringSom)
Alias: tilknyttetRegistreringSom

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TilknyttetRegistreringSom](tilknyttetregistreringsom.md) |
| Domain Of | [Dokumentbeskrivelse](dokumentbeskrivelse.md) |
| Slot URI | [ark:tilknyttetRegistreringSom](https://schema.fintlabs.no/arkiv/tilknyttetRegistreringSom) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
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
| self | ark:tilknyttetRegistreringSom |
| native | https://schema.fintlabs.no/arkiv/:tilknyttetRegistreringSom |




## LinkML Source

<details>
```yaml
name: tilknyttetRegistreringSom
description: Rolle dokumentet har i høve registreringa.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:tilknyttetRegistreringSom
alias: tilknyttetRegistreringSom
owner: Dokumentbeskrivelse
domain_of:
- Dokumentbeskrivelse
range: TilknyttetRegistreringSom
required: true
multivalued: true

```
</details>