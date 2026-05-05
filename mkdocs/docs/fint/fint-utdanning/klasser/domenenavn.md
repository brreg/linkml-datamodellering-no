

# Slot: domenenavn 


_Domenenamn for skulen._





URI: [utd:domenenavn](https://schema.fintlabs.no/utdanning/domenenavn)
Alias: domenenavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Skole](skole.md) |
| Slot URI | [utd:domenenavn](https://schema.fintlabs.no/utdanning/domenenavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Skole](skole.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:domenenavn |
| native | https://schema.fintlabs.no/utdanning/:domenenavn |




## LinkML Source

<details>
```yaml
name: domenenavn
description: Domenenamn for skulen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:domenenavn
alias: domenenavn
owner: Skole
domain_of:
- Skole
range: string

```
</details>