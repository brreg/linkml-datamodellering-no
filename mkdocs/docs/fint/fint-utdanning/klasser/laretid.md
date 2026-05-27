

# Slot: laretid 


_Læringstidsperiode for lærlingen._





URI: [utd:laretid](https://schema.fintlabs.no/utdanning/laretid)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Laerling](laerling.md) | Ein lærling i yrkesopplæring |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Periode](periode.md) |
| Domain Of | [Laerling](laerling.md) |
| Slot URI | [utd:laretid](https://schema.fintlabs.no/utdanning/laretid) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:laretid |
| native | https://schema.fintlabs.no/utdanning/:laretid |




## LinkML Source

<details>
```yaml
name: laretid
description: Læringstidsperiode for lærlingen.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:laretid
domain_of:
- Laerling
range: Periode
inlined: true

```
</details>