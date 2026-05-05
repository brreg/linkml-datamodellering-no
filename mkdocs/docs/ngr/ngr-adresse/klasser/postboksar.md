

# Slot: postboksar 



URI: [https://data.norge.no/linkml/ngr-adresse/postboksar](https://data.norge.no/linkml/ngr-adresse/postboksar)
Alias: postboksar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdresseContainer](adressecontainer.md) | Rotklasse for NGR-adresse-datafiler |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Postboks](postboks.md) |
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
| self | https://data.norge.no/linkml/ngr-adresse/postboksar |
| native | https://data.norge.no/linkml/ngr-adresse/postboksar |




## LinkML Source

<details>
```yaml
name: postboksar
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
alias: postboksar
owner: AdresseContainer
domain_of:
- AdresseContainer
range: Postboks
multivalued: true
inlined: true
inlined_as_list: true

```
</details>