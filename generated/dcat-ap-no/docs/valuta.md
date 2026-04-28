

# Slot: valuta 


_Valuta for gebyret._





URI: [cv:currency](http://data.europa.eu/m8g/currency)
Alias: valuta

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Gebyr](Gebyr.md) | Eit gebyr knytt til bruk av ein datatjeneste |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](Begrep.md) |
| Domain Of | [Gebyr](Gebyr.md) |
| Slot URI | [cv:currency](http://data.europa.eu/m8g/currency) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:currency |
| native | https://data.norge.no/linkml/dcat-ap-no/valuta |




## LinkML Source

<details>
```yaml
name: valuta
description: Valuta for gebyret.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: cv:currency
alias: valuta
domain_of:
- Gebyr
range: Begrep

```
</details>