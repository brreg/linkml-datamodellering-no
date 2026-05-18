

# Slot: kan_gjelde_borettslagsandel 


_Burettslagsandelen dette eigarforholdet eventuelt gjeld._





URI: [ngre:kanGjeldeBorettslagsandel](https://data.norge.no/vocabulary/ngr-eiendom#kanGjeldeBorettslagsandel)
Alias: kan_gjelde_borettslagsandel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IkkeTinglystEierforhold](ikketinglysteierforhold.md) | Eigarforhold som ikkje er registrert i Grunnboka |  no  |
| [TinglystEierforhold](tinglysteierforhold.md) | Eigarforhold registrert (tinglyst) i Grunnboka |  no  |
| [Eierforhold](eierforhold.md) | Abstrakt klasse for eigarforhold forvalta av Grunnboka |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Borettslagsandel](borettslagsandel.md) |
| Domain Of | [Eierforhold](eierforhold.md) |
| Slot URI | [ngre:kanGjeldeBorettslagsandel](https://data.norge.no/vocabulary/ngr-eiendom#kanGjeldeBorettslagsandel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:kanGjeldeBorettslagsandel |
| native | https://data.norge.no/linkml/ngr-eiendom/kan_gjelde_borettslagsandel |




## LinkML Source

<details>
```yaml
name: kan_gjelde_borettslagsandel
description: Burettslagsandelen dette eigarforholdet eventuelt gjeld.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:kanGjeldeBorettslagsandel
alias: kan_gjelde_borettslagsandel
domain_of:
- Eierforhold
range: Borettslagsandel

```
</details>