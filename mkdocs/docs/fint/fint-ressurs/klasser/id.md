

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://schema.fintlabs.no/:id](https://schema.fintlabs.no/:id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Elev](elev.md) | Ein elev registrert i skulesystemet |  no  |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Applikasjon](applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |  no  |
| [Applikasjonsressurs](applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  no  |
| [Applikasjonsressurstilgjengelighet](applikasjonsressurstilgjengelighet.md) | Kva organisasjonselements brukarar som har tilgang til ein ressurs |  no  |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |  no  |
| [Enhetsgruppe](enhetsgruppe.md) | Ei gruppering av einsarta digitale einingar |  no  |
| [Enhetsgruppemedlemskap](enhetsgruppemedlemskap.md) | Medlemskap mellom ei digital eining og ei einingsgruppe |  no  |
| [Identitet](identitet.md) | Identitet som identifiserer innehavaren av rettigheiter i organisasjonen |  no  |
| [Rettighet](rettighet.md) | Ei namngitt rettighet |  no  |
| [Applikasjonskategori](applikasjonskategori.md) | Kategori av applikasjonar |  no  |
| [Brukertype](brukertype.md) | Dei ulike brukartypane som kan nytte lisensen |  no  |
| [Enhetstype](enhetstype.md) | Type digital eining |  no  |
| [Handhevingstype](handhevingstype.md) | Korleis ulike lisensmodellar kan handhevast |  no  |
| [Lisensmodell](lisensmodell.md) | Lisensmodellar som kan knytast til ein lisens |  no  |
| [Plattform](plattform.md) | Plattforma tenesta kan leverast på |  no  |
| [Produsent](produsent.md) | Produsent av ei digital eining |  no  |
| [Status](status.md) | Status på ei digital eining i fagsystemet |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Begrep](begrep.md), [Elev](elev.md), [Valuta](valuta.md), [Person](person.md), [Kontaktperson](kontaktperson.md), [Virksomhet](virksomhet.md), [Applikasjon](applikasjon.md), [Applikasjonsressurs](applikasjonsressurs.md), [Applikasjonsressurstilgjengelighet](applikasjonsressurstilgjengelighet.md), [DigitalEnhet](digitalenhet.md), [Enhetsgruppe](enhetsgruppe.md), [Enhetsgruppemedlemskap](enhetsgruppemedlemskap.md), [Identitet](identitet.md), [Rettighet](rettighet.md), [Applikasjonskategori](applikasjonskategori.md), [Brukertype](brukertype.md), [Enhetstype](enhetstype.md), [Handhevingstype](handhevingstype.md), [Lisensmodell](lisensmodell.md), [Plattform](plattform.md), [Produsent](produsent.md), [Status](status.md) |

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


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/:id |
| native | https://schema.fintlabs.no/:id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/fint/fint-common
identifier: true
domain_of:
- Begrep
- Elev
- Valuta
- Person
- Kontaktperson
- Virksomhet
- Applikasjon
- Applikasjonsressurs
- Applikasjonsressurstilgjengelighet
- DigitalEnhet
- Enhetsgruppe
- Enhetsgruppemedlemskap
- Identitet
- Rettighet
- Applikasjonskategori
- Brukertype
- Enhetstype
- Handhevingstype
- Lisensmodell
- Plattform
- Produsent
- Status
range: uriorcurie
required: true

```
</details>