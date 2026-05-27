

# Slot: relatert_teneste 


_Relatert teneste._





URI: [cv:relatedService](http://data.europa.eu/m8g/relatedService)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
| Slot URI | [cv:relatedService](http://data.europa.eu/m8g/relatedService) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:relatedService |
| native | https://data.norge.no/ap-no/cpsv-ap-no/relatert_teneste |




## LinkML Source

<details>
```yaml
name: relatert_teneste
description: Relatert teneste.
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: cv:relatedService
domain_of:
- OffentligTjeneste
- Tjeneste
range: uriorcurie
multivalued: true

```
</details>