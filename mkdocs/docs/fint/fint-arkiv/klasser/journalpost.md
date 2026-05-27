

# Slot: journalpost 


_Journalpostar knytt til saksmappa._





URI: [ark:journalpost](https://schema.fintlabs.no/arkiv/journalpost)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  yes  |
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
| Range | [Journalpost](journalpost.md) |
| Domain Of | [Saksmappe](saksmappe.md) |
| Slot URI | [ark:journalpost](https://schema.fintlabs.no/arkiv/journalpost) |

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
| self | ark:journalpost |
| native | https://schema.fintlabs.no/arkiv/:journalpost |




## LinkML Source

<details>
```yaml
name: journalpost
description: Journalpostar knytt til saksmappa.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:journalpost
domain_of:
- Saksmappe
range: Journalpost
multivalued: true

```
</details>