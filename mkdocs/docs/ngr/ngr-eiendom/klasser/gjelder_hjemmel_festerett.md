

# Slot: gjelder_hjemmel_festerett 


_Heimelsdokument for festerett knytt til dette eigarforholdet._





URI: [ngre:gjelderHjemmelFesterett](https://data.norge.no/vocabulary/ngr-eiendom#gjelderHjemmelFesterett)
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
| Range | [HjemmelTilFesterett](hjemmeltilfesterett.md) |
| Domain Of | [Eierforhold](eierforhold.md) |
| Slot URI | [ngre:gjelderHjemmelFesterett](https://data.norge.no/vocabulary/ngr-eiendom#gjelderHjemmelFesterett) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:gjelderHjemmelFesterett |
| native | https://data.norge.no/ngr/ngr-eiendom/gjelder_hjemmel_festerett |




## LinkML Source

<details>
```yaml
name: gjelder_hjemmel_festerett
description: Heimelsdokument for festerett knytt til dette eigarforholdet.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_uri: ngre:gjelderHjemmelFesterett
domain_of:
- Eierforhold
range: HjemmelTilFesterett

```
</details>