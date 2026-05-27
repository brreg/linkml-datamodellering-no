

# Slot: har_gebyr 


_Gebyr knytt til tenesta._





URI: [cv:hasCost](http://data.europa.eu/m8g/hasCost)
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
| Range | [Gebyr](gebyr.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
| Slot URI | [cv:hasCost](http://data.europa.eu/m8g/hasCost) |

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
| self | cv:hasCost |
| native | https://data.norge.no/ap-no/cpsv-ap-no/har_gebyr |




## LinkML Source

<details>
```yaml
name: har_gebyr
description: Gebyr knytt til tenesta.
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: cv:hasCost
domain_of:
- OffentligTjeneste
- Tjeneste
range: Gebyr
multivalued: true

```
</details>