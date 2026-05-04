

# Slot: falskIdentitetar 



URI: [https://data.norge.no/linkml/ngr-person/falskIdentitetar](https://data.norge.no/linkml/ngr-person/falskIdentitetar)
Alias: falskIdentitetar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FalskIdentitet](FalskIdentitet.md) |
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
| self | https://data.norge.no/linkml/ngr-person/falskIdentitetar |
| native | https://data.norge.no/linkml/ngr-person/falskIdentitetar |




## LinkML Source

<details>
```yaml
name: falskIdentitetar
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: falskIdentitetar
owner: PersonContainer
domain_of:
- PersonContainer
range: FalskIdentitet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>