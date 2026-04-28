

# Slot: dokumentasjon 


_Lenke til dokumentasjon om ressursen._





URI: [foaf:page](http://xmlns.com/foaf/0.1/page)
Alias: dokumentasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Gebyr](Gebyr.md) | Eit gebyr knytt til bruk av ein datatjeneste |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Gebyr](Gebyr.md), [Distribusjon](Distribusjon.md), [Datasett](Datasett.md), [Datatjeneste](Datatjeneste.md) |
| Slot URI | [foaf:page](http://xmlns.com/foaf/0.1/page) |

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
| self | foaf:page |
| native | https://data.norge.no/linkml/dcat-ap-no/dokumentasjon |




## LinkML Source

<details>
```yaml
name: dokumentasjon
description: Lenke til dokumentasjon om ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: foaf:page
alias: dokumentasjon
domain_of:
- Gebyr
- Distribusjon
- Datasett
- Datatjeneste
range: uri
multivalued: true

```
</details>