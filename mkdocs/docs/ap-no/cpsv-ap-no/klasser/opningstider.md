

# Slot: opningstider 


_Opningstider._





URI: [cv:openingHours](http://data.europa.eu/m8g/openingHours)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktpunkt](kontaktpunkt.md) | Kontaktinformasjon for ei teneste eller ein organisasjon |  yes  |
| [Tjenestekanal](tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Kontaktpunkt](kontaktpunkt.md), [Tjenestekanal](tjenestekanal.md) |
| Slot URI | [cv:openingHours](http://data.europa.eu/m8g/openingHours) |

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
| self | cv:openingHours |
| native | https://data.norge.no/ap-no/cpsv-ap-no/opningstider |




## LinkML Source

<details>
```yaml
name: opningstider
description: Opningstider.
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: cv:openingHours
domain_of:
- Kontaktpunkt
- Tjenestekanal
range: string
multivalued: true

```
</details>