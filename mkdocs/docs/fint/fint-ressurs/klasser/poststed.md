

# Slot: poststed 


_Poststad._





URI: [fint:poststed](https://schema.fintlabs.no/poststed)
Alias: poststed

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Adresse](Adresse.md) | Fysisk adresse eller postadresse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Adresse](Adresse.md) |
| Slot URI | [fint:poststed](https://schema.fintlabs.no/poststed) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Adresse](Adresse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:poststed |
| native | https://schema.fintlabs.no/ressurs/:poststed |




## LinkML Source

<details>
```yaml
name: poststed
description: Poststad.
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: fint:poststed
alias: poststed
owner: Adresse
domain_of:
- Adresse
range: string

```
</details>