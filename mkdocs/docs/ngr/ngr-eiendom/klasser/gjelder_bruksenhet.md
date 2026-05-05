

# Slot: gjelder_bruksenhet 


_Brukseiningane den ytre inngangen gir tilgang til._





URI: [ngre:gjelderBruksenhet](https://data.norge.no/vocabulary/ngr-eiendom#gjelderBruksenhet)
Alias: gjelder_bruksenhet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [YtreInngang](ytreinngang.md) | Ytre inngang til ein bygning |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bruksenhet](bruksenhet.md) |
| Domain Of | [YtreInngang](ytreinngang.md) |
| Slot URI | [ngre:gjelderBruksenhet](https://data.norge.no/vocabulary/ngr-eiendom#gjelderBruksenhet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:gjelderBruksenhet |
| native | https://data.norge.no/linkml/ngr-eiendom/gjelder_bruksenhet |




## LinkML Source

<details>
```yaml
name: gjelder_bruksenhet
description: Brukseiningane den ytre inngangen gir tilgang til.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:gjelderBruksenhet
alias: gjelder_bruksenhet
domain_of:
- YtreInngang
range: Bruksenhet
multivalued: true

```
</details>