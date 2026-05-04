

# Slot: sivilstand 



URI: [https://data.norge.no/linkml/ngr-person/sivilstand](https://data.norge.no/linkml/ngr-person/sivilstand)
Alias: sivilstand

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Sivilstand](Sivilstand.md) |
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
| self | https://data.norge.no/linkml/ngr-person/sivilstand |
| native | https://data.norge.no/linkml/ngr-person/sivilstand |




## LinkML Source

<details>
```yaml
name: sivilstand
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: sivilstand
owner: PersonContainer
domain_of:
- PersonContainer
range: Sivilstand
multivalued: true
inlined: true
inlined_as_list: true

```
</details>