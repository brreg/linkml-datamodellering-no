

# Slot: versjonsnummer 


_Identifikasjon av versjonar innanfor same dokument._





URI: [ark:versjonsnummer](https://schema.fintlabs.no/arkiv/versjonsnummer)
Alias: versjonsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentobjekt](dokumentobjekt.md) | Referanse til éin og berre éin dokumentfil |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](integer.md) |
| Domain Of | [Dokumentobjekt](dokumentobjekt.md) |
| Slot URI | [ark:versjonsnummer](https://schema.fintlabs.no/arkiv/versjonsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentobjekt](dokumentobjekt.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:versjonsnummer |
| native | https://schema.fintlabs.no/arkiv/:versjonsnummer |




## LinkML Source

<details>
```yaml
name: versjonsnummer
description: Identifikasjon av versjonar innanfor same dokument.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:versjonsnummer
alias: versjonsnummer
owner: Dokumentobjekt
domain_of:
- Dokumentobjekt
range: integer

```
</details>