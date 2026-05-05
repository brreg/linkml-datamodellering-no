

# Slot: undervisningsgruppe 



URI: [https://schema.fintlabs.no/utdanning/:undervisningsgruppe](https://schema.fintlabs.no/utdanning/:undervisningsgruppe)
Alias: undervisningsgruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Time](time.md) | Ein time i timeplanen |  no  |
| [Fag](fag.md) | Eit skulefag |  no  |
| [Undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md) | Eit elevs medlemskap i ei undervisningsgruppe |  no  |
| [Fraversregistrering](fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Fag](fag.md), [Time](time.md), [Undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md), [Fraversregistrering](fraversregistrering.md) |

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