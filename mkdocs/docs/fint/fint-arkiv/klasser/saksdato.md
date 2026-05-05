

# Slot: saksdato 


_Datoen saka er oppretta._





URI: [ark:saksdato](https://schema.fintlabs.no/arkiv/saksdato)
Alias: saksdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  no  |
| [Sak](sak.md) | Generisk saksmappe (konkret Sak i Noark) |  no  |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [TilskuddFartoy](tilskuddfartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |
| [Personalmappe](personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](datetime.md) |
| Domain Of | [Saksmappe](saksmappe.md) |
| Slot URI | [ark:saksdato](https://schema.fintlabs.no/arkiv/saksdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Saksmappe](saksmappe.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:saksdato |
| native | https://schema.fintlabs.no/arkiv/:saksdato |




## LinkML Source

<details>
```yaml
name: saksdato
description: Datoen saka er oppretta.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:saksdato
alias: saksdato
owner: Saksmappe
domain_of:
- Saksmappe
range: datetime

```
</details>