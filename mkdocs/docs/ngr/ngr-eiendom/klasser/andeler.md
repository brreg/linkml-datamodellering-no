

# Slot: andeler 



URI: [https://data.norge.no/linkml/ngr-eiendom/andeler](https://data.norge.no/linkml/ngr-eiendom/andeler)
Alias: andeler

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](EiendomContainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Andel](Andel.md) |
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
| self | https://data.norge.no/linkml/ngr-eiendom/andeler |
| native | https://data.norge.no/linkml/ngr-eiendom/andeler |




## LinkML Source

<details>
```yaml
name: andeler
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
alias: andeler
owner: EiendomContainer
domain_of:
- EiendomContainer
range: Andel
multivalued: true
inlined: true
inlined_as_list: true

```
</details>