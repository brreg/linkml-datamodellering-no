

# Slot: følgjer 


_Regelverk tenesta følgjer._





URI: [cpsv:follows](http://purl.org/vocab/cpsv#follows)
Alias: følgjer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffentligTjeneste](OffentligTjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](Tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |
| [LovpalagtTjeneste](LovpalagtTjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Regel](Regel.md) |
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md) |
| Slot URI | [cpsv:follows](http://purl.org/vocab/cpsv#follows) |

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
| self | cpsv:follows |
| native | https://data.norge.no/linkml/cpsv-ap-no/følgjer |




## LinkML Source

<details>
```yaml
name: følgjer
description: Regelverk tenesta følgjer.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cpsv:follows
alias: følgjer
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
range: Regel
multivalued: true

```
</details>