

# Slot: sjekksum 


_Verdi som gir integritetssikring til dokumentets innhald._





URI: [ark:sjekksum](https://schema.fintlabs.no/arkiv/sjekksum)
Alias: sjekksum

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentobjekt](Dokumentobjekt.md) | Referanse til éin og berre éin dokumentfil |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Dokumentobjekt](Dokumentobjekt.md) |
| Slot URI | [ark:sjekksum](https://schema.fintlabs.no/arkiv/sjekksum) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentobjekt](Dokumentobjekt.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:sjekksum |
| native | https://schema.fintlabs.no/arkiv/:sjekksum |




## LinkML Source

<details>
```yaml
name: sjekksum
description: Verdi som gir integritetssikring til dokumentets innhald.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:sjekksum
alias: sjekksum
owner: Dokumentobjekt
domain_of:
- Dokumentobjekt
range: string

```
</details>