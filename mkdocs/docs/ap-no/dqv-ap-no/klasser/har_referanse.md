

# Slot: har_referanse 


_Referanse til ekstern ressurs (rdfs:seeAlso)._





URI: [rdfs:seeAlso](http://www.w3.org/2000/01/rdf-schema#seeAlso)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Standard](standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [RegulativRessurs](regulativressurs.md), [Standard](standard.md) |
| Slot URI | [rdfs:seeAlso](http://www.w3.org/2000/01/rdf-schema#seeAlso) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:seeAlso |
| native | https://data.norge.no/ap-no/common-ap-no/har_referanse |




## LinkML Source

<details>
```yaml
name: har_referanse
description: Referanse til ekstern ressurs (rdfs:seeAlso).
from_schema: https://data.norge.no/ap-no/common-ap-no
slot_uri: rdfs:seeAlso
domain_of:
- RegulativRessurs
- Standard
range: uri
multivalued: true

```
</details>