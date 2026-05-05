

# Slot: eksamensgruppe 



URI: [https://schema.fintlabs.no/utdanning/:eksamensgruppe](https://schema.fintlabs.no/utdanning/:eksamensgruppe)
Alias: eksamensgruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  no  |
| [Fag](fag.md) | Eit skulefag |  no  |
| [Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Eksamen](eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  no  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  no  |
| [Sensor](sensor.md) | Ein sensor for ein eksamen |  no  |
| [Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |
| [Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Skole](skole.md), [Eksamen](eksamen.md), [Fag](fag.md), [Undervisningsforhold](undervisningsforhold.md), [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md), [Eksamensvurdering](eksamensvurdering.md), [Sensor](sensor.md), [Sluttfagvurdering](sluttfagvurdering.md) |

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