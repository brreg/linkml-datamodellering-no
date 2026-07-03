

# Slot: er_motivert_av 


_Motivasjonen bak kvalitetsmerknaden._





URI: [oa:motivatedBy](http://www.w3.org/ns/oa#motivatedBy)
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
| Range | [DqvMotivasjon](dqvmotivasjon.md) |
| Domain Of | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| Slot URI | [oa:motivatedBy](http://www.w3.org/ns/oa#motivatedBy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oa:motivatedBy |
| native | https://data.norge.no/ap-no/dqv-core/er_motivert_av |




## LinkML Source

<details>
```yaml
name: er_motivert_av
description: Motivasjonen bak kvalitetsmerknaden.
from_schema: https://data.norge.no/ap-no/dqv-core
slot_uri: oa:motivatedBy
domain_of:
- Kvalitetsmerknad
range: DqvMotivasjon

```
</details>