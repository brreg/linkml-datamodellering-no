

# Slot: antallVedlegg 


_Antal fysiske vedlegg til eit fysisk hoveddokument._





URI: [ark:antallVedlegg](https://schema.fintlabs.no/arkiv/antallVedlegg)
Alias: antallVedlegg

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](integer.md) |
| Domain Of | [Journalpost](journalpost.md) |
| Slot URI | [ark:antallVedlegg](https://schema.fintlabs.no/arkiv/antallVedlegg) |

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
| self | ark:antallVedlegg |
| native | https://schema.fintlabs.no/arkiv/:antallVedlegg |




## LinkML Source

<details>
```yaml
name: antallVedlegg
description: Antal fysiske vedlegg til eit fysisk hoveddokument.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:antallVedlegg
alias: antallVedlegg
owner: Journalpost
domain_of:
- Journalpost
range: integer

```
</details>