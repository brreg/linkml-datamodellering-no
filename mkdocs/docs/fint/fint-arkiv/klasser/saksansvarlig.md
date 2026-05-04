

# Slot: saksansvarlig 


_Person som er saksansvarleg._





URI: [ark:saksansvarlig](https://schema.fintlabs.no/arkiv/saksansvarlig)
Alias: saksansvarlig

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TilskuddFredaBygningPrivatEie](TilskuddFredaBygningPrivatEie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |
| [TilskuddFartoy](TilskuddFartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |
| [Sak](Sak.md) | Generisk saksmappe (konkret Sak i Noark) |  no  |
| [SoeknadDrosjeloeyve](SoeknadDrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [Saksmappe](Saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [DispensasjonAutomatiskFredaKulturminne](DispensasjonAutomatiskFredaKulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  no  |
| [Personalmappe](Personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arkivressurs](Arkivressurs.md) |
| Domain Of | [Saksmappe](Saksmappe.md) |
| Slot URI | [ark:saksansvarlig](https://schema.fintlabs.no/arkiv/saksansvarlig) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Saksmappe](Saksmappe.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




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
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:saksansvarlig
alias: saksansvarlig
owner: Saksmappe
domain_of:
- Saksmappe
range: Arkivressurs
required: true

```
</details>