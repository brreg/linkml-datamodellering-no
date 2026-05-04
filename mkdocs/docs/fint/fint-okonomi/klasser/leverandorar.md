

# Slot: leverandorar 



URI: [https://schema.fintlabs.no/okonomi/:leverandorar](https://schema.fintlabs.no/okonomi/:leverandorar)
Alias: leverandorar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OkonomiContainer](OkonomiContainer.md) | Rotcontainer for FINT Økonomi-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Leverandor](Leverandor.md) |
| Domain Of | [OkonomiContainer](OkonomiContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [OkonomiContainer](OkonomiContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:leverandorar |
| native | https://schema.fintlabs.no/okonomi/:leverandorar |




## LinkML Source

<details>
```yaml
name: leverandorar
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
alias: leverandorar
owner: OkonomiContainer
domain_of:
- OkonomiContainer
range: Leverandor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>