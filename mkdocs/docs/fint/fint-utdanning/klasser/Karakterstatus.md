

# Slot: karakterstatus 



URI: [https://schema.fintlabs.no/utdanning/:karakterstatus](https://schema.fintlabs.no/utdanning/:karakterstatus)
Alias: karakterstatus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Karakterhistorie](karakterhistorie.md) | Historikk over endringar i ein karakter |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Karakterhistorie](karakterhistorie.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:karakterstatus |
| native | https://schema.fintlabs.no/utdanning/:karakterstatus |




## LinkML Source

<details>
```yaml
name: karakterstatus
alias: karakterstatus
domain_of:
- UtdanningContainer
- Karakterhistorie
range: string

```
</details>