

# Slot: avlagtprove 


_Avlagde prøver for lærlingen._





URI: [utd:avlagtprove](https://schema.fintlabs.no/utdanning/avlagtprove)
Alias: avlagtprove

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Laerling](laerling.md) | Ein lærling i yrkesopplæring |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AvlagtProve](avlagtprove.md) |
| Domain Of | [Laerling](laerling.md) |
| Slot URI | [utd:avlagtprove](https://schema.fintlabs.no/utdanning/avlagtprove) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | utd:avlagtprove |
| native | https://schema.fintlabs.no/utdanning/:avlagtprove |




## LinkML Source

<details>
```yaml
name: avlagtprove
description: Avlagde prøver for lærlingen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:avlagtprove
alias: avlagtprove
owner: Laerling
domain_of:
- Laerling
range: AvlagtProve
multivalued: true

```
</details>