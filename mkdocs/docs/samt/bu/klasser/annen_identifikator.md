

# Slot: annen_identifikator 


_Alternativ identifikator frå eit anna system._





URI: [adms:identifier](http://www.w3.org/ns/adms#identifier)
Alias: annen_identifikator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [adms:identifier](http://www.w3.org/ns/adms#identifier) |

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
| self | adms:identifier |
| native | samtbuskole:annen_identifikator |




## LinkML Source

<details>
```yaml
name: annen_identifikator
description: Alternativ identifikator frå eit anna system.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: adms:identifier
alias: annen_identifikator
domain_of:
- Datasett
range: Identifikator
multivalued: true

```
</details>