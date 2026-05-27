

# Slot: termin 


_Termin._





URI: [utd:termin](https://schema.fintlabs.no/utdanning/termin)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  yes  |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  yes  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  yes  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  yes  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Termin](termin.md) |
| Domain Of | [Klasse](klasse.md), [Kontaktlaerergruppe](kontaktlaerergruppe.md), [Persongruppe](persongruppe.md), [Undervisningsgruppe](undervisningsgruppe.md), [Eksamensgruppe](eksamensgruppe.md) |
| Slot URI | [utd:termin](https://schema.fintlabs.no/utdanning/termin) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:termin |
| native | https://schema.fintlabs.no/utdanning/:termin |




## LinkML Source

<details>
```yaml
name: termin
description: Termin.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:termin
domain_of:
- Klasse
- Kontaktlaerergruppe
- Persongruppe
- Undervisningsgruppe
- Eksamensgruppe
range: Termin

```
</details>