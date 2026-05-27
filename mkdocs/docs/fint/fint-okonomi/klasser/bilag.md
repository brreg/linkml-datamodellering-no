

# Slot: bilag 


_Bilag til transaksjonen._





URI: [okn:bilag](https://schema.fintlabs.no/okonomi/bilag)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bilag](bilag.md) |
| Domain Of | [Transaksjon](transaksjon.md) |
| Slot URI | [okn:bilag](https://schema.fintlabs.no/okonomi/bilag) |

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
| self | okn:bilag |
| native | https://schema.fintlabs.no/okonomi/:bilag |




## LinkML Source

<details>
```yaml
name: bilag
description: Bilag til transaksjonen.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:bilag
domain_of:
- Transaksjon
range: Bilag
multivalued: true
inlined: true
inlined_as_list: true

```
</details>