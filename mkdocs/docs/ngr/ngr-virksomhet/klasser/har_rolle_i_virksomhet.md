

# Slot: har_rolle_i_virksomhet 


_Roller registrert i hovudeininga (minimum 1)._





URI: [ngrv:harRolleIVirksomhet](https://data.norge.no/vocabulary/ngr-virksomhet#harRolleIVirksomhet)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Hovedenhet](hovedenhet.md) | Ei hovudeining er den juridiske eininga registrert i Enhetsregisteret (t |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RolleIVirksomhet](rolleivirksomhet.md) |
| Domain Of | [Hovedenhet](hovedenhet.md) |
| Slot URI | [ngrv:harRolleIVirksomhet](https://data.norge.no/vocabulary/ngr-virksomhet#harRolleIVirksomhet) |

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
| self | ngrv:harRolleIVirksomhet |
| native | https://data.norge.no/ngr/ngr-virksomhet/har_rolle_i_virksomhet |




## LinkML Source

<details>
```yaml
name: har_rolle_i_virksomhet
description: Roller registrert i hovudeininga (minimum 1).
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
slot_uri: ngrv:harRolleIVirksomhet
domain_of:
- Hovedenhet
range: RolleIVirksomhet
multivalued: true

```
</details>