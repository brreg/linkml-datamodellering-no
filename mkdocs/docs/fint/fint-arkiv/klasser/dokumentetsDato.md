

# Slot: dokumentetsDato 


_Dato påført sjølve dokumentet._





URI: [ark:dokumentetsDato](https://schema.fintlabs.no/arkiv/dokumentetsDato)
Alias: dokumentetsDato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](datetime.md) |
| Domain Of | [Journalpost](journalpost.md) |
| Slot URI | [ark:dokumentetsDato](https://schema.fintlabs.no/arkiv/dokumentetsDato) |

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
| self | ark:dokumentetsDato |
| native | https://schema.fintlabs.no/arkiv/:dokumentetsDato |




## LinkML Source

<details>
```yaml
name: dokumentetsDato
description: Dato påført sjølve dokumentet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:dokumentetsDato
alias: dokumentetsDato
owner: Journalpost
domain_of:
- Journalpost
range: datetime

```
</details>