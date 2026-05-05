

# Slot: har_epost 


_E-postadresse til kontaktpunktet._





URI: [vcard:hasEmail](http://www.w3.org/2006/vcard/ns#hasEmail)
Alias: har_epost

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon for ein aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](uri.md) |
| Domain Of | [Kontaktopplysning](kontaktopplysning.md) |
| Slot URI | [vcard:hasEmail](http://www.w3.org/2006/vcard/ns#hasEmail) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vcard:hasEmail |
| native | samtbuskole:har_epost |




## LinkML Source

<details>
```yaml
name: har_epost
description: E-postadresse til kontaktpunktet.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: vcard:hasEmail
alias: har_epost
domain_of:
- Kontaktopplysning
range: uri

```
</details>