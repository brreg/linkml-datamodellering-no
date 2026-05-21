

# Slot: tilknyttetRegistreringSomKodar 



URI: [ark:tilknyttetRegistreringSomKodar](https://schema.fintlabs.no/arkiv/tilknyttetRegistreringSomKodar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TilknyttetRegistreringSom](tilknyttetregistreringsom.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:tilknyttetRegistreringSomKodar](https://schema.fintlabs.no/arkiv/tilknyttetRegistreringSomKodar) |

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
| self | ark:tilknyttetRegistreringSomKodar |
| native | https://schema.fintlabs.no/arkiv/:tilknyttetRegistreringSomKodar |




## LinkML Source

<details>
```yaml
name: tilknyttetRegistreringSomKodar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:tilknyttetRegistreringSomKodar
domain_of:
- ArkivContainer
range: TilknyttetRegistreringSom
multivalued: true
inlined: true
inlined_as_list: true

```
</details>