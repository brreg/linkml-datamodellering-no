

# Slot: transaksjonsId 


_Intern unik identifikator i økonomisystemet._





URI: [okn:transaksjonsId](https://schema.fintlabs.no/okonomi/transaksjonsId)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Transaksjon](transaksjon.md) |
| Slot URI | [okn:transaksjonsId](https://schema.fintlabs.no/okonomi/transaksjonsId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:transaksjonsId |
| native | https://schema.fintlabs.no/okonomi/:transaksjonsId |




## LinkML Source

<details>
```yaml
name: transaksjonsId
description: Intern unik identifikator i økonomisystemet.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:transaksjonsId
domain_of:
- Transaksjon
range: Identifikator
inlined: true

```
</details>