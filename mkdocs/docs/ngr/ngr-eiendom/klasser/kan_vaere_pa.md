

# Slot: kan_vaere_pa 


_Matrikkeleininga denne eininga ligg på eller er knytt til. Festegrunn kan liggje på grunneigendom eller jordsameige; eigarseksjon kan liggje på grunneigendom, festegrunn eller anleggseigendom._





URI: [ngre:kanVaerePa](https://data.norge.no/vocabulary/ngr-eiendom#kanVaerePa)
Alias: kan_vaere_pa

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eierseksjon](Eierseksjon.md) | Ein eigarseksjon er ein eigarandel i ein seksjonert eigedom |  yes  |
| [Festegrunn](Festegrunn.md) | Ein del av ei grunneigendom eller eit jordsameige som nokon har festa til |  yes  |
| [Grunneiendom](Grunneiendom.md) | Den vanlegaste typen matrikkelenheit |  yes  |
| [Jordsameie](Jordsameie.md) | Eit fellesareal som vert eigd av fleire eigedommar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Matrikkelenhet](Matrikkelenhet.md) |
| Domain Of | [Grunneiendom](Grunneiendom.md), [Festegrunn](Festegrunn.md), [Jordsameie](Jordsameie.md), [Eierseksjon](Eierseksjon.md) |
| Slot URI | [ngre:kanVaerePa](https://data.norge.no/vocabulary/ngr-eiendom#kanVaerePa) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:kanVaerePa |
| native | https://data.norge.no/linkml/ngr-eiendom/kan_vaere_pa |




## LinkML Source

<details>
```yaml
name: kan_vaere_pa
description: Matrikkeleininga denne eininga ligg på eller er knytt til. Festegrunn
  kan liggje på grunneigendom eller jordsameige; eigarseksjon kan liggje på grunneigendom,
  festegrunn eller anleggseigendom.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:kanVaerePa
alias: kan_vaere_pa
domain_of:
- Grunneiendom
- Festegrunn
- Jordsameie
- Eierseksjon
range: Matrikkelenhet

```
</details>