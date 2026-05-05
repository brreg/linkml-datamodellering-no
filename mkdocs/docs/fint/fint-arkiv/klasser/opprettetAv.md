

# Slot: opprettetAv 



URI: [https://schema.fintlabs.no/arkiv/:opprettetAv](https://schema.fintlabs.no/arkiv/:opprettetAv)
Alias: opprettetAv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalmappe](personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  no  |
| [Sak](sak.md) | Generisk saksmappe (konkret Sak i Noark) |  no  |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  no  |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [TilskuddFartoy](tilskuddfartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |
| [Klassifikasjonssystem](klassifikasjonssystem.md) | Overordna struktur for mappene i ein eller fleire arkivdelar |  no  |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  no  |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |
| [Dokumentobjekt](dokumentobjekt.md) | Referanse til éin og berre éin dokumentfil |  no  |
| [Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Mappe](mappe.md), [Registrering](registrering.md), [Klassifikasjonssystem](klassifikasjonssystem.md), [Dokumentbeskrivelse](dokumentbeskrivelse.md), [Dokumentobjekt](dokumentobjekt.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:opprettetAv |
| native | https://schema.fintlabs.no/arkiv/:opprettetAv |




## LinkML Source

<details>
```yaml
name: opprettetAv
alias: opprettetAv
domain_of:
- Mappe
- Registrering
- Klassifikasjonssystem
- Dokumentbeskrivelse
- Dokumentobjekt
range: string

```
</details>