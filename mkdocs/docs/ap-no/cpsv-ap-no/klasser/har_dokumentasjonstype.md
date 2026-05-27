

# Slot: har_dokumentasjonstype 


_Dokumentasjon som krevst for tenesta._





URI: [cv:hasInputType](http://data.europa.eu/m8g/hasInputType)
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
| Range | [Dokumentasjonstype](dokumentasjonstype.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
| Slot URI | [cv:hasInputType](http://data.europa.eu/m8g/hasInputType) |

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
| self | cv:hasInputType |
| native | https://data.norge.no/ap-no/cpsv-ap-no/har_dokumentasjonstype |




## LinkML Source

<details>
```yaml
name: har_dokumentasjonstype
description: Dokumentasjon som krevst for tenesta.
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: cv:hasInputType
domain_of:
- OffentligTjeneste
- Tjeneste
range: Dokumentasjonstype
multivalued: true

```
</details>