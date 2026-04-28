

# Slot: er_motivert_av 


_Motivasjonen bak kvalitetsmerknaden (t.d. oa:assessing)._





URI: [oa:motivatedBy](http://www.w3.org/ns/oa#motivatedBy)
Alias: er_motivert_av

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kvalitetsmerknad](Kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |  yes  |
| [Brukartilbakemelding](Brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |  no  |
| [Kvalitetssertifikat](Kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Kvalitetsmerknad](Kvalitetsmerknad.md) |
| Slot URI | [oa:motivatedBy](http://www.w3.org/ns/oa#motivatedBy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oa:motivatedBy |
| native | https://data.norge.no/linkml/dqv-ap-no/er_motivert_av |




## LinkML Source

<details>
```yaml
name: er_motivert_av
description: Motivasjonen bak kvalitetsmerknaden (t.d. oa:assessing).
from_schema: https://data.norge.no/linkml/dqv-ap-no
rank: 1000
slot_uri: oa:motivatedBy
alias: er_motivert_av
domain_of:
- Kvalitetsmerknad
range: uriorcurie

```
</details>