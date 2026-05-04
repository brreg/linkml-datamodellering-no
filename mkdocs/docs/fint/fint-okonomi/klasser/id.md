

# Slot: id 


_URI-identifikator (tilsvarar systemId/fakturanummer/transaksjonsId i FINT)._





URI: [https://schema.fintlabs.no/okonomi/:id](https://schema.fintlabs.no/okonomi/:id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Fakturagrunnlag](Fakturagrunnlag.md) | Grunnlag for fakturering |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Merverdiavgift](Merverdiavgift.md) | Kodeverk for merverdiavgifter |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Vare](Vare.md) | Vare eller teneste som kan leverast og fakturerast |  no  |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Postering](Postering.md) | Føring på ein konto i rekneskapet |  no  |
| [Leverandorgruppe](Leverandorgruppe.md) | Gruppering av leverandørar (Leverandørgruppe) |  no  |
| [Leverandor](Leverandor.md) | Person eller verksemd som leverer produkt eller tenester (Leverandør) |  no  |
| [Person](Person.md) | Fysiske private personar |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Faktura](Faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |
| [Fakturautsteder](Fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |  no  |
| [Transaksjon](Transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |
| [Valuta](Valuta.md) | Valuta for transaksjonsbeløp |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Faktura](Faktura.md), [Fakturagrunnlag](Fakturagrunnlag.md), [Fakturautsteder](Fakturautsteder.md), [Transaksjon](Transaksjon.md), [Postering](Postering.md), [Leverandor](Leverandor.md), [Leverandorgruppe](Leverandorgruppe.md), [Vare](Vare.md), [Merverdiavgift](Merverdiavgift.md), [Valuta](Valuta.md), [Begrep](Begrep.md), [Person](Person.md), [Kontaktperson](Kontaktperson.md), [Virksomhet](Virksomhet.md) |

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


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:id |
| native | https://schema.fintlabs.no/okonomi/:id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator (tilsvarar systemId/fakturanummer/transaksjonsId i
  FINT).
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
identifier: true
alias: id
domain_of:
- Faktura
- Fakturagrunnlag
- Fakturautsteder
- Transaksjon
- Postering
- Leverandor
- Leverandorgruppe
- Vare
- Merverdiavgift
- Valuta
- Begrep
- Person
- Kontaktperson
- Virksomhet
range: uriorcurie
required: true

```
</details>