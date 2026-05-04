

# Slot: forfallsDato 


_Frist for å svare på eit inngåande dokument._





URI: [ark:forfallsDato](https://schema.fintlabs.no/arkiv/forfallsDato)
Alias: forfallsDato

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
| Slot URI | [ark:forfallsDato](https://schema.fintlabs.no/arkiv/forfallsDato) |

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
| self | ark:forfallsDato |
| native | https://schema.fintlabs.no/arkiv/:forfallsDato |




## LinkML Source

<details>
```yaml
name: forfallsDato
description: Frist for å svare på eit inngåande dokument.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:forfallsDato
alias: forfallsDato
owner: Journalpost
domain_of:
- Journalpost
range: datetime

```
</details>