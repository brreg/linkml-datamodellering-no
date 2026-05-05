

# Slot: brevtype 


_Type brev knytt til prøva._





URI: [utd:brevtype](https://schema.fintlabs.no/utdanning/brevtype)
Alias: brevtype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AvlagtProve](avlagtprove.md) | Ei avlagt prøve for ein lærling |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Brevtype](brevtype.md) |
| Domain Of | [AvlagtProve](avlagtprove.md) |
| Slot URI | [utd:brevtype](https://schema.fintlabs.no/utdanning/brevtype) |

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
| self | utd:brevtype |
| native | https://schema.fintlabs.no/utdanning/:brevtype |




## LinkML Source

<details>
```yaml
name: brevtype
description: Type brev knytt til prøva.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:brevtype
alias: brevtype
owner: AvlagtProve
domain_of:
- AvlagtProve
range: Brevtype

```
</details>