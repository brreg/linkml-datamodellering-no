

# Slot: samtykker 



URI: [pvn:samtykker](https://schema.fintlabs.no/personvern/samtykker)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonvernContainer](personverncontainer.md) | Rotcontainer for FINT Personvern-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Samtykke](samtykke.md) |
| Domain Of | [PersonvernContainer](personverncontainer.md) |
| Slot URI | [pvn:samtykker](https://schema.fintlabs.no/personvern/samtykker) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pvn:samtykker |
| native | https://schema.fintlabs.no/personvern/:samtykker |




## LinkML Source

<details>
```yaml
name: samtykker
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:samtykker
domain_of:
- PersonvernContainer
range: Samtykke
multivalued: true
inlined: true
inlined_as_list: true

```
</details>