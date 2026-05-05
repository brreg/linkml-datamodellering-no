

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/xkos-ap-no/id](https://data.norge.no/linkml/xkos-ap-no/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Spraak](spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |  no  |
| [Klassifikasjonsnivaa](klassifikasjonsnivaa.md) | Eit nivå i ein klassifikasjon (xkos:ClassificationLevel) |  no  |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [Organisasjon](organisasjon.md) | Ein organisasjon eller aktør (foaf:Agent) |  no  |
| [Kategori](kategori.md) | Ein kategori i ein klassifikasjon (skos:Concept) |  no  |
| [Klassifikasjon](klassifikasjon.md) | Ei klassifikasjon – ein systematisk struktur av kategoriar brukt til å klassi... |  no  |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [Tidsrom](tidsrom.md) | Eit tidsrom med start- og/eller sluttdato (dct:PeriodOfTime) |  no  |
| [Klassifikasjonssamanlikning](klassifikasjonssamanlikning.md) | Ein samanlikning mellom to klassifikasjonar (xkos:Correspondence) |  no  |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [Kategorisamanlikning](kategorisamanlikning.md) | Ein samanlikning mellom to kategoriar på tvers av klassifikasjonar (xkos:Conc... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Klassifikasjon](klassifikasjon.md), [Klassifikasjonsnivaa](klassifikasjonsnivaa.md), [Kategori](kategori.md), [Klassifikasjonssamanlikning](klassifikasjonssamanlikning.md), [Kategorisamanlikning](kategorisamanlikning.md), [Organisasjon](organisasjon.md), [Tidsrom](tidsrom.md), [Spraak](spraak.md), [Mediatype](mediatype.md), [Konsept](konsept.md), [Begrepssamling](begrepssamling.md) |

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