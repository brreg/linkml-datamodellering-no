

# Slot: journalAr 


_Året journalposten vart oppretta._





URI: [ark:journalAr](https://schema.fintlabs.no/arkiv/journalAr)
Alias: journalAr

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Journalpost](Journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Journalpost](Journalpost.md) |
| Slot URI | [ark:journalAr](https://schema.fintlabs.no/arkiv/journalAr) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Journalpost](Journalpost.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:journalAr |
| native | https://schema.fintlabs.no/arkiv/:journalAr |




## LinkML Source

<details>
```yaml
name: journalAr
description: Året journalposten vart oppretta.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:journalAr
alias: journalAr
owner: Journalpost
domain_of:
- Journalpost
range: string

```
</details>