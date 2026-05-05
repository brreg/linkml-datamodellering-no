

# Slot: varsel 



URI: [https://schema.fintlabs.no/utdanning/:varsel](https://schema.fintlabs.no/utdanning/:varsel)
Alias: varsel

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
| self | https://schema.fintlabs.no/utdanning/:varsel |
| native | https://schema.fintlabs.no/utdanning/:varsel |




## LinkML Source

<details>
```yaml
name: varsel
alias: varsel
domain_of:
- UtdanningContainer
- Faggruppemedlemskap
range: string

```
</details>