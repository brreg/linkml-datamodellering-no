

# Slot: kontaktperson 


_Personar kontaktpersonen er pårørande for._





URI: [fint:kontaktpersonFor](https://schema.fintlabs.no/kontaktpersonFor)
Alias: kontaktperson

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](person.md) |
| Domain Of | [Kontaktperson](kontaktperson.md) |
| Slot URI | [fint:kontaktpersonFor](https://schema.fintlabs.no/kontaktpersonFor) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kontaktperson](kontaktperson.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kontaktpersonFor |
| native | https://schema.fintlabs.no/personvern/:kontaktperson |




## LinkML Source

<details>
```yaml
name: kontaktperson
description: Personar kontaktpersonen er pårørande for.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: fint:kontaktpersonFor
alias: kontaktperson
owner: Kontaktperson
domain_of:
- Kontaktperson
range: Person
multivalued: true

```
</details>