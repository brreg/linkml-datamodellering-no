

# Slot: organisasjonsnummer 


_Niesifra organisasjonsnummer tildelt av Enhetsregisteret._





URI: [ngrv:organisasjonsnummer](https://data.norge.no/vocabulary/ngr-virksomhet#organisasjonsnummer)
Alias: organisasjonsnummer

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
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Virksomhet](virksomhet.md) |
| Slot URI | [ngrv:organisasjonsnummer](https://data.norge.no/vocabulary/ngr-virksomhet#organisasjonsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-virksomhet




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrv:organisasjonsnummer |
| native | https://data.norge.no/linkml/ngr-virksomhet/organisasjonsnummer |




## LinkML Source

<details>
```yaml
name: organisasjonsnummer
description: Niesifra organisasjonsnummer tildelt av Enhetsregisteret.
from_schema: https://data.norge.no/linkml/ngr-virksomhet
rank: 1000
slot_uri: ngrv:organisasjonsnummer
alias: organisasjonsnummer
domain_of:
- Virksomhet
range: string

```
</details>