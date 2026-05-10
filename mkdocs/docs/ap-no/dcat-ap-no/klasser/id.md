

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/common-ap-no/id](https://data.norge.no/linkml/common-ap-no/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sjekksum](sjekksum.md) | Ein sjekksum for ein distribusjon |  no  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |
| [Kvalitetssertifikat](kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |  no  |
| [Tidsrom](tidsrom.md) | Eit tidsintervall med start- og sluttdato |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Kvalitetsmerknad](kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |  no  |
| [Relasjon](relasjon.md) | Ein kvalifisert relasjon mellom to ressursar |  no  |
| [Kvalitetsdeldimensjon](kvalitetsdeldimensjon.md) | Ein deldimensjon av ein kvalitetsdimensjon |  no  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  no  |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Gebyr](gebyr.md) | Eit gebyr knytt til bruk av ein datatjeneste |  no  |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [Kvalitetsmaaling](kvalitetsmaaling.md) | Ei konkret måling av eit kvalitetsmål for eit datasett |  no  |
| [Tekstdel](tekstdel.md) | Ein tekstleg del av ein kvalitetsmerknad (Web Annotation) |  no  |
| [Aktor](aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  no  |
| [Rettighetserklaring](rettighetserklaring.md) | Ei erklæring om rettar til ein ressurs (ODRS) |  no  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |
| [Standard](standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |  no  |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [Brukartilbakemelding](brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |  no  |
| [Identifikator](identifikator.md) | Ein alternativ identifikator for ein ressurs |  no  |
| [Kvalitetsmaal](kvalitetsmaal.md) | Eit kvalitetsmål som operasjonaliserer ein kvalitetsdeldimensjon |  no  |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [KatalogisertRessurs](katalogisertressurs.md) | Basisklasse for ressursar som kan katalogiserast |  no  |
| [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon for ein aktør |  no  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Mediatype](mediatype.md), [Konsept](konsept.md), [Begrepssamling](begrepssamling.md), [Kvalitetsdimensjon](kvalitetsdimensjon.md), [Kvalitetsmaal](kvalitetsmaal.md), [Kvalitetsmerknad](kvalitetsmerknad.md), [Kvalitetsmaaling](kvalitetsmaaling.md), [Standard](standard.md), [Tekstdel](tekstdel.md), [KatalogisertRessurs](katalogisertressurs.md), [Aktor](aktor.md), [Kontaktopplysning](kontaktopplysning.md), [Tidsrom](tidsrom.md), [RegulativRessurs](regulativressurs.md), [Identifikator](identifikator.md), [Rettighetserklaring](rettighetserklaring.md), [Sjekksum](sjekksum.md), [Gebyr](gebyr.md), [Relasjon](relasjon.md), [Distribusjon](distribusjon.md), [Datasett](datasett.md), [Katalogpost](katalogpost.md) |

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
alias: id
domain_of:
- Mediatype
- Konsept
- Begrepssamling
- Kvalitetsdimensjon
- Kvalitetsmaal
- Kvalitetsmerknad
- Kvalitetsmaaling
- Standard
- Tekstdel
- KatalogisertRessurs
- Aktor
- Kontaktopplysning
- Tidsrom
- RegulativRessurs
- Identifikator
- Rettighetserklaring
- Sjekksum
- Gebyr
- Relasjon
- Distribusjon
- Datasett
- Katalogpost
range: uriorcurie
required: true

```
</details>