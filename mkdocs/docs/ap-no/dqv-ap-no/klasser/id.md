

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/dqv-ap-no/id](https://data.norge.no/linkml/dqv-ap-no/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Brukartilbakemelding](brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |  no  |
| [Datasett](datasett.md) | Eit datasett (dcat:Dataset) utvida med DQV-AP-NO-eigenskapar for kvalitetsinf... |  no  |
| [Kvalitetsmerknad](kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |  no  |
| [DcatRessurs](dcatressurs.md) | Ein katalogisert ressurs (brukt som målklasse for oa:hasTarget) |  no  |
| [Kvalitetsmaal](kvalitetsmaal.md) | Eit kvalitetsmål som operasjonaliserer ein kvalitetsdeldimensjon |  no  |
| [Spraak](spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |  no  |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [Kvalitetsdeldimensjon](kvalitetsdeldimensjon.md) | Ein deldimensjon av ein kvalitetsdimensjon |  no  |
| [Kvalitetsmaaling](kvalitetsmaaling.md) | Ei konkret måling av eit kvalitetsmål for eit datasett |  no  |
| [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål |  no  |
| [Standard](standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |  no  |
| [Kvalitetssertifikat](kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |  no  |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [Motivasjon](motivasjon.md) | Motivasjonen bak ein kvalitetsmerknad (Web Annotation) |  no  |
| [Tekstdel](tekstdel.md) | Ein tekstleg del av ein kvalitetsmerknad (Web Annotation) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [DcatRessurs](dcatressurs.md), [Datasett](datasett.md), [Kvalitetsdimensjon](kvalitetsdimensjon.md), [Kvalitetsmaal](kvalitetsmaal.md), [Kvalitetsmerknad](kvalitetsmerknad.md), [Kvalitetsmaaling](kvalitetsmaaling.md), [Standard](standard.md), [Tekstdel](tekstdel.md), [Motivasjon](motivasjon.md), [Spraak](spraak.md), [Mediatype](mediatype.md), [Konsept](konsept.md), [Begrepssamling](begrepssamling.md) |

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
- Konsept
- Begrepssamling
range: uriorcurie
required: true

```
</details>