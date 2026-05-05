

# Slot: adressenavn 



URI: [https://data.norge.no/linkml/ngr-adresse/adressenavn](https://data.norge.no/linkml/ngr-adresse/adressenavn)
Alias: adressenavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdresseContainer](adressecontainer.md) | Rotklasse for NGR-adresse-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adressenavn](adressenavn.md) |
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
| self | https://data.norge.no/linkml/ngr-adresse/adressenavn |
| native | https://data.norge.no/linkml/ngr-adresse/adressenavn |




## LinkML Source

<details>
```yaml
name: adressenavn
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
alias: adressenavn
owner: AdresseContainer
domain_of:
- AdresseContainer
range: Adressenavn
multivalued: true
inlined: true
inlined_as_list: true

```
</details>