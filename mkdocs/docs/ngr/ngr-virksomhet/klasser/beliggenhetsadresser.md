

# Slot: beliggenhetsadresser 



URI: [https://data.norge.no/linkml/ngr-virksomhet/beliggenhetsadresser](https://data.norge.no/linkml/ngr-virksomhet/beliggenhetsadresser)
Alias: beliggenhetsadresser

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirksomhetContainer](VirksomhetContainer.md) | Rotklasse for NGR-virksomhet-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Beliggenhetsadresse](Beliggenhetsadresse.md) |
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
| self | https://data.norge.no/linkml/ngr-virksomhet/beliggenhetsadresser |
| native | https://data.norge.no/linkml/ngr-virksomhet/beliggenhetsadresser |




## LinkML Source

<details>
```yaml
name: beliggenhetsadresser
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
alias: beliggenhetsadresser
owner: VirksomhetContainer
domain_of:
- VirksomhetContainer
range: Beliggenhetsadresse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>