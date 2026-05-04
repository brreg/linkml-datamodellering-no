

# Slot: eksempeldata 


_Eksempeldata som distribusjon._





URI: [adms:sample](http://www.w3.org/ns/adms#sample)
Alias: eksempeldata

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Distribusjon](Distribusjon.md) |
| Domain Of | [Datasett](Datasett.md) |
| Slot URI | [adms:sample](http://www.w3.org/ns/adms#sample) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:sample |
| native | https://data.norge.no/linkml/dcat-ap-no/eksempeldata |




## LinkML Source

<details>
```yaml
name: eksempeldata
description: Eksempeldata som distribusjon.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: adms:sample
alias: eksempeldata
domain_of:
- Datasett
range: Distribusjon
multivalued: true

```
</details>