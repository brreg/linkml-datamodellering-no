

# Slot: statsborgerskap 


_Alle statsborgarskap personen har._





URI: [fint:statsborgerskap](https://schema.fintlabs.no/statsborgerskap)
Alias: statsborgerskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  yes  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:statsborgerskap |
| native | https://schema.fintlabs.no/:statsborgerskap |




## LinkML Source

<details>
```yaml
name: statsborgerskap
description: Alle statsborgarskap personen har.
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:statsborgerskap
alias: statsborgerskap
domain_of:
- Person
range: Landkode
multivalued: true

```
</details>