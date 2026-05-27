

# Slot: saksaar 


_Inngår i M003 mappeID — viser året saksmappa vart oppretta._





URI: [ark:saksaar](https://schema.fintlabs.no/arkiv/saksaar)
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
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Saksmappe](saksmappe.md) |
| Slot URI | [ark:saksaar](https://schema.fintlabs.no/arkiv/saksaar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:saksaar |
| native | https://schema.fintlabs.no/arkiv/:saksaar |




## LinkML Source

<details>
```yaml
name: saksaar
description: Inngår i M003 mappeID — viser året saksmappa vart oppretta.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:saksaar
domain_of:
- Saksmappe
range: string

```
</details>