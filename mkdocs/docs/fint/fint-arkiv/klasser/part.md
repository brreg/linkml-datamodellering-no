

# Slot: part 


_Partar til arkivenhet._





URI: [ark:part](https://schema.fintlabs.no/arkiv/part)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |  yes  |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  yes  |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  yes  |
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
| Range | [Part](part.md) |
| Domain Of | [Mappe](mappe.md), [Registrering](registrering.md), [Dokumentbeskrivelse](dokumentbeskrivelse.md) |
| Slot URI | [ark:part](https://schema.fintlabs.no/arkiv/part) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:part |
| native | https://schema.fintlabs.no/arkiv/:part |




## LinkML Source

<details>
```yaml
name: part
description: Partar til arkivenhet.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:part
domain_of:
- Mappe
- Registrering
- Dokumentbeskrivelse
range: Part
multivalued: true
inlined: true
inlined_as_list: true

```
</details>