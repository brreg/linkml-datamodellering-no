

# Slot: undervisningsgruppe 



URI: [https://schema.fintlabs.no/utdanning/:undervisningsgruppe](https://schema.fintlabs.no/utdanning/:undervisningsgruppe)
Alias: undervisningsgruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fag](Fag.md) | Eit skulefag |  no  |
| [Undervisningsgruppemedlemskap](Undervisningsgruppemedlemskap.md) | Eit elevs medlemskap i ei undervisningsgruppe |  no  |
| [Time](Time.md) | Ein time i timeplanen |  no  |
| [Fraversregistrering](Fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Fag](Fag.md), [Time](Time.md), [Undervisningsgruppemedlemskap](Undervisningsgruppemedlemskap.md), [Fraversregistrering](Fraversregistrering.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:undervisningsgruppe |
| native | https://schema.fintlabs.no/utdanning/:undervisningsgruppe |




## LinkML Source

<details>
```yaml
name: undervisningsgruppe
alias: undervisningsgruppe
domain_of:
- Fag
- Time
- Undervisningsgruppemedlemskap
- Fraversregistrering
range: string

```
</details>