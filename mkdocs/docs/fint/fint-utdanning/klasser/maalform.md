

# Slot: maalform 


_Målform personen føretrekkjer._





URI: [fint:maalform](https://schema.fintlabs.no/maalform)
Alias: maalform

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Spraak](Spraak.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [fint:maalform](https://schema.fintlabs.no/maalform) |

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


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:maalform |
| native | https://schema.fintlabs.no/utdanning/:maalform |




## LinkML Source

<details>
```yaml
name: maalform
description: Målform personen føretrekkjer.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: fint:maalform
alias: maalform
owner: Person
domain_of:
- Person
range: Spraak

```
</details>