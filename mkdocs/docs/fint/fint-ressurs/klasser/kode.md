

# Slot: kode 



URI: [https://schema.fintlabs.no/ressurs/:kode](https://schema.fintlabs.no/ressurs/:kode)
Alias: kode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Brukertype](Brukertype.md) | Dei ulike brukartypane som kan nytte lisensen (t |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Rettighet](Rettighet.md) | Ei namngitt rettighet |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Status](Status.md) | Status på ei digital eining i fagsystemet |  no  |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Enhetstype](Enhetstype.md) | Type digital eining (t |  no  |
| [Plattform](Plattform.md) | Plattforma tenesta kan leverast på (t |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Handhevingstype](Handhevingstype.md) | Korleis ulike lisensmodellar kan handhevast (Håndhevingstype) |  no  |
| [Applikasjonskategori](Applikasjonskategori.md) | Kategori av applikasjonar |  no  |
| [Produsent](Produsent.md) | Produsent av ei digital eining |  no  |
| [Lisensmodell](Lisensmodell.md) | Lisensmodellar som kan knytast til ein lisens |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Rettighet](Rettighet.md), [Applikasjonskategori](Applikasjonskategori.md), [Brukertype](Brukertype.md), [Enhetstype](Enhetstype.md), [Handhevingstype](Handhevingstype.md), [Lisensmodell](Lisensmodell.md), [Plattform](Plattform.md), [Produsent](Produsent.md), [Status](Status.md), [Begrep](Begrep.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/ressurs/:kode |
| native | https://schema.fintlabs.no/ressurs/:kode |




## LinkML Source

<details>
```yaml
name: kode
alias: kode
domain_of:
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
range: string

```
</details>