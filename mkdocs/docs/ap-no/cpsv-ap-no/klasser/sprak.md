

# Slot: sprak 


_Språk brukt i ressursen (dct:language)._





URI: [dct:language](http://purl.org/dc/terms/language)
Alias: sprak

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Regel](Regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |  yes  |
| [Katalog](Katalog.md) | Ein katalog over offentlege tenester og hendingar |  yes  |
| [OffentligTjeneste](OffentligTjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Kontaktpunkt](Kontaktpunkt.md) | Kontaktinformasjon for ei teneste eller ein organisasjon |  yes  |
| [Tjeneste](Tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Spraak](Spraak.md) |
| Domain Of | [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md), [Kontaktpunkt](Kontaktpunkt.md), [Regel](Regel.md), [Katalog](Katalog.md) |
| Slot URI | [dct:language](http://purl.org/dc/terms/language) |

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
| self | dct:language |
| native | https://data.norge.no/linkml/cpsv-ap-no/sprak |




## LinkML Source

<details>
```yaml
name: sprak
description: Språk brukt i ressursen (dct:language).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dct:language
alias: sprak
domain_of:
- OffentligTjeneste
- Tjeneste
- Kontaktpunkt
- Regel
- Katalog
range: Spraak
multivalued: true

```
</details>