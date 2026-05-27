

# Slot: har_tilstand 


_Registrert tilstand (status) for verksemda, inkl. historikk._





URI: [ngrv:harTilstand](https://data.norge.no/vocabulary/ngr-virksomhet#harTilstand)
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
| Range | [Tilstand](tilstand.md) |
| Domain Of | [Virksomhet](virksomhet.md) |
| Slot URI | [ngrv:harTilstand](https://data.norge.no/vocabulary/ngr-virksomhet#harTilstand) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:harTilstand |
| native | https://data.norge.no/ngr/ngr-virksomhet/har_tilstand |




## LinkML Source

<details>
```yaml
name: har_tilstand
description: Registrert tilstand (status) for verksemda, inkl. historikk.
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
slot_uri: ngrv:harTilstand
domain_of:
- Virksomhet
range: Tilstand
multivalued: true

```
</details>