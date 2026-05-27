

# Slot: klasse 


_Klasse._





URI: [utd:klasse](https://schema.fintlabs.no/utdanning/klasse)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Klassemedlemskap](klassemedlemskap.md) | Eit elevs medlemskap i ei klasse |  yes  |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  yes  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |  yes  |
| [Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Klasse](klasse.md) |
| Domain Of | [Klassemedlemskap](klassemedlemskap.md), [Kontaktlaerergruppe](kontaktlaerergruppe.md), [Skole](skole.md), [Arstrinn](arstrinn.md), [Undervisningsforhold](undervisningsforhold.md) |
| Slot URI | [utd:klasse](https://schema.fintlabs.no/utdanning/klasse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:klasse |
| native | https://schema.fintlabs.no/utdanning/:klasse |




## LinkML Source

<details>
```yaml
name: klasse
description: Klasse.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:klasse
domain_of:
- Klassemedlemskap
- Kontaktlaerergruppe
- Skole
- Arstrinn
- Undervisningsforhold
range: Klasse

```
</details>