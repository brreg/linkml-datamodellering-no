

# Slot: skoleressurs 



URI: [https://schema.fintlabs.no/utdanning/:skoleressurs](https://schema.fintlabs.no/utdanning/:skoleressurs)
Alias: skoleressurs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sensor](Sensor.md) | Ein sensor for ein eksamen |  no  |
| [Skole](Skole.md) | Ein skule eller opplæringsinstitusjon |  no  |
| [Persongruppe](Persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Undervisningsforhold](Undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Persongruppe](Persongruppe.md), [Skole](Skole.md), [Undervisningsforhold](Undervisningsforhold.md), [Sensor](Sensor.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:skoleressurs |
| native | https://schema.fintlabs.no/utdanning/:skoleressurs |




## LinkML Source

<details>
```yaml
name: skoleressurs
alias: skoleressurs
domain_of:
- Persongruppe
- Skole
- Undervisningsforhold
- Sensor
range: string

```
</details>