

# Slot: begynnelse 


_Starttidspunkt for eit tidsrom._





URI: [time:hasBeginning](http://www.w3.org/6006/time#hasBeginning)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tidsrom](tidsrom.md) | Eit tidsintervall med start- og sluttdato |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Tidsrom](tidsrom.md) |
| Slot URI | [time:hasBeginning](http://www.w3.org/6006/time#hasBeginning) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | time:hasBeginning |
| native | https://data.norge.no/ap-no/dcat-ap-no/begynnelse |




## LinkML Source

<details>
```yaml
name: begynnelse
description: Starttidspunkt for eit tidsrom.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: time:hasBeginning
domain_of:
- Tidsrom
range: datetime

```
</details>