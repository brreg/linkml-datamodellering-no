

# Slot: tilrettelegging 



URI: [https://schema.fintlabs.no/utdanning/:tilrettelegging](https://schema.fintlabs.no/utdanning/:tilrettelegging)
Alias: tilrettelegging

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fag](Fag.md) | Eit skulefag |  no  |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Elevforhold](Elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |
| [Elevtilrettelegging](Elevtilrettelegging.md) | Tilrettelegging for ein elev i eit elevforhold |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [UtdanningContainer](UtdanningContainer.md), [Elevforhold](Elevforhold.md), [Elevtilrettelegging](Elevtilrettelegging.md), [Fag](Fag.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:tilrettelegging |
| native | https://schema.fintlabs.no/utdanning/:tilrettelegging |




## LinkML Source

<details>
```yaml
name: tilrettelegging
alias: tilrettelegging
domain_of:
- UtdanningContainer
- Elevforhold
- Elevtilrettelegging
- Fag
range: string

```
</details>