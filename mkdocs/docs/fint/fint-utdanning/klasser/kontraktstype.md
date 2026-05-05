

# Slot: kontraktstype 


_Type kontrakt for lærlingen._





URI: [utd:kontraktstype](https://schema.fintlabs.no/utdanning/kontraktstype)
Alias: kontraktstype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Laerling](laerling.md) | Ein lærling i yrkesopplæring |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Laerling](laerling.md) |
| Slot URI | [utd:kontraktstype](https://schema.fintlabs.no/utdanning/kontraktstype) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Laerling](laerling.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:kontraktstype |
| native | https://schema.fintlabs.no/utdanning/:kontraktstype |




## LinkML Source

<details>
```yaml
name: kontraktstype
description: Type kontrakt for lærlingen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:kontraktstype
alias: kontraktstype
owner: Laerling
domain_of:
- Laerling
range: string

```
</details>