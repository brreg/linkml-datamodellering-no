

# Slot: temaer 


_Temavokabular brukt i katalogen (dcat:themeTaxonomy)._





URI: [dcat:themeTaxonomy](http://www.w3.org/ns/dcat#themeTaxonomy)
Alias: temaer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Modelkatalog](Modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrepssamling](Begrepssamling.md) |
| Domain Of | [Modelkatalog](Modelkatalog.md) |
| Slot URI | [dcat:themeTaxonomy](http://www.w3.org/ns/dcat#themeTaxonomy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:themeTaxonomy |
| native | https://data.norge.no/linkml/modelldcat-ap-no/temaer |




## LinkML Source

<details>
```yaml
name: temaer
description: Temavokabular brukt i katalogen (dcat:themeTaxonomy).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dcat:themeTaxonomy
alias: temaer
domain_of:
- Modelkatalog
range: Begrepssamling
multivalued: true

```
</details>