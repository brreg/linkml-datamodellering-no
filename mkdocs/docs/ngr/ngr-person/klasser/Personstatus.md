

# Slot: personstatus 



URI: [https://data.norge.no/linkml/ngr-person/personstatus](https://data.norge.no/linkml/ngr-person/personstatus)
Alias: personstatus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personstatus](Personstatus.md) |
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
| self | https://data.norge.no/linkml/ngr-person/personstatus |
| native | https://data.norge.no/linkml/ngr-person/personstatus |




## LinkML Source

<details>
```yaml
name: personstatus
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: personstatus
owner: PersonContainer
domain_of:
- PersonContainer
range: Personstatus
multivalued: true
inlined: true
inlined_as_list: true

```
</details>