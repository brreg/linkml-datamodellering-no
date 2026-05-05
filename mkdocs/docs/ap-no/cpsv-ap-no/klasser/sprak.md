

# Slot: sprak 


_Språk brukt i ressursen (dct:language)._





URI: [dct:language](http://purl.org/dc/terms/language)
Alias: sprak

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktpunkt](kontaktpunkt.md) | Kontaktinformasjon for ei teneste eller ein organisasjon |  yes  |
| [Katalog](katalog.md) | Ein katalog over offentlege tenester og hendingar |  yes  |
| [Regel](regel.md) | Eit regelverk eller retningsliner som styrer levering av ei teneste |  yes  |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Spraak](spraak.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md), [Kontaktpunkt](kontaktpunkt.md), [Regel](regel.md), [Katalog](katalog.md) |
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