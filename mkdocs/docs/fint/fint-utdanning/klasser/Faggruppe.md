

# Slot: faggruppe 



URI: [https://schema.fintlabs.no/utdanning/:faggruppe](https://schema.fintlabs.no/utdanning/:faggruppe)
Alias: faggruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fag](Fag.md) | Eit skulefag |  no  |
| [Faggruppemedlemskap](Faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |  no  |
| [Skole](Skole.md) | Ein skule eller opplæringsinstitusjon |  no  |
| [Fraversregistrering](Fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Skole](Skole.md), [Fag](Fag.md), [Faggruppemedlemskap](Faggruppemedlemskap.md), [Fraversregistrering](Fraversregistrering.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:faggruppe |
| native | https://schema.fintlabs.no/utdanning/:faggruppe |




## LinkML Source

<details>
```yaml
name: faggruppe
alias: faggruppe
domain_of:
- Skole
- Fag
- Faggruppemedlemskap
- Fraversregistrering
range: string

```
</details>