

# Slot: er_i_kvalitetsdimensjon 


_Kvalitetsdimensjonen denne merknaden eller standarden gjeld._





URI: [dqv:inDimension](http://www.w3.org/ns/dqv#inDimension)
Alias: er_i_kvalitetsdimensjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Brukartilbakemelding](brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |  no  |
| [Kvalitetssertifikat](kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |  no  |
| [Standard](standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |  yes  |
| [Kvalitetsmerknad](kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |  yes  |






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
description: Kvalitetsdimensjonen denne merknaden eller standarden gjeld.
from_schema: https://data.norge.no/linkml/dqv-ap-no
rank: 1000
slot_uri: dqv:inDimension
alias: er_i_kvalitetsdimensjon
domain_of:
- Kvalitetsmerknad
- Standard
range: Kvalitetsdimensjon

```
</details>