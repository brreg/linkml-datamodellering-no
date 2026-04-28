

# Slot: versjon 


_Versjonsnummer._





URI: [dcat:version](http://www.w3.org/ns/dcat#version)
Alias: versjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Standard](Standard.md) | Ein standard som ein ressurs er i samsvar med |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Standard](Standard.md), [Datasett](Datasett.md), [Datatjeneste](Datatjeneste.md) |
| Slot URI | [dcat:version](http://www.w3.org/ns/dcat#version) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:version |
| native | https://data.norge.no/linkml/dcat-ap-no/versjon |




## LinkML Source

<details>
```yaml
name: versjon
description: Versjonsnummer.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:version
alias: versjon
domain_of:
- Standard
- Datasett
- Datatjeneste
range: string

```
</details>