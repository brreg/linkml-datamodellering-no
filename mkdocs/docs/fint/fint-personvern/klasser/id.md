

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://schema.fintlabs.no/personvern/:id](https://schema.fintlabs.no/personvern/:id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Personopplysning](personopplysning.md) | Opplysningar og vurderingar som kan knytast til enkeltpersonar |  no  |
| [Samtykke](samtykke.md) | Tillating til behandling av personopplysning |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Behandlingsgrunnlag](behandlingsgrunnlag.md) | Rettsleg grunnlag for behandling av personopplysningar |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Tjeneste](tjeneste.md) | Teneste eller system som behandlar personopplysningar |  no  |
| [Behandling](behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Behandling](behandling.md), [Samtykke](samtykke.md), [Tjeneste](tjeneste.md), [Behandlingsgrunnlag](behandlingsgrunnlag.md), [Personopplysning](personopplysning.md), [Begrep](begrep.md), [Valuta](valuta.md), [Person](person.md), [Kontaktperson](kontaktperson.md), [Virksomhet](virksomhet.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/personvern/:id |
| native | https://schema.fintlabs.no/personvern/:id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
identifier: true
alias: id
domain_of:
- Behandling
- Samtykke
- Tjeneste
- Behandlingsgrunnlag
- Personopplysning
- Begrep
- Valuta
- Person
- Kontaktperson
- Virksomhet
range: uriorcurie
required: true

```
</details>