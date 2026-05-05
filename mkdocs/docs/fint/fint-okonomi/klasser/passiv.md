

# Slot: passiv 



URI: [https://schema.fintlabs.no/okonomi/:passiv](https://schema.fintlabs.no/okonomi/:passiv)
Alias: passiv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [OkonomiValuta](okonomivaluta.md) | Valuta for transaksjonsbeløp |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Merverdiavgift](merverdiavgift.md) | Kodeverk for merverdiavgifter |  no  |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Vare](vare.md), [Merverdiavgift](merverdiavgift.md), [OkonomiValuta](okonomivaluta.md), [Begrep](begrep.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:passiv |
| native | https://schema.fintlabs.no/okonomi/:passiv |




## LinkML Source

<details>
```yaml
name: passiv
alias: passiv
domain_of:
- Vare
- Merverdiavgift
- OkonomiValuta
- Begrep
range: string

```
</details>