

# Slot: fagstatus 



URI: [https://schema.fintlabs.no/utdanning/:fagstatus](https://schema.fintlabs.no/utdanning/:fagstatus)
Alias: fagstatus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faggruppemedlemskap](Faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |  no  |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [UtdanningContainer](UtdanningContainer.md), [Faggruppemedlemskap](Faggruppemedlemskap.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:fagstatus |
| native | https://schema.fintlabs.no/utdanning/:fagstatus |




## LinkML Source

<details>
```yaml
name: fagstatus
alias: fagstatus
domain_of:
- UtdanningContainer
- Faggruppemedlemskap
range: string

```
</details>