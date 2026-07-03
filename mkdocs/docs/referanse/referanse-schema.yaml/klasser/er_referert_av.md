

# Slot: er_referert_av 


_Ressurs som refererer til dette datasettet._





URI: [dct:isReferencedBy](http://purl.org/dc/terms/isReferencedBy)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [dct:isReferencedBy](http://purl.org/dc/terms/isReferencedBy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:isReferencedBy |
| native | https://data.norge.no/ap-no/dcat-ap-no/er_referert_av |




## LinkML Source

<details>
```yaml
name: er_referert_av
description: Ressurs som refererer til dette datasettet.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dct:isReferencedBy
domain_of:
- Datasett
range: uri
multivalued: true

```
</details>