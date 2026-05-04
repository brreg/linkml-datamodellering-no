

# Slot: gyldighetsperiode 



URI: [https://schema.fintlabs.no/ressurs/:gyldighetsperiode](https://schema.fintlabs.no/ressurs/:gyldighetsperiode)
Alias: gyldighetsperiode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Enhetstype](Enhetstype.md) | Type digital eining (t |  no  |
| [Applikasjonskategori](Applikasjonskategori.md) | Kategori av applikasjonar |  no  |
| [Brukertype](Brukertype.md) | Dei ulike brukartypane som kan nytte lisensen (t |  no  |
| [Applikasjonsressurs](Applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  no  |
| [Rettighet](Rettighet.md) | Ei namngitt rettighet |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Lisensmodell](Lisensmodell.md) | Lisensmodellar som kan knytast til ein lisens |  no  |
| [Applikasjon](Applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Status](Status.md) | Status på ei digital eining i fagsystemet |  no  |
| [Plattform](Plattform.md) | Plattforma tenesta kan leverast på (t |  no  |
| [Identifikator](Identifikator.md) | Unik identifikasjon til eit objekt |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Applikasjonsressurstilgjengelighet](Applikasjonsressurstilgjengelighet.md) | Kva organisasjonselements brukarar som har tilgang til ein ressurs |  no  |
| [Handhevingstype](Handhevingstype.md) | Korleis ulike lisensmodellar kan handhevast (Håndhevingstype) |  no  |
| [Produsent](Produsent.md) | Produsent av ei digital eining |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Applikasjon](Applikasjon.md), [Applikasjonsressurs](Applikasjonsressurs.md), [Applikasjonsressurstilgjengelighet](Applikasjonsressurstilgjengelighet.md), [Rettighet](Rettighet.md), [Applikasjonskategori](Applikasjonskategori.md), [Brukertype](Brukertype.md), [Enhetstype](Enhetstype.md), [Handhevingstype](Handhevingstype.md), [Lisensmodell](Lisensmodell.md), [Plattform](Plattform.md), [Produsent](Produsent.md), [Status](Status.md), [Begrep](Begrep.md), [Identifikator](Identifikator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/ressurs/:gyldighetsperiode |
| native | https://schema.fintlabs.no/ressurs/:gyldighetsperiode |




## LinkML Source

<details>
```yaml
name: gyldighetsperiode
alias: gyldighetsperiode
domain_of:
- Applikasjon
- Applikasjonsressurs
- Applikasjonsressurstilgjengelighet
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
- Identifikator
range: string

```
</details>