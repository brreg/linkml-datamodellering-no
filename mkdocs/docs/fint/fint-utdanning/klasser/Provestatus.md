

# Slot: provestatus 


_Status for prøva._





URI: [utd:provestatus](https://schema.fintlabs.no/utdanning/provestatus)
Alias: provestatus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AvlagtProve](AvlagtProve.md) | Ei avlagt prøve for ein lærling |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Provestatus](Provestatus.md) |
| Domain Of | [AvlagtProve](AvlagtProve.md) |
| Slot URI | [utd:provestatus](https://schema.fintlabs.no/utdanning/provestatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AvlagtProve](AvlagtProve.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




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
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:provestatus
alias: provestatus
owner: AvlagtProve
domain_of:
- AvlagtProve
range: Provestatus

```
</details>