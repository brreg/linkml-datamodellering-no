

# Slot: kategori 


_Kategori for elevforholdet._





URI: [utd:kategori](https://schema.fintlabs.no/utdanning/kategori)
Alias: kategori

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elevkategori](elevkategori.md) |
| Domain Of | [Elevforhold](elevforhold.md) |
| Slot URI | [utd:kategori](https://schema.fintlabs.no/utdanning/kategori) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Elevforhold](elevforhold.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:kategori |
| native | https://schema.fintlabs.no/utdanning/:kategori |




## LinkML Source

<details>
```yaml
name: kategori
description: Kategori for elevforholdet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:kategori
alias: kategori
owner: Elevforhold
domain_of:
- Elevforhold
range: Elevkategori

```
</details>