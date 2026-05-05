

# Slot: slutt 


_Sluttidspunkt for eit tidsrom._





URI: [time:hasEnd](http://www.w3.org/6006/time#hasEnd)
Alias: slutt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tidsrom](tidsrom.md) | Eit tidsintervall med start- og sluttdato |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tidsinstant](tidsinstant.md) |
| Domain Of | [Tidsrom](tidsrom.md) |
| Slot URI | [time:hasEnd](http://www.w3.org/6006/time#hasEnd) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | time:hasEnd |
| native | samtbuskole:slutt |




## LinkML Source

<details>
```yaml
name: slutt
description: Sluttidspunkt for eit tidsrom.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: time:hasEnd
alias: slutt
domain_of:
- Tidsrom
range: Tidsinstant

```
</details>