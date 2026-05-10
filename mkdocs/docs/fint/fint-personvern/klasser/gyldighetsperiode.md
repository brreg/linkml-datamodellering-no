

# Slot: gyldighetsperiode 


_Periode ressursen er gyldig for._





URI: [fint:gyldighetsperiode](https://schema.fintlabs.no/gyldighetsperiode)
Alias: gyldighetsperiode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  yes  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Personopplysning](personopplysning.md) | Opplysningar og vurderingar som kan knytast til enkeltpersonar |  yes  |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |  no  |
| [Samtykke](samtykke.md) | Tillating til behandling av personopplysning |  yes  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Behandlingsgrunnlag](behandlingsgrunnlag.md) | Rettsleg grunnlag for behandling av personopplysningar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Periode](periode.md) |
| Domain Of | [Begrep](begrep.md), [Identifikator](identifikator.md), [Samtykke](samtykke.md), [Behandlingsgrunnlag](behandlingsgrunnlag.md), [Personopplysning](personopplysning.md) |
| Slot URI | [fint:gyldighetsperiode](https://schema.fintlabs.no/gyldighetsperiode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:gyldighetsperiode |
| native | https://schema.fintlabs.no/:gyldighetsperiode |




## LinkML Source

<details>
```yaml
name: gyldighetsperiode
description: Periode ressursen er gyldig for.
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:gyldighetsperiode
alias: gyldighetsperiode
domain_of:
- Begrep
- Identifikator
- Samtykke
- Behandlingsgrunnlag
- Personopplysning
range: Periode
inlined: true

```
</details>