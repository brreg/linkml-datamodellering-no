

# Slot: enhet 


_OT-eining knytt til ungdommen._





URI: [utd:enhet](https://schema.fintlabs.no/utdanning/enhet)
Alias: enhet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtUngdom](OtUngdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OtEnhet](OtEnhet.md) |
| Domain Of | [OtUngdom](OtUngdom.md) |
| Slot URI | [utd:enhet](https://schema.fintlabs.no/utdanning/enhet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [OtUngdom](OtUngdom.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:enhet |
| native | https://schema.fintlabs.no/utdanning/:enhet |




## LinkML Source

<details>
```yaml
name: enhet
description: OT-eining knytt til ungdommen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:enhet
alias: enhet
owner: OtUngdom
domain_of:
- OtUngdom
range: OtEnhet

```
</details>