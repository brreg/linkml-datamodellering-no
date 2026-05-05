

# Slot: vigoreferanse 



URI: [https://schema.fintlabs.no/utdanning/:vigoreferanse](https://schema.fintlabs.no/utdanning/:vigoreferanse)
Alias: vigoreferanse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fag](fag.md) | Eit skulefag |  no  |
| [Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |  no  |
| [Karakterskala](karakterskala.md) | Skala for karaktersetjing (t |  no  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  no  |
| [Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |  no  |
| [Programomrade](programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Skole](skole.md), [Arstrinn](arstrinn.md), [Programomrade](programomrade.md), [Utdanningsprogram](utdanningsprogram.md), [Fag](fag.md), [Karakterskala](karakterskala.md) |

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