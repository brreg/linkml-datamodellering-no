

# Slot: eksamensdato 


_Dato for eksamenen._





URI: [utd:eksamensdato](https://schema.fintlabs.no/utdanning/eksamensdato)
Alias: eksamensdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppe](Eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Eksamensgruppe](Eksamensgruppe.md) |
| Slot URI | [utd:eksamensdato](https://schema.fintlabs.no/utdanning/eksamensdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Eksamensgruppe](Eksamensgruppe.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:eksamensdato |
| native | https://schema.fintlabs.no/utdanning/:eksamensdato |




## LinkML Source

<details>
```yaml
name: eksamensdato
description: Dato for eksamenen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:eksamensdato
alias: eksamensdato
owner: Eksamensgruppe
domain_of:
- Eksamensgruppe
range: datetime

```
</details>