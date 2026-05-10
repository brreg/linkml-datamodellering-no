

# Slot: orgnummer 


_Organisasjonsnummer._





URI: [ark:organisasjonsnummer](https://schema.fintlabs.no/arkiv/organisasjonsnummer)
Alias: orgnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  yes  |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  yes  |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md), [Korrespondansepart](korrespondansepart.md), [Part](part.md) |
| Slot URI | [ark:organisasjonsnummer](https://schema.fintlabs.no/arkiv/organisasjonsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:organisasjonsnummer |
| native | https://schema.fintlabs.no/arkiv/:orgnummer |




## LinkML Source

<details>
```yaml
name: orgnummer
description: Organisasjonsnummer.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:organisasjonsnummer
alias: orgnummer
domain_of:
- SoeknadDrosjeloeyve
- Korrespondansepart
- Part
range: string

```
</details>