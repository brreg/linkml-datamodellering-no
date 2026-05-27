

# Slot: kan_vaere_pa 


_Matrikkeleininga denne eininga ligg på eller er knytt til. Festegrunn kan liggje på grunneigendom eller jordsameige; eigarseksjon kan liggje på grunneigendom, festegrunn eller anleggseigendom._





URI: [ngre:kanVaerePa](https://data.norge.no/vocabulary/ngr-eiendom#kanVaerePa)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Grunneiendom](grunneiendom.md) | Den vanlegaste typen matrikkelenheit |  yes  |
| [Festegrunn](festegrunn.md) | Ein del av ei grunneigendom eller eit jordsameige som nokon har festa til |  yes  |
| [Jordsameie](jordsameie.md) | Eit fellesareal som vert eigd av fleire eigedommar |  yes  |
| [Eierseksjon](eierseksjon.md) | Ein eigarseksjon er ein eigarandel i ein seksjonert eigedom |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Matrikkelenhet](matrikkelenhet.md) |
| Domain Of | [Grunneiendom](grunneiendom.md), [Festegrunn](festegrunn.md), [Jordsameie](jordsameie.md), [Eierseksjon](eierseksjon.md) |
| Slot URI | [ngre:kanVaerePa](https://data.norge.no/vocabulary/ngr-eiendom#kanVaerePa) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:kanVaerePa |
| native | https://data.norge.no/ngr/ngr-eiendom/kan_vaere_pa |




## LinkML Source

<details>
```yaml
name: kan_vaere_pa
description: Matrikkeleininga denne eininga ligg på eller er knytt til. Festegrunn
  kan liggje på grunneigendom eller jordsameige; eigarseksjon kan liggje på grunneigendom,
  festegrunn eller anleggseigendom.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_uri: ngre:kanVaerePa
domain_of:
- Grunneiendom
- Festegrunn
- Jordsameie
- Eierseksjon
range: Matrikkelenhet

```
</details>