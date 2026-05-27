

# Slot: annen_identifikator 


_Alternativ identifikator frå eit anna system._





URI: [adms:identifier](http://www.w3.org/ns/adms#identifier)
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


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:identifier |
| native | https://data.norge.no/ap-no/dcat-ap-no/annen_identifikator |




## LinkML Source

<details>
```yaml
name: annen_identifikator
description: Alternativ identifikator frå eit anna system.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
rank: 1000
slot_uri: adms:identifier
domain_of:
- Datasett
range: Identifikator
multivalued: true

```
</details>