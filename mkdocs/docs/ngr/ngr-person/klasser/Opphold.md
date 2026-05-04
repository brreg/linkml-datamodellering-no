

# Slot: opphold 



URI: [https://data.norge.no/linkml/ngr-person/opphold](https://data.norge.no/linkml/ngr-person/opphold)
Alias: opphold

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Opphold](Opphold.md) |
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
| self | https://data.norge.no/linkml/ngr-person/opphold |
| native | https://data.norge.no/linkml/ngr-person/opphold |




## LinkML Source

<details>
```yaml
name: opphold
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: opphold
owner: PersonContainer
domain_of:
- PersonContainer
range: Opphold
multivalued: true
inlined: true
inlined_as_list: true

```
</details>