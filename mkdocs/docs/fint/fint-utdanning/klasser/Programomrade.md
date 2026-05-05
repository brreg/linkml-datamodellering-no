

# Slot: programomrade 



URI: [https://schema.fintlabs.no/utdanning/:programomrade](https://schema.fintlabs.no/utdanning/:programomrade)
Alias: programomrade

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |  no  |
| [Fag](fag.md) | Eit skulefag |  no  |
| [Programomrademedlemskap](programomrademedlemskap.md) | Eit elevs tilknyting til eit programområde |  no  |
| [Laerling](laerling.md) | Ein lærling i yrkesopplæring |  no  |
| [OtUngdom](otungdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |  no  |
| [Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Arstrinn](arstrinn.md), [Programomrademedlemskap](programomrademedlemskap.md), [Utdanningsprogram](utdanningsprogram.md), [Fag](fag.md), [Laerling](laerling.md), [OtUngdom](otungdom.md) |

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