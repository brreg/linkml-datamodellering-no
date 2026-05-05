

# Slot: statsborgerskap 


_Alle statsborgarskap personen har._





URI: [fint:statsborgerskap](https://schema.fintlabs.no/statsborgerskap)
Alias: statsborgerskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Landkode](landkode.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [fint:statsborgerskap](https://schema.fintlabs.no/statsborgerskap) |

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
| self | fint:statsborgerskap |
| native | https://schema.fintlabs.no/okonomi/:statsborgerskap |




## LinkML Source

<details>
```yaml
name: statsborgerskap
description: Alle statsborgarskap personen har.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: fint:statsborgerskap
alias: statsborgerskap
owner: Person
domain_of:
- Person
range: Landkode
multivalued: true

```
</details>