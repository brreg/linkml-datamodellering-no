

# Slot: sektor 


_Industri/sektor tenesta tilhøyrer._





URI: [cv:sector](http://data.europa.eu/m8g/sector)
Alias: sektor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LovpalagtTjeneste](LovpalagtTjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  yes  |
| [OffentligTjeneste](OffentligTjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](Tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](Konsept.md) |
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md) |
| Slot URI | [cv:sector](http://data.europa.eu/m8g/sector) |

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
| self | cv:sector |
| native | https://data.norge.no/linkml/cpsv-ap-no/sektor |




## LinkML Source

<details>
```yaml
name: sektor
description: Industri/sektor tenesta tilhøyrer.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:sector
alias: sektor
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
range: Konsept
multivalued: true

```
</details>