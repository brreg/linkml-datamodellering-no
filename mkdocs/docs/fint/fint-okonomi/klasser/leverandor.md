

# Slot: leverandor 


_Leverandør._





URI: [okn:leverandor](https://schema.fintlabs.no/okonomi/leverandor)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  yes  |
| [Leverandorgruppe](leverandorgruppe.md) | Gruppering av leverandørar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Leverandor](leverandor.md) |
| Domain Of | [Transaksjon](transaksjon.md), [Leverandorgruppe](leverandorgruppe.md) |
| Slot URI | [okn:leverandor](https://schema.fintlabs.no/okonomi/leverandor) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:leverandor |
| native | https://schema.fintlabs.no/okonomi/:leverandor |




## LinkML Source

<details>
```yaml
name: leverandor
description: Leverandør.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:leverandor
domain_of:
- Transaksjon
- Leverandorgruppe
range: Leverandor

```
</details>