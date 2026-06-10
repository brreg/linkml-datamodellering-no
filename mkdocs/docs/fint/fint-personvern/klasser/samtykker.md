

# Slot: samtykker 



URI: [https://data.norge.no/fint/fint-personvern/samtykker](https://data.norge.no/fint/fint-personvern/samtykker)
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
| self | https://data.norge.no/fint/fint-personvern/samtykker |
| native | https://data.norge.no/fint/fint-personvern/samtykker |




## LinkML Source

<details>
```yaml
name: samtykker
from_schema: https://data.norge.no/fint/fint-personvern
rank: 1000
owner: PersonvernContainer
domain_of:
- PersonvernContainer
range: Samtykke
multivalued: true
inlined: true
inlined_as_list: true

```
</details>