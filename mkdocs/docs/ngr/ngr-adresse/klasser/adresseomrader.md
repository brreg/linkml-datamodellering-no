

# Slot: adresseomrader 



URI: [https://data.norge.no/linkml/ngr-adresse/adresseomrader](https://data.norge.no/linkml/ngr-adresse/adresseomrader)
Alias: adresseomrader

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdresseContainer](adressecontainer.md) | Rotklasse for NGR-adresse-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresseomrade](adresseomrade.md) |
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
| self | https://data.norge.no/linkml/ngr-adresse/adresseomrader |
| native | https://data.norge.no/linkml/ngr-adresse/adresseomrader |




## LinkML Source

<details>
```yaml
name: adresseomrader
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
alias: adresseomrader
owner: AdresseContainer
domain_of:
- AdresseContainer
range: Adresseomrade
multivalued: true
inlined: true
inlined_as_list: true

```
</details>