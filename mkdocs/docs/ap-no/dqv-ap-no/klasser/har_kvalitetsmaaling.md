

# Slot: har_kvalitetsmaaling 


_Kvalitetsmåling knytt til datasettet._





URI: [dqv:hasQualityMeasurement](http://www.w3.org/ns/dqv#hasQualityMeasurement)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kvalitetsmaaling](kvalitetsmaaling.md) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [dqv:hasQualityMeasurement](http://www.w3.org/ns/dqv#hasQualityMeasurement) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:hasQualityMeasurement |
| native | https://data.norge.no/ap-no/dqv-ap-no/har_kvalitetsmaaling |




## LinkML Source

<details>
```yaml
name: har_kvalitetsmaaling
description: Kvalitetsmåling knytt til datasettet.
from_schema: https://data.norge.no/ap-no/dqv-ap-no
rank: 1000
slot_uri: dqv:hasQualityMeasurement
domain_of:
- Datasett
range: Kvalitetsmaaling
multivalued: true

```
</details>