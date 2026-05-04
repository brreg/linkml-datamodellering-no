

# Slot: mogleg_sprak 


_Mogleg språk for tenesteresultatet._





URI: [cpsvno:possibleLanguage](https://data.norge.no/vocabulary/cpsvno#possibleLanguage)
Alias: mogleg_sprak

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjenesteresultattype](Tjenesteresultattype.md) | Typen resultat som ei teneste produserer |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Spraak](Spraak.md) |
| Domain Of | [Tjenesteresultattype](Tjenesteresultattype.md) |
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
| native | https://data.norge.no/linkml/cpsv-ap-no/mogleg_sprak |




## LinkML Source

<details>
```yaml
name: mogleg_sprak
description: Mogleg språk for tenesteresultatet.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cpsvno:possibleLanguage
alias: mogleg_sprak
domain_of:
- Tjenesteresultattype
range: Spraak
multivalued: true

```
</details>