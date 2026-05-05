

# Slot: navn 



URI: [https://schema.fintlabs.no/ressurs/:navn](https://schema.fintlabs.no/ressurs/:navn)
Alias: navn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Applikasjon](applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Status](status.md) | Status på ei digital eining i fagsystemet |  no  |
| [Enhetstype](enhetstype.md) | Type digital eining (t |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Rettighet](rettighet.md) | Ei namngitt rettighet |  no  |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Plattform](plattform.md) | Plattforma tenesta kan leverast på (t |  no  |
| [Applikasjonskategori](applikasjonskategori.md) | Kategori av applikasjonar |  no  |
| [Produsent](produsent.md) | Produsent av ei digital eining |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Brukertype](brukertype.md) | Dei ulike brukartypane som kan nytte lisensen (t |  no  |
| [Handhevingstype](handhevingstype.md) | Korleis ulike lisensmodellar kan handhevast (Håndhevingstype) |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Applikasjonsressurs](applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  no  |
| [Person](person.md) | Fysiske private personar |  no  |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |  no  |
| [Enhetsgruppe](enhetsgruppe.md) | Ei gruppering av einsarta digitale einingar (t |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Lisensmodell](lisensmodell.md) | Lisensmodellar som kan knytast til ein lisens |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Applikasjon](applikasjon.md), [Applikasjonsressurs](applikasjonsressurs.md), [DigitalEnhet](digitalenhet.md), [Enhetsgruppe](enhetsgruppe.md), [Rettighet](rettighet.md), [Applikasjonskategori](applikasjonskategori.md), [Brukertype](brukertype.md), [Enhetstype](enhetstype.md), [Handhevingstype](handhevingstype.md), [Lisensmodell](lisensmodell.md), [Plattform](plattform.md), [Produsent](produsent.md), [Status](status.md), [Begrep](begrep.md), [Valuta](valuta.md), [Person](person.md), [Kontaktperson](kontaktperson.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/ressurs/:navn |
| native | https://schema.fintlabs.no/ressurs/:navn |




## LinkML Source

<details>
```yaml
name: navn
alias: navn
domain_of:
- Applikasjon
- Applikasjonsressurs
- DigitalEnhet
- Enhetsgruppe
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
range: string

```
</details>