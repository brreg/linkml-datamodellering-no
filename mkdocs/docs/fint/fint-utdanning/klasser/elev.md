

# Slot: elev 


_Referanse til Elev (Utdanning)._





URI: [fint:elev](https://schema.fintlabs.no/elev)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  yes  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |
| [Elevtilrettelegging](elevtilrettelegging.md) | Tilrettelegging for ein elev i eit elevforhold |  yes  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elev](elev.md) |
| Domain Of | [Person](person.md), [Elevforhold](elevforhold.md), [Elevtilrettelegging](elevtilrettelegging.md), [Persongruppe](persongruppe.md) |
| Slot URI | [fint:elev](https://schema.fintlabs.no/elev) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:elev |
| native | https://schema.fintlabs.no/:elev |




## LinkML Source

<details>
```yaml
name: elev
description: Referanse til Elev (Utdanning).
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:elev
domain_of:
- Person
- Elevforhold
- Elevtilrettelegging
- Persongruppe
range: Elev

```
</details>