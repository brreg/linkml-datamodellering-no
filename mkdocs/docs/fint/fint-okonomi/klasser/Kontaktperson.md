

# Slot: kontaktperson 


_Personar kontaktpersonen er pårørande for._





URI: [fint:kontaktpersonFor](https://schema.fintlabs.no/kontaktpersonFor)
Alias: kontaktperson

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](Person.md) |
| Domain Of | [Kontaktperson](Kontaktperson.md) |
| Slot URI | [fint:kontaktpersonFor](https://schema.fintlabs.no/kontaktpersonFor) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kontaktperson](Kontaktperson.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kontaktpersonFor |
| native | https://schema.fintlabs.no/okonomi/:kontaktperson |




## LinkML Source

<details>
```yaml
name: kontaktperson
description: Personar kontaktpersonen er pårørande for.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
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