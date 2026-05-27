

# Slot: sip 


_SIP-protokoll for VoIP (IP-telefoni)._





URI: [fint:sip](https://schema.fintlabs.no/sip)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktinformasjon](kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Kontaktinformasjon](kontaktinformasjon.md) |
| Slot URI | [fint:sip](https://schema.fintlabs.no/sip) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:sip |
| native | https://schema.fintlabs.no/:sip |




## LinkML Source

<details>
```yaml
name: sip
description: SIP-protokoll for VoIP (IP-telefoni).
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:sip
domain_of:
- Kontaktinformasjon
range: string

```
</details>