

# Slot: tittel 


_Tittel eller namn på arkivenheten._





URI: [ark:tittel](https://schema.fintlabs.no/arkiv/tittel)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |  yes  |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  yes  |
| [Arkivdel](arkivdel.md) | Ein vilkårleg definert del av eit arkiv |  yes  |
| [Klassifikasjonssystem](klassifikasjonssystem.md) | Overordna struktur for mappene i ein eller fleire arkivdelar |  yes  |
| [Tilgang](tilgang.md) | Styring av kven som har tilgang til kva opplysningar |  yes  |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  yes  |
| [Klasse](klasse.md) | Ein klasse i eit klassifikasjonssystem |  yes  |
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
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Mappe](mappe.md), [Registrering](registrering.md), [Arkivdel](arkivdel.md), [Klassifikasjonssystem](klassifikasjonssystem.md), [Tilgang](tilgang.md), [Dokumentbeskrivelse](dokumentbeskrivelse.md), [Klasse](klasse.md) |
| Slot URI | [ark:tittel](https://schema.fintlabs.no/arkiv/tittel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:tittel |
| native | https://schema.fintlabs.no/arkiv/:tittel |




## LinkML Source

<details>
```yaml
name: tittel
description: Tittel eller namn på arkivenheten.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:tittel
domain_of:
- Mappe
- Registrering
- Arkivdel
- Klassifikasjonssystem
- Tilgang
- Dokumentbeskrivelse
- Klasse
range: string

```
</details>