

# Slot: belop 


_Monetært beløp._





URI: [https://data.norge.no/linkml/register-over-aksjeeiere/:belop](https://data.norge.no/linkml/register-over-aksjeeiere/:belop)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Utdeling](utdeling.md) | Konkret utdeling av verdiar til aksjeeigarar |  no  |
| [Vederlag](vederlag.md) | Vederlag knytt til ei aksjeoverdraging |  no  |
| [InnbetaltAksjekapital](innbetaltaksjekapital.md) | Innbetalt aksjekapital |  no  |
| [InnbetaltOverkurs](innbetaltoverkurs.md) | Innbetalt overkurs utover pålydande |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) |
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
| self | https://data.norge.no/linkml/register-over-aksjeeiere/:belop |
| native | https://data.norge.no/linkml/register-over-aksjeeiere/:belop |




## LinkML Source

<details>
```yaml
name: belop
description: Monetært beløp.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain_of:
- Utdeling
- Vederlag
- InnbetaltAksjekapital
- InnbetaltOverkurs
range: decimal
inlined: true

```
</details>