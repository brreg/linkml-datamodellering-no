

# Slot: foedslar 



URI: [https://data.norge.no/linkml/ngr-person/foedslar](https://data.norge.no/linkml/ngr-person/foedslar)
Alias: foedslar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Foedsel](Foedsel.md) |
| Domain Of | [PersonContainer](PersonContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PersonContainer](PersonContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/ngr-person/foedslar |
| native | https://data.norge.no/linkml/ngr-person/foedslar |




## LinkML Source

<details>
```yaml
name: foedslar
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: foedslar
owner: PersonContainer
domain_of:
- PersonContainer
range: Foedsel
multivalued: true
inlined: true
inlined_as_list: true

```
</details>