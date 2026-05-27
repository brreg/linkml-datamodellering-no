

# Slot: poststeder 



URI: [https://data.norge.no/ngr/ngr-adresse/poststeder](https://data.norge.no/ngr/ngr-adresse/poststeder)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdresseContainer](adressecontainer.md) | Rotklasse for NGR-adresse-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Poststed](poststed.md) |
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
| self | https://data.norge.no/ngr/ngr-adresse/poststeder |
| native | https://data.norge.no/ngr/ngr-adresse/poststeder |




## LinkML Source

<details>
```yaml
name: poststeder
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
owner: AdresseContainer
domain_of:
- AdresseContainer
range: Poststed
multivalued: true
inlined: true
inlined_as_list: true

```
</details>