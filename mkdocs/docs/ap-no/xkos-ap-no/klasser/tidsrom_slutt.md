

# Slot: tidsrom_slutt 


_Sluttdato for tidsromet (dct:endDate)._





URI: [dct:endDate](http://purl.org/dc/terms/endDate)
Alias: tidsrom_slutt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tidsrom](tidsrom.md) | Eit tidsrom med start- og/eller sluttdato (dct:PeriodOfTime) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](date.md) |
| Domain Of | [Tidsrom](tidsrom.md) |
| Slot URI | [dct:endDate](http://purl.org/dc/terms/endDate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/xkos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:endDate |
| native | https://data.norge.no/linkml/xkos-ap-no/tidsrom_slutt |




## LinkML Source

<details>
```yaml
name: tidsrom_slutt
description: Sluttdato for tidsromet (dct:endDate).
from_schema: https://data.norge.no/linkml/xkos-ap-no
rank: 1000
slot_uri: dct:endDate
alias: tidsrom_slutt
domain_of:
- Tidsrom
range: date

```
</details>