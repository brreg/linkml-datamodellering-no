

# Slot: klasse 



URI: [https://schema.fintlabs.no/utdanning/:klasse](https://schema.fintlabs.no/utdanning/:klasse)
Alias: klasse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |  no  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  no  |
| [Klassemedlemskap](klassemedlemskap.md) | Eit elevs medlemskap i ei klasse |  no  |
| [Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Klassemedlemskap](klassemedlemskap.md), [Kontaktlaerergruppe](kontaktlaerergruppe.md), [Skole](skole.md), [Arstrinn](arstrinn.md), [Undervisningsforhold](undervisningsforhold.md) |

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