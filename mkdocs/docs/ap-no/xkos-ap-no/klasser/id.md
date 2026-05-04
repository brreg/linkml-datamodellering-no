

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/xkos-ap-no/id](https://data.norge.no/linkml/xkos-ap-no/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kategori](Kategori.md) | Ein kategori i ein klassifikasjon (skos:Concept) |  no  |
| [Konsept](Konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [Klassifikasjonsnivaa](Klassifikasjonsnivaa.md) | Eit nivå i ein klassifikasjon (xkos:ClassificationLevel) |  no  |
| [Kategorisamanlikning](Kategorisamanlikning.md) | Ein samanlikning mellom to kategoriar på tvers av klassifikasjonar (xkos:Conc... |  no  |
| [Begrepssamling](Begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [Spraak](Spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |  no  |
| [Mediatype](Mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [Organisasjon](Organisasjon.md) | Ein organisasjon eller aktør (foaf:Agent) |  no  |
| [Klassifikasjonssamanlikning](Klassifikasjonssamanlikning.md) | Ein samanlikning mellom to klassifikasjonar (xkos:Correspondence) |  no  |
| [Tidsrom](Tidsrom.md) | Eit tidsrom med start- og/eller sluttdato (dct:PeriodOfTime) |  no  |
| [Klassifikasjon](Klassifikasjon.md) | Ei klassifikasjon – ein systematisk struktur av kategoriar brukt til å klassi... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Klassifikasjon](Klassifikasjon.md), [Klassifikasjonsnivaa](Klassifikasjonsnivaa.md), [Kategori](Kategori.md), [Klassifikasjonssamanlikning](Klassifikasjonssamanlikning.md), [Kategorisamanlikning](Kategorisamanlikning.md), [Organisasjon](Organisasjon.md), [Tidsrom](Tidsrom.md), [Spraak](Spraak.md), [Mediatype](Mediatype.md), [Konsept](Konsept.md), [Begrepssamling](Begrepssamling.md) |

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


* from schema: https://data.norge.no/linkml/xkos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/xkos-ap-no/id |
| native | https://data.norge.no/linkml/xkos-ap-no/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/xkos-ap-no
rank: 1000
identifier: true
alias: id
domain_of:
- Klassifikasjon
- Klassifikasjonsnivaa
- Kategori
- Klassifikasjonssamanlikning
- Kategorisamanlikning
- Organisasjon
- Tidsrom
- Spraak
- Mediatype
- Konsept
- Begrepssamling
range: uriorcurie
required: true

```
</details>