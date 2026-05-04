

# Slot: faggruppemedlemskap 



URI: [https://schema.fintlabs.no/utdanning/:faggruppemedlemskap](https://schema.fintlabs.no/utdanning/:faggruppemedlemskap)
Alias: faggruppemedlemskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varsel](Varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  no  |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Elevforhold](Elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |
| [Faggruppe](Faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [UtdanningContainer](UtdanningContainer.md), [Elevforhold](Elevforhold.md), [Varsel](Varsel.md), [Faggruppe](Faggruppe.md) |

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