

# Slot: sensor 



URI: [https://schema.fintlabs.no/utdanning/:sensor](https://schema.fintlabs.no/utdanning/:sensor)
Alias: sensor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppe](Eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Skoleressurs](Skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [UtdanningContainer](UtdanningContainer.md), [Skoleressurs](Skoleressurs.md), [Eksamensgruppe](Eksamensgruppe.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:sensor |
| native | https://schema.fintlabs.no/utdanning/:sensor |




## LinkML Source

<details>
```yaml
name: sensor
alias: sensor
domain_of:
- UtdanningContainer
- Skoleressurs
- Eksamensgruppe
range: string

```
</details>