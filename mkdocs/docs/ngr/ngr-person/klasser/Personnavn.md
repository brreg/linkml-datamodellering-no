

# Slot: personnavn 



URI: [https://data.norge.no/linkml/ngr-person/personnavn](https://data.norge.no/linkml/ngr-person/personnavn)
Alias: personnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](personcontainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personnavn](personnavn.md) |
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
| self | https://data.norge.no/linkml/ngr-person/personnavn |
| native | https://data.norge.no/linkml/ngr-person/personnavn |




## LinkML Source

<details>
```yaml
name: personnavn
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: personnavn
owner: PersonContainer
domain_of:
- PersonContainer
range: Personnavn
multivalued: true
inlined: true
inlined_as_list: true

```
</details>