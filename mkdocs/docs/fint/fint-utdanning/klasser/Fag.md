

# Slot: fag 



URI: [https://schema.fintlabs.no/utdanning/:fag](https://schema.fintlabs.no/utdanning/:fag)
Alias: fag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Halvaarsfagvurdering](halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |  no  |
| [Underveisfagvurdering](underveisfagvurdering.md) | Underveisfagvurdering for ein elev |  no  |
| [Faggruppe](faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  no  |
| [Fravarsoversikt](fravarsoversikt.md) | Oversikt over fråvær for ein elev i eit fag |  no  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  no  |
| [FagvurderingAbstrakt](fagvurderingabstrakt.md) | Abstrakt basisklasse for fagvurderingar |  no  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Skole](skole.md), [Faggruppe](faggruppe.md), [Undervisningsgruppe](undervisningsgruppe.md), [FagvurderingAbstrakt](fagvurderingabstrakt.md), [Eksamensgruppe](eksamensgruppe.md), [Fravarsoversikt](fravarsoversikt.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:fag |
| native | https://schema.fintlabs.no/utdanning/:fag |




## LinkML Source

<details>
```yaml
name: fag
alias: fag
domain_of:
- UtdanningContainer
- Skole
- Faggruppe
- Undervisningsgruppe
- FagvurderingAbstrakt
- Eksamensgruppe
- Fravarsoversikt
range: string

```
</details>