

# Slot: telefon 


_Telefonnummer._





URI: [cv:telephone](http://data.europa.eu/m8g/telephone)
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
| Slot URI | [cv:telephone](http://data.europa.eu/m8g/telephone) |

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
| self | cv:telephone |
| native | https://data.norge.no/linkml/cpsv-ap-no/telefon |




## LinkML Source

<details>
```yaml
name: telefon
description: Telefonnummer.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:telephone
domain_of:
- Kontaktpunkt
range: string
multivalued: true

```
</details>