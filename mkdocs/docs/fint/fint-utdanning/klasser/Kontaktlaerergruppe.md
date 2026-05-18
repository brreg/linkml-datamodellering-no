

# Slot: kontaktlaerergruppe 


_Kontaktlærargruppe._





URI: [utd:kontaktlaerergruppe](https://schema.fintlabs.no/utdanning/kontaktlaerergruppe)
Alias: kontaktlaerergruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  yes  |
| [Kontaktlaerergruppemedlemskap](kontaktlaerergruppemedlemskap.md) | Eit elevs medlemskap i ei kontaktlærargruppe |  yes  |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktlaerergruppe](kontaktlaerergruppe.md) |
| Domain Of | [Klasse](klasse.md), [Kontaktlaerergruppemedlemskap](kontaktlaerergruppemedlemskap.md), [Skole](skole.md), [Undervisningsforhold](undervisningsforhold.md) |
| Slot URI | [utd:kontaktlaerergruppe](https://schema.fintlabs.no/utdanning/kontaktlaerergruppe) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:kontaktlaerergruppe |
| native | https://schema.fintlabs.no/utdanning/:kontaktlaerergruppe |




## LinkML Source

<details>
```yaml
name: kontaktlaerergruppe
description: Kontaktlærargruppe.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:kontaktlaerergruppe
alias: kontaktlaerergruppe
domain_of:
- Klasse
- Kontaktlaerergruppemedlemskap
- Skole
- Undervisningsforhold
range: Kontaktlaerergruppe

```
</details>