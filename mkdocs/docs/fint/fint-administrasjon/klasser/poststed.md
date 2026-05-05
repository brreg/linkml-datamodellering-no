

# Slot: poststed 


_Poststad._





URI: [fint:poststed](https://schema.fintlabs.no/poststed)
Alias: poststed

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Adresse](adresse.md) | Fysisk adresse eller postadresse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Adresse](adresse.md) |
| Slot URI | [fint:poststed](https://schema.fintlabs.no/poststed) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Adresse](adresse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:poststed |
| native | https://schema.fintlabs.no/administrasjon/:poststed |




## LinkML Source

<details>
```yaml
name: poststed
description: Poststad.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: fint:poststed
alias: poststed
owner: Adresse
domain_of:
- Adresse
range: string

```
</details>