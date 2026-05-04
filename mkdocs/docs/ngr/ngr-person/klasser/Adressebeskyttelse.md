

# Slot: adressebeskyttelse 



URI: [https://data.norge.no/linkml/ngr-person/adressebeskyttelse](https://data.norge.no/linkml/ngr-person/adressebeskyttelse)
Alias: adressebeskyttelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adressebeskyttelse](Adressebeskyttelse.md) |
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
| self | https://data.norge.no/linkml/ngr-person/adressebeskyttelse |
| native | https://data.norge.no/linkml/ngr-person/adressebeskyttelse |




## LinkML Source

<details>
```yaml
name: adressebeskyttelse
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: adressebeskyttelse
owner: PersonContainer
domain_of:
- PersonContainer
range: Adressebeskyttelse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>