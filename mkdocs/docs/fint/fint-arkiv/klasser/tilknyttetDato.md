

# Slot: tilknyttetDato 


_Datoen eit dokument vart knytt til ei registrering._





URI: [ark:tilknyttetDato](https://schema.fintlabs.no/arkiv/tilknyttetDato)
Alias: tilknyttetDato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](datetime.md) |
| Domain Of | [Dokumentbeskrivelse](dokumentbeskrivelse.md) |
| Slot URI | [ark:tilknyttetDato](https://schema.fintlabs.no/arkiv/tilknyttetDato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentbeskrivelse](dokumentbeskrivelse.md) |








## In Subsets


* [Valgfri](valgfri.md)






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