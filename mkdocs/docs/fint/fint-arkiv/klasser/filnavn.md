

# Slot: filnavn 


_Dokumentfilens namn._





URI: [ark:filnavn](https://schema.fintlabs.no/arkiv/filnavn)
Alias: filnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentfil](dokumentfil.md) | Sjølve dokumentfila med data og metadata |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Dokumentfil](dokumentfil.md) |
| Slot URI | [ark:filnavn](https://schema.fintlabs.no/arkiv/filnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:filnavn |
| native | https://schema.fintlabs.no/arkiv/:filnavn |




## LinkML Source

<details>
```yaml
name: filnavn
description: Dokumentfilens namn.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:filnavn
alias: filnavn
domain_of:
- Dokumentfil
range: string

```
</details>