

# Slot: har_kvalitetsmaaling 


_Kvalitetsmåling knytt til datasettet._





URI: [dqv:hasQualityMeasurement](http://www.w3.org/ns/dqv#hasQualityMeasurement)
Alias: har_kvalitetsmaaling

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](Datasett.md) | Eit datasett (dcat:Dataset) utvida med DQV-AP-NO-eigenskapar for kvalitetsinf... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kvalitetsmaaling](Kvalitetsmaaling.md) |
| Domain Of | [Datasett](Datasett.md) |
| Slot URI | [dqv:hasQualityMeasurement](http://www.w3.org/ns/dqv#hasQualityMeasurement) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:hasQualityMeasurement |
| native | https://data.norge.no/linkml/dqv-ap-no/har_kvalitetsmaaling |




## LinkML Source

<details>
```yaml
name: har_kvalitetsmaaling
description: Kvalitetsmåling knytt til datasettet.
from_schema: https://data.norge.no/linkml/dqv-ap-no
rank: 1000
slot_uri: dqv:hasQualityMeasurement
alias: har_kvalitetsmaaling
domain_of:
- Datasett
range: Kvalitetsmaaling
multivalued: true

```
</details>