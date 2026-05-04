

# Slot: eksamensgruppe 



URI: [https://schema.fintlabs.no/utdanning/:eksamensgruppe](https://schema.fintlabs.no/utdanning/:eksamensgruppe)
Alias: eksamensgruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](Skole.md) | Ein skule eller opplæringsinstitusjon |  no  |
| [Fag](Fag.md) | Eit skulefag |  no  |
| [Sensor](Sensor.md) | Ein sensor for ein eksamen |  no  |
| [Eksamen](Eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  no  |
| [Eksamensvurdering](Eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Eksamensgruppemedlemskap](Eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  no  |
| [Undervisningsforhold](Undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  no  |
| [Sluttfagvurdering](Sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Skole](Skole.md), [Eksamen](Eksamen.md), [Fag](Fag.md), [Undervisningsforhold](Undervisningsforhold.md), [Eksamensgruppemedlemskap](Eksamensgruppemedlemskap.md), [Eksamensvurdering](Eksamensvurdering.md), [Sensor](Sensor.md), [Sluttfagvurdering](Sluttfagvurdering.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:eksamensgruppe |
| native | https://schema.fintlabs.no/utdanning/:eksamensgruppe |




## LinkML Source

<details>
```yaml
name: eksamensgruppe
alias: eksamensgruppe
domain_of:
- Skole
- Eksamen
- Fag
- Undervisningsforhold
- Eksamensgruppemedlemskap
- Eksamensvurdering
- Sensor
- Sluttfagvurdering
range: string

```
</details>