

# Slot: dokumentasjon 


_Lenke til dokumentasjon om ressursen._





URI: [foaf:page](http://xmlns.com/foaf/0.1/page)
Alias: dokumentasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Gebyr](gebyr.md) | Eit gebyr knytt til bruk av ein datatjeneste |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Gebyr](gebyr.md), [Distribusjon](distribusjon.md), [Datasett](datasett.md), [Datatjeneste](datatjeneste.md) |
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