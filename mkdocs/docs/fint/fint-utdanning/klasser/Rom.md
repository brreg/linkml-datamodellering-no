

# Slot: rom 



URI: [https://schema.fintlabs.no/utdanning/:rom](https://schema.fintlabs.no/utdanning/:rom)
Alias: rom

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Time](Time.md) | Ein time i timeplanen |  no  |
| [Eksamen](Eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  no  |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [UtdanningContainer](UtdanningContainer.md), [Eksamen](Eksamen.md), [Time](Time.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:rom |
| native | https://schema.fintlabs.no/utdanning/:rom |




## LinkML Source

<details>
```yaml
name: rom
alias: rom
domain_of:
- UtdanningContainer
- Eksamen
- Time
range: string

```
</details>