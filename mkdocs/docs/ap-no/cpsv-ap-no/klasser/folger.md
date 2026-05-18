

# Slot: folger 


_Regelverk tenesta følgjer._





URI: [cpsv:follows](http://purl.org/vocab/cpsv#follows)
Alias: folger

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Regel](regel.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
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
| native | https://data.norge.no/linkml/cpsv-ap-no/folger |




## LinkML Source

<details>
```yaml
name: folger
description: Regelverk tenesta følgjer.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cpsv:follows
alias: folger
domain_of:
- OffentligTjeneste
- Tjeneste
range: Regel
multivalued: true

```
</details>