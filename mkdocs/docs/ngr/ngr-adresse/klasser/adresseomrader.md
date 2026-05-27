

# Slot: adresseomrader 



URI: [https://data.norge.no/ngr/ngr-adresse/adresseomrader](https://data.norge.no/ngr/ngr-adresse/adresseomrader)
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


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/ngr/ngr-adresse/adresseomrader |
| native | https://data.norge.no/ngr/ngr-adresse/adresseomrader |




## LinkML Source

<details>
```yaml
name: adresseomrader
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
owner: AdresseContainer
domain_of:
- AdresseContainer
range: Adresseomrade
multivalued: true
inlined: true
inlined_as_list: true

```
</details>