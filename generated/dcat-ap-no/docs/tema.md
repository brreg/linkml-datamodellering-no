

# Slot: tema 


_Tema frå eit kontrollert vokabular._





URI: [dcat:theme](http://www.w3.org/ns/dcat#theme)
Alias: tema

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |
| [Datasettserie](Datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](Begrep.md) |
| Domain Of | [Datasett](Datasett.md), [Datasettserie](Datasettserie.md), [Datatjeneste](Datatjeneste.md) |
| Slot URI | [dcat:theme](http://www.w3.org/ns/dcat#theme) |

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
| self | dcat:theme |
| native | https://data.norge.no/linkml/dcat-ap-no/tema |




## LinkML Source

<details>
```yaml
name: tema
description: Tema frå eit kontrollert vokabular.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:theme
alias: tema
domain_of:
- Datasett
- Datasettserie
- Datatjeneste
range: Begrep
multivalued: true

```
</details>