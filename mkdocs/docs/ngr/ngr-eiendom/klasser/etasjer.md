

# Slot: etasjer 



URI: [https://data.norge.no/linkml/ngr-eiendom/etasjer](https://data.norge.no/linkml/ngr-eiendom/etasjer)
Alias: etasjer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](EiendomContainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Etasje](Etasje.md) |
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
| self | https://data.norge.no/linkml/ngr-eiendom/etasjer |
| native | https://data.norge.no/linkml/ngr-eiendom/etasjer |




## LinkML Source

<details>
```yaml
name: etasjer
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
alias: etasjer
owner: EiendomContainer
domain_of:
- EiendomContainer
range: Etasje
multivalued: true
inlined: true
inlined_as_list: true

```
</details>