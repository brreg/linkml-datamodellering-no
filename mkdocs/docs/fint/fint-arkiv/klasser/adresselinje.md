

# Slot: adresselinje 


_Adresseinformasjon._





URI: [fint:adresselinje](https://schema.fintlabs.no/adresselinje)
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
| Slot URI | [fint:adresselinje](https://schema.fintlabs.no/adresselinje) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:adresselinje |
| native | https://schema.fintlabs.no/:adresselinje |




## LinkML Source

<details>
```yaml
name: adresselinje
description: Adresseinformasjon.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:adresselinje
domain_of:
- Adresse
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details>