

# Slot: har_kvalitetsmerknad 


_Kvalitetsmerknad knytt til datasettet._





URI: [dqv:hasQualityAnnotation](http://www.w3.org/ns/dqv#hasQualityAnnotation)
Alias: har_kvalitetsmerknad

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](Datasett.md) | Eit datasett (dcat:Dataset) utvida med DQV-AP-NO-eigenskapar for kvalitetsinf... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kvalitetsmerknad](Kvalitetsmerknad.md) |
| Domain Of | [Datasett](Datasett.md) |
| Slot URI | [dqv:hasQualityAnnotation](http://www.w3.org/ns/dqv#hasQualityAnnotation) |

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
| self | dqv:hasQualityAnnotation |
| native | https://data.norge.no/linkml/dqv-ap-no/har_kvalitetsmerknad |




## LinkML Source

<details>
```yaml
name: har_kvalitetsmerknad
description: Kvalitetsmerknad knytt til datasettet.
from_schema: https://data.norge.no/linkml/dqv-ap-no
rank: 1000
slot_uri: dqv:hasQualityAnnotation
alias: har_kvalitetsmerknad
domain_of:
- Datasett
range: Kvalitetsmerknad
multivalued: true

```
</details>