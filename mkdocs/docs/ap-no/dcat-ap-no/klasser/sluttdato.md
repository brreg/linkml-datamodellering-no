

# Slot: sluttdato 


_Sluttdato for tidsrommet._





URI: [dcat:endDate](http://www.w3.org/ns/dcat#endDate)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tidsrom](tidsrom.md) | Eit tidsintervall med start- og sluttdato |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Tidsrom](tidsrom.md) |
| Slot URI | [dcat:endDate](http://www.w3.org/ns/dcat#endDate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:endDate |
| native | https://data.norge.no/ap-no/dcat-ap-no/sluttdato |




## LinkML Source

<details>
```yaml
name: sluttdato
description: Sluttdato for tidsrommet.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
rank: 1000
slot_uri: dcat:endDate
domain_of:
- Tidsrom
range: date

```
</details>