

# Slot: sendtDato 


_Dato eit internt produsert dokument vart sendt/ekspedert._





URI: [ark:sendtDato](https://schema.fintlabs.no/arkiv/sendtDato)
Alias: sendtDato

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
| Slot URI | [ark:sendtDato](https://schema.fintlabs.no/arkiv/sendtDato) |

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