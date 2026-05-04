

# Slot: utflytting 



URI: [https://data.norge.no/linkml/ngr-person/utflytting](https://data.norge.no/linkml/ngr-person/utflytting)
Alias: utflytting

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [UtflyttingFraNorge](UtflyttingFraNorge.md) |
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
| self | https://data.norge.no/linkml/ngr-person/utflytting |
| native | https://data.norge.no/linkml/ngr-person/utflytting |




## LinkML Source

<details>
```yaml
name: utflytting
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: utflytting
owner: PersonContainer
domain_of:
- PersonContainer
range: UtflyttingFraNorge
multivalued: true
inlined: true
inlined_as_list: true

```
</details>