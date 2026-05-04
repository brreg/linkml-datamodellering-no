

# Slot: termin 



URI: [https://schema.fintlabs.no/utdanning/:termin](https://schema.fintlabs.no/utdanning/:termin)
Alias: termin

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppe](Eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [Klasse](Klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |
| [Kontaktlaerergruppe](Kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Undervisningsgruppe](Undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [Persongruppe](Persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Klasse](Klasse.md), [Kontaktlaerergruppe](Kontaktlaerergruppe.md), [Persongruppe](Persongruppe.md), [Undervisningsgruppe](Undervisningsgruppe.md), [Eksamensgruppe](Eksamensgruppe.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:termin |
| native | https://schema.fintlabs.no/utdanning/:termin |




## LinkML Source

<details>
```yaml
name: termin
alias: termin
domain_of:
- Klasse
- Kontaktlaerergruppe
- Persongruppe
- Undervisningsgruppe
- Eksamensgruppe
range: string

```
</details>