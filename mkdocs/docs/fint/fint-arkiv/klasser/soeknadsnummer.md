

# Slot: soeknadsnummer 


_Søknadsnummer frå Digisak._





URI: [ark:soeknadsnummer](https://schema.fintlabs.no/arkiv/soeknadsnummer)
Alias: soeknadsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TilskuddFartoy](tilskuddfartoy.md) | Sak om søknad om tilskudd til freda fartøy |  yes  |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  yes  |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md), [TilskuddFartoy](tilskuddfartoy.md), [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) |
| Slot URI | [ark:soeknadsnummer](https://schema.fintlabs.no/arkiv/soeknadsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:soeknadsnummer |
| native | https://schema.fintlabs.no/arkiv/:soeknadsnummer |




## LinkML Source

<details>
```yaml
name: soeknadsnummer
description: Søknadsnummer frå Digisak.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:soeknadsnummer
alias: soeknadsnummer
domain_of:
- DispensasjonAutomatiskFredaKulturminne
- TilskuddFartoy
- TilskuddFredaBygningPrivatEie
range: Identifikator
inlined: true

```
</details>