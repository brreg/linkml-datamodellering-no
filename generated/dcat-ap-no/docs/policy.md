

# Slot: policy 


_ODRL-policy som regulerer bruk av ressursen._





URI: [odrl:hasPolicy](http://www.w3.org/ns/odrl/2/hasPolicy)
Alias: policy

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OdrlPolicy](OdrlPolicy.md) |
| Domain Of | [Distribusjon](Distribusjon.md) |
| Slot URI | [odrl:hasPolicy](http://www.w3.org/ns/odrl/2/hasPolicy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odrl:hasPolicy |
| native | https://data.norge.no/linkml/dcat-ap-no/policy |




## LinkML Source

<details>
```yaml
name: policy
description: ODRL-policy som regulerer bruk av ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: odrl:hasPolicy
alias: policy
domain_of:
- Distribusjon
range: OdrlPolicy

```
</details>