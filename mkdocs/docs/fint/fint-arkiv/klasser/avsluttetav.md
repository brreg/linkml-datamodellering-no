

# Slot: avsluttetAv 


_Person som avslutta/lukka arkivenheten._





URI: [ark:avsluttetAv](https://schema.fintlabs.no/arkiv/avsluttetAv)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |  yes  |
| [Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [Sak](sak.md) | Generisk saksmappe (konkret Sak i Noark) |  no  |
| [Personalmappe](personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  no  |
| [TilskuddFartoy](tilskuddfartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arkivressurs](arkivressurs.md) |
| Domain Of | [Mappe](mappe.md) |
| Slot URI | [ark:avsluttetAv](https://schema.fintlabs.no/arkiv/avsluttetAv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:avsluttetAv |
| native | https://schema.fintlabs.no/arkiv/:avsluttetAv |




## LinkML Source

<details>
```yaml
name: avsluttetAv
description: Person som avslutta/lukka arkivenheten.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:avsluttetAv
domain_of:
- Mappe
range: Arkivressurs

```
</details>