

# Slot: gjelder_hjemmel_eiendomsrett 


_Heimelsdokument for eigedomsrett knytt til dette eigarforholdet._





URI: [ngre:gjelderHjemmelEiendomsrett](https://data.norge.no/vocabulary/ngr-eiendom#gjelderHjemmelEiendomsrett)
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
| Range | [HjemmelTilEiendomsrett](hjemmeltileiendomsrett.md) |
| Domain Of | [Eierforhold](eierforhold.md) |
| Slot URI | [ngre:gjelderHjemmelEiendomsrett](https://data.norge.no/vocabulary/ngr-eiendom#gjelderHjemmelEiendomsrett) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:gjelderHjemmelEiendomsrett |
| native | https://data.norge.no/ngr/ngr-eiendom/gjelder_hjemmel_eiendomsrett |




## LinkML Source

<details>
```yaml
name: gjelder_hjemmel_eiendomsrett
description: Heimelsdokument for eigedomsrett knytt til dette eigarforholdet.
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_uri: ngre:gjelderHjemmelEiendomsrett
domain_of:
- Eierforhold
range: HjemmelTilEiendomsrett

```
</details>