

# Slot: beskrivelse 



URI: [https://schema.fintlabs.no/utdanning/:beskrivelse](https://schema.fintlabs.no/utdanning/:beskrivelse)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  no  |
| [Gruppe](gruppe.md) | Abstrakt basisklasse for alle gruppetypar i utdanning |  no  |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |  no  |
| [Fag](fag.md) | Eit skulefag |  no  |
| [Eksamen](eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  no  |
| [Time](time.md) | Ein time i timeplanen |  no  |
| [Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |  no  |
| [Faggruppe](faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  no  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [OtStatus](otstatus.md) | Status for ein ungdom i oppfølgingstenesta |  no  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |
| [Utdanningsforhold](utdanningsforhold.md) | Abstrakt basisklasse for undervisningsforhold i utdanning |  no  |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  no  |
| [Programomrade](programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Gruppe](gruppe.md), [Utdanningsforhold](utdanningsforhold.md), [Elevforhold](elevforhold.md), [Eksamen](eksamen.md), [Time](time.md), [OtStatus](otstatus.md), [Periode](periode.md) |

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