

# Slot: malgruppe 


_Målgruppe for tenesta._





URI: [dct:audience](http://purl.org/dc/terms/audience)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
| Slot URI | [dct:audience](http://purl.org/dc/terms/audience) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:audience |
| native | https://data.norge.no/linkml/cpsv-ap-no/malgruppe |




## LinkML Source

<details>
```yaml
name: malgruppe
description: Målgruppe for tenesta.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dct:audience
domain_of:
- OffentligTjeneste
- Tjeneste
range: Konsept
multivalued: true

```
</details>