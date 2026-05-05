

# Slot: parorende 


_Pårørande kontaktperson til personen._





URI: [fint:parorende](https://schema.fintlabs.no/parorende)
Alias: parorende

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktperson](kontaktperson.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [fint:parorende](https://schema.fintlabs.no/parorende) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Person](person.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:parorende |
| native | https://schema.fintlabs.no/okonomi/:parorende |




## LinkML Source

<details>
```yaml
name: parorende
description: Pårørande kontaktperson til personen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: fint:parorende
alias: parorende
owner: Person
domain_of:
- Person
range: Kontaktperson
multivalued: true

```
</details>