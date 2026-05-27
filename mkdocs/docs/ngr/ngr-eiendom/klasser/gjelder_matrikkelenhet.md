

# Slot: gjelder_matrikkelenhet 


_Matrikkeleininga dette eigarforholdet gjeld._





URI: [ngre:gjelderMatrikkelenhet](https://data.norge.no/vocabulary/ngr-eiendom#gjelderMatrikkelenhet)
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
| Range | [Matrikkelenhet](matrikkelenhet.md) |
| Domain Of | [Eierforhold](eierforhold.md) |
| Slot URI | [ngre:gjelderMatrikkelenhet](https://data.norge.no/vocabulary/ngr-eiendom#gjelderMatrikkelenhet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:gjelderMatrikkelenhet |
| native | https://data.norge.no/ngr/ngr-eiendom/gjelder_matrikkelenhet |




## LinkML Source

<details>
```yaml
name: gjelder_matrikkelenhet
description: Matrikkeleininga dette eigarforholdet gjeld.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_uri: ngre:gjelderMatrikkelenhet
domain_of:
- Eierforhold
range: Matrikkelenhet

```
</details>