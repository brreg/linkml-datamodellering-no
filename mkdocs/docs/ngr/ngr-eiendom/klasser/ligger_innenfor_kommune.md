

# Slot: ligger_innenfor_kommune 


_Kommunen matrikkeleininga ligg innanfor._





URI: [ngre:liggerInnenforKommune](https://data.norge.no/vocabulary/ngr-eiendom#liggerInnenforKommune)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelenhet](matrikkelenhet.md) | Abstrakt overklasse for alle typar matrikkeleiningar registrert i Matrikkelen |  yes  |
| [Grunneiendom](grunneiendom.md) | Den vanlegaste typen matrikkelenheit |  no  |
| [Festegrunn](festegrunn.md) | Ein del av ei grunneigendom eller eit jordsameige som nokon har festa til |  no  |
| [Jordsameie](jordsameie.md) | Eit fellesareal som vert eigd av fleire eigedommar |  no  |
| [Eierseksjon](eierseksjon.md) | Ein eigarseksjon er ein eigarandel i ein seksjonert eigedom |  no  |
| [Anleggseiendom](anleggseiendom.md) | Eit volum – ein bygning eller konstruksjon – oppretta frå ei eller fleire gru... |  no  |
| [AnnenMatrikkelenhet](annenmatrikkelenhet.md) | Matrikkelenheit som ikkje fell inn under dei andre underklassane |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kommune](kommune.md) |
| Domain Of | [Matrikkelenhet](matrikkelenhet.md) |
| Slot URI | [ngre:liggerInnenforKommune](https://data.norge.no/vocabulary/ngr-eiendom#liggerInnenforKommune) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:liggerInnenforKommune |
| native | https://data.norge.no/ngr/ngr-eiendom/ligger_innenfor_kommune |




## LinkML Source

<details>
```yaml
name: ligger_innenfor_kommune
description: Kommunen matrikkeleininga ligg innanfor.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_uri: ngre:liggerInnenforKommune
domain_of:
- Matrikkelenhet
range: Kommune

```
</details>