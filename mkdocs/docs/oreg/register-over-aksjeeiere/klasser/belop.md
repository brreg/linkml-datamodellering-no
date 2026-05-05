

# Slot: belop 


_Monetært beløp._





URI: [aksje:belop](https://example.no/ontology/aksje#belop)
Alias: belop

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InnbetaltOverkurs](innbetaltoverkurs.md) | Innbetalt overkurs utover pålydande |  no  |
| [Utdeling](utdeling.md) | Konkret utdeling av verdiar til aksjeeigarar |  no  |
| [Vederlag](vederlag.md) | Vederlag knytt til ei aksjeoverdraging |  no  |
| [InnbetaltAksjekapital](innbetaltaksjekapital.md) | Innbetalt aksjekapital |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Decimal](decimal.md) |
| Domain Of | [Utdeling](utdeling.md), [Vederlag](vederlag.md), [InnbetaltAksjekapital](innbetaltaksjekapital.md), [InnbetaltOverkurs](innbetaltoverkurs.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aksje:belop |
| native | aksje:belop |




## LinkML Source

<details>
```yaml
name: belop
description: Monetært beløp.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
alias: belop
domain_of:
- Utdeling
- Vederlag
- InnbetaltAksjekapital
- InnbetaltOverkurs
range: decimal
inlined: true

```
</details>