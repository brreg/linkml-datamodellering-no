

# Slot: bygninger 



URI: [https://data.norge.no/linkml/ngr-eiendom/bygninger](https://data.norge.no/linkml/ngr-eiendom/bygninger)
Alias: bygninger

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EiendomContainer](eiendomcontainer.md) | Rotklasse for NGR-eiendom-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bygning](bygning.md) |
| Domain Of | [EiendomContainer](eiendomcontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EiendomContainer](eiendomcontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/ngr-eiendom/bygninger |
| native | https://data.norge.no/linkml/ngr-eiendom/bygninger |




## LinkML Source

<details>
```yaml
name: bygninger
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
alias: bygninger
owner: EiendomContainer
domain_of:
- EiendomContainer
range: Bygning
multivalued: true
inlined: true
inlined_as_list: true

```
</details>