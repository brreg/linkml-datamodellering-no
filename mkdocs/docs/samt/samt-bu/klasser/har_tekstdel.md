

# Slot: har_tekstdel 


_Tekstleg innhald i merknaden._





URI: [oa:hasBody](http://www.w3.org/ns/oa#hasBody)
Alias: har_tekstdel

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
| Range | [Tekstdel](tekstdel.md) |
| Domain Of | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| Slot URI | [oa:hasBody](http://www.w3.org/ns/oa#hasBody) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oa:hasBody |
| native | https://data.norge.no/linkml/dqv-ap-no/har_tekstdel |




## LinkML Source

<details>
```yaml
name: har_tekstdel
description: Tekstleg innhald i merknaden.
from_schema: https://data.norge.no/linkml/dqv-ap-no
slot_uri: oa:hasBody
alias: har_tekstdel
domain_of:
- Kvalitetsmerknad
range: Tekstdel

```
</details>