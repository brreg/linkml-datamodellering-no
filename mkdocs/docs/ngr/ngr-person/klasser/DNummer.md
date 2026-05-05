

# Slot: dnummer 



URI: [https://data.norge.no/linkml/ngr-person/dnummer](https://data.norge.no/linkml/ngr-person/dnummer)
Alias: dnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](personcontainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DNummer](dnummer.md) |
| Domain Of | [PersonContainer](personcontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PersonContainer](personcontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/ngr-person/dnummer |
| native | https://data.norge.no/linkml/ngr-person/dnummer |




## LinkML Source

<details>
```yaml
name: dnummer
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: dnummer
owner: PersonContainer
domain_of:
- PersonContainer
range: DNummer
multivalued: true
inlined: true
inlined_as_list: true

```
</details>