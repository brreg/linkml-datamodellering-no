

# Slot: tilskuddFartoy_liste 



URI: [https://schema.fintlabs.no/arkiv/:tilskuddFartoy_liste](https://schema.fintlabs.no/arkiv/:tilskuddFartoy_liste)
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

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ArkivContainer](arkivcontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:tilskuddFartoy_liste |
| native | https://schema.fintlabs.no/arkiv/:tilskuddFartoy_liste |




## LinkML Source

<details>
```yaml
name: tilskuddFartoy_liste
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
owner: ArkivContainer
domain_of:
- ArkivContainer
range: TilskuddFartoy
multivalued: true
inlined: true
inlined_as_list: true

```
</details>