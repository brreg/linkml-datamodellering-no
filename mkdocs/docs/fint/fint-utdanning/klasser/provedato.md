

# Slot: provedato 


_Dato prøva vart avlagt._





URI: [utd:provedato](https://schema.fintlabs.no/utdanning/provedato)
Alias: provedato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AvlagtProve](AvlagtProve.md) | Ei avlagt prøve for ein lærling |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [AvlagtProve](AvlagtProve.md) |
| Slot URI | [utd:provedato](https://schema.fintlabs.no/utdanning/provedato) |

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
| self | utd:provedato |
| native | https://schema.fintlabs.no/utdanning/:provedato |




## LinkML Source

<details>
```yaml
name: provedato
description: Dato prøva vart avlagt.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:provedato
alias: provedato
owner: AvlagtProve
domain_of:
- AvlagtProve
range: date

```
</details>