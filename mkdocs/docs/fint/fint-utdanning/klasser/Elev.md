

# Slot: elev 



URI: [https://schema.fintlabs.no/utdanning/:elev](https://schema.fintlabs.no/utdanning/:elev)
Alias: elev

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Fysiske private personar |  no  |
| [Persongruppe](Persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Elevforhold](Elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |
| [Elevtilrettelegging](Elevtilrettelegging.md) | Tilrettelegging for ein elev i eit elevforhold |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Elevforhold](Elevforhold.md), [Elevtilrettelegging](Elevtilrettelegging.md), [Persongruppe](Persongruppe.md), [Person](Person.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:elev |
| native | https://schema.fintlabs.no/utdanning/:elev |




## LinkML Source

<details>
```yaml
name: elev
alias: elev
domain_of:
- Elevforhold
- Elevtilrettelegging
- Persongruppe
- Person
range: string

```
</details>