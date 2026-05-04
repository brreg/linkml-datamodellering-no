

# Slot: navn 



URI: [https://schema.fintlabs.no/personvern/:navn](https://schema.fintlabs.no/personvern/:navn)
Alias: navn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjeneste](Tjeneste.md) | Teneste eller system som behandlar personopplysningar |  no  |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Person](Person.md) | Fysiske private personar |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Valuta](Valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Personopplysning](Personopplysning.md) | Opplysningar og vurderingar som kan knytast til enkeltpersonar |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Behandlingsgrunnlag](Behandlingsgrunnlag.md) | Rettsleg grunnlag for behandling av personopplysningar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Tjeneste](Tjeneste.md), [Behandlingsgrunnlag](Behandlingsgrunnlag.md), [Personopplysning](Personopplysning.md), [Begrep](Begrep.md), [Valuta](Valuta.md), [Person](Person.md), [Kontaktperson](Kontaktperson.md) |

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