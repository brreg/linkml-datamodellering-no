

# Slot: eksamen 



URI: [https://schema.fintlabs.no/utdanning/:eksamen](https://schema.fintlabs.no/utdanning/:eksamen)
Alias: eksamen

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Rom](rom.md) | Eit rom eller lokale ved ein skule |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Rom](rom.md), [Eksamensgruppe](eksamensgruppe.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:eksamen |
| native | https://schema.fintlabs.no/utdanning/:eksamen |




## LinkML Source

<details>
```yaml
name: eksamen
alias: eksamen
domain_of:
- UtdanningContainer
- Rom
- Eksamensgruppe
range: string

```
</details>