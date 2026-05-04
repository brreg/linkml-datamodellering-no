

# Slot: journalDato 


_Datoen journalposten er oppretta/arkivert._





URI: [ark:journalDato](https://schema.fintlabs.no/arkiv/journalDato)
Alias: journalDato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Journalpost](Journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Journalpost](Journalpost.md) |
| Slot URI | [ark:journalDato](https://schema.fintlabs.no/arkiv/journalDato) |

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
| self | ark:journalDato |
| native | https://schema.fintlabs.no/arkiv/:journalDato |




## LinkML Source

<details>
```yaml
name: journalDato
description: Datoen journalposten er oppretta/arkivert.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:journalDato
alias: journalDato
owner: Journalpost
domain_of:
- Journalpost
range: datetime

```
</details>