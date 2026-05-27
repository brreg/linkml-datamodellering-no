

# Slot: posteringar 



URI: [https://schema.fintlabs.no/okonomi/:posteringar](https://schema.fintlabs.no/okonomi/:posteringar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OkonomiContainer](okonomicontainer.md) | Rotcontainer for FINT Økonomi-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Postering](postering.md) |
| Domain Of | [OkonomiContainer](okonomicontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [OkonomiContainer](okonomicontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:posteringar |
| native | https://schema.fintlabs.no/okonomi/:posteringar |




## LinkML Source

<details>
```yaml
name: posteringar
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
owner: OkonomiContainer
domain_of:
- OkonomiContainer
range: Postering
multivalued: true
inlined: true
inlined_as_list: true

```
</details>