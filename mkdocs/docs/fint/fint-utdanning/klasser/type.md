

# Slot: type 



URI: [https://schema.fintlabs.no/utdanning/:type](https://schema.fintlabs.no/utdanning/:type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varsel](Varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  no  |
| [OtStatus](OtStatus.md) | Status for ein ungdom i oppfølgingstenesta |  no  |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Varsel](Varsel.md), [OtStatus](OtStatus.md), [Kontaktperson](Kontaktperson.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:type |
| native | https://schema.fintlabs.no/utdanning/:type |




## LinkML Source

<details>
```yaml
name: type
alias: type
domain_of:
- Varsel
- OtStatus
- Kontaktperson
range: string

```
</details>