

# Slot: klassemedlemskap 



URI: [https://schema.fintlabs.no/utdanning/:klassemedlemskap](https://schema.fintlabs.no/utdanning/:klassemedlemskap)
Alias: klassemedlemskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Klasse](klasse.md) |

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