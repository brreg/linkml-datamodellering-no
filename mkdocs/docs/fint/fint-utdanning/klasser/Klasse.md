

# Slot: klasse 



URI: [https://schema.fintlabs.no/utdanning/:klasse](https://schema.fintlabs.no/utdanning/:klasse)
Alias: klasse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](Skole.md) | Ein skule eller opplæringsinstitusjon |  no  |
| [Arstrinn](Arstrinn.md) | Eit årstrinn i skulen (t |  no  |
| [Kontaktlaerergruppe](Kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Klassemedlemskap](Klassemedlemskap.md) | Eit elevs medlemskap i ei klasse |  no  |
| [Undervisningsforhold](Undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Klassemedlemskap](Klassemedlemskap.md), [Kontaktlaerergruppe](Kontaktlaerergruppe.md), [Skole](Skole.md), [Arstrinn](Arstrinn.md), [Undervisningsforhold](Undervisningsforhold.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:klasse |
| native | https://schema.fintlabs.no/utdanning/:klasse |




## LinkML Source

<details>
```yaml
name: klasse
alias: klasse
domain_of:
- Klassemedlemskap
- Kontaktlaerergruppe
- Skole
- Arstrinn
- Undervisningsforhold
range: string

```
</details>