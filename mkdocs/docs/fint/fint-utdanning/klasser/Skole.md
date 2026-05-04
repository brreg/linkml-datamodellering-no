

# Slot: skole 



URI: [https://schema.fintlabs.no/utdanning/:skole](https://schema.fintlabs.no/utdanning/:skole)
Alias: skole

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppe](Eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [Klasse](Klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |
| [Utdanningsprogram](Utdanningsprogram.md) | Eit utdanningsprogram (t |  no  |
| [Fag](Fag.md) | Eit skulefag |  no  |
| [Kontaktlaerergruppe](Kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Faggruppe](Faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  no  |
| [Undervisningsgruppe](Undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [Persongruppe](Persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Skoleressurs](Skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |  no  |
| [Elevforhold](Elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Elevforhold](Elevforhold.md), [Klasse](Klasse.md), [Kontaktlaerergruppe](Kontaktlaerergruppe.md), [Persongruppe](Persongruppe.md), [Skoleressurs](Skoleressurs.md), [Utdanningsprogram](Utdanningsprogram.md), [Fag](Fag.md), [Faggruppe](Faggruppe.md), [Undervisningsgruppe](Undervisningsgruppe.md), [Eksamensgruppe](Eksamensgruppe.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:skole |
| native | https://schema.fintlabs.no/utdanning/:skole |




## LinkML Source

<details>
```yaml
name: skole
alias: skole
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
range: string

```
</details>