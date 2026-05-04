

# Slot: arkivdel 



URI: [https://schema.fintlabs.no/arkiv/:arkivdel](https://schema.fintlabs.no/arkiv/:arkivdel)
Alias: arkivdel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TilskuddFredaBygningPrivatEie](TilskuddFredaBygningPrivatEie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |
| [Journalpost](Journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |
| [TilskuddFartoy](TilskuddFartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |
| [Registrering](Registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  no  |
| [Mappe](Mappe.md) | Abstrakt basisklasse for alle mappetypar |  no  |
| [Sak](Sak.md) | Generisk saksmappe (konkret Sak i Noark) |  no  |
| [SoeknadDrosjeloeyve](SoeknadDrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [Saksmappe](Saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [Personalmappe](Personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |
| [DispensasjonAutomatiskFredaKulturminne](DispensasjonAutomatiskFredaKulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  no  |
| [Klassifikasjonssystem](Klassifikasjonssystem.md) | Overordna struktur for mappene i ein eller fleire arkivdelar |  no  |
| [Tilgang](Tilgang.md) | Styring av kven som har tilgang til kva opplysningar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Mappe](Mappe.md), [Registrering](Registrering.md), [Klassifikasjonssystem](Klassifikasjonssystem.md), [Tilgang](Tilgang.md) |

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