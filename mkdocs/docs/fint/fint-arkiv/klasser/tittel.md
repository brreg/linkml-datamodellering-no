

# Slot: tittel 



URI: [https://schema.fintlabs.no/arkiv/:tittel](https://schema.fintlabs.no/arkiv/:tittel)
Alias: tittel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalmappe](personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  no  |
| [Klasse](klasse.md) | Ein klasse i eit klassifikasjonssystem |  no  |
| [Sak](sak.md) | Generisk saksmappe (konkret Sak i Noark) |  no  |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  no  |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [TilskuddFartoy](tilskuddfartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |
| [Arkivdel](arkivdel.md) | Ein vilkårleg definert del av eit arkiv |  no  |
| [Klassifikasjonssystem](klassifikasjonssystem.md) | Overordna struktur for mappene i ein eller fleire arkivdelar |  no  |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  no  |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |
| [Tilgang](tilgang.md) | Styring av kven som har tilgang til kva opplysningar |  no  |
| [Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Mappe](mappe.md), [Registrering](registrering.md), [Arkivdel](arkivdel.md), [Klassifikasjonssystem](klassifikasjonssystem.md), [Tilgang](tilgang.md), [Dokumentbeskrivelse](dokumentbeskrivelse.md), [Klasse](klasse.md) |

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