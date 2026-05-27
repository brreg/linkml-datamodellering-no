

# Slot: saksansvarlig 


_Person som er saksansvarleg._





URI: [ark:saksansvarlig](https://schema.fintlabs.no/arkiv/saksansvarlig)
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
| Range | [Arkivressurs](arkivressurs.md) |
| Domain Of | [Saksmappe](saksmappe.md) |
| Slot URI | [ark:saksansvarlig](https://schema.fintlabs.no/arkiv/saksansvarlig) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:saksansvarlig |
| native | https://schema.fintlabs.no/arkiv/:saksansvarlig |




## LinkML Source

<details>
```yaml
name: saksansvarlig
description: Person som er saksansvarleg.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:saksansvarlig
domain_of:
- Saksmappe
range: Arkivressurs

```
</details>