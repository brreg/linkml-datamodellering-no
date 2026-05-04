

# Slot: navn 



URI: [https://schema.fintlabs.no/ressurs/:navn](https://schema.fintlabs.no/ressurs/:navn)
Alias: navn

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
| [Enhetsgruppe](Enhetsgruppe.md) | Ei gruppering av einsarta digitale einingar (t |  no  |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Valuta](Valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Applikasjon](Applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |  no  |
| [Lisensmodell](Lisensmodell.md) | Lisensmodellar som kan knytast til ein lisens |  no  |
| [Person](Person.md) | Fysiske private personar |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Status](Status.md) | Status på ei digital eining i fagsystemet |  no  |
| [Plattform](Plattform.md) | Plattforma tenesta kan leverast på (t |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Handhevingstype](Handhevingstype.md) | Korleis ulike lisensmodellar kan handhevast (Håndhevingstype) |  no  |
| [Produsent](Produsent.md) | Produsent av ei digital eining |  no  |
| [DigitalEnhet](DigitalEnhet.md) | Ei digital eining som t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Applikasjon](Applikasjon.md), [Applikasjonsressurs](Applikasjonsressurs.md), [DigitalEnhet](DigitalEnhet.md), [Enhetsgruppe](Enhetsgruppe.md), [Rettighet](Rettighet.md), [Applikasjonskategori](Applikasjonskategori.md), [Brukertype](Brukertype.md), [Enhetstype](Enhetstype.md), [Handhevingstype](Handhevingstype.md), [Lisensmodell](Lisensmodell.md), [Plattform](Plattform.md), [Produsent](Produsent.md), [Status](Status.md), [Begrep](Begrep.md), [Valuta](Valuta.md), [Person](Person.md), [Kontaktperson](Kontaktperson.md) |

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