

# Slot: versjon 


_Versjonsnummer._





URI: [dcat:version](http://www.w3.org/ns/dcat#version)
Alias: versjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Standard](standard.md) | Ein standard som ein ressurs er i samsvar med |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Standard](standard.md), [Datasett](datasett.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [dcat:version](http://www.w3.org/ns/dcat#version) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:version |
| native | samtbuskole:versjon |




## LinkML Source

<details>
```yaml
name: versjon
description: Versjonsnummer.
from_schema: https://example.no/ontology/samt-bu-skole
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