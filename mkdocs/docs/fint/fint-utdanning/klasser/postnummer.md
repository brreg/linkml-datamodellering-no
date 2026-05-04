

# Slot: postnummer 


_Postnummer._





URI: [fint:postnummer](https://schema.fintlabs.no/postnummer)
Alias: postnummer

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
| Slot URI | [fint:postnummer](https://schema.fintlabs.no/postnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Adresse](Adresse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:postnummer |
| native | https://schema.fintlabs.no/utdanning/:postnummer |




## LinkML Source

<details>
```yaml
name: postnummer
description: Postnummer.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: fint:postnummer
alias: postnummer
owner: Adresse
domain_of:
- Adresse
range: string

```
</details>