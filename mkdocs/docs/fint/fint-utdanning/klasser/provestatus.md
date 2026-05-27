

# Slot: provestatus 


_Status for prøva._





URI: [utd:provestatus](https://schema.fintlabs.no/utdanning/provestatus)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AvlagtProve](avlagtprove.md) | Ei avlagt prøve for ein lærling |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Provestatus](provestatus.md) |
| Domain Of | [AvlagtProve](avlagtprove.md) |
| Slot URI | [utd:provestatus](https://schema.fintlabs.no/utdanning/provestatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:provestatus |
| native | https://schema.fintlabs.no/utdanning/:provestatus |




## LinkML Source

<details>
```yaml
name: provestatus
description: Status for prøva.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:provestatus
domain_of:
- AvlagtProve
range: Provestatus

```
</details>