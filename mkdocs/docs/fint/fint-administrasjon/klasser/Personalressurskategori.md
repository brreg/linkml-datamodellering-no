

# Slot: personalressurskategori 


_Kategori for personalressursen._





URI: [adm:personalressurskategori](https://schema.fintlabs.no/administrasjon/personalressurskategori)
Alias: personalressurskategori

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](Personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personalressurskategori](Personalressurskategori.md) |
| Domain Of | [Personalressurs](Personalressurs.md) |
| Slot URI | [adm:personalressurskategori](https://schema.fintlabs.no/administrasjon/personalressurskategori) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Personalressurs](Personalressurs.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:personalressurskategori |
| native | https://schema.fintlabs.no/administrasjon/:personalressurskategori |




## LinkML Source

<details>
```yaml
name: personalressurskategori
description: Kategori for personalressursen.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:personalressurskategori
alias: personalressurskategori
owner: Personalressurs
domain_of:
- Personalressurs
range: Personalressurskategori
required: true

```
</details>