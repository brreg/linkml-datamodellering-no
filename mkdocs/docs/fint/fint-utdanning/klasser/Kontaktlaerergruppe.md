

# Slot: kontaktlaerergruppe 



URI: [https://schema.fintlabs.no/utdanning/:kontaktlaerergruppe](https://schema.fintlabs.no/utdanning/:kontaktlaerergruppe)
Alias: kontaktlaerergruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Undervisningsforhold](Undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  no  |
| [Skole](Skole.md) | Ein skule eller opplæringsinstitusjon |  no  |
| [Klasse](Klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |
| [Kontaktlaerergruppemedlemskap](Kontaktlaerergruppemedlemskap.md) | Eit elevs medlemskap i ei kontaktlærargruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Klasse](Klasse.md), [Kontaktlaerergruppemedlemskap](Kontaktlaerergruppemedlemskap.md), [Skole](Skole.md), [Undervisningsforhold](Undervisningsforhold.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:kontaktlaerergruppe |
| native | https://schema.fintlabs.no/utdanning/:kontaktlaerergruppe |




## LinkML Source

<details>
```yaml
name: kontaktlaerergruppe
alias: kontaktlaerergruppe
domain_of:
- Klasse
- Kontaktlaerergruppemedlemskap
- Skole
- Undervisningsforhold
range: string

```
</details>