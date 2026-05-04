

# Slot: skoleeierType 


_Kategori for skuleeigartilknyting._





URI: [utd:skoleeierType](https://schema.fintlabs.no/utdanning/skoleeierType)
Alias: skoleeierType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](Skole.md) | Ein skule eller opplæringsinstitusjon |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skoleeiertype](Skoleeiertype.md) |
| Domain Of | [Skole](Skole.md) |
| Slot URI | [utd:skoleeierType](https://schema.fintlabs.no/utdanning/skoleeierType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Skole](Skole.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:skoleeierType |
| native | https://schema.fintlabs.no/utdanning/:skoleeierType |




## LinkML Source

<details>
```yaml
name: skoleeierType
description: Kategori for skuleeigartilknyting.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:skoleeierType
alias: skoleeierType
owner: Skole
domain_of:
- Skole
range: Skoleeiertype

```
</details>