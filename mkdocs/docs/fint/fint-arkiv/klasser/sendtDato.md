

# Slot: sendtDato 


_Dato eit internt produsert dokument vart sendt/ekspedert._





URI: [ark:sendtDato](https://schema.fintlabs.no/arkiv/sendtDato)
Alias: sendtDato

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
| Slot URI | [ark:sendtDato](https://schema.fintlabs.no/arkiv/sendtDato) |

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
| self | ark:sendtDato |
| native | https://schema.fintlabs.no/arkiv/:sendtDato |




## LinkML Source

<details>
```yaml
name: sendtDato
description: Dato eit internt produsert dokument vart sendt/ekspedert.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:sendtDato
alias: sendtDato
owner: Journalpost
domain_of:
- Journalpost
range: datetime

```
</details>