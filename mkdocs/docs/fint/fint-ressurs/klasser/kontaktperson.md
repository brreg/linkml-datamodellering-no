

# Slot: kontaktperson 


_Personar kontaktpersonen er pårørande for._





URI: [fint:kontaktpersonFor](https://schema.fintlabs.no/kontaktpersonFor)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  yes  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kontaktpersonFor |
| native | https://schema.fintlabs.no/:kontaktperson |




## LinkML Source

<details>
```yaml
name: kontaktperson
description: Personar kontaktpersonen er pårørande for.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:kontaktpersonFor
domain_of:
- Kontaktperson
range: Person
multivalued: true

```
</details>