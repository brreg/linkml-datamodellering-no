

# Slot: persongruppemedlemskap 



URI: [https://schema.fintlabs.no/utdanning/:persongruppemedlemskap](https://schema.fintlabs.no/utdanning/:persongruppemedlemskap)
Alias: persongruppemedlemskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Persongruppe](persongruppe.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:persongruppemedlemskap |
| native | https://schema.fintlabs.no/utdanning/:persongruppemedlemskap |




## LinkML Source

<details>
```yaml
name: persongruppemedlemskap
alias: persongruppemedlemskap
domain_of:
- UtdanningContainer
- Elevforhold
- Persongruppe
range: string

```
</details>