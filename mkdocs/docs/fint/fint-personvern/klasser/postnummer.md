

# Slot: postnummer 


_Postnummer._





URI: [fint:postnummer](https://schema.fintlabs.no/postnummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Adresse](adresse.md) | Fysisk adresse eller postadresse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Adresse](adresse.md) |
| Slot URI | [fint:postnummer](https://schema.fintlabs.no/postnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:postnummer |
| native | https://schema.fintlabs.no/:postnummer |




## LinkML Source

<details>
```yaml
name: postnummer
description: Postnummer.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:postnummer
domain_of:
- Adresse
range: string

```
</details>