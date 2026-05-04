

# Slot: laretid 


_Læringstidsperiode for lærlingen._





URI: [utd:laretid](https://schema.fintlabs.no/utdanning/laretid)
Alias: laretid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Laerling](Laerling.md) | Ein lærling i yrkesopplæring |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Periode](Periode.md) |
| Domain Of | [Laerling](Laerling.md) |
| Slot URI | [utd:laretid](https://schema.fintlabs.no/utdanning/laretid) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Laerling](Laerling.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:laretid |
| native | https://schema.fintlabs.no/utdanning/:laretid |




## LinkML Source

<details>
```yaml
name: laretid
description: Læringstidsperiode for lærlingen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:laretid
alias: laretid
owner: Laerling
domain_of:
- Laerling
range: Periode
inlined: true

```
</details>