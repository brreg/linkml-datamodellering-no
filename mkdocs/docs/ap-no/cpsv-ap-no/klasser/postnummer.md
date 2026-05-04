

# Slot: postnummer 


_Postnummer._





URI: [locn:postCode](http://www.w3.org/ns/locn#postCode)
Alias: postnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Adresse](Adresse.md) | Ei postadresse knytt til ein aktør, organisasjon eller kontaktpunkt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Adresse](Adresse.md) |
| Slot URI | [locn:postCode](http://www.w3.org/ns/locn#postCode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | locn:postCode |
| native | https://data.norge.no/linkml/cpsv-ap-no/postnummer |




## LinkML Source

<details>
```yaml
name: postnummer
description: Postnummer.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: locn:postCode
alias: postnummer
domain_of:
- Adresse
range: string

```
</details>