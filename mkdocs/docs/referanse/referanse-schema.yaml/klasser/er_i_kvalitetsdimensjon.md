

# Slot: er_i_kvalitetsdimensjon 


_Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld._





URI: [dqv:inDimension](http://www.w3.org/ns/dqv#inDimension)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kvalitetsmerknad](kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |  yes  |
| [Brukartilbakemelding](brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |  no  |
| [Kvalitetssertifikat](kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kvalitetsdimensjon](kvalitetsdimensjon.md) |
| Domain Of | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| Slot URI | [dqv:inDimension](http://www.w3.org/ns/dqv#inDimension) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:inDimension |
| native | https://data.norge.no/ap-no/dqv-core/er_i_kvalitetsdimensjon |




## LinkML Source

<details>
```yaml
name: er_i_kvalitetsdimensjon
description: Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld.
from_schema: https://data.norge.no/ap-no/dqv-core
slot_uri: dqv:inDimension
domain_of:
- Kvalitetsmerknad
range: Kvalitetsdimensjon
required: false
multivalued: true

```
</details>