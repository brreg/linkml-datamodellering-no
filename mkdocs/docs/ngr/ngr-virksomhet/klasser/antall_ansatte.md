

# Slot: antall_ansatte 


_Antal tilsette i verksemda (rapportert til a-ordninga)._





URI: [ngrv:antallAnsatte](https://data.norge.no/vocabulary/ngr-virksomhet#antallAnsatte)
Alias: antall_ansatte

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
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Virksomhet](virksomhet.md) |
| Slot URI | [ngrv:antallAnsatte](https://data.norge.no/vocabulary/ngr-virksomhet#antallAnsatte) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:antallAnsatte |
| native | https://data.norge.no/linkml/ngr-virksomhet/antall_ansatte |




## LinkML Source

<details>
```yaml
name: antall_ansatte
description: Antal tilsette i verksemda (rapportert til a-ordninga).
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
slot_uri: ngrv:antallAnsatte
alias: antall_ansatte
domain_of:
- Virksomhet
range: integer

```
</details>