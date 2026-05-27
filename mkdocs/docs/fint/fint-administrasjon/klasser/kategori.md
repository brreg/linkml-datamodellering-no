

# Slot: kategori 


_Kategori lønnsart._





URI: [adm:kategori](https://schema.fintlabs.no/administrasjon/kategori)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Lonsart](lonsart.md) | Type ytelse |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Lonsart](lonsart.md) |
| Slot URI | [adm:kategori](https://schema.fintlabs.no/administrasjon/kategori) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




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
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:kategori
domain_of:
- Lonsart
range: string

```
</details>