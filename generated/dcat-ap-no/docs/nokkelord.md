

# Slot: nokkelord 


_Nøkkelord som beskriv ressursen._





URI: [dcat:keyword](http://www.w3.org/ns/dcat#keyword)
Alias: nokkelord

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](LangString.md) |
| Domain Of | [Datasett](Datasett.md), [Datatjeneste](Datatjeneste.md) |
| Slot URI | [dcat:keyword](http://www.w3.org/ns/dcat#keyword) |

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
| self | dcat:keyword |
| native | https://data.norge.no/linkml/dcat-ap-no/nokkelord |




## LinkML Source

<details>
```yaml
name: nokkelord
description: Nøkkelord som beskriv ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:keyword
alias: nokkelord
domain_of:
- Datasett
- Datatjeneste
range: LangString
multivalued: true

```
</details>