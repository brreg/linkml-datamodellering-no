

# Slot: underenheter 



URI: [https://data.norge.no/linkml/ngr-virksomhet/underenheter](https://data.norge.no/linkml/ngr-virksomhet/underenheter)
Alias: underenheter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirksomhetContainer](VirksomhetContainer.md) | Rotklasse for NGR-virksomhet-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Underenhet](Underenhet.md) |
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
| self | https://data.norge.no/linkml/ngr-virksomhet/underenheter |
| native | https://data.norge.no/linkml/ngr-virksomhet/underenheter |




## LinkML Source

<details>
```yaml
name: underenheter
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
alias: underenheter
owner: VirksomhetContainer
domain_of:
- VirksomhetContainer
range: Underenhet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>