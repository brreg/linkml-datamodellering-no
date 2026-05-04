

# Slot: spraak 



URI: [https://data.norge.no/linkml/ngr-person/spraak](https://data.norge.no/linkml/ngr-person/spraak)
Alias: spraak

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SpraakForElektroniskKommunikasjon](SpraakForElektroniskKommunikasjon.md) |
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
| self | https://data.norge.no/linkml/ngr-person/spraak |
| native | https://data.norge.no/linkml/ngr-person/spraak |




## LinkML Source

<details>
```yaml
name: spraak
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: spraak
owner: PersonContainer
domain_of:
- PersonContainer
range: SpraakForElektroniskKommunikasjon
multivalued: true
inlined: true
inlined_as_list: true

```
</details>