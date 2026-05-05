

# Slot: eksempeldata 


_Eksempeldata som distribusjon._





URI: [adms:sample](http://www.w3.org/ns/adms#sample)
Alias: eksempeldata

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Distribusjon](distribusjon.md) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [adms:sample](http://www.w3.org/ns/adms#sample) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:sample |
| native | samtbuskole:eksempeldata |




## LinkML Source

<details>
```yaml
name: eksempeldata
description: Eksempeldata som distribusjon.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: adms:sample
alias: eksempeldata
domain_of:
- Datasett
range: Distribusjon
multivalued: true

```
</details>