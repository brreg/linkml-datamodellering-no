

# Slot: identifiseres_med 


_Matrikkelnummeret som identifiserer matrikkeleininga._





URI: [ngre:identifiseresMed](https://data.norge.no/vocabulary/ngr-eiendom#identifiseresMed)
Alias: identifiseres_med

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
| Range | [Matrikkelnummer](Matrikkelnummer.md) |
| Domain Of | [Matrikkelenhet](Matrikkelenhet.md) |
| Slot URI | [ngre:identifiseresMed](https://data.norge.no/vocabulary/ngr-eiendom#identifiseresMed) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:identifiseresMed |
| native | https://data.norge.no/linkml/ngr-eiendom/identifiseres_med |




## LinkML Source

<details>
```yaml
name: identifiseres_med
description: Matrikkelnummeret som identifiserer matrikkeleininga.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:identifiseresMed
alias: identifiseres_med
domain_of:
- Matrikkelenhet
range: Matrikkelnummer

```
</details>