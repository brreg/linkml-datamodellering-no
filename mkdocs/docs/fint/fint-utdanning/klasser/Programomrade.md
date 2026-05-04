

# Slot: programomrade 



URI: [https://schema.fintlabs.no/utdanning/:programomrade](https://schema.fintlabs.no/utdanning/:programomrade)
Alias: programomrade

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Utdanningsprogram](Utdanningsprogram.md) | Eit utdanningsprogram (t |  no  |
| [Fag](Fag.md) | Eit skulefag |  no  |
| [Arstrinn](Arstrinn.md) | Eit årstrinn i skulen (t |  no  |
| [OtUngdom](OtUngdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |  no  |
| [Programomrademedlemskap](Programomrademedlemskap.md) | Eit elevs tilknyting til eit programområde |  no  |
| [Laerling](Laerling.md) | Ein lærling i yrkesopplæring |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Arstrinn](Arstrinn.md), [Programomrademedlemskap](Programomrademedlemskap.md), [Utdanningsprogram](Utdanningsprogram.md), [Fag](Fag.md), [Laerling](Laerling.md), [OtUngdom](OtUngdom.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:programomrade |
| native | https://schema.fintlabs.no/utdanning/:programomrade |




## LinkML Source

<details>
```yaml
name: programomrade
alias: programomrade
domain_of:
- Arstrinn
- Programomrademedlemskap
- Utdanningsprogram
- Fag
- Laerling
- OtUngdom
range: string

```
</details>