

# Slot: vigoreferanse 



URI: [https://schema.fintlabs.no/utdanning/:vigoreferanse](https://schema.fintlabs.no/utdanning/:vigoreferanse)
Alias: vigoreferanse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](Skole.md) | Ein skule eller opplæringsinstitusjon |  no  |
| [Utdanningsprogram](Utdanningsprogram.md) | Eit utdanningsprogram (t |  no  |
| [Fag](Fag.md) | Eit skulefag |  no  |
| [Arstrinn](Arstrinn.md) | Eit årstrinn i skulen (t |  no  |
| [Karakterskala](Karakterskala.md) | Skala for karaktersetjing (t |  no  |
| [Programomrade](Programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Skole](Skole.md), [Arstrinn](Arstrinn.md), [Programomrade](Programomrade.md), [Utdanningsprogram](Utdanningsprogram.md), [Fag](Fag.md), [Karakterskala](Karakterskala.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:vigoreferanse |
| native | https://schema.fintlabs.no/utdanning/:vigoreferanse |




## LinkML Source

<details>
```yaml
name: vigoreferanse
alias: vigoreferanse
domain_of:
- Skole
- Arstrinn
- Programomrade
- Utdanningsprogram
- Fag
- Karakterskala
range: string

```
</details>