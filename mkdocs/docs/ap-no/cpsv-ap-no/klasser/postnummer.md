

# Slot: postnummer 


_Postnummer._





URI: [locn:postCode](http://www.w3.org/ns/locn#postCode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Adresse](adresse.md) | Ei postadresse knytt til ein aktør, organisasjon eller kontaktpunkt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Adresse](adresse.md) |
| Slot URI | [locn:postCode](http://www.w3.org/ns/locn#postCode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | locn:postCode |
| native | https://data.norge.no/ap-no/cpsv-ap-no/postnummer |




## LinkML Source

<details>
```yaml
name: postnummer
description: Postnummer.
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: locn:postCode
domain_of:
- Adresse
range: string

```
</details>