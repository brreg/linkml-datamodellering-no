

# Slot: tilrettelegging 



URI: [https://schema.fintlabs.no/utdanning/:tilrettelegging](https://schema.fintlabs.no/utdanning/:tilrettelegging)
Alias: tilrettelegging

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevtilrettelegging](elevtilrettelegging.md) | Tilrettelegging for ein elev i eit elevforhold |  no  |
| [Fag](fag.md) | Eit skulefag |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Elevforhold](elevforhold.md), [Elevtilrettelegging](elevtilrettelegging.md), [Fag](fag.md) |

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