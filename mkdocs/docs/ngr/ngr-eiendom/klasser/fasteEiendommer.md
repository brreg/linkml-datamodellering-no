

# Slot: fasteEiendommer 



URI: [https://data.norge.no/linkml/ngr-eiendom/fasteEiendommer](https://data.norge.no/linkml/ngr-eiendom/fasteEiendommer)
Alias: fasteEiendommer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](EiendomContainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FastEiendom](FastEiendom.md) |
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
| self | https://data.norge.no/linkml/ngr-eiendom/fasteEiendommer |
| native | https://data.norge.no/linkml/ngr-eiendom/fasteEiendommer |




## LinkML Source

<details>
```yaml
name: fasteEiendommer
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
alias: fasteEiendommer
owner: EiendomContainer
domain_of:
- EiendomContainer
range: FastEiendom
multivalued: true
inlined: true
inlined_as_list: true

```
</details>