

# Slot: rolleinnehavere 



URI: [https://data.norge.no/linkml/ngr-virksomhet/rolleinnehavere](https://data.norge.no/linkml/ngr-virksomhet/rolleinnehavere)
Alias: rolleinnehavere

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirksomhetContainer](VirksomhetContainer.md) | Rotklasse for NGR-virksomhet-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rolleinnehaver](Rolleinnehaver.md) |
| Domain Of | [VirksomhetContainer](VirksomhetContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [VirksomhetContainer](VirksomhetContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/ngr-virksomhet/rolleinnehavere |
| native | https://data.norge.no/linkml/ngr-virksomhet/rolleinnehavere |




## LinkML Source

<details>
```yaml
name: rolleinnehavere
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
alias: rolleinnehavere
owner: VirksomhetContainer
domain_of:
- VirksomhetContainer
range: Rolleinnehaver
multivalued: true
inlined: true
inlined_as_list: true

```
</details>