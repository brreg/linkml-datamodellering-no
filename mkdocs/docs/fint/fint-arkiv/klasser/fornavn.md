

# Slot: fornavn 


_Fornamn til personen._





URI: [fint:fornavn](https://schema.fintlabs.no/fornavn)
Alias: fornavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personnavn](Personnavn.md) | Namn på ein person |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Personnavn](Personnavn.md) |
| Slot URI | [fint:fornavn](https://schema.fintlabs.no/fornavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Personnavn](Personnavn.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:fornavn |
| native | https://schema.fintlabs.no/arkiv/:fornavn |




## LinkML Source

<details>
```yaml
name: fornavn
description: Fornamn til personen.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: fint:fornavn
alias: fornavn
owner: Personnavn
domain_of:
- Personnavn
range: string
required: true

```
</details>