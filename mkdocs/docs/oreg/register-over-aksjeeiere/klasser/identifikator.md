

# Slot: identifikator 


_Global identifikator for instansen._





URI: [aksje:identifikator](https://example.no/ontology/aksje#identifikator)
Alias: identifikator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vederlag](Vederlag.md) | Vederlag knytt til ei aksjeoverdraging |  no  |
| [Containerklasse](Containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |
| [Aksjekapital](Aksjekapital.md) | Den registrerte aksjekapitalen i eit aksjeselskap |  no  |
| [Utbytte](Utbytte.md) | Utbytte knytt til ein eigarposisjon |  no  |
| [Aksjeinnskudd](Aksjeinnskudd.md) | Innskot knytt til aksjar i samband med selskapshending |  no  |
| [Utdeling](Utdeling.md) | Konkret utdeling av verdiar til aksjeeigarar |  no  |
| [Aksjeeier](Aksjeeier.md) | Person eller organisasjon som eig aksjar |  no  |
| [Aksjeselskap](Aksjeselskap.md) | Selskap som utsteder aksjar og har aksjekapital |  no  |
| [Aksjepost](Aksjepost.md) | Samling aksjar eigd av ein aksjeeigar |  no  |
| [Eierposisjon](Eierposisjon.md) | Eierens samla posisjon i eit selskap |  no  |
| [Aksje](Aksje.md) | Ei enkelt aksje utstedt av eit aksjeselskap |  no  |
| [Selskapshendelse](Selskapshendelse.md) | Hending som påverkar selskapet sitt eigarskap eller kapital |  no  |
| [Eierskapstransaksjon](Eierskapstransaksjon.md) | Transaksjon som påverkar eigarskap i selskapet |  no  |
| [Aksjeklasse](Aksjeklasse.md) | Klasse aksjar høyrer til, med eigne rettigheiter |  no  |
| [Aksjeeierrettighet](Aksjeeierrettighet.md) | Rettigheiter knytt til aksjar, til dømes stemmerett |  no  |
| [Aksjeoverdragelse](Aksjeoverdragelse.md) | Overdraging av aksjar mellom partar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Containerklasse](Containerklasse.md), [Aksjeselskap](Aksjeselskap.md), [Aksjekapital](Aksjekapital.md), [Aksje](Aksje.md), [Aksjeklasse](Aksjeklasse.md), [Aksjeeierrettighet](Aksjeeierrettighet.md), [Aksjeeier](Aksjeeier.md), [Eierposisjon](Eierposisjon.md), [Aksjepost](Aksjepost.md), [Utbytte](Utbytte.md), [Utdeling](Utdeling.md), [Eierskapstransaksjon](Eierskapstransaksjon.md), [Aksjeoverdragelse](Aksjeoverdragelse.md), [Vederlag](Vederlag.md), [Selskapshendelse](Selskapshendelse.md), [Aksjeinnskudd](Aksjeinnskudd.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aksje:identifikator |
| native | aksje:identifikator |




## LinkML Source

<details>
```yaml
name: identifikator
description: Global identifikator for instansen.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
identifier: true
alias: identifikator
domain_of:
- Containerklasse
- Aksjeselskap
- Aksjekapital
- Aksje
- Aksjeklasse
- Aksjeeierrettighet
- Aksjeeier
- Eierposisjon
- Aksjepost
- Utbytte
- Utdeling
- Eierskapstransaksjon
- Aksjeoverdragelse
- Vederlag
- Selskapshendelse
- Aksjeinnskudd
range: uriorcurie
required: true

```
</details>