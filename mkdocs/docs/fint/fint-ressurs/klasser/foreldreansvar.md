

# Slot: foreldreansvar 


_Personar denne personen har foreldreansvar for._





URI: [fint:foreldreansvar](https://schema.fintlabs.no/foreldreansvar)
Alias: foreldreansvar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](Person.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [fint:foreldreansvar](https://schema.fintlabs.no/foreldreansvar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Person](Person.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:foreldreansvar |
| native | https://schema.fintlabs.no/ressurs/:foreldreansvar |




## LinkML Source

<details>
```yaml
name: foreldreansvar
description: Personar denne personen har foreldreansvar for.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: fint:foreldreansvar
alias: foreldreansvar
owner: Person
domain_of:
- Person
range: Person
multivalued: true

```
</details>