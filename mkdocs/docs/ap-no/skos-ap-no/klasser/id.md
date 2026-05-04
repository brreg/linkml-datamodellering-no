

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/skos-ap-no/id](https://data.norge.no/linkml/skos-ap-no/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Begrepssamling](Begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [Samling](Samling.md) | Ei namngitt samling av omgrep (skos:Collection) |  no  |
| [Organisasjon](Organisasjon.md) | Ein organisasjon som er utgjevar eller ansvarleg for eit omgrep |  no  |
| [Spraak](Spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |  no  |
| [Mediatype](Mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [PartitivRelasjon](PartitivRelasjon.md) | Ein partitiv relasjon mellom eit heilskapleg og eit partitivt omgrep |  no  |
| [GeneriskRelasjon](GeneriskRelasjon.md) | Ein generisk relasjon mellom eit overomgrep og eit underomgrep |  no  |
| [Begrep](Begrep.md) | Eit omgrep med definisjon og tilhøyrande metadata (skos:Concept) |  no  |
| [AssosiativRelasjon](AssosiativRelasjon.md) | Ein assosiativ relasjon mellom to omgrep |  no  |
| [Konsept](Konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [VCardKontakt](VCardKontakt.md) | Kontaktinformasjon (vCard) for omgrepseigaren |  no  |
| [Definisjon](Definisjon.md) | Ein definisjon av eit omgrep via eit eige objekt (euvoc:XlNote) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Organisasjon](Organisasjon.md), [VCardKontakt](VCardKontakt.md), [Begrep](Begrep.md), [Definisjon](Definisjon.md), [AssosiativRelasjon](AssosiativRelasjon.md), [GeneriskRelasjon](GeneriskRelasjon.md), [PartitivRelasjon](PartitivRelasjon.md), [Samling](Samling.md), [Spraak](Spraak.md), [Mediatype](Mediatype.md), [Konsept](Konsept.md), [Begrepssamling](Begrepssamling.md) |

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


* from schema: https://data.norge.no/linkml/skos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/skos-ap-no/id |
| native | https://data.norge.no/linkml/skos-ap-no/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/skos-ap-no
rank: 1000
identifier: true
alias: id
domain_of:
- Organisasjon
- VCardKontakt
- Begrep
- Definisjon
- AssosiativRelasjon
- GeneriskRelasjon
- PartitivRelasjon
- Samling
- Spraak
- Mediatype
- Konsept
- Begrepssamling
range: uriorcurie
required: true

```
</details>