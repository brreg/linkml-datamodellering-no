

# Slot: tidsrom 



URI: [https://schema.fintlabs.no/utdanning/:tidsrom](https://schema.fintlabs.no/utdanning/:tidsrom)
Alias: tidsrom

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Time](Time.md) | Ein time i timeplanen |  no  |
| [Eksamen](Eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Eksamen](Eksamen.md), [Time](Time.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:tidsrom |
| native | https://schema.fintlabs.no/utdanning/:tidsrom |




## LinkML Source

<details>
```yaml
name: tidsrom
alias: tidsrom
domain_of:
- Eksamen
- Time
range: string

```
</details>