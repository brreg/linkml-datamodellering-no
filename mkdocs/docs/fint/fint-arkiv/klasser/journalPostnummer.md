

# Slot: journalPostnummer 


_Rekkjefølgja journalpostane vart oppretta innanfor saksmappa._





URI: [ark:journalPostnummer](https://schema.fintlabs.no/arkiv/journalPostnummer)
Alias: journalPostnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](integer.md) |
| Domain Of | [Journalpost](journalpost.md) |
| Slot URI | [ark:journalPostnummer](https://schema.fintlabs.no/arkiv/journalPostnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Journalpost](journalpost.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:journalPostnummer |
| native | https://schema.fintlabs.no/arkiv/:journalPostnummer |




## LinkML Source

<details>
```yaml
name: journalPostnummer
description: Rekkjefølgja journalpostane vart oppretta innanfor saksmappa.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:journalPostnummer
alias: journalPostnummer
owner: Journalpost
domain_of:
- Journalpost
range: integer

```
</details>