

# Slot: skole 



URI: [https://schema.fintlabs.no/utdanning/:skole](https://schema.fintlabs.no/utdanning/:skole)
Alias: skole

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |  no  |
| [Fag](fag.md) | Eit skulefag |  no  |
| [Faggruppe](faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  no  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [Skoleressurs](skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |  no  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Elevforhold](elevforhold.md), [Klasse](klasse.md), [Kontaktlaerergruppe](kontaktlaerergruppe.md), [Persongruppe](persongruppe.md), [Skoleressurs](skoleressurs.md), [Utdanningsprogram](utdanningsprogram.md), [Fag](fag.md), [Faggruppe](faggruppe.md), [Undervisningsgruppe](undervisningsgruppe.md), [Eksamensgruppe](eksamensgruppe.md) |

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