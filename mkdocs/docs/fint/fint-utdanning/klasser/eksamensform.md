

# Slot: eksamensform 


_Eksamensform._





URI: [utd:eksamensform](https://schema.fintlabs.no/utdanning/eksamensform)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevtilrettelegging](elevtilrettelegging.md) | Tilrettelegging for ein elev i eit elevforhold |  yes  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eksamensform](eksamensform.md) |
| Domain Of | [Elevtilrettelegging](elevtilrettelegging.md), [Eksamensgruppe](eksamensgruppe.md) |
| Slot URI | [utd:eksamensform](https://schema.fintlabs.no/utdanning/eksamensform) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:eksamensform |
| native | https://schema.fintlabs.no/utdanning/:eksamensform |




## LinkML Source

<details>
```yaml
name: eksamensform
description: Eksamensform.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:eksamensform
domain_of:
- Elevtilrettelegging
- Eksamensgruppe
range: Eksamensform

```
</details>