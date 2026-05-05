

# Slot: sluttdato 


_Sluttdato for tidsrommet._





URI: [dcat:endDate](http://www.w3.org/ns/dcat#endDate)
Alias: sluttdato

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
| Slot URI | [dcat:endDate](http://www.w3.org/ns/dcat#endDate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:endDate |
| native | samtbuskole:sluttdato |




## LinkML Source

<details>
```yaml
name: sluttdato
description: Sluttdato for tidsrommet.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dcat:endDate
alias: sluttdato
domain_of:
- Tidsrom
range: date

```
</details>