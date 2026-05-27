

# Slot: navn 


_Registrert namn på verksemda i Enhetsregisteret._





URI: [ngrv:navn](https://data.norge.no/vocabulary/ngr-virksomhet#navn)
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
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Virksomhet](virksomhet.md) |
| Slot URI | [ngrv:navn](https://data.norge.no/vocabulary/ngr-virksomhet#navn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:navn |
| native | https://data.norge.no/ngr/ngr-virksomhet/navn |




## LinkML Source

<details>
```yaml
name: navn
description: Registrert namn på verksemda i Enhetsregisteret.
from_schema: https://data.norge.no/ngr/ngr-virksomhet
rank: 1000
slot_uri: ngrv:navn
domain_of:
- Virksomhet
range: string

```
</details>