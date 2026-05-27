

# Slot: fodselsdato 


_Dato for fødsel._





URI: [fint:fodselsdato](https://schema.fintlabs.no/fodselsdato)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Person](person.md) |
| Slot URI | [fint:fodselsdato](https://schema.fintlabs.no/fodselsdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:fodselsdato |
| native | https://schema.fintlabs.no/:fodselsdato |




## LinkML Source

<details>
```yaml
name: fodselsdato
description: Dato for fødsel.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:fodselsdato
domain_of:
- Person
range: date

```
</details>