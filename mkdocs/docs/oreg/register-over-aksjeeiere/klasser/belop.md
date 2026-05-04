

# Slot: belop 


_Monetært beløp._





URI: [aksje:belop](https://example.no/ontology/aksje#belop)
Alias: belop

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vederlag](Vederlag.md) | Vederlag knytt til ei aksjeoverdraging |  no  |
| [InnbetaltOverkurs](InnbetaltOverkurs.md) | Innbetalt overkurs utover pålydande |  no  |
| [InnbetaltAksjekapital](InnbetaltAksjekapital.md) | Innbetalt aksjekapital |  no  |
| [Utdeling](Utdeling.md) | Konkret utdeling av verdiar til aksjeeigarar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Decimal](Decimal.md) |
| Domain Of | [Utdeling](Utdeling.md), [Vederlag](Vederlag.md), [InnbetaltAksjekapital](InnbetaltAksjekapital.md), [InnbetaltOverkurs](InnbetaltOverkurs.md) |

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