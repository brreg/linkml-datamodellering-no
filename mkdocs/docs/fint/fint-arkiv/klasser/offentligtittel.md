

# Slot: offentligTittel 


_Offentleg tittel der skjerma ord er fjerna._





URI: [ark:offentligTittel](https://schema.fintlabs.no/arkiv/offentligTittel)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |  yes  |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  yes  |
| [Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
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
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Mappe](mappe.md), [Registrering](registrering.md) |
| Slot URI | [ark:offentligTittel](https://schema.fintlabs.no/arkiv/offentligTittel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:offentligTittel |
| native | https://schema.fintlabs.no/arkiv/:offentligTittel |




## LinkML Source

<details>
```yaml
name: offentligTittel
description: Offentleg tittel der skjerma ord er fjerna.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:offentligTittel
domain_of:
- Mappe
- Registrering
range: string

```
</details>