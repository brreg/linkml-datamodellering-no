

# Slot: merverdiavgifter 



URI: [https://schema.fintlabs.no/okonomi/:merverdiavgifter](https://schema.fintlabs.no/okonomi/:merverdiavgifter)
Alias: merverdiavgifter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OkonomiContainer](OkonomiContainer.md) | Rotcontainer for FINT Økonomi-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Merverdiavgift](Merverdiavgift.md) |
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
| self | https://schema.fintlabs.no/okonomi/:merverdiavgifter |
| native | https://schema.fintlabs.no/okonomi/:merverdiavgifter |




## LinkML Source

<details>
```yaml
name: merverdiavgifter
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
alias: merverdiavgifter
owner: OkonomiContainer
domain_of:
- OkonomiContainer
range: Merverdiavgift
multivalued: true
inlined: true
inlined_as_list: true

```
</details>