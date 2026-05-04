

# Slot: bevistype 


_Type kompetansebevis._





URI: [utd:bevistype](https://schema.fintlabs.no/utdanning/bevistype)
Alias: bevistype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AvlagtProve](AvlagtProve.md) | Ei avlagt prøve for ein lærling |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bevistype](Bevistype.md) |
| Domain Of | [AvlagtProve](AvlagtProve.md) |
| Slot URI | [utd:bevistype](https://schema.fintlabs.no/utdanning/bevistype) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AvlagtProve](AvlagtProve.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:bevistype |
| native | https://schema.fintlabs.no/utdanning/:bevistype |




## LinkML Source

<details>
```yaml
name: bevistype
description: Type kompetansebevis.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:bevistype
alias: bevistype
owner: AvlagtProve
domain_of:
- AvlagtProve
range: Bevistype

```
</details>