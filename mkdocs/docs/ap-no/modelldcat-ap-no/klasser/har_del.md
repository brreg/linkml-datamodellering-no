

# Slot: har_del 


_Del-ressurs inkludert i denne katalogen (dct:hasPart)._





URI: [dct:hasPart](http://purl.org/dc/terms/hasPart)
Alias: har_del

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Modelkatalog](Modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [KatalogisertRessurs](KatalogisertRessurs.md) |
| Domain Of | [Modelkatalog](Modelkatalog.md) |
| Slot URI | [dct:hasPart](http://purl.org/dc/terms/hasPart) |

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
| self | dct:hasPart |
| native | https://data.norge.no/linkml/modelldcat-ap-no/har_del |




## LinkML Source

<details>
```yaml
name: har_del
description: Del-ressurs inkludert i denne katalogen (dct:hasPart).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dct:hasPart
alias: har_del
domain_of:
- Modelkatalog
range: KatalogisertRessurs
multivalued: true

```
</details>