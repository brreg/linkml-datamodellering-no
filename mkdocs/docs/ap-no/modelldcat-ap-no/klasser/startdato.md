

# Slot: startdato 


_Startdato for tidsperioden (dcat:startDate)._





URI: [dcat:startDate](http://www.w3.org/ns/dcat#startDate)
Alias: startdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tidsperiode](Tidsperiode.md) | Eit tidsintervall med start- og sluttdato |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Tidsperiode](Tidsperiode.md) |
| Slot URI | [dcat:startDate](http://www.w3.org/ns/dcat#startDate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:startDate |
| native | https://data.norge.no/linkml/modelldcat-ap-no/startdato |




## LinkML Source

<details>
```yaml
name: startdato
description: Startdato for tidsperioden (dcat:startDate).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dcat:startDate
alias: startdato
domain_of:
- Tidsperiode
range: date

```
</details>