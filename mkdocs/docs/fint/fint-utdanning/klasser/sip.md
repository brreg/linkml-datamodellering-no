

# Slot: sip 


_SIP-protokoll for VoIP (IP-telefoni)._





URI: [fint:sip](https://schema.fintlabs.no/sip)
Alias: sip

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktinformasjon](Kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Kontaktinformasjon](Kontaktinformasjon.md) |
| Slot URI | [fint:sip](https://schema.fintlabs.no/sip) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kontaktinformasjon](Kontaktinformasjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:sip |
| native | https://schema.fintlabs.no/utdanning/:sip |




## LinkML Source

<details>
```yaml
name: sip
description: SIP-protokoll for VoIP (IP-telefoni).
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: fint:sip
alias: sip
owner: Kontaktinformasjon
domain_of:
- Kontaktinformasjon
range: string

```
</details>