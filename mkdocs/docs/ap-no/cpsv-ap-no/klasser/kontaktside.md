

# Slot: kontaktside 


_Kontaktside (nettadresse)._





URI: [cv:contactPage](http://data.europa.eu/m8g/contactPage)
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
| Slot URI | [cv:contactPage](http://data.europa.eu/m8g/contactPage) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:contactPage |
| native | https://data.norge.no/linkml/cpsv-ap-no/kontaktside |




## LinkML Source

<details>
```yaml
name: kontaktside
description: Kontaktside (nettadresse).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:contactPage
domain_of:
- Kontaktpunkt
range: uri
multivalued: true

```
</details>