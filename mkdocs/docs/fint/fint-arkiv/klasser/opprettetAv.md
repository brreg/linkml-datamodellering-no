

# Slot: opprettetAv 


_Person som oppretta/registrerte arkivenheten._





URI: [ark:opprettetAv](https://schema.fintlabs.no/arkiv/opprettetAv)
Alias: opprettetAv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalmappe](personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  yes  |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  no  |
| [Sak](sak.md) | Generisk saksmappe (konkret Sak i Noark) |  no  |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |  yes  |
| [Dokumentobjekt](dokumentobjekt.md) | Referanse til éin og berre éin dokumentfil |  yes  |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  yes  |
| [TilskuddFartoy](tilskuddfartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arkivressurs](arkivressurs.md) |
| Domain Of | [Mappe](mappe.md), [Registrering](registrering.md), [Dokumentbeskrivelse](dokumentbeskrivelse.md), [Dokumentobjekt](dokumentobjekt.md) |
| Slot URI | [ark:opprettetAv](https://schema.fintlabs.no/arkiv/opprettetAv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:opprettetAv |
| native | https://schema.fintlabs.no/arkiv/:opprettetAv |




## LinkML Source

<details>
```yaml
name: opprettetAv
description: Person som oppretta/registrerte arkivenheten.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:opprettetAv
alias: opprettetAv
domain_of:
- Mappe
- Registrering
- Dokumentbeskrivelse
- Dokumentobjekt
range: Arkivressurs

```
</details>