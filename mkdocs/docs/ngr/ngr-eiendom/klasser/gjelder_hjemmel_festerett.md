

# Slot: gjelder_hjemmel_festerett 


_Heimelsdokument for festerett knytt til dette eigarforholdet._





URI: [ngre:gjelderHjemmelFesterett](https://data.norge.no/vocabulary/ngr-eiendom#gjelderHjemmelFesterett)
Alias: gjelder_hjemmel_festerett

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eierforhold](Eierforhold.md) | Abstrakt klasse for eigarforhold forvalta av Grunnboka |  yes  |
| [IkkeTinglystEierforhold](IkkeTinglystEierforhold.md) | Eigarforhold som ikkje er registrert i Grunnboka |  no  |
| [TinglystEierforhold](TinglystEierforhold.md) | Eigarforhold registrert (tinglyst) i Grunnboka |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [HjemmelTilFesterett](HjemmelTilFesterett.md) |
| Domain Of | [Eierforhold](Eierforhold.md) |
| Slot URI | [ngre:gjelderHjemmelFesterett](https://data.norge.no/vocabulary/ngr-eiendom#gjelderHjemmelFesterett) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:gjelderHjemmelFesterett |
| native | https://data.norge.no/linkml/ngr-eiendom/gjelder_hjemmel_festerett |




## LinkML Source

<details>
```yaml
name: gjelder_hjemmel_festerett
description: Heimelsdokument for festerett knytt til dette eigarforholdet.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:gjelderHjemmelFesterett
alias: gjelder_hjemmel_festerett
domain_of:
- Eierforhold
range: HjemmelTilFesterett

```
</details>