

# Slot: postnummer 


_Postnummer._





URI: [fint:postnummer](https://schema.fintlabs.no/postnummer)
Alias: postnummer

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
| Slot URI | [fint:postnummer](https://schema.fintlabs.no/postnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Adresse](adresse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:postnummer |
| native | https://schema.fintlabs.no/ressurs/:postnummer |




## LinkML Source

<details>
```yaml
name: postnummer
description: Postnummer.
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: fint:postnummer
alias: postnummer
owner: Adresse
domain_of:
- Adresse
range: string

```
</details>