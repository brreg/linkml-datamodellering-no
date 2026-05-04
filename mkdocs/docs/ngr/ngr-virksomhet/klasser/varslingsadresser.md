

# Slot: varslingsadresser 



URI: [https://data.norge.no/linkml/ngr-virksomhet/varslingsadresser](https://data.norge.no/linkml/ngr-virksomhet/varslingsadresser)
Alias: varslingsadresser

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirksomhetContainer](VirksomhetContainer.md) | Rotklasse for NGR-virksomhet-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Varslingsadresse](Varslingsadresse.md) |
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
| self | https://data.norge.no/linkml/ngr-virksomhet/varslingsadresser |
| native | https://data.norge.no/linkml/ngr-virksomhet/varslingsadresser |




## LinkML Source

<details>
```yaml
name: varslingsadresser
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
alias: varslingsadresser
owner: VirksomhetContainer
domain_of:
- VirksomhetContainer
range: Varslingsadresse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>