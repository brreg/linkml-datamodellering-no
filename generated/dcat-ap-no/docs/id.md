

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/dcat-ap-no/id](https://data.norge.no/linkml/dcat-ap-no/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Identifikator](Identifikator.md) | Ein alternativ identifikator for ein ressurs |  no  |
| [Relasjon](Relasjon.md) | Ein kvalifisert relasjon mellom to ressursar |  no  |
| [Begrepssamling](Begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [KatalogisertRessurs](KatalogisertRessurs.md) | Basisklasse for ressursar som kan katalogiserast |  no  |
| [Katalogpost](Katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |
| [OdrlPolicy](OdrlPolicy.md) | Ein ODRL-policy |  no  |
| [Datasettserie](Datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  no  |
| [ProvAttributering](ProvAttributering.md) | Ein kvalifisert PROV-attributering |  no  |
| [ProvAktivitet](ProvAktivitet.md) | Ein PROV-aktivitet |  no  |
| [Aktor](Aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  no  |
| [Spraak](Spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |  no  |
| [RegulativRessurs](RegulativRessurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Tidsinstant](Tidsinstant.md) | Eit tidspunkt (OWL Time) |  no  |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |
| [Kontaktopplysning](Kontaktopplysning.md) | Kontaktinformasjon for ein aktør |  no  |
| [ProvenanceStatement](ProvenanceStatement.md) | Ein provenienserklæring |  no  |
| [Frekvens](Frekvens.md) | Ein oppdateringsfrekvens |  no  |
| [Standard](Standard.md) | Ein standard som ein ressurs er i samsvar med |  no  |
| [Rettighetserklaring](Rettighetserklaring.md) | Ei erklæring om rettar til ein ressurs (ODRS) |  no  |
| [Mediatype](Mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [Gebyr](Gebyr.md) | Eit gebyr knytt til bruk av ein datatjeneste |  no  |
| [Tidsrom](Tidsrom.md) | Eit tidsintervall med start- og sluttdato |  no  |
| [Sjekksum](Sjekksum.md) | Ein sjekksum for ein distribusjon |  no  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Begrep](Begrep.md) | Eit SKOS-omgrep frå eit kontrollert vokabular |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Frekvens](Frekvens.md), [ProvenanceStatement](ProvenanceStatement.md), [OdrlPolicy](OdrlPolicy.md), [ProvAktivitet](ProvAktivitet.md), [ProvAttributering](ProvAttributering.md), [Tidsinstant](Tidsinstant.md), [KatalogisertRessurs](KatalogisertRessurs.md), [Aktor](Aktor.md), [Kontaktopplysning](Kontaktopplysning.md), [Tidsrom](Tidsrom.md), [Standard](Standard.md), [RegulativRessurs](RegulativRessurs.md), [Identifikator](Identifikator.md), [Rettighetserklaring](Rettighetserklaring.md), [Sjekksum](Sjekksum.md), [Gebyr](Gebyr.md), [Relasjon](Relasjon.md), [Distribusjon](Distribusjon.md), [Katalogpost](Katalogpost.md), [Spraak](Spraak.md), [Mediatype](Mediatype.md), [Begrep](Begrep.md), [Begrepssamling](Begrepssamling.md) |

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


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/dcat-ap-no/id |
| native | https://data.norge.no/linkml/dcat-ap-no/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
identifier: true
alias: id
domain_of:
- Frekvens
- ProvenanceStatement
- OdrlPolicy
- ProvAktivitet
- ProvAttributering
- Tidsinstant
- KatalogisertRessurs
- Aktor
- Kontaktopplysning
- Tidsrom
- Standard
- RegulativRessurs
- Identifikator
- Rettighetserklaring
- Sjekksum
- Gebyr
- Relasjon
- Distribusjon
- Katalogpost
- Spraak
- Mediatype
- Begrep
- Begrepssamling
range: uriorcurie
required: true

```
</details>