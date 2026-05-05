

# Slot: arkivdel 



URI: [https://schema.fintlabs.no/arkiv/:arkivdel](https://schema.fintlabs.no/arkiv/:arkivdel)
Alias: arkivdel

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
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |
| [Tilgang](tilgang.md) | Styring av kven som har tilgang til kva opplysningar |  no  |
| [Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Mappe](mappe.md), [Registrering](registrering.md), [Klassifikasjonssystem](klassifikasjonssystem.md), [Tilgang](tilgang.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:arkivdel |
| native | https://schema.fintlabs.no/arkiv/:arkivdel |




## LinkML Source

<details>
```yaml
name: arkivdel
alias: arkivdel
domain_of:
- Mappe
- Registrering
- Klassifikasjonssystem
- Tilgang
range: string

```
</details>