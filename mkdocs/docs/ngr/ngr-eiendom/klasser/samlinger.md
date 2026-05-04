

# Slot: samlinger 



URI: [https://data.norge.no/linkml/ngr-eiendom/samlinger](https://data.norge.no/linkml/ngr-eiendom/samlinger)
Alias: samlinger

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](EiendomContainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SamletFastEiendom](SamletFastEiendom.md) |
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
| self | https://data.norge.no/linkml/ngr-eiendom/samlinger |
| native | https://data.norge.no/linkml/ngr-eiendom/samlinger |




## LinkML Source

<details>
```yaml
name: samlinger
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
alias: samlinger
owner: EiendomContainer
domain_of:
- EiendomContainer
range: SamletFastEiendom
multivalued: true
inlined: true
inlined_as_list: true

```
</details>