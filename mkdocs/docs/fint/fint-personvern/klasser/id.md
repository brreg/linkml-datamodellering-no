

# Slot: id 


_URI-identifikator (tilsvarar systemId i FINT)._





URI: [https://schema.fintlabs.no/personvern/:id](https://schema.fintlabs.no/personvern/:id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjeneste](Tjeneste.md) | Teneste eller system som behandlar personopplysningar |  no  |
| [Behandling](Behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  no  |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Person](Person.md) | Fysiske private personar |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Valuta](Valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
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
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Behandling](Behandling.md), [Samtykke](Samtykke.md), [Tjeneste](Tjeneste.md), [Behandlingsgrunnlag](Behandlingsgrunnlag.md), [Personopplysning](Personopplysning.md), [Begrep](Begrep.md), [Valuta](Valuta.md), [Person](Person.md), [Kontaktperson](Kontaktperson.md), [Virksomhet](Virksomhet.md) |

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
description: URI-identifikator (tilsvarar systemId i FINT).
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