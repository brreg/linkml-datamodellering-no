

# Slot: behandlingar 



URI: [pvn:behandlingar](https://schema.fintlabs.no/personvern/behandlingar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonvernContainer](personverncontainer.md) | Rotcontainer for FINT Personvern-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Behandling](behandling.md) |
| Domain Of | [PersonvernContainer](personverncontainer.md) |
| Slot URI | [pvn:behandlingar](https://schema.fintlabs.no/personvern/behandlingar) |

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
| self | pvn:behandlingar |
| native | https://schema.fintlabs.no/personvern/:behandlingar |




## LinkML Source

<details>
```yaml
name: behandlingar
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:behandlingar
domain_of:
- PersonvernContainer
range: Behandling
multivalued: true
inlined: true
inlined_as_list: true

```
</details>