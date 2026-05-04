

# Slot: teiger 



URI: [https://data.norge.no/linkml/ngr-eiendom/teiger](https://data.norge.no/linkml/ngr-eiendom/teiger)
Alias: teiger

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](EiendomContainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Teig](Teig.md) |
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
| self | https://data.norge.no/linkml/ngr-eiendom/teiger |
| native | https://data.norge.no/linkml/ngr-eiendom/teiger |




## LinkML Source

<details>
```yaml
name: teiger
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
alias: teiger
owner: EiendomContainer
domain_of:
- EiendomContainer
range: Teig
multivalued: true
inlined: true
inlined_as_list: true

```
</details>