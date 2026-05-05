

# Slot: mellomnavn 


_Mellomnamn._





URI: [fint:mellomnavn](https://schema.fintlabs.no/mellomnavn)
Alias: mellomnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personnavn](personnavn.md) | Namn på ein person |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Personnavn](personnavn.md) |
| Slot URI | [fint:mellomnavn](https://schema.fintlabs.no/mellomnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Personnavn](personnavn.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:mellomnavn |
| native | https://schema.fintlabs.no/okonomi/:mellomnavn |




## LinkML Source

<details>
```yaml
name: mellomnavn
description: Mellomnamn.
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: fint:mellomnavn
alias: mellomnavn
owner: Personnavn
domain_of:
- Personnavn
range: string

```
</details>