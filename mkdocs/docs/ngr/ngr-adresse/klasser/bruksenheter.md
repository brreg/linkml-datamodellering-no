

# Slot: bruksenheter 



URI: [https://data.norge.no/linkml/ngr-adresse/bruksenheter](https://data.norge.no/linkml/ngr-adresse/bruksenheter)
Alias: bruksenheter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdresseContainer](AdresseContainer.md) | Rotklasse for NGR-adresse-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bruksenhet](Bruksenhet.md) |
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
| self | https://data.norge.no/linkml/ngr-adresse/bruksenheter |
| native | https://data.norge.no/linkml/ngr-adresse/bruksenheter |




## LinkML Source

<details>
```yaml
name: bruksenheter
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
alias: bruksenheter
owner: AdresseContainer
domain_of:
- AdresseContainer
range: Bruksenhet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>