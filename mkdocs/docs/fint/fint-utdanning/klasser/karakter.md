

# Slot: karakter 


_Karakterverdi._





URI: [utd:karakter](https://schema.fintlabs.no/utdanning/karakter)
Alias: karakter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |
| [FagvurderingAbstrakt](fagvurderingabstrakt.md) | Abstrakt basisklasse for fagvurderingar |  yes  |
| [Underveisfagvurdering](underveisfagvurdering.md) | Underveisfagvurdering for ein elev |  no  |
| [Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Halvaarsfagvurdering](halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Karakterverdi](karakterverdi.md) |
| Domain Of | [FagvurderingAbstrakt](fagvurderingabstrakt.md) |
| Slot URI | [utd:karakter](https://schema.fintlabs.no/utdanning/karakter) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:karakter |
| native | https://schema.fintlabs.no/utdanning/:karakter |




## LinkML Source

<details>
```yaml
name: karakter
description: Karakterverdi.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:karakter
alias: karakter
domain_of:
- FagvurderingAbstrakt
range: Karakterverdi

```
</details>