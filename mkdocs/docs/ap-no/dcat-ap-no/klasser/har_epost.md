

# Slot: har_epost 


_E-postadresse til kontaktpunktet._





URI: [vcard:hasEmail](http://www.w3.org/2006/vcard/ns#hasEmail)
Alias: har_epost

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktopplysning](Kontaktopplysning.md) | Kontaktinformasjon for ein aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Kontaktopplysning](Kontaktopplysning.md) |
| Slot URI | [vcard:hasEmail](http://www.w3.org/2006/vcard/ns#hasEmail) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vcard:hasEmail |
| native | https://data.norge.no/linkml/dcat-ap-no/har_epost |




## LinkML Source

<details>
```yaml
name: har_epost
description: E-postadresse til kontaktpunktet.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: vcard:hasEmail
alias: har_epost
domain_of:
- Kontaktopplysning
range: uri

```
</details>