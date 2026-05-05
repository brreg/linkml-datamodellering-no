

# Slot: gyldighetsperiode 



URI: [https://schema.fintlabs.no/okonomi/:gyldighetsperiode](https://schema.fintlabs.no/okonomi/:gyldighetsperiode)
Alias: gyldighetsperiode

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
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Vare](vare.md), [Merverdiavgift](merverdiavgift.md), [OkonomiValuta](okonomivaluta.md), [Begrep](begrep.md), [Identifikator](identifikator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:gyldighetsperiode |
| native | https://schema.fintlabs.no/okonomi/:gyldighetsperiode |




## LinkML Source

<details>
```yaml
name: gyldighetsperiode
alias: gyldighetsperiode
domain_of:
- Vare
- Merverdiavgift
- OkonomiValuta
- Begrep
- Identifikator
range: string

```
</details>