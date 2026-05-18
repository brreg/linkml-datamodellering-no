

# Slot: eksamensgruppe 


_Eksamensgruppe._





URI: [utd:eksamensgruppe](https://schema.fintlabs.no/utdanning/eksamensgruppe)
Alias: eksamensgruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |  yes  |
| [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  yes  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  yes  |
| [Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  yes  |
| [Eksamen](eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  yes  |
| [Fag](fag.md) | Eit skulefag |  yes  |
| [Sensor](sensor.md) | Ein sensor for ein eksamen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eksamensgruppe](eksamensgruppe.md) |
| Domain Of | [Skole](skole.md), [Eksamen](eksamen.md), [Fag](fag.md), [Undervisningsforhold](undervisningsforhold.md), [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md), [Eksamensvurdering](eksamensvurdering.md), [Sensor](sensor.md), [Sluttfagvurdering](sluttfagvurdering.md) |
| Slot URI | [utd:eksamensgruppe](https://schema.fintlabs.no/utdanning/eksamensgruppe) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:eksamensgruppe |
| native | https://schema.fintlabs.no/utdanning/:eksamensgruppe |




## LinkML Source

<details>
```yaml
name: eksamensgruppe
description: Eksamensgruppe.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:eksamensgruppe
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
range: Eksamensgruppe

```
</details>