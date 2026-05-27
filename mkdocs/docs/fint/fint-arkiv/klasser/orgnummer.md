

# Slot: orgnummer 


_Organisasjonsnummer._





URI: [ark:organisasjonsnummer](https://schema.fintlabs.no/arkiv/organisasjonsnummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  yes  |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  yes  |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  yes  |






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


* from schema: https://data.norge.no/fint/fint-arkiv




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
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:organisasjonsnummer
domain_of:
- SoeknadDrosjeloeyve
- Korrespondansepart
- Part
range: string

```
</details>