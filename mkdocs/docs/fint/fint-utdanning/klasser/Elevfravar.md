

# Slot: elevfravar 



URI: [https://schema.fintlabs.no/utdanning/:elevfravar](https://schema.fintlabs.no/utdanning/:elevfravar)
Alias: elevfravar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fraversregistrering](fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Fraversregistrering](fraversregistrering.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:elevfravar |
| native | https://schema.fintlabs.no/utdanning/:elevfravar |




## LinkML Source

<details>
```yaml
name: elevfravar
alias: elevfravar
domain_of:
- UtdanningContainer
- Elevforhold
- Fraversregistrering
range: string

```
</details>