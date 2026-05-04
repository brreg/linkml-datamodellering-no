

# Slot: offisielleAdresser 



URI: [https://data.norge.no/linkml/ngr-adresse/offisielleAdresser](https://data.norge.no/linkml/ngr-adresse/offisielleAdresser)
Alias: offisielleAdresser

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdresseContainer](AdresseContainer.md) | Rotklasse for NGR-adresse-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OffisiellAdresse](OffisiellAdresse.md) |
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
| self | https://data.norge.no/linkml/ngr-adresse/offisielleAdresser |
| native | https://data.norge.no/linkml/ngr-adresse/offisielleAdresser |




## LinkML Source

<details>
```yaml
name: offisielleAdresser
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
alias: offisielleAdresser
owner: AdresseContainer
domain_of:
- AdresseContainer
range: OffisiellAdresse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>