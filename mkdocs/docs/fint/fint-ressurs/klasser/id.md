

# Slot: id 


_URI-identifikator (tilsvarar systemId i FINT)._





URI: [https://schema.fintlabs.no/ressurs/:id](https://schema.fintlabs.no/ressurs/:id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Enhetstype](Enhetstype.md) | Type digital eining (t |  no  |
| [Applikasjonskategori](Applikasjonskategori.md) | Kategori av applikasjonar |  no  |
| [Brukertype](Brukertype.md) | Dei ulike brukartypane som kan nytte lisensen (t |  no  |
| [Applikasjonsressurs](Applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  no  |
| [Enhetsgruppe](Enhetsgruppe.md) | Ei gruppering av einsarta digitale einingar (t |  no  |
| [Rettighet](Rettighet.md) | Ei namngitt rettighet |  no  |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Valuta](Valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Person](Person.md) | Fysiske private personar |  no  |
| [Applikasjon](Applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |  no  |
| [Lisensmodell](Lisensmodell.md) | Lisensmodellar som kan knytast til ein lisens |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Status](Status.md) | Status på ei digital eining i fagsystemet |  no  |
| [Identitet](Identitet.md) | Identitet som identifiserer innehavaren av rettigheiter i organisasjonen |  no  |
| [Plattform](Plattform.md) | Plattforma tenesta kan leverast på (t |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Applikasjonsressurstilgjengelighet](Applikasjonsressurstilgjengelighet.md) | Kva organisasjonselements brukarar som har tilgang til ein ressurs |  no  |
| [Enhetsgruppemedlemskap](Enhetsgruppemedlemskap.md) | Medlemskap mellom ei digital eining og ei einingsgruppe |  no  |
| [Handhevingstype](Handhevingstype.md) | Korleis ulike lisensmodellar kan handhevast (Håndhevingstype) |  no  |
| [Produsent](Produsent.md) | Produsent av ei digital eining |  no  |
| [DigitalEnhet](DigitalEnhet.md) | Ei digital eining som t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Applikasjon](Applikasjon.md), [Applikasjonsressurs](Applikasjonsressurs.md), [Applikasjonsressurstilgjengelighet](Applikasjonsressurstilgjengelighet.md), [DigitalEnhet](DigitalEnhet.md), [Enhetsgruppe](Enhetsgruppe.md), [Enhetsgruppemedlemskap](Enhetsgruppemedlemskap.md), [Identitet](Identitet.md), [Rettighet](Rettighet.md), [Applikasjonskategori](Applikasjonskategori.md), [Brukertype](Brukertype.md), [Enhetstype](Enhetstype.md), [Handhevingstype](Handhevingstype.md), [Lisensmodell](Lisensmodell.md), [Plattform](Plattform.md), [Produsent](Produsent.md), [Status](Status.md), [Begrep](Begrep.md), [Valuta](Valuta.md), [Person](Person.md), [Kontaktperson](Kontaktperson.md), [Virksomhet](Virksomhet.md) |

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


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/ressurs/:id |
| native | https://schema.fintlabs.no/ressurs/:id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator (tilsvarar systemId i FINT).
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
identifier: true
alias: id
domain_of:
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
- Begrep
- Valuta
- Person
- Kontaktperson
- Virksomhet
range: uriorcurie
required: true

```
</details>