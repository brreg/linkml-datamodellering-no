

# Slot: tenester 



URI: [pvn:tenester](https://schema.fintlabs.no/personvern/tenester)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonvernContainer](personverncontainer.md) | Rotcontainer for FINT Personvern-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tjeneste](tjeneste.md) |
| Domain Of | [PersonvernContainer](personverncontainer.md) |
| Slot URI | [pvn:tenester](https://schema.fintlabs.no/personvern/tenester) |

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
| self | pvn:tenester |
| native | https://schema.fintlabs.no/personvern/:tenester |




## LinkML Source

<details>
```yaml
name: tenester
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:tenester
domain_of:
- PersonvernContainer
range: Tjeneste
multivalued: true
inlined: true
inlined_as_list: true

```
</details>