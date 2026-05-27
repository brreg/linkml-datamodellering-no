

# Slot: fag 


_Fag._





URI: [utd:fag](https://schema.fintlabs.no/utdanning/fag)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [Faggruppe](faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  yes  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  yes  |
| [FagvurderingAbstrakt](fagvurderingabstrakt.md) | Abstrakt basisklasse for fagvurderingar |  yes  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  yes  |
| [Fravarsoversikt](fravarsoversikt.md) | Oversikt over fråvær for ein elev i eit fag |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |
| [Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Halvaarsfagvurdering](halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |  no  |
| [Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |
| [Underveisfagvurdering](underveisfagvurdering.md) | Underveisfagvurdering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fag](fag.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Skole](skole.md), [Faggruppe](faggruppe.md), [Undervisningsgruppe](undervisningsgruppe.md), [FagvurderingAbstrakt](fagvurderingabstrakt.md), [Eksamensgruppe](eksamensgruppe.md), [Fravarsoversikt](fravarsoversikt.md) |
| Slot URI | [utd:fag](https://schema.fintlabs.no/utdanning/fag) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:fag |
| native | https://schema.fintlabs.no/utdanning/:fag |




## LinkML Source

<details>
```yaml
name: fag
description: Fag.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:fag
domain_of:
- UtdanningContainer
- Skole
- Faggruppe
- Undervisningsgruppe
- FagvurderingAbstrakt
- Eksamensgruppe
- Fravarsoversikt
range: Fag

```
</details>