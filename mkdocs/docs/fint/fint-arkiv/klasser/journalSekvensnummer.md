

# Slot: journalSekvensnummer 


_Rekkjefølgja journalposten vart oppretta under året._





URI: [ark:journalSekvensnummer](https://schema.fintlabs.no/arkiv/journalSekvensnummer)
Alias: journalSekvensnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Journalpost](Journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Journalpost](Journalpost.md) |
| Slot URI | [ark:journalSekvensnummer](https://schema.fintlabs.no/arkiv/journalSekvensnummer) |

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
| self | ark:journalSekvensnummer |
| native | https://schema.fintlabs.no/arkiv/:journalSekvensnummer |




## LinkML Source

<details>
```yaml
name: journalSekvensnummer
description: Rekkjefølgja journalposten vart oppretta under året.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:journalSekvensnummer
alias: journalSekvensnummer
owner: Journalpost
domain_of:
- Journalpost
range: integer

```
</details>