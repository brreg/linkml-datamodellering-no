

# Slot: er_gruppert_av 


_Hending(ar) som grupperer tenesta._





URI: [cv:isGroupedBy](http://data.europa.eu/m8g/isGroupedBy)
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
| Range | [Hendelse](hendelse.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
| Slot URI | [cv:isGroupedBy](http://data.europa.eu/m8g/isGroupedBy) |

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
| self | cv:isGroupedBy |
| native | https://data.norge.no/linkml/cpsv-ap-no/er_gruppert_av |




## LinkML Source

<details>
```yaml
name: er_gruppert_av
description: Hending(ar) som grupperer tenesta.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:isGroupedBy
domain_of:
- OffentligTjeneste
- Tjeneste
range: Hendelse
multivalued: true

```
</details>