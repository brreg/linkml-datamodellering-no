

# Slot: bestar_av_fast_eiendom 


_Faste eigedommar som inngår i samlinga (minimum 2)._





URI: [ngre:bestarAvFastEiendom](https://data.norge.no/vocabulary/ngr-eiendom#bestarAvFastEiendom)
Alias: bestar_av_fast_eiendom

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SamletFastEiendom](SamletFastEiendom.md) | Samling av to eller fleire faste eigedommar som er organiserte saman |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FastEiendom](FastEiendom.md) |
| Domain Of | [SamletFastEiendom](SamletFastEiendom.md) |
| Slot URI | [ngre:bestarAvFastEiendom](https://data.norge.no/vocabulary/ngr-eiendom#bestarAvFastEiendom) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:bestarAvFastEiendom |
| native | https://data.norge.no/linkml/ngr-eiendom/bestar_av_fast_eiendom |




## LinkML Source

<details>
```yaml
name: bestar_av_fast_eiendom
description: Faste eigedommar som inngår i samlinga (minimum 2).
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:bestarAvFastEiendom
alias: bestar_av_fast_eiendom
domain_of:
- SamletFastEiendom
range: FastEiendom
multivalued: true

```
</details>