

# Slot: gyldighetsperiode 



URI: [https://schema.fintlabs.no/okonomi/:gyldighetsperiode](https://schema.fintlabs.no/okonomi/:gyldighetsperiode)
Alias: gyldighetsperiode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Identifikator](Identifikator.md) | Unik identifikasjon til eit objekt |  no  |
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
| Domain Of | [Vare](Vare.md), [Merverdiavgift](Merverdiavgift.md), [Valuta](Valuta.md), [Begrep](Begrep.md), [Identifikator](Identifikator.md) |

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
- Valuta
- Begrep
- Identifikator
range: string

```
</details>