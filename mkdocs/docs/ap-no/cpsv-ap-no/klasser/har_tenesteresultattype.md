

# Slot: har_tenesteresultattype 


_Typen resultat tenesta kan produsere._





URI: [cpsvno:hasOutputType](https://data.norge.no/vocabulary/cpsvno#hasOutputType)
Alias: har_tenesteresultattype

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
| Range | [Tjenesteresultattype](Tjenesteresultattype.md) |
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md) |
| Slot URI | [cpsvno:hasOutputType](https://data.norge.no/vocabulary/cpsvno#hasOutputType) |

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
| self | cpsvno:hasOutputType |
| native | https://data.norge.no/linkml/cpsv-ap-no/har_tenesteresultattype |




## LinkML Source

<details>
```yaml
name: har_tenesteresultattype
description: Typen resultat tenesta kan produsere.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cpsvno:hasOutputType
alias: har_tenesteresultattype
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
range: Tjenesteresultattype
multivalued: true

```
</details>