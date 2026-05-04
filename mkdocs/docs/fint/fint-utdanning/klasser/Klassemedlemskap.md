

# Slot: klassemedlemskap 



URI: [https://schema.fintlabs.no/utdanning/:klassemedlemskap](https://schema.fintlabs.no/utdanning/:klassemedlemskap)
Alias: klassemedlemskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Elevforhold](Elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |
| [Klasse](Klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [UtdanningContainer](UtdanningContainer.md), [Elevforhold](Elevforhold.md), [Klasse](Klasse.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:klassemedlemskap |
| native | https://schema.fintlabs.no/utdanning/:klassemedlemskap |




## LinkML Source

<details>
```yaml
name: klassemedlemskap
alias: klassemedlemskap
domain_of:
- UtdanningContainer
- Elevforhold
- Klasse
range: string

```
</details>