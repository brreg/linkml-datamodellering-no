

# Slot: begynnelse 


_Starttidspunkt for eit tidsrom._





URI: [time:hasBeginning](http://www.w3.org/6006/time#hasBeginning)
Alias: begynnelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tidsrom](Tidsrom.md) | Eit tidsintervall med start- og sluttdato |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tidsinstant](Tidsinstant.md) |
| Domain Of | [Tidsrom](Tidsrom.md) |
| Slot URI | [time:hasBeginning](http://www.w3.org/6006/time#hasBeginning) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | time:hasBeginning |
| native | https://data.norge.no/linkml/dcat-ap-no/begynnelse |




## LinkML Source

<details>
```yaml
name: begynnelse
description: Starttidspunkt for eit tidsrom.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: time:hasBeginning
alias: begynnelse
domain_of:
- Tidsrom
range: Tidsinstant

```
</details>