

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/common-ap-no/id](https://data.norge.no/linkml/common-ap-no/id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [Organisasjon](organisasjon.md) | Ein organisasjon som er utgjevar eller ansvarleg for eit omgrep |  no  |
| [VCardKontakt](vcardkontakt.md) | Kontaktinformasjon (vCard) for omgrepseigaren |  no  |
| [Begrep](begrep.md) | Eit omgrep med definisjon og tilhøyrande metadata (skos:Concept) |  no  |
| [Definisjon](definisjon.md) | Ein definisjon av eit omgrep via eit eige objekt (euvoc:XlNote) |  no  |
| [AssosiativRelasjon](assosiativrelasjon.md) | Ein assosiativ relasjon mellom to omgrep |  no  |
| [GeneriskRelasjon](generiskrelasjon.md) | Ein generisk relasjon mellom eit overomgrep og eit underomgrep |  no  |
| [PartitivRelasjon](partitivrelasjon.md) | Ein partitiv relasjon mellom eit heilskapleg og eit partitivt omgrep |  no  |
| [Samling](samling.md) | Ei namngitt samling av omgrep (skos:Collection) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Mediatype](mediatype.md), [Konsept](konsept.md), [Begrepssamling](begrepssamling.md), [Organisasjon](organisasjon.md), [VCardKontakt](vcardkontakt.md), [Begrep](begrep.md), [Definisjon](definisjon.md), [AssosiativRelasjon](assosiativrelasjon.md), [GeneriskRelasjon](generiskrelasjon.md), [PartitivRelasjon](partitivrelasjon.md), [Samling](samling.md) |

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


* from schema: https://data.norge.no/linkml/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/common-ap-no/id |
| native | https://data.norge.no/linkml/common-ap-no/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/common-ap-no
identifier: true
domain_of:
- Mediatype
- Konsept
- Begrepssamling
- Organisasjon
- VCardKontakt
- Begrep
- Definisjon
- AssosiativRelasjon
- GeneriskRelasjon
- PartitivRelasjon
- Samling
range: uriorcurie
required: true

```
</details>