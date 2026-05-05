

# Slot: fullfortkode 


_Kode for fullførtresultatet._





URI: [utd:fullfortkode](https://schema.fintlabs.no/utdanning/fullfortkode)
Alias: fullfortkode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AvlagtProve](avlagtprove.md) | Ei avlagt prøve for ein lærling |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fullfortkode](fullfortkode.md) |
| Domain Of | [AvlagtProve](avlagtprove.md) |
| Slot URI | [utd:fullfortkode](https://schema.fintlabs.no/utdanning/fullfortkode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AvlagtProve](avlagtprove.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:fullfortkode |
| native | https://schema.fintlabs.no/utdanning/:fullfortkode |




## LinkML Source

<details>
```yaml
name: fullfortkode
description: Kode for fullførtresultatet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:fullfortkode
alias: fullfortkode
owner: AvlagtProve
domain_of:
- AvlagtProve
range: Fullfortkode

```
</details>