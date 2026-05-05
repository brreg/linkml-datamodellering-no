

# Slot: navn 



URI: [https://schema.fintlabs.no/personvern/:navn](https://schema.fintlabs.no/personvern/:navn)
Alias: navn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Personopplysning](personopplysning.md) | Opplysningar og vurderingar som kan knytast til enkeltpersonar |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Behandlingsgrunnlag](behandlingsgrunnlag.md) | Rettsleg grunnlag for behandling av personopplysningar |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Tjeneste](tjeneste.md) | Teneste eller system som behandlar personopplysningar |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Tjeneste](tjeneste.md), [Behandlingsgrunnlag](behandlingsgrunnlag.md), [Personopplysning](personopplysning.md), [Begrep](begrep.md), [Valuta](valuta.md), [Person](person.md), [Kontaktperson](kontaktperson.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/personvern/:navn |
| native | https://schema.fintlabs.no/personvern/:navn |




## LinkML Source

<details>
```yaml
name: navn
alias: navn
domain_of:
- Tjeneste
- Behandlingsgrunnlag
- Personopplysning
- Begrep
- Valuta
- Person
- Kontaktperson
range: string

```
</details>