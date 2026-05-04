

# Slot: mottattDato 


_Dato eit eksternt dokument vart motteke._





URI: [ark:mottattDato](https://schema.fintlabs.no/arkiv/mottattDato)
Alias: mottattDato

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
| Slot URI | [ark:mottattDato](https://schema.fintlabs.no/arkiv/mottattDato) |

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
| self | ark:mottattDato |
| native | https://schema.fintlabs.no/arkiv/:mottattDato |




## LinkML Source

<details>
```yaml
name: mottattDato
description: Dato eit eksternt dokument vart motteke.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:mottattDato
alias: mottattDato
owner: Journalpost
domain_of:
- Journalpost
range: datetime

```
</details>