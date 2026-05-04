

# Slot: har_del 


_Deltenester som inngår i denne tenesta._





URI: [dct:hasPart](http://purl.org/dc/terms/hasPart)
Alias: har_del

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
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md) |
| Slot URI | [dct:hasPart](http://purl.org/dc/terms/hasPart) |

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
| self | dct:hasPart |
| native | https://data.norge.no/linkml/cpsv-ap-no/har_del |




## LinkML Source

<details>
```yaml
name: har_del
description: Deltenester som inngår i denne tenesta.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dct:hasPart
alias: har_del
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
range: uriorcurie
multivalued: true

```
</details>