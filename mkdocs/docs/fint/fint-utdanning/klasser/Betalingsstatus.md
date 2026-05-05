

# Slot: betalingsstatus 



URI: [https://schema.fintlabs.no/utdanning/:betalingsstatus](https://schema.fintlabs.no/utdanning/:betalingsstatus)
Alias: betalingsstatus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:betalingsstatus |
| native | https://schema.fintlabs.no/utdanning/:betalingsstatus |




## LinkML Source

<details>
```yaml
name: betalingsstatus
alias: betalingsstatus
domain_of:
- UtdanningContainer
- Eksamensgruppemedlemskap
range: string

```
</details>