

# Slot: skolenummer 


_Nasjonal skulenummer-identifikator._





URI: [utd:skolenummer](https://schema.fintlabs.no/utdanning/skolenummer)
Alias: skolenummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Skole](skole.md) |
| Slot URI | [utd:skolenummer](https://schema.fintlabs.no/utdanning/skolenummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Skole](skole.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:skolenummer |
| native | https://schema.fintlabs.no/utdanning/:skolenummer |




## LinkML Source

<details>
```yaml
name: skolenummer
description: Nasjonal skulenummer-identifikator.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:skolenummer
alias: skolenummer
owner: Skole
domain_of:
- Skole
range: Identifikator
inlined: true

```
</details>