

# Slot: person 


_Person som er ein personalressurs._





URI: [adm:person](https://schema.fintlabs.no/administrasjon/person)
Alias: person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](person.md) |
| Domain Of | [Personalressurs](personalressurs.md) |
| Slot URI | [adm:person](https://schema.fintlabs.no/administrasjon/person) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Personalressurs](personalressurs.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:person |
| native | https://schema.fintlabs.no/administrasjon/:person |




## LinkML Source

<details>
```yaml
name: person
description: Person som er ein personalressurs.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:person
alias: person
owner: Personalressurs
domain_of:
- Personalressurs
range: Person
required: true

```
</details>