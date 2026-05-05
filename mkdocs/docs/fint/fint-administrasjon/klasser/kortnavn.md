

# Slot: kortnavn 


_Forkorta namn som beskriv organisasjonselementet._





URI: [adm:kortnavn](https://schema.fintlabs.no/administrasjon/kortnavn)
Alias: kortnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Organisasjonselement](organisasjonselement.md) |
| Slot URI | [adm:kortnavn](https://schema.fintlabs.no/administrasjon/kortnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Organisasjonselement](organisasjonselement.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:kortnavn |
| native | https://schema.fintlabs.no/administrasjon/:kortnavn |




## LinkML Source

<details>
```yaml
name: kortnavn
description: Forkorta namn som beskriv organisasjonselementet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:kortnavn
alias: kortnavn
owner: Organisasjonselement
domain_of:
- Organisasjonselement
range: string

```
</details>