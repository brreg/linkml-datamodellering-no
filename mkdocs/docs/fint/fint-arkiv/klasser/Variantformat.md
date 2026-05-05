

# Slot: variantFormat 


_Kva variant dokumentet førekjem i._





URI: [ark:variantFormat](https://schema.fintlabs.no/arkiv/variantFormat)
Alias: variantFormat

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentobjekt](dokumentobjekt.md) | Referanse til éin og berre éin dokumentfil |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Variantformat](variantformat.md) |
| Domain Of | [Dokumentobjekt](dokumentobjekt.md) |
| Slot URI | [ark:variantFormat](https://schema.fintlabs.no/arkiv/variantFormat) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentobjekt](dokumentobjekt.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:variantFormat |
| native | https://schema.fintlabs.no/arkiv/:variantFormat |




## LinkML Source

<details>
```yaml
name: variantFormat
description: Kva variant dokumentet førekjem i.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:variantFormat
alias: variantFormat
owner: Dokumentobjekt
domain_of:
- Dokumentobjekt
range: Variantformat
required: true

```
</details>