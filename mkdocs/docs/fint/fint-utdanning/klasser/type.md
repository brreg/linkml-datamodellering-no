

# Slot: type 



URI: [https://schema.fintlabs.no/utdanning/:type](https://schema.fintlabs.no/utdanning/:type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  no  |
| [OtStatus](otstatus.md) | Status for ein ungdom i oppfølgingstenesta |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Varsel](varsel.md), [OtStatus](otstatus.md), [Kontaktperson](kontaktperson.md) |

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