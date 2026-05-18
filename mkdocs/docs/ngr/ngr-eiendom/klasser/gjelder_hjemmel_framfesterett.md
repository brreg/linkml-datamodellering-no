

# Slot: gjelder_hjemmel_framfesterett 


_Heimelsdokument for framfesterett knytt til dette eigarforholdet._





URI: [ngre:gjelderHjemmelFramfesterett](https://data.norge.no/vocabulary/ngr-eiendom#gjelderHjemmelFramfesterett)
Alias: gjelder_hjemmel_framfesterett

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
| Range | [HjemmelTilFramfesterett](hjemmeltilframfesterett.md) |
| Domain Of | [Eierforhold](eierforhold.md) |
| Slot URI | [ngre:gjelderHjemmelFramfesterett](https://data.norge.no/vocabulary/ngr-eiendom#gjelderHjemmelFramfesterett) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:gjelderHjemmelFramfesterett |
| native | https://data.norge.no/linkml/ngr-eiendom/gjelder_hjemmel_framfesterett |




## LinkML Source

<details>
```yaml
name: gjelder_hjemmel_framfesterett
description: Heimelsdokument for framfesterett knytt til dette eigarforholdet.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:gjelderHjemmelFramfesterett
alias: gjelder_hjemmel_framfesterett
domain_of:
- Eierforhold
range: HjemmelTilFramfesterett

```
</details>