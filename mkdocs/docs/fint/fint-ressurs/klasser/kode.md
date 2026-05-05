

# Slot: kode 



URI: [https://schema.fintlabs.no/ressurs/:kode](https://schema.fintlabs.no/ressurs/:kode)
Alias: kode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rettighet](rettighet.md) | Ei namngitt rettighet |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Lisensmodell](lisensmodell.md) | Lisensmodellar som kan knytast til ein lisens |  no  |
| [Handhevingstype](handhevingstype.md) | Korleis ulike lisensmodellar kan handhevast (Håndhevingstype) |  no  |
| [Plattform](plattform.md) | Plattforma tenesta kan leverast på (t |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Applikasjonskategori](applikasjonskategori.md) | Kategori av applikasjonar |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Produsent](produsent.md) | Produsent av ei digital eining |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Status](status.md) | Status på ei digital eining i fagsystemet |  no  |
| [Enhetstype](enhetstype.md) | Type digital eining (t |  no  |
| [Brukertype](brukertype.md) | Dei ulike brukartypane som kan nytte lisensen (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Rettighet](rettighet.md), [Applikasjonskategori](applikasjonskategori.md), [Brukertype](brukertype.md), [Enhetstype](enhetstype.md), [Handhevingstype](handhevingstype.md), [Lisensmodell](lisensmodell.md), [Plattform](plattform.md), [Produsent](produsent.md), [Status](status.md), [Begrep](begrep.md) |

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