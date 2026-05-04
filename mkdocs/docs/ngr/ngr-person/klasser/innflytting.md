

# Slot: innflytting 



URI: [https://data.norge.no/linkml/ngr-person/innflytting](https://data.norge.no/linkml/ngr-person/innflytting)
Alias: innflytting

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonContainer](PersonContainer.md) | Rotklasse for NGR-person-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InnflyttingTilNorge](InnflyttingTilNorge.md) |
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
| self | https://data.norge.no/linkml/ngr-person/innflytting |
| native | https://data.norge.no/linkml/ngr-person/innflytting |




## LinkML Source

<details>
```yaml
name: innflytting
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
alias: innflytting
owner: PersonContainer
domain_of:
- PersonContainer
range: InnflyttingTilNorge
multivalued: true
inlined: true
inlined_as_list: true

```
</details>