

# Slot: har_kvalitetsmerknad 


_Kvalitetsmerknad knytt til datasettet._





URI: [dqv:hasQualityAnnotation](http://www.w3.org/ns/dqv#hasQualityAnnotation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [dqv:hasQualityAnnotation](http://www.w3.org/ns/dqv#hasQualityAnnotation) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:hasQualityAnnotation |
| native | https://data.norge.no/linkml/dcat-ap-no/har_kvalitetsmerknad |




## LinkML Source

<details>
```yaml
name: har_kvalitetsmerknad
description: Kvalitetsmerknad knytt til datasettet.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dqv:hasQualityAnnotation
domain_of:
- Datasett
range: Kvalitetsmerknad
multivalued: true

```
</details>