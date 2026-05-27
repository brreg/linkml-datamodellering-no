

# Slot: relatert_ressurs 


_Generisk relasjon til ein annan ressurs._





URI: [dct:relation](http://purl.org/dc/terms/relation)
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
| Slot URI | [dct:relation](http://purl.org/dc/terms/relation) |

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
| self | dct:relation |
| native | https://data.norge.no/ap-no/dcat-ap-no/relatert_ressurs |




## LinkML Source

<details>
```yaml
name: relatert_ressurs
description: Generisk relasjon til ein annan ressurs.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dct:relation
domain_of:
- Datasett
range: uri
multivalued: true

```
</details>