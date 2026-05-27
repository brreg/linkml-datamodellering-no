

# Slot: parorende 


_Pårørande kontaktperson til personen._





URI: [fint:parorende](https://schema.fintlabs.no/parorende)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  yes  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:parorende |
| native | https://schema.fintlabs.no/:parorende |




## LinkML Source

<details>
```yaml
name: parorende
description: Pårørande kontaktperson til personen.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:parorende
domain_of:
- Person
range: Kontaktperson
multivalued: true

```
</details>