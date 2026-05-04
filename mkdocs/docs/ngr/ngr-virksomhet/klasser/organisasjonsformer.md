

# Slot: organisasjonsformer 



URI: [https://data.norge.no/linkml/ngr-virksomhet/organisasjonsformer](https://data.norge.no/linkml/ngr-virksomhet/organisasjonsformer)
Alias: organisasjonsformer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirksomhetContainer](VirksomhetContainer.md) | Rotklasse for NGR-virksomhet-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Organisasjonsform](Organisasjonsform.md) |
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
| self | https://data.norge.no/linkml/ngr-virksomhet/organisasjonsformer |
| native | https://data.norge.no/linkml/ngr-virksomhet/organisasjonsformer |




## LinkML Source

<details>
```yaml
name: organisasjonsformer
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
alias: organisasjonsformer
owner: VirksomhetContainer
domain_of:
- VirksomhetContainer
range: Organisasjonsform
multivalued: true
inlined: true
inlined_as_list: true

```
</details>