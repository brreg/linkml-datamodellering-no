

# Slot: navn_vcard 


_Formatert namn (vCard)._





URI: [vcard:fn](http://www.w3.org/2006/vcard/ns#fn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon for ein aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [Kontaktopplysning](kontaktopplysning.md) |
| Slot URI | [vcard:fn](http://www.w3.org/2006/vcard/ns#fn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vcard:fn |
| native | https://data.norge.no/ap-no/dcat-ap-no/navn_vcard |




## LinkML Source

<details>
```yaml
name: navn_vcard
description: Formatert namn (vCard).
from_schema: https://data.norge.no/ap-no/dcat-ap-no
rank: 1000
slot_uri: vcard:fn
domain_of:
- Kontaktopplysning
range: LangString
multivalued: true

```
</details>