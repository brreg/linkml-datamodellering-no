

# Slot: passiv 



URI: [https://schema.fintlabs.no/okonomi/:passiv](https://schema.fintlabs.no/okonomi/:passiv)
Alias: passiv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Vare](Vare.md) | Vare eller teneste som kan leverast og fakturerast |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Valuta](Valuta.md) | Valuta for transaksjonsbeløp |  no  |
| [Merverdiavgift](Merverdiavgift.md) | Kodeverk for merverdiavgifter |  no  |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Vare](Vare.md), [Merverdiavgift](Merverdiavgift.md), [Valuta](Valuta.md), [Begrep](Begrep.md) |

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
- Valuta
- Begrep
range: string

```
</details>