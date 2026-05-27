

# Slot: har_kontaktinformasjon 


_Kontaktinformasjon registrert på verksemda._





URI: [ngrv:harKontaktinformasjon](https://data.norge.no/vocabulary/ngr-virksomhet#harKontaktinformasjon)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virksomhet](virksomhet.md) | Abstrakt overklasse for alle einingar registrert i Enhetsregisteret |  yes  |
| [Underenhet](underenhet.md) | Ei underleining er ein geografisk lokasjon der aktiviteten til ei hovudeining... |  no  |
| [Hovedenhet](hovedenhet.md) | Ei hovudeining er den juridiske eininga registrert i Enhetsregisteret (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktinformasjon](kontaktinformasjon.md) |
| Domain Of | [Virksomhet](virksomhet.md) |
| Slot URI | [ngrv:harKontaktinformasjon](https://data.norge.no/vocabulary/ngr-virksomhet#harKontaktinformasjon) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:harKontaktinformasjon |
| native | https://data.norge.no/ngr/ngr-virksomhet/har_kontaktinformasjon |




## LinkML Source

<details>
```yaml
name: har_kontaktinformasjon
description: Kontaktinformasjon registrert på verksemda.
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
slot_uri: ngrv:harKontaktinformasjon
domain_of:
- Virksomhet
range: Kontaktinformasjon

```
</details>