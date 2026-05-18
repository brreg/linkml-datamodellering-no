

# Slot: faggruppe 


_Faggruppe._





URI: [utd:faggruppe](https://schema.fintlabs.no/utdanning/faggruppe)
Alias: faggruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [Fag](fag.md) | Eit skulefag |  yes  |
| [Fraversregistrering](fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  yes  |
| [Faggruppemedlemskap](faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Faggruppe](faggruppe.md) |
| Domain Of | [Skole](skole.md), [Fag](fag.md), [Faggruppemedlemskap](faggruppemedlemskap.md), [Fraversregistrering](fraversregistrering.md) |
| Slot URI | [utd:faggruppe](https://schema.fintlabs.no/utdanning/faggruppe) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:faggruppe |
| native | https://schema.fintlabs.no/utdanning/:faggruppe |




## LinkML Source

<details>
```yaml
name: faggruppe
description: Faggruppe.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:faggruppe
alias: faggruppe
domain_of:
- Skole
- Fag
- Faggruppemedlemskap
- Fraversregistrering
range: Faggruppe

```
</details>