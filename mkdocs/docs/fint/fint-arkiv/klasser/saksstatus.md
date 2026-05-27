

# Slot: saksstatus 


_Status til saksmappa._





URI: [ark:saksstatus](https://schema.fintlabs.no/arkiv/saksstatus)
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
| Range | [Saksstatus](saksstatus.md) |
| Domain Of | [Saksmappe](saksmappe.md) |
| Slot URI | [ark:saksstatus](https://schema.fintlabs.no/arkiv/saksstatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:saksstatus |
| native | https://schema.fintlabs.no/arkiv/:saksstatus |




## LinkML Source

<details>
```yaml
name: saksstatus
description: Status til saksmappa.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:saksstatus
domain_of:
- Saksmappe
range: Saksstatus

```
</details>