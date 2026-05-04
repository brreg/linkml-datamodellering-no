

# Slot: dokumentnummer 


_Identifikasjon av dokumenta innanfor ei registrering._





URI: [ark:dokumentnummer](https://schema.fintlabs.no/arkiv/dokumentnummer)
Alias: dokumentnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentbeskrivelse](Dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Dokumentbeskrivelse](Dokumentbeskrivelse.md) |
| Slot URI | [ark:dokumentnummer](https://schema.fintlabs.no/arkiv/dokumentnummer) |

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
| self | ark:dokumentnummer |
| native | https://schema.fintlabs.no/arkiv/:dokumentnummer |




## LinkML Source

<details>
```yaml
name: dokumentnummer
description: Identifikasjon av dokumenta innanfor ei registrering.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:dokumentnummer
alias: dokumentnummer
owner: Dokumentbeskrivelse
domain_of:
- Dokumentbeskrivelse
range: integer

```
</details>