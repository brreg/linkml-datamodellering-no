

# Slot: malgruppe 


_Målgruppe for tenesta._





URI: [dct:audience](http://purl.org/dc/terms/audience)
Alias: malgruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LovpalagtTjeneste](LovpalagtTjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  yes  |
| [OffentligTjeneste](OffentligTjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](Tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](Konsept.md) |
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md) |
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
alias: malgruppe
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
range: Konsept
multivalued: true

```
</details>