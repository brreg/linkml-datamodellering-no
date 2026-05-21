

# Slot: tilgangar 



URI: [ark:tilgangar](https://schema.fintlabs.no/arkiv/tilgangar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tilgang](tilgang.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:tilgangar](https://schema.fintlabs.no/arkiv/tilgangar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:tilgangar |
| native | https://schema.fintlabs.no/arkiv/:tilgangar |




## LinkML Source

<details>
```yaml
name: tilgangar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:tilgangar
domain_of:
- ArkivContainer
range: Tilgang
multivalued: true
inlined: true
inlined_as_list: true

```
</details>