

# Slot: faggruppemedlemskap 



URI: [https://schema.fintlabs.no/utdanning/:faggruppemedlemskap](https://schema.fintlabs.no/utdanning/:faggruppemedlemskap)
Alias: faggruppemedlemskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  no  |
| [Faggruppe](faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Varsel](varsel.md), [Faggruppe](faggruppe.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:faggruppemedlemskap |
| native | https://schema.fintlabs.no/utdanning/:faggruppemedlemskap |




## LinkML Source

<details>
```yaml
name: faggruppemedlemskap
alias: faggruppemedlemskap
domain_of:
- UtdanningContainer
- Elevforhold
- Varsel
- Faggruppe
range: string

```
</details>