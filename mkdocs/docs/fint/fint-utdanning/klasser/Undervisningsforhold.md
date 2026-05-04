

# Slot: undervisningsforhold 



URI: [https://schema.fintlabs.no/utdanning/:undervisningsforhold](https://schema.fintlabs.no/utdanning/:undervisningsforhold)
Alias: undervisningsforhold

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppe](Eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [Klasse](Klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |
| [Kontaktlaerergruppe](Kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Undervisningsgruppe](Undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |
| [Time](Time.md) | Ein time i timeplanen |  no  |
| [Persongruppe](Persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [UtdanningContainer](UtdanningContainer.md), [Klasse](Klasse.md), [Kontaktlaerergruppe](Kontaktlaerergruppe.md), [Persongruppe](Persongruppe.md), [Time](Time.md), [Undervisningsgruppe](Undervisningsgruppe.md), [Eksamensgruppe](Eksamensgruppe.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:undervisningsforhold |
| native | https://schema.fintlabs.no/utdanning/:undervisningsforhold |




## LinkML Source

<details>
```yaml
name: undervisningsforhold
alias: undervisningsforhold
domain_of:
- UtdanningContainer
- Klasse
- Kontaktlaerergruppe
- Persongruppe
- Time
- Undervisningsgruppe
- Eksamensgruppe
range: string

```
</details>