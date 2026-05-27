

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://schema.fintlabs.no/:id](https://schema.fintlabs.no/:id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Elev](elev.md) | Ein elev registrert i skulesystemet |  no  |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |  no  |
| [Fakturautsteder](fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |  no  |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |
| [Postering](postering.md) | Føring på ein konto i rekneskapet |  no  |
| [Leverandor](leverandor.md) | Person eller verksemd som leverer produkt eller tenester |  no  |
| [Leverandorgruppe](leverandorgruppe.md) | Gruppering av leverandørar |  no  |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |  no  |
| [Merverdiavgift](merverdiavgift.md) | Kodeverk for merverdiavgifter |  no  |
| [OkonomiValuta](okonomivaluta.md) | Valuta for transaksjonsbeløp |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Begrep](begrep.md), [Elev](elev.md), [Valuta](valuta.md), [Person](person.md), [Kontaktperson](kontaktperson.md), [Virksomhet](virksomhet.md), [Faktura](faktura.md), [Fakturagrunnlag](fakturagrunnlag.md), [Fakturautsteder](fakturautsteder.md), [Transaksjon](transaksjon.md), [Postering](postering.md), [Leverandor](leverandor.md), [Leverandorgruppe](leverandorgruppe.md), [Vare](vare.md), [Merverdiavgift](merverdiavgift.md), [OkonomiValuta](okonomivaluta.md) |

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


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/:id |
| native | https://schema.fintlabs.no/:id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/fint/fint-common
identifier: true
domain_of:
- Begrep
- Elev
- Valuta
- Person
- Kontaktperson
- Virksomhet
- Faktura
- Fakturagrunnlag
- Fakturautsteder
- Transaksjon
- Postering
- Leverandor
- Leverandorgruppe
- Vare
- Merverdiavgift
- OkonomiValuta
range: uriorcurie
required: true

```
</details>