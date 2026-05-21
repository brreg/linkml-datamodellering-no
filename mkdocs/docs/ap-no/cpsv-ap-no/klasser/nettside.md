

# Slot: nettside 


_Nettside for tenestekanalane._





URI: [vcard:hasURL](http://www.w3.org/2006/vcard/ns#hasURL)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjenestekanal](tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Tjenestekanal](tjenestekanal.md) |
| Slot URI | [vcard:hasURL](http://www.w3.org/2006/vcard/ns#hasURL) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vcard:hasURL |
| native | https://data.norge.no/linkml/cpsv-ap-no/nettside |




## LinkML Source

<details>
```yaml
name: nettside
description: Nettside for tenestekanalane.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: vcard:hasURL
domain_of:
- Tjenestekanal
range: uri
multivalued: true

```
</details>