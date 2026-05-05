

# Slot: kategori 


_Kategori lønnsart._





URI: [adm:kategori](https://schema.fintlabs.no/administrasjon/kategori)
Alias: kategori

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Lonsart](lonsart.md) | Type ytelse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Lonsart](lonsart.md) |
| Slot URI | [adm:kategori](https://schema.fintlabs.no/administrasjon/kategori) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Lonsart](lonsart.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:kategori |
| native | https://schema.fintlabs.no/administrasjon/:kategori |




## LinkML Source

<details>
```yaml
name: kategori
description: Kategori lønnsart.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:kategori
alias: kategori
owner: Lonsart
domain_of:
- Lonsart
range: string

```
</details>