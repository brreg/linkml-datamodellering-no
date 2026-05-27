

# Slot: sektor 


_Industri/sektor tenesta tilhøyrer._





URI: [cv:sector](http://data.europa.eu/m8g/sector)
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
| Slot URI | [cv:sector](http://data.europa.eu/m8g/sector) |

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
| self | cv:sector |
| native | https://data.norge.no/ap-no/cpsv-ap-no/sektor |




## LinkML Source

<details>
```yaml
name: sektor
description: Industri/sektor tenesta tilhøyrer.
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: cv:sector
domain_of:
- OffentligTjeneste
- Tjeneste
range: Konsept
multivalued: true

```
</details>