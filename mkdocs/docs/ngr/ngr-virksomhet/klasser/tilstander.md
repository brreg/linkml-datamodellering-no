

# Slot: tilstander 



URI: [https://data.norge.no/linkml/ngr-virksomhet/tilstander](https://data.norge.no/linkml/ngr-virksomhet/tilstander)
Alias: tilstander

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirksomhetContainer](VirksomhetContainer.md) | Rotklasse for NGR-virksomhet-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tilstand](Tilstand.md) |
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
| self | https://data.norge.no/linkml/ngr-virksomhet/tilstander |
| native | https://data.norge.no/linkml/ngr-virksomhet/tilstander |




## LinkML Source

<details>
```yaml
name: tilstander
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
alias: tilstander
owner: VirksomhetContainer
domain_of:
- VirksomhetContainer
range: Tilstand
multivalued: true
inlined: true
inlined_as_list: true

```
</details>