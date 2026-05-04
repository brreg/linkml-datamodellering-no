

# Slot: krev 


_Teneste eller ressurs denne tenesta krev._





URI: [dct:requires](http://purl.org/dc/terms/requires)
Alias: krev

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
| Slot URI | [dct:requires](http://purl.org/dc/terms/requires) |

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
| self | dct:requires |
| native | https://data.norge.no/linkml/cpsv-ap-no/krev |




## LinkML Source

<details>
```yaml
name: krev
description: Teneste eller ressurs denne tenesta krev.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dct:requires
alias: krev
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
range: uriorcurie
multivalued: true

```
</details>