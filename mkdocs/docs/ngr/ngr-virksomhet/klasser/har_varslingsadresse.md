

# Slot: har_varslingsadresse 


_Offisiell varslingsadresse for offentlege meldingar._





URI: [ngrv:harVarslingsadresse](https://data.norge.no/vocabulary/ngr-virksomhet#harVarslingsadresse)
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
| Range | [Varslingsadresse](varslingsadresse.md) |
| Domain Of | [Virksomhet](virksomhet.md) |
| Slot URI | [ngrv:harVarslingsadresse](https://data.norge.no/vocabulary/ngr-virksomhet#harVarslingsadresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:harVarslingsadresse |
| native | https://data.norge.no/ngr/ngr-virksomhet/har_varslingsadresse |




## LinkML Source

<details>
```yaml
name: har_varslingsadresse
description: Offisiell varslingsadresse for offentlege meldingar.
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
slot_uri: ngrv:harVarslingsadresse
domain_of:
- Virksomhet
range: Varslingsadresse

```
</details>