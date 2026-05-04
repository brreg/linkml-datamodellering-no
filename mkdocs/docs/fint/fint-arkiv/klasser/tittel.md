

# Slot: tittel 



URI: [https://schema.fintlabs.no/arkiv/:tittel](https://schema.fintlabs.no/arkiv/:tittel)
Alias: tittel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TilskuddFredaBygningPrivatEie](TilskuddFredaBygningPrivatEie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |
| [Journalpost](Journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |
| [Dokumentbeskrivelse](Dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  no  |
| [TilskuddFartoy](TilskuddFartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |
| [Registrering](Registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  no  |
| [Mappe](Mappe.md) | Abstrakt basisklasse for alle mappetypar |  no  |
| [Sak](Sak.md) | Generisk saksmappe (konkret Sak i Noark) |  no  |
| [SoeknadDrosjeloeyve](SoeknadDrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [Saksmappe](Saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [Personalmappe](Personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |
| [DispensasjonAutomatiskFredaKulturminne](DispensasjonAutomatiskFredaKulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  no  |
| [Klassifikasjonssystem](Klassifikasjonssystem.md) | Overordna struktur for mappene i ein eller fleire arkivdelar |  no  |
| [Klasse](Klasse.md) | Ein klasse i eit klassifikasjonssystem |  no  |
| [Arkivdel](Arkivdel.md) | Ein vilkårleg definert del av eit arkiv |  no  |
| [Tilgang](Tilgang.md) | Styring av kven som har tilgang til kva opplysningar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Mappe](Mappe.md), [Registrering](Registrering.md), [Arkivdel](Arkivdel.md), [Klassifikasjonssystem](Klassifikasjonssystem.md), [Tilgang](Tilgang.md), [Dokumentbeskrivelse](Dokumentbeskrivelse.md), [Klasse](Klasse.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:tittel |
| native | https://schema.fintlabs.no/arkiv/:tittel |




## LinkML Source

<details>
```yaml
name: tittel
alias: tittel
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