

# Slot: journalposttype 


_Namn på type journalpost._





URI: [ark:journalposttype](https://schema.fintlabs.no/arkiv/journalposttype)
Alias: journalposttype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [JournalpostType](journalposttype.md) |
| Domain Of | [Journalpost](journalpost.md) |
| Slot URI | [ark:journalposttype](https://schema.fintlabs.no/arkiv/journalposttype) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Journalpost](journalpost.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:journalposttype |
| native | https://schema.fintlabs.no/arkiv/:journalposttype |




## LinkML Source

<details>
```yaml
name: journalposttype
description: Namn på type journalpost.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:journalposttype
alias: journalposttype
owner: Journalpost
domain_of:
- Journalpost
range: JournalpostType
required: true

```
</details>