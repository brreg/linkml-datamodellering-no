

# Slot: mogleg_spraak 


_Mogleg språk for tenesteresultatet._





URI: [cpsvno:possibleLanguage](https://data.norge.no/vocabulary/cpsvno#possibleLanguage)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjenesteresultattype](tjenesteresultattype.md) | Typen resultat som ei teneste produserer |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Spraak](spraak.md) |
| Domain Of | [Tjenesteresultattype](tjenesteresultattype.md) |
| Slot URI | [cpsvno:possibleLanguage](https://data.norge.no/vocabulary/cpsvno#possibleLanguage) |

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
| self | cpsvno:possibleLanguage |
| native | https://data.norge.no/linkml/cpsv-ap-no/mogleg_spraak |




## LinkML Source

<details>
```yaml
name: mogleg_spraak
description: Mogleg språk for tenesteresultatet.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cpsvno:possibleLanguage
domain_of:
- Tjenesteresultattype
range: Spraak
multivalued: true

```
</details>