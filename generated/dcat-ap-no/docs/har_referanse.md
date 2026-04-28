

# Slot: har_referanse 


_Referanse til ekstern ressurs (rdfs:seeAlso)._





URI: [rdfs:seeAlso](http://www.w3.org/2000/01/rdf-schema#seeAlso)
Alias: har_referanse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegulativRessurs](RegulativRessurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Standard](Standard.md) | Ein standard som ein ressurs er i samsvar med |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Standard](Standard.md), [RegulativRessurs](RegulativRessurs.md) |
| Slot URI | [rdfs:seeAlso](http://www.w3.org/2000/01/rdf-schema#seeAlso) |

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
| self | rdfs:seeAlso |
| native | https://data.norge.no/linkml/dcat-ap-no/har_referanse |




## LinkML Source

<details>
```yaml
name: har_referanse
description: Referanse til ekstern ressurs (rdfs:seeAlso).
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: rdfs:seeAlso
alias: har_referanse
domain_of:
- Standard
- RegulativRessurs
range: uri
multivalued: true

```
</details>