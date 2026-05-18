

# Slot: matrikkelnummer 


_Kulturminnets/bygningens identifikator i Matrikkelen._





URI: [ark:matrikkelnummer](https://schema.fintlabs.no/arkiv/matrikkelnummer)
Alias: matrikkelnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  yes  |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Matrikkelnummer](matrikkelnummer.md) |
| Domain Of | [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md), [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) |
| Slot URI | [ark:matrikkelnummer](https://schema.fintlabs.no/arkiv/matrikkelnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:matrikkelnummer |
| native | https://schema.fintlabs.no/arkiv/:matrikkelnummer |




## LinkML Source

<details>
```yaml
name: matrikkelnummer
description: Kulturminnets/bygningens identifikator i Matrikkelen.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:matrikkelnummer
alias: matrikkelnummer
domain_of:
- DispensasjonAutomatiskFredaKulturminne
- TilskuddFredaBygningPrivatEie
range: Matrikkelnummer
inlined: true

```
</details>