

# Slot: skole 


_Skulen dette gjeld._





URI: [utd:skole](https://schema.fintlabs.no/utdanning/skole)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  yes  |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  yes  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  yes  |
| [Skoleressurs](skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |  yes  |
| [Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |  yes  |
| [Fag](fag.md) | Eit skulefag |  yes  |
| [Faggruppe](faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  yes  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  yes  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skole](skole.md) |
| Domain Of | [Elevforhold](elevforhold.md), [Klasse](klasse.md), [Kontaktlaerergruppe](kontaktlaerergruppe.md), [Persongruppe](persongruppe.md), [Skoleressurs](skoleressurs.md), [Utdanningsprogram](utdanningsprogram.md), [Fag](fag.md), [Faggruppe](faggruppe.md), [Undervisningsgruppe](undervisningsgruppe.md), [Eksamensgruppe](eksamensgruppe.md) |
| Slot URI | [utd:skole](https://schema.fintlabs.no/utdanning/skole) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:skole |
| native | https://schema.fintlabs.no/utdanning/:skole |




## LinkML Source

<details>
```yaml
name: skole
description: Skulen dette gjeld.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:skole
domain_of:
- Elevforhold
- Klasse
- Kontaktlaerergruppe
- Persongruppe
- Skoleressurs
- Utdanningsprogram
- Fag
- Faggruppe
- Undervisningsgruppe
- Eksamensgruppe
range: Skole

```
</details>