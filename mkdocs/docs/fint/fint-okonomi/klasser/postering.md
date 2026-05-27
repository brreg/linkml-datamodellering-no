

# Slot: postering 


_Posteringar tilhøyrande transaksjonen._





URI: [okn:postering](https://schema.fintlabs.no/okonomi/postering)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Postering](postering.md) |
| Domain Of | [Transaksjon](transaksjon.md) |
| Slot URI | [okn:postering](https://schema.fintlabs.no/okonomi/postering) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:postering |
| native | https://schema.fintlabs.no/okonomi/:postering |




## LinkML Source

<details>
```yaml
name: postering
description: Posteringar tilhøyrande transaksjonen.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:postering
domain_of:
- Transaksjon
range: Postering
multivalued: true

```
</details>