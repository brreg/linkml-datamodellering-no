

# Slot: bruksenhetsnummer 



URI: [https://data.norge.no/linkml/ngr-adresse/bruksenhetsnummer](https://data.norge.no/linkml/ngr-adresse/bruksenhetsnummer)
Alias: bruksenhetsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdresseContainer](AdresseContainer.md) | Rotklasse for NGR-adresse-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bruksenhetsnummer](Bruksenhetsnummer.md) |
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
| self | https://data.norge.no/linkml/ngr-adresse/bruksenhetsnummer |
| native | https://data.norge.no/linkml/ngr-adresse/bruksenhetsnummer |




## LinkML Source

<details>
```yaml
name: bruksenhetsnummer
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
alias: bruksenhetsnummer
owner: AdresseContainer
domain_of:
- AdresseContainer
range: Bruksenhetsnummer
multivalued: true
inlined: true
inlined_as_list: true

```
</details>