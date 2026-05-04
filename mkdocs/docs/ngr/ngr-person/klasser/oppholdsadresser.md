

# Slot: oppholdsadresser 



URI: [https://data.norge.no/linkml/ngr-person/oppholdsadresser](https://data.norge.no/linkml/ngr-person/oppholdsadresser)
Alias: oppholdsadresser

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Oppholdsadresse](Oppholdsadresse.md) |
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
| self | https://data.norge.no/linkml/ngr-person/oppholdsadresser |
| native | https://data.norge.no/linkml/ngr-person/oppholdsadresser |




## LinkML Source

<details>
```yaml
name: oppholdsadresser
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: oppholdsadresser
owner: PersonContainer
domain_of:
- PersonContainer
range: Oppholdsadresse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>