

# Slot: tilknyttetDato 


_Datoen eit dokument vart knytt til ei registrering._





URI: [ark:tilknyttetDato](https://schema.fintlabs.no/arkiv/tilknyttetDato)
Alias: tilknyttetDato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentbeskrivelse](Dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Dokumentbeskrivelse](Dokumentbeskrivelse.md) |
| Slot URI | [ark:tilknyttetDato](https://schema.fintlabs.no/arkiv/tilknyttetDato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentbeskrivelse](Dokumentbeskrivelse.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:tilknyttetDato |
| native | https://schema.fintlabs.no/arkiv/:tilknyttetDato |




## LinkML Source

<details>
```yaml
name: tilknyttetDato
description: Datoen eit dokument vart knytt til ei registrering.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:tilknyttetDato
alias: tilknyttetDato
owner: Dokumentbeskrivelse
domain_of:
- Dokumentbeskrivelse
range: datetime

```
</details>