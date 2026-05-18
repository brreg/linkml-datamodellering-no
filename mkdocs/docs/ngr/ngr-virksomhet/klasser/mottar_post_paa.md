

# Slot: mottar_post_paa 


_Postadressa verksemda mottar post på._





URI: [ngrv:mottarPostPaa](https://data.norge.no/vocabulary/ngr-virksomhet#mottarPostPaa)
Alias: mottar_post_paa

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
| Range | [Postadresse](postadresse.md) |
| Domain Of | [Virksomhet](virksomhet.md) |
| Slot URI | [ngrv:mottarPostPaa](https://data.norge.no/vocabulary/ngr-virksomhet#mottarPostPaa) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:mottarPostPaa |
| native | https://data.norge.no/linkml/ngr-virksomhet/mottar_post_paa |




## LinkML Source

<details>
```yaml
name: mottar_post_paa
description: Postadressa verksemda mottar post på.
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
slot_uri: ngrv:mottarPostPaa
alias: mottar_post_paa
domain_of:
- Virksomhet
range: Postadresse

```
</details>