

# Slot: karakter 


_Karakterverdien gjeve i vurderinga._





URI: [utd:karakter](https://schema.fintlabs.no/utdanning/karakter)
Alias: karakter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Underveisfagvurdering](Underveisfagvurdering.md) | Underveisfagvurdering for ein elev |  no  |
| [FagvurderingAbstrakt](FagvurderingAbstrakt.md) | Abstrakt basisklasse for fagvurderingar |  no  |
| [Eksamensvurdering](Eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |  no  |
| [Sluttfagvurdering](Sluttfagvurdering.md) | Sluttkarakter i eit fag |  no  |
| [Halvaarsfagvurdering](Halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Karakterverdi](Karakterverdi.md) |
| Domain Of | [FagvurderingAbstrakt](FagvurderingAbstrakt.md) |
| Slot URI | [utd:karakter](https://schema.fintlabs.no/utdanning/karakter) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FagvurderingAbstrakt](FagvurderingAbstrakt.md) |








## In Subsets


* [Valgfri](Valgfri.md)






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
description: Karakterverdien gjeve i vurderinga.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:karakter
alias: karakter
owner: FagvurderingAbstrakt
domain_of:
- FagvurderingAbstrakt
range: Karakterverdi

```
</details>