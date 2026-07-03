

# Slot: har_maal 


_Datasett, distribusjon eller datatjeneste merknaden gjeld._





URI: [oa:hasTarget](http://www.w3.org/ns/oa#hasTarget)
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
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| Slot URI | [oa:hasTarget](http://www.w3.org/ns/oa#hasTarget) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oa:hasTarget |
| native | https://data.norge.no/ap-no/dqv-core/har_maal |




## LinkML Source

<details>
```yaml
name: har_maal
description: Datasett, distribusjon eller datatjeneste merknaden gjeld.
from_schema: https://data.norge.no/ap-no/dqv-core
slot_uri: oa:hasTarget
domain_of:
- Kvalitetsmerknad
range: uriorcurie

```
</details>