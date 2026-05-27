

# Slot: tidspunkt 


_Tidspunkt for utbytte/eierskapstransaksjon._





URI: [https://data.norge.no/oreg/register-over-aksjeeiere/:tidspunkt](https://data.norge.no/oreg/register-over-aksjeeiere/:tidspunkt)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Utbytte](utbytte.md) | Utbytte knytt til ein eigarposisjon |  no  |
| [Eierskapstransaksjon](eierskapstransaksjon.md) | Transaksjon som påverkar eigarskap i selskapet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Utbytte](utbytte.md), [Eierskapstransaksjon](eierskapstransaksjon.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/oreg/register-over-aksjeeiere/:tidspunkt |
| native | https://data.norge.no/oreg/register-over-aksjeeiere/:tidspunkt |




## LinkML Source

<details>
```yaml
name: tidspunkt
description: Tidspunkt for utbytte/eierskapstransaksjon.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain_of:
- Utbytte
- Eierskapstransaksjon
range: date
inlined: true

```
</details>