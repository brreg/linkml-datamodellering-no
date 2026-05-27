

# Slot: tenester 



URI: [https://schema.fintlabs.no/personvern/:tenester](https://schema.fintlabs.no/personvern/:tenester)
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

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PersonvernContainer](personverncontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/personvern/:tenester |
| native | https://schema.fintlabs.no/personvern/:tenester |




## LinkML Source

<details>
```yaml
name: tenester
from_schema: https://data.norge.no/fint/fint-personvern
rank: 1000
owner: PersonvernContainer
domain_of:
- PersonvernContainer
range: Tjeneste
multivalued: true
inlined: true
inlined_as_list: true

```
</details>