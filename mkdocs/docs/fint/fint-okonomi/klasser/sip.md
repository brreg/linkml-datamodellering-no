

# Slot: sip 


_SIP-protokoll for VoIP (IP-telefoni)._





URI: [fint:sip](https://schema.fintlabs.no/sip)
Alias: sip

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktinformasjon](kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Kontaktinformasjon](kontaktinformasjon.md) |
| Slot URI | [fint:sip](https://schema.fintlabs.no/sip) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kontaktinformasjon](kontaktinformasjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:sip |
| native | https://schema.fintlabs.no/okonomi/:sip |




## LinkML Source

<details>
```yaml
name: sip
description: SIP-protokoll for VoIP (IP-telefoni).
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: fint:sip
alias: sip
owner: Kontaktinformasjon
domain_of:
- Kontaktinformasjon
range: string

```
</details>