

# Slot: avsluttetDato 


_Dato og klokkeslett når arkivenheten vart avslutta/lukka._





URI: [ark:avsluttetDato](https://schema.fintlabs.no/arkiv/avsluttetDato)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |  yes  |
| [Klassifikasjonssystem](klassifikasjonssystem.md) | Overordna struktur for mappene i ein eller fleire arkivdelar |  yes  |
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
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Mappe](mappe.md), [Klassifikasjonssystem](klassifikasjonssystem.md) |
| Slot URI | [ark:avsluttetDato](https://schema.fintlabs.no/arkiv/avsluttetDato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:avsluttetDato |
| native | https://schema.fintlabs.no/arkiv/:avsluttetDato |




## LinkML Source

<details>
```yaml
name: avsluttetDato
description: Dato og klokkeslett når arkivenheten vart avslutta/lukka.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:avsluttetDato
domain_of:
- Mappe
- Klassifikasjonssystem
range: datetime

```
</details>