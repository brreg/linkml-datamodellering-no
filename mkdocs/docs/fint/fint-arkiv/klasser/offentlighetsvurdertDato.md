

# Slot: offentlighetsvurdertDato 


_Datoen offentlegheitsvurdering vart gjennomført._





URI: [ark:offentlighetsvurdertDato](https://schema.fintlabs.no/arkiv/offentlighetsvurdertDato)
Alias: offentlighetsvurdertDato

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
| Slot URI | [ark:offentlighetsvurdertDato](https://schema.fintlabs.no/arkiv/offentlighetsvurdertDato) |

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
| self | ark:offentlighetsvurdertDato |
| native | https://schema.fintlabs.no/arkiv/:offentlighetsvurdertDato |




## LinkML Source

<details>
```yaml
name: offentlighetsvurdertDato
description: Datoen offentlegheitsvurdering vart gjennomført.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:offentlighetsvurdertDato
alias: offentlighetsvurdertDato
owner: Journalpost
domain_of:
- Journalpost
range: datetime

```
</details>