

# Slot: prokuraer 



URI: [https://data.norge.no/linkml/ngr-virksomhet/prokuraer](https://data.norge.no/linkml/ngr-virksomhet/prokuraer)
Alias: prokuraer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirksomhetContainer](virksomhetcontainer.md) | Rotklasse for NGR-virksomhet-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Prokura](prokura.md) |
| Domain Of | [VirksomhetContainer](virksomhetcontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [VirksomhetContainer](virksomhetcontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/ngr-virksomhet/prokuraer |
| native | https://data.norge.no/linkml/ngr-virksomhet/prokuraer |




## LinkML Source

<details>
```yaml
name: prokuraer
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
alias: prokuraer
owner: VirksomhetContainer
domain_of:
- VirksomhetContainer
range: Prokura
multivalued: true
inlined: true
inlined_as_list: true

```
</details>