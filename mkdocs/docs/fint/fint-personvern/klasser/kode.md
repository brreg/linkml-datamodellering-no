

# Slot: kode 



URI: [https://schema.fintlabs.no/personvern/:kode](https://schema.fintlabs.no/personvern/:kode)
Alias: kode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Personopplysning](personopplysning.md) | Opplysningar og vurderingar som kan knytast til enkeltpersonar |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Behandlingsgrunnlag](behandlingsgrunnlag.md) | Rettsleg grunnlag for behandling av personopplysningar |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Behandlingsgrunnlag](behandlingsgrunnlag.md), [Personopplysning](personopplysning.md), [Begrep](begrep.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/personvern/:kode |
| native | https://schema.fintlabs.no/personvern/:kode |




## LinkML Source

<details>
```yaml
name: kode
alias: kode
domain_of:
- Behandlingsgrunnlag
- Personopplysning
- Begrep
range: string

```
</details>