

# Slot: versjon 


_Versjonsnummer._





URI: [dcat:version](http://www.w3.org/ns/dcat#version)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Datasett](datasett.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [dcat:version](http://www.w3.org/ns/dcat#version) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:version |
| native | https://data.norge.no/ap-no/dcat-ap-no/versjon |




## LinkML Source

<details>
```yaml
name: versjon
description: Versjonsnummer.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
rank: 1000
slot_uri: dcat:version
domain_of:
- Datasett
- Datatjeneste
range: string

```
</details>