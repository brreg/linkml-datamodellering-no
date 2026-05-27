

# Slot: sakssekvensnummer 


_Inngår i M003 mappeID — viser rekkjefølgja saksmappene vart oppretta._





URI: [ark:sakssekvensnummer](https://schema.fintlabs.no/arkiv/sakssekvensnummer)
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
| Slot URI | [ark:sakssekvensnummer](https://schema.fintlabs.no/arkiv/sakssekvensnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:sakssekvensnummer |
| native | https://schema.fintlabs.no/arkiv/:sakssekvensnummer |




## LinkML Source

<details>
```yaml
name: sakssekvensnummer
description: Inngår i M003 mappeID — viser rekkjefølgja saksmappene vart oppretta.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:sakssekvensnummer
domain_of:
- Saksmappe
range: string

```
</details>