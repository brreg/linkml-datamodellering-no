

# Slot: type 


_Beskriv kva slags type kontaktperson._





URI: [fint:type](https://schema.fintlabs.no/type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Kontaktperson](kontaktperson.md) |
| Slot URI | [fint:type](https://schema.fintlabs.no/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kontaktperson](kontaktperson.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:type |
| native | https://schema.fintlabs.no/administrasjon/:type |




## LinkML Source

<details>
```yaml
name: type
description: Beskriv kva slags type kontaktperson.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: fint:type
alias: type
owner: Kontaktperson
domain_of:
- Kontaktperson
range: string
required: true

```
</details>