

# Slot: faggruppe 



URI: [https://schema.fintlabs.no/utdanning/:faggruppe](https://schema.fintlabs.no/utdanning/:faggruppe)
Alias: faggruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fag](fag.md) | Eit skulefag |  no  |
| [Fraversregistrering](fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  no  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  no  |
| [Faggruppemedlemskap](faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Skole](skole.md), [Fag](fag.md), [Faggruppemedlemskap](faggruppemedlemskap.md), [Fraversregistrering](fraversregistrering.md) |

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