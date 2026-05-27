

# Slot: kategori 


_Kategori for elevforholdet._





URI: [utd:kategori](https://schema.fintlabs.no/utdanning/kategori)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




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
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:kategori
domain_of:
- Elevforhold
range: Elevkategori

```
</details>