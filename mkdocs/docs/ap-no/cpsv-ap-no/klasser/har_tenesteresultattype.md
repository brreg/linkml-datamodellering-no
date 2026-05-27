

# Slot: har_tenesteresultattype 


_Typen resultat tenesta kan produsere._





URI: [cpsvno:hasOutputType](https://data.norge.no/vocabulary/cpsvno#hasOutputType)
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
| Range | [Tjenesteresultattype](tjenesteresultattype.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
| Slot URI | [cpsvno:hasOutputType](https://data.norge.no/vocabulary/cpsvno#hasOutputType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cpsvno:hasOutputType |
| native | https://data.norge.no/ap-no/cpsv-ap-no/har_tenesteresultattype |




## LinkML Source

<details>
```yaml
name: har_tenesteresultattype
description: Typen resultat tenesta kan produsere.
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: cpsvno:hasOutputType
domain_of:
- OffentligTjeneste
- Tjeneste
range: Tjenesteresultattype
multivalued: true

```
</details>