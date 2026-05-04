

# Slot: navn 



URI: [https://schema.fintlabs.no/okonomi/:navn](https://schema.fintlabs.no/okonomi/:navn)
Alias: navn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Leverandorgruppe](Leverandorgruppe.md) | Gruppering av leverandørar (Leverandørgruppe) |  no  |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Fakturautsteder](Fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |  no  |
| [Vare](Vare.md) | Vare eller teneste som kan leverast og fakturerast |  no  |
| [Valuta](Valuta.md) | Valuta for transaksjonsbeløp |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Merverdiavgift](Merverdiavgift.md) | Kodeverk for merverdiavgifter |  no  |
| [Person](Person.md) | Fysiske private personar |  no  |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Fakturautsteder](Fakturautsteder.md), [Leverandorgruppe](Leverandorgruppe.md), [Vare](Vare.md), [Merverdiavgift](Merverdiavgift.md), [Valuta](Valuta.md), [Begrep](Begrep.md), [Person](Person.md), [Kontaktperson](Kontaktperson.md) |

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
- Valuta
- Begrep
- Person
- Kontaktperson
range: string

```
</details>