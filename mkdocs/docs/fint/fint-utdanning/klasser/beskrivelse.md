

# Slot: beskrivelse 



URI: [https://schema.fintlabs.no/utdanning/:beskrivelse](https://schema.fintlabs.no/utdanning/:beskrivelse)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppe](Eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [Persongruppe](Persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Klasse](Klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |
| [Utdanningsprogram](Utdanningsprogram.md) | Eit utdanningsprogram (t |  no  |
| [Gruppe](Gruppe.md) | Abstrakt basisklasse for alle gruppetypar i utdanning |  no  |
| [Fag](Fag.md) | Eit skulefag |  no  |
| [Arstrinn](Arstrinn.md) | Eit årstrinn i skulen (t |  no  |
| [Periode](Periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  no  |
| [Utdanningsforhold](Utdanningsforhold.md) | Abstrakt basisklasse for undervisningsforhold i utdanning |  no  |
| [Kontaktlaerergruppe](Kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Undervisningsgruppe](Undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [Eksamen](Eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  no  |
| [Faggruppe](Faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  no  |
| [Time](Time.md) | Ein time i timeplanen |  no  |
| [OtStatus](OtStatus.md) | Status for ein ungdom i oppfølgingstenesta |  no  |
| [Programomrade](Programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  no  |
| [Elevforhold](Elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |
| [Undervisningsforhold](Undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Gruppe](Gruppe.md), [Utdanningsforhold](Utdanningsforhold.md), [Elevforhold](Elevforhold.md), [Eksamen](Eksamen.md), [Time](Time.md), [OtStatus](OtStatus.md), [Periode](Periode.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:beskrivelse |
| native | https://schema.fintlabs.no/utdanning/:beskrivelse |




## LinkML Source

<details>
```yaml
name: beskrivelse
alias: beskrivelse
domain_of:
- Gruppe
- Utdanningsforhold
- Elevforhold
- Eksamen
- Time
- OtStatus
- Periode
range: string

```
</details>