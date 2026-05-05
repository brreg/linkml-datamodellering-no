

# Slot: temaer 


_Temavokabular som vert brukt i katalogen._





URI: [dcat:themeTaxonomy](http://www.w3.org/ns/dcat#themeTaxonomy)
Alias: temaer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrepssamling](begrepssamling.md) |
| Domain Of | [Katalog](katalog.md) |
| Slot URI | [dcat:themeTaxonomy](http://www.w3.org/ns/dcat#themeTaxonomy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:themeTaxonomy |
| native | samtbuskole:temaer |




## LinkML Source

<details>
```yaml
name: temaer
description: Temavokabular som vert brukt i katalogen.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dcat:themeTaxonomy
alias: temaer
domain_of:
- Katalog
range: Begrepssamling
multivalued: true

```
</details>