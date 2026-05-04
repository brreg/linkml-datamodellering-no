

# Slot: startdato 


_Startdato for tidsrommet._





URI: [dcat:startDate](http://www.w3.org/ns/dcat#startDate)
Alias: startdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tidsrom](Tidsrom.md) | Eit tidsintervall med start- og sluttdato |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Tidsrom](Tidsrom.md) |
| Slot URI | [dcat:startDate](http://www.w3.org/ns/dcat#startDate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:startDate |
| native | https://data.norge.no/linkml/dcat-ap-no/startdato |




## LinkML Source

<details>
```yaml
name: startdato
description: Startdato for tidsrommet.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:startDate
alias: startdato
domain_of:
- Tidsrom
range: date

```
</details>