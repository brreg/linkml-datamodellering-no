

# Slot: er_del_av_teig 


_Teigen(e) matrikkeleininga er del av._





URI: [ngre:erDelAvTeig](https://data.norge.no/vocabulary/ngr-eiendom#erDelAvTeig)
Alias: er_del_av_teig

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
| Range | [Teig](Teig.md) |
| Domain Of | [Matrikkelenhet](Matrikkelenhet.md) |
| Slot URI | [ngre:erDelAvTeig](https://data.norge.no/vocabulary/ngr-eiendom#erDelAvTeig) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:erDelAvTeig |
| native | https://data.norge.no/linkml/ngr-eiendom/er_del_av_teig |




## LinkML Source

<details>
```yaml
name: er_del_av_teig
description: Teigen(e) matrikkeleininga er del av.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:erDelAvTeig
alias: er_del_av_teig
domain_of:
- Matrikkelenhet
range: Teig
multivalued: true

```
</details>