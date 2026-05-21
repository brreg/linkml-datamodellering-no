

# Slot: tilskuddFartoy_liste 



URI: [ark:tilskuddFartoy](https://schema.fintlabs.no/arkiv/tilskuddFartoy)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TilskuddFartoy](tilskuddfartoy.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:tilskuddFartoy](https://schema.fintlabs.no/arkiv/tilskuddFartoy) |

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
| self | ark:tilskuddFartoy |
| native | https://schema.fintlabs.no/arkiv/:tilskuddFartoy_liste |




## LinkML Source

<details>
```yaml
name: tilskuddFartoy_liste
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:tilskuddFartoy
domain_of:
- ArkivContainer
range: TilskuddFartoy
multivalued: true
inlined: true
inlined_as_list: true

```
</details>