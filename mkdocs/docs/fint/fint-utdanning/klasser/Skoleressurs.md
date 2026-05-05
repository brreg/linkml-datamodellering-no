

# Slot: skoleressurs 



URI: [https://schema.fintlabs.no/utdanning/:skoleressurs](https://schema.fintlabs.no/utdanning/:skoleressurs)
Alias: skoleressurs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sensor](sensor.md) | Ein sensor for ein eksamen |  no  |
| [Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  no  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Persongruppe](persongruppe.md), [Skole](skole.md), [Undervisningsforhold](undervisningsforhold.md), [Sensor](sensor.md) |

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