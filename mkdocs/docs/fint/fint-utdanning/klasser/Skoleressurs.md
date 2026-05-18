

# Slot: skoleressurs 


_Skoleressurs._





URI: [utd:skoleressurs](https://schema.fintlabs.no/utdanning/skoleressurs)
Alias: skoleressurs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  yes  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  yes  |
| [Sensor](sensor.md) | Ein sensor for ein eksamen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skoleressurs](skoleressurs.md) |
| Domain Of | [Persongruppe](persongruppe.md), [Skole](skole.md), [Undervisningsforhold](undervisningsforhold.md), [Sensor](sensor.md) |
| Slot URI | [utd:skoleressurs](https://schema.fintlabs.no/utdanning/skoleressurs) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:skoleressurs |
| native | https://schema.fintlabs.no/utdanning/:skoleressurs |




## LinkML Source

<details>
```yaml
name: skoleressurs
description: Skoleressurs.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:skoleressurs
alias: skoleressurs
domain_of:
- Persongruppe
- Skole
- Undervisningsforhold
- Sensor
range: Skoleressurs

```
</details>