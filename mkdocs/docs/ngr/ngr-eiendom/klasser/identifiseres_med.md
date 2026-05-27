

# Slot: identifiseres_med 


_Matrikkelnummeret som identifiserer matrikkeleininga._





URI: [ngre:identifiseresMed](https://data.norge.no/vocabulary/ngr-eiendom#identifiseresMed)
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
| Range | [Matrikkelnummer](matrikkelnummer.md) |
| Domain Of | [Matrikkelenhet](matrikkelenhet.md) |
| Slot URI | [ngre:identifiseresMed](https://data.norge.no/vocabulary/ngr-eiendom#identifiseresMed) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:identifiseresMed |
| native | https://data.norge.no/ngr/ngr-eiendom/identifiseres_med |




## LinkML Source

<details>
```yaml
name: identifiseres_med
description: Matrikkelnummeret som identifiserer matrikkeleininga.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_uri: ngre:identifiseresMed
domain_of:
- Matrikkelenhet
range: Matrikkelnummer

```
</details>