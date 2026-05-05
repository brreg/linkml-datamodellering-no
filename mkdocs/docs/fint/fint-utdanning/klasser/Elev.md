

# Slot: elev 



URI: [https://schema.fintlabs.no/utdanning/:elev](https://schema.fintlabs.no/utdanning/:elev)
Alias: elev

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |
| [Elevtilrettelegging](elevtilrettelegging.md) | Tilrettelegging for ein elev i eit elevforhold |  no  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Elevforhold](elevforhold.md), [Elevtilrettelegging](elevtilrettelegging.md), [Persongruppe](persongruppe.md), [Person](person.md) |

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