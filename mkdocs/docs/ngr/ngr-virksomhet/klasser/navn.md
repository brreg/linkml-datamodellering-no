

# Slot: navn 


_Registrert namn på verksemda i Enhetsregisteret._





URI: [ngrv:navn](https://data.norge.no/vocabulary/ngr-virksomhet#navn)
Alias: navn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Underenhet](Underenhet.md) | Ei underleining er ein geografisk lokasjon der aktiviteten til ei hovudeining... |  no  |
| [Virksomhet](Virksomhet.md) | Abstrakt overklasse for alle einingar registrert i Enhetsregisteret |  yes  |
| [Hovedenhet](Hovedenhet.md) | Ei hovudeining er den juridiske eininga registrert i Enhetsregisteret (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Virksomhet](Virksomhet.md) |
| Slot URI | [ngrv:navn](https://data.norge.no/vocabulary/ngr-virksomhet#navn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:navn |
| native | https://data.norge.no/linkml/ngr-virksomhet/navn |




## LinkML Source

<details>
```yaml
name: navn
description: Registrert namn på verksemda i Enhetsregisteret.
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
slot_uri: ngrv:navn
alias: navn
domain_of:
- Virksomhet
range: string

```
</details>