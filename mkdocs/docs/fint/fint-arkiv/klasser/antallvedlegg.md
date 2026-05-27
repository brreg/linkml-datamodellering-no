

# Slot: antallVedlegg 


_Antal fysiske vedlegg til eit fysisk hoveddokument._





URI: [ark:antallVedlegg](https://schema.fintlabs.no/arkiv/antallVedlegg)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Journalpost](journalpost.md) |
| Slot URI | [ark:antallVedlegg](https://schema.fintlabs.no/arkiv/antallVedlegg) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




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
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:antallVedlegg
domain_of:
- Journalpost
range: integer

```
</details>