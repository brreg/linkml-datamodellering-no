

# Slot: annen_spesifikk_relasjon 


_Kvalifisert relasjon til ein annan ressurs._





URI: [dcat:qualifiedRelation](http://www.w3.org/ns/dcat#qualifiedRelation)
Alias: annen_spesifikk_relasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Relasjon](Relasjon.md) |
| Domain Of | [Datasett](Datasett.md) |
| Slot URI | [dcat:qualifiedRelation](http://www.w3.org/ns/dcat#qualifiedRelation) |

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
| self | dcat:qualifiedRelation |
| native | https://data.norge.no/linkml/dcat-ap-no/annen_spesifikk_relasjon |




## LinkML Source

<details>
```yaml
name: annen_spesifikk_relasjon
description: Kvalifisert relasjon til ein annan ressurs.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:qualifiedRelation
alias: annen_spesifikk_relasjon
domain_of:
- Datasett
range: Relasjon
multivalued: true

```
</details>