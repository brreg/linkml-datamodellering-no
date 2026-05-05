

# Slot: undervisningsforhold 



URI: [https://schema.fintlabs.no/utdanning/:undervisningsforhold](https://schema.fintlabs.no/utdanning/:undervisningsforhold)
Alias: undervisningsforhold

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |
| [Time](time.md) | Ein time i timeplanen |  no  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Klasse](klasse.md), [Kontaktlaerergruppe](kontaktlaerergruppe.md), [Persongruppe](persongruppe.md), [Time](time.md), [Undervisningsgruppe](undervisningsgruppe.md), [Eksamensgruppe](eksamensgruppe.md) |

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