

# Slot: navn 



URI: [https://schema.fintlabs.no/okonomi/:navn](https://schema.fintlabs.no/okonomi/:navn)
Alias: navn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Fakturautsteder](fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |  no  |
| [Leverandorgruppe](leverandorgruppe.md) | Gruppering av leverandørar (Leverandørgruppe) |  no  |
| [OkonomiValuta](okonomivaluta.md) | Valuta for transaksjonsbeløp |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Merverdiavgift](merverdiavgift.md) | Kodeverk for merverdiavgifter |  no  |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Fakturautsteder](fakturautsteder.md), [Leverandorgruppe](leverandorgruppe.md), [Vare](vare.md), [Merverdiavgift](merverdiavgift.md), [OkonomiValuta](okonomivaluta.md), [Begrep](begrep.md), [Valuta](valuta.md), [Person](person.md), [Kontaktperson](kontaktperson.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:navn |
| native | https://schema.fintlabs.no/okonomi/:navn |




## LinkML Source

<details>
```yaml
name: navn
alias: navn
domain_of:
- Fakturautsteder
- Leverandorgruppe
- Vare
- Merverdiavgift
- OkonomiValuta
- Begrep
- Valuta
- Person
- Kontaktperson
range: string

```
</details>