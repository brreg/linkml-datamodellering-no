

# Slot: policy 


_ODRL-policy som regulerer bruk av ressursen._





URI: [odrl:hasPolicy](http://www.w3.org/ns/odrl/2/hasPolicy)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Distribusjon](distribusjon.md) |
| Slot URI | [odrl:hasPolicy](http://www.w3.org/ns/odrl/2/hasPolicy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | odrl:Policy |




### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odrl:hasPolicy |
| native | https://data.norge.no/ap-no/dcat-ap-no/policy |




## LinkML Source

<details>
```yaml
name: policy
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: odrl:Policy
description: ODRL-policy som regulerer bruk av ressursen.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
rank: 1000
slot_uri: odrl:hasPolicy
domain_of:
- Distribusjon
range: string

```
</details>