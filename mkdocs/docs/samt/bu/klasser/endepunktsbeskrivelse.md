

# Slot: endepunktsbeskrivelse 


_URL til beskriving av endepunktet (t.d. OpenAPI-dokument)._





URI: [dcat:endpointDescription](http://www.w3.org/ns/dcat#endpointDescription)
Alias: endepunktsbeskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](uri.md) |
| Domain Of | [Datatjeneste](datatjeneste.md) |
| Slot URI | [dcat:endpointDescription](http://www.w3.org/ns/dcat#endpointDescription) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:endpointDescription |
| native | samtbuskole:endepunktsbeskrivelse |




## LinkML Source

<details>
```yaml
name: endepunktsbeskrivelse
description: URL til beskriving av endepunktet (t.d. OpenAPI-dokument).
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dcat:endpointDescription
alias: endepunktsbeskrivelse
domain_of:
- Datatjeneste
range: uri
multivalued: true

```
</details>