

# Slot: eksamensdato 


_Dato for eksamenen._





URI: [utd:eksamensdato](https://schema.fintlabs.no/utdanning/eksamensdato)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Eksamensgruppe](eksamensgruppe.md) |
| Slot URI | [utd:eksamensdato](https://schema.fintlabs.no/utdanning/eksamensdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




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
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:eksamensdato
domain_of:
- Eksamensgruppe
range: datetime

```
</details>