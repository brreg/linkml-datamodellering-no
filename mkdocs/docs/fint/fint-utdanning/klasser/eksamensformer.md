

# Slot: eksamensformer 


_Alle eksamensformer i containeren._





URI: [utd:eksamensformer](https://schema.fintlabs.no/utdanning/eksamensformer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eksamensform](eksamensform.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:eksamensformer](https://schema.fintlabs.no/utdanning/eksamensformer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:eksamensformer |
| native | https://schema.fintlabs.no/utdanning/:eksamensformer |




## LinkML Source

<details>
```yaml
name: eksamensformer
description: Alle eksamensformer i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:eksamensformer
domain_of:
- UtdanningContainer
range: Eksamensform
multivalued: true
inlined: true
inlined_as_list: true

```
</details>