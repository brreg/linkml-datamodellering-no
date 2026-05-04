

# Slot: grepreferanse 



URI: [https://schema.fintlabs.no/utdanning/:grepreferanse](https://schema.fintlabs.no/utdanning/:grepreferanse)
Alias: grepreferanse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fag](Fag.md) | Eit skulefag |  no  |
| [Arstrinn](Arstrinn.md) | Eit årstrinn i skulen (t |  no  |
| [Programomrade](Programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  no  |
| [Utdanningsprogram](Utdanningsprogram.md) | Eit utdanningsprogram (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Arstrinn](Arstrinn.md), [Programomrade](Programomrade.md), [Utdanningsprogram](Utdanningsprogram.md), [Fag](Fag.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:grepreferanse |
| native | https://schema.fintlabs.no/utdanning/:grepreferanse |




## LinkML Source

<details>
```yaml
name: grepreferanse
alias: grepreferanse
domain_of:
- Arstrinn
- Programomrade
- Utdanningsprogram
- Fag
range: string

```
</details>