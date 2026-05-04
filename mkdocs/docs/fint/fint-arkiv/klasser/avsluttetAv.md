

# Slot: avsluttetAv 



URI: [https://schema.fintlabs.no/arkiv/:avsluttetAv](https://schema.fintlabs.no/arkiv/:avsluttetAv)
Alias: avsluttetAv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TilskuddFredaBygningPrivatEie](TilskuddFredaBygningPrivatEie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |
| [TilskuddFartoy](TilskuddFartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |
| [Sak](Sak.md) | Generisk saksmappe (konkret Sak i Noark) |  no  |
| [Mappe](Mappe.md) | Abstrakt basisklasse for alle mappetypar |  no  |
| [SoeknadDrosjeloeyve](SoeknadDrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [Saksmappe](Saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [Personalmappe](Personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |
| [DispensasjonAutomatiskFredaKulturminne](DispensasjonAutomatiskFredaKulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  no  |
| [Klassifikasjonssystem](Klassifikasjonssystem.md) | Overordna struktur for mappene i ein eller fleire arkivdelar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Mappe](Mappe.md), [Klassifikasjonssystem](Klassifikasjonssystem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:avsluttetAv |
| native | https://schema.fintlabs.no/arkiv/:avsluttetAv |




## LinkML Source

<details>
```yaml
name: avsluttetAv
alias: avsluttetAv
domain_of:
- Mappe
- Klassifikasjonssystem
range: string

```
</details>