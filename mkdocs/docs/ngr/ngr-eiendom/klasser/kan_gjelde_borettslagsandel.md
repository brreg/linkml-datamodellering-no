

# Slot: kan_gjelde_borettslagsandel 


_Burettslagsandelen dette eigarforholdet eventuelt gjeld._





URI: [ngre:kanGjeldeBorettslagsandel](https://data.norge.no/vocabulary/ngr-eiendom#kanGjeldeBorettslagsandel)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eierforhold](eierforhold.md) | Abstrakt klasse for eigarforhold forvalta av Grunnboka |  yes  |
| [TinglystEierforhold](tinglysteierforhold.md) | Eigarforhold registrert (tinglyst) i Grunnboka |  no  |
| [IkkeTinglystEierforhold](ikketinglysteierforhold.md) | Eigarforhold som ikkje er registrert i Grunnboka |  no  |






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


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:kanGjeldeBorettslagsandel |
| native | https://data.norge.no/ngr/ngr-eiendom/kan_gjelde_borettslagsandel |




## LinkML Source

<details>
```yaml
name: kan_gjelde_borettslagsandel
description: Burettslagsandelen dette eigarforholdet eventuelt gjeld.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_uri: ngre:kanGjeldeBorettslagsandel
domain_of:
- Eierforhold
range: Borettslagsandel

```
</details>