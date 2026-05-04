

# Slot: adresselinje 


_Adresseinformasjon._





URI: [fint:adresselinje](https://schema.fintlabs.no/adresselinje)
Alias: adresselinje

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
| Slot URI | [fint:adresselinje](https://schema.fintlabs.no/adresselinje) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Adresse](Adresse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:adresselinje |
| native | https://schema.fintlabs.no/administrasjon/:adresselinje |




## LinkML Source

<details>
```yaml
name: adresselinje
description: Adresseinformasjon.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: fint:adresselinje
alias: adresselinje
owner: Adresse
domain_of:
- Adresse
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details>