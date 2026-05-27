

# Slot: kategori 


_Kategori for kontaktpunktet._





URI: [vcard:category](http://www.w3.org/2006/vcard/ns#category)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktpunkt](kontaktpunkt.md) | Kontaktinformasjon for ei teneste eller ein organisasjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Kontaktpunkt](kontaktpunkt.md) |
| Slot URI | [vcard:category](http://www.w3.org/2006/vcard/ns#category) |

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
| self | vcard:category |
| native | https://data.norge.no/ap-no/cpsv-ap-no/kategori |




## LinkML Source

<details>
```yaml
name: kategori
description: Kategori for kontaktpunktet.
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: vcard:category
domain_of:
- Kontaktpunkt
range: string
multivalued: true

```
</details>