

# Slot: har_kontaktside 


_Nettside for kontakt._





URI: [vcard:hasURL](http://www.w3.org/2006/vcard/ns#hasURL)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon for ein aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Kontaktopplysning](kontaktopplysning.md) |
| Slot URI | [vcard:hasURL](http://www.w3.org/2006/vcard/ns#hasURL) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vcard:hasURL |
| native | https://data.norge.no/linkml/dcat-ap-no/har_kontaktside |




## LinkML Source

<details>
```yaml
name: har_kontaktside
description: Nettside for kontakt.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: vcard:hasURL
domain_of:
- Kontaktopplysning
range: string

```
</details>