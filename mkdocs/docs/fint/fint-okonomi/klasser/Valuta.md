

# Slot: valuta 


_Valuta for oppgjeve beløp._





URI: [okn:valuta](https://schema.fintlabs.no/okonomi/valuta)
Alias: valuta

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](Transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Valuta](Valuta.md) |
| Domain Of | [Transaksjon](Transaksjon.md) |
| Slot URI | [okn:valuta](https://schema.fintlabs.no/okonomi/valuta) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Transaksjon](Transaksjon.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:valuta |
| native | https://schema.fintlabs.no/okonomi/:valuta |




## LinkML Source

<details>
```yaml
name: valuta
description: Valuta for oppgjeve beløp.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:valuta
alias: valuta
owner: Transaksjon
domain_of:
- Transaksjon
range: Valuta
required: true

```
</details>