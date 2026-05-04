

# Slot: ligger_innenfor_kommune 


_Kommunen matrikkeleininga ligg innanfor._





URI: [ngre:liggerInnenforKommune](https://data.norge.no/vocabulary/ngr-eiendom#liggerInnenforKommune)
Alias: ligger_innenfor_kommune

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Anleggseiendom](Anleggseiendom.md) | Eit volum – ein bygning eller konstruksjon – oppretta frå ei eller fleire gru... |  no  |
| [Eierseksjon](Eierseksjon.md) | Ein eigarseksjon er ein eigarandel i ein seksjonert eigedom |  no  |
| [Festegrunn](Festegrunn.md) | Ein del av ei grunneigendom eller eit jordsameige som nokon har festa til |  no  |
| [Matrikkelenhet](Matrikkelenhet.md) | Abstrakt overklasse for alle typar matrikkeleiningar registrert i Matrikkelen |  yes  |
| [AnnenMatrikkelenhet](AnnenMatrikkelenhet.md) | Matrikkelenheit som ikkje fell inn under dei andre underklassane |  no  |
| [Jordsameie](Jordsameie.md) | Eit fellesareal som vert eigd av fleire eigedommar |  no  |
| [Grunneiendom](Grunneiendom.md) | Den vanlegaste typen matrikkelenheit |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kommune](Kommune.md) |
| Domain Of | [Matrikkelenhet](Matrikkelenhet.md) |
| Slot URI | [ngre:liggerInnenforKommune](https://data.norge.no/vocabulary/ngr-eiendom#liggerInnenforKommune) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:liggerInnenforKommune |
| native | https://data.norge.no/linkml/ngr-eiendom/ligger_innenfor_kommune |




## LinkML Source

<details>
```yaml
name: ligger_innenfor_kommune
description: Kommunen matrikkeleininga ligg innanfor.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:liggerInnenforKommune
alias: ligger_innenfor_kommune
domain_of:
- Matrikkelenhet
range: Kommune

```
</details>