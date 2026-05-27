

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/ap-no/common-ap-no/id](https://data.norge.no/ap-no/common-ap-no/id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [Klassifikasjon](klassifikasjon.md) | Ei klassifikasjon – ein systematisk struktur av kategoriar brukt til å klassi... |  no  |
| [Klassifikasjonsnivaa](klassifikasjonsnivaa.md) | Eit nivå i ein klassifikasjon (xkos:ClassificationLevel) |  no  |
| [Kategori](kategori.md) | Ein kategori i ein klassifikasjon (skos:Concept) |  no  |
| [Klassifikasjonssamanlikning](klassifikasjonssamanlikning.md) | Ein samanlikning mellom to klassifikasjonar (xkos:Correspondence) |  no  |
| [Kategorisamanlikning](kategorisamanlikning.md) | Ein samanlikning mellom to kategoriar på tvers av klassifikasjonar (xkos:Conc... |  no  |
| [Organisasjon](organisasjon.md) | Ein organisasjon eller aktør (foaf:Agent) |  no  |
| [Tidsrom](tidsrom.md) | Eit tidsrom med start- og/eller sluttdato (dct:PeriodOfTime) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Mediatype](mediatype.md), [Konsept](konsept.md), [Begrepssamling](begrepssamling.md), [Klassifikasjon](klassifikasjon.md), [Klassifikasjonsnivaa](klassifikasjonsnivaa.md), [Kategori](kategori.md), [Klassifikasjonssamanlikning](klassifikasjonssamanlikning.md), [Kategorisamanlikning](kategorisamanlikning.md), [Organisasjon](organisasjon.md), [Tidsrom](tidsrom.md) |

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


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/ap-no/common-ap-no/id |
| native | https://data.norge.no/ap-no/common-ap-no/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/ap-no/common-ap-no
identifier: true
domain_of:
- Mediatype
- Konsept
- Begrepssamling
- Klassifikasjon
- Klassifikasjonsnivaa
- Kategori
- Klassifikasjonssamanlikning
- Kategorisamanlikning
- Organisasjon
- Tidsrom
range: uriorcurie
required: true

```
</details>