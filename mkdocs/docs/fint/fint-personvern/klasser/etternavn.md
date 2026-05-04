

# Slot: etternavn 


_Etternamn til personen._





URI: [fint:etternavn](https://schema.fintlabs.no/etternavn)
Alias: etternavn

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
| Slot URI | [fint:etternavn](https://schema.fintlabs.no/etternavn) |

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


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:etternavn |
| native | https://schema.fintlabs.no/personvern/:etternavn |




## LinkML Source

<details>
```yaml
name: etternavn
description: Etternamn til personen.
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: fint:etternavn
alias: etternavn
owner: Personnavn
domain_of:
- Personnavn
range: string
required: true

```
</details>