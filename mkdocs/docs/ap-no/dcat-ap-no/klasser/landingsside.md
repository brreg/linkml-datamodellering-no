

# Slot: landingsside 


_Nettside med informasjon om ressursen._





URI: [dcat:landingPage](http://www.w3.org/ns/dcat#landingPage)
Alias: landingsside

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](uri.md) |
| Domain Of | [Datasett](datasett.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [dcat:landingPage](http://www.w3.org/ns/dcat#landingPage) |

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
| self | dcat:landingPage |
| native | https://data.norge.no/linkml/dcat-ap-no/landingsside |




## LinkML Source

<details>
```yaml
name: landingsside
description: Nettside med informasjon om ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:landingPage
alias: landingsside
domain_of:
- Datasett
- Datatjeneste
range: uri
multivalued: true

```
</details>