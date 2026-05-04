

# Slot: nokkelord 


_Nøkkelord som beskriv ressursen (dcat:keyword)._





URI: [dcat:keyword](http://www.w3.org/ns/dcat#keyword)
Alias: nokkelord

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
| Range | [LangString](LangString.md) |
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md) |
| Slot URI | [dcat:keyword](http://www.w3.org/ns/dcat#keyword) |

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
| self | dcat:keyword |
| native | https://data.norge.no/linkml/cpsv-ap-no/nokkelord |




## LinkML Source

<details>
```yaml
name: nokkelord
description: Nøkkelord som beskriv ressursen (dcat:keyword).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dcat:keyword
alias: nokkelord
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
range: LangString
multivalued: true

```
</details>