

# Slot: bostedsadresse 


_Folkeregistrert adresse til personen._





URI: [fint:bostedsadresse](https://schema.fintlabs.no/bostedsadresse)
Alias: bostedsadresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresse](Adresse.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [fint:bostedsadresse](https://schema.fintlabs.no/bostedsadresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Person](Person.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:bostedsadresse |
| native | https://schema.fintlabs.no/personvern/:bostedsadresse |




## LinkML Source

<details>
```yaml
name: bostedsadresse
description: Folkeregistrert adresse til personen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-personvern
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