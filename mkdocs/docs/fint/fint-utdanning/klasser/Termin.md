

# Slot: termin 



URI: [https://schema.fintlabs.no/utdanning/:termin](https://schema.fintlabs.no/utdanning/:termin)
Alias: termin

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Klasse](klasse.md), [Kontaktlaerergruppe](kontaktlaerergruppe.md), [Persongruppe](persongruppe.md), [Undervisningsgruppe](undervisningsgruppe.md), [Eksamensgruppe](eksamensgruppe.md) |

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