

# Slot: beskrivelse 


_Beskriven namn eller omtale._





URI: [fint:beskrivelse](https://schema.fintlabs.no/beskrivelse)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  no  |
| [Gruppe](gruppe.md) | Abstrakt basisklasse for alle gruppetypar i utdanning |  yes  |
| [Utdanningsforhold](utdanningsforhold.md) | Abstrakt basisklasse for undervisningsforhold i utdanning |  yes  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |
| [Eksamen](eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  yes  |
| [Time](time.md) | Ein time i timeplanen |  yes  |
| [OtStatus](otstatus.md) | Status for ein ungdom i oppfølgingstenesta |  yes  |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |  no  |
| [Programomrade](programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  no  |
| [Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |  no  |
| [Fag](fag.md) | Eit skulefag |  no  |
| [Faggruppe](faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  no  |
| [Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |  no  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Periode](periode.md), [Gruppe](gruppe.md), [Utdanningsforhold](utdanningsforhold.md), [Elevforhold](elevforhold.md), [Eksamen](eksamen.md), [Time](time.md), [OtStatus](otstatus.md) |
| Slot URI | [fint:beskrivelse](https://schema.fintlabs.no/beskrivelse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:beskrivelse |
| native | https://schema.fintlabs.no/:beskrivelse |




## LinkML Source

<details>
```yaml
name: beskrivelse
description: Beskriven namn eller omtale.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:beskrivelse
domain_of:
- Periode
- Gruppe
- Utdanningsforhold
- Elevforhold
- Eksamen
- Time
- OtStatus
range: string

```
</details>