

# Slot: husnummer 



URI: [https://data.norge.no/linkml/ngr-adresse/husnummer](https://data.norge.no/linkml/ngr-adresse/husnummer)
Alias: husnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdresseContainer](AdresseContainer.md) | Rotklasse for NGR-adresse-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Husnummer](Husnummer.md) |
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
| self | https://data.norge.no/linkml/ngr-adresse/husnummer |
| native | https://data.norge.no/linkml/ngr-adresse/husnummer |




## LinkML Source

<details>
```yaml
name: husnummer
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
alias: husnummer
owner: AdresseContainer
domain_of:
- AdresseContainer
range: Husnummer
multivalued: true
inlined: true
inlined_as_list: true

```
</details>