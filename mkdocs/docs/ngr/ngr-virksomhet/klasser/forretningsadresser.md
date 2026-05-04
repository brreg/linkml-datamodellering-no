

# Slot: forretningsadresser 



URI: [https://data.norge.no/linkml/ngr-virksomhet/forretningsadresser](https://data.norge.no/linkml/ngr-virksomhet/forretningsadresser)
Alias: forretningsadresser

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirksomhetContainer](VirksomhetContainer.md) | Rotklasse for NGR-virksomhet-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Forretningsadresse](Forretningsadresse.md) |
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
| self | https://data.norge.no/linkml/ngr-virksomhet/forretningsadresser |
| native | https://data.norge.no/linkml/ngr-virksomhet/forretningsadresser |




## LinkML Source

<details>
```yaml
name: forretningsadresser
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
alias: forretningsadresser
owner: VirksomhetContainer
domain_of:
- VirksomhetContainer
range: Forretningsadresse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>