

# Slot: bostedsadresse 


_Folkeregistrert adresse til personen._





URI: [fint:bostedsadresse](https://schema.fintlabs.no/bostedsadresse)
Alias: bostedsadresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresse](adresse.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [fint:bostedsadresse](https://schema.fintlabs.no/bostedsadresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Person](person.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:bostedsadresse |
| native | https://schema.fintlabs.no/ressurs/:bostedsadresse |




## LinkML Source

<details>
```yaml
name: bostedsadresse
description: Folkeregistrert adresse til personen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: fint:bostedsadresse
alias: bostedsadresse
owner: Person
domain_of:
- Person
range: Adresse
inlined: true

```
</details>