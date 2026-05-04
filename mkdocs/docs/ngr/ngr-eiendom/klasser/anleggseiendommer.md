

# Slot: anleggseiendommer 



URI: [https://data.norge.no/linkml/ngr-eiendom/anleggseiendommer](https://data.norge.no/linkml/ngr-eiendom/anleggseiendommer)
Alias: anleggseiendommer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](EiendomContainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Anleggseiendom](Anleggseiendom.md) |
| Domain Of | [EiendomContainer](EiendomContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EiendomContainer](EiendomContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/ngr-eiendom/anleggseiendommer |
| native | https://data.norge.no/linkml/ngr-eiendom/anleggseiendommer |




## LinkML Source

<details>
```yaml
name: anleggseiendommer
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
alias: anleggseiendommer
owner: EiendomContainer
domain_of:
- EiendomContainer
range: Anleggseiendom
multivalued: true
inlined: true
inlined_as_list: true

```
</details>