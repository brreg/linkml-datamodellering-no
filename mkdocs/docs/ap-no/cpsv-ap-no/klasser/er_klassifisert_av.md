

# Slot: er_klassifisert_av 


_Omgrep tenesta er klassifisert med._





URI: [cv:isClassifiedBy](http://data.europa.eu/m8g/isClassifiedBy)
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
| Slot URI | [cv:isClassifiedBy](http://data.europa.eu/m8g/isClassifiedBy) |

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
| self | cv:isClassifiedBy |
| native | https://data.norge.no/ap-no/cpsv-ap-no/er_klassifisert_av |




## LinkML Source

<details>
```yaml
name: er_klassifisert_av
description: Omgrep tenesta er klassifisert med.
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: cv:isClassifiedBy
domain_of:
- OffentligTjeneste
- Tjeneste
range: Konsept
multivalued: true

```
</details>