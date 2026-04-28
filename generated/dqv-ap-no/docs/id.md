

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/dqv-ap-no/id](https://data.norge.no/linkml/dqv-ap-no/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kvalitetsdeldimensjon](Kvalitetsdeldimensjon.md) | Ein deldimensjon av ein kvalitetsdimensjon |  no  |
| [Standard](Standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |  no  |
| [Kvalitetsmerknad](Kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |  no  |
| [Brukartilbakemelding](Brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |  no  |
| [Kvalitetssertifikat](Kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |  no  |
| [DcatRessurs](DcatRessurs.md) | Ein katalogisert ressurs (brukt som målklasse for oa:hasTarget) |  no  |
| [Kvalitetsmaal](Kvalitetsmaal.md) | Eit kvalitetsmål som operasjonaliserer ein kvalitetsdeldimensjon |  no  |
| [Begrep](Begrep.md) | Eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [Begrepssamling](Begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [Datasett](Datasett.md) | Eit datasett (dcat:Dataset) utvida med DQV-AP-NO-eigenskapar for kvalitetsinf... |  no  |
| [Mediatype](Mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [Spraak](Spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |  no  |
| [Kvalitetsdimensjon](Kvalitetsdimensjon.md) | Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål |  no  |
| [Motivasjon](Motivasjon.md) | Motivasjonen bak ein kvalitetsmerknad (Web Annotation) |  no  |
| [Kvalitetsmaaling](Kvalitetsmaaling.md) | Ei konkret måling av eit kvalitetsmål for eit datasett |  no  |
| [Tekstdel](Tekstdel.md) | Ein tekstleg del av ein kvalitetsmerknad (Web Annotation) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [DcatRessurs](DcatRessurs.md), [Datasett](Datasett.md), [Kvalitetsdimensjon](Kvalitetsdimensjon.md), [Kvalitetsmaal](Kvalitetsmaal.md), [Kvalitetsmerknad](Kvalitetsmerknad.md), [Kvalitetsmaaling](Kvalitetsmaaling.md), [Standard](Standard.md), [Tekstdel](Tekstdel.md), [Motivasjon](Motivasjon.md), [Spraak](Spraak.md), [Mediatype](Mediatype.md), [Begrep](Begrep.md), [Begrepssamling](Begrepssamling.md) |

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


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/dqv-ap-no/id |
| native | https://data.norge.no/linkml/dqv-ap-no/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/dqv-ap-no
rank: 1000
identifier: true
alias: id
domain_of:
- DcatRessurs
- Datasett
- Kvalitetsdimensjon
- Kvalitetsmaal
- Kvalitetsmerknad
- Kvalitetsmaaling
- Standard
- Tekstdel
- Motivasjon
- Spraak
- Mediatype
- Begrep
- Begrepssamling
range: uriorcurie
required: true

```
</details>