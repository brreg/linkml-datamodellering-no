

# Slot: feidenavn 


_Feide-identifikator for skoleressursen._





URI: [utd:feidenavn](https://schema.fintlabs.no/utdanning/feidenavn)
Alias: feidenavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skoleressurs](Skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](Identifikator.md) |
| Domain Of | [Skoleressurs](Skoleressurs.md) |
| Slot URI | [utd:feidenavn](https://schema.fintlabs.no/utdanning/feidenavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Skoleressurs](Skoleressurs.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:feidenavn |
| native | https://schema.fintlabs.no/utdanning/:feidenavn |




## LinkML Source

<details>
```yaml
name: feidenavn
description: Feide-identifikator for skoleressursen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:feidenavn
alias: feidenavn
owner: Skoleressurs
domain_of:
- Skoleressurs
range: Identifikator
inlined: true

```
</details>