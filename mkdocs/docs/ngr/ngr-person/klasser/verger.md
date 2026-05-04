

# Slot: verger 



URI: [https://data.norge.no/linkml/ngr-person/verger](https://data.norge.no/linkml/ngr-person/verger)
Alias: verger

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Verge](Verge.md) |
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
| self | https://data.norge.no/linkml/ngr-person/verger |
| native | https://data.norge.no/linkml/ngr-person/verger |




## LinkML Source

<details>
```yaml
name: verger
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: verger
owner: PersonContainer
domain_of:
- PersonContainer
range: Verge
multivalued: true
inlined: true
inlined_as_list: true

```
</details>