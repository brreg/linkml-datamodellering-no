

# Slot: dokumentobjekt 


_Dokumentobjekt tilhøyrande dokumentbeskrivelsa._





URI: [ark:dokumentobjekt](https://schema.fintlabs.no/arkiv/dokumentobjekt)
Alias: dokumentobjekt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Dokumentobjekt](dokumentobjekt.md) |
| Domain Of | [Dokumentbeskrivelse](dokumentbeskrivelse.md) |
| Slot URI | [ark:dokumentobjekt](https://schema.fintlabs.no/arkiv/dokumentobjekt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentbeskrivelse](dokumentbeskrivelse.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:dokumentobjekt |
| native | https://schema.fintlabs.no/arkiv/:dokumentobjekt |




## LinkML Source

<details>
```yaml
name: dokumentobjekt
description: Dokumentobjekt tilhøyrande dokumentbeskrivelsa.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:dokumentobjekt
alias: dokumentobjekt
owner: Dokumentbeskrivelse
domain_of:
- Dokumentbeskrivelse
range: Dokumentobjekt
multivalued: true
inlined: true
inlined_as_list: true

```
</details>