

# Slot: er_klassifisert_i_naeringskode 


_Næringskode(r) verksemda er klassifisert under (1–3)._





URI: [ngrv:erKlassifisertINaeringskode](https://data.norge.no/vocabulary/ngr-virksomhet#erKlassifisertINaeringskode)
Alias: er_klassifisert_i_naeringskode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Underenhet](underenhet.md) | Ei underleining er ein geografisk lokasjon der aktiviteten til ei hovudeining... |  no  |
| [Virksomhet](virksomhet.md) | Abstrakt overklasse for alle einingar registrert i Enhetsregisteret |  yes  |
| [Hovedenhet](hovedenhet.md) | Ei hovudeining er den juridiske eininga registrert i Enhetsregisteret (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Naeringskode](naeringskode.md) |
| Domain Of | [Virksomhet](virksomhet.md) |
| Slot URI | [ngrv:erKlassifisertINaeringskode](https://data.norge.no/vocabulary/ngr-virksomhet#erKlassifisertINaeringskode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:erKlassifisertINaeringskode |
| native | https://data.norge.no/linkml/ngr-virksomhet/er_klassifisert_i_naeringskode |




## LinkML Source

<details>
```yaml
name: er_klassifisert_i_naeringskode
description: Næringskode(r) verksemda er klassifisert under (1–3).
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
slot_uri: ngrv:erKlassifisertINaeringskode
alias: er_klassifisert_i_naeringskode
domain_of:
- Virksomhet
range: Naeringskode
multivalued: true

```
</details>