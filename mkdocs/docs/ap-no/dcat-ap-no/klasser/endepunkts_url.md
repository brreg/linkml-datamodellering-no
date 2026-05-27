

# Slot: endepunkts_url 


_URL til datatjenestens endepunkt._





URI: [dcat:endpointURL](http://www.w3.org/ns/dcat#endpointURL)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Datatjeneste](datatjeneste.md) |
| Slot URI | [dcat:endpointURL](http://www.w3.org/ns/dcat#endpointURL) |

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
| self | dcat:endpointURL |
| native | https://data.norge.no/ap-no/dcat-ap-no/endepunkts_url |




## LinkML Source

<details>
```yaml
name: endepunkts_url
description: URL til datatjenestens endepunkt.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
rank: 1000
slot_uri: dcat:endpointURL
domain_of:
- Datatjeneste
range: uri
multivalued: true

```
</details>