

# Slot: har_teig 


_Teigen(e) som tilhøyrer matrikkeleininga._





URI: [ngre:harTeig](https://data.norge.no/vocabulary/ngr-eiendom#harTeig)
Alias: har_teig

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
| Slot URI | [ngre:harTeig](https://data.norge.no/vocabulary/ngr-eiendom#harTeig) |

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
| self | ngre:harTeig |
| native | https://data.norge.no/linkml/ngr-eiendom/har_teig |




## LinkML Source

<details>
```yaml
name: har_teig
description: Teigen(e) som tilhøyrer matrikkeleininga.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:harTeig
alias: har_teig
domain_of:
- Matrikkelenhet
range: Teig
multivalued: true

```
</details>