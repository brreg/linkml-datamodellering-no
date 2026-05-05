

# Slot: adressekoder 



URI: [https://data.norge.no/linkml/ngr-adresse/adressekoder](https://data.norge.no/linkml/ngr-adresse/adressekoder)
Alias: adressekoder

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdresseContainer](adressecontainer.md) | Rotklasse for NGR-adresse-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adressekode](adressekode.md) |
| Domain Of | [AdresseContainer](adressecontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AdresseContainer](adressecontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/ngr-adresse/adressekoder |
| native | https://data.norge.no/linkml/ngr-adresse/adressekoder |




## LinkML Source

<details>
```yaml
name: adressekoder
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
alias: adressekoder
owner: AdresseContainer
domain_of:
- AdresseContainer
range: Adressekode
multivalued: true
inlined: true
inlined_as_list: true

```
</details>