

# Slot: journalstatus 


_Status til journalposten._





URI: [ark:journalstatus](https://schema.fintlabs.no/arkiv/journalstatus)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [JournalStatus](journalstatus.md) |
| Domain Of | [Journalpost](journalpost.md) |
| Slot URI | [ark:journalstatus](https://schema.fintlabs.no/arkiv/journalstatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




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
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:journalstatus
domain_of:
- Journalpost
range: JournalStatus

```
</details>