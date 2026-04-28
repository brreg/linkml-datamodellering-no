

# Slot: endepunktsbeskrivelse 


_URL til beskriving av endepunktet (t.d. OpenAPI-dokument)._





URI: [dcat:endpointDescription](http://www.w3.org/ns/dcat#endpointDescription)
Alias: endepunktsbeskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Datatjeneste](Datatjeneste.md) |
| Slot URI | [dcat:endpointDescription](http://www.w3.org/ns/dcat#endpointDescription) |

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
| self | dcat:endpointDescription |
| native | https://data.norge.no/linkml/dcat-ap-no/endepunktsbeskrivelse |




## LinkML Source

<details>
```yaml
name: endepunktsbeskrivelse
description: URL til beskriving av endepunktet (t.d. OpenAPI-dokument).
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:endpointDescription
alias: endepunktsbeskrivelse
domain_of:
- Datatjeneste
range: uri
multivalued: true

```
</details>