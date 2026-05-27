

# Slot: har_ansvarleg_styremakt 


_Offentleg organisasjon ansvarleg for tenesta._





URI: [cv:hasCompetentAuthority](http://data.europa.eu/m8g/hasCompetentAuthority)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OffentligOrganisasjon](offentligorganisasjon.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md) |
| Slot URI | [cv:hasCompetentAuthority](http://data.europa.eu/m8g/hasCompetentAuthority) |

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
| self | cv:hasCompetentAuthority |
| native | https://data.norge.no/ap-no/cpsv-ap-no/har_ansvarleg_styremakt |




## LinkML Source

<details>
```yaml
name: har_ansvarleg_styremakt
description: Offentleg organisasjon ansvarleg for tenesta.
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: cv:hasCompetentAuthority
domain_of:
- OffentligTjeneste
range: OffentligOrganisasjon
multivalued: true

```
</details>