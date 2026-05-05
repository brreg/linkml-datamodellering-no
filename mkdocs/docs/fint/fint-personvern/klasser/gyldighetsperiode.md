

# Slot: gyldighetsperiode 



URI: [https://schema.fintlabs.no/personvern/:gyldighetsperiode](https://schema.fintlabs.no/personvern/:gyldighetsperiode)
Alias: gyldighetsperiode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Personopplysning](personopplysning.md) | Opplysningar og vurderingar som kan knytast til enkeltpersonar |  no  |
| [Samtykke](samtykke.md) | Tillating til behandling av personopplysning |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Behandlingsgrunnlag](behandlingsgrunnlag.md) | Rettsleg grunnlag for behandling av personopplysningar |  no  |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Samtykke](samtykke.md), [Behandlingsgrunnlag](behandlingsgrunnlag.md), [Personopplysning](personopplysning.md), [Begrep](begrep.md), [Identifikator](identifikator.md) |

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