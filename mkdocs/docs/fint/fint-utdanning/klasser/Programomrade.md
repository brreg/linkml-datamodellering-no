

# Slot: programomrade 


_Programområde._





URI: [utd:programomrade](https://schema.fintlabs.no/utdanning/programomrade)
Alias: programomrade

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtUngdom](otungdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |  yes  |
| [Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |  yes  |
| [Laerling](laerling.md) | Ein lærling i yrkesopplæring |  yes  |
| [Programomrademedlemskap](programomrademedlemskap.md) | Eit elevs tilknyting til eit programområde |  yes  |
| [Fag](fag.md) | Eit skulefag |  yes  |
| [Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |  yes  |






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


* from schema: https://data.norge.no/linkml/fint-utdanning




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
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:programomrade
alias: programomrade
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