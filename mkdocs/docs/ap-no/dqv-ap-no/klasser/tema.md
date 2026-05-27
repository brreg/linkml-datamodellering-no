

# Slot: tema 


_Tema frå eit kontrollert vokabular._





URI: [dcat:theme](http://www.w3.org/ns/dcat#theme)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Datasett](datasett.md), [Datasettserie](datasettserie.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [dcat:theme](http://www.w3.org/ns/dcat#theme) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:theme |
| native | https://data.norge.no/ap-no/dcat-ap-no/tema |




## LinkML Source

<details>
```yaml
name: tema
description: Tema frå eit kontrollert vokabular.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dcat:theme
domain_of:
- Datasett
- Datasettserie
- Datatjeneste
range: string
multivalued: true

```
</details>