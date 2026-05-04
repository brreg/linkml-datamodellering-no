

# Slot: tidsrom_start 


_Startdato for tidsromet (dct:startDate)._





URI: [dct:startDate](http://purl.org/dc/terms/startDate)
Alias: tidsrom_start

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tidsrom](Tidsrom.md) | Eit tidsrom med start- og/eller sluttdato (dct:PeriodOfTime) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Tidsrom](Tidsrom.md) |
| Slot URI | [dct:startDate](http://purl.org/dc/terms/startDate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/xkos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:startDate |
| native | https://data.norge.no/linkml/xkos-ap-no/tidsrom_start |




## LinkML Source

<details>
```yaml
name: tidsrom_start
description: Startdato for tidsromet (dct:startDate).
from_schema: https://data.norge.no/linkml/xkos-ap-no
rank: 1000
slot_uri: dct:startDate
alias: tidsrom_start
domain_of:
- Tidsrom
range: date

```
</details>