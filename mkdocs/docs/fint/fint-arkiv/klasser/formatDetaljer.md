

# Slot: formatDetaljer 


_Nærare spesifikasjon av dokumentets format._





URI: [ark:formatDetaljer](https://schema.fintlabs.no/arkiv/formatDetaljer)
Alias: formatDetaljer

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
| Slot URI | [ark:formatDetaljer](https://schema.fintlabs.no/arkiv/formatDetaljer) |

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
| self | ark:formatDetaljer |
| native | https://schema.fintlabs.no/arkiv/:formatDetaljer |




## LinkML Source

<details>
```yaml
name: formatDetaljer
description: Nærare spesifikasjon av dokumentets format.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:formatDetaljer
alias: formatDetaljer
owner: Dokumentobjekt
domain_of:
- Dokumentobjekt
range: string

```
</details>