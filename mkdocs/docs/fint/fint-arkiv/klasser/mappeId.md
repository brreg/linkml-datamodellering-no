

# Slot: mappeId 


_Eintydig identifikasjon av mappa innanfor arkivet._





URI: [ark:mappeId](https://schema.fintlabs.no/arkiv/mappeId)
Alias: mappeId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalmappe](personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  no  |
| [Sak](sak.md) | Generisk saksmappe (konkret Sak i Noark) |  no  |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |  yes  |
| [TilskuddFartoy](tilskuddfartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Mappe](mappe.md) |
| Slot URI | [ark:mappeId](https://schema.fintlabs.no/arkiv/mappeId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:mappeId |
| native | https://schema.fintlabs.no/arkiv/:mappeId |




## LinkML Source

<details>
```yaml
name: mappeId
description: Eintydig identifikasjon av mappa innanfor arkivet.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:mappeId
alias: mappeId
domain_of:
- Mappe
range: Identifikator
inlined: true

```
</details>