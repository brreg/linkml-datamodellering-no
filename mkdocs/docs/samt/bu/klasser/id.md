

# Slot: id 


_URI-identifikator for ressursen._





URI: [samtbuskole:id](https://example.no/ontology/skole#id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Standard](standard.md) | Ein standard som ein ressurs er i samsvar med |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [Gebyr](gebyr.md) | Eit gebyr knytt til bruk av ein datatjeneste |  no  |
| [KatalogisertRessurs](katalogisertressurs.md) | Basisklasse for ressursar som kan katalogiserast |  no  |
| [Aktor](aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  no  |
| [Tidsrom](tidsrom.md) | Eit tidsintervall med start- og sluttdato |  no  |
| [Spraak](spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |  no  |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Rettighetserklaring](rettighetserklaring.md) | Ei erklæring om rettar til ein ressurs (ODRS) |  no  |
| [ProvAttributering](provattributering.md) | Ein kvalifisert PROV-attributering |  no  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [Tidsinstant](tidsinstant.md) | Eit tidspunkt (OWL Time) |  no  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |
| [Identifikator](identifikator.md) | Ein alternativ identifikator for ein ressurs |  no  |
| [Sjekksum](sjekksum.md) | Ein sjekksum for ein distribusjon |  no  |
| [OdrlPolicy](odrlpolicy.md) | Ein ODRL-policy |  no  |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [ProvAktivitet](provaktivitet.md) | Ein PROV-aktivitet |  no  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  no  |
| [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon for ein aktør |  no  |
| [ProvenanceStatement](provenancestatement.md) | Ein provenienserklæring |  no  |
| [Frekvens](frekvens.md) | Ein oppdateringsfrekvens |  no  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |
| [Relasjon](relasjon.md) | Ein kvalifisert relasjon mellom to ressursar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Spraak](spraak.md), [Mediatype](mediatype.md), [Konsept](konsept.md), [Begrepssamling](begrepssamling.md), [Frekvens](frekvens.md), [ProvenanceStatement](provenancestatement.md), [OdrlPolicy](odrlpolicy.md), [ProvAktivitet](provaktivitet.md), [ProvAttributering](provattributering.md), [Tidsinstant](tidsinstant.md), [KatalogisertRessurs](katalogisertressurs.md), [Aktor](aktor.md), [Kontaktopplysning](kontaktopplysning.md), [Tidsrom](tidsrom.md), [Standard](standard.md), [RegulativRessurs](regulativressurs.md), [Identifikator](identifikator.md), [Rettighetserklaring](rettighetserklaring.md), [Sjekksum](sjekksum.md), [Gebyr](gebyr.md), [Relasjon](relasjon.md), [Distribusjon](distribusjon.md), [Katalogpost](katalogpost.md) |

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


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:id |
| native | samtbuskole:id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
identifier: true
alias: id
domain_of:
- Spraak
- Mediatype
- Konsept
- Begrepssamling
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
range: uriorcurie
required: true

```
</details>