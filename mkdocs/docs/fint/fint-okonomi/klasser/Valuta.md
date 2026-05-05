

# Slot: valuta 


_Valuta for oppgjeve beløp._





URI: [okn:valuta](https://schema.fintlabs.no/okonomi/valuta)
Alias: valuta

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OkonomiValuta](okonomivaluta.md) |
| Domain Of | [Transaksjon](transaksjon.md) |
| Slot URI | [okn:valuta](https://schema.fintlabs.no/okonomi/valuta) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Transaksjon](transaksjon.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






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
range: OkonomiValuta
required: true

```
</details>