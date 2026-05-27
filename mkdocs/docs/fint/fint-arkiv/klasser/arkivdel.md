

# Slot: arkivdel 


_Arkivdel arkivenheten tilhøyrer._





URI: [ark:arkivdel](https://schema.fintlabs.no/arkiv/arkivdel)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |  yes  |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  yes  |
| [Klassifikasjonssystem](klassifikasjonssystem.md) | Overordna struktur for mappene i ein eller fleire arkivdelar |  yes  |
| [Tilgang](tilgang.md) | Styring av kven som har tilgang til kva opplysningar |  yes  |
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
| Range | [Arkivdel](arkivdel.md) |
| Domain Of | [Mappe](mappe.md), [Registrering](registrering.md), [Klassifikasjonssystem](klassifikasjonssystem.md), [Tilgang](tilgang.md) |
| Slot URI | [ark:arkivdel](https://schema.fintlabs.no/arkiv/arkivdel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:arkivdel |
| native | https://schema.fintlabs.no/arkiv/:arkivdel |




## LinkML Source

<details>
```yaml
name: arkivdel
description: Arkivdel arkivenheten tilhøyrer.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:arkivdel
domain_of:
- Mappe
- Registrering
- Klassifikasjonssystem
- Tilgang
range: Arkivdel

```
</details>