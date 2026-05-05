

# Slot: tilhorande_klassifikasjonsnivaa 


_Klassifikasjonsnivå kategorien høyrer til (xkos:belongsTo)._





URI: [xkos:belongsTo](http://rdf-vocabulary.ddialliance.org/xkos#belongsTo)
Alias: tilhorande_klassifikasjonsnivaa

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kategori](kategori.md) | Ein kategori i ein klassifikasjon (skos:Concept) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Klassifikasjonsnivaa](klassifikasjonsnivaa.md) |
| Domain Of | [Kategori](kategori.md) |
| Slot URI | [xkos:belongsTo](http://rdf-vocabulary.ddialliance.org/xkos#belongsTo) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/xkos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | xkos:belongsTo |
| native | https://data.norge.no/linkml/xkos-ap-no/tilhorande_klassifikasjonsnivaa |




## LinkML Source

<details>
```yaml
name: tilhorande_klassifikasjonsnivaa
description: Klassifikasjonsnivå kategorien høyrer til (xkos:belongsTo).
from_schema: https://data.norge.no/linkml/xkos-ap-no
rank: 1000
slot_uri: xkos:belongsTo
alias: tilhorande_klassifikasjonsnivaa
domain_of:
- Kategori
range: Klassifikasjonsnivaa

```
</details>