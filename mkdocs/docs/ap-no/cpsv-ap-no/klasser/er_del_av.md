

# Slot: er_del_av 


_Tenesta er del av ei anna teneste._





URI: [dct:isPartOf](http://purl.org/dc/terms/isPartOf)
Alias: er_del_av

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
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md) |
| Slot URI | [dct:isPartOf](http://purl.org/dc/terms/isPartOf) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:isPartOf |
| native | https://data.norge.no/linkml/cpsv-ap-no/er_del_av |




## LinkML Source

<details>
```yaml
name: er_del_av
description: Tenesta er del av ei anna teneste.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dct:isPartOf
alias: er_del_av
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
range: uriorcurie

```
</details>