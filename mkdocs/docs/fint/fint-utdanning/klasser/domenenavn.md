

# Slot: domenenavn 


_Domenenamn for skulen._





URI: [utd:domenenavn](https://schema.fintlabs.no/utdanning/domenenavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Skole](skole.md) |
| Slot URI | [utd:domenenavn](https://schema.fintlabs.no/utdanning/domenenavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




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
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:domenenavn
domain_of:
- Skole
range: string

```
</details>