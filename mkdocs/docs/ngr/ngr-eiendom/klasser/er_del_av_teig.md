

# Slot: er_del_av_teig 


_Teigen(e) matrikkeleininga er del av._





URI: [ngre:erDelAvTeig](https://data.norge.no/vocabulary/ngr-eiendom#erDelAvTeig)
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
| Range | [Teig](teig.md) |
| Domain Of | [Matrikkelenhet](matrikkelenhet.md) |
| Slot URI | [ngre:erDelAvTeig](https://data.norge.no/vocabulary/ngr-eiendom#erDelAvTeig) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:erDelAvTeig |
| native | https://data.norge.no/ngr/ngr-eiendom/er_del_av_teig |




## LinkML Source

<details>
```yaml
name: er_del_av_teig
description: Teigen(e) matrikkeleininga er del av.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_uri: ngre:erDelAvTeig
domain_of:
- Matrikkelenhet
range: Teig
multivalued: true

```
</details>