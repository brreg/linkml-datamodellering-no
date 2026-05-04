

# Slot: personar 



URI: [https://data.norge.no/linkml/ngr-person/personar](https://data.norge.no/linkml/ngr-person/personar)
Alias: personar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](Person.md) |
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
| self | https://data.norge.no/linkml/ngr-person/personar |
| native | https://data.norge.no/linkml/ngr-person/personar |




## LinkML Source

<details>
```yaml
name: personar
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: personar
owner: PersonContainer
domain_of:
- PersonContainer
range: Person
multivalued: true
inlined: true
inlined_as_list: true

```
</details>