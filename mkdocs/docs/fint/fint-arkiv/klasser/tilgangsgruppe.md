

# Slot: tilgangsgruppe 


_Tilgangsgruppe som har tilgang til arkivenheten._





URI: [ark:tilgangsgruppe](https://schema.fintlabs.no/arkiv/tilgangsgruppe)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  yes  |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  yes  |
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
| Range | [Tilgangsgruppe](tilgangsgruppe.md) |
| Domain Of | [Saksmappe](saksmappe.md), [Registrering](registrering.md) |
| Slot URI | [ark:tilgangsgruppe](https://schema.fintlabs.no/arkiv/tilgangsgruppe) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:tilgangsgruppe |
| native | https://schema.fintlabs.no/arkiv/:tilgangsgruppe |




## LinkML Source

<details>
```yaml
name: tilgangsgruppe
description: Tilgangsgruppe som har tilgang til arkivenheten.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:tilgangsgruppe
domain_of:
- Saksmappe
- Registrering
range: Tilgangsgruppe

```
</details>