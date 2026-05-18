

# Slot: undervisningsforhold 


_Undervisningsforhold._





URI: [utd:undervisningsforhold](https://schema.fintlabs.no/utdanning/undervisningsforhold)
Alias: undervisningsforhold

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  yes  |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  yes  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |
| [Time](time.md) | Ein time i timeplanen |  yes  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  yes  |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Undervisningsforhold](undervisningsforhold.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Klasse](klasse.md), [Kontaktlaerergruppe](kontaktlaerergruppe.md), [Persongruppe](persongruppe.md), [Time](time.md), [Undervisningsgruppe](undervisningsgruppe.md), [Eksamensgruppe](eksamensgruppe.md) |
| Slot URI | [utd:undervisningsforhold](https://schema.fintlabs.no/utdanning/undervisningsforhold) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:undervisningsforhold |
| native | https://schema.fintlabs.no/utdanning/:undervisningsforhold |




## LinkML Source

<details>
```yaml
name: undervisningsforhold
description: Undervisningsforhold.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:undervisningsforhold
alias: undervisningsforhold
domain_of:
- UtdanningContainer
- Klasse
- Kontaktlaerergruppe
- Persongruppe
- Time
- Undervisningsgruppe
- Eksamensgruppe
range: Undervisningsforhold
multivalued: true

```
</details>