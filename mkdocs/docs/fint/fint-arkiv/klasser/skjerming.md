

# Slot: skjerming 


_Skjerming av arkivenhet._





URI: [ark:skjerming](https://schema.fintlabs.no/arkiv/skjerming)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |  yes  |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  yes  |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  yes  |
| [Klasse](klasse.md) | Ein klasse i eit klassifikasjonssystem |  yes  |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  yes  |
| [Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |
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
| Range | [Skjerming](skjerming.md) |
| Domain Of | [Mappe](mappe.md), [Registrering](registrering.md), [Dokumentbeskrivelse](dokumentbeskrivelse.md), [Klasse](klasse.md), [Korrespondansepart](korrespondansepart.md) |
| Slot URI | [ark:skjerming](https://schema.fintlabs.no/arkiv/skjerming) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:skjerming |
| native | https://schema.fintlabs.no/arkiv/:skjerming |




## LinkML Source

<details>
```yaml
name: skjerming
description: Skjerming av arkivenhet.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:skjerming
domain_of:
- Mappe
- Registrering
- Dokumentbeskrivelse
- Klasse
- Korrespondansepart
range: Skjerming
inlined: true

```
</details>