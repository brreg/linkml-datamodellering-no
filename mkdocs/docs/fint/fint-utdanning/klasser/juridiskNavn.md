

# Slot: juridiskNavn 


_Juridisk namn på skulen._





URI: [utd:juridiskNavn](https://schema.fintlabs.no/utdanning/juridiskNavn)
Alias: juridiskNavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](Skole.md) | Ein skule eller opplæringsinstitusjon |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Skole](Skole.md) |
| Slot URI | [utd:juridiskNavn](https://schema.fintlabs.no/utdanning/juridiskNavn) |

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
| self | utd:juridiskNavn |
| native | https://schema.fintlabs.no/utdanning/:juridiskNavn |




## LinkML Source

<details>
```yaml
name: juridiskNavn
description: Juridisk namn på skulen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:juridiskNavn
alias: juridiskNavn
owner: Skole
domain_of:
- Skole
range: string

```
</details>