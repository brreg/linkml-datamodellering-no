

# Slot: epost 


_E-postadresse (mailto:-URI)._





URI: [cv:email](http://data.europa.eu/m8g/email)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktpunkt](kontaktpunkt.md) | Kontaktinformasjon for ei teneste eller ein organisasjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Kontaktpunkt](kontaktpunkt.md) |
| Slot URI | [cv:email](http://data.europa.eu/m8g/email) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:email |
| native | https://data.norge.no/ap-no/cpsv-ap-no/epost |




## LinkML Source

<details>
```yaml
name: epost
description: E-postadresse (mailto:-URI).
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: cv:email
domain_of:
- Kontaktpunkt
range: uri
multivalued: true

```
</details>