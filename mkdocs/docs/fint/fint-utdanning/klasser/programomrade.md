

# Slot: programomrade 


_Programområde._





URI: [utd:programomrade](https://schema.fintlabs.no/utdanning/programomrade)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |  yes  |
| [Programomrademedlemskap](programomrademedlemskap.md) | Eit elevs tilknyting til eit programområde |  yes  |
| [Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |  yes  |
| [Fag](fag.md) | Eit skulefag |  yes  |
| [Laerling](laerling.md) | Ein lærling i yrkesopplæring |  yes  |
| [OtUngdom](otungdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Programomrade](programomrade.md) |
| Domain Of | [Arstrinn](arstrinn.md), [Programomrademedlemskap](programomrademedlemskap.md), [Utdanningsprogram](utdanningsprogram.md), [Fag](fag.md), [Laerling](laerling.md), [OtUngdom](otungdom.md) |
| Slot URI | [utd:programomrade](https://schema.fintlabs.no/utdanning/programomrade) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:programomrade |
| native | https://schema.fintlabs.no/utdanning/:programomrade |




## LinkML Source

<details>
```yaml
name: programomrade
description: Programområde.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:programomrade
domain_of:
- Arstrinn
- Programomrademedlemskap
- Utdanningsprogram
- Fag
- Laerling
- OtUngdom
range: Programomrade

```
</details>