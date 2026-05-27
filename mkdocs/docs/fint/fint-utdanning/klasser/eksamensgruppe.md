

# Slot: eksamensgruppe 


_Eksamensgruppe._





URI: [utd:eksamensgruppe](https://schema.fintlabs.no/utdanning/eksamensgruppe)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [Eksamen](eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  yes  |
| [Fag](fag.md) | Eit skulefag |  yes  |
| [Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  yes  |
| [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  yes  |
| [Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  yes  |
| [Sensor](sensor.md) | Ein sensor for ein eksamen |  yes  |
| [Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |  yes  |






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


* from schema: https://data.norge.no/fint/fint-utdanning




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
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:eksamensgruppe
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