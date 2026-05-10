

# Slot: kode 


_Verdi som identifiserer omgrepet._





URI: [fint:kode](https://schema.fintlabs.no/kode)
Alias: kode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Brukertype](brukertype.md) | Dei ulike brukartypane som kan nytte lisensen |  yes  |
| [Rettighet](rettighet.md) | Ei namngitt rettighet |  yes  |
| [Lisensmodell](lisensmodell.md) | Lisensmodellar som kan knytast til ein lisens |  yes  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  yes  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Applikasjonskategori](applikasjonskategori.md) | Kategori av applikasjonar |  yes  |
| [Enhetstype](enhetstype.md) | Type digital eining |  yes  |
| [Status](status.md) | Status på ei digital eining i fagsystemet |  yes  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Produsent](produsent.md) | Produsent av ei digital eining |  yes  |
| [Plattform](plattform.md) | Plattforma tenesta kan leverast på |  yes  |
| [Handhevingstype](handhevingstype.md) | Korleis ulike lisensmodellar kan handhevast |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Begrep](begrep.md), [Rettighet](rettighet.md), [Applikasjonskategori](applikasjonskategori.md), [Brukertype](brukertype.md), [Enhetstype](enhetstype.md), [Handhevingstype](handhevingstype.md), [Lisensmodell](lisensmodell.md), [Plattform](plattform.md), [Produsent](produsent.md), [Status](status.md) |
| Slot URI | [fint:kode](https://schema.fintlabs.no/kode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kode |
| native | https://schema.fintlabs.no/:kode |




## LinkML Source

<details>
```yaml
name: kode
description: Verdi som identifiserer omgrepet.
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:kode
alias: kode
domain_of:
- Begrep
- Rettighet
- Applikasjonskategori
- Brukertype
- Enhetstype
- Handhevingstype
- Lisensmodell
- Plattform
- Produsent
- Status
range: string

```
</details>