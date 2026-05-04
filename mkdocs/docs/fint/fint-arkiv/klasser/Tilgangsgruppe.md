

# Slot: tilgangsgruppe 



URI: [https://schema.fintlabs.no/arkiv/:tilgangsgruppe](https://schema.fintlabs.no/arkiv/:tilgangsgruppe)
Alias: tilgangsgruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TilskuddFredaBygningPrivatEie](TilskuddFredaBygningPrivatEie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |
| [Journalpost](Journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |
| [TilskuddFartoy](TilskuddFartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |
| [Registrering](Registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  no  |
| [Sak](Sak.md) | Generisk saksmappe (konkret Sak i Noark) |  no  |
| [SoeknadDrosjeloeyve](SoeknadDrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [Saksmappe](Saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [Personalmappe](Personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |
| [DispensasjonAutomatiskFredaKulturminne](DispensasjonAutomatiskFredaKulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Saksmappe](Saksmappe.md), [Registrering](Registrering.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:tilgangsgruppe |
| native | https://schema.fintlabs.no/arkiv/:tilgangsgruppe |




## LinkML Source

<details>
```yaml
name: tilgangsgruppe
alias: tilgangsgruppe
domain_of:
- Saksmappe
- Registrering
range: string

```
</details>