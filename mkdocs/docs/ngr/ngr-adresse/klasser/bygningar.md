

# Slot: bygningar 



URI: [https://data.norge.no/linkml/ngr-adresse/bygningar](https://data.norge.no/linkml/ngr-adresse/bygningar)
Alias: bygningar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdresseContainer](AdresseContainer.md) | Rotklasse for NGR-adresse-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bygning](Bygning.md) |
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
| self | https://data.norge.no/linkml/ngr-adresse/bygningar |
| native | https://data.norge.no/linkml/ngr-adresse/bygningar |




## LinkML Source

<details>
```yaml
name: bygningar
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
alias: bygningar
owner: AdresseContainer
domain_of:
- AdresseContainer
range: Bygning
multivalued: true
inlined: true
inlined_as_list: true

```
</details>