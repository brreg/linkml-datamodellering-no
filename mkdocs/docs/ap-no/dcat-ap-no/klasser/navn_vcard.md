

# Slot: navn_vcard 


_Formatert namn (vCard)._





URI: [vcard:fn](http://www.w3.org/2006/vcard/ns#fn)
Alias: navn_vcard

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktopplysning](Kontaktopplysning.md) | Kontaktinformasjon for ein aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](LangString.md) |
| Domain Of | [Kontaktopplysning](Kontaktopplysning.md) |
| Slot URI | [vcard:fn](http://www.w3.org/2006/vcard/ns#fn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vcard:fn |
| native | https://data.norge.no/linkml/dcat-ap-no/navn_vcard |




## LinkML Source

<details>
```yaml
name: navn_vcard
description: Formatert namn (vCard).
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: vcard:fn
alias: navn_vcard
domain_of:
- Kontaktopplysning
range: LangString
multivalued: true

```
</details>