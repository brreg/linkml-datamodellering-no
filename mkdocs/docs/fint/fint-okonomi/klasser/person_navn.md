

# Slot: person_navn 


_Namn på personen._





URI: [fint:personNavn](https://schema.fintlabs.no/personNavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personnavn](personnavn.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [fint:personNavn](https://schema.fintlabs.no/personNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:personNavn |
| native | https://schema.fintlabs.no/:person_navn |




## LinkML Source

<details>
```yaml
name: person_navn
description: Namn på personen.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:personNavn
domain_of:
- Person
range: Personnavn
inlined: true

```
</details>