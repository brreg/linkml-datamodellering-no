

# Slot: er_i_kvalitetsdimensjon 


_Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld._

__





URI: [dqv:inDimension](http://www.w3.org/ns/dqv#inDimension)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kvalitetsmerknad](kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |  yes  |
| [Standard](standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |  yes  |
| [Brukartilbakemelding](brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |  no  |
| [Kvalitetssertifikat](kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kvalitetsdimensjon](kvalitetsdimensjon.md) |
| Domain Of | [Kvalitetsmerknad](kvalitetsmerknad.md), [Standard](standard.md) |
| Slot URI | [dqv:inDimension](http://www.w3.org/ns/dqv#inDimension) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dqv:inDimension |
| native | https://data.norge.no/linkml/dqv-ap-no/er_i_kvalitetsdimensjon |




## LinkML Source

<details>
```yaml
name: er_i_kvalitetsdimensjon
description: 'Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld.

  '
from_schema: https://data.norge.no/linkml/dqv-ap-no
slot_uri: dqv:inDimension
domain_of:
- Kvalitetsmerknad
- Standard
range: Kvalitetsdimensjon
required: false
multivalued: true

```
</details>