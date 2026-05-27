

# Slot: kulturminneId 


_Kulturminnets ID i Askeladden._





URI: [ark:kulturminneId](https://schema.fintlabs.no/arkiv/kulturminneId)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  yes  |
| [TilskuddFartoy](tilskuddfartoy.md) | Sak om søknad om tilskudd til freda fartøy |  yes  |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md), [TilskuddFartoy](tilskuddfartoy.md), [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) |
| Slot URI | [ark:kulturminneId](https://schema.fintlabs.no/arkiv/kulturminneId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:kulturminneId |
| native | https://schema.fintlabs.no/arkiv/:kulturminneId |




## LinkML Source

<details>
```yaml
name: kulturminneId
description: Kulturminnets ID i Askeladden.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:kulturminneId
domain_of:
- DispensasjonAutomatiskFredaKulturminne
- TilskuddFartoy
- TilskuddFredaBygningPrivatEie
range: string

```
</details>