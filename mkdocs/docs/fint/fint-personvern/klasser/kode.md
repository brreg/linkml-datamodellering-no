

# Slot: kode 



URI: [https://schema.fintlabs.no/personvern/:kode](https://schema.fintlabs.no/personvern/:kode)
Alias: kode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Personopplysning](Personopplysning.md) | Opplysningar og vurderingar som kan knytast til enkeltpersonar |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Behandlingsgrunnlag](Behandlingsgrunnlag.md) | Rettsleg grunnlag for behandling av personopplysningar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Behandlingsgrunnlag](Behandlingsgrunnlag.md), [Personopplysning](Personopplysning.md), [Begrep](Begrep.md) |

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