

# Slot: startdato 


_Startdato for tidsrommet._





URI: [dcat:startDate](http://www.w3.org/ns/dcat#startDate)
Alias: startdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tidsrom](tidsrom.md) | Eit tidsintervall med start- og sluttdato |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](date.md) |
| Domain Of | [Tidsrom](tidsrom.md) |
| Slot URI | [dcat:startDate](http://www.w3.org/ns/dcat#startDate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:startDate |
| native | samtbuskole:startdato |




## LinkML Source

<details>
```yaml
name: startdato
description: Startdato for tidsrommet.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dcat:startDate
alias: startdato
domain_of:
- Tidsrom
range: date

```
</details>