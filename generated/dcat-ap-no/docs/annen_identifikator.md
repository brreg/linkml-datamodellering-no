

# Slot: annen_identifikator 


_Alternativ identifikator frå eit anna system._





URI: [adms:identifier](http://www.w3.org/ns/adms#identifier)
Alias: annen_identifikator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](Identifikator.md) |
| Domain Of | [Datasett](Datasett.md) |
| Slot URI | [adms:identifier](http://www.w3.org/ns/adms#identifier) |

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
| self | adms:identifier |
| native | https://data.norge.no/linkml/dcat-ap-no/annen_identifikator |




## LinkML Source

<details>
```yaml
name: annen_identifikator
description: Alternativ identifikator frå eit anna system.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: adms:identifier
alias: annen_identifikator
domain_of:
- Datasett
range: Identifikator
multivalued: true

```
</details>