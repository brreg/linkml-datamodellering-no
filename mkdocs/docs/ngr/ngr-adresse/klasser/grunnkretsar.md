

# Slot: grunnkretsar 



URI: [https://data.norge.no/ngr/ngr-adresse/grunnkretsar](https://data.norge.no/ngr/ngr-adresse/grunnkretsar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdresseContainer](adressecontainer.md) | Rotklasse for NGR-adresse-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Grunnkrets](grunnkrets.md) |
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
| self | https://data.norge.no/ngr/ngr-adresse/grunnkretsar |
| native | https://data.norge.no/ngr/ngr-adresse/grunnkretsar |




## LinkML Source

<details>
```yaml
name: grunnkretsar
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
owner: AdresseContainer
domain_of:
- AdresseContainer
range: Grunnkrets
multivalued: true
inlined: true
inlined_as_list: true

```
</details>