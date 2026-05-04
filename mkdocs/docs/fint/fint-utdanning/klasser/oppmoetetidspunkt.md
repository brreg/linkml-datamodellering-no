

# Slot: oppmoetetidspunkt 


_Tidspunkt for oppmøte til eksamenen._





URI: [utd:oppmoetetidspunkt](https://schema.fintlabs.no/utdanning/oppmoetetidspunkt)
Alias: oppmoetetidspunkt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamen](Eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Eksamen](Eksamen.md) |
| Slot URI | [utd:oppmoetetidspunkt](https://schema.fintlabs.no/utdanning/oppmoetetidspunkt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Eksamen](Eksamen.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:oppmoetetidspunkt |
| native | https://schema.fintlabs.no/utdanning/:oppmoetetidspunkt |




## LinkML Source

<details>
```yaml
name: oppmoetetidspunkt
description: Tidspunkt for oppmøte til eksamenen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:oppmoetetidspunkt
alias: oppmoetetidspunkt
owner: Eksamen
domain_of:
- Eksamen
range: datetime

```
</details>