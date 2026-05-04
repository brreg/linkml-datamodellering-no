

# Slot: stemmekretsar 



URI: [https://data.norge.no/linkml/ngr-adresse/stemmekretsar](https://data.norge.no/linkml/ngr-adresse/stemmekretsar)
Alias: stemmekretsar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdresseContainer](AdresseContainer.md) | Rotklasse for NGR-adresse-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Stemmekrets](Stemmekrets.md) |
| Domain Of | [AdresseContainer](AdresseContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AdresseContainer](AdresseContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/ngr-adresse/stemmekretsar |
| native | https://data.norge.no/linkml/ngr-adresse/stemmekretsar |




## LinkML Source

<details>
```yaml
name: stemmekretsar
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
alias: stemmekretsar
owner: AdresseContainer
domain_of:
- AdresseContainer
range: Stemmekrets
multivalued: true
inlined: true
inlined_as_list: true

```
</details>