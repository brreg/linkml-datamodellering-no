

# Slot: kontonummer 


_Kontonummer til leverandøren._





URI: [okn:kontonummer](https://schema.fintlabs.no/okonomi/kontonummer)
Alias: kontonummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Leverandor](leverandor.md) | Person eller verksemd som leverer produkt eller tenester (Leverandør) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Leverandor](leverandor.md) |
| Slot URI | [okn:kontonummer](https://schema.fintlabs.no/okonomi/kontonummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Leverandor](leverandor.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:kontonummer |
| native | https://schema.fintlabs.no/okonomi/:kontonummer |




## LinkML Source

<details>
```yaml
name: kontonummer
description: Kontonummer til leverandøren.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:kontonummer
alias: kontonummer
owner: Leverandor
domain_of:
- Leverandor
range: string

```
</details>