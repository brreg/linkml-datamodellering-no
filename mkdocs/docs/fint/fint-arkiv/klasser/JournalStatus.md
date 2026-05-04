

# Slot: journalstatus 


_Status til journalposten._





URI: [ark:journalstatus](https://schema.fintlabs.no/arkiv/journalstatus)
Alias: journalstatus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Journalpost](Journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [JournalStatus](JournalStatus.md) |
| Domain Of | [Journalpost](Journalpost.md) |
| Slot URI | [ark:journalstatus](https://schema.fintlabs.no/arkiv/journalstatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Journalpost](Journalpost.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:journalstatus |
| native | https://schema.fintlabs.no/arkiv/:journalstatus |




## LinkML Source

<details>
```yaml
name: journalstatus
description: Status til journalposten.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:journalstatus
alias: journalstatus
owner: Journalpost
domain_of:
- Journalpost
range: JournalStatus
required: true

```
</details>