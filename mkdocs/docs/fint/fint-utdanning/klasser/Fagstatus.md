

# Slot: fagstatus 



URI: [https://schema.fintlabs.no/utdanning/:fagstatus](https://schema.fintlabs.no/utdanning/:fagstatus)
Alias: fagstatus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faggruppemedlemskap](faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Faggruppemedlemskap](faggruppemedlemskap.md) |

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