

# Slot: kontering 



URI: [https://schema.fintlabs.no/okonomi/:kontering](https://schema.fintlabs.no/okonomi/:kontering)
Alias: kontering

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vare](Vare.md) | Vare eller teneste som kan leverast og fakturerast |  no  |
| [Postering](Postering.md) | Føring på ein konto i rekneskapet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Postering](Postering.md), [Vare](Vare.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:kontering |
| native | https://schema.fintlabs.no/okonomi/:kontering |




## LinkML Source

<details>
```yaml
name: kontering
alias: kontering
domain_of:
- Postering
- Vare
range: string

```
</details>