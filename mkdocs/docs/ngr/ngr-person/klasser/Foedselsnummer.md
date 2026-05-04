

# Slot: foedselsnummer 



URI: [https://data.norge.no/linkml/ngr-person/foedselsnummer](https://data.norge.no/linkml/ngr-person/foedselsnummer)
Alias: foedselsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Foedselsnummer](Foedselsnummer.md) |
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
| self | https://data.norge.no/linkml/ngr-person/foedselsnummer |
| native | https://data.norge.no/linkml/ngr-person/foedselsnummer |




## LinkML Source

<details>
```yaml
name: foedselsnummer
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: foedselsnummer
owner: PersonContainer
domain_of:
- PersonContainer
range: Foedselsnummer
multivalued: true
inlined: true
inlined_as_list: true

```
</details>