

# Slot: gyldighetsperiode 



URI: [https://schema.fintlabs.no/personvern/:gyldighetsperiode](https://schema.fintlabs.no/personvern/:gyldighetsperiode)
Alias: gyldighetsperiode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Identifikator](Identifikator.md) | Unik identifikasjon til eit objekt |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Personopplysning](Personopplysning.md) | Opplysningar og vurderingar som kan knytast til enkeltpersonar |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Samtykke](Samtykke.md) | Tillating til behandling av personopplysning |  no  |
| [Behandlingsgrunnlag](Behandlingsgrunnlag.md) | Rettsleg grunnlag for behandling av personopplysningar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Samtykke](Samtykke.md), [Behandlingsgrunnlag](Behandlingsgrunnlag.md), [Personopplysning](Personopplysning.md), [Begrep](Begrep.md), [Identifikator](Identifikator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/personvern/:gyldighetsperiode |
| native | https://schema.fintlabs.no/personvern/:gyldighetsperiode |




## LinkML Source

<details>
```yaml
name: gyldighetsperiode
alias: gyldighetsperiode
domain_of:
- Samtykke
- Behandlingsgrunnlag
- Personopplysning
- Begrep
- Identifikator
range: string

```
</details>