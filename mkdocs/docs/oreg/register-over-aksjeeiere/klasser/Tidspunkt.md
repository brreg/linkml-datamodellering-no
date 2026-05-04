

# Slot: tidspunkt 


_Tidspunkt for utbytte/eierskapstransaksjon._





URI: [aksje:tidspunkt](https://example.no/ontology/aksje#tidspunkt)
Alias: tidspunkt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Utbytte](Utbytte.md) | Utbytte knytt til ein eigarposisjon |  no  |
| [Eierskapstransaksjon](Eierskapstransaksjon.md) | Transaksjon som påverkar eigarskap i selskapet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Utbytte](Utbytte.md), [Eierskapstransaksjon](Eierskapstransaksjon.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aksje:tidspunkt |
| native | aksje:tidspunkt |




## LinkML Source

<details>
```yaml
name: tidspunkt
description: Tidspunkt for utbytte/eierskapstransaksjon.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
alias: tidspunkt
domain_of:
- Utbytte
- Eierskapstransaksjon
range: date
inlined: true

```
</details>