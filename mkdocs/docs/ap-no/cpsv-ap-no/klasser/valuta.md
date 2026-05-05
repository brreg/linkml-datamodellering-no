

# Slot: valuta 


_Valuta (cv:currency)._





URI: [cv:currency](http://data.europa.eu/m8g/currency)
Alias: valuta

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Gebyr](gebyr.md) | Eit gebyr knytt til ei teneste |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Gebyr](gebyr.md) |
| Slot URI | [cv:currency](http://data.europa.eu/m8g/currency) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:currency |
| native | https://data.norge.no/linkml/cpsv-ap-no/valuta |




## LinkML Source

<details>
```yaml
name: valuta
description: Valuta (cv:currency).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:currency
alias: valuta
domain_of:
- Gebyr
range: Konsept

```
</details>