

# Slot: fag 



URI: [https://schema.fintlabs.no/utdanning/:fag](https://schema.fintlabs.no/utdanning/:fag)
Alias: fag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Underveisfagvurdering](Underveisfagvurdering.md) | Underveisfagvurdering for ein elev |  no  |
| [Eksamensgruppe](Eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [Fravarsoversikt](Fravarsoversikt.md) | Oversikt over fråvær for ein elev i eit fag |  no  |
| [Skole](Skole.md) | Ein skule eller opplæringsinstitusjon |  no  |
| [FagvurderingAbstrakt](FagvurderingAbstrakt.md) | Abstrakt basisklasse for fagvurderingar |  no  |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Eksamensvurdering](Eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Faggruppe](Faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  no  |
| [Undervisningsgruppe](Undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [Halvaarsfagvurdering](Halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |  no  |
| [Sluttfagvurdering](Sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [UtdanningContainer](UtdanningContainer.md), [Skole](Skole.md), [Faggruppe](Faggruppe.md), [Undervisningsgruppe](Undervisningsgruppe.md), [FagvurderingAbstrakt](FagvurderingAbstrakt.md), [Eksamensgruppe](Eksamensgruppe.md), [Fravarsoversikt](Fravarsoversikt.md) |

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