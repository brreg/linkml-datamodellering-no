

# Slot: er_klassifisert_som_organisasjonsform 


_Organisasjonsform (juridisk form) for verksemda._





URI: [ngrv:erKlassifisertSomOrganisasjonsform](https://data.norge.no/vocabulary/ngr-virksomhet#erKlassifisertSomOrganisasjonsform)
Alias: er_klassifisert_som_organisasjonsform

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
| Range | [Organisasjonsform](organisasjonsform.md) |
| Domain Of | [Virksomhet](virksomhet.md) |
| Slot URI | [ngrv:erKlassifisertSomOrganisasjonsform](https://data.norge.no/vocabulary/ngr-virksomhet#erKlassifisertSomOrganisasjonsform) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:erKlassifisertSomOrganisasjonsform |
| native | https://data.norge.no/linkml/ngr-virksomhet/er_klassifisert_som_organisasjonsform |




## LinkML Source

<details>
```yaml
name: er_klassifisert_som_organisasjonsform
description: Organisasjonsform (juridisk form) for verksemda.
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
slot_uri: ngrv:erKlassifisertSomOrganisasjonsform
alias: er_klassifisert_som_organisasjonsform
domain_of:
- Virksomhet
range: Organisasjonsform

```
</details>